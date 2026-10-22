---
layout: post
mathjax: true
comments: true
title: "X-Planes: Bell X-5"
date: 2025-10-11 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 6
---

<!-- A302 -->
<script>console.log("A302");</script>

The [Bell X-5][ref_bell_x5] was the first aircraft to change the sweep of its wing in flight. That sentence states the achievement and conceals the difficulty, because sweeping a wing moves the place where its lift acts, and moving the lift puts the aircraft out of trim. This article is the sixth in the [X-Planes series][related_post_a297_xplanes_framing] and the fifth per-aircraft treatment, following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], and the [X-4][related_post_a301_northrop_x4]. The [National Advisory Committee for Aeronautics][ref_naca], abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, supplied the research programme. The Air Force approved the project on 4 February 1949 \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. [Bell][ref_bell_aircraft] supplied an aircraft built around a captured German one.

The X-5 worked, and it killed a pilot, and the two outcomes have different causes. The variable-sweep wing did what it was built to do. The histories attribute the spin characteristics that destroyed the second aircraft to the tail and the aerodynamic layout around that wing, although the NACA flight reports show that the highest sweep setting was where the aircraft departed into spins most readily.

## The Research Question

The keystone is whether wing sweep can be a variable rather than a choice.

Sweep is the central compromise of transonic design and it cannot be resolved in a fixed wing. Sweeping a wing back delays the onset of compressibility drag, because only the velocity component normal to the leading edge does the compressing. Resolving the free-stream velocity into components along and across the leading edge,

$$V_n = V \cos \Lambda, \qquad V_s = V \sin \Lambda, \qquad M_n = M \cos \Lambda$$

with $V_n$ the component that must be accelerated over the section and $V_s$ the spanwise component that must not. At Mach 0.9 and 60 degrees of sweep the section sees an effective Mach number of 0.45, which is subcritical by a wide margin, while the spanwise component reaches Mach 0.78 and drags boundary layer toward the tip.

That spanwise component is not merely a bookkeeping term. It drives an instability with no unswept analogue, in which the boundary layer profile acquires an inflection in the crossflow direction and sheds stationary vortices that trip the layer to turbulence well ahead of where a straight wing would transition. The mechanism was characterized experimentally by [Dagenhart et al 1989][research_dagenhart_1989] and [Mousseux et al 1989][research_mousseux_1989], mapped across the swept-wing boundary layer experiments of [Dagenhart et al 1990][research_dagenhart_1990] and [Dagenhart 1992][research_dagenhart_1992], resolved into its secondary instability by [Kohama et al 1991][research_kohama_1991], attacked with control by [Bridges 1994][research_bridges_1994], and is still being excited deliberately for study in [Carpenter et al 2010][research_carpenter_2010]. The subject has not closed. [Borodulin et al 2026][research_borodulin_2026] follow the nonlinear development of the disturbances, [Li et al 2026][research_li_2026] apply flow control to a swept multi-element wing where the crossflow interacts with the slat wake, and [Wang et al 2026][research_wang_2026_2] use active suction against the instability at supersonic speed. [Lu et al 2025][research_lu_2025] extend the stability analysis into hypersonic swept flow, while transition prediction on a forward-swept laminar wing occupies [Fehrs and Kaiser 2025][research_fehrs_2025]. **The X-5 could vary the parameter this literature treats as fixed**, a point taken up at the end of this article, since that capability was eventually used for that purpose on a different airframe. The simple sweep relation states the benefit,

$$M_{dd}(\Lambda) \approx \frac{M_{dd}(0)}{\cos^{k} \Lambda}, \qquad 0.5 \le k \le 1$$

with $k$ nearer one half than one in practice, since the flow does not obey the infinite-yawed-wing idealization at a real wing root or tip.

A pivoting wing collects a second benefit that a fixed swept wing does not, and because the benefit is purely geometric it is treated separately here. The physical section is fixed in the panel frame, so sweeping lengthens the chord measured in the flow direction while leaving the thickness alone,

$$c_{\text{stream}} = \frac{c_n}{\cos \Lambda} \quad \Longrightarrow \quad \left( \frac{t}{c} \right)_{\text{stream}} = \left( \frac{t}{c} \right)_n \cos \Lambda$$

so that a wing quoted at 11 percent thick streamwise at the low sweep setting presents

$$\left( \frac{t}{c} \right)_{\text{stream}} (60^\circ) = 0.11 \times \frac{\cos 60^\circ}{\cos 20^\circ} = 0.059$$

or 5.9 percent, at the high setting. **Sweeping the wing makes the aeroplane thinner as well as more swept**, and both act on the same drag-rise Mach number. Against that benefit stands a penalty on everything slow. Sweep reduces the lift-curve slope, reduces the maximum lift coefficient, promotes spanwise flow toward the tip and therefore tip stall, and it does all of this at the flight condition where an aircraft needs lift most. The [swept wing][ref_swept_wing] is not a free improvement but a trade, and a fixed wing must buy one point on the trade and live at it.

The idea of refusing to choose is old and obvious. Set the sweep low for takeoff, climb, and landing, and set it high for the dash. The objection, equally obvious once stated, is geometric rather than aerodynamic. A wing that rotates about a pivot carries its lift with it. Let the panel pivot about a point at spanwise station $y_p$, and let the panel aerodynamic centre lie a distance $s_{ac}$ from that pivot measured along the panel. The streamwise position of that aerodynamic centre is then

$$x_{ac}(\Lambda) = x_p + s_{ac} \sin \Lambda$$

so that changing sweep from $\Lambda_1$ to $\Lambda_2$ translates the aerodynamic centre aft by

$$\Delta x_{ac} = s_{ac} \left( \sin \Lambda_2 - \sin \Lambda_1 \right)$$

The problem fits in one line. It contains no aerodynamics at all beyond the location of the aerodynamic centre on the panel, and it shows that the trim consequence of variable sweep is set by where the pivot is put. That consequence was the binding unknown the X-5 was built to address. Whether sweep helps was not in doubt, since [DeYoung 1947][research_deyoung_1947] had already supplied the span loading of wings of arbitrary sweep, aspect ratio, and taper, and the swept-wing fleet was flying. What was in doubt was whether an aircraft could absorb the consequence.

The NACA had been assembling the surrounding evidence for years. High-lift and stall-control devices on a 52 degree sweptback wing appear in [Foster and Fitzpatrick 1948][research_foster_1948], tip treatments in [Spearman and Becht 1948][research_spearman_1948], and the transonic design problem was gathered in the conference proceedings of [NACA Conference on Aerodynamic 1949][research_naca_1949]. The question was live and the answer was mechanical.

## Programme Origin

The aircraft begins with a captured one.

The [Messerschmitt P.1101][ref_p1101] was taken by American troops in April 1945 from the experimental facility at Oberammergau and shipped first to Wright Field in Ohio, the centre of the Army Air Forces exploitation effort known as [Operation Lusty][ref_operation_lusty], and then to the Bell Aircraft factory at Buffalo. It arrived incomplete and damaged. Its wing sweep was adjustable on the ground, to 30, 40, and 45 degrees in one account and to three angles between 35 and 45 degrees in another \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\], a testing convenience with no operational role, and the aircraft was never intended to change sweep in the air.

Bell proposed in July 1948 to make the adjustment continuous and airborne \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. Two aircraft were built, serials 50-1838 and 50-1839. The first was completed on 15 February 1951, and the two made their first flights on 20 June and 10 December 1951 \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\].

The configuration is small. A single [Allison J35-A-17A][ref_j35] turbojet of 4900 pounds thrust sits in the fuselage, giving

$$T = 4900 \times 4.4482 = 2.18 \times 10^{4} \ \text{newtons}, \qquad \frac{T}{W} = \frac{2.18 \times 10^{4}}{4479 \times 9.80665} = 0.50$$

against a gross weight of 9875 pounds, or 4479 kilograms. The wing area is 175 square feet, or 16.26 square metres, and the wing sweeps to three detented positions at 20, 40, and 60 degrees. The wing section is a [NACA 64A011][ref_naca_airfoil] at the root thinning to a 64A08.28 at the tip. Span at the low setting is 33 feet 6 inches, or 10.21 metres, and at the high setting 20 feet 9 inches, or 6.32 metres \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\].

The mass fractions follow from the empty weight of 6350 pounds \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\],

$$\frac{m_{\text{empty}}}{m_{\text{gross}}} = \frac{2880}{4479} = 0.643, \qquad \frac{m_{\text{fuel}} + m_{\text{payload}}}{m_{\text{gross}}} = 0.357$$

a heavy empty fraction for a small jet, and the place where the pivot, its carry-through, and the translation mechanism are hiding. The wing loading follows,

$$\frac{W}{S} = \frac{4479 \times 9.80665}{16.26} = 2702 \ \text{newtons per square metre}$$

which is unremarkable and deliberately so. The aircraft was not built to go fast. It reached about Mach 0.9 and 40,000 feet \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\], which is enough to make the sweep question meaningful and not enough to add a second question on top of it. That restraint is the same judgement the [X-4][related_post_a301_northrop_x4] shows and the [X-3][related_post_a300_douglas_x3] does not.

## Sizing From First Principles

The keystone relationship is the aerodynamic centre travel, and the X-5's published dimensions are enough to compute it.

### Recovering the Pivot From the Spans

The span of a pivoting wing is a function of sweep. If the pivot sits at spanwise station $y_p$ and the movable panel has length $L$ measured along its own axis, then the projected span at sweep angle $\Lambda$ is

$$b(\Lambda) = 2 \left( y_p + L \cos \Lambda \right)$$

Two published spans at two known sweep angles determine both unknowns. Writing the pair,

$$\frac{b(\Lambda_1)}{2} = y_p + L \cos \Lambda_1, \qquad \frac{b(\Lambda_2)}{2} = y_p + L \cos \Lambda_2$$

and subtracting gives the panel length directly,

$$L = \frac{b(\Lambda_1) - b(\Lambda_2)}{2 \left( \cos \Lambda_1 - \cos \Lambda_2 \right)}$$

Substituting the X-5 figures, a span of 10.211 metres at 20 degrees and 6.325 metres at 60 degrees,

$$L = \frac{10.211 - 6.325}{2 \left( 0.9397 - 0.5000 \right)} = \frac{3.886}{0.8794} = 4.42 \ \text{metres}$$

and back-substituting recovers the pivot station,

$$y_p = \frac{b(\Lambda_1)}{2} - L \cos \Lambda_1 = 5.106 - 4.42 \times 0.9397 = 0.953 \ \text{metres}$$

The pivot therefore sits 0.953 metres from the centreline, which is

$$\frac{y_p}{b(20^\circ)/2} = \frac{0.953}{5.106} = 0.187$$

or **18.7 percent of the semi-span**. An inboard pivot of this kind, close against the fuselage, is the design decision that determines everything that follows. The number is not quoted from a source. It is recovered from two spans and a cosine, and it can be checked by anyone with the same two spans.

### What the Inboard Pivot Costs

The aerodynamic centre of a tapered panel lies near the spanwise station of its mean aerodynamic chord, which for a straight-tapered panel of taper ratio $\lambda$ is

$$\frac{y_{\text{mac}}}{L} = \frac{1}{3} \, \frac{1 + 2\lambda}{1 + \lambda}$$

returning 0.41 at a taper ratio of 0.3 and 0.44 at 0.5. Taper ratio was not a free parameter to the designers either, since it governs the rolling derivatives directly, as [Brewer and Fisher 1951][research_brewer_1951] measured across swept and unswept planforms. This article uses forty percent, which is slightly inboard of that range and therefore slightly conservative, so

$$s_{ac} \approx 0.40 \, L = 0.40 \times 4.42 = 1.77 \ \text{metres}$$

and the travel between the extreme sweep settings follows from the relation derived above,

$$\Delta x_{ac} = 1.77 \times \left( \sin 60^\circ - \sin 20^\circ \right) = 1.77 \times \left( 0.8660 - 0.3420 \right) = 0.93 \ \text{metres}$$

The estimate needs a sensitivity statement, because $s_{ac}$ is the only assumed quantity in the chain. The travel is linear in it,

$$\frac{\partial \left( \Delta x_{ac} \right)}{\Delta x_{ac}} = \frac{\partial s_{ac}}{s_{ac}}$$

so the seven percent spread in the taper-ratio relation above propagates to $0.93 \pm 0.07$ metres. Nothing in the argument turns on the difference. The figure acquires meaning only when it is referred to a chord. The mean chord follows from the area and the unswept span,

$$\bar{c} = \frac{S}{b(20^\circ)} = \frac{16.26}{10.211} = 1.59 \ \text{metres}$$

so the travel is

$$\frac{\Delta x_{ac}}{\bar{c}} = \frac{0.93}{1.59} = 0.58$$

**The aerodynamic centre moves 58 percent of the mean chord when the pilot sweeps the wing.** Aircraft are designed with static margins of five to fifteen percent of chord. The X-5's sweep lever commands a change four to eleven times the entire stability budget of a conventional aeroplane, and it commands it in the air, with a pilot aboard. Nothing else about the configuration matters as much as this number.

The consequence for the [static margin][ref_longitudinal_static_stability] is direct. Writing the margin in the usual way,

$$SM = \frac{x_{np} - x_{cg}}{\bar{c}}, \qquad C_{m\alpha} = -C_{L\alpha} \, SM$$

an untreated sweep change from 20 to 60 degrees drives

$$\Delta SM = +0.58$$

which takes an aircraft trimmed with a five percent margin at low sweep to a margin of 63 percent at high sweep. Such an aircraft is not dangerous in the sense of being unstable. It is useless, because the elevator cannot trim it and the stick forces to manoeuvre it would be enormous. The relation between margin and stick force per unit load factor,

$$\frac{F_s}{n} \propto MM, \qquad MM = SM - \frac{C_{mq}}{2 \mu}, \qquad \mu = \frac{2m}{\rho S \bar{c}}$$

makes the point quantitative, since a twelvefold increase in margin is a twelvefold increase in the force required to pull a given load factor.

The usable centre-of-gravity range collapses in the same motion. The aft limit is set by the minimum acceptable static margin and the forward limit by the control power available to trim at maximum lift,

$$x_{cg,\text{aft}} = x_{np} - SM_{\min} \bar{c}, \qquad x_{cg,\text{fwd}} = x_{ac} - \frac{\left| C_{m \delta_e} \right| \delta_{e,\max}}{C_{L,\max}} \bar{c}$$

and for a fixed wing the difference between them is a design constant. For a pivoting wing the neutral point in the first expression is itself a function of sweep, so the admissible range must be the intersection taken over the whole sweep schedule,

$$\Delta x_{cg,\text{usable}} = \bigcap_{\Lambda} \left[ x_{cg,\text{fwd}}(\Lambda), \ x_{cg,\text{aft}}(\Lambda) \right]$$

which for an uncompensated aerodynamic centre travel of 0.58 chords is empty. **There is no single centre-of-gravity position at which an uncompensated X-5 is flyable at both sweep extremes.** The empty intersection states formally why a mechanism was unavoidable given the pivot Bell had chosen.

### The Translating Fix and the Outboard Alternative

Bell's answer was to translate the wing forward as it swept aft \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. A [jackscrew][ref_jackscrew] assembly drove the pivot along short horizontal rails, with disc brakes locking the wing at each detent \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\]. The required translation to null the aerodynamic centre travel exactly is, by construction,

$$\Delta x_{\text{translate}} = -\Delta x_{ac} = -0.93 \ \text{metres}$$

or three feet of fore-and-aft motion of the complete wing, through a structure that must simultaneously carry the wing bending moment. The mechanism moved the wing about 27 inches, or 0.69 metres, forward between the 20 and 60 degree settings \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\], against the 0.93 metres estimated here, so the compensation was partial, by this estimate about three quarters. The flight programme had to measure the residual, which explains why [Finch and Walker 1953][research_finch_1953_2] reports the *boundaries* of static longitudinal stability instead of a single value.

There is a cleaner way to state what Bell got wrong, and the subsequent history of variable sweep is contained in it. Suppose the pivot is moved outboard, so that a fixed inboard glove carries a fraction $f$ of the wing lift and does not move at all. The wing's aerodynamic centre is then an average weighted by lift share,

$$x_{ac,\text{wing}} = f \, x_{\text{glove}} + \left( 1 - f \right) \left( x_p + s_{ac} \sin \Lambda \right)$$

and its travel with sweep is

$$\Delta x_{ac,\text{wing}} = \left( 1 - f \right) s_{ac} \left( \sin \Lambda_2 - \sin \Lambda_1 \right)$$

The design variable is the pivot station, and the travel to be minimized is a function of it. Writing the movable panel length as what remains of the semi-span outboard of the pivot,

$$L(y_p) = \frac{b_0}{2} - y_p, \qquad s_{ac}(y_p) = \beta \left( \frac{b_0}{2} - y_p \right)$$

with $\beta$ near 0.4, and taking the glove lift fraction to grow with pivot station roughly as its share of the semi-span,

$$f(y_p) \approx \frac{y_p}{b_0 / 2}$$

the travel becomes

$$\Delta x_{ac}(y_p) = \beta \left( 1 - \frac{y_p}{b_0/2} \right) \left( \frac{b_0}{2} - y_p \right) \left( \sin \Lambda_2 - \sin \Lambda_1 \right)$$

which is quadratic in the pivot station and falls away from the centreline much faster than linearly. Two things shrink at once. The factor $(1-f)$ reduces the travel in proportion to the lift the fixed glove carries, and moving the pivot outboard shortens the movable panel and therefore reduces $s_{ac}$ as well. **The two effects multiply.** A glove carrying half the lift with a panel two-thirds the length reduces the travel to one third of its inboard-pivot value,

$$\frac{\Delta x_{ac}(\text{outboard})}{\Delta x_{ac}(\text{inboard})} = \left( 1 - f \right) \frac{s_{ac}'}{s_{ac}} = 0.5 \times 0.67 = 0.33$$

taking the X-5's 0.58 chords of travel down to 0.19. A static margin change of that size is large but no longer impossible, and the gap between the two values separates a mechanism from a design. The outboard pivot was conceived by NACA engineers at Langley in the mid-1950s, as [Hallion 1984][research_hallion_1984] records, and the finding is the subject of [Henderson and Ray 1964][research_henderson_1964], which varies pivot location explicitly and reports what it does to the longitudinal characteristics.

### Everything Else That Sweep Changes

The aerodynamic centre is the binding problem but it is not the only one. Sweeping the X-5's wing also shortens the span, and since the reference area is fixed, the aspect ratio collapses,

$$A(\Lambda) = \frac{b(\Lambda)^2}{S} = \frac{4 \left( y_p + L \cos \Lambda \right)^2}{S}$$

Evaluating at the three detents,

$$A(20^\circ) = 6.41, \qquad A(40^\circ) = 4.63, \qquad A(60^\circ) = 2.46$$

so the aircraft's aspect ratio falls by a factor of 2.6 across the sweep range. The lift-curve slope responds to both changes together, since the standard estimate depends on aspect ratio and sweep jointly,

$$C_{L\alpha} = \frac{2 \pi A}{2 + \sqrt{ \dfrac{A^2 \beta_s^2}{\kappa^2} \left( 1 + \dfrac{\tan^2 \Lambda_{c/2}}{\beta_s^2} \right) + 4 }}, \qquad \beta_s = \sqrt{1 - M^2}$$

Taking the quoted sweep angles as half-chord sweep, an approximation stated as such, and evaluating at low Mach number,

$$C_{L\alpha}(20^\circ) = 4.42, \qquad C_{L\alpha}(40^\circ) = 3.48, \qquad C_{L\alpha}(60^\circ) = 2.11 \ \text{per radian}$$

giving a ratio across the range of

$$\frac{C_{L\alpha}(20^\circ)}{C_{L\alpha}(60^\circ)} = \frac{4.42}{2.11} = 2.09$$

**The pilot can halve the aircraft's lift-curve slope with a lever.** Every derivative that contains $C_{L\alpha}$ moves with it, which is to say almost every derivative the aircraft has.

The benefit appears at the slow end. Maximum lift coefficient falls roughly with the cosine of sweep, so

$$C_{L,\max}(\Lambda) \approx C_{L,\max}(0) \cos \Lambda$$

and the stall speed follows,

$$V_{\text{stall}} = \sqrt{\frac{2 W}{\rho S C_{L,\max}}}$$

The increments a flap supplies were predictable by method rather than by test alone, and [A Method for Predicting][research_lowry_1957] give one, by the same Polhamus who would shortly lead the variable-sweep work discussed below. Evaluating with a maximum lift coefficient of 1.20 at the low sweep setting and scaling by cosine,

$$V_{\text{stall}}(20^\circ) = 60.6 \ \text{metres per second}, \qquad V_{\text{stall}}(60^\circ) = 83.1 \ \text{metres per second}$$

a rise of 37 percent. The drag-divergence side of the trade can be evaluated on the same footing using the Korn relation, which carries sweep, thickness, and lift coefficient together,

$$M_{dd} = \frac{\kappa_A}{\cos \Lambda} - \frac{\left( t/c \right)_{\text{stream}}}{\cos^2 \Lambda} - \frac{C_L}{10 \cos^3 \Lambda}$$

with $\kappa_A$ near 0.87 for a conventional section. The underlying comparison had been made by experiment, not by correlation. [Ackeret et al 1951][research_ackeret_1951] report an investigation of wings with and without sweepback at high subsonic speed, and the argument depends on that controlled experiment. Twist and camber interact with the same trade, as [Spreemann and Alford 1951][research_spreemann_1951] and [Mugler 1959][research_mugler_1959] show, and the body interference a real installation adds appears in [Martina 1956][research_martina_1956]. Evaluating at a lift coefficient of 0.3 with the streamwise thickness ratios derived above,

$$M_{dd}(20^\circ) = 0.765, \qquad M_{dd}(40^\circ) = 0.916, \qquad M_{dd}(60^\circ) = 1.27$$

The correlation compresses a decade of transonic drag work into three terms, and because the coefficients are empirical, the underlying measurements are named here. Wing-body drag at transonic speed was characterized by [Cheatham and Kurbjun 1948][research_cheatham_1948] and systematically by [Whitcomb 1956][research_whitcomb_1956], whose zero-lift drag study of wing-body combinations is the work the area rule came out of, with the moment-of-area refinements in [Dickey 1959][research_dickey_1959] and the transonic characteristics of a 52 degree sweptback configuration in [Igoe et al 1961][research_igoe_1961]. The last figure is beyond the relation's range of validity and is quoted only to show the sense of the trend. The first two are the interesting ones. **The X-5 reached about Mach 0.9, which is above the drag-rise Mach number of its unswept setting and at the drag-rise Mach number of its middle one.** The aircraft could not have reached its top speed at low sweep. Sweeping was not a refinement of the performance. It was the performance.

Stated the other way at the slow end, where the designer's interest lies, unsweeping the wing for the approach reduces the landing speed by more than a quarter. The commercial argument for variable sweep consists of that reduction, which matters because landing speed drives runway length, tyre and brake energy, and the survivability of an approach flown badly. The energy a brake must absorb scales as the square of the touchdown speed,

$$E_{\text{brake}} \approx \frac{1}{2} m V_{\text{td}}^2$$

so a 27 percent reduction in speed is a 47 percent reduction in the energy the aircraft arrives with.

The bill for all of this arrives in induced drag, which depends on the span and therefore on the sweep,

$$C_{D,i} = \frac{C_L^2}{\pi A e} = \frac{C_L^2 S}{\pi b^2 e}$$

Evaluating at a lift coefficient of 0.3 and a span efficiency of 0.85,

$$C_{D,i}(20^\circ) = 0.0053, \qquad C_{D,i}(60^\circ) = 0.0137$$

a factor of 2.61. That number will appear again in the section on the spin. **The induced drag penalty and the growth of the spin inertia parameter are numerically identical, because both quantities carry the span squared in a denominator and the sweep lever is a span lever.** The drag penalty is a real performance cost. The spin parameter grows by the same factor, and the NACA's spin correlation reads that growth as no handicap to recovery, so the shared factor marks one geometric cause and does not make the spin a cost of the same size.

### Sweep Is a Trim Problem, Not a Dynamics Problem

One number, the rate, decides how the pilot experiences all of this. The X-5 moved from full extension to full sweep in less than thirty seconds \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\], and in about twenty seconds by the NASA account \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. Taking the slower figure first,

$$\dot{\Lambda} \approx \frac{40^\circ}{30 \ \text{s}} = 1.33 \ \text{degrees per second}$$

and the aerodynamic centre therefore drifts at

$$\dot{x}_{ac} = \frac{0.93 \ \text{m}}{30 \ \text{s}} = 3.1 \ \text{centimetres per second}$$

Compare that with the timescale of the aircraft's longitudinal response. The short period frequency and damping are

$$\omega_{sp} \approx \sqrt{-M_\alpha}, \qquad M_\alpha = \frac{q S \bar{c} \, C_{m\alpha}}{I_y}, \qquad \zeta_{sp} = -\frac{M_q + M_{\dot\alpha} + Z_\alpha / V}{2 \omega_{sp}}$$

and for an aircraft of this class at its test condition the short period may be taken as near 3 radians per second, giving a period near two seconds. The ratio of timescales is therefore

$$\frac{\tau_{\text{sweep}}}{T_{sp}} \approx \frac{30}{2} = 15$$

The comparison can be sharpened from an observation into a criterion. The aircraft experiences the geometry change as quasi-static when the stability perturbation the sweep produces in one short-period cycle is small against the margin itself,

$$\epsilon_{qs} = \frac{1}{SM} \frac{\partial \left( x_{ac} / \bar{c} \right)}{\partial \Lambda} \dot{\Lambda} \, \frac{2\pi}{\omega_{sp}} \ll 1$$

and with the X-5's numbers, a margin of 0.05, a sensitivity of 0.58 chords over 40 degrees, a rate of 1.33 degrees per second, and a period of 2.1 seconds,

$$\epsilon_{qs} = \frac{1}{0.05} \times 0.0145 \times 1.33 \times 2.1 = 0.81$$

which is below unity but not comfortably. At the twenty-second figure the rate is 2.0 degrees per second, the ratio of timescales is 10, and $\epsilon_{qs}$ rises to 1.22, so the criterion is met only marginally if at all. Either way the pilot could not ignore the change and was retrimming continuously. **The sweep transient is ten to fifteen times slower than the mode it perturbs.** That inequality is why the X-5 was flyable at all. The aircraft never experiences a step change in its stability. It experiences a slow drift that the pilot trims out continuously, in the same way he trims out a fuel burn, and the formal statement is that the sweep change is quasi-static with respect to the rigid-body dynamics. Had the mechanism been ten times faster the aircraft would have needed a control system that could not have been built in 1951.

The result is stated generally here because it alone among the parts of the X-5's answer transferred without modification. Variable geometry is tractable when the geometry changes slowly compared with the vehicle's modes, and when it does not, the control problem is of a different and harder kind. The modern treatments cited below are largely about the harder case.

## Dependent Systems

### The Pivot and What Passes Through It

Every pound of lift on the movable panel is carried to the fuselage through one bearing.

The panel root bending moment at load factor $n$ is the panel lift acting at its centre of pressure,

$$M_{\text{pivot}} = n \, L_{\text{panel}} \, s_{cp}$$

with $L_{\text{panel}}$ the lift carried by one movable panel and $s_{cp}$ the spanwise distance from pivot to panel centre of pressure. Taking the panels to carry about sixty percent of the total lift between them, one panel at a design load factor of seven carries

$$L_{\text{panel}} = 0.5 \times 0.60 \times 43{,}926 \times 7 = 9.22 \times 10^{4} \ \text{newtons}$$

and with the centre of pressure at the same forty percent of panel length used above,

$$M_{\text{pivot}} = 9.22 \times 10^{4} \times 1.77 = 1.63 \times 10^{5} \ \text{newton metres}$$

That moment must pass through a joint that also has to rotate under load. A fixed wing carries its root moment through a continuous spar carry-through, a beam in bending and the most efficient structure available. A pivoting wing must replace that beam with a pin, and the pin must be sized for the moment while the surrounding structure must be sized for the reaction couple the pin imposes. The reaction on the bearing separated by a structural depth $h$ is

$$F_{\text{bearing}} = \frac{M_{\text{pivot}}}{h}$$

so a shallow fuselage multiplies the load. With a structural depth of half a metre the reaction is

$$F_{\text{bearing}} = \frac{1.63 \times 10^{5}}{0.5} = 3.26 \times 10^{5} \ \text{newtons}$$

which a lug of 0.10 metre pin diameter and 0.05 metre thickness carries at a bearing stress of

$$\sigma_{br} = \frac{F}{d \, t} = \frac{3.26 \times 10^{5}}{0.10 \times 0.05} = 65 \ \text{megapascals}$$

with the pin itself in double shear at

$$\tau = \frac{F}{2 \left( \pi d^2 / 4 \right)} = 21 \ \text{megapascals}$$

The point to take is that neither figure is alarming for steel. The design of a conventional wing root and its carry-through is a well-worked subject, treated at length in [Sager et al 1993][research_sager_1993] and [Downs et al 1993][research_downs_1993], and what those treatments assume throughout is a continuous load path. The pivot replaces it with a discontinuity. The problem has not gone away for anyone who wants variable geometry, and [Hu et al 2026][research_hu_2026] design support structures for variable-sweep and variable-span wings with the bearing capacity the joint demands, and Bell solved the same problem with a jackscrew and rails. A related modern case puts the load path in plain view, since [Ellis et al 2025][research_ellis_2025] use an actively hinged wingtip to *reduce* the wing root bending moment, turning the articulation from a structural liability into a structural instrument. **The pivot is not hard because the stresses are high. It is hard because the joint must carry them while rotating, repeatedly, without developing the free play that would turn a stiffness into a mechanism.** A bearing clearance $\delta$ at radius $s_{ac}$ registers as a sweep error,

$$\Delta \Lambda_{\text{slop}} \approx \frac{\delta}{s_{ac}}$$

so a millimetre of wear is 0.03 degrees of asymmetry between the panels, and asymmetric sweep is a rolling moment the pilot did not command. The bearing must also be stiff, because a joint that deflects under load changes the effective sweep and therefore the aerodynamics, an aeroelastic coupling treated in [Goetz and Stonesifer 1961][research_goetz_1961] and [Gurley and Ruhlin 1962][research_gurley_1962] and pursued in the component studies of [Abel et al 1966][research_abel_1966].

The mass penalty follows from the same argument, and it explains why variable sweep is now rare. Writing the structural mass fraction as a baseline plus a variable-geometry increment,

$$\frac{m_{\text{struct}}}{m_{\text{gross}}} = \left( \frac{m_{\text{struct}}}{m_{\text{gross}}} \right)_{\text{fixed}} + \Delta_{\text{VG}}$$

the increment is taken here as a few percent of gross mass, which for an aircraft of the X-5's size is of order

$$\Delta m = 0.03 \times 4479 = 134 \ \text{kilograms}$$

and it buys nothing at any single flight condition. It buys the ability to be at two flight conditions well, and whether that is worth carrying depends on how much of the mission is spent at each. The break-even condition can be written down. Let $\phi_i$ be the fraction of the mission flown at condition $i$ and $\Delta \left( L/D \right)_i$ the improvement variable sweep gives there. The configuration pays for itself when the weighted aerodynamic gain exceeds the mass penalty expressed as an equivalent range loss,

$$\sum_i \phi_i \frac{\Delta \left( L/D \right)_i}{\left( L/D \right)_i} > \frac{\Delta m_{\text{VG}}}{m_{\text{fuel}}}$$

which follows from the Breguet form,

$$R = \frac{V}{c_t} \frac{L}{D} \ln \frac{m_i}{m_f}$$

and the question it poses belongs to mission analysis, not aerodynamics. **A vehicle that spends most of its life at one condition can never justify a mechanism that helps at two.** That inequality, and not any aerodynamic discovery, eventually retired the variable-sweep fighter. The [aeroelastic][ref_aeroelasticity] and flutter consequences are a separate charge on the same account, treated for swept wings generally by [Housner and Stein 1974][research_housner_1974].

### Trim, and the Longitudinal Consequences of Moving the Wing

The translating mechanism converts a stability problem into a trim problem, imperfectly.

With partial compensation the residual aerodynamic centre travel is some fraction $\eta_c$ of the uncompensated value,

$$\Delta x_{ac,\text{residual}} = \left( 1 - \eta_c \right) \Delta x_{ac}$$

and the trim moment the tail must absorb at lift coefficient $C_L$ is

$$\Delta C_m = C_L \frac{\Delta x_{ac,\text{residual}}}{\bar{c}}$$

which the elevator must supply through its control power,

$$\delta_e = \frac{\Delta C_m}{\left| C_{m \delta_e} \right|}$$

Even a mechanism achieving eighty percent compensation leaves 0.19 metres, or 12 percent of chord, of residual travel, which at a cruise lift coefficient of 0.3 demands a trim moment increment of 0.035 and several degrees of elevator. That moment is carried by a tail load, and the load can be quantified,

$$L_t = \frac{\Delta C_m \, q \, S \, \bar{c}}{l_t}$$

At Mach 0.9 and 40,000 feet the dynamic pressure is 10,633 pascals, so with a tail arm of 4.5 metres

$$L_t = \frac{0.035 \times 10{,}633 \times 16.26 \times 1.592}{4.5} = 2.14 \times 10^{3} \ \text{newtons}$$

or **4.9 percent of the aircraft's weight carried by the tail purely to trim out what the mechanism failed to cancel**. That load also carries a drag penalty,

$$\Delta C_{D,\text{trim}} = \frac{C_{L_t}^2}{\pi A_t e_t} \frac{S_t}{S}$$

The horizontal tail therefore works continuously against the wing position. It is no accident that a large fraction of the X-5's primary literature is tail load measurement. [Rogers and Dunn 1952][research_rogers_1952] give preliminary horizontal tail loads and [Reed 1955][research_reed_1955] the measurements at 58.7 degrees of sweep, with the corresponding wing loads in [Banner et al 1955][research_banner_1955]. The same measurement problem on a fixed-wing research aircraft appears in [Stephenson 1956][research_stephenson_1956] for the [X-3][related_post_a300_douglas_x3], which makes a useful comparison because the X-3's tail loads are a function of one variable and the X-5's are a function of two.

The neutral point is the sum of wing and tail contributions,

$$\frac{x_{np}}{\bar{c}} = \frac{x_{ac,\text{wing}}}{\bar{c}} + V_H \frac{C_{L\alpha_t}}{C_{L\alpha_w}} \left( 1 - \frac{d\varepsilon}{d\alpha} \right), \qquad V_H = \frac{S_t l_t}{S \bar{c}}$$

and every term on the right is a function of sweep. The wing aerodynamic centre moves, as derived. The wing lift-curve slope in the denominator falls by a factor of two, which *increases* the tail's relative contribution. The downwash derivative depends on wing aspect ratio,

$$\frac{d\varepsilon}{d\alpha} \approx \frac{2 C_{L\alpha_w}}{\pi A}$$

and at the three sweep settings this returns 0.44, 0.48, and 0.55, so the tail loses incidence as the wing sweeps even as it gains relative authority. These effects do not cancel and there is no reason they should. The static longitudinal stability the aircraft actually exhibited across the range is the subject of [Finch and Walker 1953][research_finch_1953_2], with the broader stability and control picture in [Finch and Briggs 1953][research_finch_1953] and the dynamic behaviour at high sweep in [Videan 1955][research_videan_1955].

Ground testing had prepared the ground. The quarter-scale model work of [Kemp and Becht 1950][research_kemp_1950] covers lateral and directional characteristics, [Becht 1950][research_becht_1950] the landing configuration, and [Kemp and Few 1951][research_kemp_1951] the pressure distribution, the measurement from which an aerodynamic centre is obtained rather than assumed.

### Sweep as a Scheduling Variable

When the derivatives are functions of a commanded parameter, the aircraft has a family of dynamics in place of one set.

Write the linearized longitudinal system in the usual state-space form,

$$\dot{\mathbf{x}} = \mathbf{A}(\Lambda) \, \mathbf{x} + \mathbf{B}(\Lambda) \, \mathbf{u}$$

in which the plant matrices depend on sweep because the derivatives do. The short period frequency scales with the square root of the stability derivative,

$$\omega_{sp}(\Lambda) \propto \sqrt{ C_{L\alpha}(\Lambda) \, SM(\Lambda) }$$

and since both factors move with sweep, and in opposite senses under partial compensation, the frequency does not sit at a point but traverses a range. Even granting the mechanism perfect compensation, so that the static margin is held at 0.05 throughout, the lift-curve slope alone moves the frequency by

$$\frac{\omega_{sp}(20^\circ)}{\omega_{sp}(60^\circ)} = \sqrt{\frac{C_{L\alpha}(20^\circ)}{C_{L\alpha}(60^\circ)}} = \sqrt{2.09} = 1.45$$

so the aircraft's natural frequency spans a factor of nearly one and a half across the sweep range with the trim problem entirely solved. A controller holding constant closed-loop behaviour across that range must vary its gains,

$$k(\Lambda) = k_0 \left( \frac{\omega_{sp}(\Lambda_0)}{\omega_{sp}(\Lambda)} \right)^2$$

which is gain scheduling written down, and which the X-5 implemented by carrying a pilot. The apparatus now exists in several forms. [Enciu et al 2025][research_enciu_2025] treat the delayed case, [Barbosa and Silvestre 2025][research_barbosa_2025] the flexible-airframe case by fuzzy output feedback, and [Gao et al 2025][research_gao_2025] the linear parameter-varying formulation, in which the configuration parameter enters the plant model explicitly and the controller is synthesized once for the whole family rather than interpolated between points. That formulation describes mathematically what a variable-sweep aircraft is. The X-5 handled this the way 1951 handled everything, by putting a human in the loop and letting him adapt. The formal apparatus for the problem, in which a controller is scheduled against a measured configuration parameter, did not exist yet and is now routine. It makes the modern variable-geometry vehicles cited below tractable.

The lateral set moves too. Directional stiffness and yaw damping come from the fin,

$$C_{n\beta} = V_V \, C_{L\alpha_v} \, \eta_v, \qquad V_V = \frac{S_v l_v}{S b}, \qquad C_{n r, \text{fin}} = -2 \, \eta_v \, C_{L\alpha_v} V_V \frac{l_v}{b}$$

and the vertical tail volume coefficient contains the span in its denominator. **Sweeping the wing shortens the span and therefore increases the vertical tail volume coefficient**, which sounds like good news and is, in isolation. The [Dutch roll][ref_dutch_roll] frequency and the roll mode follow,

$$\omega_{dr} \approx \sqrt{\frac{q S b \, C_{n\beta}}{I_z}}, \qquad \tau_r = -\frac{2 I_x V}{q S b^2 C_{lp}}$$

both of which contain the span explicitly and therefore both of which the sweep lever moves. The dihedral effect $C_{l\beta}$ grows with sweep, since a swept wing in sideslip presents a smaller effective sweep to the advancing panel, and the standard first-order statement is

$$C_{l\beta,\text{sweep}} \approx -C_L \frac{\tan \Lambda}{2}$$

so that the rolling moment due to sideslip nearly quintuples between 20 and 60 degrees at fixed lift coefficient. The measured basis for that relation is [Lampert 1951][research_lampert_1951] on rolling and yawing moments for sweptback wings in sideslip, with the wing height and dihedral contributions separated by [Gillis and Chapman 1956][research_gillis_1956] and the yawing moment due to rolling estimated semiempirically by [Campbell and Goodman 1949][research_campbell_1949]. Fuselage and tail interference on the same characteristics is [Bird et al 1951][research_bird_1951_2], and the complete swept model case is [Schulderfrei et al 1951][research_schulderfrei_1951] and [Savage and Edwards 1959][research_savage_1959]. Lateral control at the high sweep setting is a separate difficulty, treated for tip ailerons by [Moseley and Watson 1951][research_moseley_1951] and for jet control by [Vogler and Turner 1956][research_vogler_1956]. Strong dihedral effect with a fin of fixed area makes an aircraft prone to a lightly damped Dutch roll, and [Childs 1953][research_childs_1953] set out to measure the sideslip behaviour at high sweep. The lateral characteristics of variable-sweep configurations generally are treated in [Eckert and Maki 1973][research_eckert_1973], the rolling derivatives in [Gainer et al 1967][research_gainer_1967], and the dynamic derivatives across the transonic and supersonic range in [Kilgore 1971][research_kilgore_1971] and [Averett and Wright 1966][research_averett_1966].

### The Spin and the Inertia Parameter

The second aircraft was lost in a spin at 60 degrees of sweep \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. The geometry already established changes the NACA's spin correlating parameter sharply, and the NACA's correlation reads that change as no handicap to recovery.

A [spin][ref_spin] is an equilibrium, not a departure. The aircraft rotates about a vertical axis at a steady rate with one wing stalled more deeply than the other, and the equilibrium is set by a balance between aerodynamic and inertial moments. The inertial coupling terms in the Euler equations are the ones that matter,

$$I_x \dot{p} = \left( I_y - I_z \right) q r + L_{\text{aero}}$$

$$I_y \dot{q} = \left( I_z - I_x \right) r p + M_{\text{aero}}$$

$$I_z \dot{r} = \left( I_x - I_y \right) p q + N_{\text{aero}}$$

and in a developed spin the products $qr$, $rp$, and $pq$ are large. The NACA correlated spin and recovery behaviour against a non-dimensional grouping of the inertia differences \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\], the natural one being

$$I_{\text{param}} = \frac{I_x - I_y}{m \, b^2}$$

which is negative for an aircraft carrying its mass along the fuselage rather than along the span. The equilibrium the parameter governs is a balance in which the aerodynamic yawing moment must cancel the inertial one,

$$N_{\text{aero}} = -\left( I_x - I_y \right) p q$$

and recovery requires the controls to break that balance. With the rudder as the recovering control, the condition is that the available control moment exceed the inertial term,

$$\left| N_{\delta_r} \right| \delta_{r,\max} \, q S b > \left| I_x - I_y \right| p q$$

**Both sides of this inequality are dimensional moments, and neither depends on the wing span.** The rudder moment is set by the fin, the rudder and the tail arm, and the coefficient $N_{\delta_r}$ carries the span only because it is normalized against it. The inertial term is set by the mass distribution. Sweeping the wing shortens the span and leaves both moments nearly as they were, so the inequality gives no reason to expect recovery to worsen with sweep. The NACA's correlation, built on models of approximately one hundred military aeroplanes, found that the rudder loses effectiveness and the elevator gains it as mass moves out along the wings. A model loaded chiefly along the fuselage, with the parameter at $-100 \times 10^{-4}$ or more negative, needed the least tail damping for recovery by the rudder alone, a tail damping power factor of $250 \times 10^{-6}$ at relative densities of 15 or less, and the requirement rose very rapidly as the parameter approached zero, to about $1500 \times 10^{-6}$ at zero \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\]. The parameter decides which control recovers the aircraft as well as how readily, and a more negative value favours the rudder. This correlation is the accumulated product of two decades of work that begins before the tunnels. [Knight 1928][research_knight_1928] tested autorotation and the flat spin directly, [Scudder 1937][research_scudder_1937] measured the forces and moments on the parts of an airplane during actual spins rather than inferring them, and [Pitkin 1943][research_pitkin_1943] established that a leading-edge slot changes the spin and recovery behaviour, the first hint that configuration details govern the outcome.

**One document bears on the X-5 more directly than any other and it predates the aircraft.** [Stone and Klinar 1948][research_stone_1948] investigate the influence of very heavy fuselage mass loadings and long nose lengths upon oscillations in the spin, the loading regime that the parameter above describes and that a swept aircraft with its mass in the fuselage occupies. Their models, all with unswept wings, replaced the steady spin with violent rolling and yawing oscillations in that regime, and model results indicated that recovery from those motions could generally be obtained if the tail design was adequate. The regime was named, characterized, and in print three years before the X-5 flew. Whether the aircraft was assessed against it, the sources consulted do not say.

The moments of inertia on which any such assessment depends were measurable by 1950, and [Turner 1950][research_turner_1950] gives a simplified method for obtaining them on a complete airplane. The X-5's inertias were measured by that method, and the NACA flight reports give them, so the values used below are measured ones wherever the reports supply them. Free-spinning-tunnel work continued through the wartime and postwar fleet in [Berman 1947][research_berman_1947], [Snyder 1947][research_snyder_1947], [Scher 1947][research_scher_1947], [Berman 1949][research_berman_1949], [Klinar and Jones 1949][research_klinar_1949], [Klinar and Wilson 1950][research_klinar_1950], and [Lee 1952][research_lee_1952], and continuing through [Burk and Healy 1955][research_burk_1955], [Bowman 1956][research_bowman_1956], and [Bowman and Healy 1959][research_bowman_1959].

Now apply it to the X-5. The moments of inertia are properties of the mass distribution and change only slightly with sweep, since the wing is a small part of the total mass and it moves only a metre. The span is not slightly changed. It falls from 10.21 metres to 6.32 metres. Since the span enters the parameter squared,

$$\frac{I_{\text{param}}(60^\circ)}{I_{\text{param}}(20^\circ)} = \left( \frac{b(20^\circ)}{b(60^\circ)} \right)^2 = \left( \frac{10.21}{6.32} \right)^2 = 2.61$$

The NACA measured the inertias at 58.7 degrees of sweep with full fuel, 5,165 slug square feet in roll and 9,495 in pitch at a weight of 10,006 pounds and a span of 20.1 feet [Videan 1955][research_videan_1955], which give

$$I_{\text{param}}(58.7^\circ) = \frac{5165 - 9495}{(10006 / 32.174) \times 20.1^2} = -0.0345$$

At 20 degrees the pitch inertia was 9,450 slug square feet at 9,960 pounds and the span 31.9 feet, and the roll inertia was not reported [Finch and Briggs 1953][research_finch_1953]. Sweeping forward carries wing mass outboard and raises the roll inertia, so the parameter at 20 degrees can be no more negative than $-0.0136$, the value it takes with the roll inertia held at its swept value. With the NACA's spans the span-squared ratio is 2.52, against the 2.61 computed from the specification spans used here.

**Sweeping the wing back moves the aircraft about two and a half times deeper into the fuselage-loaded regime, and the NACA's correlation places that regime where the rudder works best.** At 58.7 degrees the parameter lies far beyond the $-100 \times 10^{-4}$ at which the least tail damping sufficed. At 20 degrees it lies near that boundary and crosses it if the roll inertia at that setting exceeds the swept value by more than about 1,100 slug square feet. By this correlation the swept setting is, if anything, the more favourable one for recovery by the rudder.

The correlation has a second variable, and it moves the other way. The relative density $\mu = m / \rho S b$ also carries the span, and with the NACA's areas and spans it rises by a factor of 1.45 between 20 and 58.7 degrees, from 24.4 to 35.4 at sea level and from 82 to 119 at 36,000 feet. The tail damping required for recovery rose with relative density, and the data behind the correlation were meagre above 20 and stopped near 35 \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\]. The X-5 at altitude lies well outside those data at either setting, so the correlation gives a direction for this term and cannot size it. **The span-squared growth of the inertia parameter therefore does not explain the loss.** It is a change of normalization that the NACA's correlation reads as favourable to the rudder, and the one term that worsens with sweep lies outside the range on which the correlation was built.

The time available is not the constraint. A spinning aircraft descends at roughly the speed at which its high-incidence normal force balances weight,

$$V_d \approx \sqrt{\frac{2W}{\rho S C_N}} = \sqrt{\frac{2 \times 43{,}926}{1.225 \times 16.26 \times 1.2}} = 60.6 \ \text{metres per second}$$

and loses altitude per turn of

$$\Delta h_{\text{turn}} = V_d \frac{2\pi}{\Omega} = 60.6 \times \frac{2\pi}{2.0} = 190 \ \text{metres}$$

so an entry at 12,000 metres offers something like sixty turns before ground impact. Altitude margin is now treated as an optimization variable rather than a comfort, and [Bagheri and Danesh 2025][research_bagheri_2025] design spin recovery to minimize the height given up, with [Salahudden 2026][research_salahudden_2026] examining altitude margin and aileron effects for flat-spin recovery. The control formulations have moved with it, through nonlinear model predictive control in [Salahudden 2025][research_salahudden_2025] and incremental nonlinear dynamic inversion in [Salahudden 2025][research_salahudden_2025_2]. Neural approaches to the wider high-incidence problem appear in [Yu and Yu 2026][research_yu_2026], and the sensing that any of it requires, since a departing aircraft must first know what it is doing, is addressed by [Huang et al 2026][research_huang_2026] using on-board flow sensing for forebody vortex-induced yaw. **An irrecoverable spin is not one that runs out of altitude. It is one in which no control input available breaks the equilibrium**, and the extra turns simply confirm it.

The aerodynamic side of the recovery problem is where the sources place the X-5's difficulty. Recovery requires the rudder to generate an anti-spin yawing moment, and at spin attitudes the fin sits in the wake of the horizontal tail. The NACA quantified this with the tail damping power factor, the product of a tail damping ratio and an unshielded rudder volume coefficient \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\],

$$\text{TDPF} = \text{TDR} \times \text{URVC}$$

in which the unshielded rudder volume coefficient counts only the rudder area outside the horizontal tail's wake shadow. The dependence of rudder effectiveness on horizontal tail position in spin attitudes is what [Stone and Burk 1947][research_stone_1947] measured, and the limiting case of a fighter model with no horizontal tail at all is [Gale and Pumphrey 1950][research_gale_1950]. [Hallion 1984][research_hallion_1984] calls the X-5 a flawed design and states that the flaw had nothing to do with the variable-sweep wing, attributing it to the aerodynamic layout and especially to the poor position of the tail and vertical fin. The NASA fact sheet likewise attributes the poor stall and spin characteristics to the aircraft's design and says that they were not due to the variable sweep \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. A comparable case exists in the record, since [Bowman and Healy 1960][research_bowman_1960] report a free-spinning-tunnel investigation of a twin-jet swept-wing fighter model, published seven years after the X-5 was lost. Whether the spin that killed the second aircraft was predicted is treated below.

Sweep enters the record through the departure. At low Mach number the pilot found the stall approach and recovery conventional at 20 and 40 degrees, while at 58 degrees a mild longitudinal instability appeared and stability was neutral above a normal-force coefficient of 0.7 [Finch and Briggs 1953][research_finch_1953]. At 59 degrees the reduction of longitudinal stability combined with directional instability had on occasion caused accidental spins following elevator pull-ups [Finch and Walker 1953][research_finch_1953_2], and at 58.7 degrees the aircraft diverged in sideslip at the lower Mach numbers to more than 25 degrees and into a spin, although it normally responded to the elevator as the pilot recovered [Finch and Walker 1956][research_finch_walker_1956]. On 21 October 1952 Walker entered a spin at 36,000 feet, at a sweep setting the fact sheet does not give, and needed 18,000 feet to recover \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. **The highest sweep setting is where the X-5 departed most readily, and the flight reports trace that to pitch-up and directional instability at that sweep.** The span-squared term has no place in that account.

The remedy of last resort, a spin-recovery rocket, was a subject of NACA investigation in [Burk and Healy 1955][research_burk_1955], and the existence of such a document shows how seriously the problem was taken.

The subject did not close with the X-5's generation. Spin-tunnel practice continued through the general aviation fleet in [Burk et al 1977][research_burk_1977] and into the supersonic fighters with [Scher and White 1977][research_scher_1977] on the F-5E and [Whipple and White 1984][research_whipple_1984] on the F-16XL. The configuration dependence that [Pitkin 1943][research_pitkin_1943] first noticed was pursued systematically by [Stough and Patton 1979][research_stough_1979] and, in flight rather than in a tunnel, by [Stough et al 1987][research_stough_1987], who varied tail configuration and measured what it did to stall, spin, and recovery. That thread reaches an unusual endpoint. [Stough et al 1991][research_stough_1991] show that venting the tail improves yaw damping at spinning conditions, and [Stough 1993][research_stough_1993] patents an apparatus for improving spin recovery, so that the problem the X-5 met ends in a device instead of a rule.

### Propulsion and Envelope

The single Allison J35 is the least interesting component, and an adequate one.

Thrust lapses with altitude roughly as ambient pressure, with a ram recovery term,

$$\frac{T(h, M)}{T_{SL}} \approx \frac{p(h)}{p_{SL}} \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

and the atmosphere is the standard troposphere model,

$$T(h) = T_0 - \lambda h, \qquad p(h) = p_0 \left( \frac{T(h)}{T_0} \right)^{g / \lambda R}, \qquad a = \sqrt{\gamma R T}$$

The level-flight maximum follows from the thrust and drag balance,

$$M_{\max}^2 = \frac{2 T}{\gamma \, p \, S \, C_D}$$

and specific excess power governs the climb,

$$P_s = \frac{V \left( T - D \right)}{W}, \qquad h_e = h + \frac{V^2}{2g}$$

The aircraft reached about Mach 0.9 at 40,000 feet \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\]. A clean transonic airframe decelerates poorly, and the devices for dealing with that were being characterized alongside, with dive-recovery flaps measured by [Heath and Ward 1959][research_heath_1959], speed-brake position effects on longitudinal characteristics reported by [Taylor 1959][research_taylor_1959], and the load redistribution that body-mounted brakes cause quantified by [West 1960][research_west_1960]. The interesting propulsion observation is not about the engine but about the wing, since the drag polar is a function of sweep,

$$C_D(\Lambda) = C_{D0}(\Lambda) + \frac{C_L^2}{\pi A(\Lambda) e(\Lambda)}$$

with the aspect ratio in the induced term falling by a factor of 2.6 as the wing sweeps. **Sweeping back to reduce wave drag increases induced drag at the same time**, and the crossover between the two determines whether a given sweep setting is the right one at a given speed and altitude. The optimum sweep schedule is the locus where the derivative of total drag with respect to sweep vanishes,

$$\frac{\partial C_D}{\partial \Lambda} = 0$$

Carrying out the differentiation on the two-term polar makes the balance explicit, since the wave-drag term falls with sweep and the induced term rises,

$$\frac{\partial C_D}{\partial \Lambda} = \frac{\partial C_{D0}}{\partial \Lambda} + \frac{C_L^2}{\pi e} \frac{\partial}{\partial \Lambda} \left( \frac{1}{A(\Lambda)} \right) = 0$$

which is a curve in the Mach and lift coefficient plane rather than a set of three detents. The X-5's three positions are a coarse sampling of a continuous optimum, and the lift and drag actually achieved at the high setting are reported in [Bellman 1953][research_bellman_1953], with the fleet-wide comparison in [Bellman 1959][research_bellman_1959].

### Instrumentation

The programme measured loads and derivatives as functions of two independent variables rather than one, and that changes the size of the experiment.

A conventional flight test programme maps a derivative against Mach number and altitude. The X-5 must map every derivative against Mach number, altitude, and sweep, so the test matrix acquires a dimension. If a fixed-wing programme requires $N$ conditions to characterize a derivative to a given accuracy, then the variable-sweep programme requires

$$N_{\text{total}} = N \times n_\Lambda$$

conditions, with $n_\Lambda$ the number of sweep settings, which for the X-5 is three at minimum and more if intermediate positions are of interest. Hence the first aircraft alone flew about 150 times to answer one question.

The measurements are strain-gauge based \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. Wing and tail loads are obtained by calibrating a set of bridges against known applied loads and then inverting the calibration in flight,

$$\mathbf{L} = \mathbf{C}^{-1} \boldsymbol{\varepsilon}$$

with $\boldsymbol{\varepsilon}$ the measured strains and $\mathbf{C}$ the calibration matrix. The accuracy of the result depends on the conditioning of that matrix as much as on the gauges, since the relative error in the recovered loads is bounded by the condition number times the relative error in the strains,

$$\frac{\left\| \delta \mathbf{L} \right\|}{\left\| \mathbf{L} \right\|} \le \kappa(\mathbf{C}) \, \frac{\left\| \delta \boldsymbol{\varepsilon} \right\|}{\left\| \boldsymbol{\varepsilon} \right\|}, \qquad \kappa(\mathbf{C}) = \left\| \mathbf{C} \right\| \left\| \mathbf{C}^{-1} \right\|$$

A badly conditioned calibration turns a one percent strain measurement into a ten percent load. This is a practical discipline with a literature, not a theoretical caution, and the procedures are set out in [Peele and Eckstrom 1975][research_peele_1975] for a low aspect ratio thin wing, in [Jenkins et al 1977][research_jenkins_1977] for a complex wing where the load paths are not obvious, and in [Jenkins and Kuhl 1977][research_jenkins_1977_2] for the accumulated experience on a delta configuration. **A wing that changes its load path with every sweep setting is the hardest case this literature contemplates**, since the calibration is not one matrix but a family of them. The modern answer is to stop inverting a fixed matrix at all. [Luderer and Thielecke 2025][research_luderer_2025] estimate loads with a linear parameter-varying hybrid model, applying to an estimator the idea behind a scheduled controller. For a pivoting wing the calibration must be repeated at each sweep setting, because the load path changes when the geometry does. Sweep angle becomes a measured quantity with an error budget, and its error propagates into every derivative through the geometry. Differentiating the lift-curve slope relation,

$$\frac{\partial C_{L\alpha}}{\partial \Lambda} \approx \frac{C_{L\alpha}(20^\circ) - C_{L\alpha}(60^\circ)}{\Lambda_2 - \Lambda_1} = \frac{4.42 - 2.11}{0.698} = 3.31 \ \text{per radian squared}$$

so a one degree error in recorded sweep is an error of between 1.3 and 2.7 percent in the lift-curve slope attributed to that point, the spread depending on where in the sweep range the point lies, and all of that before any aerodynamic uncertainty is considered. The tunnel-side methods for obtaining the dynamic derivatives against which such flight results are read are described in [Chambers et al 1981][research_chambers_1981], and the practice of reducing a full aircraft to locally linearized derivative sets in [Budd 1984][research_budd_1984]. Uncertainty propagates in the standard way,

$$u_c^2(y) = \sum_i \left( \frac{\partial y}{\partial x_i} \right)^2 u^2(x_i)$$

Derivative extraction from the flight records used the methods of the period, with [Bird and Jaquet 1951][research_bird_1951] representative of the practice of computing lateral motions from measured derivatives, and the modern descendants beginning with the maximum likelihood and Newton-Raphson approaches of [Iliff and Taylor 1972][research_iliff_1972] and applied to a full aircraft in [Gilyard 1972][research_gilyard_1972]. Manoeuvre and buffet characterization of the sort the programme also required is described in [Ray et al 1972][research_ray_1972], and the buffet boundary practice of the era in [Rathert et al 1951][research_rathert_1951]. Loads statistics and their treatment appear in [Hamer et al 1961][research_hamer_1961] and the institutional gathering of the whole subject in the conference proceedings of [NACA Conference on Aircraft 1957][research_naca_1957].

## The Flight Test Record

Two aircraft were built and flew to about Mach 0.9 and 40,000 feet, and the flight total is given as almost two hundred \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\] and as 149 \[[Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003]\].

The contractor programme on the first aircraft ended in October 1951, and the aircraft was then grounded for the installation of a NACA instrument package. In December 1951 Air Force pilots flew a brief evaluation of six flights, which were logged as joint Air Force and NACA flights because data were taken. The NACA High-Speed Flight Station then operated the first aircraft from 1952 to late 1955, under flight numbers running to 133 with the six joint flights counted, with the NACA pilots Walker, [Crossfield][ref_crossfield], Butchart, McKay and Armstrong among those its flight chronology names, and retired it after a landing gear door separated in flight. The second aircraft was operated only by Bell and the Air Force, as recorded in [Hallion 1984][research_hallion_1984]. The NASA fact sheet gives the first aircraft 20 Bell flights, six Air Force flights and 122 NACA flights, which sum to 148 \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\], and no source consulted counts the flights of the second aircraft.

The aircraft demonstrated what it was built to demonstrate, and early testing showed, in the summary of [Hallion 1984][research_hallion_1984], that sweep could be changed in flight, the trim consequence was absorbable, and the low-speed benefit was real. [Finch and Briggs 1953][research_finch_1953] report the stability and control investigation, [Finch and Walker 1953][research_finch_1953_2] the static longitudinal stability boundaries at 59 degrees, [Childs 1953][research_childs_1953] the sideslip behaviour, [Bellman 1953][research_bellman_1953] the lift and drag, and [Videan 1955][research_videan_1955] the dynamic lateral and longitudinal stability, with the load measurements of [Rogers and Dunn 1952][research_rogers_1952], [Reed 1955][research_reed_1955], and [Banner et al 1955][research_banner_1955] alongside. For a programme whose surviving aircraft flew about 150 times the primary record is dense and complete, and denser than the [X-4][related_post_a301_northrop_x4]'s. The buffet behaviour of swept wing-fuselage-tail combinations at high subsonic speed, which bounds the useful envelope at every sweep setting, is characterized in [Sutton 1959][research_sutton_1959], and the gust-alleviation study performed on the X-5 model has a direct companion on a 35 degree swept wing in [Croom and Huffman 1957][research_croom_1957_2].

On 13 October 1953 the second aircraft failed to recover from a spin at 60 degrees of sweep and was destroyed. The pilot, an Air Force major named Raymond Popson, was killed \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. The surviving aircraft continued flying at Edwards until 1955 and served as a chase aircraft until 1958, when it went to the National Museum of the United States Air Force, where it remains \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\].

The spin cost more than the aircraft. Tentative Air Force plans to develop the configuration into a low-cost tactical fighter for NATO and other foreign air forces, which [Hallion 1984][research_hallion_1984] describes, were cancelled because of its spin characteristics \[[Wikipedia Article on the Bell X-5][ref_bell_x5]\], a reasonable response to an aircraft with vicious spin characteristics and an unreasonable one to variable sweep as an idea. The distinction between the two is the subject of the next two sections.

## Comparison With Ground Prediction

The X-5 is the case in this series where the ground facilities had the most complete prior picture and the flight programme still found something they had not.

The low-speed aerodynamics were predicted well. Quarter-scale model results in [Kemp and Becht 1950][research_kemp_1950] and [Becht 1950][research_becht_1950] anticipated the lateral, directional, and landing behaviour, and the pressure work of [Kemp and Few 1951][research_kemp_1951] supplied the aerodynamic centre location directly rather than by inference. The influence of fuselage and tail surfaces on low-speed static stability had been mapped generally in [Bird et al 1952][research_bird_1952], the role of horizontal tail area and wing sweep in [Hayes and Sleeman 1959][research_hayes_1959], and tail height effects in [Fisher and Williams 1958][research_fisher_1958]. Chordwise fences and tail position, which are the standard remedies for the swept-wing pitch-up the X-5 also had to contend with, appear in [Queijo et al 1954][research_queijo_1954], with the flight evaluation of the pitch-up in [Anderson and Bray 1955][research_anderson_1955]. The fence remedy was examined by [Bray 1953][research_bray_1953] and, with the tail contribution separated, by [Buell and Kolbe 1957][research_buell_1957], while the leading-edge notch alternative was tried by [Weil and Morrison 1953][research_weil_1953] and the double-slotted flap case measured by [Naeseth 1956][research_naeseth_1956]. A free-flight model technique for obtaining longitudinal stability and control without a tunnel comes from [Gillis and Mitchell 1957][research_gillis_1957]. Boundary-layer stability as a function of sweep angle, which governs where the spanwise flow turns into transition, was measured by [Boltz et al 1960][research_boltz_1960].

The spin is the uncomfortable case. Free-spinning-tunnel technique was mature by 1951, and models of approximately one hundred military aeroplanes had been analysed together by 1946 \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\], as the record above also shows. A spin-tunnel investigation of the X-5 configuration would have been ordinary practice. No such report is among the sources consulted, which is not evidence that none was performed. The most that can be said is that the technique existed, the fleet-wide practice existed, and the correlation that a designer would have applied was in use at the time. That correlation would have rated the swept setting no worse for recovery by the rudder than the unswept one, and at altitude the X-5's relative density lay beyond its data at either setting. A tunnel model, unlike the correlation, would have represented the tail placement that the histories blame. The sources consulted do not record whether one was tested.

Ground facilities could not supply what the programme delivered, a demonstration rather than a number. The trim consequence of variable sweep was computable in 1948 by the same one-line relation used at the top of this article. What was not computable was whether an aircraft carrying that mechanism would be an aeroplane or a contraption, and a flying article settles that judgement. The same argument appears in the [X-4][related_post_a301_northrop_x4] treatment as the recurring answer to why programmes fly aircraft whose central numbers are already known.

## What the Data Changed

The X-5 validated the concept and invalidated the mechanization, and both halves mattered.

The concept propagated immediately. Langley took up variable sweep as a research subject and pursued it for a decade, and the idea entered service because of the resulting body of work. [Alford and Henderson 1959][research_alford_1959_2] is an exploratory low-speed investigation of variable-sweep configurations, with the multi-mission study of [Alford et al 1959][research_alford_1959] alongside it. The programme is summarized in progress by [Polhamus and Hammond 1960][research_polhamus_1960] and pursued through the configuration studies of [Spencer 1960][research_spencer_1960], [Foster and Morris 1960][research_foster_1960] at Mach 1.97, and [Bielat and Pierpont 1960][research_bielat_1960] at transonic speeds. The double-pivot variant appears in [Alford et al 1962][research_alford_1962] and the low-level supersonic configurations in [Alford et al 1966][research_alford_1966].

The decisive result is the pivot. **Moving the pivot outboard and leaving a fixed glove inboard reduces the aerodynamic centre travel by the product of two factors, as derived above, and it does so without any mechanism at all.** The design problem becomes a minimization over a single variable subject to a structural floor, since the pivot cannot be moved so far outboard that the panel it carries has no useful area,

$$\min_{y_p} \ \left| \Delta x_{ac}(y_p) \right| \quad \text{subject to} \quad S_{\text{movable}}(y_p) \ge S_{\min}$$

and the interior optimum exists because the travel falls quadratically with pivot station while the useful movable area falls only linearly. [Hammond and Henderson 1961][research_hammond_1961] investigate high-lift and lateral control on a semispan variable-sweep wing with an outboard pivot, [Henderson and Ray 1964][research_henderson_1964] vary the pivot location explicitly and report the longitudinal consequences, [Henderson and Ray 1965][research_henderson_1965] extend it to planform modification, and [Huffman 1972][research_huffman_1972] treats pivot location together with forewing configuration. [Hammond and Polhamus 1965][research_hammond_1965] and [Lamar and McKinney 1971][research_lamar_1971] fill in the surrounding aerodynamics. The idea was considered novel enough to patent, and both [Toll 1962][research_toll_1962] and [Hammond and Polhamus 1970][research_hammond_1970] hold patents on variable-sweep aircraft arising from this work.

Bell's translating mechanism therefore turned out to be the answer to a question that did not have to be asked. Bell had accepted an inboard pivot, inherited from the [P.1101][ref_p1101], and then engineered around the consequence. Langley moved the pivot outside the fuselage \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\] and the consequence largely disappeared. Here a design problem was dissolved rather than solved, and this clean example is the most transferable lesson of the programme.

The consolidated statement of the arc is [Langley Research Center 1966][research_naca_1966], an explicit summary of the research and development leading to the [F-111][ref_f111], with the development support recorded in [Center 1966][research_naca_1966_2] and the spin behaviour of the resulting aircraft in [Bowman and White 1974][research_bowman_1974]. The retrospective by two of the principals, [Polhamus and Toll 1981][research_polhamus_1981], is the document to read if only one is to be read.

The service aircraft followed. The [F-111][ref_f111], the [F-14][ref_f14], the [Panavia Tornado][ref_tornado], the [B-1][ref_b1_lancer], the [MiG-23][ref_mig23] and [MiG-27][ref_mig27], the [Su-17][ref_su17] and [Su-24][ref_su24], and the [Tu-22M][ref_tu22m] and [Tu-160][ref_tu160] all carry outboard-pivot variable sweep. The supersonic transport application, which did not proceed, is represented by [Lockwood 1966][research_lockwood_1966] on pitch-up with a high-aspect-ratio variable-sweep wing.

Then it stopped. No new variable-sweep combat aircraft has entered development since the 1980s \[[NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]\]. The cause is that every term in the inequality above moved.

The approach speed the mechanism existed to reduce is set by wing loading and maximum lift together, and both were attacked directly. A [leading-edge slat][ref_slat] and a manoeuvre flap recover the lift that sweep costs without moving the wing,

$$C_{L,\max} = C_{L,\max}^{\text{clean}} \cos \Lambda + \Delta C_{L,\text{slat}} + \Delta C_{L,\text{flap}}$$

and increments of 0.5 to 0.8 from such devices, taken here as representative, restore at 45 degrees of fixed sweep most of what the X-5 bought by unsweeping to 20. The development that made those increments routine has a long literature, running from the blowing experiments of [James and Maki 1957][research_james_1957] through the jet-flap configurations of [Vogler 1976][research_vogler_1976] and [Morehouse et al 1977][research_morehouse_1977] to the systematic leading and trailing edge flap study of [Gainer et al 1984][research_gainer_1984], and arriving at the mechanical design practice codified by [Rudolph 1998][research_rudolph_1998]. The subject remains live, with seamless flap concepts for swept wings analysed by [Bui 2018][research_bui_2018]. **Every one of those increments is an increment the variable-sweep wing no longer has to buy with a pivot.** Engine thrust removed the rest of the pressure, since the approach can be flown at higher wing loading when thrust is available to arrest a sink rate, and the field length that wing loading drives scales as

$$s_{\text{field}} \propto \frac{W/S}{\sigma \, C_{L,\max} \left( T/W \right)}$$

so a thrust-to-weight ratio that rose from the X-5's 0.50 toward unity halves the field length at fixed wing loading and recovers the whole of the variable-sweep argument. Digital flight control then removed the handling penalties that had made highly swept fixed wings unpleasant, which is to say it made the numerator of the mass-penalty inequality smaller by making a fixed compromise acceptable rather than by improving the compromise. The performance bookkeeping that decides such a question had become a formal exercise. [Redin 1981][research_redin_1981] applies a performance modelling technique to an airplane with variable sweep wings, the calculation this section describes in words, and the trajectory optimization machinery of [Erzberger et al 1975][research_erzberger_1975] and [Hale 1976][research_hale_1976] supplies the mission-weighting the inequality requires. Where the answer still came out favourable the configuration survived on paper, and [Beissner et al 1984][research_beissner_1984] apply near-term technology to a Mach 2.0 variable-sweep supersonic-cruise executive jet as late as 1984. Substituting into the break-even condition, a configuration whose aerodynamic gain has been halved while its structural penalty is unchanged fails the test,

$$\sum_i \phi_i \frac{\Delta \left( L/D \right)_i}{\left( L/D \right)_i} \ \longrightarrow \ \text{halved}, \qquad \frac{\Delta m_{\text{VG}}}{m_{\text{fuel}}} \ \longrightarrow \ \text{unchanged}$$

The variable-sweep wing was a mechanical solution to a problem later solved aerodynamically and electronically, and it was abandoned the way good engineering solutions usually are, because the problem changed. What the fleet learned in the meantime was recorded along the way, with the transonic agility of the F-111 compared against a supercritical-wing variant in [Friend and Sakamoto 1978][research_friend_1978] and the research aircraft built for that comparison described in [Painter and Caw 1978][research_painter_1978].

There is a coda, and it inverts the programme. A wing whose sweep can be changed in flight is a wing on which sweep can be treated as an experimental variable, and in the 1980s NASA used an [F-14][ref_f14] in that way. The Variable-Sweep Transition Flight Experiment flew a gloved wing through a range of sweep angles to measure boundary-layer transition as a function of sweep. It studied the crossflow problem named at the start of this article on a full-scale aircraft in real flight rather than in a tunnel. The techniques are described by [Anderson et al 1988][research_anderson_1988] and the results reported across [Anderson and Meyer 1990][research_anderson_1990] and [Anderson and Meyer 1990][research_anderson_1990_2], with supporting stability code work from [Rozendaal 1986][research_rozendaal_1986] and [Rozendaal 1987][research_rozendaal_1987], and the flutter clearance that had to precede any of it carried out by [Kehoe 1987][research_kehoe_1987] and [Freudinger and Kehoe 1990][research_freudinger_1990]. **The capability the X-5 was built to demonstrate ended its career as laboratory apparatus**, a more dignified fate than obsolescence, and one the programme could not have anticipated.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Swept and tapered wing aerodynamics at low speed | 694 |
| Morphing aircraft and the sweep transient | 664 |
| Flutter, aeroelasticity, loads and structure | 611 |
| Crossflow, transition and the swept-wing boundary layer | 404 |
| Spin, stall, departure and recovery | 363 |
| Compressibility, drag rise and the high-speed swept wing | 289 |
| Variable sweep, the pivot and the aircraft that used it | 264 |
| Longitudinal stability, trim and the tail | 188 |
| Flight control, scheduling and handling qualities | 175 |
| The oblique wing | 131 |
| Lateral-directional stability and control | 95 |
| Bird flight and the biological precedent | 48 |
| The atmosphere and the flight condition | 30 |
| Moments of inertia and the time-varying aircraft | 13 |
| Stability and control measured in flight | 8 |
| Other aeronautical literature on the configuration | 75 |
| **Total** | **4,052** |

Variable geometry did not die. It changed scale and it changed name, and the modern literature is large.

The direct descendant is the variable-sweep morphing unmanned aircraft, small enough that the mass penalty of a pivot is affordable and autonomous enough that the changing dynamics can be scheduled rather than flown. [Dai et al 2020][research_dai_sweep_2020] design and analyse such a configuration, and [Dai et al 2021][research_dai_mpc_2021] close a nonlinear model predictive controller around it, giving a modern answer to the scheduling problem the X-5 handed to its pilot. [Li et al 2020][research_li_varsweep_2020] simulate the aerodynamics of the same class of vehicle and [Guo et al 2020][research_guo_unsteady_2020] treat the unsteady flow during the sweep transient, a regime the X-5 avoided by moving slowly. [Ma et al 2021][research_ma_bionic_2021] analyse the stability of a multi-section variable-sweep wing and design augmentation for it, and [Gao et al 2022][research_gao_tandem_2022] treat the mode transition of a tandem-wing vehicle with variable sweep, where the configuration change is large enough that the transition is itself a flight phase.

The question the X-5 asked, what sweep does to the flight dynamics, is being asked again with better tools. [Si et al 2025][research_si_2025] compute the effect of wing sweep *and asymmetry* on a sweep-morphing aircraft, which covers the failure case Bell's twin jackscrews existed to prevent. Unsteady loads during the sweep transit, which the X-5's slow mechanism kept small, are calculated by [Bai et al 2025][research_bai_2025] for a shear variable-sweep wing. Control laws written for the changing plant appear in [Xu et al 2026][research_xu_2026], [Ren et al 2026][research_ren_2026], and [Wang et al 2026][research_wang_2026_3], with reinforcement learning used to decide *when* to morph as well as how to fly in [Cui et al 2026][research_cui_2026] and [Yang et al 2026][research_yang_2026]. [Feng et al 2025][research_feng_2025] carry the same problem into the hypersonic regime, and [Hua et al 2025][research_hua_2025] add the rigid-elastic coupling that a real morphing structure brings. A rare experimental entry is [Moens et al 2025][research_moens_2025], which characterizes stall on a generic variable-sweep configuration in the tunnel, and the small-vehicle case where the mass penalty is affordable is [Shanmugam et al 2025][research_shanmugam_2025]. For rotorcraft the actuation survey is [Burke and Gatto 2026][research_burke_2026], and [Li et al 2025][research_li_2025_2] coordinate flight and morphing on a quadrotor.

At the transient the modern work departs from the X-5 entirely. The quasi-static inequality derived above fails when the geometry changes on the timescale of the vehicle's modes, and then the equations of motion acquire terms the fixed-geometry treatment does not have. Both the inertia tensor and the aerodynamic coefficients become explicit functions of time through the shape parameter,

$$\frac{d}{dt} \left( \mathbf{I}(\Lambda) \, \boldsymbol{\omega} \right) = \mathbf{I}(\Lambda) \dot{\boldsymbol{\omega}} + \frac{\partial \mathbf{I}}{\partial \Lambda} \dot{\Lambda} \, \boldsymbol{\omega} + \boldsymbol{\omega} \times \mathbf{I}(\Lambda) \boldsymbol{\omega}$$

in which the middle term exists only while the wing is moving and vanishes at every detent. The X-5's thirty-second transit made that term negligible, and a fast morphing vehicle cannot ignore it. The actuation is not free either, since the hinge must work against the aerodynamic moment about the pivot,

$$P_{\text{act}} = M_{\text{hinge}} \dot{\Lambda}, \qquad E_{\text{act}} = \int_{\Lambda_1}^{\Lambda_2} M_{\text{hinge}}(\Lambda) \, d\Lambda$$

so speed costs power linearly and the energy is set by the load, which is why fast morphing is easy on a small vehicle and hard on a large one. Reducing that energy is an active design problem. [Kang et al 2026][research_kang_2026] assist the switching of a dual-mode morphing wing with stored energy so the actuator does not pay the whole bill, [Kang et al 2026][research_kang_2026_2] exploit bistability in a tensegrity mechanism so that two configurations are both stable and only the transition costs anything, and [Pisaneschi et al 2026][research_pisaneschi_2026] model an actuator that carries load as well as producing motion. [Lendraitis and Lukosevicius 2025][research_lendraitis_2025] reduce a compliant mechanism to a single actuation. The aeroelastic and dynamic response during the change must then be solved rather than assumed. [Changchuan et al 2022][research_changchuan_2022] compute the aeroelastic response of a folding wing *during* the morphing process, [Zhou and Huang 2021][research_zhou_huang_2021] build reduced-order models for nonlinear aeroelastic analysis of a morphing wing, and [Tsushima et al 2019][research_tsushima_2019] treat geometrically nonlinear static aeroelasticity of composite morphing wings. [Chiarelli and Bonomo 2019][research_chiarelli_2019] examine flutter and flutter-buffet on a swept wing, the failure mode a pivot joint most threatens. Flight dynamics and aeroelasticity, which the X-5 could treat as separate subjects because its wing was stiff and its transit slow, are now solved together for flexible flying wings by [Liu et al 2026][research_liu_2026_2]. Tailoring the structure so its deformation helps rather than hinders occupies [Sharifi et al 2025][research_sharifi_2025] and [Leitch et al 2025][research_leitch_2025]. Validating any of it at reduced scale, which is how a modern programme would approach the X-5 question, is treated by [Pan et al 2026][research_pan_2026].

Span change is the other axis, and the X-5 got it for free as a side effect. [Elelwi et al 2020][research_elelwi_span_2020] compare variable span-morphing of a tapered wing, with the structural sizing in [Elelwi et al 2021][research_elelwi_topology_2021] and the weight optimization in [Elelwi et al 2022][research_elelwi_weight_2022]. These are the direct modern treatment of the mass penalty computed above. [Bishay et al 2019][research_bishay_2019] and [Geva et al 2019][research_geva_2019] develop span-morphing cores and combined span and aerofoil adjustment. Folding wingtips are a partial variable geometry with an explicit historical debt, and [Dussart et al 2019][research_dussart_xb70_2019] take their inspiration from the [XB-70][ref_xb70] directly, with the roll consequences in [Dussart et al 2019][research_dussart_roll_2019] and the gust load alleviation application in [Cheung et al 2020][research_cheung_folding_2020].

The mechanism problem has been reformulated. Where Bell used a jackscrew, rails, and disc brakes, the modern approach is to eliminate the joint. Compliant mechanisms deform rather than articulate, and [Kumar et al 2021][research_kumar_topology_2021] optimize the topology of contact-aided shape morphing compliant mechanisms while [You et al 2020][research_you_skin_2020] set design criteria for the skin such a wing needs. [Nazeer et al 2021][research_nazeer_2021] report sensing, actuation, and control of a complete morphing wing prototype in the tunnel, and [Keidel et al 2020][research_keidel_2020] measure the control authority a camber-morphing flying wing actually achieves. Control authority decides whether morphing is a control system or a trim system, and for camber the question is now being answered affirmatively. [Hu et al 2025][research_hu_2025] and [Li et al 2025][research_li_2025] both close reinforcement learning loops around a camber-morphing wing, the first for gust load control and the second against stall flutter, which are control-bandwidth tasks rather than trim tasks. [Joshi et al 2026][research_joshi_2026] argue the aerodynamic case for trailing-edge morphing over a hinged flap outright, and [Ameduri et al 2025][research_ameduri_2025] design a compliant trailing edge for the high-lift role, the role that retired variable sweep. Mechanism design continues in [Alulema et al 2025][research_alulema_2025], [Ahmer et al 2026][research_ahmer_2026], and [Liu et al 2026][research_liu_2026_3], with metamaterial and laminate approaches to the skin problem in [Wang and Niu 2026][research_wang_2026_4] and [Manu et al 2026][research_manu_2026]. Design-space methods for the exercise are [Badihi et al 2026][research_badihi_2026], [Kambayashi and Kogiso 2025][research_kambayashi_2025], and [Phuekpan et al 2025][research_phuekpan_2025], with the surface flow-field prediction that such optimization needs unified across geometries by [Du et al 2026][research_du_2026]. The aerodynamic optimization framing is [Klimczyk and Goraj 2019][research_klimczyk_2019] and [Traub 2019][research_traub_2019] supplies an experimental morphing annular wing. The [adaptive compliant wing][ref_compliant_wing] is the configuration these lines converge on.

The most striking modern result comes from biology, and it closes the circle. Gulls change the sweep of their wings at the elbow and wrist, and in doing so they move the position of their aerodynamic centre. [Harvey et al 2021][research_harvey_gull_2021] show that gull-inspired joint-driven wing morphing allows adaptive longitudinal flight control, and [Harvey and Inman 2022][research_harvey_inman_2022] establish that gull dynamic pitch stability is *controlled* by wing morphing. The aerodynamic centre travel that Bell spent a jackscrew, a set of rails, and some 27 inches of translation trying to cancel is the quantity a gull uses as its longitudinal control input. **The X-5 treated the aerodynamic centre shift as the cost of variable sweep. The bird treats it as the point of it.**

That inversion can be given a number, and doing so is the cleanest way to see both its promise and its difficulty. Treat sweep as a control effector and give it a control derivative in the same form as an elevator's,

$$C_{m \Lambda} = \frac{\partial C_m}{\partial \Lambda} = -C_L \frac{s_{ac} \cos \Lambda}{\bar{c}}$$

which for the X-5 at mid sweep and a lift coefficient of 0.3 returns

$$C_{m \Lambda}(40^\circ) = -0.3 \times \frac{1.768 \times 0.766}{1.592} = -0.26 \ \text{per radian}$$

against a representative elevator control power near $-0.7$ per radian. **Sweep is worth roughly a third of an elevator as a pitch effector**, a great deal of authority for a surface not intended as one. The obstacle is entirely rate. Producing the moment of a five degree elevator deflection requires

$$\Delta \Lambda = \frac{\left| C_{m \delta_e} \right| \delta_e}{\left| C_{m \Lambda} \right|} = \frac{0.7 \times 0.0873}{0.26} = 0.24 \ \text{radians}$$

or 13.7 degrees of sweep, and delivering it inside one short-period time constant of about 0.33 seconds demands

$$\dot{\Lambda}_{\text{required}} = \frac{13.7}{0.33} = 42 \ \text{degrees per second}$$

against the X-5's 1.33 to 2.0, **a factor of twenty-one to thirty-one**. A gull closes that gap with a wing weighing a few hundred grams and a joint driven by muscle, and the aerodynamic peculiarities of a real feathered wing raise further questions, as [Lichter 1974][research_lichter_1974] shows in measuring what porosity does to the lift and drag of bird wings. The avian result has since been given the analytical treatment it needed. [Wang et al 2026][research_wang_2026] construct a reduced-order unsteady lift model for **local sweep morphing of an avian wing**, the mathematical object this article has been circling, and [Chen et al 2026][research_chen_2026] show that tail bending contributes to the same control problem, so the bird is not relying on the wing alone. Engineered wings built to that standard of smoothness and accuracy are reported by [Zhang et al 2026][research_zhang_2026].

There is one line of aircraft work that has already crossed the gap, in a different variable. The Active Aeroelastic Wing programme used a deliberately flexible wing and drove its twist with leading and trailing edge surfaces, so that the shape of the wing became the control effector rather than the deflection of a flap on it. [Clarke et al 2005][research_clarke_2005] report the flight test, and the sensing that a shape-controlled wing requires appears in [Pena et al 2018][research_pena_2018]. That programme changed wing shape at control bandwidth rather than at trim bandwidth, satisfying the inequality the X-5 could not, and it did so by choosing a shape variable with a far smaller inertia than sweep. The aeroelastic behaviour that makes such a wing possible is the same divergence problem that constrains forward sweep, treated in [Ricketts and Doggett 1980][research_ricketts_1980], and the pitch-up alleviation methods of [Rao and Johnson 1982][research_rao_1982] belong to the same family of shape-based fixes. Whether an aircraft can be built on the same principle is an open question and the papers do not claim otherwise, but the gap lies in rate, not authority, and rate is the more tractable thing to be short of.

The other historical alternative also survives in the literature, and it deserves more than a mention because it is the road not taken. An [oblique wing][ref_oblique_wing] pivots as a single panel about the fuselage centreline. Because the panel that sweeps forward and the panel that sweeps aft are the same panel, the total lift distribution stays far more nearly fixed and **the aerodynamic centre travel that dominates this article largely cancels**. The price is asymmetry in every other axis, since an oblique wing is in permanent sideslip with respect to its own structure and its rolling, yawing, and pitching responses couple in ways a symmetric aircraft never encounters.

Robert T. Jones, whose 1947 planform work is cited in The Source Base and whose 1940 study of the wing wake underlies the [X-4][related_post_a301_northrop_x4] article, spent much of his later career on it. The design case is set out by [Jones 1977][research_jones_1977], the aeroelastic behaviour across [Jones and Nisbet 1976][research_jones_1976] and [Jones and Nisbet 1976][research_jones_1976_2], and the divergence problem the asymmetry creates by [A study of the 1973][research_naca_1973]. The configuration was carried to wind-tunnel and flight-model work on an F-8 airframe in [Graham et al 1973][research_graham_1973] and [Graham et al 1973][research_graham_1973_2], with the control characteristics in [Smith et al 1976][research_smith_1976], the transonic testing in [Kennelly et al 1990][research_kennelly_1990], and the final aerodynamic characterization in [Kennelly et al 1999][research_kennelly_1999]. Configuration studies continued in [Oblique wing transonic transport 1977][research_naca_1977] and the scissor-wing tradeoff of [Selberg et al 1990][research_selberg_1990], and [Hopkins 1975][research_hopkins_1975] examines wing bend on a low aspect ratio oblique wing. [Yue et al 2019][research_yue_oblique_2019] design sliding mode control for an oblique wing aircraft during the skewing process. The skewing transient is the same problem in a different geometry. The configuration is being revisited on its aerodynamic merits, with transonic and supersonic shape design by [Sun et al 2026][research_sun_2026] and the effects of oblique angle and leading-edge asymmetry computed by [Liu et al 2026][research_liu_2026]. The supersonic transport application that motivated most of the original work has its own live literature, and [Felix et al 2026][research_felix_2026] build reduced-order drag polars for such concepts while [Seraj and Martins 2025][research_seraj_2025] minimize trim drag on a three-surface configuration, the trim-drag bookkeeping this article also performs on a tail load. Planform efficiency as a pure geometry question is [Tiniakov and Limtrakul 2026][research_tiniakov_2026]. **The oblique wing solved the X-5's central problem and was never built for service** \[[Wikipedia Article on the Oblique Wing][ref_oblique_wing]\], a reminder that dissolving a design difficulty is necessary and not sufficient.

Spin research continued and has been reformulated as an optimal control problem. [Venkateswara Rao and Go 2019][research_rao_spin_2019] optimize spin recovery manoeuvres, [Salahudden and Ghosh 2021][research_salahudden_2021] design robust flat-spin recovery using optimally deflected surfaces, and [Kapuscinski et al 2020][research_kapuscinski_2020] address the measurement problem of determining aircraft state during recovery. High angle-of-attack aerodynamics of finite-span wings, the flow regime in which the X-5's accident occurred, is treated by [Faure and Leogrande 2020][research_faure_2020]. Planform optimization as a design activity rather than a mechanism appears in [Jim et al 2021][research_jim_planform_2021] and [Dam et al 2022][research_dam_planform_2022], and aeroelastic planform design in [Hermanutz and Hornung 2020][research_hermanutz_2020]. The modern view is that if the planform can be chosen well enough by computation, the need to change it in flight recedes, and for that quiet reason variable sweep left the fighter fleet.

### Swept and tapered wing aerodynamics at low speed

**The low-speed price of sweep, and the largest cluster.** Lift-curve slope, maximum lift and tip stall, high-lift devices and fences, vortex flows and wing-body interference on swept and delta wings at low speed, together with induced drag and planform.

**694 records.** \[[Abdelghany et al 2016][research_abdelghany_khalil_2016]\] \[[Abdelhamid and Kandil 1998][research_abdelhamid_kandil_1998]\] \[[Ackeret 1925][research_ackeret_1925]\] \[[Ackeret et al 1951][research_ackeret_1951]\] \[[Adegbindin et al 2016][research_adegbindin_love_2016]\] \[[Adhikari et al 2022][research_adhikari_loubimov_2022]\] \[[Adoghe][research_adoghe]\] \[[Advanced Aerodynamics. Selected NASA 1981][research_advanced_aerodynamics_1981]\] \[[Aerodynamic Design Wing 1969][research_aerodynamic_design_1969]\] \[[Aerodynamic Performance of Lambda 2024][research_aerodynamic_performance_2024]\] \[[Aerodynamics of Wing-Body Combinations 2010][research_aerodynamics_of_2010]\] \[[Ahmed and Jave 1995][research_ahmed_jave_1995]\] \[[Aiken et al 1979][research_aiken_falarski_1979]\] \[[Aircraft Drag 2010][research_aircraft_drag_2010]\] \[[Aircraft Wing Design 2005][research_aircraft_wing_2005]\] \[[Airfoil and Wing Theory 2014][research_airfoil_and_2014]\] \[[Airfoil and Wing/Tail Geometry 2024][research_airfoil_and_2024]\] \[[Airspeed vs Flight Path 2003][research_airspeed_vs_2003]\] \[[Alam et al 2022][research_alam_kara_2022]\] \[[Alasty et al 2004][research_alasty_alemohammad_2004]\] \[[Albers and Schröder 2020][research_albers_schroder_2020]\] \[[Aleisa et al 2023][research_aleisa_kontis_2023]\] \[[Ali 2017][research_ali_2017]\] \[[Alley and Phillips 2010][research_alley_phillips_2010]\] \[[Alley et al 2007][research_alley_phillips_2007]\] \[[Alpatskiy 2026][research_alpatskiy_2026]\] \[[An analysis of gap 1981][research_an_analysis_1981]\] \[[An experimental and computational 1978][research_an_experimental_1978]\] \[[Ando and Yamamoto 1976][research_ando_yamamoto_1976]\] \[[Ankenbruck 1946][research_ankenbruck_1946]\] \[[Another Vertical Wind Tunnel 1932][research_another_vertical_1932]\] \[[Anto 2026][research_anto_2026]\] \[[Anwar 2025][research_anwar_2025]\] \[[Anyoji et al 2013][research_anyoji_liu_2013]\] \[[Apostolyuk 2007][research_apostolyuk_2007]\] \[[Appendix H Aerodynamics of 2010][research_appendix_h_2010]\] \[[Araujo-Estrada et al 2015][research_araujoestrada_lowenberg_2015]\] \[[Araujo-Estrada et al 2016][research_araujoestrada_gong_2016]\] \[[Arnott et al 1996][research_arnott_bernstein_1996]\] \[[Arnottt and Bernstein 2000][research_arnottt_bernstein_2000]\] \[[Asaro and Vos 2026][research_asaro_vos_2026]\] \[[Ashenberg and Weihs 1984][research_ashenberg_weihs_1984]\] \[[Ashworth et al 1988][research_ashworth_mouch_1988]\] \[[Atmosphere, Aerodynamics, and Propulsion][research_atmosphere_aerodynamics]\] \[[Aubeelack][research_aubeelack]\] \[[Aubeelack and Botez 2017][research_aubeelack_botez_2017]\] \[[Aung Ko Wynn and Cao Yi Hua 2010][research_aungkowynn_caoyihua_2010]\] \[[Bagley 1962][research_bagley_1962]\] \[[Bajaj 2019][research_bajaj_2019]\] \[[Balachandran 2014][research_balachandran_2014]\] \[[Banerjee and Taneja 2025][research_banerjee_taneja_2025]\] \[[Barger and Wright 1966][research_barger_wright_1966]\] \[[Barnes and Visbal 2019][research_barnes_visbal_2019]\] \[[Barnes and Visbal 2019][research_barnes_visbal_2019_b]\] \[[Barrows 2006][research_barrows_2006]\] \[[Belotserkovskii and Nisht 1974][research_belotserkovskii_nisht_1974]\] \[[Ben-Gida et al 2019][research_bengida_gurka_2019]\] \[[Bera 1974][research_bera_1974]\] \[[Bernstein and Hamid 1995][research_bernstein_hamid_1995]\] \[[Bertelrud 1979][research_bertelrud_1979]\] \[[Bertelrud 1980][research_bertelrud_1980]\] \[[Bertelrud 1981][research_bertelrud_1981]\] \[[Bertelrud and Nordstrom 1983][research_bertelrud_nordstrom_1983]\] \[[Bidwell 2014][research_bidwell_2014]\] \[[Bidwell and Mohler 1995][research_bidwell_mohleryrjr_1995]\] \[[Bippes 1990][research_bippes_1990]\] \[[Blair et al 2008][research_blair_robinson_2008]\] \[[Boden et al 2013][research_boden_lanari_2013]\] \[[Bodonyl 1994][research_bodonyl_1994]\] \[[Bolzon et al 2016][research_bolzon_kelso_2016]\] \[[Borden 2004][research_borden_2004]\] \[[Borodulin et al 2016][research_borodulin_ivanov_2016_b]\] \[[Boudreault 1983][research_boudreault_1983_b]\] \[[Bourdin 2002][research_bourdin_2002]\] \[[Bourgault-Cote and Laurendeau 2015][research_bourgaultcote_laurendeau_2015]\] \[[Bouton 1950][research_bouton_1950]\] \[[Bragg et al 1991][research_bragg_khodadoust_1991]\] \[[Brandt and Bons 2023][research_brandt_bons_2023]\] \[[Brandt and Bons 2024][research_brandt_bons_2024]\] \[[Brandt et al 2022][research_brandt_mcfadden_2022]\] \[[Brandt et al 2023][research_brandt_mcfadden_2023]\] \[[Bridges 2005][research_bridges_2005]\] \[[Broeren et al 2013][research_broeren_potapczuk_2013]\] \[[Broeren et al 2017][research_broeren_woodard_2017]\] \[[Broeren et al 2019][research_broeren_potapczuk_2019]\] \[[Broeren et al 2020][research_broeren_lee_2020]\] \[[Broering and Lian 2010][research_broering_lian_2010]\] \[[Brune and Bogataj 1990][research_brune_bogataj_1990]\] \[[Bullens and Traub 2021][research_bullens_traub_2021]\] \[[Bunge and Kroo 2012][research_bunge_kroo_2012]\] \[[Burkett 1989][research_burkett_1989]\] \[[Buter and Rao 1984][research_buter_rao_1984]\] \[[Butler 1976][research_butler_1976]\] \[[Butler 1983][research_butler_1983]\] \[[Butler and Bons 2025][research_butler_bons_2025]\] \[[Buzica et al 2018][research_buzica_debschutz_2018]\] \[[Camello et al 2016][research_camello_lee_2016]\] \[[Camello et al 2017][research_camello_bragg_2017]\] \[[Carafoli 1969][research_carafoli_1969_b]\] \[[Carnegie][research_carnegie]\] \[[Carter 2016][research_carter_2016]\] \[[Carter 2017][research_carter_2017]\] \[[Carter et al 2011][research_carter_brandt_2011]\] \[[Caruso et al 1988][research_caruso_mendenhall_1988]\] \[[Castillo Zuñiga et al 2021][research_castillozuniga_giacobinisouza_2021]\] \[[Chana 2000][research_chana_2000]\] \[[Chao and van Dam 2004][research_chao_vandam_2004]\] \[[Chapter 2. Aerodynamics of 1960][research_chapter_2_1960]\] \[[CHAPTER NINE. The Minimum 1990][research_chapter_nine_1990]\] \[[CHAPTER SEVEN. Wings of 1990][research_chapter_seven_1990]\] \[[CHAPTER SIX. Effects of 1990][research_chapter_six_1990]\] \[[CHAPTER TEN. Drag of 1990][research_chapter_ten_1990]\] \[[Characteristic Parameters for Airfoil 2021][research_characteristic_parameters_2021]\] \[[Characteristic Parameters for Airfoil 2025][research_characteristic_parameters_2025]\] \[[Chen 2023][research_chen_2023]\] \[[Chen 2024][research_chen_2024]\] \[[Chen 2026][research_chen_2026_b]\] \[[Chen 2026][research_chen_2026_c]\] \[[Chen and Barlow 1995][research_chen_barlow_1995]\] \[[Chen et al 2001][research_chen_khalid_2001]\] \[[Chen et al 2025][research_chen_meng_2025]\] \[[Childs 1986][research_childs_1986]\] \[[Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]\] \[[Chuprun 1980][research_chuprunjr_1980]\] \[[Cianciarulo et al 2024][research_cianciarulo_schmidt_2024]\] \[[Clarke 1976][research_clarke_1976]\] \[[Coe et al 1990][research_coe_perkins_1990]\] \[[Coetzee et al 2023][research_coetzee_lowenberg_2023]\] \[[Concepts and Computational Models 2021][research_concepts_and_2021]\] \[[Conner and Foster 1947][research_conner_foster_1947]\] \[[Costello 2009][research_costello_2009]\] \[[Couillaud][research_couillaud]\] \[[Cousteix and Pailhas 1983][research_cousteix_pailhas_1983]\] \[[Covert 1984][research_covert_1984]\] \[[Coward and Hall 1996][research_coward_hall_1996]\] \[[Cummings and Sandlin 1987][research_cummings_sandlin_1987]\] \[[Curriston and White 2025][research_curriston_white_2025]\] \[[Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]\] \[[Dam et al 2022][research_dam_planform_2022]\] \[[Dannenberg 1950][research_dannenberg_1950]\] \[[Darida and Smrcek 1998][research_darida_smrcek_1998]\] \[[Das and Wichmann 2004][research_das_wichmann_2004]\] \[[Dehaan 1990][research_dehaan_1990]\] \[[DeJarnette and Jones 1978][research_dejarnette_jones_1978]\] \[[Demasi 2007][research_demasi_2007]\] \[[Demasi et al 2014][research_demasi_dipace_2014]\] \[[Demasi et al 2014][research_demasi_dipace_2014_b]\] \[[Demasi et al 2016][research_demasi_monegato_2016]\] \[[Denegri 2009][research_denegri_2009]\] \[[Denham and Owens 2016][research_denham_owens_2016]\] \[[Design of the circulation 1979][research_design_of_1979]\] \[[Dicarlo et al 1992][research_dicarlo_brown_1992]\] \[[Diebold and Bragg 2015][research_diebold_bragg_2015]\] \[[Diebold et al 2012][research_diebold_monastero_2012]\] \[[Diebold et al 2013][research_diebold_broeren_2013]\] \[[Diederich and Zlotnick 1949][research_diederich_zlotnick_1949]\] \[[Dikbas and Atik 2018][research_dikbas_atik_2018]\] \[[Drag Reduction using Suction 2011][research_drag_reduction_2011]\] \[[Draper 1950][research_draper_1950]\] \[[Durfee 1919][research_durfee_1919]\] \[[Economou 2025][research_economou_2025]\] \[[Ekaterinaris and Schiff 1994][research_ekaterinaris_schiff_1994]\] \[[El-Ramly and Rainbird 1977][research_elramly_rainbird_1977]\] \[[Elements of Aerodynamic Wing 2013][research_elements_of_2013]\] \[[Eliasson 2008][research_eliasson_2008]\] \[[Elkhoury and Nakad 2009][research_elkhoury_nakad_2009]\] \[[Ellis and Maris 1977][research_ellis_maris_1977]\] \[[ElRamly][research_elramly]\] \[[Englar 1975][research_englar_1975]\] \[[Erickson 1979][research_erickson_1979]\] \[[Erickson and Brandon 1987][research_erickson_brandon_1987]\] \[[Ericsson 1984][research_ericsson_1984]\] \[[Ericsson 1998][research_ericsson_1998_b]\] \[[Ericsson 2003][research_ericsson_2003]\] \[[Ericsson and King 1990][research_ericsson_king_1990]\] \[[Ericsson and King 1993][research_ericsson_king_1993]\] \[[Ericsson and Reding 1976][research_ericsson_reding_1976]\] \[[Esquieu 2003][research_esquieu_2003]\] \[[Estimating Wing-Body Aerodynamics 2010][research_estimating_wing_body_2010]\] \[[Evolution of modern air 1980][research_evolution_of_1980]\] \[[Experience Gained During Development 2010][research_experience_gained_2010]\] \[[F. Nonsteady Wing Characteristics 1957][research_f_nonsteady_1957]\] \[[Fan and Li 2019][research_fan_li_2019]\] \[[Feng and Wang 2020][research_feng_wang_2020]\] \[[Filippone 2006][research_filippone_2006]\] \[[Fixed, Rigid-Wing Aerodynamics 2007][research_fixed_rigid_wing_2007]\] \[[Flexible-Wing Aerodynamics 2007][research_flexible_wing_aerodynamics_2007]\] \[[Forte and Nguyen 2024][research_forte_nguyen_2024]\] \[[Fournier 1961][research_fournier_1961]\] \[[Fremaux et al 1990][research_fremaux_vijgen_1990]\] \[[Frink 2015][research_frink_2015]\] \[[Frolov 2021][research_frolov_2021]\] \[[From Tube and Wing 2013][research_from_tube_2013]\] \[[Frost and Rutherford 1963][research_frost_rutherford_1963]\] \[[Fujita et al 2014][research_fujita_motoda_2014]\] \[[Furey 1980][research_furey_1980]\] \[[Gagnon and Zingg 2016][research_gagnon_zingg_2016]\] \[[Gallman et al 1990][research_gallman_smith_1990]\] \[[Gardner 1951][research_gardner_1951]\] \[[Gego and Bugaj 2023][research_gego_bugaj_2023]\] \[[German Development of the 2010][research_german_development_2010]\] \[[Gerontakos and Lee 2005][research_gerontakos_lee_2005]\] \[[Gerontakos and Lee 2006][research_gerontakos_lee_2006]\] \[[Ghaemi et al 2019][research_ghaemi_lax_2019]\] \[[Ghasemi et al 2014][research_ghasemi_mosahebi_2014]\] \[[Ghoreyshi et al 2022][research_ghoreyshi_aref_2022]\] \[[Ghoreyshi et al 2022][research_ghoreyshi_nangia_2022]\] \[[Ghoreyshi et al 2024][research_ghoreyshi_fagley_2024]\] \[[Gilman and Burdges 1967][research_gilman_burdges_1967]\] \[[Giunta et al 1995][research_giunta_narducci_1995]\] \[[Goldschmied 1990][research_goldschmied_1990]\] \[[Goodson 1966][research_goodson_1966]\] \[[Gordnier 1991][research_gordnier_1991]\] \[[Gordnier and Visbal 2003][research_gordnier_visbal_2003]\] \[[Gordnier and Visbal 2005][research_gordnier_visbal_2005]\] \[[Gordnier and Visbal 2006][research_gordnier_visbal_2006]\] \[[Graham 1951][research_graham_1951]\] \[[Grantz 1985][research_grantz_1985]\] \[[Greenblatt and Washburn 2007][research_greenblatt_washburn_2007]\] \[[Griffin et al 1983][research_griffin_haerter_1983]\] \[[Gudmundsson 2014][research_gudmundsson_2014]\] \[[Gudmundsson 2014][research_gudmundsson_2014_b]\] \[[Gudmundsson 2022][research_gudmundsson_2022]\] \[[Gudmundsson 2022][research_gudmundsson_2022_b]\] \[[Guler and Nikbay 2026][research_guler_nikbay_2026]\] \[[Gupta 1990][research_gupta_1990]\] \[[Gupta et al 2023][research_gupta_kumar_2023]\] \[[Hahn and Drikakis 2008][research_hahn_drikakis_2008]\] \[[Hahn and Drikakis 2009][research_hahn_drikakis_2009]\] \[[Haider et al 2022][research_haider_mansor_2022]\] \[[Haider et al 2023][research_haider_mansor_2023]\] \[[Hammer and Garmann 2023][research_hammer_garmann_2023_b]\] \[[Hammond 1963][research_hammond_1963]\] \[[Hancock 1960][research_hancock_1960]\] \[[Hancock 1971][research_hancock_1971]\] \[[Hanin and Barsony-Nagy 1983][research_hanin_barsonynagy_1983]\] \[[Harms et al 2020][research_harms_kaufmann_2020]\] \[[Hartshorn 2011][research_hartshorn_2011]\] \[[Hattasanjaya 2024][research_hattasanjaya_2024]\] \[[Hauptman 1987][research_hauptman_1987]\] \[[Haynes and Reed 1997][research_haynes_reed_1997]\] \[[Haynes and Reed 2000][research_haynes_reed_2000]\] \[[Hayostek and Amitay 2018][research_hayostek_amitay_2018]\] \[[He et al 2021][research_he_guo_2021]\] \[[Hertz et al 1982][research_hertz_shirk_1982]\] \[[Hicks and Henne 1977][research_hicks_henne_1977]\] \[[Hicks and Moulton 1988][research_hicks_moulton_1988]\] \[[Hiller 2002][research_hiller_2002]\] \[[Hirschel et al 2020][research_hirschel_rizzi_2020]\] \[[Hirschel et al 2020][research_hirschel_rizzi_2020_b]\] \[[Hoang et al 2014][research_hoang_nguyen_2014]\] \[[Hoerner 1952][research_hoerner_1952]\] \[[Hopkins 1964][research_hopkins_1964]\] \[[Howe 2000][research_howe_2000]\] \[[Huang 2003][research_huang_2003]\] \[[Huehne et al 2013][research_huehne_mahmood_2013]\] \[[Human-Powered Aircraft Wing Design 2014][research_human_powered_aircraft_2014]\] \[[Hunt and Gowadia 1981][research_hunt_gowadia_1981]\] \[[Hövelmann and Breitsamter 2015][research_hovelmann_breitsamter_2015]\] \[[Ichikawa 1996][research_ichikawa_1996]\] \[[Ichikawa et al 2021][research_ichikawa_koike_2021]\] \[[Iliff 1977][research_iliff_1977]\] \[[Imber and Rogers 1996][research_imber_rogers_1996]\] \[[Iosilevskii 2025][research_iosilevskii_2025]\] \[[Iosilevskii 2025][research_iosilevskii_2025_b]\] \[[Iosilevskii 2025][research_iosilevskii_2025_c]\] \[[Iqbal et al 2025][research_iqbal_alfaruk_2025]\] \[[Irani et al 2016][research_irani_amoozgar_2016]\] \[[Isah et al 2022][research_isah_lawal_2022]\] \[[Ishtiaq and Israr 2013][research_ishtiaq_israr_2013]\] \[[Iyer and Takahashi 2025][research_iyer_takahashi_2025]\] \[[Jalil et al 2024][research_jalil_hashim_2024]\] \[[Jin 2024][research_jin_2024]\] \[[Jing and Huang 2017][research_jing_huang_2017]\] \[[Johnson 1959][research_johnson_1959]\] \[[Johnson and Hageman 1950][research_johnson_hageman_1950]\] \[[Jordan 1971][research_jordan_1971]\] \[[Kalemaris 1980][research_kalemaris_1980]\] \[[Kanazaki et al 2008][research_kanazaki_imamura_2008]\] \[[Kasuga et al 2017][research_kasuga_yoshida_2017]\] \[[Katz 1989][research_katz_1989]\] \[[Kaushik 2018][research_kaushik_2018]\] \[[Kegelman and Roos 1989][research_kegelman_roos_1989]\] \[[Khazaee Kuhpar and Seyed-Aghazadeh 2026][research_khazaeekuhpar_seyedaghazadeh_2026]\] \[[Khodadoust and Bragg 1990][research_khodadoust_bragg_1990]\] \[[Kida 1982][research_kida_1982]\] \[[Kimberlin 2003][research_kimberlin_2003]\] \[[Kirmse 2016][research_kirmse_2016]\] \[[Kjelgaard et al 1986][research_kjelgaard_sellersiii_1986]\] \[[Klopfenstein 1965][research_klopfenstein_1965]\] \[[Knight and Wenzinger 1930][research_knight_wenzinger_1930]\] \[[Kogiso et al 2000][research_kogiso_tsushima_2000]\] \[[Kolbakir 2016][research_kolbakir_2016]\] \[[Kolonay et al 2004][research_kolonay_eastep_2004]\] \[[Krienes 1941][research_krienes_1941]\] \[[Krispin and Portnoy 1988][research_krispin_portnoy_1988]\] \[[Krone 1980][research_kronejr_1980]\] \[[Krone 1980][research_kronejr_1980_b]\] \[[Kroo 1982][research_kroo_1982]\] \[[Kryvokhatko 2023][research_kryvokhatko_2023]\] \[[Kryvokhatko 2023][research_kryvokhatko_2023_b]\] \[[Kryvokhatko 2023][research_kryvokhatko_2023_c]\] \[[Kryvokhatko 2024][research_kryvokhatko_2024]\] \[[Kryvokhatko 2024][research_kryvokhatko_2024_b]\] \[[Kulfan 1979][research_kulfan_1979]\] \[[Kulfan and Vachal 1978][research_kulfan_vachal_1978]\] \[[Kumar and Aravindan 2014][research_kumar_aravindan_2014]\] \[[Kumar and Khalid 2014][research_kumar_khalid_2014]\] \[[Kumar et al 2026][research_kumar_ghosh_2026]\] \[[Kurita et al 2013][research_kurita_koike_2013]\] \[[Lacey 1979][research_lacey_1979]\] \[[Laitone 1989][research_laitone_1989]\] \[[Lam and Maull 1993][research_lam_maull_1993]\] \[[Lamar 1980][research_lamar_1980]\] \[[Lan 1976][research_lan_1976]\] \[[Landman et al 2005][research_landman_simpson_2005]\] \[[Larco et al 2018][research_larco_constatin_2018]\] \[[Large 1981][research_large_1981]\] \[[Lavoie et al 2018][research_lavoie_bourgaultcote_2018]\] \[[Lee][research_lee]\] \[[Lee 2004][research_lee_2004]\] \[[Lee 2006][research_lee_2006]\] \[[Lee 2013][research_lee_2013]\] \[[Lee and Ko 2009][research_lee_ko_2009]\] \[[Lee et al 2018][research_lee_broeren_2018]\] \[[Lee et al 2019][research_lee_broeren_2019]\] \[[Lee et al 2020][research_lee_broeren_2020]\] \[[Lei and Zha 2021][research_lei_zha_2021]\] \[[Leoviriyakit and Jameson 2005][research_leoviriyakit_jameson_2005]\] \[[Letko 1956][research_letko_1956]\] \[[Leung and Zingg 2011][research_leung_zingg_2011]\] \[[Levesque et al 2015][research_levesque_pigeon_2015]\] \[[Leylek and Costello 2013][research_leylek_costello_2013]\] \[[Li and Leschziner 2007][research_li_leschziner_2007]\] \[[Li et al 2023][research_li_qiao_2023]\] \[[Liang 2024][research_liang_2024]\] \[[Liersch and Bishop 2018][research_liersch_bishop_2018]\] \[[Lift and Drag 2017][research_lift_and_2017]\] \[[Lin 2025][research_lin_2025]\] \[[Lin et al 1996][research_lin_ng_1996]\] \[[Liu 2006][research_liu_2006]\] \[[Liu 2022][research_liu_2022]\] \[[Liu 2022][research_liu_2022_b]\] \[[Liu 2022][research_liu_2022_e]\] \[[Liu et al 2009][research_liu_liou_2009]\] \[[Lockhart][research_lockhart]\] \[[Lombardi and Morelli 1994][research_lombardi_morelli_1994]\] \[[Lombardi and Vicini 1994][research_lombardi_vicini_1994]\] \[[Lottati 1984][research_lottati_1984]\] \[[Lowe 1988][research_lowe_1988]\] \[[Lowry et al 1948][research_lowry_axelson_1948]\] \[[Lowson and Riley 1995][research_lowson_riley_1995]\] \[[Lu and Lu 1997][research_lu_lu_1997]\] \[[Lv et al 2017][research_lv_zhang_2017]\] \[[Lynch et al 2015][research_lynch_crowell_2015]\] \[[Ahmad et al 2018][research_mahmad_emnasir_2018]\] \[[Ma 1989][research_ma_1989]\] \[[Ma 2025][research_ma_2025]\] \[[Ma et al 2004][research_ma_liu_2004]\] \[[Mahaffey and Harding 1970][research_mahaffey_harding_1970]\] \[[Mahns and Amitay 2025][research_mahns_amitay_2025]\] \[[Maines et al 2018][research_maines_ghee_2018]\] \[[Mamla and Galinski 2009][research_mamla_galinski_2009]\] \[[Manchester et al 2017][research_manchester_lipton_2017]\] \[[Manoilo 2026][research_manoilo_2026]\] \[[Manokaran et al 2006][research_manokaran_vidya_2006]\] \[[Mansfield 1952][research_mansfield_1952]\] \[[Margaris and Gursul 2004][research_margaris_gursul_2004]\] \[[Marino 2004][research_marino_2004]\] \[[Marske 1975][research_marske_1975]\] \[[Marzouk 2025][research_marzouk_2025_b]\] \[[Matalla and Scholz 2021][research_matalla_scholz_2021]\] \[[Maughmer 1987][research_maughmer_1987]\] \[[McClain 2022][research_mcclain_2022]\] \[[McCormick 1959][research_mccormick_1959]\] \[[McCutchen 1989][research_mccutchen_1989]\] \[[McFadden et al 2022][research_mcfadden_brandt_2022]\] \[[McLellan and Cangelosi 1948][research_mclellan_cangelosi_1948]\] \[[Meheut et al 2012][research_meheut_arntz_2012]\] \[[Mehrotra and Lan 1978][research_mehrotra_lan_1978]\] \[[Mehrotra and Lan 1978][research_mehrotra_lan_1978_b]\] \[[Midmer and Bruecker 2024][research_midmer_bruecker_2024]\] \[[Mikhailov 2020][research_mikhailov_2020]\] \[[Miklosovic and Perry 2014][research_miklosovic_perry_2014]\] \[[Miller 1983][research_miller_1983]\] \[[Miller 1986][research_miller_1986]\] \[[Miller and Hadley 1983][research_miller_hadley_1983]\] \[[Modern Wing Shapes 1936][research_modern_wing_1936]\] \[[Moeller and Rediniotis 2000][research_moeller_rediniotis_2000]\] \[[Moeller and Rediniotis 2002][research_moeller_rediniotis_2002]\] \[[Moigne and Qin 2006][research_moigne_qin_2006]\] \[[Monfort and Whitcomb 1975][research_monfort_1975]\] \[[Monsch et al 2007][research_monsch_figliola_2007]\] \[[Moore 1965][research_moore_1965]\] \[[Moore and Frei 1983][research_moore_frei_1983]\] \[[Morehouse et al 1977][research_morehouse_1977]\] \[[Morton 1956][research_morton_1956]\] \[[Motycka and Skowronek 1967][research_motycka_skowronek_1967]\] \[[Mou-Jie 1979][research_moujie_1979]\] \[[Mouton et al 2026][research_mouton_charpentier_2026]\] \[[Muraoka et al 2009][research_muraoka_okada_2009]\] \[[Murphy et al 2004][research_murphy_klein_2004]\] \[[Naik and Ostowari 1987][research_naik_ostowari_1987]\] \[[Naik and Ostowari 1988][research_naik_ostowari_1988]\] \[[Naik and Ostowari 1990][research_naik_ostowari_1990]\] \[[Namura et al 2015][research_namura_shimoyama_2015]\] \[[Nangia et al 2003][research_nangia_palmer_2003]\] \[[nath and ana 2017][research_nath_ana_2017]\] \[[Navaratna and Pontillo 2022][research_navaratna_pontillo_2022]\] \[[Nee Chan et al 2018][research_neechan_yazdiharmin_2018]\] \[[Neely 1943][research_neely_1943]\] \[[Nelson 1992][research_nelson_1992]\] \[[Neves and Mariani 2024][research_neves_mariani_2024]\] \[[Newell and Marsh 1967][research_newell_marsh_1967]\] \[[Newey][research_newey]\] \[[Newman and Swaim 1986][research_newman_swaim_1986]\] \[[Ng et al 2003][research_ng_ray_2003]\] \[[Nicholas et al 1984][research_nicholas_naville_1984]\] \[[Nichols and Englar 1980][research_nicholsjr_englar_1980]\] \[[Nicks 1983][research_nicks_1983]\] \[[Niedling 1980][research_niedling_1980]\] \[[Nikolic 2006][research_nikolic_2006]\] \[[Nikolic 2007][research_nikolic_2007]\] \[[Nikolic 2008][research_nikolic_2008]\] \[[Nixon 2001][research_nixon_2001]\] \[[Nixon 2006][research_nixon_2006]\] \[[Nonweiler 1960][research_nonweiler_1960]\] \[[Nudson et al 2025][research_nudson_stanfieldbrown_2025]\] \[[Nugroho 2026][research_nugroho_2026]\] \[[Numerical investigation of aerodynamic 2023][research_numerical_investigation_2023]\] \[[Obayashi][research_obayashi]\] \[[Oggioni et al 2026][research_oggioni_riboldi_2026]\] \[[Oh and Tavella 1986][research_oh_tavella_1986]\] \[[Oland and Kristiansen 2013][research_oland_kristiansen_2013]\] \[[Olson and Dvorak 1976][research_olson_dvorak_1976]\] \[[Onofri et al 2026][research_onofri_antonini_2026]\] \[[Orloff 1978][research_orloff_1978]\] \[[Orloff and Ciffone 1974][research_orloff_ciffone_1974]\] \[[Ortamevzi 2015][research_ortamevzi_2015]\] \[[Oshima et al 2022][research_oshima_wygnanski_2022]\] \[[Otto and Streett 1994][research_otto_streett_1994]\] \[[Owens and Perkins 1996][research_owens_perkins_1996]\] \[[Pande 2025][research_pande_2025]\] \[[Pandi and Kumar 2025][research_pandi_kumar_2025]\] \[[Pao and Lan 1978][research_pao_lan_1978]\] \[[Papadakis et al 2003][research_papadakis_yeong_2003]\] \[[Papadakis et al 2004][research_papadakis_yeong_2004]\] \[[Paranjape and Chung 2010][research_paranjape_chung_2010]\] \[[Park et al 1996][research_park_matuda_1996]\] \[[Parsons 1958][research_parsons_1958]\] \[[Pasamanick and Sellers 1950][research_pasamanick_sellers_1950]\] \[[Pate 1964][research_pate_1964]\] \[[Patierno 1980][research_patierno_1980]\] \[[Patterson and Loving 1961][research_patterson_loving_1961]\] \[[Pattinson et al 2013][research_pattinson_lowenberg_2013_b]\] \[[Pearcey 1962][research_pearcey_1962]\] \[[Peck and Hudson 1956][research_peck_hudson_1956]\] \[[Perry and Miklosovic 2012][research_perry_miklosovic_2012]\] \[[Petrov 1993][research_petrov_1993]\] \[[Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]\] \[[Phillips et al 2006][research_phillips_fugal_2006]\] \[[Phillips et al 2019][research_phillips_wygnanski_2019]\] \[[Pogosyan 2025][research_pogosyan_2025]\] \[[Polhamus 1948][research_polhamus_1948]\] \[[Polhamus 1983][research_polhamus_1983]\] \[[Polhamus 1984][research_polhamus_1984]\] \[[Polidoro and Bhattacharya 2026][research_polidoro_bhattacharya_2026]\] \[[Popescu 1999][research_popescu_1999]\] \[[Potapczuk and Bidwell 1990][research_potapczuk_bidwell_1990]\] \[[Potapczuk and Bidwell 1991][research_potapczuk_bidwell_1991]\] \[[Potapczuk et al 2003][research_potapczuk_papadakis_2003]\] \[[Previati et al 2012][research_previati_gobbi_2012]\] \[[Prudenzano et al 2025][research_prudenzano_gand_2025]\] \[[Pugliese and Englar 1979][research_pugliese_englar_1979]\] \[[Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]\] \[[Putro et al 2025][research_putro_junipitoyo_2025]\] \[[Rajeswari and Prabhu 1987][research_rajeswari_prabhu_1987]\] \[[Ralson 1983][research_ralson_1983]\] \[[Ramprasadh and Devanandh 2015][research_ramprasadh_devanandh_2015]\] \[[Rao 1983][research_rao_1983]\] \[[Rao and Huffman 1978][research_rao_huffman_1978]\] \[[Recktenwald and Ahmed 2008][research_recktenwald_ahmed_2008]\] \[[Reddy 1981][research_reddy_1981]\] \[[Reddy and Ghaffari 1982][research_reddy_ghaffari_1982]\] \[[Reed 1984][research_reed_1984]\] \[[Reed 1985][research_reed_1985]\] \[[Reed 1987][research_reed_1987]\] \[[Reed 1991][research_reed_1991]\] \[[Report no. 257, Pressure 1927][research_report_no_1927]\] \[[Report No. 349. A 1930][research_report_no_1930]\] \[[Reubush 1977][research_reubush_1977]\] \[[Reubush 1978][research_reubush_1978]\] \[[Reubush 1979][research_reubush_1979]\] \[[Ribner 1960][research_ribner_1960]\] \[[Richardson 1976][research_richardson_1976]\] \[[Ricouard et al 2004][research_ricouard_davy_2004]\] \[[Riebe and Watson 1950][research_riebe_watson_1950]\] \[[Robb et al 2023][research_robb_vuppala_2023]\] \[[Robinson and Robinson 1980][research_robinson_robinson_1980]\] \[[Rosen and Rand 1985][research_rosen_rand_1985]\] \[[Rosin et al 2004][research_rosin_mattos_2004]\] \[[Ross 1984][research_ross_1984]\] \[[Ross and Matarazzo 1982][research_ross_matarazzo_1982]\] \[[Rudenko and Ryzhkova 1968][research_rudenko_ryzhkova_1968]\] \[[Rudolph 1998][research_rudolph_1998]\] \[[Runckel and Henderson 1952][research_runckel_henderson_1952]\] \[[Rusovici et al 2017][research_rusovici_haughey_2017]\] \[[Röntsch et al 2016][research_rontsch_taubert_2016]\] \[[S. Elangovan et al. 2019][research_selangovanetal_2019]\] \[[Sacks et al 1963][research_sacks_nielsen_1963]\] \[[Saelman 1964][research_saelman_1964]\] \[[Salem Said and Ragab 2008][research_salemsaid_ragab_2008]\] \[[San and Fei 2012][research_san_fei_2012]\] \[[Sanchez et al 2019][research_sanchez_escamilla_2019]\] \[[Sanders 1965][research_sanders_1965]\] \[[Sandhu et al 2018][research_sandhu_soltani_2018]\] \[[Santos and Mattos 2009][research_santos_mattos_2009]\] \[[Savage and Edwards 1959][research_savage_1959]\] \[[Sboev D 2024][research_sboevd_2024]\] \[[Schade 1948][research_schade_1948]\] \[[Schmidt and Duren 2002][research_schmidt_duren_2002]\] \[[Schuette et al 2018][research_schuette_vormweg_2018]\] \[[Schulderfrei et al 1951][research_schulderfrei_1951]\] \[[Schütte et al 2018][research_schutte_huber_2018]\] \[[Seacord and Campbell 1945][research_seacord_campbell_1945]\] \[[Sears 1974][research_sears_1974]\] \[[Sears 1980][research_sears_1980]\] \[[Sears 1990][research_sears_1990]\] \[[Sefcovic and Smith 2010][research_sefcovic_smith_2010]\] \[[Seidler et al 2023][research_seidler_huebner_2023]\] \[[Seitz et al 2011][research_seitz_kruse_2011]\] \[[Setyo Hariyadi et al 2021][research_setyohariyadi_sutardi_2021]\] \[[Sforza 2014][research_sforza_2014]\] \[[Shah and Ang 2025][research_shah_ang_2025]\] \[[Sharif et al 2022][research_sharif_abbas_2022]\] \[[Shcherbakov 1966][research_shcherbakov_1966]\] \[[Shen 2026][research_shen_2026]\] \[[Sherman 1937][research_sherman_1937]\] \[[Sibert 1943][research_sibert_1943]\] \[[Simpson and Jacob 2005][research_simpson_jacob_2005]\] \[[Siouris and Qin 2007][research_siouris_qin_2007]\] \[[Skomorokhov et al 2014][research_skomorokhov_nikolay_2014]\] \[[Smith 1990][research_smith_1990]\] \[[Smith and Schneider 1996][research_smith_schneider_1996]\] \[[Smith and Srokowski 1983][research_smith_srokowski_1983]\] \[[Smith et al 1987][research_smith_cliff_1987]\] \[[Smith et al 1990][research_smith_zell_1990]\] \[[Sobieczky et al 1987][research_sobieczky_hefer_1987]\] \[[Sohn and Chung 2006][research_sohn_chung_2006]\] \[[Sol and Vos 2016][research_sol_vos_2016]\] \[[Spacht 1980][research_spacht_1980]\] \[[Spearman and Comisarow 1948][research_spearman_comisarow_1948]\] \[[Spens and Bons 2022][research_spens_bons_2022]\] \[[Spens et al 2023][research_spens_mcfadden_2023]\] \[[Springer 1996][research_springer_1996]\] \[[Srigrarom and Kurosaka 2000][research_srigrarom_kurosaka_2000]\] \[[Srokowski and Orszag 1977][research_srokowski_orszag_1977]\] \[[Stark 1985][research_stark_1985]\] \[[Starn][research_starn]\] \[[Stebbins and Loth 2023][research_stebbins_loth_2023]\] \[[Stebbins et al 2019][research_stebbins_loth_2019]\] \[[Stephen 1995][research_stephen_1995]\] \[[Stewart and Paulson 1984][research_stewart_paulsonjr_1984]\] \[[Stringfield 1984][research_stringfield_1984]\] \[[Subramanian 2026][research_subramanian_2026]\] \[[Sugimoto 1992][research_sugimoto_1992]\] \[[Sundaram et al 1999][research_sundaram_viswanath_1999]\] \[[Svoboda and Rozehnal 2015][research_svoboda_rozehnal_2015]\] \[[Syverud et al 1993][research_syverud_farokhi_1993]\] \[[Szmelter 1999][research_szmelter_1999]\] \[[Szodruch 1991][research_szodruch_1991]\] \[[Szodruch and Hilbig 1988][research_szodruch_hilbig_1988]\] \[[Tagai et al 2016][research_tagai_nakakita_2016]\] \[[Tai 1991][research_tai_1991]\] \[[Taira et al 2010][research_taira_rowley_2010]\] \[[Takahashi et al 2014][research_takahashi_dulin_2014]\] \[[Tan][research_tan]\] \[[Taufik and Qasem 2025][research_taufik_qasem_2025]\] \[[Taylor 1952][research_taylor_1952]\] \[[Taylor 1953][research_taylor_1953]\] \[[Taylor et al 1982][research_taylor_jackson_1982]\] \[[Telionis 1990][research_telionis_1990]\] \[[Telionis and Vlachos 2003][research_telionis_vlachos_2003]\] \[[Tewes and Taubert 2015][research_tewes_taubert_2015]\] \[[The stability of two-phase 1997][research_the_stability_1997]\] \[[The sweep angle effect 2018][research_the_sweep_angle_2018]\] \[[The Swept - Wing 2021][research_the_swept_2021]\] \[[The Tapered Wing Again 1937][research_the_tapered_1937]\] \[[Thompson 1965][research_thompson_1965]\] \[[Three-Dimensional Wing Synthesis 2014][research_three_dimensional_wing_2014]\] \[[Thurber 1965][research_thurber_1965]\] \[[Tiniakov and Limtrakul 2026][research_tiniakov_2026]\] \[[Todorov 2015][research_todorov_2015]\] \[[Toll and Queijo 1948][research_toll_queijo_1948]\] \[[Torenbeek 1976][research_torenbeek_1976]\] \[[Torenbeek 1982][research_torenbeek_1982]\] \[[Tormalm et al 2018][research_tormalm_leroy_2018]\] \[[Toyoda et al 2015][research_toyoda_kwak_2015]\] \[[Traub 1994][research_traub_1994]\] \[[Traub 1995][research_traub_1995]\] \[[Traub 1997][research_traub_1997]\] \[[Traub 1997][research_traub_1997_b]\] \[[Traub 2009][research_traub_2009]\] \[[Traub 2021][research_traub_2021]\] \[[Traub 2023][research_traub_2023]\] \[[Traub and Campbell 2019][research_traub_campbell_2019]\] \[[Traub and Chandrashekar 2016][research_traub_chandrashekar_2016]\] \[[Traub et al 1999][research_traub_galls_1999]\] \[[Trussa et al 2021][research_trussa_whitfield_2021]\] \[[Trussa et al 2022][research_trussa_whitfield_2022]\] \[[Trussa et al 2026][research_trussa_whitfield_2026]\] \[[Tsao et al 2009][research_tsao_vargas_2009]\] \[[Tufts et al 2013][research_tufts_reed_2013]\] \[[Tufts et al 2014][research_tufts_reed_2014]\] \[[Tzong et al 1992][research_tzong_sikes_1992]\] \[[Udin and Anderson 1992][research_udin_anderson_1992]\] \[[Use of Aerodynamic Forces 2022][research_use_of_2022]\] \[[Uzun et al 2023][research_uzun_bilgic_2023]\] \[[van Dam 1985][research_vandam_1985]\] \[[Van Dam 1986][research_vandam_1986]\] \[[Van Dam et al 1990][research_vandam_vijgen_1990]\] \[[van Es 2002][research_vanes_2002]\] \[[Vargas 2007][research_vargas_2007]\] \[[Vargas and Kreeger 2009][research_vargas_kreeger_2009]\] \[[Vargas et al 2002][research_vargas_ratvasky_2002]\] \[[Vatandas 2010][research_vatandas_2010]\] \[[Veerman et al 2013][research_veerman_kannemans_2013]\] \[[Velkova and Todorov 2015][research_velkova_todorov_2015]\] \[[Venkatakrishnan et al 2006][research_venkatakrishnan_sundaram_2006]\] \[[Visonneau et al 2022][research_visonneau_guilmineau_2022]\] \[[Vogeltanz 2016][research_vogeltanz_2016]\] \[[Vogler 1976][research_vogler_1976]\] \[[Von Glahn and Groesbeck 1976][research_vonglahn_groesbeck_1976]\] \[[Vos and Farokhi 2015][research_vos_farokhi_2015]\] \[[Waggoner and Allison 1987][research_waggoner_allison_1987]\] \[[Wakayama and Kroo 1995][research_wakayama_kroo_1995]\] \[[Wakimoto et al 2021][research_wakimoto_chiba_2021]\] \[[Walker et al 2016][research_walker_hipp_2016]\] \[[Wallace 1952][research_wallace_1952]\] \[[Wallis et al 1982][research_wallis_ellis_1982]\] \[[Wan 2024][research_wan_2024]\] \[[Wang 2024][research_wang_2024_b]\] \[[Wang and Zha 2019][research_wang_zha_2019]\] \[[Wang et al 2013][research_wang_bai_2013]\] \[[Wang et al 2025][research_wang_sun_2025]\] \[[Watanabe et al 2021][research_watanabe_sunada_2021]\] \[[Weber 1990][research_weber_1990]\] \[[Wei et al 2019][research_wei_new_2019]\] \[[Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]\] \[[Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]\] \[[Wells and Olson 2011][research_wells_olson_2011]\] \[[Wenzinger and Harris 1931][research_wenzinger_harris_1931]\] \[[White et al 2015][research_white_kapania_2015]\] \[[Whittle and Lipson 1953][research_whittle_lipson_1953]\] \[[Wieszala et al 2022][research_wieszala_kolodziej_2022]\] \[[Wildschek 2014][research_wildschek_2014]\] \[[Wind Tunnel Test to 2004][research_wind_tunnel_2004]\] \[[Wing Design 2012][research_wing_design_2012]\] \[[Wing Design 2025][research_wing_design_2025]\] \[[Wing Design Considerations 2021][research_wing_design_2021]\] \[[Wing Shapes and Nomenclature 2022][research_wing_shapes_2022]\] \[[Wing tunnel model for 1998][research_wing_tunnel_1998]\] \[[Wings 2017][research_wings_2017]\] \[[Winski et al 2025][research_winski_langston_2025]\] \[[Wolkovitch 1984][research_wolkovitch_1984]\] \[[Wong and va 1995][research_wong_va_1995]\] \[[Woodard and Bragg 2020][research_woodard_bragg_2020]\] \[[Woods and Spooner 1948][research_woods_spooner_1948]\] \[[Wortman 1999][research_wortman_1999]\] \[[Xiaolong He et al 2017][research_xiaolonghe_junqiangbai_2017]\] \[[Xinbing et al 2019][research_xinbing_wen_2019]\] \[[Xinbing et al 2020][research_xinbing_wen_2020]\] \[[Xu and Amano 2004][research_xu_amano_2004]\] \[[Xu et al 2025][research_xu_zhang_2025]\] \[[Xu et al 2026][research_xu_lessis_2026]\] \[[Yajnik and Subbaiah 1976][research_yajnik_subbaiah_1976]\] \[[Yamamoto 1992][research_yamamoto_1992]\] \[[Yan et al 2025][research_yan_mccrink_2025]\] \[[Yang and Przekwas 1993][research_yang_przekwas_1993_b]\] \[[Yen 2011][research_yen_2011]\] \[[Yen and Huang 2011][research_yen_huang_2011]\] \[[Yen et al 2013][research_yen_san_2013]\] \[[Yildirim and Tuncer 2021][research_yildirim_tuncer_2021]\] \[[Yip and Shubert 1977][research_yip_shubert_1977]\] \[[Yip et al 1992][research_yip_vijgen_1992]\] \[[Yip et al 1993][research_yip_vijgen_1993]\] \[[Yoshida et al 2021][research_yoshida_bragg_2021]\] \[[Yukish and Valenti 2020][research_yukish_valenti_2020]\] \[[Zeiger et al 2002][research_zeiger_gerlach_2002]\] \[[Zhang and Taira 2022][research_zhang_taira_2022]\] \[[Zhang et al 2013][research_zhang_yu_2013]\] \[[Zhang et al 2020][research_zhang_yan_2020]\] \[[Zhang et al 2024][research_zhang_zhang_2024]\] \[[Zhou 2018][research_zhou_2018]\]

### Morphing aircraft and the sweep transient

**Variable geometry at small scale.** Camber, span, twist, folding and sweep morphing, the actuators and compliant structures that produce them, and the control of a vehicle while its shape changes. **This literature belongs to the present century.** Of its 654 dated records, 640 were published in 2000 or later.

**664 records.** \[[Abdessemed et al 2018][research_abdessemed_yao_2018]\] \[[Abdulrahim 2005][research_abdulrahim_2005]\] \[[Abou Khalil][research_aboukhalil]\] \[[Aerodynamic characteristics of telescopic 2018][research_aerodynamic_characteristics_of_2018]\] \[[Aguirrebeitia et al 2012][research_aguirrebeitia_aviles_2012]\] \[[Ahmad et al 2024][research_ahmad_gour_2024]\] \[[Ai and Weaver 2017][research_ai_weaver_2017]\] \[[Ajaj and Jankee 2018][research_ajaj_jankee_2018]\] \[[Ajaj et al 2013][research_ajaj_saavedraflores_2013]\] \[[Ajaj et al 2016][research_ajaj_friswell_2016]\] \[[Allen and Bridges 2003][research_allen_bridges_2003]\] \[[Alsaidi et al 2019][research_alsaidi_joe_2019]\] \[[Alulema et al 2020][research_alulema_valencia_2020]\] \[[Alulema et al 2025][research_alulema_2025]\] \[[Ameduri et al 2025][research_ameduri_2025]\] \[[Amendola et al 2018][research_amendola_dimino_2018]\] \[[Ameri et al 2007][research_ameri_lowenberg_2007]\] \[[Ameri et al 2008][research_ameri_lowenberg_2008]\] \[[Andersen et al 2007][research_andersen_cowan_2007]\] \[[Application Status and Future 2023][research_application_status_2023]\] \[[Apuleo 2018][research_apuleo_2018]\] \[[Arena et al 2018][research_arena_amoroso_2018]\] \[[Arunkumar et al 2023][research_arunkumar_sravanthi_2023]\] \[[Assessment of variable camber 1980][research_assessment_of_1980]\] \[[Ataei-Esfahani and Qian Wang 2006][research_ataeiesfahani_qianwang_2006]\] \[[August et al 2026][research_august_kopsaftopoulos_2026]\] \[[Badihi et al 2026][research_badihi_2026]\] \[[Bae et al 2004][research_bae_seigler_2004]\] \[[Bae et al 2005][research_bae_seigler_2005]\] \[[Bai et al 2020][research_bai_xing_2020]\] \[[Bai et al 2025][research_bai_li_2025]\] \[[Bajer et al 2025][research_bajer_hrstka_2025]\] \[[Balon et al 2021][research_balon_benes_2021]\] \[[Bartels et al 2019][research_bartels_stanford_2019]\] \[[Bashir and Rajendran 2018][research_bashir_rajendran_2018]\] \[[Battaglia and Riccio 2026][research_battaglia_riccio_2026]\] \[[Beatty et al 1977][research_beatty_brooks_1977]\] \[[Beaverstock et al 2015][research_beaverstock_woods_2015]\] \[[Bilgen et al 2007][research_bilgen_kochersberger_2007]\] \[[Bin Bai and Chaoyang Dong 2013][research_binbai_chaoyangdong_2013]\] \[[Bing and Wei 2024][research_bing_wei_2024]\] \[[Birk and Smith 1986][research_birk_smith_1986]\] \[[Bishay et al 2019][research_bishay_2019]\] \[[Blondeau and Pines 2004][research_blondeau_pines_2004]\] \[[Boltz and Pena 1977][research_boltz_pena_1977]\] \[[Boothe et al 2005][research_boothe_fitzpatrick_2005]\] \[[Bosak et al 2026][research_bosak_eric_2026]\] \[[Boskovic and Redding 2009][research_boskovic_redding_2009]\] \[[Boston and Arrieta 2021][research_boston_arrieta_2021]\] \[[Boston et al 2022][research_boston_phillips_2022]\] \[[Botez et al 2011][research_botez_grigorie_2011]\] \[[Botez et al 2015][research_botez_kammegne_2015]\] \[[Boughou et al 2025][research_boughou_batistic_2025]\] \[[Bourdin et al 2006][research_bourdin_gatto_2006]\] \[[Bourdin et al 2007][research_bourdin_gatto_2007]\] \[[Bowman 2003][research_bowman_2003]\] \[[Bowman et al 2002][research_bowman_sanders_2002]\] \[[Bowman et al 2007][research_bowman_sanders_2007]\] \[[Bradley et al 2026][research_bradley_haughn_2026]\] \[[Burdette and Martins][research_burdette_martins]\] \[[Burke and Gatto 2025][research_burke_gatto_2025]\] \[[Burke and Gatto 2026][research_burke_2026]\] \[[Cai et al 2022][research_cai_yang_2022]\] \[[Cai et al 2024][research_cai_su_2024]\] \[[Cai et al 2026][research_cai_zheng_2026]\] \[[Cao and Lyu 2024][research_cao_lyu_2024]\] \[[Cao et al 2025][research_cao_lin_2025]\] \[[Cardoso et al 2013][research_cardoso_suleman_2013]\] \[[Carrillo Córcoles et al 2023][research_carrillocorcoles_mertens_2023]\] \[[Castillo Acero et al 2018][research_castilloacero_delaescalera_2018]\] \[[Castrichini et al 2016][research_castrichini_hodigeresiddaramaiah_2016]\] \[[Cavalieri et al 2024][research_cavalieri_degaspari_2024]\] \[[Cen et al 2025][research_cen_xu_2025]\] \[[Cen et al 2026][research_cen_xu_2026]\] \[[Cetinsoy 2015][research_cetinsoy_2015]\] \[[Changchuan et al 2022][research_changchuan_2022]\] \[[Che and Wu 2026][research_che_wu_2026]\] \[[Chellangi et al 2025][research_chellangi_santhanam_2025]\] \[[Chen 2010][research_chen_2010]\] \[[Chen et al 2016][research_chen_guo_2016]\] \[[Cheng et al 2017][research_cheng_dong_2017]\] \[[Cheng et al 2017][research_cheng_dong_2017_b]\] \[[Cheng et al 2023][research_cheng_li_2023]\] \[[Cheng et al 2025][research_cheng_song_2025]\] \[[Cheng et al 2025][research_cheng_zhang_2025]\] \[[Cheung et al 2019][research_cheung_rezgui_2019]\] \[[Cheung et al 2020][research_cheung_folding_2020]\] \[[Clements and Djidjeli 2024][research_clements_djidjeli_2024]\] \[[Coban 2020][research_coban_2020]\] \[[Cooper 2023][research_cooper_2023]\] \[[Courchesne et al 2010][research_courchesne_popov_2010]\] \[[Coutu et al 2009][research_coutu_brailovski_2009]\] \[[Coutu et al 2011][research_coutu_brailovski_2011]\] \[[Crossley 2005][research_crossley_2005]\] \[[Crossley and Cook 2001][research_crossley_cook_2001]\] \[[Crossley et al 2011][research_crossley_skillen_2011]\] \[[Cui et al 2026][research_cui_2026]\] \[[Cuji and Garcia 2008][research_cuji_garcia_2008]\] \[[Dai et al 2020][research_dai_yan_2020]\] \[[De 2020][research_de_2020]\] \[[De Breuker et al 2007][research_debreuker_abdalla_2007]\] \[[De Gaspari and Ricci 2015][research_degaspari_ricci_2015]\] \[[De Gaspari et al 2018][research_degaspari_riccobene_2018]\] \[[Decamp and Hardy 1984][research_decamp_hardy_1984]\] \[[Delplanche et al 2026][research_delplanche_greil_2026]\] \[[Dimino et al 2014][research_dimino_flauto_2014]\] \[[Dimino et al 2015][research_dimino_ciminello_2015]\] \[[Dimino et al 2016][research_dimino_diodati_2016]\] \[[Dimino et al 2018][research_dimino_amendola_2018]\] \[[Dimino et al 2019][research_dimino_gallorini_2019]\] \[[DiPalma and Gandhi 2016][research_dipalma_gandhi_2016]\] \[[do Vale et al 2018][research_dovale_afonso_2018]\] \[[Donati et al 2026][research_donati_pacheco_2026]\] \[[Dong and Sun 2011][research_dong_sun_2011]\] \[[Dong et al 2013][research_dong_li_2013]\] \[[Dong et al 2018][research_dong_zhang_2018]\] \[[Dove-Jay 2014][research_dovejay_2014]\] \[[Dumont 2018][research_dumont_2018]\] \[[Durmuş and Kaya 2021][research_durmus_kaya_2021]\] \[[Durmuş and Kaya 2023][research_durmus_kaya_2023]\] \[[Dussart et al 2018][research_dussart_yusuf_2018]\] \[[Dussart et al 2019][research_dussart_roll_2019]\] \[[Dussart et al 2019][research_dussart_xb70_2019]\] \[[Akoury et al 2026][research_elakoury_aboukhalil_2026]\] \[[El-Salamony and Aziz 2020][research_elsalamony_aziz_2020]\] \[[Elelwi et al 2020][research_elelwi_span_2020]\] \[[Elelwi et al 2021][research_elelwi_calvet_2021]\] \[[Elelwi et al 2021][research_elelwi_topology_2021]\] \[[Elelwi et al 2022][research_elelwi_weight_2022]\] \[[Elsloo et al 2025][research_elsloo_rooij_2025]\] \[[Eraslan and Oktay 2023][research_eraslan_oktay_2023]\] \[[Eraslan and Oktay 2024][research_eraslan_oktay_2024]\] \[[Fan et al 2025][research_fan_wu_2025]\] \[[Fasel 2020][research_fasel_2020]\] \[[Felício et al 2011][research_felicio_santos_2011]\] \[[Feng et al 2023][research_feng_guo_2023]\] \[[Feng et al 2025][research_feng_2025]\] \[[Fichera et al 2019][research_fichera_isnardi_2019]\] \[[Finistauri 2021][research_finistauri_2021]\] \[[Finistauri et al 2011][research_finistauri_xi_2011]\] \[[Finistauri et al 2012][research_finistauri_xi_2012]\] \[[Flanagan et al 2007][research_flanagan_strutzenberg_2007]\] \[[Fonte et al 2018][research_fonte_iannaccone_2018]\] \[[Friswell 2014][research_friswell_2014]\] \[[Fu and Sun 2025][research_fu_sun_2025]\] \[[Fujiwara et al 2018][research_fujiwara_nguyen_2018]\] \[[Gabor et al 2013][research_gabor_koreanschi_2013]\] \[[Gabor et al 2016][research_gabor_koreanschi_2016]\] \[[Gamble and Inman 2016][research_gamble_inman_2016]\] \[[Gamboa and Santos 2016][research_gamboa_santos_2016]\] \[[Gandhi et al 2007][research_gandhi_jha_2007]\] \[[Gandhi et al 2009][research_gandhi_cooper_2009]\] \[[Ganesh et al 2022][research_ganesh_paul_2022]\] \[[Gang Tao et al][research_gangtao_shuhaochen]\] \[[Gano and Renaud 2002][research_gano_renaud_2002]\] \[[Gano et al 2004][research_gano_perez_2004]\] \[[Gao et al 2015][research_gao_zhao_2015]\] \[[Gao et al 2016][research_gao_kang_2016]\] \[[Gao et al 2023][research_gao_pabon_2023]\] \[[Gao et al 2026][research_gao_tian_2026]\] \[[Garcia et al 2003][research_garcia_abdulrahim_2003]\] \[[Geva et al 2019][research_geva_2019]\] \[[Ghanem et al 2023][research_ghanem_bicer_2023]\] \[[Gilani 2023][research_gilani_2023]\] \[[Gilbert 1980][research_gilbert_1980]\] \[[Gilbert 1981][research_gilbert_1981]\] \[[Gong and Ma 2019][research_gong_ma_2019_b]\] \[[Gong et al 2019][research_gong_wang_2019]\] \[[Gong et al 2019][research_gong_wang_2019_b]\] \[[Gong et al 2020][research_gong_wang_2020]\] \[[Grant and Lind 2010][research_grant_lind_2010]\] \[[Grant et al 2006][research_grant_abdulrahim_2006]\] \[[Grant et al 2009][research_grant_chakravarthy_2009]\] \[[Grant et al 2010][research_grant_abdulrahim_2010]\] \[[Grant et al 2012][research_grant_sorley_2012]\] \[[Green and Ott 2003][research_green_ott_2003]\] \[[Green and Ott 2005][research_green_ott_2005]\] \[[Greff 1990][research_greff_1990]\] \[[Griffin][research_griffin]\] \[[Grigorie and Botez 2014][research_grigorie_botez_2014]\] \[[Grigorie and Botez 2018][research_grigorie_botez_2018]\] \[[Grigorie and Botez 2023][research_grigorie_botez_2023]\] \[[Grigorie et al 2009][research_grigorie_botez_2009]\] \[[Grigorie et al 2011][research_grigorie_botez_2011]\] \[[Grigorie et al 2011][research_grigorie_popov_2011]\] \[[Grigorie et al 2011][research_grigorie_popov_2011_b]\] \[[Grigorie et al 2012][research_grigorie_botez_2012]\] \[[Grigorie et al 2012][research_grigorie_popov_2012]\] \[[Grogorie et al 2013][research_grogorie_popov_2013]\] \[[Groves-Raines et al 2026][research_grovesraines_watkins_2026]\] \[[Gu and Hong 2020][research_gu_hong_2020]\] \[[Gu et al 2022][research_gu_healy_2022]\] \[[Guiler][research_guiler]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]\] \[[Gunduz 2025][research_gunduz_2025]\] \[[Guo et al 2017][research_guo_bai_2017]\] \[[Guo et al 2025][research_guo_wang_2025]\] \[[Gupta 2012][research_gupta_2012]\] \[[Gupta et al 2025][research_gupta_kim_2025]\] \[[Haider et al 2023][research_haider_ajaj_2023]\] \[[Han 2016][research_han_2016]\] \[[Han 2016][research_han_2016_b]\] \[[Han et al 2007][research_han_lee_2007]\] \[[He and Guo 2012][research_he_guo_2012]\] \[[He et al 2015][research_he_yin_2015]\] \[[He et al 2015][research_he_zhang_2015]\] \[[He et al 2017][research_he_li_2017]\] \[[Heeb and Woods 2024][research_heeb_woods_2024]\] \[[Henry and Pines 2007][research_henry_pines_2007]\] \[[Henry et al 2017][research_henry_molinari_2017]\] \[[Henry et al 2019][research_henry_molinari_2019]\] \[[Heredia and Ollero 2010][research_heredia_ollero_2010]\] \[[Herencia et al 2007][research_herencia_weaver_2007]\] \[[Hintz et al 2014][research_hintz_torno_2014]\] \[[Hodson et al 2017][research_hodson_hunsaker_2017]\] \[[Hossain et al 2020][research_hossain_wang_2020]\] \[[Hu][research_hu]\] \[[Hu et al 2016][research_hu_yang_2016]\] \[[Hu et al 2023][research_hu_ge_2023]\] \[[Hu et al 2025][research_hu_2025]\] \[[Hua et al 2025][research_hua_2025]\] \[[Huang and Qiu 2013][research_huang_qiu_2013_b]\] \[[Huang et al 2013][research_huang_qiu_2013]\] \[[Huang et al 2018][research_huang_yang_2018]\] \[[Huang et al 2020][research_huang_fu_2020]\] \[[Huang et al 2021][research_huang_fu_2021]\] \[[Huang et al 2021][research_huang_fu_2021_b]\] \[[Huang et al 2023][research_huang_guo_2023]\] \[[Huang et al 2023][research_huang_liu_2023]\] \[[Huebsch et al 2012][research_huebsch_hamburg_2012]\] \[[Hui and Chen 2023][research_hui_chen_2023]\] \[[Hurst et al 2009][research_hurst_wickenheiser_2009]\] \[[Iannuzzo et al 2018][research_iannuzzo_russo_2018]\] \[[Inoyama et al 2007][research_inoyama_sanders_2007]\] \[[Inoyama et al 2008][research_inoyama_sanders_2008]\] \[[Islam et al 2025][research_islam_rahman_2025]\] \[[Ivanco et al 2007][research_ivanco_scott_2007]\] \[[Jackuliak and Bugaj 2022][research_jackuliak_bugaj_2022]\] \[[Jasa et al 2018][research_jasa_hwang_2018]\] \[[Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]\] \[[Jeong and Bae 2022][research_jeong_bae_2022]\] \[[Jiang and Yang 2026][research_jiang_yang_2026]\] \[[Jiang et al 2015][research_jiang_dong_2015]\] \[[Jiang et al 2020][research_jiang_wu_2020]\] \[[Jie 2018][research_jie_2018]\] \[[Jo and Majid 2023][research_jo_majid_2023]\] \[[Jo et al 2016][research_jo_choi_2016]\] \[[Jones and Cohen 2011][research_jones_cohen_2011]\] \[[Joo et al 2006][research_joo_sanders_2006]\] \[[Joseph et al 2020][research_joseph_golubev_2020]\] \[[Joseph et al 2021][research_joseph_adamski_2021]\] \[[Joshi et al 2004][research_joshi_tidwell_2004]\] \[[Joshi et al 2020][research_joshi_vazquez_2020]\] \[[Joshi et al 2026][research_joshi_2026]\] \[[Joshua and Adams 2006][research_joshua_adams_2006]\] \[[Jouannet et al 2009][research_jouannet_lundstrom_2009]\] \[[Jung and Kim 2013][research_jung_kim_2013]\] \[[Jung and Kim 2022][research_jung_kim_2022]\] \[[Kabir et al 2023][research_kabir_alobaidi_2023]\] \[[Kalaji 2023][research_kalaji_2023]\] \[[Kambayashi and Kogiso 2025][research_kambayashi_2025]\] \[[Kammegne and Botez 2019][research_kammegne_botez_2019]\] \[[Kammegne et al 2016][research_kammegne_botez_2016]\] \[[Kang et al 2026][research_kang_2026]\] \[[Kang et al 2026][research_kang_2026_2]\] \[[Kang et al 2026][research_kang_lu_2026]\] \[[Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]\] \[[Karow 2026][research_karow_2026]\] \[[Karpel et al 2008][research_karpel_selitrennik_2008]\] \[[Kaul and Nguyen 2017][research_kaul_nguyen_2017]\] \[[Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]\] \[[Keidel et al 2019][research_keidel_fasel_2019]\] \[[Keidel et al 2020][research_keidel_2020]\] \[[Khan 2008][research_khan_2008]\] \[[Khan et al 2019][research_khan_grigorie_2019]\] \[[Kim et al 2013][research_kim_lee_2013]\] \[[Kim et al 2020][research_kim_lee_2020]\] \[[Kim et al 2024][research_kim_kang_2024]\] \[[Klimczyk and Goraj 2019][research_klimczyk_2019]\] \[[Komp et al 2024][research_komp_hajek_2024]\] \[[Krishna 2021][research_krishna_2021]\] \[[Krishnamurthi and Gandhi 2016][research_krishnamurthi_gandhi_2016]\] \[[Kumar et al 2021][research_kumar_topology_2021]\] \[[Kumar et al 2026][research_kumar_mathi_2026]\] \[[Kumkam et al 2025][research_kumkam_suratemeekul_2025]\] \[[Kwong 2021][research_kwong_2021]\] \[[La et al 2018][research_la_joe_2018]\] \[[Laxman Hattalli and Srivatsa 2018][research_laxmanhattalli_srivatsa_2018]\] \[[Lebofsky et al 2014][research_lebofsky_ting_2014]\] \[[Lebofsky et al 2015][research_lebofsky_ting_2015]\] \[[Lee and Lee 2023][research_lee_lee_2023]\] \[[Lee et al 2019][research_lee_kim_2019]\] \[[Lee et al 2020][research_lee_kim_2020]\] \[[Lee et al 2020][research_lee_kim_2020_b]\] \[[Lego and Altman 2013][research_lego_altman_2013]\] \[[Lendraitis and Lukosevicius 2025][research_lendraitis_2025]\] \[[Leonard et al 2023][research_leonard_prasetiyo_2023]\] \[[Leylek and Costello 2010][research_leylek_costello_2010]\] \[[Li and Jin 2018][research_li_jin_2018]\] \[[Li and Liu 2024][research_li_liu_2024]\] \[[Li et al 2012][research_li_guo_2012]\] \[[Li et al 2012][research_li_guo_2012_b]\] \[[Li et al 2016][research_li_guo_2016]\] \[[Li et al 2016][research_li_guo_2016_b]\] \[[Li et al 2019][research_li_qian_2019]\] \[[Li et al 2024][research_li_zhang_2024]\] \[[Li et al 2025][research_li_2025]\] \[[Li et al 2025][research_li_2025_2]\] \[[Li et al 2025][research_li_li_2025]\] \[[Li et al 2025][research_li_wang_2025]\] \[[Liang et al 2021][research_liang_wang_2021]\] \[[Lin et al 2022][research_lin_song_2022]\] \[[Lindner 2006][research_lindner_2006]\] \[[Liu and Zhang 2013][research_liu_zhang_2013]\] \[[Liu et al 2012][research_liu_li_2012]\] \[[Liu et al 2019][research_liu_yan_2019]\] \[[Liu et al 2020][research_liu_gao_2020]\] \[[Liu et al 2020][research_liu_shan_2020]\] \[[Liu et al 2022][research_liu_bai_2022]\] \[[Liu et al 2022][research_liu_shan_2022]\] \[[Liu et al 2026][research_liu_2026_2]\] \[[Liu et al 2026][research_liu_fan_2026]\] \[[Liu et al 2026][research_liu_qian_2026]\] \[[Livne et al 2014][research_livne_precup_2014]\] \[[Love et al 2004][research_love_zink_2004]\] \[[Lu et al 2025][research_lu_lin_2025]\] \[[Lucian et al 2012][research_lucian_mihaela_2012]\] \[[Lyu and Martins 2014][research_lyu_martins_2014]\] \[[Lyu and Martins 2015][research_lyu_martins_2015]\] \[[Ma et al 2023][research_ma_hui_2023]\] \[[Ma et al 2023][research_ma_liu_2023]\] \[[Ma et al 2024][research_ma_zhou_2024]\] \[[Madhan Kumar. G et al. 2019][research_madhankumargetal_2019]\] \[[Mahmood et al 2022][research_mahmood_hashemi_2022]\] \[[Majji et al 2007][research_majji_rediniotis_2007]\] \[[Maki 2016][research_maki_2016]\] \[[Manu et al 2026][research_manu_2026]\] \[[Manzo and Garcia 2010][research_manzo_garcia_2010]\] \[[Mao et al 2019][research_mao_xie_2019]\] \[[Mardanpour and Hodges 2013][research_mardanpour_hodges_2013]\] \[[Mardanpour and Hodges 2013][research_mardanpour_hodges_2013_b]\] \[[Mardanpour and Hodges 2014][research_mardanpour_hodges_2014]\] \[[Mares and Suresh Babu 2026][research_mares_sureshbabu_2026]\] \[[Marouf et al 2023][research_marouf_hoarau_2023]\] \[[Martin and Crossley 2002][research_martin_crossley_2002]\] \[[Martins 2016][research_martins_2016]\] \[[Mehndiratta et al 2026][research_mehndiratta_malhotra_2026]\] \[[Mehta et al 2008][research_mehta_frecker_2008]\] \[[Meng et al 2024][research_meng_wang_2024]\] \[[Mennu et al 2022][research_mennu_tran_2022]\] \[[Menon et al 2018][research_menon_chakravarthy_2018]\] \[[Mestrinho et al 2011][research_mestrinho_gamboa_2011]\] \[[Michaud et al 2018][research_michaud_dalir_2018]\] \[[Mir et al 2018][research_mir_maqsood_2018]\] \[[Mishriky and Walsh 2021][research_mishriky_walsh_2021]\] \[[Mishriky and Walsh 2023][research_mishriky_walsh_2023]\] \[[Mitashova 2022][research_mitashova_2022]\] \[[Mkhoyan et al 2020][research_mkhoyan_thakrar_2020]\] \[[Mkhoyan et al 2021][research_mkhoyan_thakrar_2021]\] \[[Mkhoyan et al 2022][research_mkhoyan_thakrar_2022]\] \[[Mo et al 2019][research_mo_kim_2019]\] \[[Moens 2019][research_moens_2019]\] \[[Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]\] \[[Montgomery et al 2019][research_montgomery_hunsaker_2019]\] \[[Moored and Bart-Smith 2005][research_moored_bartsmith_2005]\] \[[Moosavi 2025][research_moosavi_2025]\] \[[Moosavi and Elasha 2022][research_moosavi_elasha_2022]\] \[[Moosavian et al 2013][research_moosavian_xi_2013]\] \[[Morphing WING REAL TIME 2010][research_morphing_wing_2010]\] \[[Morphing Wing Technologies 2018][research_morphing_wing_2018]\] \[[Muhammad Umer et al 2020][research_muhammadumer_maqsood_2020]\] \[[Mukhtar 2023][research_mukhtar_2023]\] \[[Nagel et al 2015][research_nagel_fiedler_2015]\] \[[Nakamura et al 2017][research_nakamura_uehara_2017]\] \[[Nakhla and Elruby 2021][research_nakhla_elruby_2021]\] \[[Namdeo et al 2023][research_namdeo_bhattacharyya_2023]\] \[[Nazeer et al 2021][research_nazeer_2021]\] \[[Negahban et al 2025][research_negahban_hallonet_2025]\] \[[Negahban et al 2025][research_negahban_saci_2025]\] \[[Nguyen et al 2013][research_nguyen_ting_2013]\] \[[Nguyen et al 2014][research_nguyen_livne_2014]\] \[[Nguyen et al 2014][research_nguyen_ting_2014]\] \[[Ni et al 2015][research_ni_hou_2015]\] \[[Nigam et al 2020][research_nigam_tang_2020]\] \[[Nobleheart et al 2012][research_nobleheart_l_2012]\] \[[Nobleheart et al 2013][research_nobleheart_shivanapuralakshmikanth_2013]\] \[[Noviello et al 2016][research_noviello_rea_2016]\] \[[Noviello et al 2019][research_noviello_dimino_2019]\] \[[O'Grady et al 2009][research_ogrady_reich_2009]\] \[[Obradovic and Subbarao 2009][research_obradovic_subbarao_2009]\] \[[Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]\] \[[Obradovic and Subbarao 2011][research_obradovic_subbarao_2011]\] \[[Obradovic and Subbarao 2011][research_obradovic_subbarao_2011_b]\] \[[Obradovic and Subbarao 2011][research_obradovic_subbarao_2011_c]\] \[[Obradovic and Subbarao 2012][research_obradovic_subbarao_2012]\] \[[Oktay and Eraslan 2022][research_oktay_eraslan_2022]\] \[[Oktay and Eraslan 2024][research_oktay_eraslan_2024]\] \[[Oktay and Sultan 2014][research_oktay_sultan_2014]\] \[[Oktay and Özen 2022][research_oktay_ozen_2022]\] \[[Olivett et al 2020][research_olivett_corrao_2020]\] \[[Olivett et al 2021][research_olivett_corrao_2021]\] \[[Ortiz and Alley 2018][research_ortiz_alley_2018]\] \[[Ozbek et al 2023][research_ozbek_ekici_2023]\] \[[Ozbek et al 2024][research_ozbek_ekici_2024]\] \[[Pagano 2018][research_pagano_2018]\] \[[Pamnani and Jeughale 2021][research_pamnani_jeughale_2021]\] \[[Pamnani and Jeughale 2021][research_pamnani_jeughale_2021_b]\] \[[Paudel 2021][research_paudel_2021]\] \[[Pecora 2018][research_pecora_2018]\] \[[Pecora 2021][research_pecora_2021]\] \[[Pecora and Pecora 2018][research_pecora_pecora_2018]\] \[[Pecora et al 2012][research_pecora_amoroso_2012]\] \[[Pengyuan et al 2024][research_pengyuan_yanfei_2024]\] \[[Perera 2021][research_perera_2021]\] \[[Peter and Stumpf 2018][research_peter_stumpf_2018]\] \[[Pham and Peraza Hernandez 2021][research_pham_perazahernandez_2021]\] \[[Pisaneschi et al 2026][research_pisaneschi_2026]\] \[[Podugu and Ananthasuresh 2010][research_podugu_ananthasuresh_2010]\] \[[Popov et al 2008][research_popov_labib_2008]\] \[[Popov et al 2010][research_popov_grigorie_2010]\] \[[Popov et al 2010][research_popov_grigorie_2010_b]\] \[[Popov et al 2010][research_popov_grigorie_2010_c]\] \[[Powers et al 1992][research_powers_webb_1992]\] \[[Prabhakar 2025][research_prabhakar_2025]\] \[[Prabhakar and Murugan 2022][research_prabhakar_murugan_2022]\] \[[Prabhakar and Murugan 2024][research_prabhakar_murugan_2024]\] \[[Prabhakar and Murugan 2026][research_prabhakar_murugan_2026]\] \[[Prasad et al 2024][research_prasad_raghavulu_2024]\] \[[Previtali et al 2013][research_previtali_arrieta_2013]\] \[[Previtali et al 2014][research_previtali_arrieta_2014]\] \[[Pu et al 2024][research_pu_zhang_2024]\] \[[Pyeon and Bae 2026][research_pyeon_bae_2026]\] \[[Qiao et al 2018][research_qiao_zhang_2018]\] \[[Qingbao et al 2026][research_qingbao_hui_2026]\] \[[Qu et al 2025][research_qu_wang_2025]\] \[[Rade and de Souza 2016][research_rade_desouza_2016]\] \[[Rahn and Reinertson 1986][research_rahn_reinertson_1986]\] \[[Rajesh Senthil Kumar et al 2020][research_rajeshsenthilkumar_venugopal_2020]\] \[[2017][research_rea_pecora_2017]\] \[[Rea et al 2018][research_rea_pecora_2018]\] \[[Reich and Sanders 2007][research_reich_sanders_2007_b]\] \[[Reich et al 2007][research_reich_sanders_2007]\] \[[Ren et al 2025][research_ren_kan_2025]\] \[[Ren et al 2025][research_ren_wei_2025]\] \[[Ren et al 2025][research_ren_wei_2025_b]\] \[[Ren et al 2026][research_ren_2026]\] \[[Rivas-Padilla et al 2023][research_rivaspadilla_boston_2023]\] \[[Roberts 1965][research_roberts_1965]\] \[[Rodriguez 2007][research_rodriguez_2007]\] \[[Rongqi and Jianmei 2013][research_rongqi_jianmei_2013]\] \[[Rouaix][research_rouaix]\] \[[Roy and Mukherjee 2020][research_roy_mukherjee_2020]\] \[[Rudnick-Cohen et al 2020][research_rudnickcohen_hodson_2020]\] \[[Rudnick-Cohen et al 2022][research_rudnickcohen_hodson_2022]\] \[[Ruxandra Mihaela et al 2012][research_ruxandramihaela_samuel_2012]\] \[[Sabri et al 2022][research_sabri_elzaabalawy_2022]\] \[[Sacchi et al 2026][research_sacchi_sneddon_2026]\] \[[Samareh et al 2007][research_samareh_chwalowski_2007]\] \[[Sanders et al 2003][research_sanders_eastep_2003]\] \[[Sanghi et al 2024][research_sanghi_cesnik_2024]\] \[[Santos et al 2018][research_santos_sousa_2018]\] \[[Schorsch et al 2018][research_schorsch_nagel_2018]\] \[[Schweikert et al 2022][research_schweikert_patel_2022]\] \[[Secanell et al 2005][research_secanell_suleman_2005]\] \[[Segui et al 2017][research_segui_gabor_2017]\] \[[Seigler and Neal 2009][research_seigler_neal_2009]\] \[[Seigler et al 2007][research_seigler_neal_2007]\] \[[Shanmugam et al 2016][research_shanmugam_raja_2016]\] \[[Shanmugam et al 2025][research_shanmugam_2025]\] \[[Shao et al 2017][research_shao_zhou_2017]\] \[[Sherrow et al 2026][research_sherrow_hassen_2026]\] \[[Shi and Peng 2014][research_shi_peng_2014]\] \[[Shi and Peng 2015][research_shi_peng_2015]\] \[[Shi and Song 2012][research_shi_song_2012]\] \[[Shi and Wan 2015][research_shi_wan_2015]\] \[[Si et al 2025][research_si_2025]\] \[[Sihite et al 2023][research_sihite_salagame_2023]\] \[[Singh 2024][research_singh_2024]\] \[[Singha 2025][research_singha_2025]\] \[[Singha and Murugan 2022][research_singha_murugan_2022]\] \[[Singha and Murugan 2023][research_singha_murugan_2023]\] \[[Singha and Murugan 2026][research_singha_murugan_2026]\] \[[Sinha and Yuan 2026][research_sinha_yuan_2026]\] \[[Skillen and Crossley 2005][research_skillen_crossley_2005]\] \[[Skillen and Crossley 2007][research_skillen_crossley_2007]\] \[[Skillen and Crossley 2008][research_skillen_crossley_2008]\] \[[Skillen and Crossley 2008][research_skillen_crossley_2008_b]\] \[[Sleesongsom and Bureerat 2011][research_sleesongsom_bureerat_2011]\] \[[Sleesongsom et al 2013][research_sleesongsom_bureerat_2013]\] \[[Smith and Nelson 1988][research_smith_nelson_1988]\] \[[Smith et al 2007][research_smith_butt_2007]\] \[[Smith et al 2014][research_smith_lowenberg_2014]\] \[[Sneed et al 2007][research_sneed_smith_2007]\] \[[Snyder et al 2009][research_snyder_sanders_2009]\] \[[Sofla et al 2010][research_sofla_meguid_2010]\] \[[Sofla et al 2010][research_sofla_meguid_2010_b]\] \[[Soneda et al 2020][research_soneda_yokozeki_2020]\] \[[Soneda et al 2021][research_soneda_yokozeki_2021]\] \[[Soneda et al 2022][research_soneda_tsushima_2022]\] \[[Soneda et al 2023][research_soneda_tsushima_2023]\] \[[Soneda et al 2023][research_soneda_tsushima_2023_b]\] \[[Srivastava et al 2025][research_srivastava_patel_2025]\] \[[Strayer and Manoharan 2025][research_strayer_manoharan_2025]\] \[[Sturm et al 2019][research_sturm_achleitner_2019]\] \[[Su 2026][research_su_2026]\] \[[Su et al 2016][research_su_swei_2016]\] \[[Sun et al 2022][research_sun_li_2022]\] \[[Svoboda et al 2018][research_svoboda_hromcik_2018]\] \[[Svoboda et al 2023][research_svoboda_hengstermovric_2023]\] \[[Syed et al 2022][research_syed_moshtaghzadeh_2022]\] \[[Syed et al 2022][research_syed_moshtaghzadeh_2022_b]\] \[[Szilder and Lozowski 2018][research_szilder_lozowski_2018]\] \[[Takarics et al 2020][research_takarics_mocsanyi_2020]\] \[[Tal and Nguyen 2015][research_tal_nguyen_2015]\] \[[Tandale et al 2004][research_tandale_rong_2004]\] \[[Tang and Dowell 2008][research_tang_dowell_2008]\] \[[Tang et al 2023][research_tang_che_2023]\] \[[Tarabi et al 2015][research_tarabi_ghasemloo_2015]\] \[[Tarnowski 2017][research_tarnowski_2017]\] \[[Taylor and Hunsaker 2023][research_taylor_hunsaker_2023]\] \[[Tchatchueng Kammegne et al 2016][research_tchatchuengkammegne_botez_2016]\] \[[The Mission Adaptive Wing 1986][research_the_mission_1986]\] \[[Tian et al 2024][research_tian_zhang_2024]\] \[[Tian et al 2025][research_tian_huang_2025]\] \[[Traub 2019][research_traub_2019]\] \[[Tsushima et al 2018][research_tsushima_yokozeki_2018]\] \[[Tsushima et al 2019][research_tsushima_2019]\] \[[Tsushima et al 2019][research_tsushima_arizono_2019]\] \[[Tsushima et al 2020][research_tsushima_arizono_2020]\] \[[Tsushima et al 2020][research_tsushima_tamayama_2020]\] \[[Ukolov and Gamboa 2026][research_ukolov_gamboa_2026]\] \[[Uzun and Oktay 2023][research_uzun_oktay_2023]\] \[[Valasek et al 2009][research_valasek_lampton_2009]\] \[[Valasek et al 2012][research_valasek_kirkpatrick_2012]\] \[[Vale et al 2011][research_vale_leite_2011]\] \[[Vale et al 2013][research_vale_lau_2013]\] \[[Vasista et al 2016][research_vasista_degaspari_2016]\] \[[Vasista et al 2017][research_vasista_riemenschneider_2017]\] \[[Vazquez et al 2020][research_vazquez_joshi_2020]\] \[[Verrastro and Metge 2015][research_verrastro_metge_2015]\] \[[Vigliotti and Pasini 2018][research_vigliotti_pasini_2018]\] \[[Vishwanathan][research_vishwanathan]\] \[[Vocke et al 2011][research_vocke_kothera_2011]\] \[[Vocke III et al 2012][research_vockeiii_s_2012]\] \[[Vos et al 2007][research_vos_debreuker_2007]\] \[[Vos et al 2010][research_vos_gurdal_2010]\] \[[Vu][research_vu]\] \[[Wales et al 2015][research_wales_cheung_2015]\] \[[Wang][research_wang]\] \[[Wang 2026][research_wang_2026_b]\] \[[Wang and Guo 2024][research_wang_guo_2024_b]\] \[[Wang and Niu 2026][research_wang_2026_4]\] \[[Wang et al 2015][research_wang_dong_2015]\] \[[Wang et al 2019][research_wang_gong_2019]\] \[[Wang et al 2021][research_wang_hou_2021]\] \[[Wang et al 2023][research_wang_hou_2023]\] \[[Wang et al 2024][research_wang_zhao_2024]\] \[[Wang et al 2026][research_wang_2026_3]\] \[[Wei et al 2026][research_wei_tong_2026]\] \[[Weisshaar 2013][research_weisshaar_2013]\] \[[Werter and De Breuker 2015][research_werter_debreuker_2015]\] \[[Westfall et al 2007][research_westfall_canfield_2007]\] \[[Wickenheiser and Garcia 2012][research_wickenheiser_garcia_2012]\] \[[Wiggins et al 2004][research_wiggins_stubbs_2004]\] \[[Wilbur et al 2018][research_wilbur_mistry_2018]\] \[[Wildschek et al 2008][research_wildschek_judas_2008]\] \[[Wing Morphing Design Using 2013][research_wing_morphing_2013]\] \[[Wittmann et al 2009][research_wittmann_steiner_2009]\] \[[Wlezien et al 1998][research_wlezien_horner_1998]\] \[[Woldhuis et al 2026][research_woldhuis_asaro_2026]\] \[[Wong et al 2022][research_wong_bil_2022]\] \[[Woods et al 2013][research_woods_wereley_2013]\] \[[Wu and Xu 2023][research_wu_xu_2023]\] \[[Wu et al 2016][research_wu_lu_2016]\] \[[Wu et al 2017][research_wu_lu_2017]\] \[[Wu et al 2017][research_wu_xiao_2017]\] \[[Wu et al 2018][research_wu_xiao_2018]\] \[[Wu et al 2021][research_wu_tan_2021]\] \[[Wu et al 2023][research_wu_hu_2023]\] \[[Wu et al 2026][research_wu_cai_2026]\] \[[Wu et al 2026][research_wu_cai_2026_b]\] \[[Xia et al 2014][research_xia_ajaj_2014]\] \[[Xia et al 2023][research_xia_jing_2023]\] \[[Xiang et al 2018][research_xiang_liu_2018]\] \[[Xie et al 2022][research_xie_chen_2022]\] \[[Xijuan et al 2016][research_xijuan_qiang_2016]\] \[[Xin and Li 2025][research_xin_li_2025]\] \[[Xiong et al 2021][research_xiong_bartels_2021]\] \[[Xiong et al 2022][research_xiong_nguyen_2022]\] \[[Xiong et al 2022][research_xiong_nguyen_2022_b]\] \[[Xu 2012][research_xu_2012]\] \[[Xu et al 2018][research_xu_lu_2018]\] \[[Xu et al 2018][research_xu_zhang_2018]\] \[[Xu et al 2019][research_xu_han_2019]\] \[[Xu et al 2022][research_xu_li_2022_b]\] \[[Yaman 2017][research_yaman_2017]\] \[[Yan et al 2019][research_yan_li_2019]\] \[[Yan et al 2019][research_yan_li_2019_b]\] \[[Yan et al 2025][research_yan_han_2025]\] \[[Yang and Chen 2023][research_yang_chen_2023]\] \[[Yang et al 2015][research_yang_sartor_2015]\] \[[Yang et al 2019][research_yang_guo_2019]\] \[[Yang et al 2022][research_yang_cai_2022]\] \[[Yang et al 2023][research_yang_lu_2023]\] \[[Yang et al 2023][research_yang_tan_2023]\] \[[Yang et al 2024][research_yang_xiao_2024]\] \[[Yang et al 2024][research_yang_xu_2024]\] \[[Yang et al 2026][research_yang_2026]\] \[[Yang et al 2026][research_yang_zhao_2026]\] \[[Yao and Wu 2019][research_yao_wu_2019]\] \[[Ye et al 2025][research_ye_xu_2025]\] \[[Ye et al 2026][research_ye_peng_2026]\] \[[You et al 2019][research_you_kim_2019]\] \[[You et al 2020][research_you_skin_2020]\] \[[Yu and He 2016][research_yu_he_2016]\] \[[Yu and Ma 2022][research_yu_ma_2022]\] \[[Yu et al 2009][research_yu_liu_2009]\] \[[Yu et al 2019][research_yu_yang_2019]\] \[[Yu et al 2024][research_yu_zhou_2024]\] \[[Yu et al 2026][research_yu_yan_2026]\] \[[Yue et al 2009][research_yue_wang_2009]\] \[[Yue et al 2013][research_yue_wang_2013]\] \[[Yue et al 2013][research_yue_wang_2013_b]\] \[[Yue et al 2013][research_yue_wang_2013_c]\] \[[Yue et al 2013][research_yue_wang_2013_d]\] \[[Yue et al 2017][research_yue_wang_2017]\] \[[Yue et al 2017][research_yue_zhang_2017]\] \[[Yutong et al 2025][research_yutong_ying_2025]\] \[[Ze et al 2024][research_ze_shen_2024]\] \[[Zebedee et al 2019][research_zebedee_mohammed_2019]\] \[[Zhang and Wang 2019][research_zhang_wang_2019]\] \[[Zhang and Wu 2014][research_zhang_wu_2014]\] \[[Zhang and Wu 2014][research_zhang_wu_2014_b]\] \[[Zhang and Yu 2012][research_zhang_yu_2012]\] \[[Zhang and Zhao 2023][research_zhang_zhao_2023]\] \[[Zhang et al 2015][research_zhang_zhou_2015]\] \[[Zhang et al 2016][research_zhang_yang_2016]\] \[[Zhang et al 2017][research_zhang_wang_2017]\] \[[Zhang et al 2018][research_zhang_shaw_2018]\] \[[Zhang et al 2021][research_zhang_shaw_2021]\] \[[Zhang et al 2025][research_zhang_guo_2025]\] \[[Zhang et al 2025][research_zhang_song_2025]\] \[[Zhang et al 2025][research_zhang_yang_2025]\] \[[Zhang et al 2026][research_zhang_pu_2026]\] \[[Zhang et al 2026][research_zhang_pu_2026_b]\] \[[Zhao and Hu 2013][research_zhao_hu_2013]\] \[[Zhao and Hu 2013][research_zhao_hu_2013_b]\] \[[Zhao et al 2021][research_zhao_xi_2021]\] \[[Zhao et al 2026][research_zhao_zhang_2026]\] \[[Zhen et al 2017][research_zhen_yingying_2017]\] \[[Zhou and Huang 2021][research_zhou_huang_2021]\] \[[Zhou and Huang 2021][research_zhou_huang_2021_b]\] \[[Zhou et al 2018][research_zhou_plummer_2018]\] \[[Zhou et al 2022][research_zhou_plummer_2022]\] \[[Zhu 2018][research_zhu_2018]\] \[[Zhu et al 2017][research_zhu_liu_2017]\] \[[Zhu et al 2025][research_zhu_zhou_2025]\] \[[Zhu et al 2025][research_zhu_zhou_2025_b]\] \[[Zientarski et al 2015][research_zientarski_marks_2015]\] \[[Şahin and Yaman 2018][research_sahin_yaman_2018]\] \[[Şahin and Yaman 2018][research_sahin_yaman_2018_b]\] \[[Şahin et al 2018][research_sahin_cakir_2018]\] \[[Şahin et al 2018][research_sahin_cakir_2018_b]\]

### Flutter, aeroelasticity, loads and structure

**The structure and the moving joint.** Flutter, divergence and static aeroelasticity of swept and forward-swept wings, measured and predicted wing loads, and structural design.

**611 records.** \[[Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]\] \[[Abrego et al 1999][research_abrego_maier_1999]\] \[[Acree et al 2004][research_acree_peyran_2004]\] \[[Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]\] \[[Ahmad et al 2018][research_ahmad_baig_2018]\] \[[Aircraft flutter control system 2011][research_aircraft_flutter_2011]\] \[[Aircraft Load 2010][research_aircraft_load_2010]\] \[[Alcorta et al 2023][research_alcorta_chouvion_2023]\] \[[Allen et al 2005][research_allen_lizotte_2005]\] \[[Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]\] \[[Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]\] \[[An Aeroelastic Metamodel Based 2013][research_an_aeroelastic_2013]\] \[[Andrews and Perez 2015][research_andrews_perez_2015]\] \[[Appendix C Flutter Analysis 2016][research_appendix_c_2016]\] \[[Arabian et al 1961][research_arabian_runckel_1961]\] \[[Armstrong et al 2006][research_armstrong_lindberg_2006]\] \[[Arnold 1942][research_arnold_1942]\] \[[Arslan and Carlson 1994][research_arslan_carlson_1994]\] \[[Arun Kumar et al 2010][research_arunkumar_viswamurthy_2010]\] \[[Asher et al 1957][research_asher_martuccelli_1957]\] \[[Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]\] \[[Azam and Sulaeman 2014][research_azam_sulaeman_2014]\] \[[Baker 1953][research_baker_1953]\] \[[Balabanov and Haftka 1996][research_balabanov_haftka_1996]\] \[[Bardin 2021][research_bardin_2021]\] \[[Barmby et al 1951][research_barmby_cunningham_1951]\] \[[Barnard 1969][research_barnard_1969]\] \[[Barthelemy and Bergen 1988][research_barthelemy_bergen_1988]\] \[[Batina et al 1988][research_batina_bennett_1988]\] \[[Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]\] \[[Ben Asher and Raveh 2023][research_benasher_raveh_2023]\] \[[Benaouali and Kachel 2017][research_benaouali_kachel_2017]\] \[[Bendiksen 2008][research_bendiksen_2008]\] \[[Bennett 1981][research_bennett_1981]\] \[[Bennett and Batina 1989][research_bennett_batina_1989]\] \[[Bennett and Yates 1963][research_bennett_yates_1963]\] \[[Bennett et al 1988][research_bennett_batina_1988]\] \[[Berci 2017][research_berci_2017]\] \[[Bergman 1979][research_bergman_1979]\] \[[Bhat 2018][research_bhat_2018]\] \[[Birchfield 1970][research_birchfield_1970]\] \[[Bird 1949][research_bird_1949]\] \[[Blair and Weisshaar 1982][research_blair_weisshaar_1982]\] \[[Bland 1980][research_bland_1980]\] \[[Boehm et al 2001][research_boehm_flick_2001]\] \[[Bohon and Dixon 1964][research_bohon_dixon_1964]\] \[[Bolding and Stearman 1976][research_bolding_stearman_1976]\] \[[Borglund and Kroo 2002][research_borglund_kroo_2002]\] \[[Boswinkle and Smith 1958][research_boswinkle_smith_1958]\] \[[Bottai et al 2022][research_bottai_campbell_2022]\] \[[Boudreault 1983][research_boudreault_1983]\] \[[Boyd 1977][research_boyd_1977]\] \[[Brady et al 1954][research_brady_maier_1954]\] \[[Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]\] \[[Brenner 2007][research_brenner_2007]\] \[[Brewer 1953][research_brewer_1953]\] \[[Brown et al 1980][research_brownjr_price_1980]\] \[[Browne et al 2024][research_browne_maldonado_2024]\] \[[Buchnik and Karpel 2014][research_buchnik_karpel_2014]\] \[[Buddhamatya et al 2026][research_buddhamatya_miranda_2026]\] \[[Burkhalter et al 1992][research_burkhalter_spring_1992]\] \[[Burkhart 1980][research_burkhart_1980]\] \[[Burner and Martinson 1996][research_burner_martinson_1996]\] \[[Busan 1998][research_busan_1998]\] \[[Böhnisch et al 2024][research_bohnisch_braun_2024]\] \[[Candida et al 2019][research_candida_souzadepaula_2019]\] \[[Carlsson 2005][research_carlsson_2005]\] \[[Carlsson and Kuttenkeuler 2003][research_carlsson_kuttenkeuler_2003]\] \[[Casey 1988][research_casey_1988]\] \[[Cassetti et al 1961][research_cassetti_re_1961]\] \[[Castellani et al 2016][research_castellani_cooper_2016]\] \[[Castile and Herr 1949][research_castile_herr_1949]\] \[[Catalano et al 2024][research_catalano_diodati_2024]\] \[[Celi and Friedmann 1988][research_celi_friedmann_1988]\] \[[Cella and Biancolini 2012][research_cella_biancolini_2012]\] \[[Chen et al 1998][research_chen_chang_1998]\] \[[Chen et al 2002][research_chen_sulaeman_2002]\] \[[Chen et al 2024][research_chen_zhang_2024]\] \[[Chen et al 2026][research_chen_gray_2026]\] \[[Cheng 1982][research_cheng_1982]\] \[[Chiarelli and Bonomo 2019][research_chiarelli_2019]\] \[[Chipman and Malone 1977][research_chipman_malone_1977]\] \[[Chipman et al 1982][research_chipman_zislin_1982]\] \[[Chipman et al 1984][research_chipman_rauch_1984]\] \[[Chipman et al 1985][research_chipman_rauch_1985]\] \[[Choi et al 2013][research_choi_park_2013]\] \[[Choi et al 2016][research_choi_kang_2016]\] \[[Choi et al 2020][research_choi_lim_2020]\] \[[Clarke et al 2005][research_clarke_2005]\] \[[Cole 1986][research_cole_1986]\] \[[Cole 1986][research_cole_1986_b]\] \[[Cole 1988][research_cole_1988]\] \[[Cole 1990][research_cole_1990]\] \[[Cole 1991][research_cole_1991]\] \[[Colella et al 2012][research_colella_bernadini_2012]\] \[[Collar 1946][research_collar_1946]\] \[[Cooper and Stroud 1972][research_cooper_stroud_1972]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1953][research_cornellaeronauticallabincbuffalony_1953]\] \[[Cornette 1961][research_cornette_1961]\] \[[Costigan and Calico 1989][research_costigan_calico_1989]\] \[[Crouch et al 2018][research_crouch_garbaruk_2018]\] \[[Cunningham 1951][research_cunningham_1951]\] \[[Cunningham et al 1987][research_cunningham_batina_1987]\] \[[Cunningham et al 1988][research_cunningham_batina_1988]\] \[[Currao and Yeh 2026][research_currao_yeh_2026]\] \[[D'Aguanno et al 2022][research_daguanno_campspons_2022]\] \[[D'Aguanno et al 2022][research_daguanno_schrijer_2022]\] \[[D'Ewart et al 1958][research_dewart_jr_1958]\] \[[Dal'Carobo and Fensterseifer 2010][research_dalcarobo_fensterseifer_2010]\] \[[Damstrom and Mayes 1970][research_damstrom_mayes_1970]\] \[[Dandois 2016][research_dandois_2016]\] \[[Dansberry et al 1990][research_dansberry_rivera_1990]\] \[[Das et al 2021][research_das_venkatraman_2021]\] \[[Davis 1969][research_davis_1969]\] \[[de Melo et al 2024][research_demelo_bussamra_2024]\] \[[Deangelis 1981][research_deangelis_1981]\] \[[DeAngelis 1982][research_deangelis_1982]\] \[[Delgado et al 2026][research_delgado_datta_2026]\] \[[Delgado Regis et al 2004][research_delgadoregis_mattos_2004]\] \[[Denegri et al 2021][research_denegri_sharma_2021]\] \[[Deng et al 2022][research_deng_wang_2022]\] \[[Designing Airplane Wing Structures 2025][research_designing_airplane_2025]\] \[[Desmarais and Reed 1980][research_desmarais_reediii_1980]\] \[[DeYoung 1947][research_deyoung_1947]\] \[[Diederich and Budiansky 1948][research_diederich_budiansky_1948]\] \[[Dillinger et al 2019][research_dillinger_abdalla_2019]\] \[[Dive Testing for Flutter 2003][research_dive_testing_2003]\] \[[Djojodihardjo 2023][research_djojodihardjo_2023]\] \[[Doggett and Farmer 1976][research_doggett_farmer_1976]\] \[[Doggett et al 1959][research_doggett_morgan_1959]\] \[[Doggett and Ricketts 1977][research_doggettjr_ricketts_1977]\] \[[Dowell 1996][research_dowell_1996]\] \[[Dowell 1999][research_dowell_1999]\] \[[Dowell and Hall 2003][research_dowell_hall_2003]\] \[[Downs and Prazenica 2022][research_downs_prazenica_2022]\] \[[Downs and Prazenica 2023][research_downs_prazenica_2023]\] \[[Downs et al 1993][research_downs_1993]\] \[[Drachinsky et al 2022][research_drachinsky_avin_2022]\] \[[Dugundji 1965][research_dugundji_1965]\] \[[Dugundji and Ghareeb 1965][research_dugundji_ghareeb_1965]\] \[[Dugundji et al 1962][research_dugundji_dowell_1962]\] \[[Edwards 1992][research_edwards_1992]\] \[[Edwards 1998][research_edwards_1998]\] \[[Elham and Timmer 2016][research_elham_timmer_2016]\] \[[Ellis et al 2025][research_ellis_2025]\] \[[Elshazly et al 2025][research_elshazly_kassem_2025]\] \[[Engelbrecht][research_engelbrecht]\] \[[Er-El 1988][research_erel_1988]\] \[[Ericsson 1986][research_ericsson_1986]\] \[[Ericsson 1987][research_ericsson_1987]\] \[[Estimating the Takeoff Wing 2010][research_estimating_the_2010]\] \[[Evaluation of methods for 1981][research_evaluation_of_1981]\] \[[Experimental and Numerical Unsteady 2024][research_experimental_and_2024]\] \[[Farhat 1998][research_farhat_1998]\] \[[Farhat 2000][research_farhat_2000]\] \[[Farhat 2001][research_farhat_2001]\] \[[Farmer and Hanson 1976][research_farmer_hanson_1976]\] \[[Fenwick and Allen 2007][research_fenwick_allen_2007]\] \[[Figge and Bernhardt 1975][research_figge_bernhardt_1975]\] \[[Filippou et al 2024][research_filippou_kilimtzidis_2024]\] \[[Firouz-Abadi et al 2013][research_firouzabadi_askarian_2013]\] \[[Fisher 1951][research_fisher_1951]\] \[[Floros and Kang 2017][research_floros_kang_2017]\] \[[Forster et al 1996][research_forster_kolonay_1996]\] \[[Francois et al 2016][research_francois_cooper_2016]\] \[[Freidmann 2001][research_freidmann_2001]\] \[[Fugate et al 2019][research_fugate_nguyen_2019]\] \[[Fukumoto et al 2023][research_fukumoto_kouchi_2023]\] \[[Furuya and Fukuchi 2001][research_furuya_fukuchi_2001]\] \[[Gainer et al 1984][research_gainer_1984]\] \[[Garre 2017][research_garre_2017]\] \[[Garrick and Reed 1981][research_garrick_reed_1981]\] \[[Gibson and Ung 1995][research_gibson_ung_1995]\] \[[Gilbert and Silva 1987][research_gilbert_silva_1987]\] \[[Gilbert et al 1982][research_gilbert_schmidt_1982]\] \[[Gilbert et al 1984][research_gilbert_schmidt_1984]\] \[[Giles 1986][research_giles_1986]\] \[[Giles 1995][research_giles_1995]\] \[[Gimmestad 1981][research_gimmestad_1981]\] \[[Goetz and Doggett 1974][research_goetz_doggett_1974]\] \[[Goizueta et al 2022][research_goizueta_wynn_2022]\] \[[Goland 1945][research_goland_1945]\] \[[Goland et al 1954][research_goland_luke_1954]\] \[[Gordnier and Visbal 1994][research_gordnier_visbal_1994]\] \[[Green 1987][research_green_1987]\] \[[Green et al 1990][research_green_lee_1990]\] \[[Griffin and Eastep 1981][research_griffin_eastep_1981]\] \[[Griffin and Eastep 1982][research_griffin_eastep_1982]\] \[[Grose 1979][research_grose_1979]\] \[[Grossman et al 1986][research_grossman_gurdal_1986]\] \[[Gu et al 2024][research_gu_healy_2024]\] \[[Gul and Datta 2021][research_gul_datta_2021]\] \[[Gurdal 2002][research_gurdal_2002]\] \[[Gurdal et al 1999][research_gurdal_haftka_1999]\] \[[Guruswamy 2010][research_guruswamy_2010]\] \[[Guruswamy et al 1984][research_guruswamy_yang_1984]\] \[[Haas and Chopra 1987][research_haas_chopra_1987]\] \[[Haftka 1977][research_haftka_1977]\] \[[Hamer et al 1961][research_hamer_1961]\] \[[Hansen 2011][research_hansen_2011]\] \[[Hanson 1973][research_hanson_1973]\] \[[Havenar and Ilie 2025][research_havenar_ilie_2025]\] \[[Helm et al 2021][research_helm_fehrs_2021]\] \[[Henning 1953][research_henning_1953]\] \[[Hermanutz and Hornung 2020][research_hermanutz_2020]\] \[[Herrmann et al 1966][research_herrmann_nematnasser_1966]\] \[[Herrmann et al 1967][research_herrmann_nematnasser_1967]\] \[[Hess 1987][research_hess_1987]\] \[[Hilger and Ritter 2021][research_hilger_ritter_2021]\] \[[HlCKEY 1969][research_hlckey_1969]\] \[[Hopkins 1951][research_hopkins_1951]\] \[[Hord][research_hord]\] \[[Hosder et al 2008][research_hosder_walters_2008]\] \[[Hoshi et al 2020][research_hoshi_kuya_2020]\] \[[Hou 2025][research_hou_2025]\] \[[Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]\] \[[Housner and Stein 1974][research_housner_1974]\] \[[Hu et al 2026][research_hu_traisnel_2026]\] \[[Huang et al 2017][research_huang_wu_2017]\] \[[Hubbard et al 2014][research_hubbard_fontenot_2014]\] \[[Hutchison et al 1992][research_hutchison_huang_1992]\] \[[Hutchison et al 1992][research_hutchison_unger_1992]\] \[[Hwang and Pi 1979][research_hwang_pi_1979]\] \[[Hwu and Tsai 2002][research_hwu_tsai_2002]\] \[[Ilie and Havenar 2022][research_ilie_havenar_2022]\] \[[Jenkins 1986][research_jenkins_1986]\] \[[Jenkins and Kuhl 1977][research_jenkins_1977_2]\] \[[Jenkins et al 1977][research_jenkins_1977]\] \[[Jian and Ke-Qin 2004][research_jian_keqin_2004]\] \[[Jin et al 2011][research_jin_song_2011]\] \[[Johns 1960][research_johns_1960]\] \[[Johnson 1953][research_johnson_1953_b]\] \[[Jones and Unangst 1963][research_jones_unangst_1963]\] \[[Jung and Reimerdes 2003][research_jung_reimerdes_2003]\] \[[Kamiya et al 1978][research_kamiya_nishi_1978]\] \[[Kandil et al 1993][research_kandil_kandil_1993_b]\] \[[Kannemans 1995][research_kannemans_1995]\] \[[Kapania et al 1991][research_kapania_eldred_1991]\] \[[Kargarnovin and Sayrarfie 1995][research_kargarnovin_sayrarfie_1995]\] \[[Karpouzian and Librescu 1993][research_karpouzian_librescu_1993]\] \[[Kawazoe and Kato 2005][research_kawazoe_kato_2005]\] \[[Kayran 2004][research_kayran_2004]\] \[[Kearns 1962][research_kearns_1962]\] \[[Keller et al 1991][research_keller_sandford_1991]\] \[[Kim and Lee 2001][research_kim_lee_2001]\] \[[Kim and Marciniak 2002][research_kim_marciniak_2002]\] \[[Kimler and Canfield 2006][research_kimler_canfield_2006]\] \[[Klein and Viswanathan 1973][research_klein_viswanathan_1973]\] \[[Klepl 1992][research_klepl_1992]\] \[[Klug et al 2023][research_klug_ullah_2023]\] \[[Klyde et al 2004][research_klyde_harris_2004]\] \[[Kodigaddi 2026][research_kodigaddi_2026]\] \[[Kolar and Lile 1971][research_kolar_lile_1971]\] \[[Kong 1994][research_kong_1994]\] \[[Koo 2001][research_koo_2001]\] \[[Koohi et al 2014][research_koohi_shahverdi_2014]\] \[[Kornev et al 2021][research_kornev_ambrozhevich_2021]\] \[[Kosmatka and Panza 2003][research_kosmatka_panza_2003]\] \[[Krener 2001][research_krener_2001]\] \[[Krengel 2024][research_krengel_2024]\] \[[Krüger et al 2014][research_kruger_klimmek_2014]\] \[[Kuo and Hsu 1997][research_kuo_hsu_1997]\] \[[Kyser and Willis 1973][research_kyser_willis_1973]\] \[[Körpe and Kanat 2019][research_korpe_kanat_2019]\] \[[Laitone 1978][research_laitone_1978]\] \[[Laitone 1978][research_laitone_1978_b]\] \[[Laitone 1994][research_laitone_1994]\] \[[Lasauskas 2016][research_lasauskas_2016]\] \[[Lauten et al 1954][research_lauten_lundstrom_1954]\] \[[Lee 1994][research_lee_1994_b]\] \[[Lee and Chen 2004][research_lee_chen_2004]\] \[[Lee et al 1986][research_lee_tavella_1986]\] \[[Lee-Rausch and Batina 1993][research_leerausch_batina_1993]\] \[[Lee-Rausch and Batina 1993][research_leerausch_batina_1993_b]\] \[[Lee-Rausch and Batina 1993][research_leerausch_batina_1993_c]\] \[[Leishman 2026][research_leishman_2026]\] \[[Leitch et al 2025][research_leitch_2025]\] \[[Lemley 1968][research_lemley_1968]\] \[[Lemley and Mullans 1973][research_lemley_mullans_1973]\] \[[Lemley and Mullans 1974][research_lemley_mullans_1974]\] \[[Leoviriyakit and Jameson 2004][research_leoviriyakit_jameson_2004]\] \[[Leoviriyakit and Jameson 2004][research_leoviriyakit_jameson_2004_b]\] \[[Leoviriyakit et al 2004][research_leoviriyakit_kim_2004]\] \[[Lesoinne 2007][research_lesoinne_2007]\] \[[Li 2015][research_li_2015]\] \[[Li 2023][research_li_2023]\] \[[Li and Guo 2013][research_li_guo_2013]\] \[[Li et al 2013][research_li_yang_2013]\] \[[Li et al 2014][research_li_zhang_2014]\] \[[Li et al 2026][research_li_wei_2026]\] \[[Librescu and Khdeir 1988][research_librescu_khdeir_1988]\] \[[Librescu and Simovich 1988][research_librescu_simovich_1988]\] \[[Librescu and Thangjitham 1988][research_librescu_thangjitham_1988]\] \[[Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]\] \[[Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]\] \[[Lindsley 2009][research_lindsley_2009]\] \[[Liu 2024][research_liu_2024]\] \[[Liu and Wang 2025][research_liu_wang_2025]\] \[[Liu et al 2016][research_liu_hou_2016]\] \[[Liu et al 2019][research_liu_ouyang_2019]\] \[[Liu et al 2020][research_liu_xu_2020]\] \[[Livne and Li 1994][research_livne_li_1994]\] \[[Livne and Li 1995][research_livne_li_1995]\] \[[Lockwood 1974][research_lockwood_1974]\] \[[Loewy 1969][research_loewy_1969]\] \[[Lokos et al 2005][research_lokos_lizotte_2005]\] \[[Long et al 2014][research_long_liu_2014]\] \[[Lottati 1985][research_lottati_1985]\] \[[Lottati 1987][research_lottati_1987]\] \[[Lottati 1988][research_lottati_1988]\] \[[A Method for Predicting][research_lowry_1957]\] \[[Luce 1949][research_luce_jr_1949]\] \[[Luderer and Thielecke 2025][research_luderer_2025]\] \[[Lundry 1967][research_lundry_1967]\] \[[Lundry 1977][research_lundry_1977]\] \[[Lyubomirov and Yartsev 2015][research_lyubomirov_yartsev_2015]\] \[[Ma et al 2017][research_ma_su_2017]\] \[[Mahzan et al 2013][research_mahzan_muhamad_2013]\] \[[Manan and Cooper 2008][research_manan_cooper_2008]\] \[[Mangalam et al 2010][research_mangalam_jutte_2010]\] \[[Marchetti 2023][research_marchetti_2023]\] \[[Marchman et al 1983][research_marchmaniii_donatelli_1983]\] \[[Marsden and Price 2001][research_marsden_price_2001]\] \[[Martina 1956][research_martina_1956]\] \[[Martina 1956][research_martina_1956_b]\] \[[Martina and Young 1955][research_martina_young_1955]\] \[[Marzocca et al 2001][research_marzocca_librescu_2001]\] \[[Mason 1953][research_mason_1953]\] \[[Mayes et al 1970][research_mayes_lores_1970]\] \[[McCuish and Caldwell 2018][research_mccuish_caldwell_2018]\] \[[McGeer 1984][research_mcgeer_1984]\] \[[McGurk et al 2024][research_mcgurk_stodieck_2024]\] \[[McTavish][research_mctavish]\] \[[Mei and Striz 1992][research_mei_striz_1992]\] \[[Melville and Gordnier 1998][research_melville_gordnier_1998]\] \[[Melvin and Zhao 2023][research_melvin_zhao_2023]\] \[[Melvin and Zhao 2024][research_melvin_zhao_2024]\] \[[Merrett 2015][research_merrett_2015]\] \[[Miles 1949][research_miles_1949]\] \[[Miller et al 1982][research_miller_wykes_1982]\] \[[Miller et al 1983][research_miller_wykes_1983]\] \[[Miyake and Terashima 2026][research_miyake_terashima_2026]\] \[[Model Rotor Testing for 2006][research_model_rotor_2006]\] \[[Molton et al 2013][research_molton_dandois_2013]\] \[[Monstein et al 2019][research_monstein_capone_2019]\] \[[Moon 1996][research_moon_1996]\] \[[Moseley and Gainer 1959][research_moseley_gainer_1959]\] \[[Moskalenko and Kosyrev 2019][research_moskalenko_kosyrev_2019]\] \[[Mottershead and Cooper 2012][research_mottershead_cooper_2012]\] \[[Mukhopadhyay 1995][research_mukhopadhyay_1995]\] \[[Murphy et al 1976][research_murphy_peloubet_1976]\] \[[Murphy et al 1983][research_murphy_rogers_1983]\] \[[Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]\] \[[Muñoz and García-Fogeda 2023][research_munoz_garciafogeda_2023]\] \[[Myers et al 1983][research_myers_guruswamy_1983]\] \[[NACA Conference on Aircraft 1957][research_naca_1957]\] \[[Nagornov 2020][research_nagornov_2020]\] \[[Nam et al 1998][research_nam_chattopadhyay_1998]\] \[[Nam et al 2000][research_nam_chattopadhyay_2000]\] \[[Neuert and Dinkler 2020][research_neuert_dinkler_2020]\] \[[Nguyen et al 2018][research_nguyen_hashemi_2018]\] \[[Nicolas et al 2016][research_nicolas_sullivan_2016]\] \[[Niel][research_niel]\] \[[Nieto Gómez and Chimeno Manguán 2025][research_nietogomez_chimenomanguan_2025]\] \[[Nikbay and Acar 2015][research_nikbay_acar_2015]\] \[[Nixon 1992][research_nixon_1992]\] \[[Noll and Huttsell 1978][research_noll_huttsell_1978]\] \[[Noll et al 1983][research_noll_calico_1983]\] \[[Noll et al 1983][research_noll_eastep_1983]\] \[[Noll et al 1984][research_noll_eastep_1984]\] \[[Nonlinear aerolasticity, continuum theory 2007][research_nonlinear_aerolasticity_2007]\] \[[O'Kelly 1955][research_okelly_1955]\] \[[O'Kelly et al 1954][research_okelly_lundstrom_1954]\] \[[Ohmichi et al 2018][research_ohmichi_ishida_2018]\] \[[Ouyang et al 2021][research_ouyang_zeng_2021]\] \[[Oyibo 1984][research_oyibo_1984]\] \[[Pak and Lung 2011][research_pak_lung_2011]\] \[[Pak and Truong 2015][research_pak_truong_2015]\] \[[Palaia et al 2025][research_palaia_salem_2025]\] \[[Pan and Cheng 1994][research_pan_cheng_1994]\] \[[Panel flutter in a 1991][research_panel_flutter_1991]\] \[[Park 2007][research_park_2007]\] \[[Parra 2023][research_parra_2023]\] \[[Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]\] \[[Pate and German 2014][research_pate_german_2014]\] \[[Patil 2003][research_patil_2003]\] \[[Patil 2004][research_patil_2004]\] \[[Peele and Eckstrom 1975][research_peele_1975]\] \[[Pena 2020][research_pena_2020]\] \[[Pena et al 2018][research_pena_2018]\] \[[Pengelley and Wilson 1954][research_pengelley_wilson_1954]\] \[[Perera and Guo 2008][research_perera_guo_2008]\] \[[Peterson and Menees 1961][research_peterson_menees_1961]\] \[[Peterson and Menees 1961][research_peterson_menees_1961_b]\] \[[Petre and Ashley 1975][research_petre_ashley_1975]\] \[[Petre and Ashley 1976][research_petre_ashley_1976]\] \[[Pettit and Grandhi 2003][research_pettit_grandhi_2003]\] \[[Phillips et al 2019][research_phillips_hunsaker_2019]\] \[[Phillips et al 2020][research_phillips_hunsaker_2020]\] \[[Phuekpan et al 2025][research_phuekpan_2025]\] \[[Pitcher and Maple 2008][research_pitcher_maple_2008]\] \[[Pitkin et al 1947][research_pitkin_gardner_1947]\] \[[Pitt 2004][research_pitt_2004]\] \[[Plante et al 2017][research_plante_dandois_2017]\] \[[Poomadath and Ajaj 2025][research_poomadath_ajaj_2025]\] \[[Popescu 2000][research_popescu_2000]\] \[[Popescu 2002][research_popescu_2002]\] \[[Prajapati and Kapania 2026][research_prajapati_kapania_2026]\] \[[Prediction of transonic flutter 1981][research_prediction_of_1981]\] \[[Qi et al 2023][research_qi_zhao_2023]\] \[[Qian and Guan 2012][research_qian_guan_2012]\] \[[Qiao et al 2019][research_qiao_zhou_2019]\] \[[Rathert et al 1951][research_rathert_1951]\] \[[Rausch et al 1992][research_rausch_batina_1992]\] \[[Raveh and Levy 2004][research_raveh_levy_2004]\] \[[Ray et al 1972][research_ray_1972]\] \[[Razi and Ghadiri 2008][research_razi_ghadiri_2008]\] \[[Redd et al 1974][research_redd_gilman_1974]\] \[[Reich et al 2002][research_reich_raveh_2002]\] \[[Reich et al 2004][research_reich_raveh_2004]\] \[[Reimer et al][research_reimer_braun]\] \[[Revivo and Raveh 2025][research_revivo_raveh_2025]\] \[[Rhoads 1952][research_rhoads_1952]\] \[[Rhodes and Johns 1966][research_rhodes_johns_1966]\] \[[Ricketts 1985][research_ricketts_1985]\] \[[Ricketts and Doggett 1980][research_ricketts_1980]\] \[[Rimer et al 1983][research_rimer_chipman_1983]\] \[[Rimer et al 1984][research_rimer_chipman_1984]\] \[[Rimer et al 1984][research_rimer_chipman_1984_b]\] \[[Rimer et al 1986][research_rimer_chipman_1986]\] \[[Riso and Cesnik 2022][research_riso_cesnik_2022]\] \[[Riso et al 2018][research_riso_divincenzo_2018]\] \[[Ritter et al 2017][research_ritter_dillinger_2017]\] \[[Ro et al 1992][research_ro_barlow_1992]\] \[[Robinson][research_robinson]\] \[[Robinson 2004][research_robinson_2004]\] \[[Robinson et al 1990][research_robinson_batina_1990]\] \[[Rocha Da Costa][research_rochadacosta]\] \[[Rockwell 1994][research_rockwell_1994]\] \[[Rodden 1989][research_rodden_1989]\] \[[Rodden 1989][research_rodden_1989_b]\] \[[Rogers 1970][research_rogers_1970]\] \[[Rongrong et al 2018][research_rongrong_zhengyin_2018]\] \[[Roos 1985][research_roos_1985]\] \[[Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]\] \[[S and Gangamkote 2023][research_s_gangamkote_2023]\] \[[Sager et al 1993][research_sager_1993]\] \[[Saitoh et al 1995][research_saitoh_hashidate_1995]\] \[[Saitoh et al 2012][research_saitoh_tamayama_2012]\] \[[Samikkannu 2011][research_samikkannu_2011]\] \[[Samuels 1982][research_samuels_1982]\] \[[Santos et al 2026][research_santos_marques_2026]\] \[[Sartor and Timme 2016][research_sartor_timme_2016]\] \[[Scanlan 1948][research_scanlan_1948]\] \[[Schewe and Mai 2018][research_schewe_mai_2018]\] \[[Schewe and Mai 2019][research_schewe_mai_2019]\] \[[Schmidt 1991][research_schmidt_1991]\] \[[Schmidt 2016][research_schmidt_2016]\] \[[Schmidt 2016][research_schmidt_2016_b]\] \[[Sharifi et al 2025][research_sharifi_2025]\] \[[Sheta 2004][research_sheta_2004]\] \[[Shevell 1978][research_shevell_1978]\] \[[Shields and Mohseni 2012][research_shields_mohseni_2012]\] \[[Shivaji et al 2025][research_shivaji_basavaraju_2025]\] \[[Silva][research_silva]\] \[[Silva][research_silva_b]\] \[[Silva et al 2023][research_silva_guimaraes_2023]\] \[[Singha and Murugan 2026][research_singha_murugan_2026_b]\] \[[Sivanandi et al 2022][research_sivanandi_gupta_2022]\] \[[Slater 1985][research_slater_1985]\] \[[Smith 1977][research_smith_1977]\] \[[Snyder and Weisshaar 2013][research_snyder_weisshaar_2013]\] \[[Soistmann 1992][research_soistmann_1992]\] \[[Soontornpasatch 2025][research_soontornpasatch_2025]\] \[[Sorbilli et al 2018][research_sorbilli_dibianchi_2018]\] \[[Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]\] \[[Sotoudeh and Hosking 2018][research_sotoudeh_hosking_2018]\] \[[Sotoudeh et al 2010][research_sotoudeh_hodges_2010]\] \[[Souahi 1983][research_souahi_1983]\] \[[Spain et al 1990][research_spain_soistmann_1990]\] \[[Spearman and Driver 1959][research_spearman_driver_1959]\] \[[Srinathkumar 2011][research_srinathkumar_2011]\] \[[Stanford and Ifju 2008][research_stanford_ifju_2008]\] \[[Stanford and Jacobson 2023][research_stanford_jacobson_2023]\] \[[Starossek 2021][research_starossek_2021]\] \[[Stebbins and Loth 2022][research_stebbins_loth_2022]\] \[[Stegmüller et al 2022][research_stegmuller_katzenmeier_2022]\] \[[Stegmüller et al 2026][research_stegmuller_haybock_2026]\] \[[Steimle et al 2008][research_steimle_schroder_2008]\] \[[Steimle et al 2010][research_steimle_schroder_2010]\] \[[Stepanyan and Nguyen][research_stepanyan_nguyen]\] \[[Stephenson 1956][research_stephenson_1956]\] \[[Stojakovic][research_stojakovic]\] \[[Streitenberger and Feldwisch 2025][research_streitenberger_feldwisch_2025]\] \[[Striz 1991][research_striz_1991]\] \[[Su et al 2018][research_su_wang_2018]\] \[[Sui 2022][research_sui_2022]\] \[[Suleman 2007][research_suleman_2007]\] \[[Sun et al 2024][research_sun_zhou_2024]\] \[[Sutton 1959][research_sutton_1959]\] \[[Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]\] \[[Svoboda 1999][research_svoboda_1999]\] \[[Swaim 1961][research_swaim_1961]\] \[[Swaim and Yen 1979][research_swaim_yen_1979]\] \[[Takahashi and Barchfeld 2016][research_takahashi_barchfeld_2016]\] \[[Takahashi and Donovan 2011][research_takahashi_donovan_2011]\] \[[Tamura and Yumitori 2024][research_tamura_yumitori_2024]\] \[[Tao et al 2019][research_tao_sun_2019]\] \[[Taylor and Gursul 2004][research_taylor_gursul_2004]\] \[[Taylor and Gursul 2004][research_taylor_gursul_2004_b]\] \[[The Wing Structure and 2013][research_the_wing_2013]\] \[[Theodorsen 1935][research_theodorsen_1935]\] \[[Tian et al 2016][research_tian_yang_2016]\] \[[Ting et al 2014][research_ting_nguyen_2014]\] \[[Tjatra et al 1992][research_tjatra_kapania_1992]\] \[[Torenbeek 1972][research_torenbeek_1972]\] \[[Torrigiani and Berci 2021][research_torrigiani_berci_2021]\] \[[Townsend et al 2018][research_townsend_stanford_2018]\] \[[Trenka et al 1963][research_trenka_white_1963]\] \[[Triplett 1980][research_triplett_1980]\] \[[Triplett et al 1973][research_triplett_kappus_1973]\] \[[Tu 1992][research_tu_1992_b]\] \[[Turner 1981][research_turner_1981]\] \[[Unangst 1959][research_unangst_1959]\] \[[Unsteady Aerodynamics and Flutter 2006][research_unsteady_aerodynamics_2006]\] \[[Utaka 2004][research_utaka_2004]\] \[[Utsch and Rockwell 1990][research_utsch_rockwell_1990]\] \[[Uzun 2025][research_uzun_2025]\] \[[Vale and Albuquerque 2025][research_vale_albuquerque_2025]\] \[[Vepa 2008][research_vepa_2008]\] \[[Viglietti et al 2019][research_viglietti_zappino_2019]\] \[[Vinayagamurthy et al 2011][research_vinayagamurthy_parammasivam_2011]\] \[[Vindigni 2023][research_vindigni_2023]\] \[[Voracek 2007][research_voracek_2007]\] \[[Voss 2018][research_voss_2018]\] \[[Waldmann et al 2023][research_waldmann_ehrle_2023]\] \[[Wan et al 2003][research_wan_yang_2003]\] \[[Wang 2019][research_wang_2019]\] \[[Wang 2024][research_wang_2024]\] \[[Wang 2025][research_wang_2025]\] \[[Wang and Tu 2010][research_wang_tu_2010]\] \[[Wang and Zhan 2005][research_wang_zhan_2005]\] \[[Wang et al 2018][research_wang_su_2018]\] \[[Wang et al 2023][research_wang_chen_2023]\] \[[Wang et al 2023][research_wang_qian_2023]\] \[[Wang et al 2023][research_wang_yu_2023]\] \[[Wang et al 2026][research_wang_jia_2026]\] \[[Warwick et al 2019][research_warwick_bras_2019]\] \[[Waszak and Buttrill 1991][research_waszak_buttrill_1991]\] \[[Waszak and Srinathkumar 1992][research_waszak_srinathkumar_1992]\] \[[Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]\] \[[Weisshaar 1978][research_weisshaar_1978]\] \[[Weisshaar 1979][research_weisshaar_1979]\] \[[Weisshaar 1979][research_weisshaar_1979_b]\] \[[Weisshaar 1980][research_weisshaar_1980]\] \[[Weisshaar 1981][research_weisshaar_1981]\] \[[Weisshaar 1983][research_weisshaar_1983]\] \[[Weisshaar 1985][research_weisshaar_1985]\] \[[Weisshaar and Ashley 1973][research_weisshaar_ashley_1973]\] \[[Weisshaar and Ashley 1974][research_weisshaar_ashley_1974]\] \[[Weisshaar and Schmidt 1981][research_weisshaar_schmidt_1981]\] \[[West 1960][research_west_1960]\] \[[Whitcomb et al 1961][research_whitcomb_critzos_1961]\] \[[White 1970][research_white_1970]\] \[[White and Crimi 1961][research_white_crimi_1961]\] \[[Whitlow 1993][research_whitlow_1993]\] \[[Wiggins and Kuhn 1953][research_wiggins_kuhn_1953]\] \[[Wing Loads 1996][research_wing_loads_1996]\] \[[Woo 1992][research_woo_1992]\] \[[Woods and Wood 2000][research_woods_wood_2000]\] \[[Woods et al 1989][research_woods_gilbert_1989]\] \[[Wu et al 2013][research_wu_dai_2013]\] \[[Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]\] \[[Wunderlich et al 2017][research_wunderlich_dahne_2017_b]\] \[[Xiong and Liu 2013][research_xiong_liu_2013]\] \[[Xiong and Nguyen 2024][research_xiong_nguyen_2024]\] \[[Xiong and Yang 2001][research_xiong_yang_2001]\] \[[Xiong et al 2022][research_xiong_nguyen_2022_c]\] \[[Xiong et al 2023][research_xiong_nguyen_2023]\] \[[xu et al 2023][research_xu_song_2023]\] \[[Xue et al 2019][research_xue_ye_2019]\] \[[Yaman and Dalmış 2026][research_yaman_dalmis_2026]\] \[[Yang and Li 2022][research_yang_li_2022]\] \[[Yang and Wan 1978][research_yang_wan_1978]\] \[[Yang et al 1980][research_yang_guruswamy_1980]\] \[[Yaniktepe and Rockwell 2004][research_yaniktepe_rockwell_2004]\] \[[Yao et al 2023][research_yao_song_2023]\] \[[Yates 1960][research_yates_1960]\] \[[Yates 1960][research_yates_1960_b]\] \[[Yates 1963][research_yates_1963]\] \[[Yates 1967][research_yates_1967]\] \[[Yates and Chu 1987][research_yates_chu_1987]\] \[[Yates et al 1982][research_yates_cunningham_1982]\] \[[Yavuz 2012][research_yavuz_2012]\] \[[Yen and Hsu 2007][research_yen_hsu_2007]\] \[[Yu and Hornung 2026][research_yu_hornung_2026]\] \[[Yuan et al 1994][research_yuan_friedman_1994]\] \[[Yuan et al 2016][research_yuan_sandhu_2016]\] \[[Yurkovich 1996][research_yurkovich_1996]\] \[[Zhang and Lu 2026][research_zhang_lu_2026]\] \[[Zhang et al 2014][research_zhang_hua_2014]\] \[[Zhang et al 2017][research_zhang_wei_2017]\] \[[Zhang et al 2018][research_zhang_zhou_2018]\] \[[Zhang et al 2026][research_zhang_deng_2026]\] \[[Zhang et al 2026][research_zhang_zhao_2026]\] \[[Zhao and Kapania 2017][research_zhao_kapania_2017]\] \[[Zhao et al 2023][research_zhao_yang_2023]\] \[[Zhu and Breuer 2022][research_zhu_breuer_2022]\] \[[Zhu et al 2026][research_zhu_zhu_2026]\] \[[Zink et al 2000][research_zink_mavris_2000]\] \[[Zink et al 2001][research_zink_mavris_2001]\]

### Crossflow, transition and the swept-wing boundary layer

**The boundary layer that sweep creates.** Crossflow instability, attachment-line contamination, receptivity and laminar flow control on swept wings, in the tunnel and in flight, including the sweep-dependent transition measured on the F-14.

**404 records.** \[[Gaponov et al 2008][research_agaponov_gyermolaev_2008]\] \[[Abdullaev A et al 2024][research_abdullaeva_moralevi_2024]\] \[[Abegg et al 2000][research_abegg_bippes_2000]\] \[[Afanasyev et al 2025][research_afanasyev_yermolaev_2025]\] \[[Ahmed et al 1989][research_ahmed_wentz_1989]\] \[[Al-Malki et al 2022][research_almalki_fildes_2022]\] \[[Anderson and Meyer 1990][research_anderson_1990]\] \[[Anderson and Meyer 1990][research_anderson_1990_2]\] \[[Aoyagi and Hickey 1959][research_aoyagi_hickey_1959]\] \[[Appel et al 2021][research_appel_cooke_2021]\] \[[Arai et al 2000][research_arai_noto_2000]\] \[[Archambaud et al 2004][research_archambaud_louis_2004]\] \[[Arnal and Juillen 1990][research_arnal_juillen_1990]\] \[[Arnal et al 1990][research_arnal_casalis_1990]\] \[[Arnal et al 2000][research_arnal_seraudie_2000]\] \[[Ayers 1969][research_ayers_1969]\] \[[Barahona et al 2024][research_barahona_weijer_2024]\] \[[Baskaran and Bradshaw 1988][research_baskaran_bradshaw_1988]\] \[[Befus et al 1987][research_befus_nelson_1987]\] \[[Belisle et al 2010][research_belisle_neale_2010]\] \[[Belisle et al 2012][research_belisle_roberts_2012]\] \[[Bender et al 2010][research_bender_westphal_2010]\] \[[Beyak et al][research_beyak_choudhari]\] \[[Beyak et al 2024][research_beyak_choudhari_2024]\] \[[Bidwell 1991][research_bidwell_1991]\] \[[Bippes et al 1997][research_bippes_lerche_1997]\] \[[Biriukov 1959][research_biriukov_1959]\] \[[Boiko 2002][research_boiko_2002]\] \[[Boiko et al 1995][research_boiko_kozlov_1995]\] \[[Boiko et al 2021][research_boiko_borodulin_2021]\] \[[Boiko et al 2024][research_boiko_kirilovskiy_2024]\] \[[Boiko et al 2024][research_boiko_kirilovskiy_2024_b]\] \[[Boltz et al 1960][research_boltz_1960]\] \[[Borodulin et al 2015][research_borodulin_ivanov_2015]\] \[[Borodulin et al 2016][research_borodulin_ivanov_2016]\] \[[Borodulin et al 2017][research_borodulin_ivanov_2017]\] \[[Borodulin et al 2018][research_borodulin_ivanov_2018]\] \[[Borodulin et al 2019][research_borodulin_ivanov_2019]\] \[[Borodulin et al 2019][research_borodulin_ivanov_2019_b]\] \[[Borodulin et al 2020][research_borodulin_ivanov_2020]\] \[[Borodulin et al 2022][research_borodulin_ivanov_2022]\] \[[Borodulin et al 2023][research_borodulin_ivanov_2023]\] \[[Borodulin et al 2023][research_borodulin_ivanov_2023_b]\] \[[Borodulin et al 2024][research_borodulin_ivanov_2024]\] \[[Borodulin et al 2025][research_borodulin_kachanov_2025]\] \[[Borodulin et al 2026][research_borodulin_2026]\] \[[Borodulin et al 2026][research_borodulin_ivanov_2026]\] \[[Botter][research_botter]\] \[[Bradshaw and Pontikos 1985][research_bradshaw_pontikos_1985]\] \[[Braslow 1999][research_braslow_1999]\] \[[Bridges 1994][research_bridges_1994]\] \[[Brinza 2024][research_brinza_2024]\] \[[Campbell and Lynde 2016][research_campbell_lynde_2016]\] \[[Carpenter et al 2008][research_carpenter_saric_2008]\] \[[Carpenter et al 2010][research_carpenter_2010]\] \[[Carpenter et al 2018][research_carpenter_solomon_2018]\] \[[Casacuberta et al 2022][research_casacuberta_groot_2022]\] \[[Casacuberta et al 2023][research_casacuberta_hickel_2023]\] \[[Casacuberta et al 2026][research_casacuberta_groot_2026]\] \[[Cattafesta et al 1995][research_cattafesta_iyer_1995]\] \[[Cebeci 1974][research_cebeci_1974]\] \[[Chang 2003][research_chang_2003]\] \[[Chapman 1961][research_chapman_1961]\] \[[Chen 2018][research_chen_2018]\] \[[Chen et al 2021][research_chen_dong_2021]\] \[[Chernoray et al 2005][research_chernoray_dovgal_2005]\] \[[Chernoray et al 2010][research_chernoray_dovgal_2010]\] \[[Chernoray et al 2013][research_chernoray_dovgal_2013]\] \[[Chernyshev et al 2015][research_chernyshev_kuryachii_2015]\] \[[Choudhari 1996][research_choudhari_1996]\] \[[Choudhari et al 2016][research_choudhari_li_2016]\] \[[Clayton][research_clayton]\] \[[Collier et al 1990][research_collier_bartlett_1990]\] \[[Cooke et al 2019][research_cooke_mughal_2019]\] \[[Creel 1991][research_creel_1991]\] \[[Creel et al 1987][research_creel_malik_1987]\] \[[Cumpsty and Head 1967][research_cumpsty_head_1967]\] \[[Cumpsty and Head 1967][research_cumpsty_head_1967_b]\] \[[Dagenhart 1992][research_dagenhart_1992]\] \[[Dagenhart and Saric 1999][research_dagenhart_saric_1999]\] \[[Dagenhart et al 1989][research_dagenhart_1989]\] \[[Dagenhart et al 1990][research_dagenhart_1990]\] \[[de Rosa et al 2020][research_derosa_donelli_2020]\] \[[De Vincentiis et al 2021][research_devincentiis_henningson_2021]\] \[[Denison et al 2019][research_denison_garai_2019]\] \[[Distributed Surface-Vortex Receptivity of 2025][research_distributed_surface_vortex_receptivity_2025]\] \[[Distributed Surface-Vortex Receptivity of 2025][research_distributed_surface_vortex_receptivity_2025_b]\] \[[Drake and Solomon 2010][research_drake_solomon_2010]\] \[[Dryasov et al 2016][research_dryasov_yermolaev_2016]\] \[[Duan et al 2013][research_duan_choudhari_2013]\] \[[Duncan et al 2013][research_duncan_crawford_2013]\] \[[Edwards 1996][research_edwards_1996]\] \[[Eppink][research_eppink]\] \[[Eppink 2017][research_eppink_2017]\] \[[Eppink 2023][research_eppink_2023]\] \[[Eppink and Wlezien 2012][research_eppink_wlezien_2012]\] \[[Eppink and Yao 2017][research_eppink_yao_2017]\] \[[Eppink and Yao 2017][research_eppink_yao_2017_b]\] \[[Eppink et al 2015][research_eppink_wlezien_2015]\] \[[Eppink et al 2019][research_eppink_wlezien_2019]\] \[[Ermolaev et al 2018][research_ermolaev_kosinov_2018]\] \[[Fan et al 2017][research_fan_song_2017]\] \[[Fan et al 2021][research_fan_yu_2021]\] \[[Fedorov 1988][research_fedorov_1988]\] \[[Fedorov 2012][research_fedorov_2012]\] \[[Fedorov and Egorov 2021][research_fedorov_egorov_2021]\] \[[Fedorov and Novikov 2023][research_fedorov_novikov_2023]\] \[[Fehrs and Kaiser 2025][research_fehrs_2025]\] \[[Fischer et al 1983][research_fischer_wrightjr_1983]\] \[[Fischer et al 1989][research_fischer_ehrenstein_1989]\] \[[Frederick et al 2014][research_frederick_banks_2014]\] \[[Friederich and Kloker 2011][research_friederich_kloker_2011]\] \[[Fujimori and Lin 1973][research_fujimori_lin_1973]\] \[[Funk and Cooney 1959][research_funk_1959]\] \[[Gaponenko et al 1995][research_gaponenko_ivanov_1995]\] \[[Gaponenko et al 2002][research_gaponenko_ivanov_2002]\] \[[Gaster 2008][research_gaster_2008]\] \[[Glauser et al 2011][research_glauser_saric_2011]\] \[[Glauser et al 2014][research_glauser_saric_2014]\] \[[Gorev et al 2007][research_gorev_katasonov_2007]\] \[[Govindarajan and Narasimha 2000][research_govindarajan_narasimha_2000]\] \[[Gowree and Atkin 2017][research_gowree_atkin_2017]\] \[[Guo and Kloker 2026][research_guo_kloker_2026]\] \[[Gürdamar et al 2006][research_gurdamar_cete_2006]\] \[[Haas et al 2021][research_haas_hader_2021]\] \[[Haas et al 2022][research_haas_hader_2022]\] \[[Harvey et al 1990][research_harvey_harris_1990]\] \[[Hawley 1999][research_hawley_1999]\] \[[Haynes and Reed 1996][research_haynes_reed_1996]\] \[[Hickey and Aoyagi 1960][research_hickey_aoyagi_1960]\] \[[Holmes and Obara 1992][research_holmes_obara_1992]\] \[[Horstmann 2008][research_horstmann_2008]\] \[[Hosseini et al 2013][research_hosseini_tempelmann_2013]\] \[[Huai et al 1997][research_huai_piomelli_1997]\] \[[Hunt and Saric 2011][research_hunt_saric_2011]\] \[[Hussain and Bons 2019][research_hussain_bons_2019]\] \[[Ichikawa et al 2026][research_ichikawa_nakagawa_2026]\] \[[Inger 1994][research_inger_1994]\] \[[Inger 1995][research_inger_1995]\] \[[Ishida and Ueshima 2026][research_ishida_ueshima_2026]\] \[[Itoh and Kobayashi 1999][research_itoh_kobayashi_1999]\] \[[Itoh and Kobayashi 2000][research_itoh_kobayashi_2000]\] \[[Ivanov et al 2020][research_ivanov_mischenko_2020]\] \[[Iyer et al 1992][research_iyer_spall_1992]\] \[[Jacobson and Joshi 1977][research_jacobson_joshi_1977]\] \[[Jacobson and Joshi 1978][research_jacobson_joshi_1978]\] \[[Janke et al 2001][research_janke_bertolotti_2001]\] \[[Jansen 1980][research_jansen_1980]\] \[[Jisheng and Heng 1998][research_jisheng_heng_1998]\] \[[Joslin 1995][research_joslin_1995]\] \[[Joslin and Streett 1992][research_joslin_streett_1992]\] \[[Juillen and Arnal 1995][research_juillen_arnal_1995]\] \[[Kachanov 1996][research_kachanov_1996]\] \[[Kachanov and Tararykin 1990][research_kachanov_tararykin_1990]\] \[[Kachanov et al 2016][research_kachanov_borodulin_2016]\] \[[Keller 2019][research_keller_2019]\] \[[Kirilovskiy et al 2019][research_kirilovskiy_boiko_2019]\] \[[Kloker 2008][research_kloker_2008]\] \[[Kohama 1987][research_kohama_1987]\] \[[Kohama 1987][research_kohama_1987_b]\] \[[Kohama et al 1991][research_kohama_1991]\] \[[Kohama et al 1995][research_kohama_kodashima_1995]\] \[[Kolosov and Kosinov 2016][research_kolosov_kosinov_2016]\] \[[Kolosov et al 2017][research_kolosov_kosinov_2017]\] \[[Kosarev et al 2016][research_kosarev_seror_2016]\] \[[Kosinov et al 2016][research_kosinov_kolosov_2016]\] \[[Kozlov et al 2006][research_kozlov_chernoray_2006]\] \[[Kozlov et al 2009][research_kozlov_zverkov_2009]\] \[[Kozlov et al 2014][research_kozlov_grek_2014]\] \[[Krishnan et al][research_krishnan_mukund]\] \[[Kube 2026][research_kube_2026]\] \[[Kuryachii et al 2014][research_kuryachii_manuilovich_2014]\] \[[Kurz and Kloker 2014][research_kurz_kloker_2014]\] \[[Kurz and Kloker 2015][research_kurz_kloker_2015]\] \[[Kurz and Kloker 2016][research_kurz_kloker_2016]\] \[[Laminar flow control wing 1999][research_laminar_flow_1999]\] \[[Lampropoulos et al 2025][research_lampropoulos_sarris_2025]\] \[[Lekoudis 1980][research_lekoudis_1980]\] \[[Lekoudis 1980][research_lekoudis_1980_b]\] \[[Lekoudis 1981][research_lekoudis_1981]\] \[[Levchenko and Scherbakov 1997][research_levchenko_scherbakov_1997]\] \[[Li et al 2010][research_li_choudhari_2010]\] \[[Li et al 2011][research_li_choudhari_2011]\] \[[Li et al 2013][research_li_wang_2013]\] \[[Li et al 2026][research_li_2026]\] \[[Lin and Reed 1993][research_lin_reed_1993]\] \[[Liu et al 2023][research_liu_liu_2023]\] \[[Lombardi et al 1996][research_lombardi_morelli_1996]\] \[[Lombardi et al 1997][research_lombardi_salvetti_1997]\] \[[Lu and Luo 2017][research_lu_luo_2017]\] \[[Lu et al 2025][research_lu_2025]\] \[[Luo and Zhou 2000][research_luo_zhou_2000]\] \[[Lux 1978][research_lux_1978]\] \[[lyer et al 1994][research_lyer_spall_1994]\] \[[Lynde and Campbell 2017][research_lynde_campbell_2017]\] \[[Lynde et al 2021][research_lynde_campbell_2021]\] \[[Mack 1979][research_mack_1979]\] \[[Maddalon and Wagner 1986][research_maddalon_wagner_1986]\] \[[Maddalon et al 1989][research_maddalon_collier_1989]\] \[[Maddalon et al 1990][research_maddalon_collier_1990]\] \[[Maki 1959][research_maki_1959]\] \[[Malik and Li 1993][research_malik_li_1993]\] \[[Malik et al 1996][research_malik_li_1996]\] \[[Malik et al 1999][research_malik_li_1999]\] \[[Malik et al 2013][research_malik_liao_2013]\] \[[Malik et al 2015][research_malik_liao_2015]\] \[[Manuilovich 2014][research_manuilovich_2014]\] \[[Manuilovich 2021][research_manuilovich_2021]\] \[[Manuilovich 2023][research_manuilovich_2023]\] \[[Martin 2008][research_martin_2008]\] \[[Martin et al 2008][research_martin_carpenter_2008]\] \[[Mathioulakis and Georgantopoulou 2025][research_mathioulakis_georgantopoulou_2025]\] \[[Matsuno et al 2020][research_matsuno_esaki_2020]\] \[[Mavriplis et al 2020][research_mavriplis_yang_2020]\] \[[McFadden et al 2022][research_mcfadden_brandt_2022_b]\] \[[Meneghello et al 2015][research_meneghello_schmid_2015]\] \[[Meng et al 2025][research_meng_lei_2025]\] \[[Methel et al 2022][research_methel_mery_2022]\] \[[Method of the Qualitative 2020][research_method_of_2020]\] \[[Michel et al 1985][research_michel_arnal_1985]\] \[[Mignosi et al 1986][research_mignosi_dor_1986]\] \[[Mistry et al 2012][research_mistry_page_2012]\] \[[Mistry et al 2013][research_mistry_page_2013]\] \[[Miwa et al 2022][research_miwa_yoshimi_2022]\] \[[Mori et al 2024][research_mori_yakeno_2024]\] \[[Mori et al 2024][research_mori_yakeno_2024_b]\] \[[Mousseux et al 1989][research_mousseux_1989]\] \[[Mughal and Ashworth 2013][research_mughal_ashworth_2013]\] \[[Müller et al 2020][research_muller_lutz_2020]\] \[[Nagamatsu and Ficarra 1985][research_nagamatsu_ficarra_1985]\] \[[Nakagawa et al 2023][research_nakagawa_ishida_2023]\] \[[Nangia et al 2003][research_nangia_palmer_2003_b]\] \[[Nangia et al 2005][research_nangia_palmer_2005]\] \[[Nellner 1993][research_nellner_1993]\] \[[Nellner and Zierep 1993][research_nellner_zierep_1993]\] \[[Neyland and Filippov 2004][research_neyland_filippov_2004]\] \[[Ng and Crouch 1999][research_ng_crouch_1999]\] \[[Nguyen et al 2016][research_nguyen_tran_2016]\] \[[Nicholson et al 2018][research_nicholson_zhang_2018]\] \[[Nicholson et al 2019][research_nicholson_duan_2019]\] \[[Nishino and Shariff 2009][research_nishino_shariff_2009]\] \[[Nitschke-Kowsky and Bippes 1988][research_nitschkekowsky_bippes_1988]\] \[[Nomura 2003][research_nomura_2003]\] \[[Nomura 2006][research_nomura_2006]\] \[[Novikov et al 2024][research_novikov_obraz_2024]\] \[[Ohira et al 2013][research_ohira_kwak_2013]\] \[[Panina et al 2021][research_panina_yatskikh_2021]\] \[[Pate and Brillhart 1963][research_pate_brillhart_1963]\] \[[Pate and Deitering 1963][research_pate_deitering_1963]\] \[[Pate and Deitering 1963][research_pate_deitering_1963_b]\] \[[Peck et al 2024][research_peck_groot_2024]\] \[[Peltzer et al 2009][research_peltzer_wicke_2009]\] \[[Peng et al 2022][research_peng_avallone_2022]\] \[[Peng et al 2024][research_peng_avallone_2024]\] \[[Penner et al 2025][research_penner_sousa_2025]\] \[[Perez et al 2011][research_perez_rodriguez_2011]\] \[[Perraud et al 2003][research_perraud_moens_2003]\] \[[Perraud et al 2004][research_perraud_seraudie_2004]\] \[[Pfenninger and Bacon 1961][research_pfenninger_bacon_1961]\] \[[Pfenninger and Bacon 1969][research_pfenninger_bacon_1969]\] \[[Pfenninger and Groth 1961][research_pfenninger_groth_1961]\] \[[Pfenninger and Vemuru 1988][research_pfenninger_vemuru_1988]\] \[[Philipsen et al 2015][research_philipsen_postma_2015]\] \[[Pier 2003][research_pier_2003]\] \[[Poll and Danks 1995][research_poll_danks_1995]\] \[[Poll and Paisley 1985][research_poll_paisley_1985]\] \[[Pruett et al 2000][research_pruett_chang_2000]\] \[[Pérez et al 2012][research_perez_rodriguez_2012]\] \[[Pérez Pérez][research_perezperez]\] \[[Quan et al 2026][research_quan_deng_2026]\] \[[Quast et al 1990][research_quast_henke_1990]\] \[[Quigley et al 1960][research_quigley_1960]\] \[[Radeztsky et al 1995][research_radeztsky_reibert_1995]\] \[[Radzetsky et al 1994][research_radzetskyjr_reibert_1994]\] \[[Rambacher et al 2024][research_rambacher_butler_2024]\] \[[Redeker and Wichmann 1988][research_redeker_wichmann_1988]\] \[[Redeker and Wichmann 1991][research_redeker_wichmann_1991]\] \[[Reed 1989][research_reed_1989]\] \[[Reed and Saric 2002][research_reed_saric_2002]\] \[[Reeh et al 2013][research_reeh_weismuller_2013]\] \[[Reeh et al 2014][research_reeh_weismuller_2014]\] \[[Reibert et al 1996][research_reibert_saric_1996]\] \[[Reibert et al 1997][research_reibert_saric_1997]\] \[[Reid et al 1994][research_reid_rajagopal_1994]\] \[[Reshotko et al 2000][research_reshotko_vargas_2000]\] \[[Riahi and Vonderwell 1994][research_riahi_vonderwell_1994]\] \[[Ribeiro et al 2022][research_ribeiro_yeh_2022]\] \[[Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]\] \[[Rizzo et al 2019][research_rizzo_serpieri_2019]\] \[[Roberts et al 2012][research_roberts_reed_2012]\] \[[Romano et al 2017][research_romano_derosa_2017]\] \[[Runyan and George-Falvy 1979][research_runyan_georgefalvy_1979]\] \[[Saeed and Graham 2015][research_saeed_graham_2015]\] \[[Saeed et al 2016][research_saeed_mughal_2016]\] \[[Sakakibara et al 2021][research_sakakibara_nimura_2021]\] \[[Saric 1996][research_saric_1996]\] \[[Saric 1997][research_saric_1997]\] \[[Saric 2010][research_saric_2010]\] \[[Saric and Yeates 1985][research_saric_yeates_1985]\] \[[Saric et al 1990][research_saric_dagenhart_1990]\] \[[Saric et al 2015][research_saric_west_2015]\] \[[Saric et al 2019][research_saric_west_2019]\] \[[Schuelein 2008][research_schuelein_2008]\] \[[Semionov and Kosinov 2007][research_semionov_kosinov_2007]\] \[[Semionov et al 2006][research_semionov_kosinov_2006]\] \[[Semionov et al 2009][research_semionov_kosinov_2009]\] \[[Semionov et al 2011][research_semionov_kosinov_2011]\] \[[Semionov et al 2011][research_semionov_kosinov_2011_b]\] \[[Semionov et al 2013][research_semionov_kosinov_2013]\] \[[Semionov et al 2017][research_semionov_yermolaev_2017]\] \[[Semionov et al 2018][research_semionov_yermolaev_2018]\] \[[Semionov et al 2022][research_semionov_yermolaev_2022]\] \[[Sengupta and Dipankar 2005][research_sengupta_dipankar_2005]\] \[[Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]\] \[[Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016]\] \[[Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016_b]\] \[[Shahriari et al 2018][research_shahriari_kollert_2018]\] \[[Shipul et al 2024][research_shipul_kosinov_2024]\] \[[Sorenson 1974][research_sorenson_1974]\] \[[Sousa and Silva 2004][research_sousa_silva_2004]\] \[[Speer et al 2004][research_speer_zhong_2004]\] \[[Steers 1981][research_steers_1981]\] \[[Stewartson 1981][research_stewartson_1981]\] \[[Stock 2005][research_stock_2005]\] \[[Suardi et al 2020][research_suardi_pinelli_2020]\] \[[Subaschandar and Prabhu 2002][research_subaschandar_prabhu_2002]\] \[[Sugiura et al 2001][research_sugiura_yoshida_2001]\] \[[Séraudie et al 2003][research_seraudie_perraud_2003]\] \[[Taylor et al 1997][research_taylor_peake_1997]\] \[[Tempelmann et al 2011][research_tempelmann_schrader_2011]\] \[[Tempelmann et al 2012][research_tempelmann_hanifi_2012]\] \[[Tempelmann et al 2012][research_tempelmann_schrader_2012]\] \[[The stability of the 1979][research_the_stability_1979]\] \[[Theofilis 1998][research_theofilis_1998]\] \[[Theofilis and Dallmann 1997][research_theofilis_dallmann_1997]\] \[[Theofilis et al 1990][research_theofilis_duck_1990]\] \[[Thomas et al 2016][research_thomas_mughal_2016]\] \[[Thomas et al 2017][research_thomas_mughal_2017]\] \[[Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]\] \[[Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]\] \[[Tolkachev et al 2022][research_tolkachev_kiselev_2022]\] \[[Tolkachev et al 2024][research_tolkachev_baranov_2024]\] \[[Touzani 1987][research_touzani_1987]\] \[[Transonic flight test of 1994][research_transonic_flight_1994]\] \[[Tucker et al 2014][research_tucker_saric_2014]\] \[[Tufts et al 2014][research_tufts_suffixjrsuffix_2014]\] \[[Tufts et al 2015][research_tufts_reed_2015]\] \[[Turbeville and Schneider 2018][research_turbeville_schneider_2018]\] \[[Ustinov 2001][research_ustinov_2001]\] \[[Ustinov 2013][research_ustinov_2013]\] \[[Ustinov 2017][research_ustinov_2017]\] \[[Ustinov 2018][research_ustinov_2018]\] \[[Ustinov 2018][research_ustinov_2018_b]\] \[[Ustinov 2021][research_ustinov_2021]\] \[[Van Den Berg et al 1975][research_vandenberg_elsenaar_1975]\] \[[Vasile et al 2010][research_vasile_elimelech_2010]\] \[[Vavra et al 2005][research_vavra_solomon_2005]\] \[[Vermeersch et al 2015][research_vermeersch_yoshida_2015]\] \[[Viken et al 1990][research_viken_collier_1990]\] \[[Vonderwell and Riahi 1998][research_vonderwell_riahi_1998]\] \[[Waggoner 1986][research_waggoner_1986]\] \[[Waggoner et al 1986][research_waggoner_campbell_1986]\] \[[Wagner et al 1986][research_wagner_fisher_1986]\] \[[Wagner et al 1988][research_wagner_bartlett_1988]\] \[[Wagner et al 1988][research_wagner_maddalon_1988]\] \[[Wagner et al 1992][research_wagner_maddalon_1992]\] \[[Walker and Bons 2018][research_walker_bons_2018]\] \[[Wang et al 1994][research_wang_herbert_1994]\] \[[Wang et al 1994][research_wang_herbert_1994_b]\] \[[Wang et al 2025][research_wang_duan_2025]\] \[[Wang et al 2025][research_wang_tu_2025]\] \[[Wang et al 2026][research_wang_2026_2]\] \[[Wang et al 2026][research_wang_tu_2026]\] \[[Warren et al 1997][research_warren_hassan_1997]\] \[[Wentz et al 1985][research_wentz_ahmed_1985]\] \[[Wentz and Nyenhuis 1984][research_wentzjr_nyenhuis_1984]\] \[[Werner et al 2022][research_werner_schutte_2022]\] \[[White et al 2001][research_white_saric_2001]\] \[[Wildschek et al 2009][research_wildschek_maier_2009]\] \[[Woodruff et al 2011][research_woodruff_saric_2011]\] \[[Wu and Squires 1995][research_wu_squires_1995]\] \[[Xu and Wu 2022][research_xu_wu_2022]\] \[[Xu et al 2019][research_xu_chen_2019]\] \[[Xu et al 2019][research_xu_han_2019_b]\] \[[Xu et al 2021][research_xu_han_2021]\] \[[Xu et al 2021][research_xu_he_2021]\] \[[Yadala Venkata et al 2018][research_yadalavenkata_hehner_2018]\] \[[Yakeno and Obayashi 2021][research_yakeno_obayashi_2021]\] \[[Yamamoto et al 2012][research_yamamoto_tanaka_2012]\] \[[Yang et al 2021][research_yang_zhong_2021]\] \[[Yang et al 2022][research_yang_wang_2022]\] \[[Yasuaki and Egami 1999][research_yasuaki_egami_1999]\] \[[Yatskikh et al 2017][research_yatskikh_rumenskikh_2017]\] \[[Ye 2025][research_ye_2025]\] \[[Yen and Hsu 2006][research_yen_hsu_2006]\] \[[Yermolaev et al 2014][research_yermolaev_kosinov_2014]\] \[[Yermolaev et al 2017][research_yermolaev_yatskikh_2017]\] \[[Yermolaev et al 2020][research_yermolaev_yatskikh_2020]\] \[[Zeng and Kukreja 2013][research_zeng_kukreja_2013]\] \[[Zhang et al 2017][research_zhang_liu_2017]\] \[[Zhao 1998][research_zhao_1998]\] \[[Zhu et al 2019][research_zhu_li_2019]\] \[[Zoppini et al 2022][research_zoppini_ragni_2022]\] \[[Zoppini et al 2022][research_zoppini_ragni_2022_b]\]

### Spin, stall, departure and recovery

**The hazard that ended the second aircraft.** Spin-tunnel model reports, spin-recovery devices and techniques, stall and departure of swept and general aviation configurations, and the recent recasting of recovery as a control problem.

**363 records.** \[[Adams 1973][research_adams_1973]\] \[[Airplane Spin Testing 2003][research_airplane_spin_2003]\] \[[Allred and Fleck 1992][research_allred_fleck_1992]\] \[[Amano et al 2011][research_amano_avdeev_2011]\] \[[Anderson 1978][research_anderson_1978]\] \[[Anderson 1979][research_anderson_1979]\] \[[Anderson 1984][research_anderson_1984]\] \[[Anderson 1985][research_anderson_1985]\] \[[Anderson et al 1983][research_anderson_enevoldson_1983]\] \[[Anglin 1965][research_anglin_1965]\] \[[Anglin 1967][research_anglin_1967]\] \[[Anglin 1978][research_anglin_1978]\] \[[Arcidiacono et al 1970][research_arcidiacono_carta_1970]\] \[[Arena and Nelson 1989][research_arena_nelson_1989]\] \[[Attar and Gordnier 2008][research_attar_gordnier_2008]\] \[[Bagheri and Danesh 2025][research_bagheri_2025]\] \[[Ballin 1982][research_ballin_1982]\] \[[Bamber and House 1937][research_bamber_house_1937]\] \[[Bennett and Lawson 2018][research_bennett_lawson_2018]\] \[[Bennett et al 2017][research_bennett_lawson_2017]\] \[[Berman 1947][research_berman_1947]\] \[[Berman 1948][research_berman_1948]\] \[[Berman 1949][research_berman_1949]\] \[[Berman 1949][research_berman_1949_b]\] \[[Berman and Pumphrey 1950][research_berman_pumphrey_1950]\] \[[Berrier 1980][research_berrier_1980]\] \[[Beyers and Brown 2006][research_beyers_brown_2006]\] \[[Bihrle 1976][research_bihrle_1976]\] \[[Black 1956][research_black_1956]\] \[[Blanchard 1981][research_blanchard_1981]\] \[[Bowman 1955][research_bowman_1955]\] \[[Bowman 1955][research_bowman_1955_b]\] \[[Bowman 1956][research_bowman_1956]\] \[[Bowman 1956][research_bowman_1956_b]\] \[[Bowman 1957][research_bowman_1957]\] \[[Bowman 1958][research_bowman_1958]\] \[[Bowman 1965][research_bowman_1965]\] \[[Bowman 1965][research_bowman_1965_b]\] \[[Bowman 1966][research_bowman_1966]\] \[[Bowman 1971][research_bowman_1971]\] \[[Bowman and Burk 1973][research_bowman_burk_1973]\] \[[Bowman and Burk 1974][research_bowman_burk_1974]\] \[[Bowman and Chambers 1970][research_bowman_chambers_1970]\] \[[Bowman and Healy 1958][research_bowman_healy_1958]\] \[[Bowman and Healy 1959][research_bowman_1959]\] \[[Bowman and Healy 1959][research_bowman_healy_1959]\] \[[Bowman and Healy 1960][research_bowman_1960]\] \[[Bowman et al 1987][research_bowman_whipple_1987]\] \[[Bowman et al 1978][research_bowmanjr_stough_1978]\] \[[Bradshaw 1980][research_bradshaw_1980]\] \[[Bramantya and Nugroho 2025][research_bramantya_nugroho_2025]\] \[[Briggs et al 1982][research_briggs_reed_1982]\] \[[Browman and Healy 1959][research_browman_healy_1959]\] \[[Bui 2013][research_bui_2013]\] \[[Bui 2015][research_bui_2015]\] \[[Bui 2016][research_bui_2016]\] \[[Bunge et al 2015][research_bunge_munerasavino_2015]\] \[[Bunge et al 2016][research_bunge_alkurdi_2016]\] \[[Burk 1971][research_burk_1971]\] \[[Burk 1972][research_burk_1972]\] \[[Burk 1974][research_burk_1974]\] \[[Burk and Healy 1955][research_burk_1955]\] \[[Burk and Libbey 1961][research_burk_1961]\] \[[Burk and Wilson 1975][research_burk_wilson_1975]\] \[[Burk et al 1977][research_burk_1977]\] \[[Burris and Hutchins 1970][research_burris_hutchins_1970]\] \[[Buzica et al 2018][research_buzica_biswanger_2018]\] \[[Calico and Fuller 1981][research_calicojr_fuller_1981]\] \[[Casteel and Weyl 1970][research_casteel_weyl_1970]\] \[[Chambers and Bowman 1971][research_chambers_bowman_1971]\] \[[Chambers and Stough 1986][research_chambers_stough_1986]\] \[[Chinvorarat et al 2024][research_chinvorarat_watjatrakul_2024]\] \[[Chung et al 2019][research_chung_cho_2019]\] \[[Clark and Spurlin 1962][research_clark_spurlin_1962]\] \[[Cobleigh 1994][research_cobleigh_1994]\] \[[Craig 1976][research_craig_1976]\] \[[Culler and Farnsworth 2019][research_culler_farnsworth_2019]\] \[[Cunis][research_cunis]\] \[[Currao and Jiang 2026][research_currao_jiang_2026]\] \[[Cvetkovi et al 2012][research_cvetkovi_radakovi_2012]\] \[[De Voogt and Ganapathisubramani 2022][research_devoogt_ganapathisubramani_2022]\] \[[Del Frate 1992][research_delfrate_1992]\] \[[Dicarlo and Johnson 1979][research_dicarlo_johnson_1979]\] \[[Dicarlo et al 1984][research_dicarlo_glover_1984]\] \[[Dongmo 2011][research_dongmo_2011]\] \[[Engelbrecht et al 2012][research_engelbrecht_pauck_2012]\] \[[Ericsson 1983][research_ericsson_1983]\] \[[Ericsson 1985][research_ericsson_1985]\] \[[Ericsson 1996][research_ericsson_1996_c]\] \[[Ericsson 1997][research_ericsson_1997]\] \[[Ericsson 1998][research_ericsson_1998]\] \[[Estevadeordal et al 2022][research_estevadeordal_ullah_2022]\] \[[Exploratory study of the 1979][research_exploratory_study_1979]\] \[[Fagley et al 2016][research_fagley_seidel_2016]\] \[[Fala 2022][research_fala_2022]\] \[[Farcy et al 2020][research_farcy_khrabrov_2020]\] \[[Faure and Leogrande 2020][research_faure_2020]\] \[[Feistel et al 1978][research_feistel_anderson_1978]\] \[[Flat spin 2001][research_flat_spin_2001]\] \[[Foster and Fitzpatrick 1948][research_foster_1948]\] \[[Fouda and Taha 2022][research_fouda_taha_2022]\] \[[Fremaux 1997][research_fremaux_1997]\] \[[Fuchs 1930][research_fuchs_1930]\] \[[Fuchs and Schmidt 1931][research_fuchs_schmidt_1931]\] \[[Gale 1948][research_gale_1948]\] \[[Gale and Pumphrey 1950][research_gale_1950]\] \[[Garmann and Visbal 2020][research_garmann_visbal_2020]\] \[[Garmann and Visbal 2021][research_garmann_visbal_2021]\] \[[Garmann and Visbal 2022][research_garmann_visbal_2022]\] \[[Garmann and Visbal 2022][research_garmann_visbal_2022_b]\] \[[Garmann and Visbal 2023][research_garmann_visbal_2023]\] \[[Go and Ramnath 2001][research_go_ramnath_2001]\] \[[Golovkin et al 2019][research_golovkin_gorbunov_2019]\] \[[Goraj et al 2002][research_goraj_baron_2002]\] \[[Grafton 1966][research_grafton_1966]\] \[[Grafton and Grantham 1965][research_grafton_grantham_1965]\] \[[Grafton et al 1974][research_grafton_chambers_1974]\] \[[Grafton et al 1982][research_grafton_gilber_1982]\] \[[Grantham and Scher 1960][research_grantham_scher_1960]\] \[[Gresham et al 2024][research_gresham_simmons_2024]\] \[[Gunasekaran and Mukherjee 2016][research_gunasekaran_mukherjee_2016]\] \[[Hall and Woodson 2003][research_hall_woodson_2003]\] \[[Hammer et al 2021][research_hammer_garmann_2021]\] \[[Hammer et al 2023][research_hammer_garmann_2023]\] \[[Hebbar and Leedy 1992][research_hebbar_leedy_1992]\] \[[Herrmann 1929][research_herrmann_1929]\] \[[Hoehler 1949][research_hoehler_1949]\] \[[Hoff and Gratton 2013][research_hoff_gratton_2013]\] \[[Holcomb 1979][research_holcomb_1979]\] \[[Hosangadi et al 2015][research_hosangadi_paul_2015]\] \[[Huang et al 2026][research_huang_2026]\] \[[Huffschmid 1950][research_huffschmid_1950]\] \[[Hwang and Pi 1978][research_hwang_pi_1978]\] \[[I 1938][research_i_1938]\] \[[Iliff 1980][research_iliff_1980]\] \[[Imbrie 1981][research_imbrie_1981]\] \[[Inertia Coupling and Spin 2004][research_inertia_coupling_2004]\] \[[Inertia Coupling and Spin 2015][research_inertia_coupling_2015]\] \[[Irving 1933][research_irving_1933]\] \[[Isogai 2013][research_isogai_2013]\] \[[Jamwal et al 2018][research_jamwal_hosangadi_2018]\] \[[Jaramillo et al 1995][research_jaramillo_cho_1995]\] \[[Jin Song et al 2012][research_jinsong_junma_2012]\] \[[Johnson and Lind 2009][research_johnson_lind_2009]\] \[[Johnson and Lind 2010][research_johnson_lind_2010]\] \[[Johnson and Willen 1976][research_johnson_willen_1976]\] \[[Johnson et al 1980][research_johnson_grafton_1980]\] \[[Jones and Klinar 1950][research_jones_klinar_1950]\] \[[Kapuscinski et al 2020][research_kapuscinski_2020]\] \[[Katz and Feistel 1987][research_katz_feistel_1987]\] \[[Kerr 1954][research_kerr_1954]\] \[[Kim et al 2017][research_kim_oh_2017]\] \[[Klein and Batterson 1983][research_klein_batterson_1983]\] \[[Klein et al 1981][research_klein_batterson_1981]\] \[[Klinar and Healy 1952][research_klinar_healy_1952]\] \[[Klinar and Jones 1948][research_klinar_jones_1948]\] \[[Klinar and Jones 1949][research_klinar_1949]\] \[[Klinar and Lee 1954][research_klinar_lee_1954]\] \[[Klinar and Lee 1955][research_klinar_lee_1955]\] \[[Klinar and Snyder 1948][research_klinar_snyder_1948]\] \[[Klinar and Wilson 1950][research_klinar_1950]\] \[[Knight 1928][research_knight_1928]\] \[[Kohama and Suda 1993][research_kohama_suda_1993]\] \[[Kroeger and Feistel 1976][research_kroeger_feistel_1976]\] \[[Kumar et al 2004][research_kumar_raghavendra_2004]\] \[[Kumar et al 2025][research_kumar_palanivel_2025]\] \[[Lee 1952][research_lee_1952]\] \[[Lee 1963][research_lee_1963]\] \[[Lee 1964][research_lee_1964]\] \[[Lee 1964][research_lee_1964_b]\] \[[Lee 1969][research_lee_1969]\] \[[Lee 1969][research_lee_1969_b]\] \[[Lee 1970][research_lee_1970]\] \[[Lee and Batina 1991][research_lee_batina_1991]\] \[[Lee and Healy 1964][research_lee_1964_2]\] \[[Lee and Libbey 1961][research_lee_libbey_1961]\] \[[Lee and Nagati 2004][research_lee_nagati_2004]\] \[[Li et al 2025][research_li_tu_2025]\] \[[Li et al 2026][research_li_tu_2026]\] \[[Lina and Moul 1965][research_lina_moul_1965]\] \[[Lindsay 2021][research_lindsay_2021]\] \[[Lorber 1992][research_lorber_1992_b]\] \[[Lorber and Carta 1991][research_lorber_carta_1991]\] \[[Lorber et al 1991][research_lorber_covinojr_1991]\] \[[Lucy 1985][research_lucy_1985]\] \[[Lutze and Lluch 1996][research_lutze_lluch_1996]\] \[[MacDougall and Lichtenstein 1946][research_macdougall_lichtenstein_1946]\] \[[Malcolm 1978][research_malcolm_1978]\] \[[Malcolm 1979][research_malcolm_1979]\] \[[Malcolm and Clarkson 1976][research_malcolm_clarkson_1976]\] \[[Malcolm and Davis 1978][research_malcolm_davis_1978]\] \[[Malik et al 2017][research_malik_akhtar_2017]\] \[[Malik et al 2017][research_malik_akhtar_2017_b]\] \[[Malik et al 2020][research_malik_masud_2020]\] \[[Malik et al 2021][research_malik_masud_2021]\] \[[Malvestuto 1946][research_malvestuto_1946]\] \[[Malvestuto 1948][research_malvestuto_1948]\] \[[Mancini et al 1976][research_mancini_matsuhiro_1976]\] \[[Manor and Wentz 1985][research_manor_wentz_1985]\] \[[Marquart 1993][research_marquart_1993]\] \[[Marschalk et al 2021][research_marschalk_luteijn_2021]\] \[[Martin and Hill 1989][research_martin_hill_1989]\] \[[Masud et al 2016][research_masud_malik_2016]\] \[[McConnell 2004][research_mcconnell_2004]\] \[[McElroy and Sharp 1971][research_mcelroy_sharp_1971]\] \[[McFall 1964][research_mcfall_1964]\] \[[Medina et al 2019][research_medina_rockwood_2019]\] \[[Moghadam et al 2018][research_moghadam_ure_2018]\] \[[Montgomery and Moul 1966][research_montgomery_moul_1966]\] \[[Moore et al 1980][research_moore_skow_1980]\] \[[Murch and Foster 2007][research_murch_foster_2007]\] \[[Murri et al 1983][research_murri_croom_1983]\] \[[Neihouse 1940][research_neihouse_1940]\] \[[Neihouse 1949][research_neihouse_1949]\] \[[Neihouse and Carmel 1942][research_neihouse_carmel_1942]\] \[[Neihouse and Lee 1951][research_neihouse_lee_1951]\] \[[Neihouse et al 1946][research_neihouse_lichtenstein_1946]\] \[[Ng et al 1993][research_ng_skaff_1993]\] \[[Ng et al 1994][research_ng_skaff_1994]\] \[[Nial 1972][research_nial_1972]\] \[[Nowak and Solies 2000][research_nowak_solies_2000]\] \[[Pabla 2021][research_pabla_2021]\] \[[Pamadi 1988][research_pamadi_1988]\] \[[Pamadi and Taylor 1982][research_pamadi_taylor_1982]\] \[[Paranjape 2022][research_paranjape_2022]\] \[[Paranjape 2023][research_paranjape_2023]\] \[[Paranjape and Ananthkrishnan 2010][research_paranjape_ananthkrishnan_2010]\] \[[Patton 1980][research_patton_1980]\] \[[Patton 1980][research_patton_1980_b]\] \[[Patton et al 1979][research_patton_stough_1979]\] \[[Pavelka and Tatum 1980][research_pavelka_tatum_1980]\] \[[Pepoon 1944][research_pepoon_1944]\] \[[Phillips and Anderson 2002][research_phillips_anderson_2002_b]\] \[[Pirrung et al 2026][research_pirrung_sorensen_2026]\] \[[Pitkin 1943][research_pitkin_1943]\] \[[Planeaux 1991][research_planeaux_1991]\] \[[Poplingher and Raveh 2023][research_poplingher_raveh_2023]\] \[[Poplingher and Raveh 2024][research_poplingher_raveh_2024]\] \[[Pratt and Shields 1952][research_pratt_shields_1952]\] \[[Pusztai et al 2024][research_pusztai_lowenberg_2024]\] \[[Quan et al 2013][research_quan_ye_2013]\] \[[Raghavendra et al 2005][research_raghavendra_sahai_2005]\] \[[Ramirez Zeigler and Avery 2026][research_ramirezzeigler_avery_2026]\] \[[Rao 1992][research_rao_1992]\] \[[Rao and Sinha 2010][research_rao_sinha_2010]\] \[[Razak et al 2011][research_razak_andrianne_2011]\] \[[Rockwood et al 2019][research_rockwood_medina_2019]\] \[[Rogalski et al 2020][research_rogalski_rzucidlo_2020]\] \[[Rose et al 1952][research_rose_jr_1952]\] \[[Salahudden 2024][research_salahudden_2024]\] \[[Salahudden 2025][research_salahudden_2025]\] \[[Salahudden 2025][research_salahudden_2025_2]\] \[[Salahudden 2026][research_salahudden_2026]\] \[[Salahudden and Ghosh 2021][research_salahudden_2021]\] \[[Salahudden and Ghosh 2022][research_salahudden_ghosh_2022]\] \[[Salahudden and Ghosh 2022][research_salahudden_ghosh_2022_b]\] \[[Salahudden et al 2020][research_salahudden_dwivedi_2020]\] \[[Salahudden et al 2020][research_salahudden_giri_2020]\] \[[Salahudden et al 2021][research_salahudden_dwivedi_2021]\] \[[Salahudden et al 2022][research_salahudden_das_2022]\] \[[Salahudden et al 2023][research_salahudden_sanwale_2023]\] \[[Salahudden et al 2024][research_salahudden_singh_2024]\] \[[Salahudden et al 2025][research_salahudden_kumar_2025]\] \[[Salari and Roache 1990][research_salari_roache_1990]\] \[[Samuel and Mukherjee 2016][research_samuel_mukherjee_2016]\] \[[Schairer 1941][research_schairer_1941]\] \[[Scher 1947][research_scher_1947]\] \[[Scher 1947][research_scher_1947_b]\] \[[Scher 1951][research_scher_1951]\] \[[Scher and Draper 1950][research_scher_draper_1950]\] \[[Scher and White 1977][research_scher_1977]\] \[[Schuster and Byrd 2003][research_schuster_byrd_2003]\] \[[Scudder 1933][research_scudder_1933]\] \[[Scudder 1937][research_scudder_1937]\] \[[Scudder and Seidman 1935][research_scudder_seidman_1935]\] \[[Seidman 1942][research_seidman_1942]\] \[[Seidman and McAvoy 1940][research_seidman_mcavoy_1940]\] \[[Sereez et al 2024][research_sereez_abramov_2024]\] \[[Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]\] \[[Shah et al 2003][research_shah_unnikrishnan_2003]\] \[[Shahzad et al 2012][research_shahzad_hamdani_2012]\] \[[Shao et al 2022][research_shao_liu_2022]\] \[[Shumsky 2006][research_shumsky_2006]\] \[[Sibilski and Wróblewski 2012][research_sibilski_wroblewski_2012]\] \[[Sidoryuk and Khrabrov 2019][research_sidoryuk_khrabrov_2019]\] \[[Sliwa 1979][research_sliwa_1979]\] \[[Snyder 1947][research_snyder_1947]\] \[[Snyder 1947][research_snyder_1947_b]\] \[[Snyder 1948][research_snyder_1948]\] \[[Squires 2002][research_squires_2002]\] \[[Stall Characteristics 2003][research_stall_characteristics_2003]\] \[[Stall Speed Measurement 2003][research_stall_speed_2003]\] \[[Stallings and Lamb 1981][research_stallingsjr_lamb_1981]\] \[[Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]\] \[[Stone and Berman 1946][research_stone_berman_1946]\] \[[Stone and Burk 1947][research_stone_1947]\] \[[Stone and Daughtridge 1948][research_stone_daughtridge_1948]\] \[[Stone and Klinar 1948][research_stone_1948]\] \[[Stough 1990][research_stough_1990]\] \[[Stough 1993][research_stough_1993]\] \[[Stough and Patton 1979][research_stough_1979]\] \[[Stough et al 1984][research_stough_dicarlo_1984]\] \[[Stough et al 1985][research_stough_dicarlo_1985]\] \[[Stough et al 1985][research_stough_jordan_1985]\] \[[Stough et al 1987][research_stough_1987]\] \[[Stough et al 1991][research_stough_1991]\] \[[Study on Flat Tail 2022][research_study_on_2022]\] \[[Suarez et al 1992][research_suarez_kramer_1992]\] \[[Suarez et al 1993][research_suarez_smith_1993]\] \[[Tapolcai et al 2012][research_tapolcai_omran_2012]\] \[[Taylor and Miller 1982][research_taylor_miller_1982]\] \[[Telionis 1995][research_telionis_1995]\] \[[Telionis 2001][research_telionis_2001]\] \[[Temgoua Dongmo and Kwatny][research_temgouadongmo_kwatny]\] \[[The effects of canard-wing 1988][research_the_effects_1988]\] \[[Thurston 1934][research_thurston_1934]\] \[[Tischler and Barlow 1979][research_tischler_barlow_1979]\] \[[Tischler and Barlow 1980][research_tischler_barlow_1980]\] \[[Tischler and Barlow 1980][research_tischler_barlow_1980_b]\] \[[Tischler and Barlow 1981][research_tischler_barlow_1981]\] \[[Tischler and Barlow 1982][research_tischler_barlow_1982]\] \[[Tomek et al 2020][research_tomek_ullah_2020]\] \[[Tumlinson et al 1981][research_tumlinson_holcomb_1981]\] \[[Ullah et al 2021][research_ullah_tomek_2021]\] \[[Ullah et al 2022][research_ullah_fabijanic_2022]\] \[[Venkateswara Rao and Go 2019][research_rao_spin_2019]\] \[[Visbal and Garmann 2019][research_visbal_garmann_2019]\] \[[Walchli 1994][research_walchli_1994]\] \[[Walchli et al 1992][research_walchli_guyton_1992]\] \[[Wang 1979][research_wang_1979]\] \[[Wang et al 2024][research_wang_wang_2024]\] \[[Ward et al 1976][research_ward_bennett_1976]\] \[[Weissman 1969][research_weissman_1969]\] \[[Weissman 1973][research_weissman_1973]\] \[[Weissman 1975][research_weissman_1975]\] \[[Whipple 1980][research_whipple_1980]\] \[[Whipple 1982][research_whipple_1982]\] \[[Whipple and White 1984][research_whipple_1984]\] \[[White 1947][research_white_1947]\] \[[White 1985][research_white_1985]\] \[[White 1985][research_white_1985_b]\] \[[Wild 2013][research_wild_2013]\] \[[Willen 1975][research_willen_1975]\] \[[Winkelman and Barlow 1980][research_winkelman_barlow_1980]\] \[[Winkelmann 1989][research_winkelmann_1989]\] \[[Witkowski et al 2022][research_witkowski_williams_2022]\] \[[Wong et al 1993][research_wong_rock_1993]\] \[[Wood 1946][research_wood_1946]\] \[[Xiong and Nguyen 2023][research_xiong_nguyen_2023_b]\] \[[Xiong et al 2026][research_xiong_nguyen_2026]\] \[[Xu et al 2013][research_xu_deng_2013]\] \[[Yamada and Nakamura 2002][research_yamada_nakamura_2002]\] \[[Yip et al 1992][research_yip_ross_1992]\] \[[Yoo 2018][research_yoo_2018]\] \[[Young 1974][research_young_1974]\] \[[Young 2026][research_young_2026]\] \[[Young and Adams 1972][research_young_adams_1972]\] \[[Yu and Yu 2026][research_yu_2026]\] \[[Zarutskaya and Arieli 2005][research_zarutskaya_arieli_2005]\] \[[Zhao and Zhu 2016][research_zhao_zhu_2016]\] \[[Zhou and Wu 2025][research_zhou_wu_2025]\] \[[Zhu et al 2019][research_zhu_liu_2019]\] \[[Zverkov et al 2012][research_zverkov_kozlov_2012]\]

### Compressibility, drag rise and the high-speed swept wing

**The speed regime that sweep is for.** Transonic and supersonic swept-wing aerodynamics, drag rise and wave drag, and the tunnel and free-flight methods that measured them.

**289 records.** \[[A'Harrah 1964][research_aharrah_1964]\] \[[A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]\] \[[Agrawal et al 1991][research_agrawal_kinard_1991]\] \[[Alford and Byrnes 1952][research_alford_byrnes_1952]\] \[[Alternative Methods for Modeling 1989][research_alternative_methods_1989]\] \[[Alviani et al 2022][research_alviani_blaisdell_2022]\] \[[Anderson and Bray 1951][research_anderson_bray_1951]\] \[[Anderson and Bray 1955][research_anderson_1955]\] \[[Application of Computational Methods 1982][research_application_of_1982]\] \[[Ashkenas 1964][research_ashkenas_1964]\] \[[Ashkenas 1964][research_ashkenas_1964_b]\] \[[Avkhadiev and Elizarov 2001][research_avkhadiev_elizarov_2001]\] \[[Axelson 1959][research_axelson_1959]\] \[[Ballhaus and Bailey 1972][research_ballhaus_bailey_1972]\] \[[Bartlett et al 1973][research_bartlett_1973]\] \[[Basic Equations for Unsteady 1989][research_basic_equations_1989]\] \[[Batina et al 1988][research_batina_seidel_1988]\] \[[Batina et al 1989][research_batina_seidel_1989]\] \[[Bauer et al 2016][research_bauer_grund_2016]\] \[[Beeler et al 1956][research_beeler_1956]\] \[[Begnini et al 2018][research_begnini_bones_2018]\] \[[Bellman 1959][research_bellman_1959]\] \[[Bertelrud 1981][research_bertelrud_1981_b]\] \[[Bertelrud and Graves 1994][research_bertelrud_graves_1994]\] \[[Bielat and Wiley 1959][research_bielat_wiley_1959]\] \[[Boling and Zha 2021][research_boling_zha_2021]\] \[[Boppe and Aidala 1980][research_boppe_aidala_1980]\] \[[Bore and Boyd 1963][research_bore_boyd_1963]\] \[[Braginsky 2020][research_braginsky_2020]\] \[[Bray 1953][research_bray_1953]\] \[[Bridges 2008][research_bridges_2008]\] \[[Broeren et al 2018][research_broeren_lee_2018]\] \[[Brown 1961][research_brown_1961]\] \[[Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]\] \[[Bui 2018][research_bui_2018]\] \[[Bui 2018][research_bui_2018_b]\] \[[Burner et al 2008][research_burner_goad_2008]\] \[[Bushnell 1990][research_bushnell_1990]\] \[[Campbell and Smith 1987][research_campbell_smith_1987]\] \[[Campion 1954][research_campion_1954]\] \[[Carlson and Weed 1985][research_carlson_weed_1985]\] \[[Carter et al 2009][research_carter_vicroy_2009]\] \[[Chaparro et al 2017][research_chaparro_fujiwara_2017]\] \[[Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]\] \[[Chau and Zingg 2022][research_chau_zingg_2022]\] \[[Cheatham and Kurbjun 1948][research_cheatham_1948]\] \[[Chen et al 1984][research_chen_vassberg_1984]\] \[[Chen et al 2015][research_chen_zhang_2015]\] \[[Chen et al 2026][research_chen_xiao_2026]\] \[[Cheng et al 1980][research_cheng_meng_1980]\] \[[Cinquegrana and Iuliano 2017][research_cinquegrana_iuliano_2017]\] \[[Clyde et al 1984][research_clyde_bonner_1984]\] \[[Cole 1988][research_cole_1988_b]\] \[[Computational Methods for Unsteady 1989][research_computational_methods_1989]\] \[[Cook 1979][research_cook_1979]\] \[[Covell et al 1987][research_covell_wood_1987]\] \[[Croom and Huffman 1957][research_croom_1957_2]\] \[[Davies 2020][research_davies_2020]\] \[[Davies 2025][research_davies_2025]\] \[[Davis 1952][research_davis_1952]\] \[[Deng et al 2013][research_deng_qin_2013]\] \[[Dickey 1959][research_dickey_1959]\] \[[Dodbele and Plotkin 1985][research_dodbele_plotkin_1985]\] \[[Duc et al 2004][research_duc_sesterhenn_2004]\] \[[Ericsson 1980][research_ericsson_1980]\] \[[Ericsson and Reding 1977][research_ericsson_reding_1977]\] \[[Ericsson and Reding 1978][research_ericsson_reding_1978]\] \[[Experimental Testing at Transonic 1982][research_experimental_testing_1982]\] \[[Fejtek et al 2001][research_fejtek_jones_2001]\] \[[Felix et al 2026][research_felix_2026]\] \[[Fisher and Williams 1958][research_fisher_1958]\] \[[Flat Wings in Inviscid 2020][research_flat_wings_2020]\] \[[Flores and Van Dalsem 1985][research_flores_vandalsem_1985]\] \[[Foster 1960][research_foster_1960_b]\] \[[Foughner 1989][research_foughner_1989]\] \[[Fournier and Silvers 1958][research_fournier_silvers_1958]\] \[[Franciolini et al 2018][research_franciolini_daronch_2018]\] \[[Fujii and Obayashi 1986][research_fujii_obayashi_1986]\] \[[Fuller 1967][research_fuller_1967]\] \[[Gally and Carlson 1987][research_gally_carlson_1987]\] \[[Gao et al 2025][research_gao_tyrrell_2025]\] \[[Gapcynski and Landrum 1958][research_gapcynski_landrum_1958]\] \[[Ghoreyshi et al 2024][research_ghoreyshi_aref_2024]\] \[[Ghoreyshi et al 2025][research_ghoreyshi_aref_2025]\] \[[Gillis and Chapman 1956][research_gillis_1956]\] \[[Gillis and Mitchell 1957][research_gillis_1957]\] \[[Glauert 1928][research_glauert_1928]\] \[[Goodheart et al 2003][research_goodheart_dykas_2003]\] \[[Goto et al 2007][research_goto_obayashi_2007]\] \[[Greenman et al 1996][research_greenman_cheung_1996]\] \[[Grosser 1965][research_grosser_1965]\] \[[Grosser 1982][research_grosser_1982]\] \[[Guderley 1987][research_guderley_1987]\] \[[Guderley 1988][research_guderley_1988]\] \[[Haines 1957][research_haines_1957]\] \[[Hallissy and Ayers 1977][research_hallissy_ayers_1977]\] \[[Haney et al 1978][research_haney_waggoner_1978]\] \[[Haney et al 1980][research_haney_johnson_1980]\] \[[Harrison et al 2016][research_harrison_darragh_2016]\] \[[Hayes 1971][research_hayes_1971]\] \[[Heath and Ward 1959][research_heath_1959]\] \[[Henderson 1960][research_henderson_1960]\] \[[Henderson 1974][research_henderson_1974]\] \[[Henderson and Huffman 1975][research_henderson_huffman_1975]\] \[[Henne 1981][research_henne_1981]\] \[[Hieser et al 1956][research_hieser_kudlacik_1956]\] \[[High-Speed Flight and Its 2010][research_high_speed_flight_2010]\] \[[Hillenherms et al 2001][research_hillenherms_schroeder_2001]\] \[[Hilton 1955][research_hilton_1955]\] \[[Historic Review of the 2010][research_historic_review_2010]\] \[[Hoerner 1936][research_hoerner_1936]\] \[[Hussain and Pei 2025][research_hussain_pei_2025]\] \[[Hutchison et al 1994][research_hutchison_unger_1994]\] \[[Igoe et al 1961][research_igoe_1961]\] \[[Ito and Takanashi 1991][research_ito_takanashi_1991]\] \[[Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]\] \[[Jacobs 1983][research_jacobs_1983]\] \[[Jacobsen 1953][research_jacobsen_1953]\] \[[Jameson][research_jameson]\] \[[Jameson 1977][research_jameson_1977]\] \[[Jameson and Caughey 1977][research_jameson_caughey_1977]\] \[[Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]\] \[[Jernell and McKinney 1965][research_jernell_mckinney_1965]\] \[[Jiang et al 2014][research_jiang_xu_2014]\] \[[Jim et al 2021][research_jim_planform_2021]\] \[[Johnston 1998][research_johnston_1998]\] \[[Jones 1947][research_jones_1947]\] \[[Jones 1976][research_jones_1976_c]\] \[[Jones 1980][research_jones_1980]\] \[[Jones and Alksne 1951][research_jones_alksne_1951]\] \[[Kameda et al 2008][research_kameda_seki_2008]\] \[[Kandil et al 1993][research_kandil_kandil_1993]\] \[[Kandil et al 1994][research_kandil_kalisch_1994]\] \[[Kaul 2024][research_kaul_2024]\] \[[Keener 1984][research_keener_1984]\] \[[Kim and Sung 1993][research_kim_sung_1993]\] \[[Kirkman and Takahashi 2017][research_kirkman_takahashi_2017]\] \[[Kishi et al 2017][research_kishi_kitazaki_2017]\] \[[Kishi et al 2022][research_kishi_kanazaki_2022]\] \[[Knight et al 2011][research_knight_braun_2011]\] \[[Ko et al 2003][research_ko_mason_2003]\] \[[Konrath et al 2006][research_konrath_schroder_2006]\] \[[Krenz 1979][research_krenz_1979]\] \[[Kruse et al 2012][research_kruse_wunderlich_2012]\] \[[Kuhlman and Brown 1989][research_kuhlman_brown_1989]\] \[[Kuhlman et al 1988][research_kuhlman_cerney_1988]\] \[[Kulfan 1974][research_kulfan_1974]\] \[[Kulfan et al 1973][research_kulfan_neumann_1973]\] \[[Kurus et al 2021][research_kurus_takahashi_2021]\] \[[Kutzbach et al 2004][research_kutzbach_lutz_2004]\] \[[Lampert 1951][research_lampert_1951]\] \[[Lampropoulos et al 2025][research_lampropoulos_vouros_2025]\] \[[Lange et al 1974][research_lange_cahill_1974]\] \[[Lee and Marnineau-Mes 1996][research_lee_marnineaumes_1996]\] \[[Lijewski 1987][research_lijewski_1987]\] \[[Liu 2022][research_liu_2022_c]\] \[[Liu 2022][research_liu_2022_d]\] \[[Liu et al 2017][research_liu_yang_2017]\] \[[Lock 1964][research_lock_1964]\] \[[Lovell 2001][research_lovell_2001]\] \[[Loving 1961][research_loving_1961]\] \[[Loving 1961][research_loving_1961_b]\] \[[Mack et al 2009][research_mack_schmid_2009]\] \[[Maikapar 2000][research_maikapar_2000]\] \[[Mann and Mercer 1985][research_mann_mercer_1985]\] \[[Mann and Mercer 1986][research_mann_mercer_1986]\] \[[Margolis 1947][research_margolis_1947]\] \[[Mason 1982][research_mason_1982]\] \[[Mason 1983][research_mason_1983]\] \[[Masson et al 1999][research_masson_veilleux_1999]\] \[[Mateer and Bertelrud 1983][research_mateer_bertelrud_1983]\] \[[Matsushima and Takanashi 1996][research_matsushima_takanashi_1996]\] \[[McFadden and Bons 2025][research_mcfadden_bons_2025]\] \[[McGrath 1993][research_mcgrath_1993]\] \[[Mele et al 2017][research_mele_ostieri_2017]\] \[[Menzies et al 1995][research_menzies_kandil_1995]\] \[[Miles 1953][research_miles_1953]\] \[[Mitcham 1957][research_mitcham_1957]\] \[[Mitcham and Blanchard 1950][research_mitcham_blanchard_1950]\] \[[Moeckel 1948][research_moeckel_1948]\] \[[Moorthamers et al 2021][research_moorthamers_wiberg_2021]\] \[[Moseley and Watson 1951][research_moseley_1951]\] \[[Mugler 1958][research_mugler_1958]\] \[[Mugler 1959][research_mugler_1959]\] \[[Mugler 1959][research_mugler_1959_b]\] \[[Mugler and Woodall 1960][research_mugler_woodall_1960]\] \[[NACA Conference on Aerodynamic 1949][research_naca_1949]\] \[[NACA Conference on Aerodynamic 1947][research_naca_conference_1947]\] \[[Equations, tables, and charts 1953][research_naca_1135]\] \[[Nangia et al 2023][research_nangia_ghoreyshi_2023]\] \[[Nielsen et al 1953][research_nielsen_kaattari_1953]\] \[[Obayashi et al 1997][research_obayashi_yamaguchi_1997]\] \[[Olstad and Fischetti 1958][research_olstad_fischetti_1958]\] \[[Oyama et al 2008][research_oyama_ito_2008]\] \[[Painter and Caw 1978][research_painter_1978]\] \[[Parlett and Shivers 1976][research_parlett_shivers_1976]\] \[[Petrov 2009][research_petrov_2009]\] \[[Pfaff 1965][research_pfaff_1965]\] \[[Physical Phenomena Associated with 1989][research_physical_phenomena_1989]\] \[[Potential Equation Methods for 1982][research_potential_equation_1982]\] \[[Qin 2012][research_qin_2012]\] \[[Rahman et al 2022][research_rahman_aljibory_2022]\] \[[Rambacher and Bons 2023][research_rambacher_bons_2023]\] \[[Ratcliff and Carlson 1989][research_ratcliff_carlson_1989]\] \[[Rein et al 2025][research_rein_henne_2025]\] \[[Review of Transonic Aerodynamics 1982][research_review_of_1982]\] \[[Riou et al 2010][research_riou_garnier_2010]\] \[[Rizzi 1984][research_rizzi_1984]\] \[[Runckel and Hieser 1961][research_runckel_hieser_1961]\] \[[Runckel et al 1960][research_runckel_schmeer_1960]\] \[[Russo et al 2020][research_russo_tognaccini_2020]\] \[[Russo et al 2020][research_russo_tognaccini_2020_b]\] \[[Sachs et al 2021][research_sachs_gruter_2021]\] \[[Sachs et al 2021][research_sachs_gruter_2021_b]\] \[[Sadoff et al 1954][research_sadoff_matteson_1954]\] \[[Sammonds 1960][research_sammonds_1960]\] \[[Samputh et al 2024][research_samputh_moey_2024]\] \[[Sankar et al 1985][research_sankar_malone_1985]\] \[[Sawyer and Trant 1950][research_sawyer_trant_1950]\] \[[Schiavetta et al 2006][research_schiavetta_boelens_2006]\] \[[Schmeer and Cassetti 1960][research_schmeer_cassetti_1960]\] \[[Schmitt et al 1983][research_schmitt_destarac_1983]\] \[[Schuette and Hummel 2024][research_schuette_hummel_2024]\] \[[Schütte and Hummel 2025][research_schutte_hummel_2025]\] \[[Seraj and Martins 2023][research_seraj_martins_2023]\] \[[Seraj and Martins 2025][research_seraj_2025]\] \[[Shahjahan and Ahuja 2026][research_shahjahan_ahuja_2026]\] \[[Shahjahan et al 2026][research_shahjahan_enriquez_2026]\] \[[Shamshurin 1974][research_shamshurin_1974]\] \[[Shankar and Malmuth 1982][research_shankar_malmuth_1982]\] \[[Shen and Mo 1996][research_shen_mo_1996]\] \[[Shtin and Savelyev 2022][research_shtin_savelyev_2022]\] \[[Silsby and Kennedy 1947][research_silsby_kennedy_1947]\] \[[Singh and Dwivedi 2022][research_singh_dwivedi_2022]\] \[[Smith 1959][research_smith_1959]\] \[[Sohail et al 2011][research_sohail_muhammad_2011]\] \[[Solies 1995][research_solies_1995]\] \[[Spearman 1980][research_spearman_1980]\] \[[Spreemann and Alford 1951][research_spreemann_1951]\] \[[Spreiter and Stahara 1970][research_spreiter_stahara_1970]\] \[[Squire 1975][research_squire_1975]\] \[[Srinivas and Potti 2014][research_srinivas_potti_2014]\] \[[Stanbrook 1954][research_stanbrook_1954]\] \[[Steer 2003][research_steer_2003]\] \[[Steimle et al 2012][research_steimle_karhoff_2012]\] \[[Stevens 1955][research_stevens_1955]\] \[[Sudhi et al 2021][research_sudhi_radespiel_2021]\] \[[Szema and Shankar 1984][research_szema_shankar_1984]\] \[[Taisul Ahn et al][research_taisulahn_hyoungjinkim]\] \[[Takahashi et al 2019][research_takahashi_boccieri_2019]\] \[[Takanashi 1984][research_takanashi_1984]\] \[[Tamayo][research_tamayo]\] \[[Tempelmeyer and Osborne 1954][research_tempelmeyer_osborne_1954]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]\] \[[Transfer of German High-Speed 2010][research_transfer_of_2010]\] \[[Transonic Aerodynamics 1982][research_transonic_aerodynamics_1982]\] \[[Transonic Aerodynamics-History and Statement 1982][research_transonic_aerodynamics_history_1982]\] \[[Transonic Computational Experience for 1982][research_transonic_computational_1982]\] \[[Transonic Design Using Computational 1982][research_transonic_design_1982]\] \[[Transonic Wing Shape Design 2015][research_transonic_wing_2015]\] \[[Tseng 1990][research_tseng_1990]\] \[[Tursi 2003][research_tursi_2003]\] \[[Unger and Coen 1993][research_unger_coen_1993]\] \[[Unsteady Transonic Aerodynamics 1989][research_unsteady_transonic_1989]\] \[[Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]\] \[[Visbal and Gordnier 1995][research_visbal_gordnier_1995]\] \[[Visonneau et al 2015][research_visonneau_guilmineau_2015]\] \[[Vogler and Turner 1956][research_vogler_1956]\] \[[Walkley 1986][research_walkley_1986]\] \[[Wang 2025][research_wang_2025_b]\] \[[Ward 1949][research_ward_1949]\] \[[Weatherill and Ehlers 1989][research_weatherill_ehlers_1989]\] \[[Weed et al 1983][research_weed_carlson_1983]\] \[[Weed et al 1984][research_weed_carlson_1984]\] \[[Werner et al 2024][research_werner_henne_2024]\] \[[Whitcomb 1956][research_whitcomb_1956]\] \[[Whitcomb 1983][research_whitcomb_1983]\] \[[Whitcomb and Norton 1961][research_whitcomb_1961]\] \[[Winski et al][research_winski_langston]\] \[[Woan and Chakravarthy 1988][research_woan_chakravarthy_1988]\] \[[Wooden et al 2007][research_wooden_smith_2007]\] \[[Wright and Loving 1953][research_wright_loving_1953]\] \[[Wu et al 2024][research_wu_huang_2024]\] \[[Xia et al 1993][research_xia_zhu_1993]\] \[[Yu and Campbell 1992][research_yu_campbell_1992]\] \[[Zhang and Zhou 2022][research_zhang_zhou_2022]\] \[[Zhao 1988][research_zhao_1988]\] \[[Zimper and Rein 2014][research_zimper_rein_2014]\]

### Variable sweep, the pivot and the aircraft that used it

**The keystone, and the literature the X-5 began.** Wind-tunnel and flight reports on variable-sweep configurations, the location of the pivot and the aerodynamic centre of a pivoting wing, the F-111, F-14 and Tornado that carried the outboard pivot into service, and the variable-sweep morphing vehicles of the present. **Its record falls into two periods.** Of its 263 dated records, 162 date from 1950 to 1989, when variable sweep was a research and production subject, 21 from 1990 to 2009, and 80 from 2010 on, when the small variable-sweep morphing vehicle revived it.

**264 records.** \[[Abel et al 1966][research_abel_1966]\] \[[Al-Khafaji et al 2023][research_alkhafaji_panatov_2023]\] \[[Alford and Henderson 1959][research_alford_1959_2]\] \[[Alford and Luoma 1960][research_alford_luoma_1960]\] \[[Alford and Polhamus 1962][research_alford_polhamus_1962]\] \[[Alford et al 1959][research_alford_1959]\] \[[Alford et al 1962][research_alford_1962]\] \[[Alford et al 1966][research_alford_1966]\] \[[An et al 1986][research_an_yan_1986]\] \[[An et al 1988][research_an_yan_1988]\] \[[Anderson et al 1988][research_anderson_1988]\] \[[Anderson et al 1991][research_anderson_meyer_1991]\] \[[Anderson et al 2012][research_anderson_robertrmeyer_2012]\] \[[Antaran et al 1992][research_antaran_belete_1992]\] \[[Aoyagi et al 1965][research_aoyagi_cook_1965]\] \[[Ascani et al 1971][research_ascani_mellin_1971]\] \[[Averett and Wright 1966][research_averett_1966]\] \[[Ayers 1973][research_ayers_1973]\] \[[Baals and Polhamus 1963][research_baals_polhamus_1963]\] \[[Bai et al 2022][research_bai_ding_2022]\] \[[Bai et al 2024][research_bai_yang_2024]\] \[[Bai et al 2024][research_bai_yang_2024_b]\] \[[Bai et al 2025][research_bai_2025]\] \[[Bai et al 2026][research_bai_yang_2026]\] \[[Banner et al 1955][research_banner_1955]\] \[[Becht 1950][research_becht_1950]\] \[[Becht and Few 1950][research_becht_few_1950]\] \[[Beissner et al 1984][research_beissner_1984]\] \[[Bellman 1953][research_bellman_1953]\] \[[Benepe et al 1975][research_benepe_cunningham_1975]\] \[[Benepe et al 1978][research_benepe_cunningham_1978]\] \[[Bielat and Campbell 1953][research_bielat_campbell_1953]\] \[[Bielat and Pierpont 1960][research_bielat_1960]\] \[[Bird 1973][research_bird_1973]\] \[[Bobbitt and Foughner 1985][research_bobbitt_foughner_1985]\] \[[Bolonkin and Gilyard 1999][research_bolonkin_gilyard_1999]\] \[[Bonnema and Lokos 1989][research_bonnema_lokos_1989]\] \[[Bonnema and Smith 1988][research_bonnema_smith_1988]\] \[[Bowman and White 1974][research_bowman_1974]\] \[[Briggs 1954][research_briggs_1954]\] \[[Bulekov and Teryev 1972][research_bulekov_teryev_1972]\] \[[Burchill et al 2002][research_burchill_mcdonald_2002]\] \[[Cangelosi 1963][research_cangelosi_1963]\] \[[Cao and Chen 2024][research_cao_chen_2024]\] \[[Cao and Lu 2024][research_cao_lu_2024]\] \[[Chai et al 2018][research_chai_smart_2018]\] \[[Chakravarthy et al 2009][research_chakravarthy_grant_2009]\] \[[Chakravarthy et al 2012][research_chakravarthy_grant_2012]\] \[[Chen et al 2015][research_chen_yue_2015]\] \[[Cheng et al 2024][research_cheng_song_2024]\] \[[Chester 2002][research_chester_2002]\] \[[Childs 1953][research_childs_1953]\] \[[Coe and Cunningham 1987][research_coe_cunningham_1987]\] \[[Cook 1968][research_cook_1968]\] \[[Croom and Huffman 1957][research_croom_1957]\] \[[Croom and Huffman 1957][research_croom_huffman_1957]\] \[[Cunningham and Coe 1990][research_cunningham_coe_1990]\] \[[Dai et al 2020][research_dai_sweep_2020]\] \[[Dai et al 2021][research_dai_mpc_2021]\] \[[Dobbs et al 1985][research_dobbs_miller_1985]\] \[[Du et al 2026][research_du_2026]\] \[[Durán Ferreras 2009][research_duranferreras_2009]\] \[[Eckert and Maki 1973][research_eckert_1973]\] \[[Eckert and Maki 1973][research_eckert_maki_1973]\] \[[England 1975][research_england_1975]\] \[[English 1953][research_english_1953]\] \[[feng et al 2025][research_feng_wu_2025]\] \[[Finch 1955][research_finch_1955]\] \[[Finch and Briggs 1953][research_finch_1953]\] \[[Finch and Walker 1953][research_finch_1953_2]\] \[[Finch and Walker 1956][research_finch_walker_1956]\] \[[Fletcher et al 2022][research_fletcher_clarke_2022]\] \[[Foster and Morris 1960][research_foster_1960]\] \[[Foster and Morris 1960][research_foster_morris_1960]\] \[[Foster and Morris 1961][research_foster_morris_1961]\] \[[Foster and Spearman 1959][research_foster_spearman_1959]\] \[[Freudinger and Kehoe 1990][research_freudinger_1990]\] \[[Friend and Sakamoto 1978][research_friend_1978]\] \[[Gainer et al 1967][research_gainer_1967]\] \[[Gao et al 2018][research_gao_jin_2018]\] \[[Gao et al 2022][research_gao_tandem_2022]\] \[[Gao et al 2023][research_gao_zhu_2023]\] \[[Gera et al 1981][research_gera_wilson_1981]\] \[[Goetz and Stonesifer 1961][research_goetz_1961]\] \[[Gong and Ma 2019][research_gong_ma_2019]\] \[[Goorjian et al 1985][research_goorjian_guruswamy_1985]\] \[[Goradia et al 1989][research_goradia_bobbitt_1989]\] \[[Grafton and Anglin 1972][research_grafton_anglin_1972]\] \[[Grant and Lind 2007][research_grant_lind_2007]\] \[[Graves 1975][research_graves_1975]\] \[[Greatwood et al 2017][research_greatwood_waldock_2017]\] \[[Grow and Landrum 1967][research_grow_landrum_1967]\] \[[Guan et al 2026][research_guan_zhuang_2026]\] \[[Guo et al 2020][research_guo_unsteady_2020]\] \[[Gurley and Ruhlin 1962][research_gurley_1962]\] \[[Guruswamy et al 1985][research_guruswamy_goorjian_1985]\] \[[Guruswamy et al 1986][research_guruswamy_goorjian_1986]\] \[[Hall et al 2005][research_hall_mohseni_2005]\] \[[Hallissy and Harris 1974][research_hallissy_harris_1974]\] \[[Hallissy and Phillips 1989][research_hallissy_phillips_1989]\] \[[Hammond and Henderson 1961][research_hammond_1961]\] \[[Hammond and Polhamus 1965][research_hammond_1965]\] \[[Hammond and Polhamus 1970][research_hammond_1970]\] \[[Han et al 2014][research_han_hu_2014]\] \[[Hang et al 2026][research_hang_liu_2026]\] \[[Harvey 1967][research_harvey_1967]\] \[[Henderson and Ray 1964][research_henderson_1964]\] \[[Henderson and Ray 1965][research_henderson_1965]\] \[[Higgins and Shomber 1964][research_higgins_shomber_1964]\] \[[Higgins and Shomber 1965][research_higgins_shomber_1965]\] \[[Hou et al 2024][research_hou_cao_2024]\] \[[Hu et al 2026][research_hu_2026]\] \[[Huffman 1972][research_huffman_1972]\] \[[Huffman et al 1977][research_huffman_jr_1977]\] \[[Inayat et al 2018][research_inayat_amin_2018]\] \[[Jahnke and Culick 1990][research_jahnke_culick_1990]\] \[[Jingeleski et al 2013][research_jingeleski_schetz_2013]\] \[[Kanamori et al 2009][research_kanamori_imamura_2009]\] \[[Kehoe 1987][research_kehoe_1987]\] \[[Kelley et al 1978][research_kelley_shinar_1978]\] \[[Kelley et al 1979][research_kelley_shinar_1979]\] \[[Kemp and Becht 1950][research_kemp_1950]\] \[[Kemp and Few 1951][research_kemp_1951]\] \[[Kempel et al 1989][research_kempel_phillips_1989]\] \[[Kennedy 1951][research_kennedy_1951]\] \[[Kilgore 1971][research_kilgore_1971]\] \[[Kilgore 1971][research_kilgore_1971_b]\] \[[Kilgore and Adcock 1972][research_kilgore_adcock_1972]\] \[[Kolnick and Kennedy 1952][research_kolnick_kennedy_1952]\] \[[Kress 1983][research_kress_1983]\] \[[Kunwar et al 2025][research_kunwar_mccormick_2025]\] \[[Lamar 1968][research_lamar_1968]\] \[[Lamar and Margason 1967][research_lamar_margason_1967]\] \[[Lamar and McKinney 1971][research_lamar_1971]\] \[[Landfield and Rajkovic 1984][research_landfield_rajkovic_1984]\] \[[Landfield and Rajkovic 1986][research_landfield_rajkovic_1986]\] \[[Landgraf and Herring 1967][research_landgraf_herring_1967]\] \[[Larson 1986][research_larson_1986]\] \[[Larson 1987][research_larson_1987]\] \[[Lehman and Stearman 1977][research_lehman_stearman_1977]\] \[[Lei et al 2020][research_lei_zhang_2020]\] \[[Lei et al 2024][research_lei_an_2024]\] \[[Levinsky and Palko 1982][research_levinsky_palko_1982]\] \[[Li et al 2020][research_li_varsweep_2020]\] \[[Li et al 2026][research_li_yu_2026]\] \[[Liu et al 2023][research_liu_liang_2023]\] \[[Lockwood 1966][research_lockwood_1966]\] \[[Lockwood 1966][research_lockwood_1966_b]\] \[[Lockwood and Thompson 1964][research_lockwood_thompson_1964]\] \[[Lorincz 1980][research_lorincz_1980]\] \[[Losee et al 1980][research_losee_willis_1980]\] \[[Louma 1961][research_louma_1961]\] \[[Luochuan Li et al 2016][research_luochuanli_zhenghualiu_2016]\] \[[Luoma 1961][research_luoma_1961]\] \[[Ma et al 2018][research_ma_feng_2018]\] \[[Ma et al 2021][research_ma_bionic_2021]\] \[[Ma et al 2022][research_ma_fan_2022]\] \[[Ma et al 2026][research_ma_alwi_2026]\] \[[Martin 1953][research_martin_1953]\] \[[Martin et al 1988][research_martin_beissner_1988]\] \[[McLaughlin et al 1967][research_mclaughlin_sawyer_1967]\] \[[McLemore et al 1974][research_mclemore_parlett_1974]\] \[[McLemore et al 1977][research_mclemore_parlett_1977]\] \[[Melton][research_melton]\] \[[Melton and Dudley 2016][research_melton_dudley_2016]\] \[[Meyer et al 1987][research_meyer_trujillo_1987]\] \[[Moens et al 2025][research_moens_2025]\] \[[Molent and Jones 2018][research_molent_jones_2018]\] \[[Monaghan 1978][research_monaghan_1978]\] \[[Montoya et al 1981][research_montoya_steers_1981]\] \[[Moosavian 2021][research_moosavian_2021]\] \[[Moosavian et al 2014][research_moosavian_xi_2014]\] \[[Morris and Silsby 1952][research_morris_silsby_1952]\] \[[Morris and Silsby 1954][research_morris_silsby_1954]\] \[[Morris et al 1950][research_morris_kennedy_1950]\] \[[Langley Research Center 1966][research_naca_1966]\] \[[Center 1966][research_naca_1966_2]\] \[[Nguyen et al 1980][research_nguyen_gilbert_1980]\] \[[Nugent 1956][research_nugent_1956]\] \[[Onewein 1967][research_onewein_1967]\] \[[Page 1965][research_page_1965]\] \[[Paget 1967][research_paget_1967]\] \[[Paniszczyn 1967][research_paniszczyn_1967]\] \[[Perry 1966][research_perry_1966]\] \[[Polhamus 1963][research_polhamus_1963]\] \[[Polhamus and Hammond 1960][research_polhamus_1960]\] \[[Polhamus and Toll 1981][research_polhamus_1981]\] \[[Powers 1977][research_powers_1977]\] \[[Powers and Webb 1997][research_powers_webb_1997]\] \[[Prabhakar et al 2015][research_prabhakar_prazenica_2015]\] \[[Preston et al 2025][research_preston_palacios_2025]\] \[[Preston et al 2026][research_preston_fasel_2026]\] \[[Priest et al 2023][research_priest_snyder_2023]\] \[[Qu et al 2024][research_qu_wang_2024]\] \[[Radhakrishnan P et al 2021][research_radhakrishnanp_ramanang_2021]\] \[[Ramachandran and Wells 1974][research_ramachandran_wells_1974]\] \[[Ramachandran and Wells 1975][research_ramachandran_wells_1975]\] \[[Re and Reubush 1979][research_re_reubush_1979]\] \[[Redin 1981][research_redin_1981]\] \[[Reed 1955][research_reed_1955]\] \[[Reubush and Mercer 1974][research_reubush_mercer_1974]\] \[[Reubush and Mercer 1975][research_reubush_mercer_1975]\] \[[Richardson 1968][research_richardson_1968]\] \[[Richardson 1968][research_richardson_1968_b]\] \[[Ritchie 1973][research_ritchie_1973]\] \[[Robins et al 1983][research_robins_beissner_1983]\] \[[Rogers and Dunn 1952][research_rogers_1952]\] \[[Rokhsaz and Selberg 1989][research_rokhsaz_selberg_1989]\] \[[Rozendaal 1986][research_rozendaal_1986]\] \[[Rozendaal 1987][research_rozendaal_1987]\] \[[Rozendaal and Behbehani 1990][research_rozendaal_behbehani_1990]\] \[[Runyan and Steers 1980][research_runyan_steers_1980]\] \[[Runyan et al 1984][research_runyan_navran_1984]\] \[[Sawyer et al 1951][research_sawyer_kennedy_1951]\] \[[Schneider 1976][research_schneider_1976]\] \[[Selberg and Vitt 1993][research_selberg_vitt_1993]\] \[[Shah 2014][research_shah_2014]\] \[[Shao et al 2025][research_shao_zhang_2025]\] \[[Si et al 2024][research_si_wu_2024]\] \[[Silsby and Morris 1953][research_silsby_morris_1953]\] \[[Silsby et al 1950][research_silsby_morris_1950]\] \[[Sim and Curry 1978][research_sim_curry_1978]\] \[[Simmons and Freund 2005][research_simmons_freund_2005]\] \[[Sims and Carter 1981][research_sims_carter_1981]\] \[[Smith et al 1992][research_smith_lock_1992]\] \[[Spearman 2012][research_spearman_2012]\] \[[Spencer 1960][research_spencer_1960]\] \[[Swihart and Goodman 1965][research_swihart_goodman_1965]\] \[[Swihart and Goodmanson 1964][research_swihart_goodmanson_1964]\] \[[tarabi et al 2016][research_tarabi_ghasemloo_2016]\] \[[Tasci and Ozdemir 2025][research_tasci_ozdemir_2025]\] \[[Thornton 1993][research_thornton_1993]\] \[[Toll 1962][research_toll_1962]\] \[[Tong and Ji 2013][research_tong_ji_2013]\] \[[Tong and Ji 2014][research_tong_ji_2014]\] \[[Van Thullenar 1957][research_vanthullenar_1957]\] \[[Variable sweep today 1965][research_variable_sweep_1965]\] \[[Variable sweep wing design 1980][research_variable_sweep_1980]\] \[[Videan 1955][research_videan_1955]\] \[[Waggoner et al 1985][research_waggoner_campbell_1985]\] \[[Waggoner et al 1985][research_waggoner_phillips_1985]\] \[[Waggoner et al 1987][research_waggoner_campbell_1987]\] \[[Wang et al 2025][research_wang_zeng_2025]\] \[[Webb et al 1988][research_webb_mccain_1988]\] \[[Xi et al 2025][research_xi_dai_2025]\] \[[Xiao et al 2023][research_xiao_guo_2023]\] \[[Xu et al 2012][research_xu_yang_2012]\] \[[Xu et al 2012][research_xu_yang_2012_b]\] \[[Xu et al 2022][research_xu_li_2022]\] \[[Xu et al 2023][research_xu_li_2023]\] \[[Xu et al 2025][research_xu_song_2025]\] \[[Xu et al 2026][research_xu_2026]\] \[[Xu et al 2026][research_xu_song_2026]\] \[[Yan et al 2019][research_yan_dai_2019]\] \[[Yang et al 2015][research_yang_tang_2015]\] \[[Yang et al 2021][research_yang_guo_2021]\] \[[Yang et al 2021][research_yang_guo_2021_b]\] \[[Yang et al 2022][research_yang_guo_2022]\] \[[Yang et al 2025][research_yang_li_2025]\] \[[Yurkovich 2008][research_yurkovich_2008]\] \[[Yurkovich 2009][research_yurkovich_2009]\] \[[Zeng et al 2023][research_zeng_liu_2023]\] \[[Zhang et al 2024][research_zhang_wen_2024]\] \[[Zheng et al 2014][research_zheng_he_2014]\]

### Longitudinal stability, trim and the tail

**The trim problem.** Longitudinal stability and the neutral point, tail position and downwash, trim drag and the pitch-up of swept wings.

**188 records.** \[[Airplane Trim 2012][research_airplane_trim_2012]\] \[[Airplane Trim 2022][research_airplane_trim_2022]\] \[[Al-Bayati 2026][research_albayati_2026]\] \[[An Introduction to the 1966][research_an_introduction_1966]\] \[[Ananthkrishnan 2004][research_ananthkrishnan_2004]\] \[[Appendix G Development of 2003][research_appendix_g_2003]\] \[[Ashworth et al 1986][research_ashworth_waltrip_1986]\] \[[Babister 1980][research_babister_1980]\] \[[Benjamin et al 2021][research_benjamin_hesse_2021]\] \[[Beppu et al 1966][research_beppu_curtiss_1966]\] \[[Bird et al 1951][research_bird_1951_2]\] \[[Bird et al 1952][research_bird_1952]\] \[[Bloy 1996][research_bloy_1996]\] \[[Bond et al 2010][research_bond_canfield_2010]\] \[[Bragg and Soltani 1990][research_bragg_soltani_1990]\] \[[Brewer and Lichtenstein 1950][research_brewer_lichtenstein_1950]\] \[[Brigido-Gonzalez and Rodriguez-Cortes 2014][research_brigidogonzalez_rodriguezcortes_2014]\] \[[Budd 1984][research_budd_1984]\] \[[Buell and Kolbe 1957][research_buell_1957]\] \[[Burkhalter 1993][research_burkhalter_1993]\] \[[Butler 1982][research_butler_1982]\] \[[Cai et al 2021][research_cai_xie_2021]\] \[[Chapter 12. Control of 1994][research_chapter_12_1994]\] \[[Cheung et al 2023][research_cheung_rezgui_2023]\] \[[Clark and Hodapp 1972][research_clarkjr_hodappjr_1972]\] \[[Coe and Kulla 1974][research_coe_kulla_1974]\] \[[Correia et al 2009][research_correia_silva_2009]\] \[[Crowe 1937][research_crowe_1937]\] \[[Curtiss et al 1967][research_curtiss_hc_1967]\] \[[Deandrea et al 1991][research_deandrea_roache_1991]\] \[[Development of Longitudinal and 2014][research_development_of_2014]\] \[[Ding 2023][research_ding_2023]\] \[[Dizdarevic 2013][research_dizdarevic_2013]\] \[[Dollyhigh 1970][research_dollyhigh_1970]\] \[[Dong et al 2022][research_dong_choi_2022]\] \[[Donlan and Sleeman 1976][research_donlan_sleeman_1976]\] \[[Dynamic Longitudinal Stability Flight 2003][research_dynamic_longitudinal_2003]\] \[[Dynamic Longitudinal Stability Theory 2003][research_dynamic_longitudinal_2003_b]\] \[[Ericsson 1996][research_ericsson_1996]\] \[[Ericsson 1996][research_ericsson_1996_b]\] \[[Ericsson 1997][research_ericsson_1997_b]\] \[[Ericsson and Ericsson 1997][research_ericsson_ericsson_1997]\] \[[Erturk and Dogan 2017][research_erturk_dogan_2017]\] \[[Ferrero-Guillén et al 2022][research_ferreroguillen_diezgonzalez_2022]\] \[[Figat 2022][research_figat_2022]\] \[[Figat and Kwiek 2023][research_figat_kwiek_2023]\] \[[Fischel and O'Hare 1950][research_fischel_ohare_1950]\] \[[Frazier 1991][research_frazier_1991]\] \[[Garcia et al 2001][research_garcia_slingerland_2001]\] \[[Gardner et al 2018][research_gardner_merz_2018]\] \[[Gardner et al 2019][research_gardner_merz_2019]\] \[[Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]\] \[[Gopalarathnam and McAvoy 2001][research_gopalarathnam_mcavoy_2001]\] \[[Grismer and Nelson 1994][research_grismer_nelson_1994]\] \[[Guo et al 1988][research_guo_wang_1988]\] \[[Ham 1981][research_ham_1981]\] \[[Hargraves 1961][research_hargraves_1961]\] \[[Hayes and Sleeman 1959][research_hayes_1959]\] \[[Herdiana et al 2024][research_herdiana_pinindriya_2024]\] \[[Heron and Myose 2007][research_heron_myose_2007]\] \[[Hoang and Bui 2019][research_hoang_bui_2019]\] \[[Hoang and Bui 2019][research_hoang_bui_2019_b]\] \[[Hoang et al 1993][research_hoang_rediniotis_1993]\] \[[Hooker 2023][research_hooker_2023]\] \[[Hua Tian 2018][research_huatian_2018]\] \[[Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]\] \[[Irving 1966][research_irving_1966_b]\] \[[James and Maki 1957][research_james_1957]\] \[[Jaquet 1952][research_jaquet_1952]\] \[[Ji et al 2024][research_ji_huang_2024]\] \[[Johnson 1953][research_johnson_1953]\] \[[Jones and Nakamura 2007][research_jones_nakamura_2007]\] \[[Karthik et al 1999][research_karthik_tulapurkara_1999]\] \[[Kazhan et al 2019][research_kazhan_kazhan_2019]\] \[[Keith and Selberg 1984][research_keith_selberg_1984]\] \[[Kendall 1984][research_kendall_1984]\] \[[Kendall 1985][research_kendall_1985]\] \[[Kentfield 2006][research_kentfield_2006]\] \[[Kentfield and Spragins 2004][research_kentfield_spragins_2004]\] \[[Khan and Deng 2012][research_khan_deng_2012]\] \[[Klausmeyer and Laflin 2023][research_klausmeyer_laflin_2023]\] \[[Kolesar 1971][research_kolesar_1971]\] \[[Kornev and Pimenov 2022][research_kornev_pimenov_2022]\] \[[Kusunose 2004][research_kusunose_2004]\] \[[Lapin et al 1952][research_lapin_crookshanks_1952]\] \[[Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]\] \[[Liang and Wang 2018][research_liang_wang_2018]\] \[[Lichtenstein 1951][research_lichtenstein_1951]\] \[[Lichtenstein 1951][research_lichtenstein_1951_b]\] \[[Lichtenstein 1952][research_lichtenstein_1952_b]\] \[[Liu 2012][research_liu_2012]\] \[[Liu et al 2012][research_liu_xu_2012]\] \[[Lockwood and Watson 1948][research_lockwood_watson_1948]\] \[[Longitudinal Control and Trim 2003][research_longitudinal_control_2003]\] \[[Longitudinal Maneuvering Stability Theory 2003][research_longitudinal_maneuvering_2003]\] \[[Lowry and Schneiter 1947][research_lowry_schneiter_1947]\] \[[Lutze 1977][research_lutze_1977]\] \[[Maji et al 2024][research_maji_pandi_2024]\] \[[Mann et al 1987][research_mann_huffman_1987]\] \[[Mardanpour et al 2013][research_mardanpour_hodges_2013_c]\] \[[Matějů 2019][research_mateju_2019]\] \[[McFadden and Heinle 1954][research_mcfadden_heinle_1954]\] \[[McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]\] \[[Mendenhall and Spangler 1979][research_mendenhall_spangler_1979]\] \[[Methods for Improving Longitudinal 2003][research_methods_for_2003_b]\] \[[Miller et al 2003][research_miller_jacques_2003]\] \[[Millidere et al 2021][research_millidere_karaman_2021]\] \[[Mohammed 2015][research_mohammed_2015]\] \[[Mohd. Nasir 2026][research_mohdnasir_2026]\] \[[Moorthamers and Hunsaker 2019][research_moorthamers_hunsaker_2019]\] \[[Moura et al 2024][research_moura_nepomuceno_2024]\] \[[Naeseth 1956][research_naeseth_1956]\] \[[Naeseth 1956][research_naeseth_1956_b]\] \[[Nangia and Palmer 2002][research_nangia_palmer_2002]\] \[[Neely and Koven 1947][research_neely_koven_1947]\] \[[Ness 1971][research_ness_1971]\] \[[Olugbeji Jemitola and Peter Okonkwo 2021][research_olugbejijemitola_peterokonkwo_2021]\] \[[Ordaz et al 2015][research_ordaz_geiselhart_2015]\] \[[Pashilkar 1996][research_pashilkar_1996]\] \[[Pattinson et al 2013][research_pattinson_lowenberg_2013]\] \[[Paziresh et al 2017][research_paziresh_nikseresht_2017]\] \[[Phillips 1948][research_phillips_1948]\] \[[Phillips and West 2017][research_phillips_west_2017]\] \[[Phillips and West 2019][research_phillips_west_2019]\] \[[Phillips et al 2002][research_phillips_anderson_2002]\] \[[Phillips et al 2008][research_phillips_hunsaker_2008]\] \[[Prakash et al 2009][research_prakash_uthup_2009]\] \[[Prior et al 2023][research_prior_rozinka_2023]\] \[[Purser et al 1947][research_purser_spearman_1947]\] \[[Qi et al 2021][research_qi_zong_2021]\] \[[Queijo and Wolhart 1951][research_queijo_wolhart_1951]\] \[[Queijo et al 1954][research_queijo_1954]\] \[[Raghavan and Patil 2009][research_raghavan_patil_2009]\] \[[Raheel and Toropov 2018][research_raheel_toropov_2018]\] \[[Rajamurthy 2002][research_rajamurthy_2002]\] \[[Rao and Johnson 1982][research_rao_1982]\] \[[Rashad et al 2025][research_rashad_elbadawy_2025]\] \[[Rediniotis et al 1994][research_rediniotis_klute_1994]\] \[[Rhudy 2016][research_rhudy_2016]\] \[[Roache 1965][research_roache_1965]\] \[[Rodgers 1964][research_rodgers_1964]\] \[[Rodgers 1965][research_rodgers_1965]\] \[[Russell 1996][research_russell_1996_b]\] \[[Rymarz and Ramaprian 1995][research_rymarz_ramaprian_1995]\] \[[Sachs 1978][research_sachs_1978]\] \[[Sachs 1980][research_sachs_1980]\] \[[Sandoz et al 2018][research_sandoz_ahuja_2018]\] \[[Scallion 1952][research_scallion_1952]\] \[[Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]\] \[[Schneider 1956][research_schneider_1956]\] \[[Shankar 2013][research_shankar_2013]\] \[[Shitrit 2021][research_shitrit_2021]\] \[[Sinkovec et al 2015][research_sinkovec_loshek_2015]\] \[[Smith et al 1973][research_smith_lebacqz_1973]\] \[[Spencer 1961][research_spencer_1961]\] \[[Spencer 1981][research_spencer_1981]\] \[[Srichitturi 2026][research_srichitturi_2026]\] \[[Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]\] \[[Static Longitudinal Stability Theory 2003][research_static_longitudinal_2003_b]\] \[[Stephen and Sopirak 1994][research_stephen_sopirak_1994]\] \[[Strickland et al 1990][research_strickland_tadios_1990]\] \[[Tan et al 2017][research_tan_wang_2017]\] \[[Taylor 1959][research_taylor_1959]\] \[[The effects of aft-loaded 1989][research_the_effects_1989]\] \[[Thomas and Wolhart 1957][research_thomas_wolhart_1957]\] \[[Thrust-induced effects on pitching-up 1994][research_thrust_induced_effects_1994]\] \[[Traub 1997][research_traub_1997_c]\] \[[Trim Drag and Maneuvering 2010][research_trim_drag_2010]\] \[[Tu 1992][research_tu_1992]\] \[[Tupy and Zelinka 2008][research_tupy_zelinka_2008]\] \[[Ullah et al 2021][research_ullah_fabijanic_2021]\] \[[van Dommelen et al 2019][research_vandommelen_dsilva_2019]\] \[[Vaughan and Wood 1995][research_vaughan_wood_1995]\] \[[Visbal and Garmann 2018][research_visbal_garmann_2018]\] \[[Wang et al 2022][research_wang_tai_2022]\] \[[Wasserman and Mitchell 1973][research_wasserman_mitchell_1973]\] \[[Weil and Morrison 1953][research_weil_1953]\] \[[Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]\] \[[Wilmott 1986][research_wilmott_1986]\] \[[Xie et al 2026][research_xie_cai_2026]\] \[[Xu and Zhou 2015][research_xu_zhou_2015]\] \[[Yeo et al 2015][research_yeo_atkins_2015]\] \[[Yigit and Millidere 2021][research_yigit_millidere_2021]\] \[[You 2026][research_you_2026]\] \[[Yuhong et al 2017][research_yuhong_guanxin_2017]\] \[[Zangeneh 2021][research_zangeneh_2021]\] \[[Zangeneh 2022][research_zangeneh_2022]\] \[[Zhao et al 2022][research_zhao_luo_2022]\]

### Flight control, scheduling and handling qualities

**Flying a plant that changes.** Gain scheduling, flight control law design and the handling qualities criteria against which a configuration change is judged.

**175 records.** \[[Adams 1972][research_adams_1972]\] \[[Adams and Hatch 1970][research_adams_hatchjr_1970]\] \[[Aircraft Flight Control 2014][research_aircraft_flight_2014]\] \[[Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]\] \[[Aircraft longitudinal handling qualities 2011][research_aircraft_longitudinal_2011]\] \[[Ameho and Prempain 2011][research_ameho_prempain_2011]\] \[[Aouf et al 2002][research_aouf_boulet_2002]\] \[[Application of dynamic flight][research_application_of]\] \[[Ashkenas 1984][research_ashkenas_1984]\] \[[Atman and Bambang 2015][research_atman_bambang_2015]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]\] \[[Ballouz and Chang][research_ballouz_chang]\] \[[Barbosa and Silvestre 2025][research_barbosa_2025]\] \[[Barbosa et al 2018][research_barbosa_bertolin_2018]\] \[[Baughman and Longeauay 2015][research_baughman_longeauay_2015]\] \[[Beaufrere 1988][research_beaufrere_1988]\] \[[Beh et al 2018][research_beh_hofinger_2018]\] \[[Bihrle 1969][research_bihrlejr_1969]\] \[[Bischoff 1983][research_bischoff_1983]\] \[[Blight et al 2018][research_blight_lanedailey_2018]\] \[[Bosworth and Cox 1989][research_bosworth_cox_1989]\] \[[Bouadi][research_bouadi]\] \[[Brandon et al 1995][research_brandon_brown_1995]\] \[[Breul 1963][research_breul_1963]\] \[[Brown 1970][research_brownjr_1970]\] \[[Burton and Kneeland 1981][research_burton_kneelandjr_1981]\] \[[Carlson et al 1965][research_carlson_mabli_1965]\] \[[Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]\] \[[Chetty and Raol 1992][research_chetty_raol_1992]\] \[[Choi et al 2015][research_choi_jimenez_2015]\] \[[Citurs 1984][research_citurs_1984]\] \[[Clark 1964][research_clark_1964]\] \[[Control Allocation and Flight 2016][research_control_allocation_2016]\] \[[Cosenza and Vos 2017][research_cosenza_vos_2017]\] \[[Design Objectives for Flying][research_design_objectives_b]\] \[[Design Objectives for Handling][research_design_objectives]\] \[[Difranco 1969][research_difranco_1969]\] \[[Difranco 1970][research_difranco_1970]\] \[[Efremov et al 1998][research_efremov_ogloblin_1998]\] \[[Enciu et al 2025][research_enciu_2025]\] \[[Eney 1968][research_eney_1968]\] \[[Enns 2015][research_enns_2015]\] \[[Estimation and Sensitivity in 2026][research_estimation_and_2026]\] \[[Feedback Flight Control 2026][research_feedback_flight_2026]\] \[[Fielding and Southworth 2001][research_fielding_southworth_2001]\] \[[Flight Control 2015][research_flight_control_2015]\] \[[Flight control system design 2011][research_flight_control_2011]\] \[[Flight control system for 1999][research_flight_control_1999]\] \[[Flying Qualities 2003][research_flying_qualities_2003]\] \[[Fujimori 2004][research_fujimori_2004]\] \[[Fujimori and Nikiforuk 1999][research_fujimori_nikiforuk_1999]\] \[[Fujimori et al 1997][research_fujimori_wu_1997]\] \[[Fujimori et al 1998][research_fujimori_wu_1998]\] \[[Fujimori et al 2003][research_fujimori_terui_2003]\] \[[Fujimori et al 2005][research_fujimori_terui_2005]\] \[[Fusato and Celi 2006][research_fusato_celi_2006]\] \[[Gain Scheduled Fuzzy Control 2004][research_gain_scheduled_2004]\] \[[Gallagher 1971][research_gallagher_1971]\] \[[Gao et al 2021][research_gao_an_2021]\] \[[Gao et al 2025][research_gao_2025]\] \[[Gaylor 1984][research_gaylor_1984]\] \[[Generally on automatic flight][research_generally_on]\] \[[Gertsen and Shomber 1965][research_gertsen_shomber_1965]\] \[[Gibson 1990][research_gibson_1990]\] \[[Giles 1970][research_giles_1970]\] \[[Giles 1972][research_giles_1972]\] \[[Gonsalves and Zacharias 1994][research_gonsalves_zacharias_1994]\] \[[Gray 1964][research_grayjr_1964]\] \[[Guo 2021][research_guo_2021]\] \[[Hall et al 1974][research_hall_weingarten_1974]\] \[[Harper and Cooper 1984][research_harperjr_cooper_1984]\] \[[Harris et al 2000][research_harris_gautrey_2000]\] \[[Hart 1956][research_hart_1956]\] \[[Hart 1968][research_hart_1968]\] \[[Hess 1981][research_hess_1981]\] \[[Hess 1984][research_hess_1984]\] \[[Hess and Hess 1997][research_hess_hess_1997]\] \[[Hess and Joyce 2013][research_hess_joyce_2013]\] \[[Hoadley and McGraw 1995][research_hoadley_mcgraw_1995]\] \[[Hodgkinson and Lamanna 1977][research_hodgkinson_lamanna_1977]\] \[[Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]\] \[[Hoh and Mitchell 2018][research_hoh_mitchell_2018]\] \[[Huang 1990][research_huang_1990]\] \[[Hutchin 2019][research_hutchin_2019]\] \[[Jenks et al 1977][research_jenks_henry_1977]\] \[[Jianliang Wang and Weiqiang Zhang][research_jianliangwang_weiqiangzhang]\] \[[Karahan 2026][research_karahan_2026]\] \[[Kass 1970][research_kass_1970]\] \[[Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]\] \[[Lawrence and Padfield 2005][research_lawrence_padfield_2005]\] \[[Lawrence and Padfield 2006][research_lawrence_padfield_2006]\] \[[Lee 1975][research_lee_1975]\] \[[Lee and Van Kampen 2021][research_lee_vankampen_2021]\] \[[Lee et al 2003][research_lee_rodchenko_2003]\] \[[Levison 1982][research_levison_1982]\] \[[Lin][research_lin]\] \[[Linear Quadratic Flight Control 2026][research_linear_quadratic_2026]\] \[[Liu et al 2022][research_liu_qian_2022]\] \[[Lu et al 2004][research_lu_wu_2004]\] \[[Malcom 1969][research_malcom_1969]\] \[[Malcom and Husband 1976][research_malcom_husband_1976]\] \[[Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]\] \[[McFarlane et al 2008][research_mcfarlane_richardson_2008]\] \[[McMaster and Schenk 1973][research_mcmaster_schenk_1973]\] \[[Miller 1970][research_miller_1970]\] \[[Miller and Clark 1965][research_miller_clark_1965]\] \[[Multiloop Flight Control Systems 1990][research_multiloop_flight_1990]\] \[[Mushitani and Hiramoto 2019][research_mushitani_hiramoto_2019]\] \[[Musso et al 2026][research_musso_vo_2026]\] \[[Nagy and Kirsten 1976][research_nagy_kirsten_1976]\] \[[Nardi 1970][research_nardi_1970]\] \[[Nasir and Kuntjoro 2013][research_nasir_kuntjoro_2013]\] \[[Nettleton 1965][research_nettleton_1965]\] \[[Nichols et al 1993][research_nichols_reichert_1993]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]\] \[[Nusyirwan and Kung 2016][research_nusyirwan_kung_2016]\] \[[Oosterom and Babuska][research_oosterom_babuska]\] \[[Oosterom and Babuška 2006][research_oosterom_babuska_2006]\] \[[Patterson 1984][research_patterson_1984]\] \[[Petersen 1979][research_petersen_1979]\] \[[Peterson and Grant 2011][research_peterson_grant_2011]\] \[[Placement in Flight Control 2026][research_placement_in_2026]\] \[[Prabhakar et al 2019][research_prabhakar_prazenica_2019]\] \[[Purwanto et al 2001][research_purwanto_riyanto_2001]\] \[[Puyou and Berard 2007][research_puyou_berard_2007]\] \[[Quantitative Design Requirements for 2017][research_quantitative_design_2017]\] \[[Querry][research_querry]\] \[[Rao 2019][research_rao_2019]\] \[[Raol and Singh 2023][research_raol_singh_2023]\] \[[Rhoads 1970][research_rhoads_1970]\] \[[Richardson et al 2003][research_richardson_davison_2003]\] \[[Rickard 1978][research_rickard_1978]\] \[[Rieber and Allgöwer 2006][research_rieber_allgower_2006]\] \[[Sang][research_sang]\] \[[Sato 2013][research_sato_2013]\] \[[Sato 2014][research_sato_2014]\] \[[Sato 2018][research_sato_2018]\] \[[Sato 2022][research_sato_2022]\] \[[Saussié et al 2011][research_saussie_saydy_2011]\] \[[Schmidt 1983][research_schmidt_1983]\] \[[Shanks et al 2018][research_shanks_gale_2018]\] \[[Shimomura][research_shimomura]\] \[[Shmul et al 2018][research_shmul_erenthal_2018]\] \[[Shomber and Gertsen 1967][research_shomber_gertsen_1967]\] \[[Shue et al 1996][research_shue_sawan_1996]\] \[[Shue et al 1998][research_shue_agarwal_1998]\] \[[Simulation Requirements for Flight 2017][research_simulation_requirements_2017]\] \[[Singh and Chowdhury 2021][research_singh_chowdhury_2021]\] \[[Smith et al 1971][research_smith_hammer_1971]\] \[[Sonneveldt et al 2011][research_sonneveldt_chu_2011]\] \[[Stability, Control, and Handling 2024][research_stability_control_2024]\] \[[Tancredi and Corraro 2012][research_tancredi_corraro_2012]\] \[[Teofilatto 2001][research_teofilatto_2001]\] \[[Teper and Stapleford 1965][research_teper_stapleford_1965]\] \[[Teper and Stapleford 1966][research_teper_stapleford_1966]\] \[[Test Techniques for Flight 2021][research_test_techniques_2021]\] \[[Tischler 2018][research_tischler_2018]\] \[[Tischler 2018][research_tischler_2018_b]\] \[[Tomczyk 2001][research_tomczyk_2001]\] \[[Tomczyk 2002][research_tomczyk_2002]\] \[[Tomczyk 2008][research_tomczyk_2008]\] \[[Tomczyk 2008][research_tomczyk_2008_b]\] \[[Van Dam et al 1980][research_vandam_holmes_1980]\] \[[van Dam et al 1981][research_vandam_holmes_1981]\] \[[Vandierendonck 1973][research_vandierendonck_1973]\] \[[Vepa 2023][research_vepa_2023_b]\] \[[Wang et al 2024][research_wang_guo_2024]\] \[[Weingarten and Chalk 1982][research_weingarten_chalk_1982]\] \[[Widowati et al 2012][research_widowati_riyanto_2012]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Wise 1992][research_wise_1992]\] \[[Yang][research_yang]\] \[[Yang et al 2017][research_yang_an_2017]\] \[[Yechout and Oelschlaeger 1976][research_yechout_oelschlaeger_1976]\]

### The oblique wing

**The single-pivot alternative.** The oblique wing from the F-8 model tests through the AD-1 research aircraft to the oblique flying wing, with the aeroelastic divergence and the decoupling control that its asymmetry requires. Of its 131 dated records, 109 date from 1970 to 1999, the years of the AD-1 and the studies around it.

**131 records.** \[[Alag 1987][research_alag_1987]\] \[[Alag and Burken 1987][research_alag_burken_1987]\] \[[Alag et al 1986][research_alag_burken_1986]\] \[[Alag et al 1986][research_alag_kempel_1986]\] \[[Alag et al 1986][research_alag_kempel_1986_b]\] \[[Andrews 1980][research_andrews_1980]\] \[[Andrews et al 1980][research_andrews_sim_1980]\] \[[Black et al 1975][research_black_beamish_1975]\] \[[Bohlmann 1989][research_bohlmann_1989]\] \[[Bohlmann et al 1988][research_bohlmann_weisshaar_1988]\] \[[Bohlmann et al 1990][research_bohlmann_eckstrom_1990]\] \[[Bradley et al 1976][research_bradley_honrath_1976]\] \[[Burken et al 1986][research_burken_alag_1986]\] \[[Cheng 1978][research_cheng_1978]\] \[[Cheng and Meng 1979][research_cheng_meng_1979]\] \[[Cho 2009][research_cho_2009]\] \[[Clark and LeTron 1989][research_clark_letron_1989]\] \[[Crittenden et al 1977][research_crittenden_weisshaar_1977]\] \[[Crittenden et al 1978][research_crittenden_weishaar_1978]\] \[[Curry and Sim 1982][research_curry_sim_1982]\] \[[Curry and Sim 1983][research_curry_sim_1983]\] \[[Curry and Sim 1984][research_curry_sim_1984]\] \[[Dawson and Fortin 1987][research_dawson_fortin_1987]\] \[[Enns et al 1988][research_enns_bugajski_1988]\] \[[Galloway et al 1996][research_galloway_phillips_1996]\] \[[Gilyard 1989][research_gilyard_1989]\] \[[Graham et al 1972][research_graham_jones_1972]\] \[[Graham et al 1973][research_graham_1973]\] \[[Graham et al 1973][research_graham_1973_2]\] \[[Gregory 1985][research_gregory_1985]\] \[[Gwin 1974][research_gwin_1974]\] \[[Gwin 1976][research_gwin_1976]\] \[[Hicks and Mendoza 1973][research_hicks_mendoza_1973]\] \[[Hitch 1978][research_hitch_1978]\] \[[Hopkins 1975][research_hopkins_1975]\] \[[Hopkins 1977][research_hopkins_1977]\] \[[Hopkins and Levin 1974][research_hopkins_levin_1974]\] \[[Hopkins and Levin 1975][research_hopkins_levin_1975]\] \[[Hopkins and Lovette 1976][research_hopkins_lovette_1976]\] \[[Hopkins and Lovette 1976][research_hopkins_lovette_1976_b]\] \[[Hopkins and Lovette 1977][research_hopkins_lovette_1977]\] \[[Hopkins and Nelson 1976][research_hopkins_nelson_1976]\] \[[Hopkins and Yee 1977][research_hopkins_yee_1977]\] \[[Hopkins and Yee 1977][research_hopkins_yee_1977_b]\] \[[Ivanov et al 2018][research_ivanov_mischenko_2018]\] \[[Jones 1948][research_jones_1948]\] \[[Jones 1976][research_jones_1976_b]\] \[[Jones 1976][research_jones_1976_d]\] \[[Jones 1976][research_jones_1976_e]\] \[[Jones 1977][research_jones_1977]\] \[[Jones and Nisbet 1974][research_jones_nisbet_1974]\] \[[Jones and Nisbet 1976][research_jones_1976]\] \[[Jones and Nisbet 1976][research_jones_1976_2]\] \[[Kempel et al 1988][research_kempel_mcneill_1988]\] \[[Kempel et al 1988][research_kempel_mcneill_1988_b]\] \[[Kempel et al 1992][research_kempel_pahle_1992]\] \[[Kennelly et al 1990][research_kennelly_1990]\] \[[Kennelly et al 1992][research_kennelly_strong_1992]\] \[[Kennelly et al 1999][research_kennelly_1999]\] \[[Koltko et al 1975][research_koltko_katz_1975]\] \[[Kroo 1986][research_kroo_1986]\] \[[Kroo 1994][research_kroo_1994]\] \[[Kroo and Van Der Velden 1990][research_kroo_vandervelden_1990]\] \[[Lee 1994][research_lee_1994]\] \[[Lee 1995][research_lee_1995]\] \[[Lee et al 1990][research_lee_miura_1990]\] \[[Li et al 1996][research_li_seebass_1996]\] \[[Li et al 1999][research_li_sobieczky_1999]\] \[[Liebrecht et al 2003][research_liebrecht_neuwerth_2003]\] \[[Liu et al 2026][research_liu_2026]\] \[[Liu et al 2026][research_liu_li_2026]\] \[[Macconochie and Breiner 1989][research_macconochie_breiner_1989]\] \[[MacConochie and Briener 1991][research_macconochie_briener_1991]\] \[[Maine 1977][research_maine_1977]\] \[[Maine 1978][research_maine_1978]\] \[[Manuilovich 2020][research_manuilovich_2020]\] \[[Matušů and Prokop 2015][research_matusu_prokop_2015]\] \[[McDaniel and Wilks 2004][research_mcdaniel_wilks_2004]\] \[[McLachlan et al 1995][research_mclachlan_bell_1995]\] \[[McMurtry et al 1981][research_mcmurtry_sim_1981]\] \[[Mehta 1986][research_mehta_1986]\] \[[Morris 1990][research_morris_1990]\] \[[Nangia and Palmer 2007][research_nangia_palmer_2007]\] \[[A study of the 1973][research_naca_1973]\] \[[Oblique wing transonic transport 1977][research_naca_1977]\] \[[Nathan 2026][research_nathan_2026]\] \[[Nelms 1976][research_nelms_1976]\] \[[Nelms and Bailey 1974][research_nelms_bailey_1974]\] \[[Oblique Wing Aircraft 2020][research_oblique_wing_2020]\] \[[Oblique Wing Remotely Piloted 1974][research_oblique_wing_1974]\] \[[Pahle 1990][research_pahle_1990]\] \[[Painter 1983][research_painter_1983]\] \[[Panina et al 2017][research_panina_kosinov_2017]\] \[[Phillips 1989][research_phillips_1989]\] \[[Pongkorung 2026][research_pongkorung_2026]\] \[[Purser and Spearman 1951][research_purser_spearman_1951]\] \[[Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]\] \[[Rutkowski 1977][research_rutkowski_1977]\] \[[Rutkowski 1979][research_rutkowski_1979]\] \[[Schmidt et al 1988][research_schmidt_moore_1988]\] \[[Selberg et al 1990][research_selberg_1990]\] \[[Sim and Curry 1984][research_sim_curry_1984]\] \[[Sim and Curry 1985][research_sim_curry_1985]\] \[[Smith et al 1975][research_smith_jones_1975]\] \[[Smith et al 1976][research_smith_1976]\] \[[Smith et al 1999][research_smith_kennelly_1999]\] \[[Sun et al 2026][research_sun_2026]\] \[[Tang et al 2007][research_tang_liu_2007]\] \[[Travassos et al 1980][research_travassos_gupta_1980]\] \[[Van der Velden 1987][research_vandervelden_1987]\] \[[Van Der Velden 1992][research_vandervelden_1992]\] \[[Van der Velden and Kroo 1994][research_vandervelden_kroo_1994]\] \[[van der Velden and Torenbeek 1989][research_vandervelden_torenbeek_1989]\] \[[Vandervelden 1989][research_vandervelden_1989]\] \[[Vandervelden and Kroo 1990][research_vandervelden_kroo_1990]\] \[[Vincent 1991][research_vincent_1991]\] \[[Wang et al 2016][research_wang_xu_2016]\] \[[Wang et al 2024][research_wang_sun_2024]\] \[[Waters et al 1992][research_waters_ardema_1992]\] \[[Weisshaar 1974][research_weisshaar_1974]\] \[[Weisshaar 1975][research_weisshaar_1975]\] \[[Weisshaar 1976][research_weisshaar_1976]\] \[[Weisshaar 1990][research_weisshaar_1990]\] \[[Weisshaar 1994][research_weisshaar_1994]\] \[[Weisshaar and Crittenden 1976][research_weisshaar_crittenden_1976]\] \[[White and Bowman 1982][research_white_bowman_1982]\] \[[Wiler and White 1984][research_wiler_white_1984]\] \[[Wiler and White 1985][research_wiler_white_1985]\] \[[Wintzer et al 2006][research_wintzer_sturdza_2006]\] \[[Xu et al 2016][research_xu_yue_2016]\] \[[Yue et al 2019][research_yue_oblique_2019]\]

### Lateral-directional stability and control

**The other two axes.** Rolling and yawing derivatives of swept wings, directional stability and the vertical tail, and roll control.

**95 records.** \[[Ananthkrishnan and Sudhakar 1994][research_ananthkrishnan_sudhakar_1994]\] \[[Ananthkrishnan and Sudhakar 1995][research_ananthkrishnan_sudhakar_1995]\] \[[Beyers and Ericsson 2002][research_beyers_ericsson_2002]\] \[[Bird and Jaquet 1951][research_bird_1951]\] \[[Boisseau and Paulson 1956][research_boisseau_paulson_1956]\] \[[Bourdin 2001][research_bourdin_2001]\] \[[Boyden 1978][research_boyden_1978]\] \[[Brandt et al 2011][research_brandt_fossum_2011]\] \[[Brewer and Fisher 1951][research_brewer_1951]\] \[[Bryson 1954][research_bryson_1954]\] \[[Bryson 1954][research_bryson_1954_b]\] \[[Campbell and Goodman 1949][research_campbell_1949]\] \[[Cancro 1953][research_cancro_1953]\] \[[Chambers et al 1981][research_chambers_1981]\] \[[Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]\] \[[Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]\] \[[Dandwani et al 2025][research_dandwani_bragadoaldana_2025]\] \[[David and Seifert 2012][research_david_seifert_2012]\] \[[Dağ et al 2026][research_dag_ozgur_2026]\] \[[Directional Control 2003][research_directional_control_2003]\] \[[Djahid et al 2022][research_djahid_elena_2022]\] \[[Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]\] \[[Effect of Sweep Angle 2019][research_effect_of_2019]\] \[[Fischel and Schneiter 1948][research_fischel_schneiter_1948]\] \[[Fischel and Watson 1949][research_fischel_watson_1949]\] \[[Fischel et al 1952][research_fischel_naeseth_1952]\] \[[Fisher 1958][research_fisher_1958_b]\] \[[Gebhardt 2017][research_gebhardt_2017]\] \[[Goland 1952][research_goland_1952]\] \[[Goodman and Wolhart 1951][research_goodman_wolhart_1951]\] \[[Gordnier 1995][research_gordnier_1995]\] \[[Hancock 1972][research_hancock_1972]\] \[[Hewes 1951][research_hewes_1951]\] \[[Hong and Roberts 1995][research_hong_roberts_1995]\] \[[Huang and Wu 2006][research_huang_wu_2006]\] \[[Huang et al 2002][research_huang_lin_2002]\] \[[Hunsaker et al 2019][research_hunsaker_montgomery_2019]\] \[[Hunsaker et al 2019][research_hunsaker_moorthamers_2019]\] \[[Johnson and Hagerman 1951][research_johnson_hagerman_1951]\] \[[Kumar et al 2020][research_kumar_mandal_2020]\] \[[Lan 1977][research_lan_1977]\] \[[Lateral Control Power Rolling 2003][research_lateral_control_2003]\] \[[Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]\] \[[Letko and Brewer 1949][research_letko_brewer_1949]\] \[[Letko and Cowan 1948][research_letko_cowan_1948]\] \[[Letko and Jaquet 1948][research_letko_jaquet_1948]\] \[[Lichtenstein 1948][research_lichtenstein_1948]\] \[[Lichtenstein 1952][research_lichtenstein_1952]\] \[[Lichtenstein and Williams 1958][research_lichtenstein_williams_1958]\] \[[Lichtenstein and Williams 1961][research_lichtenstein_williams_1961]\] \[[Llewellyn and Wolhart 1960][research_llewellyn_wolhart_1960]\] \[[Loechert et al 2018][research_loechert_huber_2018]\] \[[Lowenberg 2010][research_lowenberg_2010]\] \[[Maggin and Bennett 1947][research_maggin_bennett_1947]\] \[[McLemore 1958][research_mclemore_1958]\] \[[Modi and Ananthkrishnan 1998][research_modi_ananthkrishnan_1998]\] \[[Mohammed 2007][research_mohammed_2007]\] \[[Musa et al 2015][research_musa_mansor_2015]\] \[[Musa et al 2026][research_musa_mansor_2026]\] \[[Navaratna et al 2022][research_navaratna_lowenberg_2022]\] \[[Pamadi and Pai 1980][research_pamadi_pai_1980]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Pfnür et al 2018][research_pfnur_oppelt_2018]\] \[[Poll 1986][research_poll_1986]\] \[[Poojari 2022][research_poojari_2022]\] \[[Prediction of vortex breakdown 1994][research_prediction_of_1994]\] \[[Putman 1969][research_putman_1969]\] \[[Qin et al 2014][research_qin_wang_2014]\] \[[Queijo and Jaquet 1948][research_queijo_jaquet_1948]\] \[[Queijo and Jaquet 1948][research_queijo_jaquet_1948_b]\] \[[Queijo and Lichtenstein 1948][research_queijo_lichtenstein_1948]\] \[[Raney 1987][research_raney_1987]\] \[[Raney and Batterson 1989][research_raney_batterson_1989]\] \[[Romberg 2003][research_romberg_2003]\] \[[Roysdon and Khalid 2010][research_roysdon_khalid_2010]\] \[[Roysdon and Khalid 2011][research_roysdon_khalid_2011]\] \[[Russell 1996][research_russell_1996]\] \[[Sachs and Moelyadi 2006][research_sachs_moelyadi_2006]\] \[[Schneiter and Fischel 1948][research_schneiter_fischel_1948]\] \[[Schneiter and Watson 1948][research_schneiter_watson_1948]\] \[[Schuette and Hummel 2022][research_schuette_hummel_2022]\] \[[Spearman and Becht 1948][research_spearman_1948]\] \[[Summers 1953][research_summers_1953]\] \[[Tai et al 2023][research_tai_wang_2023]\] \[[Tavoularis 1999][research_tavoularis_1999]\] \[[Tosti 1947][research_tosti_1947]\] \[[Traub 2000][research_traub_2000]\] \[[Ueno et al 1998][research_ueno_matsuno_1998]\] \[[Wang et al 2013][research_wang_qin_2013]\] \[[Wang et al 2026][research_wang_liu_2026]\] \[[Wen et al 2013][research_wen_deng_2013]\] \[[Whittle and Lipson 1954][research_whittle_lipson_1954]\] \[[Williams and DiCamillo 1959][research_williams_dicamillo_1959]\] \[[Wolhart 1951][research_wolhart_1951]\] \[[Zhao et al 2026][research_zhao_guo_2026]\]

### Bird flight and the biological precedent

**The precedent in which the shift of the aerodynamic centre is the point.** Gull, falcon and bat wing morphing measured in animals, and the gull-wing aircraft and bio-inspired wings and drones that copy it for pitch control.

**48 records.** \[[Abdulrahim and Lind 2004][research_abdulrahim_lind_2004]\] \[[Agenbag et al 2009][research_agenbag_theron_2009]\] \[[Ahmer et al 2026][research_ahmer_2026]\] \[[Ajanic et al 2020][research_ajanic_feroskhan_2020]\] \[[Alvarez and Wissa 2021][research_alvarez_wissa_2021]\] \[[Basaeri et al 2014][research_basaeri_yousefikoma_2014]\] \[[Ben-Gida and Gurka 2022][research_bengida_gurka_2022]\] \[[Chang et al 2024][research_chang_chin_2024]\] \[[Chen et al 2026][research_chen_2026]\] \[[Cheng et al 2026][research_cheng_yu_2026]\] \[[Chu et al 2022][research_chu_gu_2022]\] \[[Colorado et al 2015][research_colorado_rossi_2015]\] \[[Davis and Spedding 2015][research_davis_spedding_2015]\] \[[Grauer and Hubbard 2012][research_grauer_hubbard_2012]\] \[[Guo et al 2016][research_guo_hou_2016]\] \[[Guo et al 2017][research_guo_hou_2017]\] \[[Guo et al 2017][research_guo_hou_2017_b]\] \[[Harvey 2023][research_harvey_2023]\] \[[Harvey and Inman 2022][research_harvey_inman_2022]\] \[[Harvey et al 2019][research_harvey_baliga_2019]\] \[[Harvey et al 2021][research_harvey_gull_2021]\] \[[Hui et al 2019][research_hui_zhang_2019]\] \[[Hui et al 2020][research_hui_zhang_2020]\] \[[Hurst et al 2008][research_hurst_wickenheiser_2008]\] \[[Inman et al 2024][research_inman_perry_2024]\] \[[Jeger et al 2024][research_jeger_wuest_2024]\] \[[Li and Cao 2025][research_li_cao_2025]\] \[[Lichter 1974][research_lichter_1974]\] \[[Lin et al 2026][research_lin_yi_2026]\] \[[Liu et al 2026][research_liu_2026_3]\] \[[Ma et al 2016][research_ma_zhou_2016]\] \[[Machireddy 2025][research_machireddy_2025]\] \[[Momodu et al 2026][research_momodu_beg_2026]\] \[[Moulton et al 2026][research_moulton_bolander_2026]\] \[[Newsam et al 2024][research_newsam_midmer_2024]\] \[[Outlaw 2011][research_outlaw_2011]\] \[[Pons and Cirak 2023][research_pons_cirak_2023]\] \[[Selim et al 2021][research_selim_gowree_2021]\] \[[Sharma et al 2025][research_sharma_rana_2025]\] \[[Stacey 2024][research_stacey_2024]\] \[[Stacey and Thomas 2019][research_stacey_thomas_2019]\] \[[Stacey and Thomas 2022][research_stacey_thomas_2022]\] \[[Tang et al 2024][research_tang_shi_2024]\] \[[Wang et al 2026][research_wang_2026]\] \[[Xiao et al 2019][research_xiao_chen_2019]\] \[[Zhan and Wang 2007][research_zhan_wang_2007]\] \[[Zhang et al 2026][research_zhang_2026]\] \[[Zhang et al 2026][research_zhang_yang_2026]\]

### The atmosphere and the flight condition

**The medium, named rather than assumed.** Standard atmosphere tables and properties, which fix the density in the stall speed relations.

**30 records.** \[[A Properties of Standard 2006][research_a_properties_2006]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]\] \[[Appendix A Standard Atmosphere 2021][research_appendix_a_2021]\] \[[Appendix A. The Standard 2011][research_appendix_a_2011_b]\] \[[Appendix B Properties of 2003][research_appendix_b_2003]\] \[[B-34. U. S. Standard 1963][research_b_34_u_1963]\] \[[Definition of the standard 1954][research_definition_of_1954]\] \[[Essenhigh 2006][research_essenhigh_2006]\] \[[International Standard Atmosphere 2010][research_international_standard_2010]\] \[[Kaushik 2018][research_kaushik_2018_b]\] \[[Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]\] \[[Kurzke et al 2025][research_kurzke_halliwell_2025]\] \[[Pressures and Temperatures for 2000][research_pressures_and_2000]\] \[[Properties of the U.S 2014][research_properties_of_2014]\] \[[Properties of the U.S 2024][research_properties_of_2024]\] \[[Report No. 538, altitude-pressure 1935][research_report_no_1935]\] \[[Space environment natural and][research_space_environment]\] \[[Standard Atmosphere 2005][research_standard_atmosphere_2005]\] \[[Standard Atmosphere 2023][research_standard_atmosphere_2023]\] \[[Standard Atmosphere 2024][research_standard_atmosphere_2024]\] \[[Standard atmosphere chart 1927][research_standard_atmosphere_1927]\] \[[Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]\] \[[The Flight Environment Standard 2021][research_the_flight_2021]\] \[[The International Standard Atmosphere 2017][research_the_international_2017]\] \[[The international standard atmosphere 2026][research_the_international_2026]\] \[[The Standard Atmosphere 1964][research_the_standard_1964]\] \[[The Standard Atmosphere 1976][research_the_standard_1976]\] \[[Turns and Kraige][research_turns_kraige]\] \[[US Standard Atmosphere Model 2014][research_us_standard_2014]\] \[[Vaughan 2003][research_vaughan_2003]\]

### Moments of inertia and the time-varying aircraft

**The mass properties on which the spin and the sweep transient depend.** The measurement of aircraft moments of inertia on the ground and from flight data, the moment-of-inertia parameter, and the dynamics and piloting of an aircraft whose inertia changes in flight.

**13 records.** \[[Aircraft moments of inertia 1996][research_aircraft_moments_1996]\] \[[Dantsker et al 2018][research_dantsker_vahora_2018]\] \[[de Jong and Mulder 1987][research_dejong_mulder_1987]\] \[[Gu and Shou 2025][research_gu_shou_2025]\] \[[Han and Hong 2015][research_han_hong_2015]\] \[[Hess 2012][research_hess_2012]\] \[[Iannelli et al 2019][research_iannelli_seiler_2019]\] \[[Morelli 2021][research_morelli_2021]\] \[[Morelli 2022][research_morelli_2022]\] \[[Turner 1950][research_turner_1950]\] \[[Ullah and Devi 1973][research_ullah_devi_1973]\] \[[Valenti and Stanton 2024][research_valenti_stanton_2024]\] \[[Wang et al 2016][research_wang_dong_2016]\]

### Stability and control measured in flight

**The derivatives as a flight programme obtains them.** Stability and control derivatives identified from flight data, and the flight-test methods for static and dynamic stability by which a flight programme reports the quantities this article computes.

**8 records.** \[[Gilyard 1972][research_gilyard_1972]\] \[[Iliff and Taylor 1972][research_iliff_1972]\] \[[Introduction to Stability and 2003][research_introduction_to_2003]\] \[[Irving 1966][research_irving_1966]\] \[[Kamal et al 2015][research_kamal_aly_2015]\] \[[Shafer 1975][research_shafer_1975]\] \[[Smith 1975][research_smith_1975_b]\] \[[Szymanski et al 2025][research_szymanski_ghazi_2025]\]

### Other aeronautical literature on the configuration

**The residual, reported and not hidden.** Aeronautical records on flight research, aircraft dynamics, static stability in general and the research-airplane programmes that belong to no cluster above, together with the foundational works on similarity, viscosity, information and the design of experiments that the article cites.

**75 records.** \[[Abzug and DaRos 1955][research_abzug_daros_1955]\] \[[Advanced Aircraft Control 2026][research_advanced_aircraft_2026]\] \[[Aircraft Dynamic Stability 2003][research_aircraft_dynamic_2003]\] \[[Aircraft Dynamic Stability 2014][research_aircraft_dynamic_2014]\] \[[Aircraft Equations of Motion 2003][research_aircraft_equations_2003]\] \[[Aircraft Non-Linear Dynamics Equations 2014][research_aircraft_non_linear_2014]\] \[[Aircraft Stability and Control 2003][research_aircraft_stability_2003]\] \[[Aircraft Stability and Control 2014][research_aircraft_stability_2014]\] \[[Aircraft Stability and Control 2022][research_aircraft_stability_2022]\] \[[Aircraft Stability and Control 2026][research_aircraft_stability_2026]\] \[[Aircraft Static Stability 2003][research_aircraft_static_2003]\] \[[Aircraft Static Stability 2014][research_aircraft_static_2014]\] \[[Aircraft Static Stability 2024][research_aircraft_static_2024]\] \[[Ananthasayanam 2002][research_ananthasayanam_2002]\] \[[Appendix H Stability Characteristics 2003][research_appendix_h_2003]\] \[[Biber 2016][research_biber_2016]\] \[[Bowers et al 2021][research_bowers_murillo_2021]\] \[[Buckingham 1914][research_buckingham_1914]\] \[[Buffington 1997][research_buffington_1997]\] \[[Buffington 1999][research_buffington_1999]\] \[[Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]\] \[[Chapter 3. Dynamics of 2005][research_chapter_3_2005]\] \[[Complete model of aircraft][research_complete_model]\] \[[Dynamic Stability and Control][research_dynamic_stability]\] \[[Dynamics of Aircraft Motion 2015][research_dynamics_of_2015]\] \[[Dynamics of Very Flexible 2023][research_dynamics_of_2023]\] \[[Erzberger et al 1975][research_erzberger_1975]\] \[[Flight Dynamics of Elastic 2014][research_flight_dynamics_2014]\] \[[Flight Envelope Awareness/Protection][research_flight_envelope]\] \[[From Steady Flight to 2011][research_from_steady_2011]\] \[[From Steady Flight to 2011][research_from_steady_2011_b]\] \[[Fundamentals of Airplane Flight 2007][research_fundamentals_of_2007]\] \[[Gera 1986][research_gera_1986]\] \[[Guerreiro et al 2006][research_guerreiro_hubbard_2006]\] \[[Hale 1976][research_hale_1976]\] \[[Hall 1971][research_hall_1971]\] \[[Hallion 1984][research_hallion_1984]\] \[[Hill 1987][research_hill_1987]\] \[[Holleman 1974][research_holleman_1974]\] \[[Introduction to Airplane Flight][research_introduction_to]\] \[[Ishmael and Wierzbanowski 1985][research_ishmael_wierzbanowski_1985]\] \[[Kotsabasis 1981][research_kotsabasis_1981]\] \[[Larson and Schweikhard 1971][research_larson_schweikhard_1971]\] \[[Lindley 1956][research_lindley_1956]\] \[[Malcolm 1985][research_malcolm_1985]\] \[[Martinez 1961][research_martinez_1961]\] \[[McKenzie 1973][research_mckenzie_1973]\] \[[Methods for Reducing Data 2003][research_methods_for_2003]\] \[[Nominal aircraft dynamics][research_nominal_aircraft]\] \[[Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]\] \[[Nyquist 1928][research_nyquist_1928]\] \[[Pan et al 2026][research_pan_2026]\] \[[Pant and Fielding 1999][research_pant_fielding_1999]\] \[[Prandtl 1928][research_prandtl_1928]\] \[[Putnam and Ayers 1988][research_putnam_ayers_1988]\] \[[Putnam and Ayers 1989][research_putnam_ayers_1989]\] \[[Reed 1975][research_reed_1975]\] \[[Rigid-Body Flight Dynamics 2026][research_rigid_body_flight_2026]\] \[[Shannon 1948][research_shannon_1948]\] \[[Stability Characteristics of Selected 2014][research_stability_characteristics_2014]\] \[[Static Flight Stability and 2026][research_static_flight_2026]\] \[[Static Stability and Control][research_static_stability]\] \[[Static Stability and Control 2010][research_static_stability_2010]\] \[[Stifel 1979][research_stifel_1979]\] \[[Sutherland 1893][research_sutherland_1893]\] \[[Sóbester 2021][research_sobester_2021]\] \[[Takeda 1970][research_takeda_1970]\] \[[Teel 1999][research_teel_1999]\] \[[Teel 1999][research_teel_1999_b]\] \[[Thelander 1965][research_thelander_1965]\] \[[Vepa 2023][research_vepa_2023]\] \[[Vepa 2023][research_vepa_2023_c]\] \[[Vepa 2023][research_vepa_2023_d]\] \[[Drake and Williams 1958][research_williams_drake_1948]\] \[[Wright 1936][research_wright_1936]\]

## Where the Framing Breaks Down

The keystone framework fits the X-5 awkwardly in three ways.

The central number was computable before the aircraft was built. The aerodynamic centre travel derived at the top of this article requires a pivot location and a panel geometry, and both were fixed the moment Bell chose to work from the [P.1101][ref_p1101] layout. An instrument model that treats a research aircraft as reducing uncertainty about a physical quantity struggles when the quantity was arithmetic. What the aircraft reduced uncertainty about was whether the resulting machine would be flyable, a different kind of proposition and one the framework prices badly.

The programme's most valuable output was a negative finding about its own solution. The X-5 demonstrated that in-flight sweep change works and that Bell's way of doing it was the wrong way. A framework that scores a programme by what it settled must handle the case where the settled thing is the programme's approach, and where the eventual answer came from a wind tunnel at a different institution five years later. The X-5 is best understood as having established the value of a problem rather than the value of a solution.

The fatal accident sits outside the keystone entirely. [Hallion 1984][research_hallion_1984] attributes the X-5's spin behaviour to tail placement and the aerodynamic layout and states that it had nothing to do with the variable-sweep wing, and the NASA fact sheet agrees. The analysis above leaves that reading standing, since the inertia parameter that grows with sweep through the span alone is one the NACA correlation rates as no worse for the rudder. Sweep enters the accident through the departure, because the flight reports show pitch-up and directional divergence leading to spins at the highest setting, and an aircraft with the same tail and a fixed wing at that sweep would be expected to share them. A framework organized around a single research question will tend to absorb an accident into that question, and here that would be wrong.

## The Source Base

The primary record is unusually good for a programme whose first aircraft flew about 150 times. The flight reports are [Finch and Briggs 1953][research_finch_1953], [Finch and Walker 1953][research_finch_1953_2], [Childs 1953][research_childs_1953], [Bellman 1953][research_bellman_1953], and [Videan 1955][research_videan_1955], with the load measurements in [Rogers and Dunn 1952][research_rogers_1952], [Reed 1955][research_reed_1955], and [Banner et al 1955][research_banner_1955]. The model work that preceded flight is [Kemp and Becht 1950][research_kemp_1950], [Becht 1950][research_becht_1950], and [Kemp and Few 1951][research_kemp_1951], with the later gust-alleviation study of [Croom and Huffman 1957][research_croom_1957] using the same model. The variable-sweep development literature that followed is large and is cited at length above, with [Polhamus and Toll 1981][research_polhamus_1981] and [Langley Research Center 1966][research_naca_1966] the two summary documents.

The secondary literature treats the aircraft briefly. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment, with [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1984][research_hallion_1984], [Hallion 1981][book_hallion_1981_test_pilots], [Gorn 2001][book_gorn_2001_expanding_envelope], and [Bilstein 1989][book_bilstein_1989_orders] supplying programme and institutional context, and [Gunston 1992][book_gunston_1992_faster_than_sound] and [Wolfe 1979][book_wolfe_1979_right_stuff] the wider and popular framing. [Chambers and Chambers 2008][book_chambers_2008_radical_wings] covers the unconventional configuration lineage.

The engineering texts behind the relations are [Etkin and Reid 1996][book_etkin_reid_1996], [Nelson 1998][book_nelson_1998], [Stengel 2004][book_stengel_2004], [Stevens and Lewis 2015][book_stevens_lewis_2015], [McRuer Ashkenas and Graham 1973][book_mcruer_ashkenas_graham_1973], and [Hurt 1965][book_hurt_1965] for flight dynamics, with [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2002][book_anderson_2002_modern_compressible], [Anderson 2012][book_anderson_2012_aircraft_performance], [Anderson 1997][book_anderson_1997_history_aerodynamics], [Bertin and Cummings 2013][book_bertin_cummings_2013], [Shapiro 1953][book_shapiro_1953], [Liepmann and Roshko 1957][book_liepmann_roshko_1957], [Ashley and Landahl 1965][book_ashley_landahl_1965], [Kuchemann 1978][book_kuchemann_1978], [Schlichting and Gersten 2017][book_schlichting_gersten_2017], and [White 2006][book_white_2006_viscous] for the aerodynamics. Design method is [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], [Roskam 1985][book_roskam_1985], [Stinton 2001][book_stinton_2001], and [Whitford 1987][book_whitford_1987], the last of which is the standard treatment of fighter configuration evolution and therefore of variable sweep as a design choice. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016], aeroelasticity [Bisplinghoff Ashley and Halfman 1955][book_bisplinghoff_ashley_halfman_1955], [Fung 1955][book_fung_1955], and [Dowell 2014][book_dowell_2014], and propulsion [Sutton and Biblarz 2016][book_sutton_biblarz_2016], [Hill and Peterson 1991][book_hill_peterson_1991], and [Huzel and Huang 1992][book_huzel_huang_1992]. Flight test practice is [Kimberlin 2003][book_kimberlin_2003] and [Ward Strganac and Niewoehner 2006][book_ward_strganac_niewoehner_2006], with error analysis in [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], the organizational reading [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error], and the information accounting [Cover and Thomas 2006][book_cover_thomas_2006] with design of experiments in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005], [Gelman et al 2013][book_gelman_et_al_2013], [Lindley 1956][research_lindley_1956], and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]. Sampling and channel capacity are [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948]. Tunnel and institutional histories are [Baals and Corliss 1981][book_baals_corliss_1981] and [Hansen 1987][book_hansen_1987_engineer_in_charge], the theoretical lineage [von Karman and Edson 1967][book_von_karman_edson_1967] and [Gorn 1992][book_gorn_1992_universal_man], and the thermal thread [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier], [Truitt 1960][book_truitt_1960], [Bertin 1994][book_bertin_1994_hypersonic], [Anderson 2006][book_anderson_2006_hypersonic], [Incropera and DeWitt][book_incropera_heat_transfer], [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and [Boley and Weiner 1960][book_boley_weiner_1960], with the X-15 and successor works [Jenkins 2007][book_jenkins_2007_x15], [Jenkins 2000][book_jenkins_2000_hypersonics], [Thompson 1992][book_thompson_1992_edge_of_space], [Launius and Jenkins 2012][book_launius_jenkins_2012], and [Merlin 2009][book_merlin_2009_blackbird].

Foundational primaries bearing on the arguments include [Williams and Drake][research_williams_drake_1948] on the research airplane rationale, [Buckingham 1914][research_buckingham_1914] on similarity, [Sutherland 1893][research_sutherland_1893] on viscosity, [Glauert 1928][research_glauert_1928] and [Prandtl 1928][research_prandtl_1928] on compressibility and the boundary layer, [Jones 1947][research_jones_1947] on planform, [Ackeret 1925][research_ackeret_1925] on supersonic lift, [NACA Report 1135][research_naca_1135] for the compressible relations, [Theodorsen 1935][research_theodorsen_1935], [Collar 1946][research_collar_1946], and [Garrick and Reed 1981][research_garrick_reed_1981] on aeroelasticity, [Phillips 1948][research_phillips_1948] on rolling coupling, [Beeler et al 1956][research_beeler_1956] on drag measurement, and [Wright 1936][research_wright_1936] on unit cost at these quantities. The wider configuration context appears in [James and Maki 1957][research_james_1957], [Quigley et al 1960][research_quigley_1960], [Whitcomb and Norton 1961][research_whitcomb_1961], [Cornette 1961][research_cornette_1961], [Funk and Cooney 1959][research_funk_1959], [Burk and Libbey 1961][research_burk_1961], [Lee 1964][research_lee_1964], [Lee and Healy 1964][research_lee_1964_2], [Hanson 1973][research_hanson_1973], [Bartlett et al 1973][research_bartlett_1973], and [Monfort and Whitcomb 1975][research_monfort_1975]. The equivalent problems at model scale are worked on this blog in [Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_a118_propulsion_sizing], [Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_a120_staged_boosted_propulsion], [Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_a122_stability_configuration], [Dynamic Stability and Control for Fixed-Wing UAVs][related_post_a123_dynamic_stability], and [Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_a127_structures_flight_envelope], the rocketplane lineage in [History of Rocketplanes][related_post_a96_history_rocketplanes], large high-speed configurations in [Two-Stage Flying Delta Wing Vehicles for Civil and National Security Applications][related_post_a106_two_stage_delta_wing], propellant chemistry in [Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217_rocket_propellant_chemistry], the computing and simulation infrastructure in [Aerospace, Programming Languages, and Information Technology Co-Development: Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing] and [Aerospace, Programming Languages, and Information Technology Co-Development: Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation], and space policy in [Introduction to Space Studies][related_post_a90_intro_space_studies]. The [NASA Technical Reports Server][ref_ntrs] and the [NASA History Office][ref_nasa_x3_factsheet] hold the record, with the [Armstrong Flight Research Center][ref_nasa_armstrong] the institutional successor and the [wind tunnel][ref_wind_tunnel] and [flight test][ref_flight_test] literatures the methodological background.

**The survey rests on 4,052 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 899 are report primaries by the identifier rule set out under The Definition of Primary, being 22.2 percent. Of the 3,985 dated records, the median year of publication is 2006, 1,701 were published before 2000, and 1,467, or 36.8 percent, in 2015 or later. The article's own argument rests on the 257 research records cited in its prose before this section, of which 164 are report primaries.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when it is a NASA Technical Reports Server record or carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. By that rule 767 records are NASA Technical Reports Server records and 132 are Defense Technical Information Center reports. **The rule suits this aircraft unusually well**, because the X-5's flight reports, load measurements and model tests are research memoranda of the National Advisory Committee for Aeronautics and are held by the NASA Technical Reports Server.

**The rule still undercounts what is first-hand.** A journal or conference paper written by the people who flew or tested a configuration is a primary source for that configuration, and an identifier rule cannot see it, so the F-14 transition papers in the American Institute of Aeronautics and Astronautics series and the modern morphing flight tests are counted as secondary. 22.2 percent is a lower bound on how much of this survey is first-hand.

### Thin Subjects

**Five subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| the aerodynamic centre travel of a pivoting wing and the pivot location | pivot location, outboard pivot, double pivot, aerodynamic center movement, aerodynamic center shift, aerodynamic centre movement | 7 |
| the structure and bearing of the pivot | pivot fitting, pivot bearing, pivot joint, pivot mechanism, pivot system, pivot fairing, carry through | 5 |
| translating the wing to hold the aerodynamic centre | translating wing, wing translation, translating, fore and aft, sliding wing | 2 |
| the spin inertia parameter and the relative density | inertia parameter, moment of inertia parameter, relative density, mass distribution, inertia yawing | 3 |
| the rate of a shape change against the aircraft's own modes | morphing process, morphing rate, sweep rate, time varying inertia, during morphing, quasi static, quasi steady | 13 |

**The keystone relation of this article has a literature of a handful of reports.** Six of the seven records on pivot location and the travel of the aerodynamic centre are reports of 1960 to 1972 on variable-sweep configurations, [Bielat and Pierpont 1960][research_bielat_1960], [Hammond and Henderson 1961][research_hammond_1961], [Alford et al 1962][research_alford_1962], [Henderson and Ray 1964][research_henderson_1964], [Lamar 1968][research_lamar_1968] and [Huffman 1972][research_huffman_1972]. The subject closed when the outboard pivot answered it, and the remaining record, [van Dommelen et al 2019][research_vandommelen_dsilva_2019], concerns the shift that a body induces on a fixed wing. **The pivot as a structure is documented mainly through one aircraft's service experience.** Three of its five records, [Burchill et al 2002][research_burchill_mcdonald_2002], [Chester 2002][research_chester_2002] and [Molent and Jones 2018][research_molent_jones_2018], concern the fatigue, reinforcement and repair of the F-111's wing pivot fitting, and the others, [Losee et al 1980][research_losee_willis_1980] and [Priest et al 2023][research_priest_snyder_2023], a pivot fairing and a pivot mechanism. **The translating wing that the X-5 used has no literature of its own in this survey**, and the two records that carry the word, [Macconochie and Breiner 1989][research_macconochie_breiner_1989] and [MacConochie and Briener 1991][research_macconochie_briener_1991], concern a translating oblique wing on a launch vehicle, which is consistent with a mechanism that one aircraft used and none repeated.

### What the Survey Admits

**The research survey admits a record only when a person reading its title finds it on this article's subject.** Candidate records are drawn from the three archives by title against this article's subject vocabulary, which names the swept and pivoting wing, morphing, the spin, stability and trim, aeroelasticity, crossflow transition and the standard atmosphere, and every title so drawn has then been read, so the vocabulary proposes records and the reading decides them.

**Many words this subject depends on also name something else, and a record that shares only such a word is excluded.** Sweep also names frequency and sine sweeps and the sweep rate of voltammetry, and swept also names swept-source optics and the swept volume of an engine. Spin also names the spin of electrons and nuclei and the spin coating of surfaces. Morphing also names image and mesh morphing. Wing also names the political wing, the military wing as a unit, the rear wing of a racing car, the insect wing of developmental biology, and the gull-wing shape of electronic packages, bridges and lenses, and gull also names a seabird studied for its ecology and its parasites. Rotary wing names the helicopter rotor, and the spin of a projectile or a spacecraft is not the spin of an aeroplane. Flutter also names a cardiac rhythm and a software framework, and variable geometry also names turbochargers and turbine vanes. The standard atmosphere of materials conditioning is not the atmosphere of flight. Correction, erratum and retraction notices, and the indexes and front matter of books, are excluded as well, because a survey counts research works and those are editorial events or parts of works.

**Records on the aeroplane wing that bear on none of the subjects this argument uses are excluded too.** Ground effect, the tip vortex and the wake of an unswept wing, formation flight and the encounter of one aircraft with another's wake, the unsteady pitching, plunging and dynamic stall of unswept wings and aerofoils, the aerodynamics of micro air vehicles at low Reynolds number, the installation of propellers, nacelles, nozzles and inlets, the separation and loading of external stores, the wings of missiles and the rotors of rotor-wing hybrids, the fabrication, materials and component tests of particular airframes, whole-aircraft weight estimation, tunnel facilities and the correction of tunnel walls, fault-tolerant and damaged-aircraft control, and the performance testing of light aircraft and airliners are each a literature of its own on which no derivation here depends. The design of the wing's primary structure, its root, carry-through, joints and structural weight, is kept, because the pivot is sized here against the load path it replaces. A title that names sweep, a delta planform, the stall of a swept wing, flutter or morphing keeps such a record, so the pitching swept wing and the flutter of a wing carrying stores remain. Generic chapters, appendices and bibliographies whose titles name no subject of this article are excluded with the editorial items.

**Reviews of books, reference and definition entries and notices are not admitted, and a document deposited twice is admitted once.** An authored encyclopedia article of more than two pages and a chapter of a textbook are research works and are kept, and where one document is held twice the journal or report version is the one admitted.

**The residual cluster admits a record only when it concerns the dynamics, stability, control or flight research of an aeroplane in general and belongs to no named cluster, or is a foundational work that the article cites.** Its 75 records include flight dynamics and stability texts and chapters, flight research programmes and their methods, the control of tailless and control-configured aircraft, mission and takeoff performance analyses, and the cited works on similarity, viscosity, information and the design of experiments.

**Some records of doubtful relevance are kept.** Rotor blades with swept tips, crossflow instability on the rotating disk, ice accretion on swept wings and the wind-tunnel aerodynamics of tilt-wing models each share a phenomenon or a method with the swept-wing literature of this subject, so each is kept and a reader may weigh it accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement rather than of sampling.** Many of the records removed are rotorcraft records, because rotary wing names the helicopter rotor as well as the aeroplane's wing, and a rotorcraft record is kept only when its title concerns sweep, morphing, aeroelasticity or a wing.

## Epistemic State

Established historical fact includes the capture of the P.1101 in April 1945 and its delivery to Bell, its ground-adjustable sweep, the building of two aircraft with serials 50-1838 and 50-1839, the completion of the first on 15 February 1951, the first flights on 20 June and 10 December 1951, the three sweep detents at 20, 40, and 60 degrees, the jackscrew and rail mechanism with disc brake locking, the sweep transit time of under thirty seconds, the loss of the second aircraft in a spin at 60 degrees sweep on 13 October 1953 with the death of its pilot, the continued use of the first aircraft to 1955 and as a chase aircraft to 1958, and its preservation at the National Museum of the United States Air Force. Several of these rest on a single source. The dimensions, weights and engine rating come from one compiled specification, and the disc brake locking and the thirty-second transit come from one secondary account that gives no source for them, although the NASA fact sheet confirms the rails, the forward translation and a transit of about twenty seconds.

Established engineering analysis includes every relation in the sizing sections. The pivot recovery from two spans, the aerodynamic centre travel relation, the aspect ratio and lift-curve slope variation with sweep, the stall speed relation, the neutral point decomposition, the spin inertia parameter, the tail volume coefficients, and the drag polar decomposition are standard results applied to published dimensions.

**Derived here and not taken from a source** are the pivot station of 0.95 metres and 18.7 percent of semi-span, the movable panel length of 4.42 metres, the aerodynamic centre travel of 0.93 metres or 58 percent of mean chord, the lift-curve slope ratio of 2.09 across the sweep range, the stall speed pair of 60.6 and 83.1 metres per second, the pivot bending moment of $1.63 \times 10^{5}$ newton metres, the factor of 2.61 by which the spin inertia parameter grows in magnitude between the sweep extremes, and the parameter values of $-0.0345$ at 58.7 degrees and no more negative than $-0.0136$ at 20 degrees, with the relative density ratio of 1.45, computed from the NACA's measured inertias, weights, areas and spans. These follow by arithmetic from published spans, areas, inertias and weights, and any reader with those inputs can reproduce or refute them.

Inference includes the reading of the spin. The factor of 2.61 is arithmetic. That its growth does not make recovery by the rudder harder is an inference from a correlation built on fixed-wing models at lower relative densities than the X-5 at altitude, and the attribution of the poor recovery to the tail and layout rests on Hallion 1984 and the NASA fact sheet. The flight reports establish that the aircraft departed into spins at the highest sweep setting. None of the sources consulted gives the entry or the recovery attempt of the fatal spin beyond its 60 degree sweep setting.

Weakly supported are the representative values. The roll inertia at 20 degrees was not reported, so the parameter at that setting is a bound, and the ratio between the two sweep settings computed from the spans alone is more trustworthy than either absolute value. The panel lift fraction of sixty percent, the aerodynamic centre at forty percent of panel length, the maximum lift coefficient of 1.20, and the structural mass increment of three percent are all representative figures. The taking of the quoted sweep angles as half-chord sweep in the lift-curve slope estimate is an approximation of unknown size.

Contested or unresolved in the sources consulted is the date on which the aircraft passed to the Air Force and the NACA, the sweep transit time, given as under thirty seconds and as about twenty, the exact flight total, given as almost two hundred and as 149, with the first aircraft's flights summing to 148 from the NASA fact sheet's counts and the NACA's alone given as 122 or as flight numbers running to 133, while no source consulted counts the second aircraft's flights, the maximum conditions, given as about Mach 0.9 and 40,000 feet and as Mach 0.98 and 42,000 feet, which aircraft was lost, since one inventory names the first where the NACA record names the second, and whether a spin-tunnel investigation of the X-5 configuration was performed before the loss. No such report was located, which is not the same as none existing.

A note on temporal position. This article carries an editorial date of 2025-10-11 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the [X-1][related_post_a298_bell_x1], [X-2][related_post_a299_bell_x2], [X-3][related_post_a300_douglas_x3], or [X-4][related_post_a301_northrop_x4] beyond the comparisons drawn, all of which have their own articles, nor the [X-15][ref_na_x15], which appears later. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficients, [lift-to-drag][ref_lift_to_drag], [Reynolds][ref_reynolds_number] and [Prandtl][ref_prandtl_number] numbers, [measurement uncertainty][ref_measurement_uncertainty] and its [propagation][ref_propagation_of_uncertainty], and the [standard atmosphere][ref_isa] in its [tabulated form][ref_us_standard_atmosphere].

It does not attempt a history of the [F-111][ref_f111] or the other production variable-sweep aircraft, which are named only as inheritors, nor of the [P.1101][ref_p1101] except as ancestor. It does not cover [shock waves][ref_shock_wave] and [oblique shocks][ref_oblique_shock], [wave drag][ref_wave_drag], [supersonic][ref_supersonic_speed] flow, [boundary layer][ref_boundary_layer] and [separation][ref_flow_separation] behaviour, [buffeting][ref_buffeting], [aerodynamic centre][ref_aerodynamic_center] and [mean aerodynamic chord][ref_mac] theory, [longitudinal][ref_longitudinal_static_stability] and [directional][ref_directional_stability] stability as general subjects, the [phugoid][ref_phugoid], [flight dynamics][ref_flight_dynamics] generally, [inertia coupling][ref_inertia_coupling] and [Euler's equations][ref_euler_equations_rigid], [moments of inertia][ref_moment_of_inertia] as a subject, [reaction control][ref_rcs], [stabilators][ref_stabilator], [yaw dampers][ref_yaw_damper], [stability augmentation][ref_stability_augmentation], [duralumin][ref_duralumin], [yield][ref_yield_strength], [telemetry][ref_telemetry], [strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], the [sound barrier][ref_sound_barrier], [transonic][ref_transonic] flow, the [aspect ratio][ref_aspect_ratio], [wing twist][ref_wing_twist], [wing root][ref_wing_root] structure, [wing configuration][ref_wing_configuration] as a taxonomy, [delta wings][ref_delta_wing], [Mach][ref_mach_number] and [dynamic pressure][ref_dynamic_pressure] as quantities, the [speed of sound][ref_speed_of_sound], [takeoff][ref_takeoff] and [landing gear][ref_landing_gear], [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, the [National Museum of the United States Air Force][ref_nmusaf], the [list of X-planes][ref_list_of_x_planes], or [experimental aircraft][ref_experimental_aircraft] as a category, all of which are treated where they belong.

## Conclusion

The Bell X-5 was built to find out whether a wing could change its sweep in flight, and it found out, and the answer has a number attached to it.

Sweeping a pivoting wing translates its aerodynamic centre by the panel arm times the change in the sine of the sweep angle. For the X-5 that is 0.93 metres, or 58 percent of the mean chord, four to eleven times the entire static margin of a conventional aeroplane. Bell absorbed it by translating the wing forward on rails as it swept back, which worked partially, cost mass, and put the full wing bending moment through a moving joint. Langley later found that moving the pivot outboard and leaving a fixed glove inboard shrinks the same travel by the product of two factors and needs no mechanism at all. That finding put variable sweep into the F-111, the F-14, the Tornado, the B-1, and their Soviet contemporaries, and it dissolved a design problem that Bell had tried to solve.

The programme also carried a hazard, and the same geometry explains less of it than it first appears to. The NACA's spin-recovery correlating parameter carries the square of the span in its denominator, and sweeping the X-5's wing back shortens the span from 10.21 metres to 6.32, so the parameter grows in magnitude by a factor of 2.61 with no change in mass distribution. The NACA's correlation reads that growth as favourable to recovery by the rudder. The aircraft that was lost was lost at the highest sweep setting, where the flight reports record pitch-up and directional divergence into spins, and the histories attribute its poor recovery to the tail and the aerodynamic layout. The lever had moved, but the sources place the outcome with the tail.

One inequality made the aircraft flyable. The sweep took twenty to thirty seconds and the aircraft's short period took two, so the geometry change was ten to fifteen times slower than the dynamics it perturbed and the pilot met a slow drift rather than a step. Modern morphing aircraft do not always enjoy that margin, which is why so much of the contemporary literature is about the transient rather than the endpoints.

The next article takes the [Convair X-6][ref_convair_x6], the [nuclear-powered][ref_anp] aircraft that was never built, and asks what a programme cancelled before flight can be said to have established.

## References

### Books

- [Anderson 1997 A History of Aerodynamics][book_anderson_1997_history_aerodynamics]
- [Anderson 2001 Fundamentals of Aerodynamics][book_anderson_2001_fundamentals]
- [Anderson 2002 Modern Compressible Flow][book_anderson_2002_modern_compressible]
- [Anderson 2006 Hypersonic and High-Temperature Gas Dynamics][book_anderson_2006_hypersonic]
- [Anderson 2012 Aircraft Performance and Design][book_anderson_2012_aircraft_performance]
- [Ashley and Landahl 1965 Aerodynamics of Wings and Bodies][book_ashley_landahl_1965]
- [Baals and Corliss 1981 Wind Tunnels of NASA][book_baals_corliss_1981]
- [Bertin 1994 Hypersonic Aerothermodynamics][book_bertin_1994_hypersonic]
- [Bertin and Cummings 2013 Aerodynamics for Engineers][book_bertin_cummings_2013]
- [Bevington and Robinson 2002 Data Reduction and Error Analysis][book_bevington_robinson_2002]
- [Bilstein 1989 Orders of Magnitude, A History of the NACA and NASA][book_bilstein_1989_orders]
- [Bisplinghoff Ashley and Halfman 1955 Aeroelasticity][book_bisplinghoff_ashley_halfman_1955]
- [Boley and Weiner 1960 Theory of Thermal Stresses][book_boley_weiner_1960]
- [Box Hunter and Hunter 2005 Statistics for Experimenters][book_box_hunter_hunter_2005]
- [Bruhn 1973 Analysis and Design of Flight Vehicle Structures][book_bruhn_1973]
- [Carslaw and Jaeger 1959 Conduction of Heat in Solids][book_carslaw_jaeger_1959]
- [Chambers and Chambers 2008 Radical Wings and Wind Tunnels][book_chambers_2008_radical_wings]
- [Cover and Thomas 2006 Elements of Information Theory][book_cover_thomas_2006]
- [Dowell 2014 A Modern Course in Aeroelasticity][book_dowell_2014]
- [Etkin and Reid 1996 Dynamics of Flight, Stability and Control][book_etkin_reid_1996]
- [Ferguson 1992 Engineering and the Mind's Eye][book_ferguson_1992]
- [Fung 1955 An Introduction to the Theory of Aeroelasticity][book_fung_1955]
- [Gelman et al 2013 Bayesian Data Analysis][book_gelman_et_al_2013]
- [Gorn 1992 The Universal Man, Theodore von Karman][book_gorn_1992_universal_man]
- [Gorn 2001 Expanding the Envelope, Flight Research at NACA and NASA][book_gorn_2001_expanding_envelope]
- [Gunston 1992 Faster Than Sound][book_gunston_1992_faster_than_sound]
- [Hallion 1972 Supersonic Flight, Breaking the Sound Barrier and Beyond][book_hallion_1972_supersonic_flight]
- [Hallion 1981 Test Pilots, The Frontiersmen of Flight][book_hallion_1981_test_pilots]
- [Hansen 1987 Engineer in Charge][book_hansen_1987_engineer_in_charge]
- [Heppenheimer 2007 Facing the Heat Barrier, A History of Hypersonics][book_heppenheimer_2007_heat_barrier]
- [Hill and Peterson 1991 Mechanics and Thermodynamics of Propulsion][book_hill_peterson_1991]
- [Hurt 1965 Aerodynamics for Naval Aviators][book_hurt_1965]
- [Huzel and Huang 1992 Modern Engineering for Design of Liquid-Propellant Rocket Engines][book_huzel_huang_1992]
- [Incropera and DeWitt, Fundamentals of Heat and Mass Transfer][book_incropera_heat_transfer]
- [Jenkins 2000 Hypersonics Before the Shuttle][book_jenkins_2000_hypersonics]
- [Jenkins 2007 X-15, Extending the Frontiers of Flight][book_jenkins_2007_x15]
- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Kimberlin 2003 Flight Testing of Fixed-Wing Aircraft][book_kimberlin_2003]
- [Kuchemann 1978 The Aerodynamic Design of Aircraft][book_kuchemann_1978]
- [Launius and Jenkins 2012 Coming Home, Reentry and Recovery from Space][book_launius_jenkins_2012]
- [Liepmann and Roshko 1957 Elements of Gasdynamics][book_liepmann_roshko_1957]
- [McRuer Ashkenas and Graham 1973 Aircraft Dynamics and Automatic Control][book_mcruer_ashkenas_graham_1973]
- [Megson 2016 Aircraft Structures for Engineering Students][book_megson_2016]
- [Merlin 2009 Design and Development of the Blackbird][book_merlin_2009_blackbird]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001_x_planes]
- [Nelson 1998 Flight Stability and Automatic Control][book_nelson_1998]
- [Nicolai and Carichner 2010 Fundamentals of Aircraft and Airship Design][book_nicolai_carichner_2010]
- [Niu 1988 Airframe Structural Design][book_niu_1988_airframe]
- [Peebles 2014 Probing the Sky, Selected NACA Research Airplanes][book_peebles_2014_probing_the_sky]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Petroski 1985 To Engineer Is Human][book_petroski_1985]
- [Raymer 2018 Aircraft Design, A Conceptual Approach][book_raymer_2018]
- [Reason 1990 Human Error][book_reason_1990_human_error]
- [Roskam 1985 Airplane Design][book_roskam_1985]
- [Sagan 1993 The Limits of Safety][book_sagan_1993]
- [Schlichting and Gersten 2017 Boundary-Layer Theory][book_schlichting_gersten_2017]
- [Shapiro 1953 The Dynamics and Thermodynamics of Compressible Fluid Flow][book_shapiro_1953]
- [Stengel 2004 Flight Dynamics][book_stengel_2004]
- [Stevens and Lewis 2015 Aircraft Control and Simulation][book_stevens_lewis_2015]
- [Stinton 2001 The Design of the Aeroplane][book_stinton_2001]
- [Sutton and Biblarz 2016 Rocket Propulsion Elements][book_sutton_biblarz_2016]
- [Taylor 1997 An Introduction to Error Analysis][book_taylor_1997_error_analysis]
- [Thompson 1992 At the Edge of Space][book_thompson_1992_edge_of_space]
- [Torenbeek 1982 Synthesis of Subsonic Airplane Design][book_torenbeek_1982]
- [Truitt 1960 Fundamentals of Aerodynamic Heating][book_truitt_1960]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Vincenti 1990 What Engineers Know and How They Know It][book_vincenti_1990]
- [von Karman and Edson 1967 The Wind and Beyond][book_von_karman_edson_1967]
- [Ward Strganac and Niewoehner 2006 Introduction to Flight Test Engineering][book_ward_strganac_niewoehner_2006]
- [White 2006 Viscous Fluid Flow][book_white_2006_viscous]
- [Whitford 1987 Design for Air Combat][book_whitford_1987]
- [Winchester 2005 X-Planes and Prototypes][book_winchester_2005_x_planes]
- [Wolfe 1979 The Right Stuff][book_wolfe_1979_right_stuff]

### Reference

- [NASA Armstrong Flight Research Center][ref_nasa_armstrong]
- [NASA History Office][ref_nasa_x3_factsheet]
- [NASA Technical Reports Server][ref_ntrs]
- [NASA X-5 Fact Sheet][ref_nasa_x5_factsheet]
- [Wikipedia Article on Aeroelasticity][ref_aeroelasticity]
- [Wikipedia Article on Aircraft Nuclear Propulsion][ref_anp]
- [Wikipedia Article on Bell Aircraft][ref_bell_aircraft]
- [Wikipedia Article on Directional Stability][ref_directional_stability]
- [Wikipedia Article on Duralumin][ref_duralumin]
- [Wikipedia Article on Dutch Roll][ref_dutch_roll]
- [Wikipedia Article on Dynamic Pressure][ref_dynamic_pressure]
- [Wikipedia Article on Edwards Air Force Base][ref_edwards_afb]
- [Wikipedia Article on Euler's Equations for Rigid Body Dynamics][ref_euler_equations_rigid]
- [Wikipedia Article on Experimental Aircraft][ref_experimental_aircraft]
- [Wikipedia Article on Flight Dynamics][ref_flight_dynamics]
- [Wikipedia Article on Flight Testing][ref_flight_test]
- [Wikipedia Article on Flow Separation][ref_flow_separation]
- [Wikipedia Article on Inertia Coupling][ref_inertia_coupling]
- [Wikipedia Article on Landing Gear][ref_landing_gear]
- [Wikipedia Article on Longitudinal Static Stability][ref_longitudinal_static_stability]
- [Wikipedia Article on Measurement Uncertainty][ref_measurement_uncertainty]
- [Wikipedia Article on NASA][ref_nasa]
- [Wikipedia Article on Operation Lusty][ref_operation_lusty]
- [Wikipedia Article on Propagation of Uncertainty][ref_propagation_of_uncertainty]
- [Wikipedia Article on Scott Crossfield][ref_crossfield]
- [Wikipedia Article on Supersonic Speed][ref_supersonic_speed]
- [Wikipedia Article on Takeoff][ref_takeoff]
- [Wikipedia Article on Telemetry][ref_telemetry]
- [Wikipedia Article on the Accelerometer][ref_accelerometer]
- [Wikipedia Article on the Adaptive Compliant Wing][ref_compliant_wing]
- [Wikipedia Article on the Aerodynamic Center][ref_aerodynamic_center]
- [Wikipedia Article on the Allison J35][ref_j35]
- [Wikipedia Article on the Armstrong Flight Research Center][ref_armstrong_frc]
- [Wikipedia Article on the Aspect Ratio][ref_aspect_ratio]
- [Wikipedia Article on the Bell X-5][ref_bell_x5]
- [Wikipedia Article on the Boundary Layer][ref_boundary_layer]
- [Wikipedia Article on the Convair X-6][ref_convair_x6]
- [Wikipedia Article on the Delta Wing][ref_delta_wing]
- [Wikipedia Article on the Drag Coefficient][ref_drag_coefficient]
- [Wikipedia Article on the Flight Envelope][ref_flight_envelope]
- [Wikipedia Article on the General Dynamics F-111 Aardvark][ref_f111]
- [Wikipedia Article on the Grumman F-14 Tomcat][ref_f14]
- [Wikipedia Article on the International Standard Atmosphere][ref_isa]
- [Wikipedia Article on the Jackscrew][ref_jackscrew]
- [Wikipedia Article on the Leading-Edge Slat][ref_slat]
- [Wikipedia Article on the Lift Coefficient][ref_lift_coefficient]
- [Wikipedia Article on the Lift-to-Drag Ratio][ref_lift_to_drag]
- [Wikipedia Article on the Load Factor][ref_load_factor]
- [Wikipedia Article on the Mach Number][ref_mach_number]
- [Wikipedia Article on the Mean Aerodynamic Chord][ref_mac]
- [Wikipedia Article on the Messerschmitt P.1101][ref_p1101]
- [Wikipedia Article on the Mikoyan-Gurevich MiG-23][ref_mig23]
- [Wikipedia Article on the Mikoyan-Gurevich MiG-27][ref_mig27]
- [Wikipedia Article on the Moment of Inertia][ref_moment_of_inertia]
- [Wikipedia Article on the NACA Airfoil][ref_naca_airfoil]
- [Wikipedia Article on the National Advisory Committee for Aeronautics][ref_naca]
- [Wikipedia Article on the National Museum of the United States Air Force][ref_nmusaf]
- [Wikipedia Article on the North American X-15][ref_na_x15]
- [Wikipedia Article on the North American XB-70 Valkyrie][ref_xb70]
- [Wikipedia Article on the Oblique Shock][ref_oblique_shock]
- [Wikipedia Article on the Oblique Wing][ref_oblique_wing]
- [Wikipedia Article on the Panavia Tornado][ref_tornado]
- [Wikipedia Article on the Phugoid][ref_phugoid]
- [Wikipedia Article on the Prandtl Number][ref_prandtl_number]
- [Wikipedia Article on the Reaction Control System][ref_rcs]
- [Wikipedia Article on the Reynolds Number][ref_reynolds_number]
- [Wikipedia Article on the Rockwell B-1 Lancer][ref_b1_lancer]
- [Wikipedia Article on the Shock Wave][ref_shock_wave]
- [Wikipedia Article on the Sound Barrier][ref_sound_barrier]
- [Wikipedia Article on the Speed of Sound][ref_speed_of_sound]
- [Wikipedia Article on the Spin][ref_spin]
- [Wikipedia Article on the Stabilator][ref_stabilator]
- [Wikipedia Article on the Stability Augmentation System][ref_stability_augmentation]
- [Wikipedia Article on the Strain Gauge][ref_strain_gauge]
- [Wikipedia Article on the Sukhoi Su-17][ref_su17]
- [Wikipedia Article on the Sukhoi Su-24][ref_su24]
- [Wikipedia Article on the Swept Wing][ref_swept_wing]
- [Wikipedia Article on the Tupolev Tu-160][ref_tu160]
- [Wikipedia Article on the Tupolev Tu-22M][ref_tu22m]
- [Wikipedia Article on the U.S. Standard Atmosphere][ref_us_standard_atmosphere]
- [Wikipedia Article on the Wind Tunnel][ref_wind_tunnel]
- [Wikipedia Article on the Wing Root][ref_wing_root]
- [Wikipedia Article on the Yaw Damper][ref_yaw_damper]
- [Wikipedia Article on Transonic Flow][ref_transonic]
- [Wikipedia Article on Wave Drag][ref_wave_drag]
- [Wikipedia Article on Wing Configuration][ref_wing_configuration]
- [Wikipedia Article on Wing Loading][ref_wing_loading]
- [Wikipedia Article on Wing Twist][ref_wing_twist]
- [Wikipedia Article on Yield in Engineering][ref_yield_strength]
- [Wikipedia List of X-Planes][ref_list_of_x_planes]
- [Wikipedia Section on Buffeting][ref_buffeting]

### Research

- [2017][research_rea_pecora_2017]
- [A Method for Predicting][research_lowry_1957]
- [A Properties of Standard 2006][research_a_properties_2006]
- [A study of the 1973][research_naca_1973]
- [A'Harrah 1964][research_aharrah_1964]
- [A-7 Transonic Wing Designs 1982][research_a_7_transonic_1982]
- [Abdelghany et al 2016][research_abdelghany_khalil_2016]
- [Abdelhamid and Kandil 1998][research_abdelhamid_kandil_1998]
- [Abdessemed et al 2018][research_abdessemed_yao_2018]
- [Abdullaev A et al 2024][research_abdullaeva_moralevi_2024]
- [Abdulrahim 2005][research_abdulrahim_2005]
- [Abdulrahim and Lind 2004][research_abdulrahim_lind_2004]
- [Abegg et al 2000][research_abegg_bippes_2000]
- [Abel et al 1966][research_abel_1966]
- [Abou Khalil][research_aboukhalil]
- [Abraham-Doman and Merrett 2014][research_abrahamdoman_merrett_2014]
- [Abrego et al 1999][research_abrego_maier_1999]
- [Abzug and DaRos 1955][research_abzug_daros_1955]
- [Ackeret 1925][research_ackeret_1925]
- [Ackeret et al 1951][research_ackeret_1951]
- [Acree et al 2004][research_acree_peyran_2004]
- [Adams 1972][research_adams_1972]
- [Adams 1973][research_adams_1973]
- [Adams and Hatch 1970][research_adams_hatchjr_1970]
- [Adegbindin et al 2016][research_adegbindin_love_2016]
- [Adhikari et al 2022][research_adhikari_loubimov_2022]
- [Adoghe][research_adoghe]
- [Advanced Aerodynamics. Selected NASA 1981][research_advanced_aerodynamics_1981]
- [Advanced Aircraft Control 2026][research_advanced_aircraft_2026]
- [Aerodynamic characteristics of telescopic 2018][research_aerodynamic_characteristics_of_2018]
- [Aerodynamic Design Wing 1969][research_aerodynamic_design_1969]
- [Aerodynamic Performance of Lambda 2024][research_aerodynamic_performance_2024]
- [Aerodynamics of Wing-Body Combinations 2010][research_aerodynamics_of_2010]
- [Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]
- [Afanasyev et al 2025][research_afanasyev_yermolaev_2025]
- [Agenbag et al 2009][research_agenbag_theron_2009]
- [Agrawal et al 1991][research_agrawal_kinard_1991]
- [Aguirrebeitia et al 2012][research_aguirrebeitia_aviles_2012]
- [Ahmad et al 2018][research_ahmad_baig_2018]
- [Ahmad et al 2018][research_mahmad_emnasir_2018]
- [Ahmad et al 2024][research_ahmad_gour_2024]
- [Ahmed and Jave 1995][research_ahmed_jave_1995]
- [Ahmed et al 1989][research_ahmed_wentz_1989]
- [Ahmer et al 2026][research_ahmer_2026]
- [Ai and Weaver 2017][research_ai_weaver_2017]
- [Aiken et al 1979][research_aiken_falarski_1979]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Aircraft Drag 2010][research_aircraft_drag_2010]
- [Aircraft Dynamic Stability 2003][research_aircraft_dynamic_2003]
- [Aircraft Dynamic Stability 2014][research_aircraft_dynamic_2014]
- [Aircraft Equations of Motion 2003][research_aircraft_equations_2003]
- [Aircraft Flight Control 2014][research_aircraft_flight_2014]
- [Aircraft flutter control system 2011][research_aircraft_flutter_2011]
- [Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]
- [Aircraft Load 2010][research_aircraft_load_2010]
- [Aircraft longitudinal handling qualities 2011][research_aircraft_longitudinal_2011]
- [Aircraft moments of inertia 1996][research_aircraft_moments_1996]
- [Aircraft Non-Linear Dynamics Equations 2014][research_aircraft_non_linear_2014]
- [Aircraft Stability and Control 2003][research_aircraft_stability_2003]
- [Aircraft Stability and Control 2014][research_aircraft_stability_2014]
- [Aircraft Stability and Control 2022][research_aircraft_stability_2022]
- [Aircraft Stability and Control 2026][research_aircraft_stability_2026]
- [Aircraft Static Stability 2003][research_aircraft_static_2003]
- [Aircraft Static Stability 2014][research_aircraft_static_2014]
- [Aircraft Static Stability 2024][research_aircraft_static_2024]
- [Aircraft Wing Design 2005][research_aircraft_wing_2005]
- [Airfoil and Wing Theory 2014][research_airfoil_and_2014]
- [Airfoil and Wing/Tail Geometry 2024][research_airfoil_and_2024]
- [Airplane Spin Testing 2003][research_airplane_spin_2003]
- [Airplane Trim 2012][research_airplane_trim_2012]
- [Airplane Trim 2022][research_airplane_trim_2022]
- [Airspeed vs Flight Path 2003][research_airspeed_vs_2003]
- [Ajaj and Jankee 2018][research_ajaj_jankee_2018]
- [Ajaj et al 2013][research_ajaj_saavedraflores_2013]
- [Ajaj et al 2016][research_ajaj_friswell_2016]
- [Ajanic et al 2020][research_ajanic_feroskhan_2020]
- [Akoury et al 2026][research_elakoury_aboukhalil_2026]
- [Al-Bayati 2026][research_albayati_2026]
- [Al-Khafaji et al 2023][research_alkhafaji_panatov_2023]
- [Al-Malki et al 2022][research_almalki_fildes_2022]
- [Alag 1987][research_alag_1987]
- [Alag and Burken 1987][research_alag_burken_1987]
- [Alag et al 1986][research_alag_burken_1986]
- [Alag et al 1986][research_alag_kempel_1986]
- [Alag et al 1986][research_alag_kempel_1986_b]
- [Alam et al 2022][research_alam_kara_2022]
- [Alasty et al 2004][research_alasty_alemohammad_2004]
- [Albers and Schröder 2020][research_albers_schroder_2020]
- [Alcorta et al 2023][research_alcorta_chouvion_2023]
- [Aleisa et al 2023][research_aleisa_kontis_2023]
- [Alford and Byrnes 1952][research_alford_byrnes_1952]
- [Alford and Henderson 1959][research_alford_1959_2]
- [Alford and Luoma 1960][research_alford_luoma_1960]
- [Alford and Polhamus 1962][research_alford_polhamus_1962]
- [Alford et al 1959][research_alford_1959]
- [Alford et al 1962][research_alford_1962]
- [Alford et al 1966][research_alford_1966]
- [Ali 2017][research_ali_2017]
- [Allen and Bridges 2003][research_allen_bridges_2003]
- [Allen et al 2005][research_allen_lizotte_2005]
- [Alley and Phillips 2010][research_alley_phillips_2010]
- [Alley et al 2007][research_alley_phillips_2007]
- [Allred and Fleck 1992][research_allred_fleck_1992]
- [Alpatskiy 2026][research_alpatskiy_2026]
- [Alsaidi et al 2019][research_alsaidi_joe_2019]
- [Alternative Methods for Modeling 1989][research_alternative_methods_1989]
- [Alulema et al 2020][research_alulema_valencia_2020]
- [Alulema et al 2025][research_alulema_2025]
- [Alvarez and Wissa 2021][research_alvarez_wissa_2021]
- [Alviani et al 2022][research_alviani_blaisdell_2022]
- [Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [Amano et al 2011][research_amano_avdeev_2011]
- [Ameduri et al 2025][research_ameduri_2025]
- [Ameho and Prempain 2011][research_ameho_prempain_2011]
- [Amendola et al 2018][research_amendola_dimino_2018]
- [Ameri et al 2007][research_ameri_lowenberg_2007]
- [Ameri et al 2008][research_ameri_lowenberg_2008]
- [An Aeroelastic Metamodel Based 2013][research_an_aeroelastic_2013]
- [An analysis of gap 1981][research_an_analysis_1981]
- [An et al 1986][research_an_yan_1986]
- [An et al 1988][research_an_yan_1988]
- [An experimental and computational 1978][research_an_experimental_1978]
- [An Introduction to the 1966][research_an_introduction_1966]
- [Ananthasayanam 2002][research_ananthasayanam_2002]
- [Ananthkrishnan 2004][research_ananthkrishnan_2004]
- [Ananthkrishnan and Sudhakar 1994][research_ananthkrishnan_sudhakar_1994]
- [Ananthkrishnan and Sudhakar 1995][research_ananthkrishnan_sudhakar_1995]
- [Andersen et al 2007][research_andersen_cowan_2007]
- [Anderson 1978][research_anderson_1978]
- [Anderson 1979][research_anderson_1979]
- [Anderson 1984][research_anderson_1984]
- [Anderson 1985][research_anderson_1985]
- [Anderson and Bray 1951][research_anderson_bray_1951]
- [Anderson and Bray 1955][research_anderson_1955]
- [Anderson and Meyer 1990][research_anderson_1990]
- [Anderson and Meyer 1990][research_anderson_1990_2]
- [Anderson et al 1983][research_anderson_enevoldson_1983]
- [Anderson et al 1988][research_anderson_1988]
- [Anderson et al 1991][research_anderson_meyer_1991]
- [Anderson et al 2012][research_anderson_robertrmeyer_2012]
- [Ando and Yamamoto 1976][research_ando_yamamoto_1976]
- [Andrews 1980][research_andrews_1980]
- [Andrews and Perez 2015][research_andrews_perez_2015]
- [Andrews et al 1980][research_andrews_sim_1980]
- [Anglin 1965][research_anglin_1965]
- [Anglin 1967][research_anglin_1967]
- [Anglin 1978][research_anglin_1978]
- [Ankenbruck 1946][research_ankenbruck_1946]
- [Another Vertical Wind Tunnel 1932][research_another_vertical_1932]
- [Antaran et al 1992][research_antaran_belete_1992]
- [Anto 2026][research_anto_2026]
- [Anwar 2025][research_anwar_2025]
- [Anyoji et al 2013][research_anyoji_liu_2013]
- [Aouf et al 2002][research_aouf_boulet_2002]
- [Aoyagi and Hickey 1959][research_aoyagi_hickey_1959]
- [Aoyagi et al 1965][research_aoyagi_cook_1965]
- [Apostolyuk 2007][research_apostolyuk_2007]
- [Appel et al 2021][research_appel_cooke_2021]
- [Appendix A Standard Atmosphere 2021][research_appendix_a_2021]
- [Appendix A. The Standard 2011][research_appendix_a_2011_b]
- [Appendix B Properties of 2003][research_appendix_b_2003]
- [Appendix C Flutter Analysis 2016][research_appendix_c_2016]
- [Appendix G Development of 2003][research_appendix_g_2003]
- [Appendix H Aerodynamics of 2010][research_appendix_h_2010]
- [Appendix H Stability Characteristics 2003][research_appendix_h_2003]
- [Application of Computational Methods 1982][research_application_of_1982]
- [Application of dynamic flight][research_application_of]
- [Application Status and Future 2023][research_application_status_2023]
- [Apuleo 2018][research_apuleo_2018]
- [Arabian et al 1961][research_arabian_runckel_1961]
- [Arai et al 2000][research_arai_noto_2000]
- [Araujo-Estrada et al 2015][research_araujoestrada_lowenberg_2015]
- [Araujo-Estrada et al 2016][research_araujoestrada_gong_2016]
- [Archambaud et al 2004][research_archambaud_louis_2004]
- [Arcidiacono et al 1970][research_arcidiacono_carta_1970]
- [Arena and Nelson 1989][research_arena_nelson_1989]
- [Arena et al 2018][research_arena_amoroso_2018]
- [Armstrong et al 2006][research_armstrong_lindberg_2006]
- [Arnal and Juillen 1990][research_arnal_juillen_1990]
- [Arnal et al 1990][research_arnal_casalis_1990]
- [Arnal et al 2000][research_arnal_seraudie_2000]
- [Arnold 1942][research_arnold_1942]
- [Arnott et al 1996][research_arnott_bernstein_1996]
- [Arnottt and Bernstein 2000][research_arnottt_bernstein_2000]
- [Arslan and Carlson 1994][research_arslan_carlson_1994]
- [Arun Kumar et al 2010][research_arunkumar_viswamurthy_2010]
- [Arunkumar et al 2023][research_arunkumar_sravanthi_2023]
- [Asaro and Vos 2026][research_asaro_vos_2026]
- [Ascani et al 1971][research_ascani_mellin_1971]
- [Ashenberg and Weihs 1984][research_ashenberg_weihs_1984]
- [Asher et al 1957][research_asher_martuccelli_1957]
- [Ashkenas 1964][research_ashkenas_1964]
- [Ashkenas 1964][research_ashkenas_1964_b]
- [Ashkenas 1984][research_ashkenas_1984]
- [Ashworth et al 1986][research_ashworth_waltrip_1986]
- [Ashworth et al 1988][research_ashworth_mouch_1988]
- [Assessment of variable camber 1980][research_assessment_of_1980]
- [Ataei-Esfahani and Qian Wang 2006][research_ataeiesfahani_qianwang_2006]
- [Atman and Bambang 2015][research_atman_bambang_2015]
- [Atmosphere, Aerodynamics, and Propulsion][research_atmosphere_aerodynamics]
- [Attar and Gordnier 2008][research_attar_gordnier_2008]
- [Aubeelack][research_aubeelack]
- [Aubeelack and Botez 2017][research_aubeelack_botez_2017]
- [August et al 2026][research_august_kopsaftopoulos_2026]
- [Aung Ko Wynn and Cao Yi Hua 2010][research_aungkowynn_caoyihua_2010]
- [Averett and Wright 1966][research_averett_1966]
- [Avkhadiev and Elizarov 2001][research_avkhadiev_elizarov_2001]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]
- [Axelson 1959][research_axelson_1959]
- [Ayers 1969][research_ayers_1969]
- [Ayers 1973][research_ayers_1973]
- [Azam and Sulaeman 2014][research_azam_sulaeman_2014]
- [B-34. U. S. Standard 1963 B-34. U. S. Standard Atmosphere, 1962][research_b_34_u_1963]
- [Baals and Polhamus 1963][research_baals_polhamus_1963]
- [Babister 1980][research_babister_1980]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]
- [Badihi et al 2026][research_badihi_2026]
- [Bae et al 2004][research_bae_seigler_2004]
- [Bae et al 2005][research_bae_seigler_2005]
- [Bagheri and Danesh 2025][research_bagheri_2025]
- [Bagley 1962][research_bagley_1962]
- [Bai et al 2020][research_bai_xing_2020]
- [Bai et al 2022][research_bai_ding_2022]
- [Bai et al 2024][research_bai_yang_2024]
- [Bai et al 2024][research_bai_yang_2024_b]
- [Bai et al 2025][research_bai_2025]
- [Bai et al 2025][research_bai_li_2025]
- [Bai et al 2026][research_bai_yang_2026]
- [Bajaj 2019][research_bajaj_2019]
- [Bajer et al 2025][research_bajer_hrstka_2025]
- [Baker 1953][research_baker_1953]
- [Balabanov and Haftka 1996][research_balabanov_haftka_1996]
- [Balachandran 2014][research_balachandran_2014]
- [Ballhaus and Bailey 1972][research_ballhaus_bailey_1972]
- [Ballin 1982][research_ballin_1982]
- [Ballouz and Chang][research_ballouz_chang]
- [Balon et al 2021][research_balon_benes_2021]
- [Bamber and House 1937][research_bamber_house_1937]
- [Banerjee and Taneja 2025][research_banerjee_taneja_2025]
- [Banner et al 1955][research_banner_1955]
- [Barahona et al 2024][research_barahona_weijer_2024]
- [Barbosa and Silvestre 2025][research_barbosa_2025]
- [Barbosa et al 2018][research_barbosa_bertolin_2018]
- [Bardin 2021][research_bardin_2021]
- [Barger and Wright 1966][research_barger_wright_1966]
- [Barmby et al 1951][research_barmby_cunningham_1951]
- [Barnard 1969][research_barnard_1969]
- [Barnes and Visbal 2019][research_barnes_visbal_2019]
- [Barnes and Visbal 2019][research_barnes_visbal_2019_b]
- [Barrows 2006][research_barrows_2006]
- [Bartels et al 2019][research_bartels_stanford_2019]
- [Barthelemy and Bergen 1988][research_barthelemy_bergen_1988]
- [Bartlett et al 1973][research_bartlett_1973]
- [Basaeri et al 2014][research_basaeri_yousefikoma_2014]
- [Bashir and Rajendran 2018][research_bashir_rajendran_2018]
- [Basic Equations for Unsteady 1989][research_basic_equations_1989]
- [Baskaran and Bradshaw 1988][research_baskaran_bradshaw_1988]
- [Batina et al 1988][research_batina_bennett_1988]
- [Batina et al 1988][research_batina_seidel_1988]
- [Batina et al 1989][research_batina_seidel_1989]
- [Battaglia and Riccio 2026][research_battaglia_riccio_2026]
- [Bauer et al 2016][research_bauer_grund_2016]
- [Baughman and Longeauay 2015][research_baughman_longeauay_2015]
- [Beatty et al 1977][research_beatty_brooks_1977]
- [Beaufrere 1988][research_beaufrere_1988]
- [Beaverstock et al 2015][research_beaverstock_woods_2015]
- [Becht 1950][research_becht_1950]
- [Becht and Few 1950][research_becht_few_1950]
- [Beeler et al 1956][research_beeler_1956]
- [Befus et al 1987][research_befus_nelson_1987]
- [Begnini et al 2018][research_begnini_bones_2018]
- [Beh et al 2018][research_beh_hofinger_2018]
- [Beissner et al 1984][research_beissner_1984]
- [Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]
- [Belisle et al 2010][research_belisle_neale_2010]
- [Belisle et al 2012][research_belisle_roberts_2012]
- [Bellman 1953][research_bellman_1953]
- [Bellman 1959][research_bellman_1959]
- [Belotserkovskii and Nisht 1974][research_belotserkovskii_nisht_1974]
- [Ben Asher and Raveh 2023][research_benasher_raveh_2023]
- [Ben-Gida and Gurka 2022][research_bengida_gurka_2022]
- [Ben-Gida et al 2019][research_bengida_gurka_2019]
- [Benaouali and Kachel 2017][research_benaouali_kachel_2017]
- [Bender et al 2010][research_bender_westphal_2010]
- [Bendiksen 2008][research_bendiksen_2008]
- [Benepe et al 1975][research_benepe_cunningham_1975]
- [Benepe et al 1978][research_benepe_cunningham_1978]
- [Benjamin et al 2021][research_benjamin_hesse_2021]
- [Bennett 1981][research_bennett_1981]
- [Bennett and Batina 1989][research_bennett_batina_1989]
- [Bennett and Lawson 2018][research_bennett_lawson_2018]
- [Bennett and Yates 1963][research_bennett_yates_1963]
- [Bennett et al 1988][research_bennett_batina_1988]
- [Bennett et al 2017][research_bennett_lawson_2017]
- [Beppu et al 1966][research_beppu_curtiss_1966]
- [Bera 1974][research_bera_1974]
- [Berci 2017][research_berci_2017]
- [Bergman 1979][research_bergman_1979]
- [Berman 1947][research_berman_1947]
- [Berman 1948][research_berman_1948]
- [Berman 1949][research_berman_1949]
- [Berman 1949][research_berman_1949_b]
- [Berman and Pumphrey 1950][research_berman_pumphrey_1950]
- [Bernstein and Hamid 1995][research_bernstein_hamid_1995]
- [Berrier 1980][research_berrier_1980]
- [Bertelrud 1979][research_bertelrud_1979]
- [Bertelrud 1980][research_bertelrud_1980]
- [Bertelrud 1981][research_bertelrud_1981]
- [Bertelrud 1981][research_bertelrud_1981_b]
- [Bertelrud and Graves 1994][research_bertelrud_graves_1994]
- [Bertelrud and Nordstrom 1983][research_bertelrud_nordstrom_1983]
- [Beyak et al][research_beyak_choudhari]
- [Beyak et al 2024][research_beyak_choudhari_2024]
- [Beyers and Brown 2006][research_beyers_brown_2006]
- [Beyers and Ericsson 2002][research_beyers_ericsson_2002]
- [Bhat 2018][research_bhat_2018]
- [Biber 2016][research_biber_2016]
- [Bidwell 1991][research_bidwell_1991]
- [Bidwell 2014][research_bidwell_2014]
- [Bidwell and Mohler 1995][research_bidwell_mohleryrjr_1995]
- [Bielat and Campbell 1953][research_bielat_campbell_1953]
- [Bielat and Pierpont 1960][research_bielat_1960]
- [Bielat and Wiley 1959][research_bielat_wiley_1959]
- [Bihrle 1969][research_bihrlejr_1969]
- [Bihrle 1976][research_bihrle_1976]
- [Bilgen et al 2007][research_bilgen_kochersberger_2007]
- [Bin Bai and Chaoyang Dong 2013][research_binbai_chaoyangdong_2013]
- [Bing and Wei 2024][research_bing_wei_2024]
- [Bippes 1990][research_bippes_1990]
- [Bippes et al 1997][research_bippes_lerche_1997]
- [Birchfield 1970][research_birchfield_1970]
- [Bird 1949][research_bird_1949]
- [Bird 1973][research_bird_1973]
- [Bird and Jaquet 1951][research_bird_1951]
- [Bird et al 1951][research_bird_1951_2]
- [Bird et al 1952][research_bird_1952]
- [Biriukov 1959][research_biriukov_1959]
- [Birk and Smith 1986][research_birk_smith_1986]
- [Bischoff 1983][research_bischoff_1983]
- [Bishay et al 2019][research_bishay_2019]
- [Black 1956][research_black_1956]
- [Black et al 1975][research_black_beamish_1975]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Blair et al 2008][research_blair_robinson_2008]
- [Blanchard 1981][research_blanchard_1981]
- [Bland 1980][research_bland_1980]
- [Blight et al 2018][research_blight_lanedailey_2018]
- [Blondeau and Pines 2004][research_blondeau_pines_2004]
- [Bloy 1996][research_bloy_1996]
- [Bobbitt and Foughner 1985][research_bobbitt_foughner_1985]
- [Boden et al 2013][research_boden_lanari_2013]
- [Bodonyl 1994][research_bodonyl_1994]
- [Boehm et al 2001][research_boehm_flick_2001]
- [Bohlmann 1989][research_bohlmann_1989]
- [Bohlmann et al 1988][research_bohlmann_weisshaar_1988]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bohon and Dixon 1964][research_bohon_dixon_1964]
- [Boiko 2002][research_boiko_2002]
- [Boiko et al 1995][research_boiko_kozlov_1995]
- [Boiko et al 2021][research_boiko_borodulin_2021]
- [Boiko et al 2024][research_boiko_kirilovskiy_2024]
- [Boiko et al 2024][research_boiko_kirilovskiy_2024_b]
- [Boisseau and Paulson 1956][research_boisseau_paulson_1956]
- [Bolding and Stearman 1976][research_bolding_stearman_1976]
- [Boling and Zha 2021][research_boling_zha_2021]
- [Bolonkin and Gilyard 1999][research_bolonkin_gilyard_1999]
- [Boltz and Pena 1977][research_boltz_pena_1977]
- [Boltz et al 1960][research_boltz_1960]
- [Bolzon et al 2016][research_bolzon_kelso_2016]
- [Bond et al 2010][research_bond_canfield_2010]
- [Bonnema and Lokos 1989][research_bonnema_lokos_1989]
- [Bonnema and Smith 1988][research_bonnema_smith_1988]
- [Boothe et al 2005][research_boothe_fitzpatrick_2005]
- [Boppe and Aidala 1980][research_boppe_aidala_1980]
- [Borden 2004][research_borden_2004]
- [Bore and Boyd 1963][research_bore_boyd_1963]
- [Borglund and Kroo 2002][research_borglund_kroo_2002]
- [Borodulin et al 2015][research_borodulin_ivanov_2015]
- [Borodulin et al 2016][research_borodulin_ivanov_2016]
- [Borodulin et al 2016][research_borodulin_ivanov_2016_b]
- [Borodulin et al 2017][research_borodulin_ivanov_2017]
- [Borodulin et al 2018][research_borodulin_ivanov_2018]
- [Borodulin et al 2019][research_borodulin_ivanov_2019]
- [Borodulin et al 2019][research_borodulin_ivanov_2019_b]
- [Borodulin et al 2020][research_borodulin_ivanov_2020]
- [Borodulin et al 2022][research_borodulin_ivanov_2022]
- [Borodulin et al 2023][research_borodulin_ivanov_2023]
- [Borodulin et al 2023][research_borodulin_ivanov_2023_b]
- [Borodulin et al 2024][research_borodulin_ivanov_2024]
- [Borodulin et al 2025][research_borodulin_kachanov_2025]
- [Borodulin et al 2026][research_borodulin_2026]
- [Borodulin et al 2026][research_borodulin_ivanov_2026]
- [Bosak et al 2026][research_bosak_eric_2026]
- [Boskovic and Redding 2009][research_boskovic_redding_2009]
- [Boston and Arrieta 2021][research_boston_arrieta_2021]
- [Boston et al 2022][research_boston_phillips_2022]
- [Boswinkle and Smith 1958][research_boswinkle_smith_1958]
- [Bosworth and Cox 1989][research_bosworth_cox_1989]
- [Botez et al 2011][research_botez_grigorie_2011]
- [Botez et al 2015][research_botez_kammegne_2015]
- [Bottai et al 2022][research_bottai_campbell_2022]
- [Botter][research_botter]
- [Bouadi][research_bouadi]
- [Boudreault 1983][research_boudreault_1983]
- [Boudreault 1983][research_boudreault_1983_b]
- [Boughou et al 2025][research_boughou_batistic_2025]
- [Bourdin 2001][research_bourdin_2001]
- [Bourdin 2002][research_bourdin_2002]
- [Bourdin et al 2006][research_bourdin_gatto_2006]
- [Bourdin et al 2007][research_bourdin_gatto_2007]
- [Bourgault-Cote and Laurendeau 2015][research_bourgaultcote_laurendeau_2015]
- [Bouton 1950][research_bouton_1950]
- [Bowers et al 2021][research_bowers_murillo_2021]
- [Bowman 1955][research_bowman_1955]
- [Bowman 1955][research_bowman_1955_b]
- [Bowman 1956][research_bowman_1956]
- [Bowman 1956][research_bowman_1956_b]
- [Bowman 1957][research_bowman_1957]
- [Bowman 1958][research_bowman_1958]
- [Bowman 1965][research_bowman_1965]
- [Bowman 1965][research_bowman_1965_b]
- [Bowman 1966][research_bowman_1966]
- [Bowman 1971][research_bowman_1971]
- [Bowman 2003][research_bowman_2003]
- [Bowman and Burk 1973][research_bowman_burk_1973]
- [Bowman and Burk 1974][research_bowman_burk_1974]
- [Bowman and Chambers 1970][research_bowman_chambers_1970]
- [Bowman and Healy 1958][research_bowman_healy_1958]
- [Bowman and Healy 1959][research_bowman_1959]
- [Bowman and Healy 1959][research_bowman_healy_1959]
- [Bowman and Healy 1960][research_bowman_1960]
- [Bowman and White 1974][research_bowman_1974]
- [Bowman et al 1978][research_bowmanjr_stough_1978]
- [Bowman et al 1987][research_bowman_whipple_1987]
- [Bowman et al 2002][research_bowman_sanders_2002]
- [Bowman et al 2007][research_bowman_sanders_2007]
- [Boyd 1977][research_boyd_1977]
- [Boyden 1978][research_boyden_1978]
- [Bradley et al 1976][research_bradley_honrath_1976]
- [Bradley et al 2026][research_bradley_haughn_2026]
- [Bradshaw 1980][research_bradshaw_1980]
- [Bradshaw and Pontikos 1985][research_bradshaw_pontikos_1985]
- [Brady et al 1954][research_brady_maier_1954]
- [Bragg and Soltani 1990][research_bragg_soltani_1990]
- [Bragg et al 1991][research_bragg_khodadoust_1991]
- [Braginsky 2020][research_braginsky_2020]
- [Bramantya and Nugroho 2025][research_bramantya_nugroho_2025]
- [Brandon et al 1995][research_brandon_brown_1995]
- [Brandt and Bons 2023][research_brandt_bons_2023]
- [Brandt and Bons 2024][research_brandt_bons_2024]
- [Brandt et al 2011][research_brandt_fossum_2011]
- [Brandt et al 2022][research_brandt_mcfadden_2022]
- [Brandt et al 2023][research_brandt_mcfadden_2023]
- [Braslow 1999][research_braslow_1999]
- [Bray 1953 The Effects of Fences on the High-speed Longitudinal Stability of a Swept-wing Airplane][research_bray_1953]
- [Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]
- [Brenner 2007][research_brenner_2007]
- [Breul 1963][research_breul_1963]
- [Brewer 1953][research_brewer_1953]
- [Brewer and Fisher 1951 Effect of Taper Ratio on the Low-speed Rolling Stability Derivatives of Swept and Unswept Wings of Aspect Ratio 2.61][research_brewer_1951]
- [Brewer and Lichtenstein 1950][research_brewer_lichtenstein_1950]
- [Bridges 1994][research_bridges_1994]
- [Bridges 2005][research_bridges_2005]
- [Bridges 2008][research_bridges_2008]
- [Briggs 1954][research_briggs_1954]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Brigido-Gonzalez and Rodriguez-Cortes 2014][research_brigidogonzalez_rodriguezcortes_2014]
- [Brinza 2024][research_brinza_2024]
- [Broeren et al 2013][research_broeren_potapczuk_2013]
- [Broeren et al 2017][research_broeren_woodard_2017]
- [Broeren et al 2018][research_broeren_lee_2018]
- [Broeren et al 2019][research_broeren_potapczuk_2019]
- [Broeren et al 2020][research_broeren_lee_2020]
- [Broering and Lian 2010][research_broering_lian_2010]
- [Browman and Healy 1959][research_browman_healy_1959]
- [Brown 1961][research_brown_1961]
- [Brown 1970][research_brownjr_1970]
- [Brown et al 1980][research_brownjr_price_1980]
- [Browne et al 2024][research_browne_maldonado_2024]
- [Brune and Bogataj 1990][research_brune_bogataj_1990]
- [Bryson 1954][research_bryson_1954]
- [Bryson 1954][research_bryson_1954_b]
- [Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]
- [Buchnik and Karpel 2014][research_buchnik_karpel_2014]
- [Buckingham 1914][research_buckingham_1914]
- [Budd 1984][research_budd_1984]
- [Buddhamatya et al 2026][research_buddhamatya_miranda_2026]
- [Buell and Kolbe 1957 The Effects at Subsonic Speeds of Wing Fences and a Tail on the Longitudinal Characteristics of a 63 Degree Swept-wing Fuselage Combination][research_buell_1957]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Bui 2013][research_bui_2013]
- [Bui 2015][research_bui_2015]
- [Bui 2016][research_bui_2016]
- [Bui 2018][research_bui_2018]
- [Bui 2018][research_bui_2018_b]
- [Bulekov and Teryev 1972][research_bulekov_teryev_1972]
- [Bullens and Traub 2021][research_bullens_traub_2021]
- [Bunge and Kroo 2012][research_bunge_kroo_2012]
- [Bunge et al 2015][research_bunge_munerasavino_2015]
- [Bunge et al 2016][research_bunge_alkurdi_2016]
- [Burchill et al 2002][research_burchill_mcdonald_2002]
- [Burdette and Martins][research_burdette_martins]
- [Burk 1971][research_burk_1971]
- [Burk 1972][research_burk_1972]
- [Burk 1974][research_burk_1974]
- [Burk and Healy 1955][research_burk_1955]
- [Burk and Libbey 1961][research_burk_1961]
- [Burk and Wilson 1975][research_burk_wilson_1975]
- [Burk et al 1977][research_burk_1977]
- [Burke and Gatto 2025][research_burke_gatto_2025]
- [Burke and Gatto 2026][research_burke_2026]
- [Burken et al 1986][research_burken_alag_1986]
- [Burkett 1989][research_burkett_1989]
- [Burkhalter 1993][research_burkhalter_1993]
- [Burkhalter et al 1992][research_burkhalter_spring_1992]
- [Burkhart 1980][research_burkhart_1980]
- [Burner and Martinson 1996][research_burner_martinson_1996]
- [Burner et al 2008][research_burner_goad_2008]
- [Burris and Hutchins 1970][research_burris_hutchins_1970]
- [Burton and Kneeland 1981][research_burton_kneelandjr_1981]
- [Busan 1998][research_busan_1998]
- [Bushnell 1990][research_bushnell_1990]
- [Buter and Rao 1984][research_buter_rao_1984]
- [Butler 1976][research_butler_1976]
- [Butler 1982][research_butler_1982]
- [Butler 1983][research_butler_1983]
- [Butler and Bons 2025][research_butler_bons_2025]
- [Buzica et al 2018][research_buzica_biswanger_2018]
- [Buzica et al 2018][research_buzica_debschutz_2018]
- [Böhnisch et al 2024][research_bohnisch_braun_2024]
- [Cai et al 2021][research_cai_xie_2021]
- [Cai et al 2022][research_cai_yang_2022]
- [Cai et al 2024][research_cai_su_2024]
- [Cai et al 2026][research_cai_zheng_2026]
- [Calico and Fuller 1981][research_calicojr_fuller_1981]
- [Camello et al 2016][research_camello_lee_2016]
- [Camello et al 2017][research_camello_bragg_2017]
- [Campbell and Goodman 1949 A semiempirical method for estimating the rolling moment due to yawing of airplanes][research_campbell_1949]
- [Campbell and Lynde 2016][research_campbell_lynde_2016]
- [Campbell and Smith 1987][research_campbell_smith_1987]
- [Campion 1954][research_campion_1954]
- [Cancro 1953][research_cancro_1953]
- [Candida et al 2019][research_candida_souzadepaula_2019]
- [Cangelosi 1963][research_cangelosi_1963]
- [Cao and Chen 2024][research_cao_chen_2024]
- [Cao and Lu 2024][research_cao_lu_2024]
- [Cao and Lyu 2024][research_cao_lyu_2024]
- [Cao et al 2025][research_cao_lin_2025]
- [Carafoli 1969][research_carafoli_1969_b]
- [Cardoso et al 2013][research_cardoso_suleman_2013]
- [Carlson and Weed 1985][research_carlson_weed_1985]
- [Carlson et al 1965][research_carlson_mabli_1965]
- [Carlsson 2005][research_carlsson_2005]
- [Carlsson and Kuttenkeuler 2003][research_carlsson_kuttenkeuler_2003]
- [Carnegie][research_carnegie]
- [Carpenter et al 2008][research_carpenter_saric_2008]
- [Carpenter et al 2010 Excitation of Crossflow Instabilities in a Swept Wing Boundary Layer][research_carpenter_2010]
- [Carpenter et al 2018][research_carpenter_solomon_2018]
- [Carrillo Córcoles et al 2023][research_carrillocorcoles_mertens_2023]
- [Carter 2016][research_carter_2016]
- [Carter 2017][research_carter_2017]
- [Carter et al 2009][research_carter_vicroy_2009]
- [Carter et al 2011][research_carter_brandt_2011]
- [Caruso et al 1988][research_caruso_mendenhall_1988]
- [Casacuberta et al 2022][research_casacuberta_groot_2022]
- [Casacuberta et al 2023][research_casacuberta_hickel_2023]
- [Casacuberta et al 2026][research_casacuberta_groot_2026]
- [Casey 1988][research_casey_1988]
- [Cassetti et al 1961][research_cassetti_re_1961]
- [Casteel and Weyl 1970][research_casteel_weyl_1970]
- [Castellani et al 2016][research_castellani_cooper_2016]
- [Castile and Herr 1949][research_castile_herr_1949]
- [Castillo Acero et al 2018][research_castilloacero_delaescalera_2018]
- [Castillo Zuñiga et al 2021][research_castillozuniga_giacobinisouza_2021]
- [Castrichini et al 2016][research_castrichini_hodigeresiddaramaiah_2016]
- [Catalano et al 2024][research_catalano_diodati_2024]
- [Cattafesta et al 1995][research_cattafesta_iyer_1995]
- [Cavalieri et al 2024][research_cavalieri_degaspari_2024]
- [Cebeci 1974][research_cebeci_1974]
- [Celi and Friedmann 1988][research_celi_friedmann_1988]
- [Cella and Biancolini 2012][research_cella_biancolini_2012]
- [Cen et al 2025][research_cen_xu_2025]
- [Cen et al 2026][research_cen_xu_2026]
- [Center 1966][research_naca_1966_2]
- [Cetinsoy 2015][research_cetinsoy_2015]
- [Chai et al 2018][research_chai_smart_2018]
- [Chakravarthy et al 2009][research_chakravarthy_grant_2009]
- [Chakravarthy et al 2012][research_chakravarthy_grant_2012]
- [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]
- [Chambers and Bowman 1971][research_chambers_bowman_1971]
- [Chambers and Stough 1986][research_chambers_stough_1986]
- [Chambers et al 1981 Curved-flow, rolling-flow, and oscillatory pure-yawing wind-tunnel test methods for determination of dynamic stability derivatives][research_chambers_1981]
- [Chana 2000][research_chana_2000]
- [Chang 2003][research_chang_2003]
- [Chang et al 2024][research_chang_chin_2024]
- [Changchuan et al 2022][research_changchuan_2022]
- [Chao and van Dam 2004][research_chao_vandam_2004]
- [Chaparro et al 2017][research_chaparro_fujiwara_2017]
- [Chapman 1961][research_chapman_1961]
- [Chapter 12. Control of 1994][research_chapter_12_1994]
- [Chapter 2. Aerodynamics of 1960][research_chapter_2_1960]
- [Chapter 3. Aerodynamics of 1960][research_chapter_3_1960]
- [Chapter 3. Dynamics of 2005][research_chapter_3_2005]
- [CHAPTER NINE. The Minimum 1990][research_chapter_nine_1990]
- [CHAPTER SEVEN. Wings of 1990][research_chapter_seven_1990]
- [CHAPTER SIX. Effects of 1990][research_chapter_six_1990]
- [CHAPTER TEN. Drag of 1990][research_chapter_ten_1990]
- [Characteristic Parameters for Airfoil 2021][research_characteristic_parameters_2021]
- [Characteristic Parameters for Airfoil 2025][research_characteristic_parameters_2025]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Che and Wu 2026][research_che_wu_2026]
- [Cheatham and Kurbjun 1948][research_cheatham_1948]
- [Chellangi et al 2025][research_chellangi_santhanam_2025]
- [Chen 2010][research_chen_2010]
- [Chen 2018][research_chen_2018]
- [Chen 2023][research_chen_2023]
- [Chen 2024][research_chen_2024]
- [Chen 2026][research_chen_2026_b]
- [Chen 2026][research_chen_2026_c]
- [Chen and Barlow 1995][research_chen_barlow_1995]
- [Chen et al 1984][research_chen_vassberg_1984]
- [Chen et al 1998][research_chen_chang_1998]
- [Chen et al 2001][research_chen_khalid_2001]
- [Chen et al 2002][research_chen_sulaeman_2002]
- [Chen et al 2015][research_chen_yue_2015]
- [Chen et al 2015][research_chen_zhang_2015]
- [Chen et al 2016][research_chen_guo_2016]
- [Chen et al 2021][research_chen_dong_2021]
- [Chen et al 2024][research_chen_zhang_2024]
- [Chen et al 2025][research_chen_meng_2025]
- [Chen et al 2026][research_chen_2026]
- [Chen et al 2026][research_chen_gray_2026]
- [Chen et al 2026][research_chen_xiao_2026]
- [Cheng 1978][research_cheng_1978]
- [Cheng 1982][research_cheng_1982]
- [Cheng and Meng 1979][research_cheng_meng_1979]
- [Cheng et al 1980][research_cheng_meng_1980]
- [Cheng et al 2017][research_cheng_dong_2017]
- [Cheng et al 2017][research_cheng_dong_2017_b]
- [Cheng et al 2023][research_cheng_li_2023]
- [Cheng et al 2024][research_cheng_song_2024]
- [Cheng et al 2025][research_cheng_song_2025]
- [Cheng et al 2025][research_cheng_zhang_2025]
- [Cheng et al 2026][research_cheng_yu_2026]
- [Chernoray et al 2005][research_chernoray_dovgal_2005]
- [Chernoray et al 2010][research_chernoray_dovgal_2010]
- [Chernoray et al 2013][research_chernoray_dovgal_2013]
- [Chernyshev et al 2015][research_chernyshev_kuryachii_2015]
- [Chester 2002][research_chester_2002]
- [Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]
- [Chetty and Raol 1992][research_chetty_raol_1992]
- [Cheung et al 2019][research_cheung_rezgui_2019]
- [Cheung et al 2020][research_cheung_folding_2020]
- [Cheung et al 2023][research_cheung_rezgui_2023]
- [Chiarelli and Bonomo 2019][research_chiarelli_2019]
- [Childs 1953][research_childs_1953]
- [Childs 1986][research_childs_1986]
- [Chinvorarat et al 2024][research_chinvorarat_watjatrakul_2024]
- [Chipman and Malone 1977][research_chipman_malone_1977]
- [Chipman et al 1982][research_chipman_zislin_1982]
- [Chipman et al 1984][research_chipman_rauch_1984]
- [Chipman et al 1985][research_chipman_rauch_1985]
- [Cho 2009][research_cho_2009]
- [Choi et al 2013][research_choi_park_2013]
- [Choi et al 2015][research_choi_jimenez_2015]
- [Choi et al 2016][research_choi_kang_2016]
- [Choi et al 2020][research_choi_lim_2020]
- [Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]
- [Choudhari 1996][research_choudhari_1996]
- [Choudhari et al 2016][research_choudhari_li_2016]
- [Chu et al 2022][research_chu_gu_2022]
- [Chung et al 2019][research_chung_cho_2019]
- [Chuprun 1980][research_chuprunjr_1980]
- [Cianciarulo et al 2024][research_cianciarulo_schmidt_2024]
- [Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]
- [Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]
- [Cinquegrana and Iuliano 2017][research_cinquegrana_iuliano_2017]
- [Citurs 1984][research_citurs_1984]
- [Clark 1964][research_clark_1964]
- [Clark and Hodapp 1972][research_clarkjr_hodappjr_1972]
- [Clark and LeTron 1989][research_clark_letron_1989]
- [Clark and Spurlin 1962][research_clark_spurlin_1962]
- [Clarke 1976][research_clarke_1976]
- [Clarke et al 2005][research_clarke_2005]
- [Clayton][research_clayton]
- [Clements and Djidjeli 2024][research_clements_djidjeli_2024]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Coban 2020][research_coban_2020]
- [Cobleigh 1994][research_cobleigh_1994]
- [Coe and Cunningham 1987][research_coe_cunningham_1987]
- [Coe and Kulla 1974][research_coe_kulla_1974]
- [Coe et al 1990][research_coe_perkins_1990]
- [Coetzee et al 2023][research_coetzee_lowenberg_2023]
- [Cole 1986][research_cole_1986]
- [Cole 1986][research_cole_1986_b]
- [Cole 1988][research_cole_1988]
- [Cole 1988][research_cole_1988_b]
- [Cole 1990][research_cole_1990]
- [Cole 1991][research_cole_1991]
- [Colella et al 2012][research_colella_bernadini_2012]
- [Collar 1946][research_collar_1946]
- [Collier et al 1990][research_collier_bartlett_1990]
- [Colorado et al 2015][research_colorado_rossi_2015]
- [Complete model of aircraft][research_complete_model]
- [Computational Methods for Unsteady 1989][research_computational_methods_1989]
- [Concepts and Computational Models 2021][research_concepts_and_2021]
- [Conner and Foster 1947][research_conner_foster_1947]
- [Control Allocation and Flight 2016][research_control_allocation_2016]
- [Cook 1968][research_cook_1968]
- [Cook 1979][research_cook_1979]
- [Cooke et al 2019][research_cooke_mughal_2019]
- [Cooper 2023][research_cooper_2023]
- [Cooper and Stroud 1972][research_cooper_stroud_1972]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1953][research_cornellaeronauticallabincbuffalony_1953]
- [Cornette 1961][research_cornette_1961]
- [Correia et al 2009][research_correia_silva_2009]
- [Cosenza and Vos 2017][research_cosenza_vos_2017]
- [Costello 2009][research_costello_2009]
- [Costigan and Calico 1989][research_costigan_calico_1989]
- [Couillaud][research_couillaud]
- [Courchesne et al 2010][research_courchesne_popov_2010]
- [Cousteix and Pailhas 1983][research_cousteix_pailhas_1983]
- [Coutu et al 2009][research_coutu_brailovski_2009]
- [Coutu et al 2011][research_coutu_brailovski_2011]
- [Covell et al 1987][research_covell_wood_1987]
- [Covert 1984][research_covert_1984]
- [Coward and Hall 1996][research_coward_hall_1996]
- [Craig 1976][research_craig_1976]
- [Creel 1991][research_creel_1991]
- [Creel et al 1987][research_creel_malik_1987]
- [Crittenden et al 1977][research_crittenden_weisshaar_1977]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Croom and Huffman 1957][research_croom_1957]
- [Croom and Huffman 1957][research_croom_huffman_1957]
- [Croom and Huffman 1957 Investigation at Transonic Speeds of Deflectors and Spoilers as Gust Alleviators on a 35 Degree Swept Wing Transonic Bump Method][research_croom_1957_2]
- [Crossley 2005][research_crossley_2005]
- [Crossley and Cook 2001][research_crossley_cook_2001]
- [Crossley et al 2011][research_crossley_skillen_2011]
- [Crouch et al 2018][research_crouch_garbaruk_2018]
- [Crowe 1937][research_crowe_1937]
- [Cui et al 2026][research_cui_2026]
- [Cuji and Garcia 2008][research_cuji_garcia_2008]
- [Culler and Farnsworth 2019][research_culler_farnsworth_2019]
- [Cummings and Sandlin 1987][research_cummings_sandlin_1987]
- [Cumpsty and Head 1967][research_cumpsty_head_1967]
- [Cumpsty and Head 1967][research_cumpsty_head_1967_b]
- [Cunis][research_cunis]
- [Cunningham 1951][research_cunningham_1951]
- [Cunningham and Coe 1990][research_cunningham_coe_1990]
- [Cunningham et al 1987][research_cunningham_batina_1987]
- [Cunningham et al 1988][research_cunningham_batina_1988]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Currao and Yeh 2026][research_currao_yeh_2026]
- [Curriston and White 2025][research_curriston_white_2025]
- [Curry and Sim 1982][research_curry_sim_1982]
- [Curry and Sim 1983][research_curry_sim_1983]
- [Curry and Sim 1984][research_curry_sim_1984]
- [Curtiss et al 1967][research_curtiss_hc_1967]
- [Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]
- [Cvetkovi et al 2012][research_cvetkovi_radakovi_2012]
- [D'Aguanno et al 2022][research_daguanno_campspons_2022]
- [D'Aguanno et al 2022][research_daguanno_schrijer_2022]
- [D'Ewart et al 1958][research_dewart_jr_1958]
- [Dagenhart 1992][research_dagenhart_1992]
- [Dagenhart and Saric 1999][research_dagenhart_saric_1999]
- [Dagenhart et al 1989][research_dagenhart_1989]
- [Dagenhart et al 1990][research_dagenhart_1990]
- [Dai et al 2020][research_dai_sweep_2020]
- [Dai et al 2020][research_dai_yan_2020]
- [Dai et al 2021][research_dai_mpc_2021]
- [Dal'Carobo and Fensterseifer 2010][research_dalcarobo_fensterseifer_2010]
- [Dam et al 2022][research_dam_planform_2022]
- [Damstrom and Mayes 1970][research_damstrom_mayes_1970]
- [Dandois 2016][research_dandois_2016]
- [Dandwani et al 2025][research_dandwani_bragadoaldana_2025]
- [Dannenberg 1950][research_dannenberg_1950]
- [Dansberry et al 1990][research_dansberry_rivera_1990]
- [Dantsker et al 2018][research_dantsker_vahora_2018]
- [Darida and Smrcek 1998][research_darida_smrcek_1998]
- [Das and Wichmann 2004][research_das_wichmann_2004]
- [Das et al 2021][research_das_venkatraman_2021]
- [David and Seifert 2012][research_david_seifert_2012]
- [Davies 2020][research_davies_2020]
- [Davies 2025][research_davies_2025]
- [Davis 1952][research_davis_1952]
- [Davis 1969][research_davis_1969]
- [Davis and Spedding 2015][research_davis_spedding_2015]
- [Dawson and Fortin 1987][research_dawson_fortin_1987]
- [Dağ et al 2026][research_dag_ozgur_2026]
- [De 2020][research_de_2020]
- [De Breuker et al 2007][research_debreuker_abdalla_2007]
- [De Gaspari and Ricci 2015][research_degaspari_ricci_2015]
- [De Gaspari et al 2018][research_degaspari_riccobene_2018]
- [de Jong and Mulder 1987][research_dejong_mulder_1987]
- [de Melo et al 2024][research_demelo_bussamra_2024]
- [de Rosa et al 2020][research_derosa_donelli_2020]
- [De Vincentiis et al 2021][research_devincentiis_henningson_2021]
- [De Voogt and Ganapathisubramani 2022][research_devoogt_ganapathisubramani_2022]
- [Deandrea et al 1991][research_deandrea_roache_1991]
- [Deangelis 1981][research_deangelis_1981]
- [DeAngelis 1982][research_deangelis_1982]
- [Decamp and Hardy 1984][research_decamp_hardy_1984]
- [Definition of the standard 1954][research_definition_of_1954]
- [Dehaan 1990][research_dehaan_1990]
- [DeJarnette and Jones 1978][research_dejarnette_jones_1978]
- [Del Frate 1992][research_delfrate_1992]
- [Delgado et al 2026][research_delgado_datta_2026]
- [Delgado Regis et al 2004][research_delgadoregis_mattos_2004]
- [Delplanche et al 2026][research_delplanche_greil_2026]
- [Demasi 2007][research_demasi_2007]
- [Demasi et al 2014][research_demasi_dipace_2014]
- [Demasi et al 2014][research_demasi_dipace_2014_b]
- [Demasi et al 2016][research_demasi_monegato_2016]
- [Denegri 2009][research_denegri_2009]
- [Denegri et al 2021][research_denegri_sharma_2021]
- [Deng et al 2013][research_deng_qin_2013]
- [Deng et al 2022][research_deng_wang_2022]
- [Denham and Owens 2016][research_denham_owens_2016]
- [Denison et al 2019][research_denison_garai_2019]
- [Design Objectives for Flying][research_design_objectives_b]
- [Design Objectives for Handling][research_design_objectives]
- [Design of the circulation 1979][research_design_of_1979]
- [Designing Airplane Wing Structures 2025][research_designing_airplane_2025]
- [Desmarais and Reed 1980][research_desmarais_reediii_1980]
- [Development of Longitudinal and 2014][research_development_of_2014]
- [Deyoung 1947][research_deyoung_1947]
- [Dicarlo and Johnson 1979][research_dicarlo_johnson_1979]
- [Dicarlo et al 1984][research_dicarlo_glover_1984]
- [Dicarlo et al 1992][research_dicarlo_brown_1992]
- [Dickey 1959][research_dickey_1959]
- [Diebold and Bragg 2015][research_diebold_bragg_2015]
- [Diebold et al 2012][research_diebold_monastero_2012]
- [Diebold et al 2013][research_diebold_broeren_2013]
- [Diederich and Budiansky 1948][research_diederich_budiansky_1948]
- [Diederich and Zlotnick 1949][research_diederich_zlotnick_1949]
- [Difranco 1969][research_difranco_1969]
- [Difranco 1970][research_difranco_1970]
- [Dikbas and Atik 2018][research_dikbas_atik_2018]
- [Dillinger et al 2019][research_dillinger_abdalla_2019]
- [Dimino et al 2014][research_dimino_flauto_2014]
- [Dimino et al 2015][research_dimino_ciminello_2015]
- [Dimino et al 2016][research_dimino_diodati_2016]
- [Dimino et al 2018][research_dimino_amendola_2018]
- [Dimino et al 2019][research_dimino_gallorini_2019]
- [Ding 2023][research_ding_2023]
- [DiPalma and Gandhi 2016][research_dipalma_gandhi_2016]
- [Directional Control 2003][research_directional_control_2003]
- [Distributed Surface-Vortex Receptivity of 2025][research_distributed_surface_vortex_receptivity_2025]
- [Distributed Surface-Vortex Receptivity of 2025][research_distributed_surface_vortex_receptivity_2025_b]
- [Dive Testing for Flutter 2003][research_dive_testing_2003]
- [Dizdarevic 2013][research_dizdarevic_2013]
- [Djahid et al 2022][research_djahid_elena_2022]
- [Djojodihardjo 2023][research_djojodihardjo_2023]
- [do Vale et al 2018][research_dovale_afonso_2018]
- [Dobbs et al 1985][research_dobbs_miller_1985]
- [Dodbele and Plotkin 1985][research_dodbele_plotkin_1985]
- [Doggett and Farmer 1976][research_doggett_farmer_1976]
- [Doggett and Ricketts 1977][research_doggettjr_ricketts_1977]
- [Doggett et al 1959][research_doggett_morgan_1959]
- [Dollyhigh 1970][research_dollyhigh_1970]
- [Donati et al 2026][research_donati_pacheco_2026]
- [Dong and Sun 2011][research_dong_sun_2011]
- [Dong et al 2013][research_dong_li_2013]
- [Dong et al 2018][research_dong_zhang_2018]
- [Dong et al 2022][research_dong_choi_2022]
- [Dongmo 2011][research_dongmo_2011]
- [Donlan and Sleeman 1976][research_donlan_sleeman_1976]
- [Dove-Jay 2014][research_dovejay_2014]
- [Dowell 1996][research_dowell_1996]
- [Dowell 1999][research_dowell_1999]
- [Dowell and Hall 2003][research_dowell_hall_2003]
- [Downs and Prazenica 2022][research_downs_prazenica_2022]
- [Downs and Prazenica 2023][research_downs_prazenica_2023]
- [Downs et al 1993 Aircraft wing structural detail design (wing, aileron, flaps, and subsystems)][research_downs_1993]
- [Drachinsky et al 2022][research_drachinsky_avin_2022]
- [Drag Reduction using Suction 2011][research_drag_reduction_2011]
- [Drake and Solomon 2010][research_drake_solomon_2010]
- [Drake and Williams 1958][research_williams_drake_1948]
- [Draper 1950][research_draper_1950]
- [Dryasov et al 2016][research_dryasov_yermolaev_2016]
- [Du et al 2026][research_du_2026]
- [Duan et al 2013][research_duan_choudhari_2013]
- [Duc et al 2004][research_duc_sesterhenn_2004]
- [Dugundji 1965][research_dugundji_1965]
- [Dugundji and Ghareeb 1965][research_dugundji_ghareeb_1965]
- [Dugundji et al 1962][research_dugundji_dowell_1962]
- [Dumont 2018][research_dumont_2018]
- [Duncan et al 2013][research_duncan_crawford_2013]
- [Durfee 1919][research_durfee_1919]
- [Durmuş and Kaya 2021][research_durmus_kaya_2021]
- [Durmuş and Kaya 2023][research_durmus_kaya_2023]
- [Durán Ferreras 2009][research_duranferreras_2009]
- [Dussart et al 2018][research_dussart_yusuf_2018]
- [Dussart et al 2019][research_dussart_roll_2019]
- [Dussart et al 2019][research_dussart_xb70_2019]
- [Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]
- [Dynamic Longitudinal Stability Flight 2003][research_dynamic_longitudinal_2003]
- [Dynamic Longitudinal Stability Theory 2003][research_dynamic_longitudinal_2003_b]
- [Dynamic Stability and Control][research_dynamic_stability]
- [Dynamics of Aircraft Motion 2015][research_dynamics_of_2015]
- [Dynamics of Very Flexible 2023][research_dynamics_of_2023]
- [Eckert and Maki 1973][research_eckert_1973]
- [Eckert and Maki 1973][research_eckert_maki_1973]
- [Economou 2025][research_economou_2025]
- [Edwards 1992][research_edwards_1992]
- [Edwards 1996][research_edwards_1996]
- [Edwards 1998][research_edwards_1998]
- [Effect of Sweep Angle 2019][research_effect_of_2019]
- [Efremov et al 1998][research_efremov_ogloblin_1998]
- [Ekaterinaris and Schiff 1994][research_ekaterinaris_schiff_1994]
- [El-Ramly and Rainbird 1977][research_elramly_rainbird_1977]
- [El-Salamony and Aziz 2020][research_elsalamony_aziz_2020]
- [Elelwi et al 2020][research_elelwi_span_2020]
- [Elelwi et al 2021][research_elelwi_calvet_2021]
- [Elelwi et al 2021][research_elelwi_topology_2021]
- [Elelwi et al 2022][research_elelwi_weight_2022]
- [Elements of Aerodynamic Wing 2013][research_elements_of_2013]
- [Elham and Timmer 2016][research_elham_timmer_2016]
- [Eliasson 2008][research_eliasson_2008]
- [Elkhoury and Nakad 2009][research_elkhoury_nakad_2009]
- [Ellis and Maris 1977][research_ellis_maris_1977]
- [Ellis et al 2025][research_ellis_2025]
- [ElRamly][research_elramly]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Elsloo et al 2025][research_elsloo_rooij_2025]
- [Enciu et al 2025][research_enciu_2025]
- [Eney 1968][research_eney_1968]
- [Engelbrecht][research_engelbrecht]
- [Engelbrecht et al 2012][research_engelbrecht_pauck_2012]
- [England 1975][research_england_1975]
- [Englar 1975][research_englar_1975]
- [English 1953][research_english_1953]
- [Enns 2015][research_enns_2015]
- [Enns et al 1988][research_enns_bugajski_1988]
- [Eppink][research_eppink]
- [Eppink 2017][research_eppink_2017]
- [Eppink 2023][research_eppink_2023]
- [Eppink and Wlezien 2012][research_eppink_wlezien_2012]
- [Eppink and Yao 2017][research_eppink_yao_2017]
- [Eppink and Yao 2017][research_eppink_yao_2017_b]
- [Eppink et al 2015][research_eppink_wlezien_2015]
- [Eppink et al 2019][research_eppink_wlezien_2019]
- [Equations, tables, and charts 1953][research_naca_1135]
- [Er-El 1988][research_erel_1988]
- [Eraslan and Oktay 2023][research_eraslan_oktay_2023]
- [Eraslan and Oktay 2024][research_eraslan_oktay_2024]
- [Erickson 1979][research_erickson_1979]
- [Erickson and Brandon 1987][research_erickson_brandon_1987]
- [Ericsson 1980][research_ericsson_1980]
- [Ericsson 1983][research_ericsson_1983]
- [Ericsson 1984][research_ericsson_1984]
- [Ericsson 1985][research_ericsson_1985]
- [Ericsson 1986][research_ericsson_1986]
- [Ericsson 1987][research_ericsson_1987]
- [Ericsson 1996][research_ericsson_1996]
- [Ericsson 1996][research_ericsson_1996_b]
- [Ericsson 1996][research_ericsson_1996_c]
- [Ericsson 1997][research_ericsson_1997]
- [Ericsson 1997][research_ericsson_1997_b]
- [Ericsson 1998][research_ericsson_1998]
- [Ericsson 1998][research_ericsson_1998_b]
- [Ericsson 2003][research_ericsson_2003]
- [Ericsson and Ericsson 1997][research_ericsson_ericsson_1997]
- [Ericsson and King 1990][research_ericsson_king_1990]
- [Ericsson and King 1993][research_ericsson_king_1993]
- [Ericsson and Reding 1976][research_ericsson_reding_1976]
- [Ericsson and Reding 1977][research_ericsson_reding_1977]
- [Ericsson and Reding 1978][research_ericsson_reding_1978]
- [Ermolaev et al 2018][research_ermolaev_kosinov_2018]
- [Erturk and Dogan 2017][research_erturk_dogan_2017]
- [Erzberger et al 1975][research_erzberger_1975]
- [Esquieu 2003][research_esquieu_2003]
- [Essenhigh 2006][research_essenhigh_2006]
- [Estevadeordal et al 2022][research_estevadeordal_ullah_2022]
- [Estimating the Takeoff Wing 2010][research_estimating_the_2010]
- [Estimating Wing-Body Aerodynamics 2010][research_estimating_wing_body_2010]
- [Estimation and Sensitivity in 2026][research_estimation_and_2026]
- [Evaluation of methods for 1981][research_evaluation_of_1981]
- [Evolution of modern air 1980][research_evolution_of_1980]
- [Experience Gained During Development 2010][research_experience_gained_2010]
- [Experimental and Numerical Unsteady 2024][research_experimental_and_2024]
- [Experimental Testing at Transonic 1982][research_experimental_testing_1982]
- [Exploratory study of the 1979][research_exploratory_study_1979]
- [F. Nonsteady Wing Characteristics 1957][research_f_nonsteady_1957]
- [Fagley et al 2016][research_fagley_seidel_2016]
- [Fala 2022][research_fala_2022]
- [Fan and Li 2019][research_fan_li_2019]
- [Fan et al 2017][research_fan_song_2017]
- [Fan et al 2021][research_fan_yu_2021]
- [Fan et al 2025][research_fan_wu_2025]
- [Farcy et al 2020][research_farcy_khrabrov_2020]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Farmer and Hanson 1976][research_farmer_hanson_1976]
- [Fasel 2020][research_fasel_2020]
- [Faure and Leogrande 2020][research_faure_2020]
- [Fedorov 1988][research_fedorov_1988]
- [Fedorov 2012][research_fedorov_2012]
- [Fedorov and Egorov 2021][research_fedorov_egorov_2021]
- [Fedorov and Novikov 2023][research_fedorov_novikov_2023]
- [Feedback Flight Control 2026][research_feedback_flight_2026]
- [Fehrs and Kaiser 2025][research_fehrs_2025]
- [Feistel et al 1978][research_feistel_anderson_1978]
- [Fejtek et al 2001][research_fejtek_jones_2001]
- [Felix et al 2026][research_felix_2026]
- [Felício et al 2011][research_felicio_santos_2011]
- [Feng and Wang 2020][research_feng_wang_2020]
- [Feng et al 2023][research_feng_guo_2023]
- [Feng et al 2025][research_feng_2025]
- [feng et al 2025][research_feng_wu_2025]
- [Fenwick and Allen 2007][research_fenwick_allen_2007]
- [Ferrero-Guillén et al 2022][research_ferreroguillen_diezgonzalez_2022]
- [Fichera et al 2019][research_fichera_isnardi_2019]
- [Fielding and Southworth 2001][research_fielding_southworth_2001]
- [Figat 2022][research_figat_2022]
- [Figat and Kwiek 2023][research_figat_kwiek_2023]
- [Figge and Bernhardt 1975][research_figge_bernhardt_1975]
- [Filippone 2006][research_filippone_2006]
- [Filippou et al 2024][research_filippou_kilimtzidis_2024]
- [Finch 1955][research_finch_1955]
- [Finch and Briggs 1953][research_finch_1953]
- [Finch and Walker 1953][research_finch_1953_2]
- [Finch and Walker 1956][research_finch_walker_1956]
- [Finistauri 2021][research_finistauri_2021]
- [Finistauri et al 2011][research_finistauri_xi_2011]
- [Finistauri et al 2012][research_finistauri_xi_2012]
- [Firouz-Abadi et al 2013][research_firouzabadi_askarian_2013]
- [Fischel and O'Hare 1950][research_fischel_ohare_1950]
- [Fischel and Schneiter 1948][research_fischel_schneiter_1948]
- [Fischel and Watson 1949][research_fischel_watson_1949]
- [Fischel et al 1952][research_fischel_naeseth_1952]
- [Fischer et al 1983][research_fischer_wrightjr_1983]
- [Fischer et al 1989][research_fischer_ehrenstein_1989]
- [Fisher 1951][research_fisher_1951]
- [Fisher 1958][research_fisher_1958_b]
- [Fisher and Williams 1958][research_fisher_1958]
- [Fixed, Rigid-Wing Aerodynamics 2007][research_fixed_rigid_wing_2007]
- [Flanagan et al 2007][research_flanagan_strutzenberg_2007]
- [Flat spin 2001][research_flat_spin_2001]
- [Flat Wings in Inviscid 2020][research_flat_wings_2020]
- [Fletcher et al 2022][research_fletcher_clarke_2022]
- [Flexible-Wing Aerodynamics 2007][research_flexible_wing_aerodynamics_2007]
- [Flight Control 2015][research_flight_control_2015]
- [Flight control system design 2011][research_flight_control_2011]
- [Flight control system for 1999][research_flight_control_1999]
- [Flight Dynamics of Elastic 2014][research_flight_dynamics_2014]
- [Flight Envelope Awareness/Protection][research_flight_envelope]
- [Flores and Van Dalsem 1985][research_flores_vandalsem_1985]
- [Floros and Kang 2017][research_floros_kang_2017]
- [Flying Qualities 2003][research_flying_qualities_2003]
- [Fonte et al 2018][research_fonte_iannaccone_2018]
- [Forster et al 1996][research_forster_kolonay_1996]
- [Forte and Nguyen 2024][research_forte_nguyen_2024]
- [Foster 1960][research_foster_1960_b]
- [Foster and Fitzpatrick 1948][research_foster_1948]
- [Foster and Morris 1960][research_foster_1960]
- [Foster and Morris 1960][research_foster_morris_1960]
- [Foster and Morris 1961][research_foster_morris_1961]
- [Foster and Spearman 1959][research_foster_spearman_1959]
- [Fouda and Taha 2022][research_fouda_taha_2022]
- [Foughner 1989][research_foughner_1989]
- [Fournier 1961][research_fournier_1961]
- [Fournier and Silvers 1958][research_fournier_silvers_1958]
- [Franciolini et al 2018][research_franciolini_daronch_2018]
- [Francois et al 2016][research_francois_cooper_2016]
- [Frazier 1991][research_frazier_1991]
- [Frederick et al 2014][research_frederick_banks_2014]
- [Freidmann 2001][research_freidmann_2001]
- [Fremaux 1997][research_fremaux_1997]
- [Fremaux et al 1990][research_fremaux_vijgen_1990]
- [Freudinger and Kehoe 1990][research_freudinger_1990]
- [Friederich and Kloker 2011][research_friederich_kloker_2011]
- [Friend and Sakamoto 1978][research_friend_1978]
- [Frink 2015][research_frink_2015]
- [Friswell 2014][research_friswell_2014]
- [Frolov 2021][research_frolov_2021]
- [From Steady Flight to 2011][research_from_steady_2011]
- [From Steady Flight to 2011][research_from_steady_2011_b]
- [From Tube and Wing 2013][research_from_tube_2013]
- [Frost and Rutherford 1963][research_frost_rutherford_1963]
- [Fu and Sun 2025][research_fu_sun_2025]
- [Fuchs 1930][research_fuchs_1930]
- [Fuchs and Schmidt 1931][research_fuchs_schmidt_1931]
- [Fugate et al 2019][research_fugate_nguyen_2019]
- [Fujii and Obayashi 1986][research_fujii_obayashi_1986]
- [Fujimori 2004][research_fujimori_2004]
- [Fujimori and Lin 1973][research_fujimori_lin_1973]
- [Fujimori and Nikiforuk 1999][research_fujimori_nikiforuk_1999]
- [Fujimori et al 1997][research_fujimori_wu_1997]
- [Fujimori et al 1998][research_fujimori_wu_1998]
- [Fujimori et al 2003][research_fujimori_terui_2003]
- [Fujimori et al 2005][research_fujimori_terui_2005]
- [Fujita et al 2014][research_fujita_motoda_2014]
- [Fujiwara et al 2018][research_fujiwara_nguyen_2018]
- [Fukumoto et al 2023][research_fukumoto_kouchi_2023]
- [Fuller 1967][research_fuller_1967]
- [Fundamentals of Airplane Flight 2007][research_fundamentals_of_2007]
- [Funk and Cooney 1959 Some Effects of Yaw Damping on Airplane Motions and Vertical-Tail Loads in Turbulent Air][research_funk_1959]
- [Furey 1980][research_furey_1980]
- [Furuya and Fukuchi 2001][research_furuya_fukuchi_2001]
- [Fusato and Celi 2006][research_fusato_celi_2006]
- [Gabor et al 2013][research_gabor_koreanschi_2013]
- [Gabor et al 2016][research_gabor_koreanschi_2016]
- [Gagnon and Zingg 2016][research_gagnon_zingg_2016]
- [Gain Scheduled Fuzzy Control 2004][research_gain_scheduled_2004]
- [Gainer et al 1967][research_gainer_1967]
- [Gainer et al 1984][research_gainer_1984]
- [Gale 1948][research_gale_1948]
- [Gale and Pumphrey 1950 Spin and recovery characteristics of a model of a fighter type of airplane without a horizontal tail having either a single vertical tail or twin][research_gale_1950]
- [Gallagher 1971][research_gallagher_1971]
- [Gallman et al 1990][research_gallman_smith_1990]
- [Galloway et al 1996][research_galloway_phillips_1996]
- [Gally and Carlson 1987][research_gally_carlson_1987]
- [Gamble and Inman 2016][research_gamble_inman_2016]
- [Gamboa and Santos 2016][research_gamboa_santos_2016]
- [Gandhi et al 2007][research_gandhi_jha_2007]
- [Gandhi et al 2009][research_gandhi_cooper_2009]
- [Ganesh et al 2022][research_ganesh_paul_2022]
- [Gang Tao et al][research_gangtao_shuhaochen]
- [Gano and Renaud 2002][research_gano_renaud_2002]
- [Gano et al 2004][research_gano_perez_2004]
- [Gao et al 2015][research_gao_zhao_2015]
- [Gao et al 2016][research_gao_kang_2016]
- [Gao et al 2018][research_gao_jin_2018]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2022][research_gao_tandem_2022]
- [Gao et al 2023][research_gao_pabon_2023]
- [Gao et al 2023][research_gao_zhu_2023]
- [Gao et al 2025][research_gao_2025]
- [Gao et al 2025][research_gao_tyrrell_2025]
- [Gao et al 2026][research_gao_tian_2026]
- [Gapcynski and Landrum 1958][research_gapcynski_landrum_1958]
- [Gaponenko et al 1995][research_gaponenko_ivanov_1995]
- [Gaponenko et al 2002][research_gaponenko_ivanov_2002]
- [Gaponov et al 2008][research_agaponov_gyermolaev_2008]
- [Garcia et al 2001][research_garcia_slingerland_2001]
- [Garcia et al 2003][research_garcia_abdulrahim_2003]
- [Gardner 1951][research_gardner_1951]
- [Gardner et al 2018][research_gardner_merz_2018]
- [Gardner et al 2019][research_gardner_merz_2019]
- [Garmann and Visbal 2020][research_garmann_visbal_2020]
- [Garmann and Visbal 2021][research_garmann_visbal_2021]
- [Garmann and Visbal 2022][research_garmann_visbal_2022]
- [Garmann and Visbal 2022][research_garmann_visbal_2022_b]
- [Garmann and Visbal 2023][research_garmann_visbal_2023]
- [Garre 2017][research_garre_2017]
- [Garrick and Reed 1981][research_garrick_reed_1981]
- [Gaster 2008][research_gaster_2008]
- [Gaylor 1984][research_gaylor_1984]
- [Gebhardt 2017][research_gebhardt_2017]
- [Gego and Bugaj 2023][research_gego_bugaj_2023]
- [Generally on automatic flight][research_generally_on]
- [Gera 1986][research_gera_1986]
- [Gera et al 1981][research_gera_wilson_1981]
- [German Development of the 2010 German Development of the Swept Wing 1935-1945][research_german_development_2010]
- [Gerontakos and Lee 2005][research_gerontakos_lee_2005]
- [Gerontakos and Lee 2006][research_gerontakos_lee_2006]
- [Gertsen and Shomber 1965][research_gertsen_shomber_1965]
- [Geva et al 2019][research_geva_2019]
- [Ghaemi et al 2019][research_ghaemi_lax_2019]
- [Ghanem et al 2023][research_ghanem_bicer_2023]
- [Ghasemi et al 2014][research_ghasemi_mosahebi_2014]
- [Ghoreyshi et al 2022][research_ghoreyshi_aref_2022]
- [Ghoreyshi et al 2022][research_ghoreyshi_nangia_2022]
- [Ghoreyshi et al 2024][research_ghoreyshi_aref_2024]
- [Ghoreyshi et al 2024][research_ghoreyshi_fagley_2024]
- [Ghoreyshi et al 2025][research_ghoreyshi_aref_2025]
- [Gibson 1990][research_gibson_1990]
- [Gibson and Ung 1995][research_gibson_ung_1995]
- [Gilani 2023][research_gilani_2023]
- [Gilbert 1980][research_gilbert_1980]
- [Gilbert 1981][research_gilbert_1981]
- [Gilbert and Silva 1987][research_gilbert_silva_1987]
- [Gilbert et al 1982][research_gilbert_schmidt_1982]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Giles 1970][research_giles_1970]
- [Giles 1972][research_giles_1972]
- [Giles 1986][research_giles_1986]
- [Giles 1995][research_giles_1995]
- [Gillis and Chapman 1956][research_gillis_1956]
- [Gillis and Mitchell 1957][research_gillis_1957]
- [Gilman and Burdges 1967][research_gilman_burdges_1967]
- [Gilyard 1972][research_gilyard_1972]
- [Gilyard 1989][research_gilyard_1989]
- [Gimmestad 1981][research_gimmestad_1981]
- [Giunta et al 1995][research_giunta_narducci_1995]
- [Glauert 1928][research_glauert_1928]
- [Glauser et al 2011][research_glauser_saric_2011]
- [Glauser et al 2014][research_glauser_saric_2014]
- [Go and Ramnath 2001][research_go_ramnath_2001]
- [Goetz and Doggett 1974][research_goetz_doggett_1974]
- [Goetz and Stonesifer 1961][research_goetz_1961]
- [Goizueta et al 2022][research_goizueta_wynn_2022]
- [Goland 1945][research_goland_1945]
- [Goland 1952][research_goland_1952]
- [Goland et al 1954][research_goland_luke_1954]
- [Goldschmied 1990][research_goldschmied_1990]
- [Golovkin et al 2019][research_golovkin_gorbunov_2019]
- [Gong and Ma 2019][research_gong_ma_2019]
- [Gong and Ma 2019][research_gong_ma_2019_b]
- [Gong et al 2019][research_gong_wang_2019]
- [Gong et al 2019][research_gong_wang_2019_b]
- [Gong et al 2020][research_gong_wang_2020]
- [Gonsalves and Zacharias 1994][research_gonsalves_zacharias_1994]
- [Goodheart et al 2003][research_goodheart_dykas_2003]
- [Goodman and Wolhart 1951][research_goodman_wolhart_1951]
- [Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]
- [Goodson 1966][research_goodson_1966]
- [Goorjian et al 1985][research_goorjian_guruswamy_1985]
- [Gopalarathnam and McAvoy 2001][research_gopalarathnam_mcavoy_2001]
- [Goradia et al 1989][research_goradia_bobbitt_1989]
- [Goraj et al 2002][research_goraj_baron_2002]
- [Gordnier 1991][research_gordnier_1991]
- [Gordnier 1995][research_gordnier_1995]
- [Gordnier and Visbal 1994][research_gordnier_visbal_1994]
- [Gordnier and Visbal 2003][research_gordnier_visbal_2003]
- [Gordnier and Visbal 2005][research_gordnier_visbal_2005]
- [Gordnier and Visbal 2006][research_gordnier_visbal_2006]
- [Gorev et al 2007][research_gorev_katasonov_2007]
- [Goto et al 2007][research_goto_obayashi_2007]
- [Govindarajan and Narasimha 2000][research_govindarajan_narasimha_2000]
- [Gowree and Atkin 2017][research_gowree_atkin_2017]
- [Grafton 1966][research_grafton_1966]
- [Grafton and Anglin 1972][research_grafton_anglin_1972]
- [Grafton and Grantham 1965][research_grafton_grantham_1965]
- [Grafton et al 1974][research_grafton_chambers_1974]
- [Grafton et al 1982][research_grafton_gilber_1982]
- [Graham 1951][research_graham_1951]
- [Graham et al 1972][research_graham_jones_1972]
- [Graham et al 1973][research_graham_1973]
- [Graham et al 1973][research_graham_1973_2]
- [Grant and Lind 2007][research_grant_lind_2007]
- [Grant and Lind 2010][research_grant_lind_2010]
- [Grant et al 2006][research_grant_abdulrahim_2006]
- [Grant et al 2009][research_grant_chakravarthy_2009]
- [Grant et al 2010][research_grant_abdulrahim_2010]
- [Grant et al 2012][research_grant_sorley_2012]
- [Grantham and Scher 1960][research_grantham_scher_1960]
- [Grantz 1985][research_grantz_1985]
- [Grauer and Hubbard 2012][research_grauer_hubbard_2012]
- [Graves 1975][research_graves_1975]
- [Gray 1964][research_grayjr_1964]
- [Greatwood et al 2017][research_greatwood_waldock_2017]
- [Green 1987][research_green_1987]
- [Green and Ott 2003][research_green_ott_2003]
- [Green and Ott 2005][research_green_ott_2005]
- [Green et al 1990][research_green_lee_1990]
- [Greenblatt and Washburn 2007][research_greenblatt_washburn_2007]
- [Greenman et al 1996][research_greenman_cheung_1996]
- [Greff 1990][research_greff_1990]
- [Gregory 1985][research_gregory_1985]
- [Gresham et al 2024][research_gresham_simmons_2024]
- [Griffin][research_griffin]
- [Griffin and Eastep 1981][research_griffin_eastep_1981]
- [Griffin and Eastep 1982][research_griffin_eastep_1982]
- [Griffin et al 1983][research_griffin_haerter_1983]
- [Grigorie and Botez 2014][research_grigorie_botez_2014]
- [Grigorie and Botez 2018][research_grigorie_botez_2018]
- [Grigorie and Botez 2023][research_grigorie_botez_2023]
- [Grigorie et al 2009][research_grigorie_botez_2009]
- [Grigorie et al 2011][research_grigorie_botez_2011]
- [Grigorie et al 2011][research_grigorie_popov_2011]
- [Grigorie et al 2011][research_grigorie_popov_2011_b]
- [Grigorie et al 2012][research_grigorie_botez_2012]
- [Grigorie et al 2012][research_grigorie_popov_2012]
- [Grismer and Nelson 1994][research_grismer_nelson_1994]
- [Grogorie et al 2013][research_grogorie_popov_2013]
- [Grose 1979][research_grose_1979]
- [Grosser 1965][research_grosser_1965]
- [Grosser 1982][research_grosser_1982]
- [Grossman et al 1986][research_grossman_gurdal_1986]
- [Groves-Raines et al 2026][research_grovesraines_watkins_2026]
- [Grow and Landrum 1967][research_grow_landrum_1967]
- [Gu and Hong 2020][research_gu_hong_2020]
- [Gu and Shou 2025][research_gu_shou_2025]
- [Gu et al 2022][research_gu_healy_2022]
- [Gu et al 2024][research_gu_healy_2024]
- [Guan et al 2026][research_guan_zhuang_2026]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Gudmundsson 2014][research_gudmundsson_2014]
- [Gudmundsson 2014][research_gudmundsson_2014_b]
- [Gudmundsson 2022][research_gudmundsson_2022]
- [Gudmundsson 2022][research_gudmundsson_2022_b]
- [Guerreiro et al 2006][research_guerreiro_hubbard_2006]
- [Guiler][research_guiler]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]
- [Gul and Datta 2021][research_gul_datta_2021]
- [Guler and Nikbay 2026][research_guler_nikbay_2026]
- [Gunasekaran and Mukherjee 2016][research_gunasekaran_mukherjee_2016]
- [Gunduz 2025][research_gunduz_2025]
- [Guo 2021][research_guo_2021]
- [Guo and Kloker 2026][research_guo_kloker_2026]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2016][research_guo_hou_2016]
- [Guo et al 2017][research_guo_bai_2017]
- [Guo et al 2017][research_guo_hou_2017]
- [Guo et al 2017][research_guo_hou_2017_b]
- [Guo et al 2020][research_guo_unsteady_2020]
- [Guo et al 2025][research_guo_wang_2025]
- [Gupta 1990][research_gupta_1990]
- [Gupta 2012][research_gupta_2012]
- [Gupta et al 2023][research_gupta_kumar_2023]
- [Gupta et al 2025][research_gupta_kim_2025]
- [Gurdal 2002][research_gurdal_2002]
- [Gurdal et al 1999][research_gurdal_haftka_1999]
- [Gurley and Ruhlin 1962][research_gurley_1962]
- [Guruswamy 2010][research_guruswamy_2010]
- [Guruswamy et al 1984][research_guruswamy_yang_1984]
- [Guruswamy et al 1985][research_guruswamy_goorjian_1985]
- [Guruswamy et al 1986][research_guruswamy_goorjian_1986]
- [Gwin 1974][research_gwin_1974]
- [Gwin 1976][research_gwin_1976]
- [Gürdamar et al 2006][research_gurdamar_cete_2006]
- [Haas and Chopra 1987][research_haas_chopra_1987]
- [Haas et al 2021][research_haas_hader_2021]
- [Haas et al 2022][research_haas_hader_2022]
- [Haftka 1977][research_haftka_1977]
- [Hahn and Drikakis 2008][research_hahn_drikakis_2008]
- [Hahn and Drikakis 2009][research_hahn_drikakis_2009]
- [Haider et al 2022][research_haider_mansor_2022]
- [Haider et al 2023][research_haider_ajaj_2023]
- [Haider et al 2023][research_haider_mansor_2023]
- [Haines 1957][research_haines_1957]
- [Hale 1976][research_hale_1976]
- [Hall 1971][research_hall_1971]
- [Hall and Woodson 2003][research_hall_woodson_2003]
- [Hall et al 1974][research_hall_weingarten_1974]
- [Hall et al 2005][research_hall_mohseni_2005]
- [Hallion 1984][research_hallion_1984]
- [Hallissy and Ayers 1977][research_hallissy_ayers_1977]
- [Hallissy and Harris 1974][research_hallissy_harris_1974]
- [Hallissy and Phillips 1989][research_hallissy_phillips_1989]
- [Ham 1981][research_ham_1981]
- [Hamer et al 1961][research_hamer_1961]
- [Hammer and Garmann 2023][research_hammer_garmann_2023_b]
- [Hammer et al 2021][research_hammer_garmann_2021]
- [Hammer et al 2023][research_hammer_garmann_2023]
- [Hammond 1963][research_hammond_1963]
- [Hammond and Henderson 1961][research_hammond_1961]
- [Hammond and Polhamus 1965][research_hammond_1965]
- [Hammond and Polhamus 1970][research_hammond_1970]
- [Han 2016][research_han_2016]
- [Han 2016][research_han_2016_b]
- [Han and Hong 2015][research_han_hong_2015]
- [Han et al 2007][research_han_lee_2007]
- [Han et al 2014][research_han_hu_2014]
- [Hancock 1960][research_hancock_1960]
- [Hancock 1971][research_hancock_1971]
- [Hancock 1972][research_hancock_1972]
- [Haney et al 1978][research_haney_waggoner_1978]
- [Haney et al 1980][research_haney_johnson_1980]
- [Hang et al 2026][research_hang_liu_2026]
- [Hanin and Barsony-Nagy 1983][research_hanin_barsonynagy_1983]
- [Hansen 2011][research_hansen_2011]
- [Hanson 1973][research_hanson_1973]
- [Hargraves 1961][research_hargraves_1961]
- [Harms et al 2020][research_harms_kaufmann_2020]
- [Harper and Cooper 1984][research_harperjr_cooper_1984]
- [Harris et al 2000][research_harris_gautrey_2000]
- [Harrison et al 2016][research_harrison_darragh_2016]
- [Hart 1956][research_hart_1956]
- [Hart 1968][research_hart_1968]
- [Hartshorn 2011][research_hartshorn_2011]
- [Harvey 1967][research_harvey_1967]
- [Harvey 2023][research_harvey_2023]
- [Harvey and Inman 2022][research_harvey_inman_2022]
- [Harvey et al 1990][research_harvey_harris_1990]
- [Harvey et al 2019][research_harvey_baliga_2019]
- [Harvey et al 2021][research_harvey_gull_2021]
- [Hattasanjaya 2024][research_hattasanjaya_2024]
- [Hauptman 1987][research_hauptman_1987]
- [Havenar and Ilie 2025][research_havenar_ilie_2025]
- [Hawley 1999][research_hawley_1999]
- [Hayes 1971][research_hayes_1971]
- [Hayes and Sleeman 1959][research_hayes_1959]
- [Haynes and Reed 1996][research_haynes_reed_1996]
- [Haynes and Reed 1997][research_haynes_reed_1997]
- [Haynes and Reed 2000][research_haynes_reed_2000]
- [Hayostek and Amitay 2018][research_hayostek_amitay_2018]
- [He and Guo 2012][research_he_guo_2012]
- [He et al 2015][research_he_yin_2015]
- [He et al 2015][research_he_zhang_2015]
- [He et al 2017][research_he_li_2017]
- [He et al 2021][research_he_guo_2021]
- [Heath and Ward 1959][research_heath_1959]
- [Hebbar and Leedy 1992][research_hebbar_leedy_1992]
- [Heeb and Woods 2024][research_heeb_woods_2024]
- [Helm et al 2021][research_helm_fehrs_2021]
- [Henderson 1960][research_henderson_1960]
- [Henderson 1974][research_henderson_1974]
- [Henderson and Huffman 1975][research_henderson_huffman_1975]
- [Henderson and Ray 1964][research_henderson_1964]
- [Henderson and Ray 1965][research_henderson_1965]
- [Henne 1981][research_henne_1981]
- [Henning 1953][research_henning_1953]
- [Henry and Pines 2007][research_henry_pines_2007]
- [Henry et al 2017][research_henry_molinari_2017]
- [Henry et al 2019][research_henry_molinari_2019]
- [Herdiana et al 2024][research_herdiana_pinindriya_2024]
- [Heredia and Ollero 2010][research_heredia_ollero_2010]
- [Herencia et al 2007][research_herencia_weaver_2007]
- [Hermanutz and Hornung 2020][research_hermanutz_2020]
- [Heron and Myose 2007][research_heron_myose_2007]
- [Herrmann 1929][research_herrmann_1929]
- [Herrmann et al 1966][research_herrmann_nematnasser_1966]
- [Herrmann et al 1967][research_herrmann_nematnasser_1967]
- [Hertz et al 1982][research_hertz_shirk_1982]
- [Hess 1981][research_hess_1981]
- [Hess 1984][research_hess_1984]
- [Hess 1987][research_hess_1987]
- [Hess 2012][research_hess_2012]
- [Hess and Hess 1997][research_hess_hess_1997]
- [Hess and Joyce 2013][research_hess_joyce_2013]
- [Hewes 1951][research_hewes_1951]
- [Hickey and Aoyagi 1960][research_hickey_aoyagi_1960]
- [Hicks and Henne 1977][research_hicks_henne_1977]
- [Hicks and Mendoza 1973][research_hicks_mendoza_1973]
- [Hicks and Moulton 1988][research_hicks_moulton_1988]
- [Hieser et al 1956][research_hieser_kudlacik_1956]
- [Higgins and Shomber 1964][research_higgins_shomber_1964]
- [Higgins and Shomber 1965][research_higgins_shomber_1965]
- [High-Speed Flight and Its 2010][research_high_speed_flight_2010]
- [Hilger and Ritter 2021][research_hilger_ritter_2021]
- [Hill 1987][research_hill_1987]
- [Hillenherms et al 2001][research_hillenherms_schroeder_2001]
- [Hiller 2002][research_hiller_2002]
- [Hilton 1955][research_hilton_1955]
- [Hintz et al 2014][research_hintz_torno_2014]
- [Hirschel et al 2020][research_hirschel_rizzi_2020]
- [Hirschel et al 2020][research_hirschel_rizzi_2020_b]
- [Historic Review of the 2010][research_historic_review_2010]
- [Hitch 1978][research_hitch_1978]
- [HlCKEY 1969][research_hlckey_1969]
- [Hoadley and McGraw 1995][research_hoadley_mcgraw_1995]
- [Hoang and Bui 2019][research_hoang_bui_2019]
- [Hoang and Bui 2019][research_hoang_bui_2019_b]
- [Hoang et al 1993][research_hoang_rediniotis_1993]
- [Hoang et al 2014][research_hoang_nguyen_2014]
- [Hodgkinson and Lamanna 1977][research_hodgkinson_lamanna_1977]
- [Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]
- [Hodson et al 2017][research_hodson_hunsaker_2017]
- [Hoehler 1949][research_hoehler_1949]
- [Hoerner 1936][research_hoerner_1936]
- [Hoerner 1952][research_hoerner_1952]
- [Hoff and Gratton 2013][research_hoff_gratton_2013]
- [Hoh and Mitchell 2018][research_hoh_mitchell_2018]
- [Holcomb 1979][research_holcomb_1979]
- [Holleman 1974][research_holleman_1974]
- [Holmes and Obara 1992][research_holmes_obara_1992]
- [Hong and Roberts 1995][research_hong_roberts_1995]
- [Hooker 2023][research_hooker_2023]
- [Hopkins 1951][research_hopkins_1951]
- [Hopkins 1964][research_hopkins_1964]
- [Hopkins 1975][research_hopkins_1975]
- [Hopkins 1977][research_hopkins_1977]
- [Hopkins and Levin 1974][research_hopkins_levin_1974]
- [Hopkins and Levin 1975][research_hopkins_levin_1975]
- [Hopkins and Lovette 1976][research_hopkins_lovette_1976]
- [Hopkins and Lovette 1976][research_hopkins_lovette_1976_b]
- [Hopkins and Lovette 1977][research_hopkins_lovette_1977]
- [Hopkins and Nelson 1976][research_hopkins_nelson_1976]
- [Hopkins and Yee 1977][research_hopkins_yee_1977]
- [Hopkins and Yee 1977][research_hopkins_yee_1977_b]
- [Hord][research_hord]
- [Horstmann 2008][research_horstmann_2008]
- [Hosangadi et al 2015][research_hosangadi_paul_2015]
- [Hosder et al 2008][research_hosder_walters_2008]
- [Hoshi et al 2020][research_hoshi_kuya_2020]
- [Hossain et al 2020][research_hossain_wang_2020]
- [Hosseini et al 2013][research_hosseini_tempelmann_2013]
- [Hou 2025][research_hou_2025]
- [Hou and Satyanarayana 2000][research_hou_satyanarayana_2000]
- [Hou et al 2024][research_hou_cao_2024]
- [Housner and Stein 1974][research_housner_1974]
- [Howe 2000][research_howe_2000]
- [Hu][research_hu]
- [Hu et al 2016][research_hu_yang_2016]
- [Hu et al 2023][research_hu_ge_2023]
- [Hu et al 2025][research_hu_2025]
- [Hu et al 2026][research_hu_2026]
- [Hu et al 2026][research_hu_traisnel_2026]
- [Hua et al 2025][research_hua_2025]
- [Hua Tian 2018][research_huatian_2018]
- [Huai et al 1997][research_huai_piomelli_1997]
- [Huang 1990][research_huang_1990]
- [Huang 2003][research_huang_2003]
- [Huang and Qiu 2013][research_huang_qiu_2013_b]
- [Huang and Wu 2006][research_huang_wu_2006]
- [Huang et al 2002][research_huang_lin_2002]
- [Huang et al 2013][research_huang_qiu_2013]
- [Huang et al 2017][research_huang_wu_2017]
- [Huang et al 2018][research_huang_yang_2018]
- [Huang et al 2020][research_huang_fu_2020]
- [Huang et al 2021][research_huang_fu_2021]
- [Huang et al 2021][research_huang_fu_2021_b]
- [Huang et al 2023][research_huang_guo_2023]
- [Huang et al 2023][research_huang_liu_2023]
- [Huang et al 2026][research_huang_2026]
- [Hubbard et al 2014][research_hubbard_fontenot_2014]
- [Huebsch et al 2012][research_huebsch_hamburg_2012]
- [Huehne et al 2013][research_huehne_mahmood_2013]
- [Huffman 1972][research_huffman_1972]
- [Huffman et al 1977][research_huffman_jr_1977]
- [Huffschmid 1950][research_huffschmid_1950]
- [Hui and Chen 2023][research_hui_chen_2023]
- [Hui et al 2019][research_hui_zhang_2019]
- [Hui et al 2020][research_hui_zhang_2020]
- [Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]
- [Human-Powered Aircraft Wing Design 2014][research_human_powered_aircraft_2014]
- [Hunsaker et al 2019][research_hunsaker_montgomery_2019]
- [Hunsaker et al 2019][research_hunsaker_moorthamers_2019]
- [Hunt and Gowadia 1981][research_hunt_gowadia_1981]
- [Hunt and Saric 2011][research_hunt_saric_2011]
- [Hurst et al 2008][research_hurst_wickenheiser_2008]
- [Hurst et al 2009][research_hurst_wickenheiser_2009]
- [Hussain and Bons 2019][research_hussain_bons_2019]
- [Hussain and Pei 2025][research_hussain_pei_2025]
- [Hutchin 2019][research_hutchin_2019]
- [Hutchison et al 1992][research_hutchison_huang_1992]
- [Hutchison et al 1992][research_hutchison_unger_1992]
- [Hutchison et al 1994][research_hutchison_unger_1994]
- [Hwang and Pi 1978][research_hwang_pi_1978]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwu and Tsai 2002][research_hwu_tsai_2002]
- [Hövelmann and Breitsamter 2015][research_hovelmann_breitsamter_2015]
- [I 1938][research_i_1938]
- [Iannelli et al 2019][research_iannelli_seiler_2019]
- [Iannuzzo et al 2018][research_iannuzzo_russo_2018]
- [Ichikawa 1996][research_ichikawa_1996]
- [Ichikawa et al 2021][research_ichikawa_koike_2021]
- [Ichikawa et al 2026][research_ichikawa_nakagawa_2026]
- [Igoe et al 1961][research_igoe_1961]
- [Ilie and Havenar 2022][research_ilie_havenar_2022]
- [Iliff 1977][research_iliff_1977]
- [Iliff 1980][research_iliff_1980]
- [Iliff and Taylor 1972][research_iliff_1972]
- [Imber and Rogers 1996][research_imber_rogers_1996]
- [Imbrie 1981][research_imbrie_1981]
- [Inayat et al 2018][research_inayat_amin_2018]
- [Inertia Coupling and Spin 2004][research_inertia_coupling_2004]
- [Inertia Coupling and Spin 2015][research_inertia_coupling_2015]
- [Inger 1994][research_inger_1994]
- [Inger 1995][research_inger_1995]
- [Inman et al 2024][research_inman_perry_2024]
- [Inoyama et al 2007][research_inoyama_sanders_2007]
- [Inoyama et al 2008][research_inoyama_sanders_2008]
- [International Standard Atmosphere 2010][research_international_standard_2010]
- [Introduction to Airplane Flight][research_introduction_to]
- [Introduction to Stability and 2003][research_introduction_to_2003]
- [Iosilevskii 2025][research_iosilevskii_2025]
- [Iosilevskii 2025][research_iosilevskii_2025_b]
- [Iosilevskii 2025][research_iosilevskii_2025_c]
- [Iqbal et al 2025][research_iqbal_alfaruk_2025]
- [Irani et al 2016][research_irani_amoozgar_2016]
- [Irving 1933][research_irving_1933]
- [Irving 1966][research_irving_1966]
- [Irving 1966][research_irving_1966_b]
- [Isah et al 2022][research_isah_lawal_2022]
- [Ishida and Ueshima 2026][research_ishida_ueshima_2026]
- [Ishmael and Wierzbanowski 1985][research_ishmael_wierzbanowski_1985]
- [Ishtiaq and Israr 2013][research_ishtiaq_israr_2013]
- [Islam et al 2025][research_islam_rahman_2025]
- [Isogai 2013][research_isogai_2013]
- [Ito and Takanashi 1991][research_ito_takanashi_1991]
- [Itoh and Kobayashi 1999][research_itoh_kobayashi_1999]
- [Itoh and Kobayashi 2000][research_itoh_kobayashi_2000]
- [Ivanco et al 2007][research_ivanco_scott_2007]
- [Ivanov et al 2018][research_ivanov_mischenko_2018]
- [Ivanov et al 2020][research_ivanov_mischenko_2020]
- [Iyer and Takahashi 2025][research_iyer_takahashi_2025]
- [Iyer et al 1992][research_iyer_spall_1992]
- [Jackuliak and Bugaj 2022][research_jackuliak_bugaj_2022]
- [Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]
- [Jacobs 1983][research_jacobs_1983]
- [Jacobsen 1953][research_jacobsen_1953]
- [Jacobson and Joshi 1977][research_jacobson_joshi_1977]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jahnke and Culick 1990][research_jahnke_culick_1990]
- [Jalil et al 2024][research_jalil_hashim_2024]
- [James and Maki 1957][research_james_1957]
- [Jameson][research_jameson]
- [Jameson 1977][research_jameson_1977]
- [Jameson and Caughey 1977][research_jameson_caughey_1977]
- [Jamwal et al 2018][research_jamwal_hosangadi_2018]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Janke et al 2001][research_janke_bertolotti_2001]
- [Jansen 1980][research_jansen_1980]
- [Jaquet 1952][research_jaquet_1952]
- [Jaramillo et al 1995][research_jaramillo_cho_1995]
- [Jasa et al 2018][research_jasa_hwang_2018]
- [Jeger et al 2024][research_jeger_wuest_2024]
- [Jenkins 1986][research_jenkins_1986]
- [Jenkins and Kuhl 1977][research_jenkins_1977_2]
- [Jenkins et al 1977][research_jenkins_1977]
- [Jenks et al 1977][research_jenks_henry_1977]
- [Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]
- [Jeong and Bae 2022][research_jeong_bae_2022]
- [Jernell and McKinney 1965][research_jernell_mckinney_1965]
- [Ji et al 2024][research_ji_huang_2024]
- [Jian and Ke-Qin 2004][research_jian_keqin_2004]
- [Jiang and Yang 2026][research_jiang_yang_2026]
- [Jiang et al 2014][research_jiang_xu_2014]
- [Jiang et al 2015][research_jiang_dong_2015]
- [Jiang et al 2020][research_jiang_wu_2020]
- [Jianliang Wang and Weiqiang Zhang][research_jianliangwang_weiqiangzhang]
- [Jie 2018][research_jie_2018]
- [Jim et al 2021][research_jim_planform_2021]
- [Jin 2024][research_jin_2024]
- [Jin et al 2011][research_jin_song_2011]
- [Jin Song et al 2012][research_jinsong_junma_2012]
- [Jing and Huang 2017][research_jing_huang_2017]
- [Jingeleski et al 2013][research_jingeleski_schetz_2013]
- [Jisheng and Heng 1998][research_jisheng_heng_1998]
- [Jo and Majid 2023][research_jo_majid_2023]
- [Jo et al 2016][research_jo_choi_2016]
- [Johns 1960][research_johns_1960]
- [Johnson 1953][research_johnson_1953]
- [Johnson 1953][research_johnson_1953_b]
- [Johnson 1959][research_johnson_1959]
- [Johnson and Hageman 1950][research_johnson_hageman_1950]
- [Johnson and Hagerman 1951][research_johnson_hagerman_1951]
- [Johnson and Lind 2009][research_johnson_lind_2009]
- [Johnson and Lind 2010][research_johnson_lind_2010]
- [Johnson and Willen 1976][research_johnson_willen_1976]
- [Johnson et al 1980][research_johnson_grafton_1980]
- [Johnston 1998][research_johnston_1998]
- [Jones 1947][research_jones_1947]
- [Jones 1948][research_jones_1948]
- [Jones 1976][research_jones_1976_b]
- [Jones 1976][research_jones_1976_c]
- [Jones 1976][research_jones_1976_d]
- [Jones 1976][research_jones_1976_e]
- [Jones 1977][research_jones_1977]
- [Jones 1980][research_jones_1980]
- [Jones and Alksne 1951][research_jones_alksne_1951]
- [Jones and Cohen 2011][research_jones_cohen_2011]
- [Jones and Klinar 1950][research_jones_klinar_1950]
- [Jones and Nakamura 2007][research_jones_nakamura_2007]
- [Jones and Nisbet 1974][research_jones_nisbet_1974]
- [Jones and Nisbet 1976][research_jones_1976]
- [Jones and Nisbet 1976][research_jones_1976_2]
- [Jones and Unangst 1963][research_jones_unangst_1963]
- [Joo et al 2006][research_joo_sanders_2006]
- [Jordan 1971][research_jordan_1971]
- [Joseph et al 2020][research_joseph_golubev_2020]
- [Joseph et al 2021][research_joseph_adamski_2021]
- [Joshi et al 2004][research_joshi_tidwell_2004]
- [Joshi et al 2020][research_joshi_vazquez_2020]
- [Joshi et al 2026][research_joshi_2026]
- [Joshua and Adams 2006][research_joshua_adams_2006]
- [Joslin 1995][research_joslin_1995]
- [Joslin and Streett 1992][research_joslin_streett_1992]
- [Jouannet et al 2009][research_jouannet_lundstrom_2009]
- [Juillen and Arnal 1995][research_juillen_arnal_1995]
- [Jung and Kim 2013][research_jung_kim_2013]
- [Jung and Kim 2022][research_jung_kim_2022]
- [Jung and Reimerdes 2003][research_jung_reimerdes_2003]
- [Kabir et al 2023][research_kabir_alobaidi_2023]
- [Kachanov 1996][research_kachanov_1996]
- [Kachanov and Tararykin 1990][research_kachanov_tararykin_1990]
- [Kachanov et al 2016][research_kachanov_borodulin_2016]
- [Kalaji 2023][research_kalaji_2023]
- [Kalemaris 1980][research_kalemaris_1980]
- [Kamal et al 2015][research_kamal_aly_2015]
- [Kambayashi and Kogiso 2025][research_kambayashi_2025]
- [Kameda et al 2008][research_kameda_seki_2008]
- [Kamiya et al 1978][research_kamiya_nishi_1978]
- [Kammegne and Botez 2019][research_kammegne_botez_2019]
- [Kammegne et al 2016][research_kammegne_botez_2016]
- [Kanamori et al 2009][research_kanamori_imamura_2009]
- [Kanazaki et al 2008][research_kanazaki_imamura_2008]
- [Kandil et al 1993][research_kandil_kandil_1993]
- [Kandil et al 1993][research_kandil_kandil_1993_b]
- [Kandil et al 1994][research_kandil_kalisch_1994]
- [Kang et al 2026][research_kang_2026]
- [Kang et al 2026][research_kang_2026_2]
- [Kang et al 2026][research_kang_lu_2026]
- [Kannemans 1995][research_kannemans_1995]
- [Kapania et al 1991][research_kapania_eldred_1991]
- [Kapuscinski et al 2020][research_kapuscinski_2020]
- [Karahan 2026][research_karahan_2026]
- [Kargarnovin and Sayrarfie 1995][research_kargarnovin_sayrarfie_1995]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karow 2026][research_karow_2026]
- [Karpel et al 2008][research_karpel_selitrennik_2008]
- [Karpouzian and Librescu 1993][research_karpouzian_librescu_1993]
- [Karthik et al 1999][research_karthik_tulapurkara_1999]
- [Kass 1970][research_kass_1970]
- [Kasuga et al 2017][research_kasuga_yoshida_2017]
- [Katz 1989][research_katz_1989]
- [Katz and Feistel 1987][research_katz_feistel_1987]
- [Kaul 2024][research_kaul_2024]
- [Kaul and Nguyen 2017][research_kaul_nguyen_2017]
- [Kaushik 2018][research_kaushik_2018]
- [Kaushik 2018][research_kaushik_2018_b]
- [Kawazoe and Kato 2005][research_kawazoe_kato_2005]
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kayran 2004][research_kayran_2004]
- [Kazhan et al 2019][research_kazhan_kazhan_2019]
- [Kearns 1962][research_kearns_1962]
- [Keener 1984][research_keener_1984]
- [Kegelman and Roos 1989][research_kegelman_roos_1989]
- [Kehoe 1987][research_kehoe_1987]
- [Keidel et al 2019][research_keidel_fasel_2019]
- [Keidel et al 2020][research_keidel_2020]
- [Keith and Selberg 1984][research_keith_selberg_1984]
- [Keller 2019][research_keller_2019]
- [Keller et al 1991][research_keller_sandford_1991]
- [Kelley et al 1978][research_kelley_shinar_1978]
- [Kelley et al 1979][research_kelley_shinar_1979]
- [Kemp and Becht 1950][research_kemp_1950]
- [Kemp and Few 1951][research_kemp_1951]
- [Kempel et al 1988][research_kempel_mcneill_1988]
- [Kempel et al 1988][research_kempel_mcneill_1988_b]
- [Kempel et al 1989][research_kempel_phillips_1989]
- [Kempel et al 1992][research_kempel_pahle_1992]
- [Kendall 1984][research_kendall_1984]
- [Kendall 1985][research_kendall_1985]
- [Kennedy 1951][research_kennedy_1951]
- [Kennelly et al 1990][research_kennelly_1990]
- [Kennelly et al 1992][research_kennelly_strong_1992]
- [Kennelly et al 1999][research_kennelly_1999]
- [Kentfield 2006][research_kentfield_2006]
- [Kentfield and Spragins 2004][research_kentfield_spragins_2004]
- [Kerr 1954][research_kerr_1954]
- [Khan 2008][research_khan_2008]
- [Khan and Deng 2012][research_khan_deng_2012]
- [Khan et al 2019][research_khan_grigorie_2019]
- [Khazaee Kuhpar and Seyed-Aghazadeh 2026][research_khazaeekuhpar_seyedaghazadeh_2026]
- [Khodadoust and Bragg 1990][research_khodadoust_bragg_1990]
- [Kida 1982][research_kida_1982]
- [Kilgore 1971][research_kilgore_1971]
- [Kilgore 1971][research_kilgore_1971_b]
- [Kilgore and Adcock 1972][research_kilgore_adcock_1972]
- [Kim and Lee 2001][research_kim_lee_2001]
- [Kim and Marciniak 2002][research_kim_marciniak_2002]
- [Kim and Sung 1993][research_kim_sung_1993]
- [Kim et al 2013][research_kim_lee_2013]
- [Kim et al 2017][research_kim_oh_2017]
- [Kim et al 2020][research_kim_lee_2020]
- [Kim et al 2024][research_kim_kang_2024]
- [Kimberlin 2003][research_kimberlin_2003]
- [Kimler and Canfield 2006][research_kimler_canfield_2006]
- [Kirilovskiy et al 2019][research_kirilovskiy_boiko_2019]
- [Kirkman and Takahashi 2017][research_kirkman_takahashi_2017]
- [Kirmse 2016][research_kirmse_2016]
- [Kishi et al 2017][research_kishi_kitazaki_2017]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kjelgaard et al 1986][research_kjelgaard_sellersiii_1986]
- [Klausmeyer and Laflin 2023][research_klausmeyer_laflin_2023]
- [Klein and Batterson 1983][research_klein_batterson_1983]
- [Klein and Viswanathan 1973][research_klein_viswanathan_1973]
- [Klein et al 1981][research_klein_batterson_1981]
- [Klepl 1992][research_klepl_1992]
- [Klimczyk and Goraj 2019][research_klimczyk_2019]
- [Klinar and Healy 1952][research_klinar_healy_1952]
- [Klinar and Jones 1948][research_klinar_jones_1948]
- [Klinar and Jones 1949][research_klinar_1949]
- [Klinar and Lee 1954][research_klinar_lee_1954]
- [Klinar and Lee 1955][research_klinar_lee_1955]
- [Klinar and Snyder 1948][research_klinar_snyder_1948]
- [Klinar and Wilson 1950][research_klinar_1950]
- [Kloker 2008][research_kloker_2008]
- [Klopfenstein 1965][research_klopfenstein_1965]
- [Klug et al 2023][research_klug_ullah_2023]
- [Klyde et al 2004][research_klyde_harris_2004]
- [Knight 1928][research_knight_1928]
- [Knight and Wenzinger 1930][research_knight_wenzinger_1930]
- [Knight et al 2011][research_knight_braun_2011]
- [Ko et al 2003][research_ko_mason_2003]
- [Kodigaddi 2026][research_kodigaddi_2026]
- [Kogiso et al 2000][research_kogiso_tsushima_2000]
- [Kohama 1987][research_kohama_1987]
- [Kohama 1987][research_kohama_1987_b]
- [Kohama and Suda 1993][research_kohama_suda_1993]
- [Kohama et al 1991][research_kohama_1991]
- [Kohama et al 1995][research_kohama_kodashima_1995]
- [Kolar and Lile 1971][research_kolar_lile_1971]
- [Kolbakir 2016][research_kolbakir_2016]
- [Kolesar 1971][research_kolesar_1971]
- [Kolnick and Kennedy 1952][research_kolnick_kennedy_1952]
- [Kolonay et al 2004][research_kolonay_eastep_2004]
- [Kolosov and Kosinov 2016][research_kolosov_kosinov_2016]
- [Kolosov et al 2017][research_kolosov_kosinov_2017]
- [Koltko et al 1975][research_koltko_katz_1975]
- [Komp et al 2024][research_komp_hajek_2024]
- [Kong 1994][research_kong_1994]
- [Konrath et al 2006][research_konrath_schroder_2006]
- [Koo 2001][research_koo_2001]
- [Koohi et al 2014][research_koohi_shahverdi_2014]
- [Kornev and Pimenov 2022][research_kornev_pimenov_2022]
- [Kornev et al 2021][research_kornev_ambrozhevich_2021]
- [Kosarev et al 2016][research_kosarev_seror_2016]
- [Kosinov et al 2016][research_kosinov_kolosov_2016]
- [Kosmatka and Panza 2003][research_kosmatka_panza_2003]
- [Kotsabasis 1981][research_kotsabasis_1981]
- [Kozlov et al 2006][research_kozlov_chernoray_2006]
- [Kozlov et al 2009][research_kozlov_zverkov_2009]
- [Kozlov et al 2014][research_kozlov_grek_2014]
- [Krener 2001][research_krener_2001]
- [Krengel 2024][research_krengel_2024]
- [Krenz 1979][research_krenz_1979]
- [Kress 1983][research_kress_1983]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Krienes 1941][research_krienes_1941]
- [Krishna 2021][research_krishna_2021]
- [Krishnamurthi and Gandhi 2016][research_krishnamurthi_gandhi_2016]
- [Krishnan et al][research_krishnan_mukund]
- [Krispin and Portnoy 1988][research_krispin_portnoy_1988]
- [Kroeger and Feistel 1976][research_kroeger_feistel_1976]
- [Krone 1980][research_kronejr_1980]
- [Krone 1980][research_kronejr_1980_b]
- [Kroo 1982][research_kroo_1982]
- [Kroo 1986][research_kroo_1986]
- [Kroo 1994][research_kroo_1994]
- [Kroo and Van Der Velden 1990][research_kroo_vandervelden_1990]
- [Kruse et al 2012][research_kruse_wunderlich_2012]
- [Kryvokhatko 2023][research_kryvokhatko_2023]
- [Kryvokhatko 2023][research_kryvokhatko_2023_b]
- [Kryvokhatko 2023][research_kryvokhatko_2023_c]
- [Kryvokhatko 2024][research_kryvokhatko_2024]
- [Kryvokhatko 2024][research_kryvokhatko_2024_b]
- [Krüger et al 2014][research_kruger_klimmek_2014]
- [Kube 2026][research_kube_2026]
- [Kuhlman and Brown 1989][research_kuhlman_brown_1989]
- [Kuhlman et al 1988][research_kuhlman_cerney_1988]
- [Kulfan 1974][research_kulfan_1974]
- [Kulfan 1979][research_kulfan_1979]
- [Kulfan and Vachal 1978][research_kulfan_vachal_1978]
- [Kulfan et al 1973][research_kulfan_neumann_1973]
- [Kumar and Aravindan 2014][research_kumar_aravindan_2014]
- [Kumar and Khalid 2014][research_kumar_khalid_2014]
- [Kumar et al 2004][research_kumar_raghavendra_2004]
- [Kumar et al 2020][research_kumar_mandal_2020]
- [Kumar et al 2021][research_kumar_topology_2021]
- [Kumar et al 2025][research_kumar_palanivel_2025]
- [Kumar et al 2026][research_kumar_ghosh_2026]
- [Kumar et al 2026][research_kumar_mathi_2026]
- [Kumkam et al 2025][research_kumkam_suratemeekul_2025]
- [Kunwar et al 2025][research_kunwar_mccormick_2025]
- [Kuo and Hsu 1997][research_kuo_hsu_1997]
- [Kurita et al 2013][research_kurita_koike_2013]
- [Kurus et al 2021][research_kurus_takahashi_2021]
- [Kuryachii et al 2014][research_kuryachii_manuilovich_2014]
- [Kurz and Kloker 2014][research_kurz_kloker_2014]
- [Kurz and Kloker 2015][research_kurz_kloker_2015]
- [Kurz and Kloker 2016][research_kurz_kloker_2016]
- [Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]
- [Kurzke et al 2025][research_kurzke_halliwell_2025]
- [Kusunose 2004][research_kusunose_2004]
- [Kutzbach et al 2004][research_kutzbach_lutz_2004]
- [Kwong 2021][research_kwong_2021]
- [Kyser and Willis 1973][research_kyser_willis_1973]
- [Körpe and Kanat 2019][research_korpe_kanat_2019]
- [La et al 2018][research_la_joe_2018]
- [Lacey 1979][research_lacey_1979]
- [Laitone 1978][research_laitone_1978]
- [Laitone 1978][research_laitone_1978_b]
- [Laitone 1989][research_laitone_1989]
- [Laitone 1994][research_laitone_1994]
- [Lam and Maull 1993][research_lam_maull_1993]
- [Lamar 1968][research_lamar_1968]
- [Lamar 1980][research_lamar_1980]
- [Lamar and Margason 1967][research_lamar_margason_1967]
- [Lamar and McKinney 1971][research_lamar_1971]
- [Laminar flow control wing 1999][research_laminar_flow_1999]
- [Lampert 1951 Rolling and yawing moments for swept-back wings in sideslip at supersonic speeds][research_lampert_1951]
- [Lampropoulos et al 2025][research_lampropoulos_sarris_2025]
- [Lampropoulos et al 2025][research_lampropoulos_vouros_2025]
- [Lan 1976][research_lan_1976]
- [Lan 1977][research_lan_1977]
- [Landfield and Rajkovic 1984][research_landfield_rajkovic_1984]
- [Landfield and Rajkovic 1986][research_landfield_rajkovic_1986]
- [Landgraf and Herring 1967][research_landgraf_herring_1967]
- [Landman et al 2005][research_landman_simpson_2005]
- [Lange et al 1974][research_lange_cahill_1974]
- [Langley Research Center 1966][research_naca_1966]
- [Lapin et al 1952][research_lapin_crookshanks_1952]
- [Larco et al 2018][research_larco_constatin_2018]
- [Large 1981][research_large_1981]
- [Larson 1986][research_larson_1986]
- [Larson 1987][research_larson_1987]
- [Larson and Schweikhard 1971][research_larson_schweikhard_1971]
- [Lasauskas 2016][research_lasauskas_2016]
- [Lateral Control Power Rolling 2003][research_lateral_control_2003]
- [Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]
- [Lauten et al 1954][research_lauten_lundstrom_1954]
- [Lavoie et al 2018][research_lavoie_bourgaultcote_2018]
- [Lawrence and Padfield 2005][research_lawrence_padfield_2005]
- [Lawrence and Padfield 2006][research_lawrence_padfield_2006]
- [Laxman Hattalli and Srivatsa 2018][research_laxmanhattalli_srivatsa_2018]
- [Lebofsky et al 2014][research_lebofsky_ting_2014]
- [Lebofsky et al 2015][research_lebofsky_ting_2015]
- [Lee][research_lee]
- [Lee 1952][research_lee_1952]
- [Lee 1963][research_lee_1963]
- [Lee 1964][research_lee_1964]
- [Lee 1964][research_lee_1964_b]
- [Lee 1969][research_lee_1969]
- [Lee 1969][research_lee_1969_b]
- [Lee 1970][research_lee_1970]
- [Lee 1975][research_lee_1975]
- [Lee 1994][research_lee_1994]
- [Lee 1994][research_lee_1994_b]
- [Lee 1995][research_lee_1995]
- [Lee 2004][research_lee_2004]
- [Lee 2006][research_lee_2006]
- [Lee 2013][research_lee_2013]
- [Lee and Batina 1991][research_lee_batina_1991]
- [Lee and Chen 2004][research_lee_chen_2004]
- [Lee and Healy 1964][research_lee_1964_2]
- [Lee and Ko 2009][research_lee_ko_2009]
- [Lee and Lee 2023][research_lee_lee_2023]
- [Lee and Libbey 1961][research_lee_libbey_1961]
- [Lee and Marnineau-Mes 1996][research_lee_marnineaumes_1996]
- [Lee and Nagati 2004][research_lee_nagati_2004]
- [Lee and Van Kampen 2021][research_lee_vankampen_2021]
- [Lee et al 1986][research_lee_tavella_1986]
- [Lee et al 1990][research_lee_miura_1990]
- [Lee et al 2003][research_lee_rodchenko_2003]
- [Lee et al 2018][research_lee_broeren_2018]
- [Lee et al 2019][research_lee_broeren_2019]
- [Lee et al 2019][research_lee_kim_2019]
- [Lee et al 2020][research_lee_broeren_2020]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2020][research_lee_kim_2020_b]
- [Lee-Rausch and Batina 1993][research_leerausch_batina_1993]
- [Lee-Rausch and Batina 1993][research_leerausch_batina_1993_b]
- [Lee-Rausch and Batina 1993][research_leerausch_batina_1993_c]
- [Lego and Altman 2013][research_lego_altman_2013]
- [Lehman and Stearman 1977][research_lehman_stearman_1977]
- [Lei and Zha 2021][research_lei_zha_2021]
- [Lei et al 2020][research_lei_zhang_2020]
- [Lei et al 2024][research_lei_an_2024]
- [Leishman 2026][research_leishman_2026]
- [Leitch et al 2025][research_leitch_2025]
- [Lekoudis 1980][research_lekoudis_1980]
- [Lekoudis 1980][research_lekoudis_1980_b]
- [Lekoudis 1981][research_lekoudis_1981]
- [Lemley 1968][research_lemley_1968]
- [Lemley and Mullans 1973][research_lemley_mullans_1973]
- [Lemley and Mullans 1974][research_lemley_mullans_1974]
- [Lendraitis and Lukosevicius 2025][research_lendraitis_2025]
- [Leonard et al 2023][research_leonard_prasetiyo_2023]
- [Leoviriyakit and Jameson 2004][research_leoviriyakit_jameson_2004]
- [Leoviriyakit and Jameson 2004][research_leoviriyakit_jameson_2004_b]
- [Leoviriyakit and Jameson 2005][research_leoviriyakit_jameson_2005]
- [Leoviriyakit et al 2004][research_leoviriyakit_kim_2004]
- [Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]
- [Lesoinne 2007][research_lesoinne_2007]
- [Letko 1956][research_letko_1956]
- [Letko and Brewer 1949][research_letko_brewer_1949]
- [Letko and Cowan 1948][research_letko_cowan_1948]
- [Letko and Jaquet 1948][research_letko_jaquet_1948]
- [Leung and Zingg 2011][research_leung_zingg_2011]
- [Levchenko and Scherbakov 1997][research_levchenko_scherbakov_1997]
- [Levesque et al 2015][research_levesque_pigeon_2015]
- [Levinsky and Palko 1982][research_levinsky_palko_1982]
- [Levison 1982][research_levison_1982]
- [Leylek and Costello 2010][research_leylek_costello_2010]
- [Leylek and Costello 2013][research_leylek_costello_2013]
- [Li 2015][research_li_2015]
- [Li 2023][research_li_2023]
- [Li and Cao 2025][research_li_cao_2025]
- [Li and Guo 2013][research_li_guo_2013]
- [Li and Jin 2018][research_li_jin_2018]
- [Li and Leschziner 2007][research_li_leschziner_2007]
- [Li and Liu 2024][research_li_liu_2024]
- [Li et al 1996][research_li_seebass_1996]
- [Li et al 1999][research_li_sobieczky_1999]
- [Li et al 2010][research_li_choudhari_2010]
- [Li et al 2011][research_li_choudhari_2011]
- [Li et al 2012][research_li_guo_2012]
- [Li et al 2012][research_li_guo_2012_b]
- [Li et al 2013][research_li_wang_2013]
- [Li et al 2013][research_li_yang_2013]
- [Li et al 2014][research_li_zhang_2014]
- [Li et al 2016][research_li_guo_2016]
- [Li et al 2016][research_li_guo_2016_b]
- [Li et al 2019][research_li_qian_2019]
- [Li et al 2020][research_li_varsweep_2020]
- [Li et al 2023][research_li_qiao_2023]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2025][research_li_2025]
- [Li et al 2025][research_li_2025_2]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_tu_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2026][research_li_2026]
- [Li et al 2026][research_li_tu_2026]
- [Li et al 2026][research_li_wei_2026]
- [Li et al 2026][research_li_yu_2026]
- [Liang 2024][research_liang_2024]
- [Liang and Wang 2018][research_liang_wang_2018]
- [Liang et al 2021][research_liang_wang_2021]
- [Librescu and Khdeir 1988][research_librescu_khdeir_1988]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Thangjitham 1988][research_librescu_thangjitham_1988]
- [Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Lichtenstein 1948][research_lichtenstein_1948]
- [Lichtenstein 1951][research_lichtenstein_1951]
- [Lichtenstein 1951][research_lichtenstein_1951_b]
- [Lichtenstein 1952][research_lichtenstein_1952]
- [Lichtenstein 1952][research_lichtenstein_1952_b]
- [Lichtenstein and Williams 1958][research_lichtenstein_williams_1958]
- [Lichtenstein and Williams 1961][research_lichtenstein_williams_1961]
- [Lichter 1974 The Effect of Porosity on the Lift and Drag of Bird's Wings][research_lichter_1974]
- [Liebrecht et al 2003][research_liebrecht_neuwerth_2003]
- [Liersch and Bishop 2018][research_liersch_bishop_2018]
- [Lift and Drag 2017][research_lift_and_2017]
- [Lijewski 1987][research_lijewski_1987]
- [Lin][research_lin]
- [Lin 2025][research_lin_2025]
- [Lin and Reed 1993][research_lin_reed_1993]
- [Lin et al 1996][research_lin_ng_1996]
- [Lin et al 2022][research_lin_song_2022]
- [Lin et al 2026][research_lin_yi_2026]
- [Lina and Moul 1965][research_lina_moul_1965]
- [Lindley 1956][research_lindley_1956]
- [Lindner 2006][research_lindner_2006]
- [Lindsay 2021][research_lindsay_2021]
- [Lindsley 2009][research_lindsley_2009]
- [Linear Quadratic Flight Control 2026][research_linear_quadratic_2026]
- [Liu 2006][research_liu_2006]
- [Liu 2012][research_liu_2012]
- [Liu 2022][research_liu_2022]
- [Liu 2022][research_liu_2022_b]
- [Liu 2022][research_liu_2022_c]
- [Liu 2022][research_liu_2022_d]
- [Liu 2022][research_liu_2022_e]
- [Liu 2024][research_liu_2024]
- [Liu and Wang 2025][research_liu_wang_2025]
- [Liu and Zhang 2013][research_liu_zhang_2013]
- [Liu et al 2009][research_liu_liou_2009]
- [Liu et al 2012][research_liu_li_2012]
- [Liu et al 2012][research_liu_xu_2012]
- [Liu et al 2016][research_liu_hou_2016]
- [Liu et al 2017][research_liu_yang_2017]
- [Liu et al 2019][research_liu_ouyang_2019]
- [Liu et al 2019][research_liu_yan_2019]
- [Liu et al 2020][research_liu_gao_2020]
- [Liu et al 2020][research_liu_shan_2020]
- [Liu et al 2020][research_liu_xu_2020]
- [Liu et al 2022][research_liu_bai_2022]
- [Liu et al 2022][research_liu_qian_2022]
- [Liu et al 2022][research_liu_shan_2022]
- [Liu et al 2023][research_liu_liang_2023]
- [Liu et al 2023][research_liu_liu_2023]
- [Liu et al 2026][research_liu_2026]
- [Liu et al 2026][research_liu_2026_2]
- [Liu et al 2026][research_liu_2026_3]
- [Liu et al 2026][research_liu_fan_2026]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_qian_2026]
- [Livne and Li 1994][research_livne_li_1994]
- [Livne and Li 1995][research_livne_li_1995]
- [Livne et al 2014][research_livne_precup_2014]
- [Llewellyn and Wolhart 1960][research_llewellyn_wolhart_1960]
- [Lock 1964][research_lock_1964]
- [Lockhart][research_lockhart]
- [Lockwood 1966][research_lockwood_1966]
- [Lockwood 1966][research_lockwood_1966_b]
- [Lockwood 1974][research_lockwood_1974]
- [Lockwood and Thompson 1964][research_lockwood_thompson_1964]
- [Lockwood and Watson 1948][research_lockwood_watson_1948]
- [Loechert et al 2018][research_loechert_huber_2018]
- [Loewy 1969][research_loewy_1969]
- [Lokos et al 2005][research_lokos_lizotte_2005]
- [Lombardi and Morelli 1994][research_lombardi_morelli_1994]
- [Lombardi and Vicini 1994][research_lombardi_vicini_1994]
- [Lombardi et al 1996][research_lombardi_morelli_1996]
- [Lombardi et al 1997][research_lombardi_salvetti_1997]
- [Long et al 2014][research_long_liu_2014]
- [Longitudinal Control and Trim 2003][research_longitudinal_control_2003]
- [Longitudinal Maneuvering Stability Theory 2003][research_longitudinal_maneuvering_2003]
- [Lorber 1992][research_lorber_1992_b]
- [Lorber and Carta 1991][research_lorber_carta_1991]
- [Lorber et al 1991][research_lorber_covinojr_1991]
- [Lorincz 1980][research_lorincz_1980]
- [Losee et al 1980][research_losee_willis_1980]
- [Lottati 1984][research_lottati_1984]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1987][research_lottati_1987]
- [Lottati 1988][research_lottati_1988]
- [Louma 1961][research_louma_1961]
- [Love et al 2004][research_love_zink_2004]
- [Lovell 2001][research_lovell_2001]
- [Loving 1961][research_loving_1961]
- [Loving 1961][research_loving_1961_b]
- [Lowe 1988][research_lowe_1988]
- [Lowenberg 2010][research_lowenberg_2010]
- [Lowry and Schneiter 1947][research_lowry_schneiter_1947]
- [Lowry et al 1948][research_lowry_axelson_1948]
- [Lowson and Riley 1995][research_lowson_riley_1995]
- [Lu and Lu 1997][research_lu_lu_1997]
- [Lu and Luo 2017][research_lu_luo_2017]
- [Lu et al 2004][research_lu_wu_2004]
- [Lu et al 2025][research_lu_2025]
- [Lu et al 2025][research_lu_lin_2025]
- [Luce 1949][research_luce_jr_1949]
- [Lucian et al 2012][research_lucian_mihaela_2012]
- [Lucy 1985][research_lucy_1985]
- [Luderer and Thielecke 2025][research_luderer_2025]
- [Lundry 1967][research_lundry_1967]
- [Lundry 1977][research_lundry_1977]
- [Luo and Zhou 2000][research_luo_zhou_2000]
- [Luochuan Li et al 2016][research_luochuanli_zhenghualiu_2016]
- [Luoma 1961][research_luoma_1961]
- [Lutze 1977][research_lutze_1977]
- [Lutze and Lluch 1996][research_lutze_lluch_1996]
- [Lux 1978][research_lux_1978]
- [Lv et al 2017][research_lv_zhang_2017]
- [lyer et al 1994][research_lyer_spall_1994]
- [Lynch et al 2015][research_lynch_crowell_2015]
- [Lynde and Campbell 2017][research_lynde_campbell_2017]
- [Lynde et al 2021][research_lynde_campbell_2021]
- [Lyu and Martins 2014][research_lyu_martins_2014]
- [Lyu and Martins 2015][research_lyu_martins_2015]
- [Lyubomirov and Yartsev 2015][research_lyubomirov_yartsev_2015]
- [Ma 1989][research_ma_1989]
- [Ma 2025][research_ma_2025]
- [Ma et al 2004][research_ma_liu_2004]
- [Ma et al 2016][research_ma_zhou_2016]
- [Ma et al 2017][research_ma_su_2017]
- [Ma et al 2018][research_ma_feng_2018]
- [Ma et al 2021][research_ma_bionic_2021]
- [Ma et al 2022][research_ma_fan_2022]
- [Ma et al 2023][research_ma_hui_2023]
- [Ma et al 2023][research_ma_liu_2023]
- [Ma et al 2024][research_ma_zhou_2024]
- [Ma et al 2026][research_ma_alwi_2026]
- [Macconochie and Breiner 1989][research_macconochie_breiner_1989]
- [MacConochie and Briener 1991][research_macconochie_briener_1991]
- [MacDougall and Lichtenstein 1946][research_macdougall_lichtenstein_1946]
- [Machireddy 2025][research_machireddy_2025]
- [Mack 1979][research_mack_1979]
- [Mack et al 2009][research_mack_schmid_2009]
- [Maddalon and Wagner 1986][research_maddalon_wagner_1986]
- [Maddalon et al 1989][research_maddalon_collier_1989]
- [Maddalon et al 1990][research_maddalon_collier_1990]
- [Madhan Kumar. G et al. 2019][research_madhankumargetal_2019]
- [Maggin and Bennett 1947][research_maggin_bennett_1947]
- [Mahaffey and Harding 1970][research_mahaffey_harding_1970]
- [Mahmood et al 2022][research_mahmood_hashemi_2022]
- [Mahns and Amitay 2025][research_mahns_amitay_2025]
- [Mahzan et al 2013][research_mahzan_muhamad_2013]
- [Maikapar 2000][research_maikapar_2000]
- [Maine 1977][research_maine_1977]
- [Maine 1978][research_maine_1978]
- [Maines et al 2018][research_maines_ghee_2018]
- [Maji et al 2024][research_maji_pandi_2024]
- [Majji et al 2007][research_majji_rediniotis_2007]
- [Maki 1959][research_maki_1959]
- [Maki 2016][research_maki_2016]
- [Malcolm 1978][research_malcolm_1978]
- [Malcolm 1979][research_malcolm_1979]
- [Malcolm 1985][research_malcolm_1985]
- [Malcolm and Clarkson 1976][research_malcolm_clarkson_1976]
- [Malcolm and Davis 1978][research_malcolm_davis_1978]
- [Malcom 1969][research_malcom_1969]
- [Malcom and Husband 1976][research_malcom_husband_1976]
- [Malik and Li 1993][research_malik_li_1993]
- [Malik et al 1996][research_malik_li_1996]
- [Malik et al 1999][research_malik_li_1999]
- [Malik et al 2013][research_malik_liao_2013]
- [Malik et al 2015][research_malik_liao_2015]
- [Malik et al 2017][research_malik_akhtar_2017]
- [Malik et al 2017][research_malik_akhtar_2017_b]
- [Malik et al 2020][research_malik_masud_2020]
- [Malik et al 2021][research_malik_masud_2021]
- [Malvestuto 1946][research_malvestuto_1946]
- [Malvestuto 1948][research_malvestuto_1948]
- [Mamla and Galinski 2009][research_mamla_galinski_2009]
- [Manan and Cooper 2008][research_manan_cooper_2008]
- [Manchester et al 2017][research_manchester_lipton_2017]
- [Mancini et al 1976][research_mancini_matsuhiro_1976]
- [Mangalam et al 2010][research_mangalam_jutte_2010]
- [Mann and Mercer 1985][research_mann_mercer_1985]
- [Mann and Mercer 1986][research_mann_mercer_1986]
- [Mann et al 1987][research_mann_huffman_1987]
- [Manoilo 2026][research_manoilo_2026]
- [Manokaran et al 2006][research_manokaran_vidya_2006]
- [Manor and Wentz 1985][research_manor_wentz_1985]
- [Mansfield 1952][research_mansfield_1952]
- [Manu et al 2026][research_manu_2026]
- [Manuilovich 2014][research_manuilovich_2014]
- [Manuilovich 2020][research_manuilovich_2020]
- [Manuilovich 2021][research_manuilovich_2021]
- [Manuilovich 2023][research_manuilovich_2023]
- [Manzo and Garcia 2010][research_manzo_garcia_2010]
- [Mao et al 2019][research_mao_xie_2019]
- [Marchetti 2023][research_marchetti_2023]
- [Marchman et al 1983][research_marchmaniii_donatelli_1983]
- [Mardanpour and Hodges 2013][research_mardanpour_hodges_2013]
- [Mardanpour and Hodges 2013][research_mardanpour_hodges_2013_b]
- [Mardanpour and Hodges 2014][research_mardanpour_hodges_2014]
- [Mardanpour et al 2013][research_mardanpour_hodges_2013_c]
- [Mares and Suresh Babu 2026][research_mares_sureshbabu_2026]
- [Margaris and Gursul 2004][research_margaris_gursul_2004]
- [Margolis 1947][research_margolis_1947]
- [Marino 2004][research_marino_2004]
- [Marouf et al 2023][research_marouf_hoarau_2023]
- [Marquart 1993][research_marquart_1993]
- [Marschalk et al 2021][research_marschalk_luteijn_2021]
- [Marsden and Price 2001][research_marsden_price_2001]
- [Marske 1975][research_marske_1975]
- [Martin 1953][research_martin_1953]
- [Martin 2008][research_martin_2008]
- [Martin and Crossley 2002][research_martin_crossley_2002]
- [Martin and Hill 1989][research_martin_hill_1989]
- [Martin et al 1988][research_martin_beissner_1988]
- [Martin et al 2008][research_martin_carpenter_2008]
- [Martina 1956][research_martina_1956]
- [Martina 1956][research_martina_1956_b]
- [Martina and Young 1955][research_martina_young_1955]
- [Martinez 1961][research_martinez_1961]
- [Martins 2016][research_martins_2016]
- [Marzocca et al 2001][research_marzocca_librescu_2001]
- [Marzouk 2025][research_marzouk_2025_b]
- [Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]
- [Mason 1953][research_mason_1953]
- [Mason 1982][research_mason_1982]
- [Mason 1983][research_mason_1983]
- [Masson et al 1999][research_masson_veilleux_1999]
- [Masud et al 2016][research_masud_malik_2016]
- [Matalla and Scholz 2021][research_matalla_scholz_2021]
- [Mateer and Bertelrud 1983][research_mateer_bertelrud_1983]
- [Mathioulakis and Georgantopoulou 2025][research_mathioulakis_georgantopoulou_2025]
- [Matsuno et al 2020][research_matsuno_esaki_2020]
- [Matsushima and Takanashi 1996][research_matsushima_takanashi_1996]
- [Matušů and Prokop 2015][research_matusu_prokop_2015]
- [Matějů 2019][research_mateju_2019]
- [Maughmer 1987][research_maughmer_1987]
- [Mavriplis et al 2020][research_mavriplis_yang_2020]
- [Mayes et al 1970][research_mayes_lores_1970]
- [McClain 2022][research_mcclain_2022]
- [McConnell 2004][research_mcconnell_2004]
- [McCormick 1959][research_mccormick_1959]
- [McCuish and Caldwell 2018][research_mccuish_caldwell_2018]
- [McCutchen 1989][research_mccutchen_1989]
- [McDaniel and Wilks 2004][research_mcdaniel_wilks_2004]
- [McElroy and Sharp 1971][research_mcelroy_sharp_1971]
- [McFadden and Bons 2025][research_mcfadden_bons_2025]
- [McFadden and Heinle 1954][research_mcfadden_heinle_1954]
- [McFadden et al 2022][research_mcfadden_brandt_2022]
- [McFadden et al 2022][research_mcfadden_brandt_2022_b]
- [McFall 1964][research_mcfall_1964]
- [McFarlane et al 2008][research_mcfarlane_richardson_2008]
- [McGeer 1984][research_mcgeer_1984]
- [McGrath 1993][research_mcgrath_1993]
- [McGurk et al 2024][research_mcgurk_stodieck_2024]
- [McKenzie 1973][research_mckenzie_1973]
- [McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]
- [McLachlan et al 1995][research_mclachlan_bell_1995]
- [McLaughlin et al 1967][research_mclaughlin_sawyer_1967]
- [McLellan and Cangelosi 1948][research_mclellan_cangelosi_1948]
- [McLemore 1958][research_mclemore_1958]
- [McLemore et al 1974][research_mclemore_parlett_1974]
- [McLemore et al 1977][research_mclemore_parlett_1977]
- [McMaster and Schenk 1973][research_mcmaster_schenk_1973]
- [McMurtry et al 1981][research_mcmurtry_sim_1981]
- [McTavish][research_mctavish]
- [Medina et al 2019][research_medina_rockwood_2019]
- [Meheut et al 2012][research_meheut_arntz_2012]
- [Mehndiratta et al 2026][research_mehndiratta_malhotra_2026]
- [Mehrotra and Lan 1978][research_mehrotra_lan_1978]
- [Mehrotra and Lan 1978][research_mehrotra_lan_1978_b]
- [Mehta 1986][research_mehta_1986]
- [Mehta et al 2008][research_mehta_frecker_2008]
- [Mei and Striz 1992][research_mei_striz_1992]
- [Mele et al 2017][research_mele_ostieri_2017]
- [Melton][research_melton]
- [Melton and Dudley 2016][research_melton_dudley_2016]
- [Melville and Gordnier 1998][research_melville_gordnier_1998]
- [Melvin and Zhao 2023][research_melvin_zhao_2023]
- [Melvin and Zhao 2024][research_melvin_zhao_2024]
- [Mendenhall and Spangler 1979][research_mendenhall_spangler_1979]
- [Meneghello et al 2015][research_meneghello_schmid_2015]
- [Meng et al 2024][research_meng_wang_2024]
- [Meng et al 2025][research_meng_lei_2025]
- [Mennu et al 2022][research_mennu_tran_2022]
- [Menon et al 2018][research_menon_chakravarthy_2018]
- [Menzies et al 1995][research_menzies_kandil_1995]
- [Merrett 2015][research_merrett_2015]
- [Mestrinho et al 2011][research_mestrinho_gamboa_2011]
- [Methel et al 2022][research_methel_mery_2022]
- [Method of the Qualitative 2020][research_method_of_2020]
- [Methods for Improving Longitudinal 2003][research_methods_for_2003_b]
- [Methods for Reducing Data 2003][research_methods_for_2003]
- [Meyer et al 1987][research_meyer_trujillo_1987]
- [Michaud et al 2018][research_michaud_dalir_2018]
- [Michel et al 1985][research_michel_arnal_1985]
- [Midmer and Bruecker 2024][research_midmer_bruecker_2024]
- [Mignosi et al 1986][research_mignosi_dor_1986]
- [Mikhailov 2020][research_mikhailov_2020]
- [Miklosovic and Perry 2014][research_miklosovic_perry_2014]
- [Miles 1949][research_miles_1949]
- [Miles 1953][research_miles_1953]
- [Miller 1970][research_miller_1970]
- [Miller 1983][research_miller_1983]
- [Miller 1986][research_miller_1986]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller and Hadley 1983][research_miller_hadley_1983]
- [Miller et al 1982][research_miller_wykes_1982]
- [Miller et al 1983][research_miller_wykes_1983]
- [Miller et al 2003][research_miller_jacques_2003]
- [Millidere et al 2021][research_millidere_karaman_2021]
- [Mir et al 2018][research_mir_maqsood_2018]
- [Mishriky and Walsh 2021][research_mishriky_walsh_2021]
- [Mishriky and Walsh 2023][research_mishriky_walsh_2023]
- [Mistry et al 2012][research_mistry_page_2012]
- [Mistry et al 2013][research_mistry_page_2013]
- [Mitashova 2022][research_mitashova_2022]
- [Mitcham 1957][research_mitcham_1957]
- [Mitcham and Blanchard 1950][research_mitcham_blanchard_1950]
- [Miwa et al 2022][research_miwa_yoshimi_2022]
- [Miyake and Terashima 2026][research_miyake_terashima_2026]
- [Mkhoyan et al 2020][research_mkhoyan_thakrar_2020]
- [Mkhoyan et al 2021][research_mkhoyan_thakrar_2021]
- [Mkhoyan et al 2022][research_mkhoyan_thakrar_2022]
- [Mo et al 2019][research_mo_kim_2019]
- [Model Rotor Testing for 2006][research_model_rotor_2006]
- [Modern Wing Shapes 1936][research_modern_wing_1936]
- [Modi and Ananthkrishnan 1998][research_modi_ananthkrishnan_1998]
- [Moeckel 1948][research_moeckel_1948]
- [Moeller and Rediniotis 2000][research_moeller_rediniotis_2000]
- [Moeller and Rediniotis 2002][research_moeller_rediniotis_2002]
- [Moens 2019][research_moens_2019]
- [Moens et al 2025][research_moens_2025]
- [Moghadam et al 2018][research_moghadam_ure_2018]
- [Mohammed 2007][research_mohammed_2007]
- [Mohammed 2015][research_mohammed_2015]
- [Mohd. Nasir 2026][research_mohdnasir_2026]
- [Moigne and Qin 2006][research_moigne_qin_2006]
- [Molent and Jones 2018][research_molent_jones_2018]
- [Molton et al 2013][research_molton_dandois_2013]
- [Momodu et al 2026][research_momodu_beg_2026]
- [Monaghan 1978][research_monaghan_1978]
- [Monfort and Whitcomb 1975][research_monfort_1975]
- [Monsch et al 2007][research_monsch_figliola_2007]
- [Monstein et al 2019][research_monstein_capone_2019]
- [Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]
- [Montgomery and Moul 1966][research_montgomery_moul_1966]
- [Montgomery et al 2019][research_montgomery_hunsaker_2019]
- [Montoya et al 1981][research_montoya_steers_1981]
- [Moon 1996][research_moon_1996]
- [Moore 1965][research_moore_1965]
- [Moore and Frei 1983][research_moore_frei_1983]
- [Moore et al 1980][research_moore_skow_1980]
- [Moored and Bart-Smith 2005][research_moored_bartsmith_2005]
- [Moorthamers and Hunsaker 2019][research_moorthamers_hunsaker_2019]
- [Moorthamers et al 2021][research_moorthamers_wiberg_2021]
- [Moosavi 2025][research_moosavi_2025]
- [Moosavi and Elasha 2022][research_moosavi_elasha_2022]
- [Moosavian 2021][research_moosavian_2021]
- [Moosavian et al 2013][research_moosavian_xi_2013]
- [Moosavian et al 2014][research_moosavian_xi_2014]
- [Morehouse et al 1977][research_morehouse_1977]
- [Morelli 2021][research_morelli_2021]
- [Morelli 2022][research_morelli_2022]
- [Mori et al 2024][research_mori_yakeno_2024]
- [Mori et al 2024][research_mori_yakeno_2024_b]
- [Morphing WING REAL TIME 2010][research_morphing_wing_2010]
- [Morphing Wing Technologies 2018][research_morphing_wing_2018]
- [Morris 1990][research_morris_1990]
- [Morris and Silsby 1952][research_morris_silsby_1952]
- [Morris and Silsby 1954][research_morris_silsby_1954]
- [Morris et al 1950][research_morris_kennedy_1950]
- [Morton 1956][research_morton_1956]
- [Moseley and Gainer 1959][research_moseley_gainer_1959]
- [Moseley and Watson 1951 Investigation of wing-tip ailerons on a 51.3 degrees sweptback wing at transonic speeds by the transonic-bump method][research_moseley_1951]
- [Moskalenko and Kosyrev 2019][research_moskalenko_kosyrev_2019]
- [Mottershead and Cooper 2012][research_mottershead_cooper_2012]
- [Motycka and Skowronek 1967][research_motycka_skowronek_1967]
- [Mou-Jie 1979][research_moujie_1979]
- [Moulton et al 2026][research_moulton_bolander_2026]
- [Moura et al 2024][research_moura_nepomuceno_2024]
- [Mousseux et al 1989][research_mousseux_1989]
- [Mouton et al 2026][research_mouton_charpentier_2026]
- [Mughal and Ashworth 2013][research_mughal_ashworth_2013]
- [Mugler 1958][research_mugler_1958]
- [Mugler 1959][research_mugler_1959]
- [Mugler 1959][research_mugler_1959_b]
- [Mugler and Woodall 1960][research_mugler_woodall_1960]
- [Muhammad Umer et al 2020][research_muhammadumer_maqsood_2020]
- [Mukhopadhyay 1995][research_mukhopadhyay_1995]
- [Mukhtar 2023][research_mukhtar_2023]
- [Multiloop Flight Control Systems 1990][research_multiloop_flight_1990]
- [Muraoka et al 2009][research_muraoka_okada_2009]
- [Murch and Foster 2007][research_murch_foster_2007]
- [Murphy et al 1976][research_murphy_peloubet_1976]
- [Murphy et al 1983][research_murphy_rogers_1983]
- [Murphy et al 2004][research_murphy_klein_2004]
- [Murri et al 1983][research_murri_croom_1983]
- [Musa et al 2015][research_musa_mansor_2015]
- [Musa et al 2026][research_musa_mansor_2026]
- [Mushitani and Hiramoto 2019][research_mushitani_hiramoto_2019]
- [Musso et al 2026][research_musso_vo_2026]
- [Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]
- [Muñoz and García-Fogeda 2023][research_munoz_garciafogeda_2023]
- [Myers et al 1983][research_myers_guruswamy_1983]
- [Müller et al 2020][research_muller_lutz_2020]
- [NACA Conference on Aerodynamic 1947][research_naca_conference_1947]
- [NACA Conference on Aerodynamic 1949][research_naca_1949]
- [NACA Conference on Aircraft 1957][research_naca_1957]
- [Naeseth 1956][research_naeseth_1956]
- [Naeseth 1956][research_naeseth_1956_b]
- [Nagamatsu and Ficarra 1985][research_nagamatsu_ficarra_1985]
- [Nagel et al 2015][research_nagel_fiedler_2015]
- [Nagornov 2020][research_nagornov_2020]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Naik and Ostowari 1987][research_naik_ostowari_1987]
- [Naik and Ostowari 1988][research_naik_ostowari_1988]
- [Naik and Ostowari 1990][research_naik_ostowari_1990]
- [Nakagawa et al 2023][research_nakagawa_ishida_2023]
- [Nakamura et al 2017][research_nakamura_uehara_2017]
- [Nakhla and Elruby 2021][research_nakhla_elruby_2021]
- [Nam et al 1998][research_nam_chattopadhyay_1998]
- [Nam et al 2000][research_nam_chattopadhyay_2000]
- [Namdeo et al 2023][research_namdeo_bhattacharyya_2023]
- [Namura et al 2015][research_namura_shimoyama_2015]
- [Nangia and Palmer 2002][research_nangia_palmer_2002]
- [Nangia and Palmer 2007][research_nangia_palmer_2007]
- [Nangia et al 2003][research_nangia_palmer_2003]
- [Nangia et al 2003][research_nangia_palmer_2003_b]
- [Nangia et al 2005][research_nangia_palmer_2005]
- [Nangia et al 2023][research_nangia_ghoreyshi_2023]
- [Nardi 1970][research_nardi_1970]
- [Nasir and Kuntjoro 2013][research_nasir_kuntjoro_2013]
- [nath and ana 2017][research_nath_ana_2017]
- [Nathan 2026][research_nathan_2026]
- [Navaratna and Pontillo 2022][research_navaratna_pontillo_2022]
- [Navaratna et al 2022][research_navaratna_lowenberg_2022]
- [Nazeer et al 2021][research_nazeer_2021]
- [Nee Chan et al 2018][research_neechan_yazdiharmin_2018]
- [Neely 1943][research_neely_1943]
- [Neely and Koven 1947][research_neely_koven_1947]
- [Negahban et al 2025][research_negahban_hallonet_2025]
- [Negahban et al 2025][research_negahban_saci_2025]
- [Neihouse 1940][research_neihouse_1940]
- [Neihouse 1949][research_neihouse_1949]
- [Neihouse and Carmel 1942][research_neihouse_carmel_1942]
- [Neihouse and Lee 1951][research_neihouse_lee_1951]
- [Neihouse et al 1946][research_neihouse_lichtenstein_1946]
- [Nellner 1993][research_nellner_1993]
- [Nellner and Zierep 1993][research_nellner_zierep_1993]
- [Nelms 1976][research_nelms_1976]
- [Nelms and Bailey 1974][research_nelms_bailey_1974]
- [Nelson 1992][research_nelson_1992]
- [Ness 1971][research_ness_1971]
- [Nettleton 1965][research_nettleton_1965]
- [Neuert and Dinkler 2020][research_neuert_dinkler_2020]
- [Neves and Mariani 2024][research_neves_mariani_2024]
- [Newell and Marsh 1967][research_newell_marsh_1967]
- [Newey][research_newey]
- [Newman and Swaim 1986][research_newman_swaim_1986]
- [Newsam et al 2024][research_newsam_midmer_2024]
- [Neyland and Filippov 2004][research_neyland_filippov_2004]
- [Ng and Crouch 1999][research_ng_crouch_1999]
- [Ng et al 1993][research_ng_skaff_1993]
- [Ng et al 1994][research_ng_skaff_1994]
- [Ng et al 2003][research_ng_ray_2003]
- [Nguyen et al 1980][research_nguyen_gilbert_1980]
- [Nguyen et al 2013][research_nguyen_ting_2013]
- [Nguyen et al 2014][research_nguyen_livne_2014]
- [Nguyen et al 2014][research_nguyen_ting_2014]
- [Nguyen et al 2016][research_nguyen_tran_2016]
- [Nguyen et al 2018][research_nguyen_hashemi_2018]
- [Ni et al 2015][research_ni_hou_2015]
- [Nial 1972][research_nial_1972]
- [Nicholas et al 1984][research_nicholas_naville_1984]
- [Nichols and Englar 1980][research_nicholsjr_englar_1980]
- [Nichols et al 1993][research_nichols_reichert_1993]
- [Nicholson et al 2018][research_nicholson_zhang_2018]
- [Nicholson et al 2019][research_nicholson_duan_2019]
- [Nicks 1983][research_nicks_1983]
- [Nicolas et al 2016][research_nicolas_sullivan_2016]
- [Niedling 1980][research_niedling_1980]
- [Niel][research_niel]
- [Nielsen et al 1953][research_nielsen_kaattari_1953]
- [Nieto Gómez and Chimeno Manguán 2025][research_nietogomez_chimenomanguan_2025]
- [Nigam et al 2020][research_nigam_tang_2020]
- [Nikbay and Acar 2015][research_nikbay_acar_2015]
- [Nikolic 2006][research_nikolic_2006]
- [Nikolic 2007][research_nikolic_2007]
- [Nikolic 2008][research_nikolic_2008]
- [Nishino and Shariff 2009][research_nishino_shariff_2009]
- [Nitschke-Kowsky and Bippes 1988][research_nitschkekowsky_bippes_1988]
- [Nixon 1992][research_nixon_1992]
- [Nixon 2001][research_nixon_2001]
- [Nixon 2006][research_nixon_2006]
- [Nobleheart et al 2012][research_nobleheart_l_2012]
- [Nobleheart et al 2013][research_nobleheart_shivanapuralakshmikanth_2013]
- [Noll and Huttsell 1978][research_noll_huttsell_1978]
- [Noll et al 1983][research_noll_calico_1983]
- [Noll et al 1983][research_noll_eastep_1983]
- [Noll et al 1984][research_noll_eastep_1984]
- [Nominal aircraft dynamics][research_nominal_aircraft]
- [Nomura 2003][research_nomura_2003]
- [Nomura 2006][research_nomura_2006]
- [Nonlinear aerolasticity, continuum theory 2007][research_nonlinear_aerolasticity_2007]
- [Nonweiler 1960][research_nonweiler_1960]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]
- [Noviello et al 2016][research_noviello_rea_2016]
- [Noviello et al 2019][research_noviello_dimino_2019]
- [Novikov et al 2024][research_novikov_obraz_2024]
- [Nowak and Solies 2000][research_nowak_solies_2000]
- [Nudson et al 2025][research_nudson_stanfieldbrown_2025]
- [Nugent 1956][research_nugent_1956]
- [Nugroho 2026][research_nugroho_2026]
- [Numerical investigation of aerodynamic 2023][research_numerical_investigation_2023]
- [Nusyirwan and Kung 2016][research_nusyirwan_kung_2016]
- [Nyquist 1928][research_nyquist_1928]
- [O'Grady et al 2009][research_ogrady_reich_2009]
- [O'Kelly 1955][research_okelly_1955]
- [O'Kelly et al 1954][research_okelly_lundstrom_1954]
- [Obayashi][research_obayashi]
- [Obayashi et al 1997][research_obayashi_yamaguchi_1997]
- [Oblique Wing Aircraft 2020][research_oblique_wing_2020]
- [Oblique Wing Remotely Piloted 1974][research_oblique_wing_1974]
- [Oblique wing transonic transport 1977][research_naca_1977]
- [Obradovic and Subbarao 2009][research_obradovic_subbarao_2009]
- [Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]
- [Obradovic and Subbarao 2011][research_obradovic_subbarao_2011]
- [Obradovic and Subbarao 2011][research_obradovic_subbarao_2011_b]
- [Obradovic and Subbarao 2011][research_obradovic_subbarao_2011_c]
- [Obradovic and Subbarao 2012][research_obradovic_subbarao_2012]
- [Oggioni et al 2026][research_oggioni_riboldi_2026]
- [Oh and Tavella 1986][research_oh_tavella_1986]
- [Ohira et al 2013][research_ohira_kwak_2013]
- [Ohmichi et al 2018][research_ohmichi_ishida_2018]
- [Oktay and Eraslan 2022][research_oktay_eraslan_2022]
- [Oktay and Eraslan 2024][research_oktay_eraslan_2024]
- [Oktay and Sultan 2014][research_oktay_sultan_2014]
- [Oktay and Özen 2022][research_oktay_ozen_2022]
- [Oland and Kristiansen 2013][research_oland_kristiansen_2013]
- [Olivett et al 2020][research_olivett_corrao_2020]
- [Olivett et al 2021][research_olivett_corrao_2021]
- [Olson and Dvorak 1976][research_olson_dvorak_1976]
- [Olstad and Fischetti 1958][research_olstad_fischetti_1958]
- [Olugbeji Jemitola and Peter Okonkwo 2021][research_olugbejijemitola_peterokonkwo_2021]
- [Onewein 1967][research_onewein_1967]
- [Onofri et al 2026][research_onofri_antonini_2026]
- [Oosterom and Babuska][research_oosterom_babuska]
- [Oosterom and Babuška 2006][research_oosterom_babuska_2006]
- [Ordaz et al 2015][research_ordaz_geiselhart_2015]
- [Orloff 1978][research_orloff_1978]
- [Orloff and Ciffone 1974][research_orloff_ciffone_1974]
- [Ortamevzi 2015][research_ortamevzi_2015]
- [Ortiz and Alley 2018][research_ortiz_alley_2018]
- [Oshima et al 2022][research_oshima_wygnanski_2022]
- [Otto and Streett 1994][research_otto_streett_1994]
- [Outlaw 2011][research_outlaw_2011]
- [Ouyang et al 2021][research_ouyang_zeng_2021]
- [Owens and Perkins 1996][research_owens_perkins_1996]
- [Oyama et al 2008][research_oyama_ito_2008]
- [Oyibo 1984][research_oyibo_1984]
- [Ozbek et al 2023][research_ozbek_ekici_2023]
- [Ozbek et al 2024][research_ozbek_ekici_2024]
- [Pabla 2021][research_pabla_2021]
- [Pagano 2018][research_pagano_2018]
- [Page 1965][research_page_1965]
- [Paget 1967][research_paget_1967]
- [Pahle 1990][research_pahle_1990]
- [Painter 1983][research_painter_1983]
- [Painter and Caw 1978][research_painter_1978]
- [Pak and Lung 2011][research_pak_lung_2011]
- [Pak and Truong 2015][research_pak_truong_2015]
- [Palaia et al 2025][research_palaia_salem_2025]
- [Pamadi 1988][research_pamadi_1988]
- [Pamadi and Pai 1980][research_pamadi_pai_1980]
- [Pamadi and Taylor 1982][research_pamadi_taylor_1982]
- [Pamnani and Jeughale 2021][research_pamnani_jeughale_2021]
- [Pamnani and Jeughale 2021][research_pamnani_jeughale_2021_b]
- [Pan and Cheng 1994][research_pan_cheng_1994]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan et al 2026][research_pan_2026]
- [Pande 2025][research_pande_2025]
- [Pandi and Kumar 2025][research_pandi_kumar_2025]
- [Panel flutter in a 1991][research_panel_flutter_1991]
- [Panina et al 2017][research_panina_kosinov_2017]
- [Panina et al 2021][research_panina_yatskikh_2021]
- [Paniszczyn 1967][research_paniszczyn_1967]
- [Pant and Fielding 1999][research_pant_fielding_1999]
- [Pao and Lan 1978][research_pao_lan_1978]
- [Papadakis et al 2003][research_papadakis_yeong_2003]
- [Papadakis et al 2004][research_papadakis_yeong_2004]
- [Paranjape 2022][research_paranjape_2022]
- [Paranjape 2023][research_paranjape_2023]
- [Paranjape and Ananthkrishnan 2010][research_paranjape_ananthkrishnan_2010]
- [Paranjape and Chung 2010][research_paranjape_chung_2010]
- [Park 2007][research_park_2007]
- [Park et al 1996][research_park_matuda_1996]
- [Parlett and Shivers 1976][research_parlett_shivers_1976]
- [Parra 2023][research_parra_2023]
- [Parsons 1958][research_parsons_1958]
- [Pasamanick and Sellers 1950][research_pasamanick_sellers_1950]
- [Pashilkar 1996][research_pashilkar_1996]
- [Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]
- [Pate 1964][research_pate_1964]
- [Pate and Brillhart 1963][research_pate_brillhart_1963]
- [Pate and Deitering 1963][research_pate_deitering_1963]
- [Pate and Deitering 1963][research_pate_deitering_1963_b]
- [Pate and German 2014][research_pate_german_2014]
- [Patierno 1980][research_patierno_1980]
- [Patil 2003][research_patil_2003]
- [Patil 2004][research_patil_2004]
- [Patterson 1984][research_patterson_1984]
- [Patterson and Loving 1961][research_patterson_loving_1961]
- [Pattinson et al 2013][research_pattinson_lowenberg_2013]
- [Pattinson et al 2013][research_pattinson_lowenberg_2013_b]
- [Patton 1980][research_patton_1980]
- [Patton 1980][research_patton_1980_b]
- [Patton et al 1979][research_patton_stough_1979]
- [Paudel 2021][research_paudel_2021]
- [Pavelka and Tatum 1980][research_pavelka_tatum_1980]
- [Paziresh et al 2017][research_paziresh_nikseresht_2017]
- [Pearcey 1962][research_pearcey_1962]
- [Peck and Hudson 1956][research_peck_hudson_1956]
- [Peck et al 2024][research_peck_groot_2024]
- [Pecora 2018][research_pecora_2018]
- [Pecora 2021][research_pecora_2021]
- [Pecora and Pecora 2018][research_pecora_pecora_2018]
- [Pecora et al 2012][research_pecora_amoroso_2012]
- [Peele and Eckstrom 1975][research_peele_1975]
- [Peltzer et al 2009][research_peltzer_wicke_2009]
- [Pena 2020][research_pena_2020]
- [Pena et al 2018][research_pena_2018]
- [Peng et al 2022][research_peng_avallone_2022]
- [Peng et al 2024][research_peng_avallone_2024]
- [Pengelley and Wilson 1954][research_pengelley_wilson_1954]
- [Pengyuan et al 2024][research_pengyuan_yanfei_2024]
- [Penner et al 2025][research_penner_sousa_2025]
- [Pepoon 1944][research_pepoon_1944]
- [Perera 2021][research_perera_2021]
- [Perera and Guo 2008][research_perera_guo_2008]
- [Perez et al 2011][research_perez_rodriguez_2011]
- [Perraud et al 2003][research_perraud_moens_2003]
- [Perraud et al 2004][research_perraud_seraudie_2004]
- [Perry 1966][research_perry_1966]
- [Perry and Miklosovic 2012][research_perry_miklosovic_2012]
- [Peter and Stumpf 2018][research_peter_stumpf_2018]
- [Petersen 1979][research_petersen_1979]
- [Peterson and Grant 2011][research_peterson_grant_2011]
- [Peterson and Menees 1961][research_peterson_menees_1961]
- [Peterson and Menees 1961][research_peterson_menees_1961_b]
- [Petre and Ashley 1975][research_petre_ashley_1975]
- [Petre and Ashley 1976][research_petre_ashley_1976]
- [Petrov 1993][research_petrov_1993]
- [Petrov 2009][research_petrov_2009]
- [Pettit and Grandhi 2003][research_pettit_grandhi_2003]
- [Pfaff 1965][research_pfaff_1965]
- [Pfenninger and Bacon 1961][research_pfenninger_bacon_1961]
- [Pfenninger and Bacon 1969][research_pfenninger_bacon_1969]
- [Pfenninger and Groth 1961][research_pfenninger_groth_1961]
- [Pfenninger and Vemuru 1988][research_pfenninger_vemuru_1988]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Pfnür et al 2018][research_pfnur_oppelt_2018]
- [Pham and Peraza Hernandez 2021][research_pham_perazahernandez_2021]
- [Philipsen et al 2015][research_philipsen_postma_2015]
- [Phillips 1948][research_phillips_1948]
- [Phillips 1989][research_phillips_1989]
- [Phillips and Anderson 2002][research_phillips_anderson_2002_b]
- [Phillips and West 2017][research_phillips_west_2017]
- [Phillips and West 2019][research_phillips_west_2019]
- [Phillips et al 2002][research_phillips_anderson_2002]
- [Phillips et al 2006][research_phillips_fugal_2006]
- [Phillips et al 2008][research_phillips_hunsaker_2008]
- [Phillips et al 2019][research_phillips_hunsaker_2019]
- [Phillips et al 2019][research_phillips_wygnanski_2019]
- [Phillips et al 2020][research_phillips_hunsaker_2020]
- [Phuekpan et al 2025][research_phuekpan_2025]
- [Physical Phenomena Associated with 1989][research_physical_phenomena_1989]
- [Pier 2003][research_pier_2003]
- [Pirrung et al 2026][research_pirrung_sorensen_2026]
- [Pisaneschi et al 2026][research_pisaneschi_2026]
- [Pitcher and Maple 2008][research_pitcher_maple_2008]
- [Pitkin 1943][research_pitkin_1943]
- [Pitkin et al 1947][research_pitkin_gardner_1947]
- [Pitt 2004][research_pitt_2004]
- [Placement in Flight Control 2026][research_placement_in_2026]
- [Planeaux 1991][research_planeaux_1991]
- [Plante et al 2017][research_plante_dandois_2017]
- [Podugu and Ananthasuresh 2010][research_podugu_ananthasuresh_2010]
- [Pogosyan 2025][research_pogosyan_2025]
- [Polhamus 1948][research_polhamus_1948]
- [Polhamus 1963][research_polhamus_1963]
- [Polhamus 1983][research_polhamus_1983]
- [Polhamus 1984][research_polhamus_1984]
- [Polhamus and Hammond 1960][research_polhamus_1960]
- [Polhamus and Toll 1981][research_polhamus_1981]
- [Polidoro and Bhattacharya 2026][research_polidoro_bhattacharya_2026]
- [Poll 1986][research_poll_1986]
- [Poll and Danks 1995][research_poll_danks_1995]
- [Poll and Paisley 1985][research_poll_paisley_1985]
- [Pongkorung 2026][research_pongkorung_2026]
- [Pons and Cirak 2023][research_pons_cirak_2023]
- [Poojari 2022][research_poojari_2022]
- [Poomadath and Ajaj 2025][research_poomadath_ajaj_2025]
- [Popescu 1999][research_popescu_1999]
- [Popescu 2000][research_popescu_2000]
- [Popescu 2002][research_popescu_2002]
- [Poplingher and Raveh 2023][research_poplingher_raveh_2023]
- [Poplingher and Raveh 2024][research_poplingher_raveh_2024]
- [Popov et al 2008][research_popov_labib_2008]
- [Popov et al 2010][research_popov_grigorie_2010]
- [Popov et al 2010][research_popov_grigorie_2010_b]
- [Popov et al 2010][research_popov_grigorie_2010_c]
- [Potapczuk and Bidwell 1990][research_potapczuk_bidwell_1990]
- [Potapczuk and Bidwell 1991][research_potapczuk_bidwell_1991]
- [Potapczuk et al 2003][research_potapczuk_papadakis_2003]
- [Potential Equation Methods for 1982][research_potential_equation_1982]
- [Powers 1977][research_powers_1977]
- [Powers and Webb 1997][research_powers_webb_1997]
- [Powers et al 1992][research_powers_webb_1992]
- [Prabhakar 2025][research_prabhakar_2025]
- [Prabhakar and Murugan 2022][research_prabhakar_murugan_2022]
- [Prabhakar and Murugan 2024][research_prabhakar_murugan_2024]
- [Prabhakar and Murugan 2026][research_prabhakar_murugan_2026]
- [Prabhakar et al 2015][research_prabhakar_prazenica_2015]
- [Prabhakar et al 2019][research_prabhakar_prazenica_2019]
- [Prajapati and Kapania 2026][research_prajapati_kapania_2026]
- [Prakash et al 2009][research_prakash_uthup_2009]
- [Prandtl 1928][research_prandtl_1928]
- [Prasad et al 2024][research_prasad_raghavulu_2024]
- [Pratt and Shields 1952][research_pratt_shields_1952]
- [Prediction of transonic flutter 1981][research_prediction_of_1981]
- [Prediction of vortex breakdown 1994][research_prediction_of_1994]
- [Pressures and Temperatures for 2000][research_pressures_and_2000]
- [Preston et al 2025][research_preston_palacios_2025]
- [Preston et al 2026][research_preston_fasel_2026]
- [Previati et al 2012][research_previati_gobbi_2012]
- [Previtali et al 2013][research_previtali_arrieta_2013]
- [Previtali et al 2014][research_previtali_arrieta_2014]
- [Priest et al 2023][research_priest_snyder_2023]
- [Prior et al 2023][research_prior_rozinka_2023]
- [Properties of the U.S 2014][research_properties_of_2014]
- [Properties of the U.S 2024][research_properties_of_2024]
- [Prudenzano et al 2025][research_prudenzano_gand_2025]
- [Pruett et al 2000][research_pruett_chang_2000]
- [Pu et al 2024][research_pu_zhang_2024]
- [Pugliese and Englar 1979][research_pugliese_englar_1979]
- [Purser and Spearman 1951][research_purser_spearman_1951]
- [Purser et al 1947][research_purser_spearman_1947]
- [Purwanto et al 2001][research_purwanto_riyanto_2001]
- [Pusztai et al 2024][research_pusztai_lowenberg_2024]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putman 1969][research_putman_1969]
- [Putnam and Ayers 1988][research_putnam_ayers_1988]
- [Putnam and Ayers 1989][research_putnam_ayers_1989]
- [Putro et al 2025][research_putro_junipitoyo_2025]
- [Puyou and Berard 2007][research_puyou_berard_2007]
- [Pyeon and Bae 2026][research_pyeon_bae_2026]
- [Pérez et al 2012][research_perez_rodriguez_2012]
- [Pérez Pérez][research_perezperez]
- [Qi et al 2021][research_qi_zong_2021]
- [Qi et al 2023][research_qi_zhao_2023]
- [Qian and Guan 2012][research_qian_guan_2012]
- [Qiao et al 2018][research_qiao_zhang_2018]
- [Qiao et al 2019][research_qiao_zhou_2019]
- [Qin 2012][research_qin_2012]
- [Qin et al 2014][research_qin_wang_2014]
- [Qingbao et al 2026][research_qingbao_hui_2026]
- [Qu et al 2024][research_qu_wang_2024]
- [Qu et al 2025][research_qu_wang_2025]
- [Quan et al 2013][research_quan_ye_2013]
- [Quan et al 2026][research_quan_deng_2026]
- [Quantitative Design Requirements for 2017][research_quantitative_design_2017]
- [Quast et al 1990][research_quast_henke_1990]
- [Queijo and Jaquet 1948][research_queijo_jaquet_1948]
- [Queijo and Jaquet 1948][research_queijo_jaquet_1948_b]
- [Queijo and Lichtenstein 1948][research_queijo_lichtenstein_1948]
- [Queijo and Wolhart 1951][research_queijo_wolhart_1951]
- [Queijo et al 1954][research_queijo_1954]
- [Querry][research_querry]
- [Quigley et al 1960][research_quigley_1960]
- [Rade and de Souza 2016][research_rade_desouza_2016]
- [Radeztsky et al 1995][research_radeztsky_reibert_1995]
- [Radhakrishnan P et al 2021][research_radhakrishnanp_ramanang_2021]
- [Radzetsky et al 1994][research_radzetskyjr_reibert_1994]
- [Raghavan and Patil 2009][research_raghavan_patil_2009]
- [Raghavendra et al 2005][research_raghavendra_sahai_2005]
- [Raheel and Toropov 2018][research_raheel_toropov_2018]
- [Rahman et al 2022][research_rahman_aljibory_2022]
- [Rahn and Reinertson 1986][research_rahn_reinertson_1986]
- [Rajamurthy 2002][research_rajamurthy_2002]
- [Rajesh Senthil Kumar et al 2020][research_rajeshsenthilkumar_venugopal_2020]
- [Rajeswari and Prabhu 1987][research_rajeswari_prabhu_1987]
- [Ralson 1983][research_ralson_1983]
- [Ramachandran and Wells 1974][research_ramachandran_wells_1974]
- [Ramachandran and Wells 1975][research_ramachandran_wells_1975]
- [Rambacher and Bons 2023][research_rambacher_bons_2023]
- [Rambacher et al 2024][research_rambacher_butler_2024]
- [Ramirez Zeigler and Avery 2026][research_ramirezzeigler_avery_2026]
- [Ramprasadh and Devanandh 2015][research_ramprasadh_devanandh_2015]
- [Raney 1987][research_raney_1987]
- [Raney and Batterson 1989][research_raney_batterson_1989]
- [Rao 1983][research_rao_1983]
- [Rao 1992][research_rao_1992]
- [Rao 2019][research_rao_2019]
- [Rao and Huffman 1978][research_rao_huffman_1978]
- [Rao and Johnson 1982][research_rao_1982]
- [Rao and Sinha 2010][research_rao_sinha_2010]
- [Raol and Singh 2023][research_raol_singh_2023]
- [Rashad et al 2025][research_rashad_elbadawy_2025]
- [Ratcliff and Carlson 1989][research_ratcliff_carlson_1989]
- [Rathert et al 1951][research_rathert_1951]
- [Rausch et al 1992][research_rausch_batina_1992]
- [Raveh and Levy 2004][research_raveh_levy_2004]
- [Ray et al 1972][research_ray_1972]
- [Razak et al 2011][research_razak_andrianne_2011]
- [Razi and Ghadiri 2008][research_razi_ghadiri_2008]
- [Re and Reubush 1979][research_re_reubush_1979]
- [Rea et al 2018][research_rea_pecora_2018]
- [Recktenwald and Ahmed 2008][research_recktenwald_ahmed_2008]
- [Redd et al 1974][research_redd_gilman_1974]
- [Reddy 1981][research_reddy_1981]
- [Reddy and Ghaffari 1982][research_reddy_ghaffari_1982]
- [Redeker and Wichmann 1988][research_redeker_wichmann_1988]
- [Redeker and Wichmann 1991][research_redeker_wichmann_1991]
- [Redin 1981][research_redin_1981]
- [Rediniotis et al 1994][research_rediniotis_klute_1994]
- [Reed 1955][research_reed_1955]
- [Reed 1975][research_reed_1975]
- [Reed 1984][research_reed_1984]
- [Reed 1985][research_reed_1985]
- [Reed 1987][research_reed_1987]
- [Reed 1989][research_reed_1989]
- [Reed 1991][research_reed_1991]
- [Reed and Saric 2002][research_reed_saric_2002]
- [Reeh et al 2013][research_reeh_weismuller_2013]
- [Reeh et al 2014][research_reeh_weismuller_2014]
- [Reibert et al 1996][research_reibert_saric_1996]
- [Reibert et al 1997][research_reibert_saric_1997]
- [Reich and Sanders 2007][research_reich_sanders_2007_b]
- [Reich et al 2002][research_reich_raveh_2002]
- [Reich et al 2004][research_reich_raveh_2004]
- [Reich et al 2007][research_reich_sanders_2007]
- [Reid et al 1994][research_reid_rajagopal_1994]
- [Reimer et al][research_reimer_braun]
- [Rein et al 2025][research_rein_henne_2025]
- [Ren et al 2025][research_ren_kan_2025]
- [Ren et al 2025][research_ren_wei_2025]
- [Ren et al 2025][research_ren_wei_2025_b]
- [Ren et al 2026][research_ren_2026]
- [Report no. 257, Pressure 1927][research_report_no_1927]
- [Report No. 349. A 1930][research_report_no_1930]
- [Report No. 538, altitude-pressure 1935][research_report_no_1935]
- [Reshotko et al 2000][research_reshotko_vargas_2000]
- [Reubush 1977][research_reubush_1977]
- [Reubush 1978][research_reubush_1978]
- [Reubush 1979][research_reubush_1979]
- [Reubush and Mercer 1974][research_reubush_mercer_1974]
- [Reubush and Mercer 1975][research_reubush_mercer_1975]
- [Review of Transonic Aerodynamics 1982][research_review_of_1982]
- [Revivo and Raveh 2025][research_revivo_raveh_2025]
- [Rhoads 1952][research_rhoads_1952]
- [Rhoads 1970][research_rhoads_1970]
- [Rhodes and Johns 1966][research_rhodes_johns_1966]
- [Rhudy 2016][research_rhudy_2016]
- [Riahi and Vonderwell 1994][research_riahi_vonderwell_1994]
- [Ribeiro et al 2022][research_ribeiro_yeh_2022]
- [Ribner 1960][research_ribner_1960]
- [Richardson 1968][research_richardson_1968]
- [Richardson 1968][research_richardson_1968_b]
- [Richardson 1976][research_richardson_1976]
- [Richardson et al 2003][research_richardson_davison_2003]
- [Rickard 1978][research_rickard_1978]
- [Ricketts 1985][research_ricketts_1985]
- [Ricketts and Doggett 1980][research_ricketts_1980]
- [Ricouard et al 2004][research_ricouard_davy_2004]
- [Riebe and Watson 1950][research_riebe_watson_1950]
- [Rieber and Allgöwer 2006][research_rieber_allgower_2006]
- [Rigid-Body Flight Dynamics 2026][research_rigid_body_flight_2026]
- [Rimer et al 1983][research_rimer_chipman_1983]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1984][research_rimer_chipman_1984_b]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Riou et al 2010][research_riou_garnier_2010]
- [Riso and Cesnik 2022][research_riso_cesnik_2022]
- [Riso et al 2018][research_riso_divincenzo_2018]
- [Ritchie 1973][research_ritchie_1973]
- [Ritter et al 2017][research_ritter_dillinger_2017]
- [Rivas-Padilla et al 2023][research_rivaspadilla_boston_2023]
- [Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]
- [Rizzi 1984][research_rizzi_1984]
- [Rizzo et al 2019][research_rizzo_serpieri_2019]
- [Ro et al 1992][research_ro_barlow_1992]
- [Roache 1965][research_roache_1965]
- [Robb et al 2023][research_robb_vuppala_2023]
- [Roberts 1965][research_roberts_1965]
- [Roberts et al 2012][research_roberts_reed_2012]
- [Robins et al 1983][research_robins_beissner_1983]
- [Robinson][research_robinson]
- [Robinson 2004][research_robinson_2004]
- [Robinson and Robinson 1980][research_robinson_robinson_1980]
- [Robinson et al 1990][research_robinson_batina_1990]
- [Rocha Da Costa][research_rochadacosta]
- [Rockwell 1994][research_rockwell_1994]
- [Rockwood et al 2019][research_rockwood_medina_2019]
- [Rodden 1989][research_rodden_1989]
- [Rodden 1989][research_rodden_1989_b]
- [Rodgers 1964][research_rodgers_1964]
- [Rodgers 1965][research_rodgers_1965]
- [Rodriguez 2007][research_rodriguez_2007]
- [Rogalski et al 2020][research_rogalski_rzucidlo_2020]
- [Rogers 1970][research_rogers_1970]
- [Rogers and Dunn 1952][research_rogers_1952]
- [Rokhsaz and Selberg 1989][research_rokhsaz_selberg_1989]
- [Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]
- [Romano et al 2017][research_romano_derosa_2017]
- [Romberg 2003][research_romberg_2003]
- [Rongqi and Jianmei 2013][research_rongqi_jianmei_2013]
- [Rongrong et al 2018][research_rongrong_zhengyin_2018]
- [Roos 1985][research_roos_1985]
- [Rose et al 1952][research_rose_jr_1952]
- [Rosen and Rand 1985][research_rosen_rand_1985]
- [Rosin et al 2004][research_rosin_mattos_2004]
- [Ross 1984][research_ross_1984]
- [Ross and Matarazzo 1982][research_ross_matarazzo_1982]
- [Rouaix][research_rouaix]
- [Roy and Mukherjee 2020][research_roy_mukherjee_2020]
- [Roysdon and Khalid 2010][research_roysdon_khalid_2010]
- [Roysdon and Khalid 2011][research_roysdon_khalid_2011]
- [Rozendaal 1986][research_rozendaal_1986]
- [Rozendaal 1987][research_rozendaal_1987]
- [Rozendaal and Behbehani 1990][research_rozendaal_behbehani_1990]
- [Rudenko and Ryzhkova 1968][research_rudenko_ryzhkova_1968]
- [Rudnick-Cohen et al 2020][research_rudnickcohen_hodson_2020]
- [Rudnick-Cohen et al 2022][research_rudnickcohen_hodson_2022]
- [Rudolph 1998 Mechanical Design of High Lift Systems for High Aspect Ratio Swept Wings][research_rudolph_1998]
- [Ruhlin and Pratt-Barlow 1981][research_ruhlin_prattbarlow_1981]
- [Runckel and Henderson 1952][research_runckel_henderson_1952]
- [Runckel and Hieser 1961][research_runckel_hieser_1961]
- [Runckel et al 1960][research_runckel_schmeer_1960]
- [Runyan and George-Falvy 1979][research_runyan_georgefalvy_1979]
- [Runyan and Steers 1980][research_runyan_steers_1980]
- [Runyan et al 1984][research_runyan_navran_1984]
- [Rusovici et al 2017][research_rusovici_haughey_2017]
- [Russell 1996][research_russell_1996]
- [Russell 1996][research_russell_1996_b]
- [Russo et al 2020][research_russo_tognaccini_2020]
- [Russo et al 2020][research_russo_tognaccini_2020_b]
- [Rutkowski 1977][research_rutkowski_1977]
- [Rutkowski 1979][research_rutkowski_1979]
- [Ruxandra Mihaela et al 2012][research_ruxandramihaela_samuel_2012]
- [Rymarz and Ramaprian 1995][research_rymarz_ramaprian_1995]
- [Röntsch et al 2016][research_rontsch_taubert_2016]
- [S and Gangamkote 2023][research_s_gangamkote_2023]
- [S. Elangovan et al. 2019][research_selangovanetal_2019]
- [Sabri et al 2022][research_sabri_elzaabalawy_2022]
- [Sacchi et al 2026][research_sacchi_sneddon_2026]
- [Sachs 1978][research_sachs_1978]
- [Sachs 1980][research_sachs_1980]
- [Sachs and Moelyadi 2006][research_sachs_moelyadi_2006]
- [Sachs et al 2021][research_sachs_gruter_2021]
- [Sachs et al 2021][research_sachs_gruter_2021_b]
- [Sacks et al 1963][research_sacks_nielsen_1963]
- [Sadoff et al 1954][research_sadoff_matteson_1954]
- [Saeed and Graham 2015][research_saeed_graham_2015]
- [Saeed et al 2016][research_saeed_mughal_2016]
- [Saelman 1964][research_saelman_1964]
- [Sager et al 1993][research_sager_1993]
- [Saitoh et al 1995][research_saitoh_hashidate_1995]
- [Saitoh et al 2012][research_saitoh_tamayama_2012]
- [Sakakibara et al 2021][research_sakakibara_nimura_2021]
- [Salahudden 2024][research_salahudden_2024]
- [Salahudden 2025][research_salahudden_2025]
- [Salahudden 2025][research_salahudden_2025_2]
- [Salahudden 2026][research_salahudden_2026]
- [Salahudden and Ghosh 2021][research_salahudden_2021]
- [Salahudden and Ghosh 2022][research_salahudden_ghosh_2022]
- [Salahudden and Ghosh 2022][research_salahudden_ghosh_2022_b]
- [Salahudden et al 2020][research_salahudden_dwivedi_2020]
- [Salahudden et al 2020][research_salahudden_giri_2020]
- [Salahudden et al 2021][research_salahudden_dwivedi_2021]
- [Salahudden et al 2022][research_salahudden_das_2022]
- [Salahudden et al 2023][research_salahudden_sanwale_2023]
- [Salahudden et al 2024][research_salahudden_singh_2024]
- [Salahudden et al 2025][research_salahudden_kumar_2025]
- [Salari and Roache 1990][research_salari_roache_1990]
- [Salem Said and Ragab 2008][research_salemsaid_ragab_2008]
- [Samareh et al 2007][research_samareh_chwalowski_2007]
- [Samikkannu 2011][research_samikkannu_2011]
- [Sammonds 1960][research_sammonds_1960]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Samuel and Mukherjee 2016][research_samuel_mukherjee_2016]
- [Samuels 1982][research_samuels_1982]
- [San and Fei 2012][research_san_fei_2012]
- [Sanchez et al 2019][research_sanchez_escamilla_2019]
- [Sanders 1965][research_sanders_1965]
- [Sanders et al 2003][research_sanders_eastep_2003]
- [Sandhu et al 2018][research_sandhu_soltani_2018]
- [Sandoz et al 2018][research_sandoz_ahuja_2018]
- [Sang][research_sang]
- [Sanghi et al 2024][research_sanghi_cesnik_2024]
- [Sankar et al 1985][research_sankar_malone_1985]
- [Santos and Mattos 2009][research_santos_mattos_2009]
- [Santos et al 2018][research_santos_sousa_2018]
- [Santos et al 2026][research_santos_marques_2026]
- [Saric 1996][research_saric_1996]
- [Saric 1997][research_saric_1997]
- [Saric 2010][research_saric_2010]
- [Saric and Yeates 1985][research_saric_yeates_1985]
- [Saric et al 1990][research_saric_dagenhart_1990]
- [Saric et al 2015][research_saric_west_2015]
- [Saric et al 2019][research_saric_west_2019]
- [Sartor and Timme 2016][research_sartor_timme_2016]
- [Sato 2013][research_sato_2013]
- [Sato 2014][research_sato_2014]
- [Sato 2018][research_sato_2018]
- [Sato 2022][research_sato_2022]
- [Saussié et al 2011][research_saussie_saydy_2011]
- [Savage and Edwards 1959][research_savage_1959]
- [Sawyer and Trant 1950][research_sawyer_trant_1950]
- [Sawyer et al 1951][research_sawyer_kennedy_1951]
- [Sboev D 2024][research_sboevd_2024]
- [Scallion 1952][research_scallion_1952]
- [Scanlan 1948][research_scanlan_1948]
- [Schade 1948][research_schade_1948]
- [Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]
- [Schairer 1941][research_schairer_1941]
- [Scher 1947][research_scher_1947]
- [Scher 1947][research_scher_1947_b]
- [Scher 1951][research_scher_1951]
- [Scher and Draper 1950][research_scher_draper_1950]
- [Scher and White 1977][research_scher_1977]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schewe and Mai 2019][research_schewe_mai_2019]
- [Schiavetta et al 2006][research_schiavetta_boelens_2006]
- [Schmeer and Cassetti 1960][research_schmeer_cassetti_1960]
- [Schmidt 1983][research_schmidt_1983]
- [Schmidt 1991][research_schmidt_1991]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt 2016][research_schmidt_2016_b]
- [Schmidt and Duren 2002][research_schmidt_duren_2002]
- [Schmidt et al 1988][research_schmidt_moore_1988]
- [Schmitt et al 1983][research_schmitt_destarac_1983]
- [Schneider 1956][research_schneider_1956]
- [Schneider 1976][research_schneider_1976]
- [Schneiter and Fischel 1948][research_schneiter_fischel_1948]
- [Schneiter and Watson 1948][research_schneiter_watson_1948]
- [Schorsch et al 2018][research_schorsch_nagel_2018]
- [Schuelein 2008][research_schuelein_2008]
- [Schuette and Hummel 2022][research_schuette_hummel_2022]
- [Schuette and Hummel 2024][research_schuette_hummel_2024]
- [Schuette et al 2018][research_schuette_vormweg_2018]
- [Schulderfrei et al 1951][research_schulderfrei_1951]
- [Schuster and Byrd 2003][research_schuster_byrd_2003]
- [Schweikert et al 2022][research_schweikert_patel_2022]
- [Schütte and Hummel 2025][research_schutte_hummel_2025]
- [Schütte et al 2018][research_schutte_huber_2018]
- [Scudder 1933][research_scudder_1933]
- [Scudder 1937][research_scudder_1937]
- [Scudder and Seidman 1935][research_scudder_seidman_1935]
- [Seacord and Campbell 1945][research_seacord_campbell_1945]
- [Sears 1974][research_sears_1974]
- [Sears 1980][research_sears_1980]
- [Sears 1990][research_sears_1990]
- [Secanell et al 2005][research_secanell_suleman_2005]
- [Sefcovic and Smith 2010][research_sefcovic_smith_2010]
- [Segui et al 2017][research_segui_gabor_2017]
- [Seidler et al 2023][research_seidler_huebner_2023]
- [Seidman 1942][research_seidman_1942]
- [Seidman and McAvoy 1940][research_seidman_mcavoy_1940]
- [Seigler and Neal 2009][research_seigler_neal_2009]
- [Seigler et al 2007][research_seigler_neal_2007]
- [Seitz et al 2011][research_seitz_kruse_2011]
- [Selberg and Vitt 1993][research_selberg_vitt_1993]
- [Selberg et al 1990][research_selberg_1990]
- [Selim et al 2021][research_selim_gowree_2021]
- [Semionov and Kosinov 2007][research_semionov_kosinov_2007]
- [Semionov et al 2006][research_semionov_kosinov_2006]
- [Semionov et al 2009][research_semionov_kosinov_2009]
- [Semionov et al 2011][research_semionov_kosinov_2011]
- [Semionov et al 2011][research_semionov_kosinov_2011_b]
- [Semionov et al 2013][research_semionov_kosinov_2013]
- [Semionov et al 2017][research_semionov_yermolaev_2017]
- [Semionov et al 2018][research_semionov_yermolaev_2018]
- [Semionov et al 2022][research_semionov_yermolaev_2022]
- [Sengupta and Dipankar 2005][research_sengupta_dipankar_2005]
- [Seraj and Martins 2023][research_seraj_martins_2023]
- [Seraj and Martins 2025][research_seraj_2025]
- [Sereez et al 2024][research_sereez_abramov_2024]
- [Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]
- [Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016]
- [Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016_b]
- [Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]
- [Setyo Hariyadi et al 2021][research_setyohariyadi_sutardi_2021]
- [Sforza 2014][research_sforza_2014]
- [Shafer 1975][research_shafer_1975]
- [Shah 2014][research_shah_2014]
- [Shah and Ang 2025][research_shah_ang_2025]
- [Shah et al 2003][research_shah_unnikrishnan_2003]
- [Shahjahan and Ahuja 2026][research_shahjahan_ahuja_2026]
- [Shahjahan et al 2026][research_shahjahan_enriquez_2026]
- [Shahriari et al 2018][research_shahriari_kollert_2018]
- [Shahzad et al 2012][research_shahzad_hamdani_2012]
- [Shamshurin 1974][research_shamshurin_1974]
- [Shankar 2013][research_shankar_2013]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shanks et al 2018][research_shanks_gale_2018]
- [Shanmugam et al 2016][research_shanmugam_raja_2016]
- [Shanmugam et al 2025][research_shanmugam_2025]
- [Shannon 1948][research_shannon_1948]
- [Shao et al 2017][research_shao_zhou_2017]
- [Shao et al 2022][research_shao_liu_2022]
- [Shao et al 2025][research_shao_zhang_2025]
- [Sharif et al 2022][research_sharif_abbas_2022]
- [Sharifi et al 2025][research_sharifi_2025]
- [Sharma et al 2025][research_sharma_rana_2025]
- [Shcherbakov 1966][research_shcherbakov_1966]
- [Shen 2026][research_shen_2026]
- [Shen and Mo 1996][research_shen_mo_1996]
- [Sherman 1937][research_sherman_1937]
- [Sherrow et al 2026][research_sherrow_hassen_2026]
- [Sheta 2004][research_sheta_2004]
- [Shevell 1978][research_shevell_1978]
- [Shi and Peng 2014][research_shi_peng_2014]
- [Shi and Peng 2015][research_shi_peng_2015]
- [Shi and Song 2012][research_shi_song_2012]
- [Shi and Wan 2015][research_shi_wan_2015]
- [Shields and Mohseni 2012][research_shields_mohseni_2012]
- [Shimomura][research_shimomura]
- [Shipul et al 2024][research_shipul_kosinov_2024]
- [Shitrit 2021][research_shitrit_2021]
- [Shivaji et al 2025][research_shivaji_basavaraju_2025]
- [Shmul et al 2018][research_shmul_erenthal_2018]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Shtin and Savelyev 2022][research_shtin_savelyev_2022]
- [Shue et al 1996][research_shue_sawan_1996]
- [Shue et al 1998][research_shue_agarwal_1998]
- [Shumsky 2006][research_shumsky_2006]
- [Si et al 2024][research_si_wu_2024]
- [Si et al 2025][research_si_2025]
- [Sibert 1943][research_sibert_1943]
- [Sibilski and Wróblewski 2012][research_sibilski_wroblewski_2012]
- [Sidoryuk and Khrabrov 2019][research_sidoryuk_khrabrov_2019]
- [Sihite et al 2023][research_sihite_salagame_2023]
- [Silsby and Kennedy 1947][research_silsby_kennedy_1947]
- [Silsby and Morris 1953][research_silsby_morris_1953]
- [Silsby et al 1950][research_silsby_morris_1950]
- [Silva][research_silva]
- [Silva][research_silva_b]
- [Silva et al 2023][research_silva_guimaraes_2023]
- [Sim and Curry 1978][research_sim_curry_1978]
- [Sim and Curry 1984][research_sim_curry_1984]
- [Sim and Curry 1985][research_sim_curry_1985]
- [Simmons and Freund 2005][research_simmons_freund_2005]
- [Simpson and Jacob 2005][research_simpson_jacob_2005]
- [Sims and Carter 1981][research_sims_carter_1981]
- [Simulation Requirements for Flight 2017][research_simulation_requirements_2017]
- [Singh 2024][research_singh_2024]
- [Singh and Chowdhury 2021][research_singh_chowdhury_2021]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singha 2025][research_singha_2025]
- [Singha and Murugan 2022][research_singha_murugan_2022]
- [Singha and Murugan 2023][research_singha_murugan_2023]
- [Singha and Murugan 2026][research_singha_murugan_2026]
- [Singha and Murugan 2026][research_singha_murugan_2026_b]
- [Sinha and Yuan 2026][research_sinha_yuan_2026]
- [Sinkovec et al 2015][research_sinkovec_loshek_2015]
- [Siouris and Qin 2007][research_siouris_qin_2007]
- [Sivanandi et al 2022][research_sivanandi_gupta_2022]
- [Skillen and Crossley 2005][research_skillen_crossley_2005]
- [Skillen and Crossley 2007][research_skillen_crossley_2007]
- [Skillen and Crossley 2008][research_skillen_crossley_2008]
- [Skillen and Crossley 2008][research_skillen_crossley_2008_b]
- [Skomorokhov et al 2014][research_skomorokhov_nikolay_2014]
- [Slater 1985][research_slater_1985]
- [Sleesongsom and Bureerat 2011][research_sleesongsom_bureerat_2011]
- [Sleesongsom et al 2013][research_sleesongsom_bureerat_2013]
- [Sliwa 1979][research_sliwa_1979]
- [Smith 1959][research_smith_1959]
- [Smith 1975][research_smith_1975_b]
- [Smith 1977][research_smith_1977]
- [Smith 1990][research_smith_1990]
- [Smith and Nelson 1988][research_smith_nelson_1988]
- [Smith and Schneider 1996][research_smith_schneider_1996]
- [Smith and Srokowski 1983][research_smith_srokowski_1983]
- [Smith et al 1971][research_smith_hammer_1971]
- [Smith et al 1973][research_smith_lebacqz_1973]
- [Smith et al 1975][research_smith_jones_1975]
- [Smith et al 1976][research_smith_1976]
- [Smith et al 1987][research_smith_cliff_1987]
- [Smith et al 1990][research_smith_zell_1990]
- [Smith et al 1992][research_smith_lock_1992]
- [Smith et al 1999][research_smith_kennelly_1999]
- [Smith et al 2007][research_smith_butt_2007]
- [Smith et al 2014][research_smith_lowenberg_2014]
- [Sneed et al 2007][research_sneed_smith_2007]
- [Snyder 1947][research_snyder_1947]
- [Snyder 1947][research_snyder_1947_b]
- [Snyder 1948][research_snyder_1948]
- [Snyder and Weisshaar 2013][research_snyder_weisshaar_2013]
- [Snyder et al 2009][research_snyder_sanders_2009]
- [Sobieczky et al 1987][research_sobieczky_hefer_1987]
- [Sofla et al 2010][research_sofla_meguid_2010]
- [Sofla et al 2010][research_sofla_meguid_2010_b]
- [Sohail et al 2011][research_sohail_muhammad_2011]
- [Sohn and Chung 2006][research_sohn_chung_2006]
- [Soistmann 1992][research_soistmann_1992]
- [Sol and Vos 2016][research_sol_vos_2016]
- [Solies 1995][research_solies_1995]
- [Soneda et al 2020][research_soneda_yokozeki_2020]
- [Soneda et al 2021][research_soneda_yokozeki_2021]
- [Soneda et al 2022][research_soneda_tsushima_2022]
- [Soneda et al 2023][research_soneda_tsushima_2023]
- [Soneda et al 2023][research_soneda_tsushima_2023_b]
- [Sonneveldt et al 2011][research_sonneveldt_chu_2011]
- [Soontornpasatch 2025][research_soontornpasatch_2025]
- [Sorbilli et al 2018][research_sorbilli_dibianchi_2018]
- [Sorenson 1974][research_sorenson_1974]
- [Sotoudeh and Ferman 2019][research_sotoudeh_ferman_2019]
- [Sotoudeh and Hosking 2018][research_sotoudeh_hosking_2018]
- [Sotoudeh et al 2010][research_sotoudeh_hodges_2010]
- [Souahi 1983][research_souahi_1983]
- [Sousa and Silva 2004][research_sousa_silva_2004]
- [Space environment natural and][research_space_environment]
- [Spacht 1980][research_spacht_1980]
- [Spain et al 1990][research_spain_soistmann_1990]
- [Spearman 1980][research_spearman_1980]
- [Spearman 2012][research_spearman_2012]
- [Spearman and Becht 1948][research_spearman_1948]
- [Spearman and Comisarow 1948][research_spearman_comisarow_1948]
- [Spearman and Driver 1959][research_spearman_driver_1959]
- [Speer et al 2004][research_speer_zhong_2004]
- [Spencer 1960][research_spencer_1960]
- [Spencer 1961][research_spencer_1961]
- [Spencer 1981][research_spencer_1981]
- [Spens and Bons 2022][research_spens_bons_2022]
- [Spens et al 2023][research_spens_mcfadden_2023]
- [Spreemann and Alford 1951][research_spreemann_1951]
- [Spreiter and Stahara 1970][research_spreiter_stahara_1970]
- [Springer 1996][research_springer_1996]
- [Squire 1975][research_squire_1975]
- [Squires 2002][research_squires_2002]
- [Srichitturi 2026][research_srichitturi_2026]
- [Srigrarom and Kurosaka 2000][research_srigrarom_kurosaka_2000]
- [Srinathkumar 2011][research_srinathkumar_2011]
- [Srinivas and Potti 2014][research_srinivas_potti_2014]
- [Srivastava et al 2025][research_srivastava_patel_2025]
- [Srokowski and Orszag 1977][research_srokowski_orszag_1977]
- [Stability Characteristics of Selected 2014][research_stability_characteristics_2014]
- [Stability, Control, and Handling 2024][research_stability_control_2024]
- [Stacey 2024][research_stacey_2024]
- [Stacey and Thomas 2019][research_stacey_thomas_2019]
- [Stacey and Thomas 2022][research_stacey_thomas_2022]
- [Stall Characteristics 2003][research_stall_characteristics_2003]
- [Stall Speed Measurement 2003][research_stall_speed_2003]
- [Stallings and Lamb 1981][research_stallingsjr_lamb_1981]
- [Stanbrook 1954][research_stanbrook_1954]
- [Standard Atmosphere 2005][research_standard_atmosphere_2005]
- [Standard Atmosphere 2023][research_standard_atmosphere_2023]
- [Standard Atmosphere 2024][research_standard_atmosphere_2024]
- [Standard atmosphere chart 1927][research_standard_atmosphere_1927]
- [Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]
- [Stanford and Ifju 2008][research_stanford_ifju_2008]
- [Stanford and Jacobson 2023][research_stanford_jacobson_2023]
- [Stark 1985][research_stark_1985]
- [Starn][research_starn]
- [Starossek 2021][research_starossek_2021]
- [Static Flight Stability and 2026][research_static_flight_2026]
- [Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]
- [Static Longitudinal Stability Theory 2003][research_static_longitudinal_2003_b]
- [Static Stability and Control][research_static_stability]
- [Static Stability and Control 2010][research_static_stability_2010]
- [Stebbins and Loth 2022][research_stebbins_loth_2022]
- [Stebbins and Loth 2023][research_stebbins_loth_2023]
- [Stebbins et al 2019][research_stebbins_loth_2019]
- [Steer 2003][research_steer_2003]
- [Steers 1981][research_steers_1981]
- [Stegmüller et al 2022][research_stegmuller_katzenmeier_2022]
- [Stegmüller et al 2026][research_stegmuller_haybock_2026]
- [Steimle et al 2008][research_steimle_schroder_2008]
- [Steimle et al 2010][research_steimle_schroder_2010]
- [Steimle et al 2012][research_steimle_karhoff_2012]
- [Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]
- [Stepanyan and Nguyen][research_stepanyan_nguyen]
- [Stephen 1995][research_stephen_1995]
- [Stephen and Sopirak 1994][research_stephen_sopirak_1994]
- [Stephenson 1956][research_stephenson_1956]
- [Stevens 1955][research_stevens_1955]
- [Stewart and Paulson 1984][research_stewart_paulsonjr_1984]
- [Stewartson 1981][research_stewartson_1981]
- [Stifel 1979][research_stifel_1979]
- [Stock 2005][research_stock_2005]
- [Stojakovic][research_stojakovic]
- [Stone and Berman 1946][research_stone_berman_1946]
- [Stone and Burk 1947][research_stone_1947]
- [Stone and Daughtridge 1948][research_stone_daughtridge_1948]
- [Stone and Klinar 1948][research_stone_1948]
- [Stough 1990][research_stough_1990]
- [Stough 1993][research_stough_1993]
- [Stough and Patton 1979][research_stough_1979]
- [Stough et al 1984][research_stough_dicarlo_1984]
- [Stough et al 1985][research_stough_dicarlo_1985]
- [Stough et al 1985][research_stough_jordan_1985]
- [Stough et al 1987][research_stough_1987]
- [Stough et al 1991][research_stough_1991]
- [Strayer and Manoharan 2025][research_strayer_manoharan_2025]
- [Streitenberger and Feldwisch 2025][research_streitenberger_feldwisch_2025]
- [Strickland et al 1990][research_strickland_tadios_1990]
- [Stringfield 1984][research_stringfield_1984]
- [Striz 1991][research_striz_1991]
- [Study on Flat Tail 2022][research_study_on_2022]
- [Sturm et al 2019][research_sturm_achleitner_2019]
- [Su 2026][research_su_2026]
- [Su et al 2016][research_su_swei_2016]
- [Su et al 2018][research_su_wang_2018]
- [Suardi et al 2020][research_suardi_pinelli_2020]
- [Suarez et al 1992][research_suarez_kramer_1992]
- [Suarez et al 1993][research_suarez_smith_1993]
- [Subaschandar and Prabhu 2002][research_subaschandar_prabhu_2002]
- [Subramanian 2026][research_subramanian_2026]
- [Sudhi et al 2021][research_sudhi_radespiel_2021]
- [Sugimoto 1992][research_sugimoto_1992]
- [Sugiura et al 2001][research_sugiura_yoshida_2001]
- [Sui 2022][research_sui_2022]
- [Suleman 2007][research_suleman_2007]
- [Summers 1953][research_summers_1953]
- [Sun et al 2022][research_sun_li_2022]
- [Sun et al 2024][research_sun_zhou_2024]
- [Sun et al 2026][research_sun_2026]
- [Sundaram et al 1999][research_sundaram_viswanath_1999]
- [Sutherland 1893][research_sutherland_1893]
- [Sutton 1959][research_sutton_1959]
- [Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]
- [Svoboda 1999][research_svoboda_1999]
- [Svoboda and Rozehnal 2015][research_svoboda_rozehnal_2015]
- [Svoboda et al 2018][research_svoboda_hromcik_2018]
- [Svoboda et al 2023][research_svoboda_hengstermovric_2023]
- [Swaim 1961][research_swaim_1961]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swihart and Goodman 1965][research_swihart_goodman_1965]
- [Swihart and Goodmanson 1964][research_swihart_goodmanson_1964]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022_b]
- [Syverud et al 1993][research_syverud_farokhi_1993]
- [Szema and Shankar 1984][research_szema_shankar_1984]
- [Szilder and Lozowski 2018][research_szilder_lozowski_2018]
- [Szmelter 1999][research_szmelter_1999]
- [Szodruch 1991][research_szodruch_1991]
- [Szodruch and Hilbig 1988][research_szodruch_hilbig_1988]
- [Szymanski et al 2025][research_szymanski_ghazi_2025]
- [Séraudie et al 2003][research_seraudie_perraud_2003]
- [Sóbester 2021][research_sobester_2021]
- [Tagai et al 2016][research_tagai_nakakita_2016]
- [Tai 1991][research_tai_1991]
- [Tai et al 2023][research_tai_wang_2023]
- [Taira et al 2010][research_taira_rowley_2010]
- [Taisul Ahn et al][research_taisulahn_hyoungjinkim]
- [Takahashi and Barchfeld 2016][research_takahashi_barchfeld_2016]
- [Takahashi and Donovan 2011][research_takahashi_donovan_2011]
- [Takahashi et al 2014][research_takahashi_dulin_2014]
- [Takahashi et al 2019][research_takahashi_boccieri_2019]
- [Takanashi 1984][research_takanashi_1984]
- [Takarics et al 2020][research_takarics_mocsanyi_2020]
- [Takeda 1970][research_takeda_1970]
- [Tal and Nguyen 2015][research_tal_nguyen_2015]
- [Tamayo][research_tamayo]
- [Tamura and Yumitori 2024][research_tamura_yumitori_2024]
- [Tan][research_tan]
- [Tan et al 2017][research_tan_wang_2017]
- [Tancredi and Corraro 2012][research_tancredi_corraro_2012]
- [Tandale et al 2004][research_tandale_rong_2004]
- [Tang and Dowell 2008][research_tang_dowell_2008]
- [Tang et al 2007][research_tang_liu_2007]
- [Tang et al 2023][research_tang_che_2023]
- [Tang et al 2024][research_tang_shi_2024]
- [Tao et al 2019][research_tao_sun_2019]
- [Tapolcai et al 2012][research_tapolcai_omran_2012]
- [Tarabi et al 2015][research_tarabi_ghasemloo_2015]
- [tarabi et al 2016][research_tarabi_ghasemloo_2016]
- [Tarnowski 2017][research_tarnowski_2017]
- [Tasci and Ozdemir 2025][research_tasci_ozdemir_2025]
- [Taufik and Qasem 2025][research_taufik_qasem_2025]
- [Tavoularis 1999][research_tavoularis_1999]
- [Taylor 1952][research_taylor_1952]
- [Taylor 1953][research_taylor_1953]
- [Taylor 1959][research_taylor_1959]
- [Taylor and Gursul 2004][research_taylor_gursul_2004]
- [Taylor and Gursul 2004][research_taylor_gursul_2004_b]
- [Taylor and Hunsaker 2023][research_taylor_hunsaker_2023]
- [Taylor and Miller 1982][research_taylor_miller_1982]
- [Taylor et al 1982][research_taylor_jackson_1982]
- [Taylor et al 1997][research_taylor_peake_1997]
- [Tchatchueng Kammegne et al 2016][research_tchatchuengkammegne_botez_2016]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Telionis 1990][research_telionis_1990]
- [Telionis 1995][research_telionis_1995]
- [Telionis 2001][research_telionis_2001]
- [Telionis and Vlachos 2003][research_telionis_vlachos_2003]
- [Temgoua Dongmo and Kwatny][research_temgouadongmo_kwatny]
- [Tempelmann et al 2011][research_tempelmann_schrader_2011]
- [Tempelmann et al 2012][research_tempelmann_hanifi_2012]
- [Tempelmann et al 2012][research_tempelmann_schrader_2012]
- [Tempelmeyer and Osborne 1954][research_tempelmeyer_osborne_1954]
- [Teofilatto 2001][research_teofilatto_2001]
- [Teper and Stapleford 1965][research_teper_stapleford_1965]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Test Techniques for Flight 2021][research_test_techniques_2021]
- [Tewes and Taubert 2015][research_tewes_taubert_2015]
- [The effects of aft-loaded 1989][research_the_effects_1989]
- [The effects of canard-wing 1988][research_the_effects_1988]
- [The Flight Environment Standard 2021][research_the_flight_2021]
- [The International Standard Atmosphere 2017][research_the_international_2017]
- [The international standard atmosphere 2026][research_the_international_2026]
- [The Mission Adaptive Wing 1986][research_the_mission_1986]
- [The stability of the 1979][research_the_stability_1979]
- [The stability of two-phase 1997][research_the_stability_1997]
- [The Standard Atmosphere 1964][research_the_standard_1964]
- [The Standard Atmosphere 1976][research_the_standard_1976]
- [The sweep angle effect 2018][research_the_sweep_angle_2018]
- [The Swept - Wing 2021][research_the_swept_2021]
- [The Tapered Wing Again 1937][research_the_tapered_1937]
- [The Wing Structure and 2013][research_the_wing_2013]
- [Thelander 1965][research_thelander_1965]
- [Theodorsen 1979][research_theodorsen_1935]
- [Theofilis 1998][research_theofilis_1998]
- [Theofilis and Dallmann 1997][research_theofilis_dallmann_1997]
- [Theofilis et al 1990][research_theofilis_duck_1990]
- [Thomas and Wolhart 1957][research_thomas_wolhart_1957]
- [Thomas et al 2016][research_thomas_mughal_2016]
- [Thomas et al 2017][research_thomas_mughal_2017]
- [Thompson 1965][research_thompson_1965]
- [Thornton 1993][research_thornton_1993]
- [Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]
- [Three-Dimensional Wing Synthesis 2014][research_three_dimensional_wing_2014]
- [Thrust-induced effects on pitching-up 1994][research_thrust_induced_effects_1994]
- [Thurber 1965][research_thurber_1965]
- [Thurston 1934][research_thurston_1934]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2024][research_tian_zhang_2024]
- [Tian et al 2025][research_tian_huang_2025]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Ting et al 2014][research_ting_nguyen_2014]
- [Tiniakov and Limtrakul 2026][research_tiniakov_2026]
- [Tischler 2018][research_tischler_2018]
- [Tischler 2018][research_tischler_2018_b]
- [Tischler and Barlow 1979][research_tischler_barlow_1979]
- [Tischler and Barlow 1980][research_tischler_barlow_1980]
- [Tischler and Barlow 1980][research_tischler_barlow_1980_b]
- [Tischler and Barlow 1981][research_tischler_barlow_1981]
- [Tischler and Barlow 1982][research_tischler_barlow_1982]
- [Tjatra et al 1992][research_tjatra_kapania_1992]
- [Todorov 2015][research_todorov_2015]
- [Tokugawa and Yoshida 2006][research_tokugawa_yoshida_2006]
- [Tolkachev et al 2022][research_tolkachev_kiselev_2022]
- [Tolkachev et al 2024][research_tolkachev_baranov_2024]
- [Toll 1962][research_toll_1962]
- [Toll and Queijo 1948][research_toll_queijo_1948]
- [Tomczyk 2001][research_tomczyk_2001]
- [Tomczyk 2002][research_tomczyk_2002]
- [Tomczyk 2008][research_tomczyk_2008]
- [Tomczyk 2008][research_tomczyk_2008_b]
- [Tomek et al 2020][research_tomek_ullah_2020]
- [Tong and Ji 2013][research_tong_ji_2013]
- [Tong and Ji 2014][research_tong_ji_2014]
- [Torenbeek 1972][research_torenbeek_1972]
- [Torenbeek 1976][research_torenbeek_1976]
- [Torenbeek 1982][research_torenbeek_1982]
- [Tormalm et al 2018][research_tormalm_leroy_2018]
- [Torrigiani and Berci 2021][research_torrigiani_berci_2021]
- [Tosti 1947][research_tosti_1947]
- [Touzani 1987][research_touzani_1987]
- [Townsend et al 2018][research_townsend_stanford_2018]
- [Toyoda et al 2015][research_toyoda_kwak_2015]
- [Transfer of German High-Speed 2010 Transfer of German High-Speed Aerodynamics After 1945][research_transfer_of_2010]
- [Transonic Aerodynamics 1982][research_transonic_aerodynamics_1982]
- [Transonic Aerodynamics-History and Statement 1982][research_transonic_aerodynamics_history_1982]
- [Transonic Computational Experience for 1982][research_transonic_computational_1982]
- [Transonic Design Using Computational 1982][research_transonic_design_1982]
- [Transonic flight test of 1994][research_transonic_flight_1994]
- [Transonic Wing Shape Design 2015][research_transonic_wing_2015]
- [Traub 1994][research_traub_1994]
- [Traub 1995][research_traub_1995]
- [Traub 1997][research_traub_1997]
- [Traub 1997][research_traub_1997_b]
- [Traub 1997][research_traub_1997_c]
- [Traub 2000][research_traub_2000]
- [Traub 2009][research_traub_2009]
- [Traub 2019][research_traub_2019]
- [Traub 2021][research_traub_2021]
- [Traub 2023][research_traub_2023]
- [Traub and Campbell 2019][research_traub_campbell_2019]
- [Traub and Chandrashekar 2016][research_traub_chandrashekar_2016]
- [Traub et al 1999][research_traub_galls_1999]
- [Travassos et al 1980][research_travassos_gupta_1980]
- [Trenka et al 1963][research_trenka_white_1963]
- [Trim Drag and Maneuvering 2010][research_trim_drag_2010]
- [Triplett 1980][research_triplett_1980]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Trussa et al 2021][research_trussa_whitfield_2021]
- [Trussa et al 2022][research_trussa_whitfield_2022]
- [Trussa et al 2026][research_trussa_whitfield_2026]
- [Tsao et al 2009][research_tsao_vargas_2009]
- [Tseng 1990][research_tseng_1990]
- [Tsushima et al 2018][research_tsushima_yokozeki_2018]
- [Tsushima et al 2019][research_tsushima_2019]
- [Tsushima et al 2019][research_tsushima_arizono_2019]
- [Tsushima et al 2020][research_tsushima_arizono_2020]
- [Tsushima et al 2020][research_tsushima_tamayama_2020]
- [Tu 1992][research_tu_1992]
- [Tu 1992][research_tu_1992_b]
- [Tucker et al 2014][research_tucker_saric_2014]
- [Tufts et al 2013][research_tufts_reed_2013]
- [Tufts et al 2014][research_tufts_reed_2014]
- [Tufts et al 2014][research_tufts_suffixjrsuffix_2014]
- [Tufts et al 2015][research_tufts_reed_2015]
- [Tumlinson et al 1981][research_tumlinson_holcomb_1981]
- [Tupy and Zelinka 2008][research_tupy_zelinka_2008]
- [Turbeville and Schneider 2018][research_turbeville_schneider_2018]
- [Turner 1950][research_turner_1950]
- [Turner 1981][research_turner_1981]
- [Turns and Kraige][research_turns_kraige]
- [Tursi 2003][research_tursi_2003]
- [Tzong et al 1992][research_tzong_sikes_1992]
- [Udin and Anderson 1992][research_udin_anderson_1992]
- [Ueno et al 1998][research_ueno_matsuno_1998]
- [Ukolov and Gamboa 2026][research_ukolov_gamboa_2026]
- [Ullah and Devi 1973][research_ullah_devi_1973]
- [Ullah et al 2021][research_ullah_fabijanic_2021]
- [Ullah et al 2021][research_ullah_tomek_2021]
- [Ullah et al 2022][research_ullah_fabijanic_2022]
- [Unangst 1959][research_unangst_1959]
- [Unger and Coen 1993][research_unger_coen_1993]
- [Unsteady Aerodynamics and Flutter 2006][research_unsteady_aerodynamics_2006]
- [Unsteady Transonic Aerodynamics 1989][research_unsteady_transonic_1989]
- [Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]
- [US Standard Atmosphere Model 2014][research_us_standard_2014]
- [Use of Aerodynamic Forces 2022][research_use_of_2022]
- [Ustinov 2001][research_ustinov_2001]
- [Ustinov 2013][research_ustinov_2013]
- [Ustinov 2017][research_ustinov_2017]
- [Ustinov 2018][research_ustinov_2018]
- [Ustinov 2018][research_ustinov_2018_b]
- [Ustinov 2021][research_ustinov_2021]
- [Utaka 2004][research_utaka_2004]
- [Utsch and Rockwell 1990][research_utsch_rockwell_1990]
- [Uzun 2025][research_uzun_2025]
- [Uzun and Oktay 2023][research_uzun_oktay_2023]
- [Uzun et al 2023][research_uzun_bilgic_2023]
- [Valasek et al 2009][research_valasek_lampton_2009]
- [Valasek et al 2012][research_valasek_kirkpatrick_2012]
- [Vale and Albuquerque 2025][research_vale_albuquerque_2025]
- [Vale et al 2011][research_vale_leite_2011]
- [Vale et al 2013][research_vale_lau_2013]
- [Valenti and Stanton 2024][research_valenti_stanton_2024]
- [van Dam 1985][research_vandam_1985]
- [Van Dam 1986][research_vandam_1986]
- [Van Dam et al 1980][research_vandam_holmes_1980]
- [van Dam et al 1981][research_vandam_holmes_1981]
- [Van Dam et al 1990][research_vandam_vijgen_1990]
- [Van Den Berg et al 1975][research_vandenberg_elsenaar_1975]
- [Van der Velden 1987][research_vandervelden_1987]
- [Van Der Velden 1992][research_vandervelden_1992]
- [Van der Velden and Kroo 1994][research_vandervelden_kroo_1994]
- [van der Velden and Torenbeek 1989][research_vandervelden_torenbeek_1989]
- [van Dommelen et al 2019][research_vandommelen_dsilva_2019]
- [van Es 2002][research_vanes_2002]
- [Van Thullenar 1957][research_vanthullenar_1957]
- [Vandervelden 1989][research_vandervelden_1989]
- [Vandervelden and Kroo 1990][research_vandervelden_kroo_1990]
- [Vandierendonck 1973][research_vandierendonck_1973]
- [Vargas 2007][research_vargas_2007]
- [Vargas and Kreeger 2009][research_vargas_kreeger_2009]
- [Vargas et al 2002][research_vargas_ratvasky_2002]
- [Variable sweep today 1965][research_variable_sweep_1965]
- [Variable sweep wing design 1980][research_variable_sweep_1980]
- [Vasile et al 2010][research_vasile_elimelech_2010]
- [Vasista et al 2016][research_vasista_degaspari_2016]
- [Vasista et al 2017][research_vasista_riemenschneider_2017]
- [Vatandas 2010][research_vatandas_2010]
- [Vaughan 2003][research_vaughan_2003]
- [Vaughan and Wood 1995][research_vaughan_wood_1995]
- [Vavra et al 2005][research_vavra_solomon_2005]
- [Vazquez et al 2020][research_vazquez_joshi_2020]
- [Veerman et al 2013][research_veerman_kannemans_2013]
- [Velkova and Todorov 2015][research_velkova_todorov_2015]
- [Venkatakrishnan et al 2006][research_venkatakrishnan_sundaram_2006]
- [Venkateswara Rao and Go 2019][research_rao_spin_2019]
- [Vepa 2008][research_vepa_2008]
- [Vepa 2023][research_vepa_2023]
- [Vepa 2023][research_vepa_2023_b]
- [Vepa 2023][research_vepa_2023_c]
- [Vepa 2023][research_vepa_2023_d]
- [Vermeersch et al 2015][research_vermeersch_yoshida_2015]
- [Verrastro and Metge 2015][research_verrastro_metge_2015]
- [Videan 1955][research_videan_1955]
- [Viglietti et al 2019][research_viglietti_zappino_2019]
- [Vigliotti and Pasini 2018][research_vigliotti_pasini_2018]
- [Viken et al 1990][research_viken_collier_1990]
- [Vinayagamurthy et al 2011][research_vinayagamurthy_parammasivam_2011]
- [Vincent 1991][research_vincent_1991]
- [Vindigni 2023][research_vindigni_2023]
- [Visbal and Garmann 2018][research_visbal_garmann_2018]
- [Visbal and Garmann 2019][research_visbal_garmann_2019]
- [Visbal and Gordnier 1995][research_visbal_gordnier_1995]
- [Vishwanathan][research_vishwanathan]
- [Visonneau et al 2015][research_visonneau_guilmineau_2015]
- [Visonneau et al 2022][research_visonneau_guilmineau_2022]
- [Vocke et al 2011][research_vocke_kothera_2011]
- [Vocke III et al 2012][research_vockeiii_s_2012]
- [Vogeltanz 2016][research_vogeltanz_2016]
- [Vogler 1976][research_vogler_1976]
- [Vogler and Turner 1956 Wind-tunnel investigation at transonic speeds of a jet control on a 35 degree swept wing, transonic-bump method][research_vogler_1956]
- [Von Glahn and Groesbeck 1976][research_vonglahn_groesbeck_1976]
- [Vonderwell and Riahi 1998][research_vonderwell_riahi_1998]
- [Voracek 2007][research_voracek_2007]
- [Vos and Farokhi 2015][research_vos_farokhi_2015]
- [Vos et al 2007][research_vos_debreuker_2007]
- [Vos et al 2010][research_vos_gurdal_2010]
- [Voss 2018][research_voss_2018]
- [Vu][research_vu]
- [Waggoner 1986][research_waggoner_1986]
- [Waggoner and Allison 1987][research_waggoner_allison_1987]
- [Waggoner et al 1985][research_waggoner_campbell_1985]
- [Waggoner et al 1985][research_waggoner_phillips_1985]
- [Waggoner et al 1986][research_waggoner_campbell_1986]
- [Waggoner et al 1987][research_waggoner_campbell_1987]
- [Wagner et al 1986][research_wagner_fisher_1986]
- [Wagner et al 1988][research_wagner_bartlett_1988]
- [Wagner et al 1988][research_wagner_maddalon_1988]
- [Wagner et al 1992][research_wagner_maddalon_1992]
- [Wakayama and Kroo 1995][research_wakayama_kroo_1995]
- [Wakimoto et al 2021][research_wakimoto_chiba_2021]
- [Walchli 1994][research_walchli_1994]
- [Walchli et al 1992][research_walchli_guyton_1992]
- [Waldmann et al 2023][research_waldmann_ehrle_2023]
- [Wales et al 2015][research_wales_cheung_2015]
- [Walker and Bons 2018][research_walker_bons_2018]
- [Walker et al 2016][research_walker_hipp_2016]
- [Walkley 1986][research_walkley_1986]
- [Wallace 1952][research_wallace_1952]
- [Wallis et al 1982][research_wallis_ellis_1982]
- [Wan 2024][research_wan_2024]
- [Wan et al 2003][research_wan_yang_2003]
- [Wang][research_wang]
- [Wang 1979][research_wang_1979]
- [Wang 2019][research_wang_2019]
- [Wang 2024][research_wang_2024]
- [Wang 2024][research_wang_2024_b]
- [Wang 2025][research_wang_2025]
- [Wang 2025][research_wang_2025_b]
- [Wang 2026][research_wang_2026_b]
- [Wang and Guo 2024][research_wang_guo_2024_b]
- [Wang and Niu 2026][research_wang_2026_4]
- [Wang and Tu 2010][research_wang_tu_2010]
- [Wang and Zha 2019][research_wang_zha_2019]
- [Wang and Zhan 2005][research_wang_zhan_2005]
- [Wang et al 1994][research_wang_herbert_1994]
- [Wang et al 1994][research_wang_herbert_1994_b]
- [Wang et al 2013][research_wang_bai_2013]
- [Wang et al 2013][research_wang_qin_2013]
- [Wang et al 2015][research_wang_dong_2015]
- [Wang et al 2016][research_wang_dong_2016]
- [Wang et al 2016][research_wang_xu_2016]
- [Wang et al 2018][research_wang_su_2018]
- [Wang et al 2019][research_wang_gong_2019]
- [Wang et al 2021][research_wang_hou_2021]
- [Wang et al 2022][research_wang_tai_2022]
- [Wang et al 2023][research_wang_chen_2023]
- [Wang et al 2023][research_wang_hou_2023]
- [Wang et al 2023][research_wang_qian_2023]
- [Wang et al 2023][research_wang_yu_2023]
- [Wang et al 2024][research_wang_guo_2024]
- [Wang et al 2024][research_wang_sun_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2024][research_wang_zhao_2024]
- [Wang et al 2025][research_wang_duan_2025]
- [Wang et al 2025][research_wang_sun_2025]
- [Wang et al 2025][research_wang_tu_2025]
- [Wang et al 2025][research_wang_zeng_2025]
- [Wang et al 2026][research_wang_2026]
- [Wang et al 2026][research_wang_2026_2]
- [Wang et al 2026][research_wang_2026_3]
- [Wang et al 2026][research_wang_jia_2026]
- [Wang et al 2026][research_wang_liu_2026]
- [Wang et al 2026][research_wang_tu_2026]
- [Ward 1949][research_ward_1949]
- [Ward et al 1976][research_ward_bennett_1976]
- [Warren et al 1997][research_warren_hassan_1997]
- [Warwick et al 2019][research_warwick_bras_2019]
- [Wasserman and Mitchell 1973][research_wasserman_mitchell_1973]
- [Waszak and Buttrill 1991][research_waszak_buttrill_1991]
- [Waszak and Srinathkumar 1992][research_waszak_srinathkumar_1992]
- [Watanabe et al 2021][research_watanabe_sunada_2021]
- [Waters et al 1992][research_waters_ardema_1992]
- [Weatherill and Ehlers 1989][research_weatherill_ehlers_1989]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Webb et al 1988][research_webb_mccain_1988]
- [Weber 1990][research_weber_1990]
- [Weed et al 1983][research_weed_carlson_1983]
- [Weed et al 1984][research_weed_carlson_1984]
- [Wei et al 2019][research_wei_new_2019]
- [Wei et al 2026][research_wei_tong_2026]
- [Weil and Morrison 1953][research_weil_1953]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weisshaar 1974][research_weisshaar_1974]
- [Weisshaar 1975][research_weisshaar_1975]
- [Weisshaar 1976][research_weisshaar_1976]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1979][research_weisshaar_1979_b]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1983][research_weisshaar_1983]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar 1990][research_weisshaar_1990]
- [Weisshaar 1994][research_weisshaar_1994]
- [Weisshaar 2013][research_weisshaar_2013]
- [Weisshaar and Ashley 1973][research_weisshaar_ashley_1973]
- [Weisshaar and Ashley 1974][research_weisshaar_ashley_1974]
- [Weisshaar and Crittenden 1976][research_weisshaar_crittenden_1976]
- [Weisshaar and Schmidt 1981][research_weisshaar_schmidt_1981]
- [Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]
- [Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]
- [Weissman 1969][research_weissman_1969]
- [Weissman 1973][research_weissman_1973]
- [Weissman 1975][research_weissman_1975]
- [Wells and Olson 2011][research_wells_olson_2011]
- [Wen et al 2013][research_wen_deng_2013]
- [Wentz and Nyenhuis 1984][research_wentzjr_nyenhuis_1984]
- [Wentz et al 1985][research_wentz_ahmed_1985]
- [Wenzinger and Harris 1931][research_wenzinger_harris_1931]
- [Werner et al 2022][research_werner_schutte_2022]
- [Werner et al 2024][research_werner_henne_2024]
- [Werter and De Breuker 2015][research_werter_debreuker_2015]
- [West 1960 Effect of Body-Mounted Lateral Controls and Speed Brakes on the Aerodynamic Load Distribution over a 45 deg Swept Wing at Mach Numbers from 0.80][research_west_1960]
- [Westfall et al 2007][research_westfall_canfield_2007]
- [Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]
- [Whipple 1980][research_whipple_1980]
- [Whipple 1982][research_whipple_1982]
- [Whipple and White 1984][research_whipple_1984]
- [Whitcomb 1956][research_whitcomb_1956]
- [Whitcomb 1983][research_whitcomb_1983]
- [Whitcomb and Norton 1961][research_whitcomb_1961]
- [Whitcomb et al 1961][research_whitcomb_critzos_1961]
- [White 1947][research_white_1947]
- [White 1970][research_white_1970]
- [White 1985][research_white_1985]
- [White 1985][research_white_1985_b]
- [White and Bowman 1982][research_white_bowman_1982]
- [White and Crimi 1961][research_white_crimi_1961]
- [White et al 2001][research_white_saric_2001]
- [White et al 2015][research_white_kapania_2015]
- [Whitlow 1993][research_whitlow_1993]
- [Whittle and Lipson 1953][research_whittle_lipson_1953]
- [Whittle and Lipson 1954][research_whittle_lipson_1954]
- [Wickenheiser and Garcia 2012][research_wickenheiser_garcia_2012]
- [Widowati et al 2012][research_widowati_riyanto_2012]
- [Wieszala et al 2022][research_wieszala_kolodziej_2022]
- [Wiggins and Kuhn 1953][research_wiggins_kuhn_1953]
- [Wiggins et al 2004][research_wiggins_stubbs_2004]
- [Wilbur et al 2018][research_wilbur_mistry_2018]
- [Wild 2013][research_wild_2013]
- [Wildschek 2014][research_wildschek_2014]
- [Wildschek et al 2008][research_wildschek_judas_2008]
- [Wildschek et al 2009][research_wildschek_maier_2009]
- [Wiler and White 1984][research_wiler_white_1984]
- [Wiler and White 1985][research_wiler_white_1985]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Willen 1975][research_willen_1975]
- [Williams and DiCamillo 1959][research_williams_dicamillo_1959]
- [Wilmott 1986][research_wilmott_1986]
- [Wind Tunnel Test to 2004][research_wind_tunnel_2004]
- [Wing Design 2012][research_wing_design_2012]
- [Wing Design 2025][research_wing_design_2025]
- [Wing Design Considerations 2021][research_wing_design_2021]
- [Wing Loads 1996][research_wing_loads_1996]
- [Wing Morphing Design Using 2013][research_wing_morphing_2013]
- [Wing Shapes and Nomenclature 2022][research_wing_shapes_2022]
- [Wing tunnel model for 1998][research_wing_tunnel_1998]
- [Wings 2017][research_wings_2017]
- [Winkelman and Barlow 1980][research_winkelman_barlow_1980]
- [Winkelmann 1989][research_winkelmann_1989]
- [Winski et al][research_winski_langston]
- [Winski et al 2025][research_winski_langston_2025]
- [Wintzer et al 2006][research_wintzer_sturdza_2006]
- [Wise 1992][research_wise_1992]
- [Witkowski et al 2022][research_witkowski_williams_2022]
- [Wittmann et al 2009][research_wittmann_steiner_2009]
- [Wlezien et al 1998][research_wlezien_horner_1998]
- [Woan and Chakravarthy 1988][research_woan_chakravarthy_1988]
- [Woldhuis et al 2026][research_woldhuis_asaro_2026]
- [Wolhart 1951][research_wolhart_1951]
- [Wolkovitch 1984][research_wolkovitch_1984]
- [Wong and va 1995][research_wong_va_1995]
- [Wong et al 1993][research_wong_rock_1993]
- [Wong et al 2022][research_wong_bil_2022]
- [Woo 1992][research_woo_1992]
- [Wood 1946][research_wood_1946]
- [Woodard and Bragg 2020][research_woodard_bragg_2020]
- [Wooden et al 2007][research_wooden_smith_2007]
- [Woodruff et al 2011][research_woodruff_saric_2011]
- [Woods and Spooner 1948][research_woods_spooner_1948]
- [Woods and Wood 2000][research_woods_wood_2000]
- [Woods et al 1989][research_woods_gilbert_1989]
- [Woods et al 2013][research_woods_wereley_2013]
- [Wortman 1999][research_wortman_1999]
- [Wright 1936][research_wright_1936]
- [Wright and Loving 1953][research_wright_loving_1953]
- [Wu and Squires 1995][research_wu_squires_1995]
- [Wu and Xu 2023][research_wu_xu_2023]
- [Wu et al 2013][research_wu_dai_2013]
- [Wu et al 2016][research_wu_lu_2016]
- [Wu et al 2017][research_wu_lu_2017]
- [Wu et al 2017][research_wu_xiao_2017]
- [Wu et al 2018][research_wu_xiao_2018]
- [Wu et al 2021][research_wu_tan_2021]
- [Wu et al 2023][research_wu_hu_2023]
- [Wu et al 2024][research_wu_huang_2024]
- [Wu et al 2026][research_wu_cai_2026]
- [Wu et al 2026][research_wu_cai_2026_b]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017_b]
- [Xi et al 2025][research_xi_dai_2025]
- [Xia et al 1993][research_xia_zhu_1993]
- [Xia et al 2014][research_xia_ajaj_2014]
- [Xia et al 2023][research_xia_jing_2023]
- [Xiang et al 2018][research_xiang_liu_2018]
- [Xiao et al 2019][research_xiao_chen_2019]
- [Xiao et al 2023][research_xiao_guo_2023]
- [Xiaolong He et al 2017][research_xiaolonghe_junqiangbai_2017]
- [Xie et al 2022][research_xie_chen_2022]
- [Xie et al 2026][research_xie_cai_2026]
- [Xijuan et al 2016][research_xijuan_qiang_2016]
- [Xin and Li 2025][research_xin_li_2025]
- [Xinbing et al 2019][research_xinbing_wen_2019]
- [Xinbing et al 2020][research_xinbing_wen_2020]
- [Xiong and Liu 2013][research_xiong_liu_2013]
- [Xiong and Nguyen 2023][research_xiong_nguyen_2023_b]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024]
- [Xiong and Yang 2001][research_xiong_yang_2001]
- [Xiong et al 2021][research_xiong_bartels_2021]
- [Xiong et al 2022][research_xiong_nguyen_2022]
- [Xiong et al 2022][research_xiong_nguyen_2022_b]
- [Xiong et al 2022][research_xiong_nguyen_2022_c]
- [Xiong et al 2023][research_xiong_nguyen_2023]
- [Xiong et al 2026][research_xiong_nguyen_2026]
- [Xu 2012][research_xu_2012]
- [Xu and Amano 2004][research_xu_amano_2004]
- [Xu and Wu 2022][research_xu_wu_2022]
- [Xu and Zhou 2015][research_xu_zhou_2015]
- [Xu et al 2012][research_xu_yang_2012]
- [Xu et al 2012][research_xu_yang_2012_b]
- [Xu et al 2013][research_xu_deng_2013]
- [Xu et al 2016][research_xu_yue_2016]
- [Xu et al 2018][research_xu_lu_2018]
- [Xu et al 2018][research_xu_zhang_2018]
- [Xu et al 2019][research_xu_chen_2019]
- [Xu et al 2019][research_xu_han_2019]
- [Xu et al 2019][research_xu_han_2019_b]
- [Xu et al 2021][research_xu_han_2021]
- [Xu et al 2021][research_xu_he_2021]
- [Xu et al 2022][research_xu_li_2022]
- [Xu et al 2022][research_xu_li_2022_b]
- [Xu et al 2023][research_xu_li_2023]
- [xu et al 2023][research_xu_song_2023]
- [Xu et al 2025][research_xu_song_2025]
- [Xu et al 2025][research_xu_zhang_2025]
- [Xu et al 2026][research_xu_2026]
- [Xu et al 2026][research_xu_lessis_2026]
- [Xu et al 2026][research_xu_song_2026]
- [Xue et al 2019][research_xue_ye_2019]
- [Yadala Venkata et al 2018][research_yadalavenkata_hehner_2018]
- [Yajnik and Subbaiah 1976][research_yajnik_subbaiah_1976]
- [Yakeno and Obayashi 2021][research_yakeno_obayashi_2021]
- [Yamada and Nakamura 2002][research_yamada_nakamura_2002]
- [Yamamoto 1992][research_yamamoto_1992]
- [Yamamoto et al 2012][research_yamamoto_tanaka_2012]
- [Yaman 2017][research_yaman_2017]
- [Yaman and Dalmış 2026][research_yaman_dalmis_2026]
- [Yan et al 2019][research_yan_dai_2019]
- [Yan et al 2019][research_yan_li_2019]
- [Yan et al 2019][research_yan_li_2019_b]
- [Yan et al 2025][research_yan_han_2025]
- [Yan et al 2025][research_yan_mccrink_2025]
- [Yang][research_yang]
- [Yang and Chen 2023][research_yang_chen_2023]
- [Yang and Li 2022][research_yang_li_2022]
- [Yang and Przekwas 1993][research_yang_przekwas_1993_b]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang et al 1980][research_yang_guruswamy_1980]
- [Yang et al 2015][research_yang_sartor_2015]
- [Yang et al 2015][research_yang_tang_2015]
- [Yang et al 2017][research_yang_an_2017]
- [Yang et al 2019][research_yang_guo_2019]
- [Yang et al 2021][research_yang_guo_2021]
- [Yang et al 2021][research_yang_guo_2021_b]
- [Yang et al 2021][research_yang_zhong_2021]
- [Yang et al 2022][research_yang_cai_2022]
- [Yang et al 2022][research_yang_guo_2022]
- [Yang et al 2022][research_yang_wang_2022]
- [Yang et al 2023][research_yang_lu_2023]
- [Yang et al 2023][research_yang_tan_2023]
- [Yang et al 2024][research_yang_xiao_2024]
- [Yang et al 2024][research_yang_xu_2024]
- [Yang et al 2025][research_yang_li_2025]
- [Yang et al 2026][research_yang_2026]
- [Yang et al 2026][research_yang_zhao_2026]
- [Yaniktepe and Rockwell 2004][research_yaniktepe_rockwell_2004]
- [Yao and Wu 2019][research_yao_wu_2019]
- [Yao et al 2023][research_yao_song_2023]
- [Yasuaki and Egami 1999][research_yasuaki_egami_1999]
- [Yates 1960][research_yates_1960]
- [Yates 1960][research_yates_1960_b]
- [Yates 1963][research_yates_1963]
- [Yates 1967][research_yates_1967]
- [Yates and Chu 1987][research_yates_chu_1987]
- [Yates et al 1982][research_yates_cunningham_1982]
- [Yatskikh et al 2017][research_yatskikh_rumenskikh_2017]
- [Yavuz 2012][research_yavuz_2012]
- [Ye 2025][research_ye_2025]
- [Ye et al 2025][research_ye_xu_2025]
- [Ye et al 2026][research_ye_peng_2026]
- [Yechout and Oelschlaeger 1976][research_yechout_oelschlaeger_1976]
- [Yen 2011][research_yen_2011]
- [Yen and Hsu 2006][research_yen_hsu_2006]
- [Yen and Hsu 2007][research_yen_hsu_2007]
- [Yen and Huang 2011][research_yen_huang_2011]
- [Yen et al 2013][research_yen_san_2013]
- [Yeo et al 2015][research_yeo_atkins_2015]
- [Yermolaev et al 2014][research_yermolaev_kosinov_2014]
- [Yermolaev et al 2017][research_yermolaev_yatskikh_2017]
- [Yermolaev et al 2020][research_yermolaev_yatskikh_2020]
- [Yigit and Millidere 2021][research_yigit_millidere_2021]
- [Yildirim and Tuncer 2021][research_yildirim_tuncer_2021]
- [Yip and Shubert 1977][research_yip_shubert_1977]
- [Yip et al 1992][research_yip_ross_1992]
- [Yip et al 1992][research_yip_vijgen_1992]
- [Yip et al 1993][research_yip_vijgen_1993]
- [Yoo 2018][research_yoo_2018]
- [Yoshida et al 2021][research_yoshida_bragg_2021]
- [You 2026][research_you_2026]
- [You et al 2019][research_you_kim_2019]
- [You et al 2020][research_you_skin_2020]
- [Young 1974][research_young_1974]
- [Young 2026][research_young_2026]
- [Young and Adams 1972][research_young_adams_1972]
- [Yu and Campbell 1992][research_yu_campbell_1992]
- [Yu and He 2016][research_yu_he_2016]
- [Yu and Hornung 2026][research_yu_hornung_2026]
- [Yu and Ma 2022][research_yu_ma_2022]
- [Yu and Yu 2026][research_yu_2026]
- [Yu et al 2009][research_yu_liu_2009]
- [Yu et al 2019][research_yu_yang_2019]
- [Yu et al 2024][research_yu_zhou_2024]
- [Yu et al 2026][research_yu_yan_2026]
- [Yuan et al 1994][research_yuan_friedman_1994]
- [Yuan et al 2016][research_yuan_sandhu_2016]
- [Yue et al 2009][research_yue_wang_2009]
- [Yue et al 2013][research_yue_wang_2013]
- [Yue et al 2013][research_yue_wang_2013_b]
- [Yue et al 2013][research_yue_wang_2013_c]
- [Yue et al 2013][research_yue_wang_2013_d]
- [Yue et al 2017][research_yue_wang_2017]
- [Yue et al 2017][research_yue_zhang_2017]
- [Yue et al 2019][research_yue_oblique_2019]
- [Yuhong et al 2017][research_yuhong_guanxin_2017]
- [Yukish and Valenti 2020][research_yukish_valenti_2020]
- [Yurkovich 1996][research_yurkovich_1996]
- [Yurkovich 2008][research_yurkovich_2008]
- [Yurkovich 2009][research_yurkovich_2009]
- [Yutong et al 2025][research_yutong_ying_2025]
- [Zangeneh 2021][research_zangeneh_2021]
- [Zangeneh 2022][research_zangeneh_2022]
- [Zarutskaya and Arieli 2005][research_zarutskaya_arieli_2005]
- [Ze et al 2024][research_ze_shen_2024]
- [Zebedee et al 2019][research_zebedee_mohammed_2019]
- [Zeiger et al 2002][research_zeiger_gerlach_2002]
- [Zeng and Kukreja 2013][research_zeng_kukreja_2013]
- [Zeng et al 2023][research_zeng_liu_2023]
- [Zhan and Wang 2007][research_zhan_wang_2007]
- [Zhang and Lu 2026][research_zhang_lu_2026]
- [Zhang and Taira 2022][research_zhang_taira_2022]
- [Zhang and Wang 2019][research_zhang_wang_2019]
- [Zhang and Wu 2014][research_zhang_wu_2014]
- [Zhang and Wu 2014][research_zhang_wu_2014_b]
- [Zhang and Yu 2012][research_zhang_yu_2012]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhou 2022][research_zhang_zhou_2022]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2014][research_zhang_hua_2014]
- [Zhang et al 2015][research_zhang_zhou_2015]
- [Zhang et al 2016][research_zhang_yang_2016]
- [Zhang et al 2017][research_zhang_liu_2017]
- [Zhang et al 2017][research_zhang_wang_2017]
- [Zhang et al 2017][research_zhang_wei_2017]
- [Zhang et al 2018][research_zhang_shaw_2018]
- [Zhang et al 2018][research_zhang_zhou_2018]
- [Zhang et al 2020][research_zhang_yan_2020]
- [Zhang et al 2021][research_zhang_shaw_2021]
- [Zhang et al 2024][research_zhang_wen_2024]
- [Zhang et al 2024][research_zhang_zhang_2024]
- [Zhang et al 2025][research_zhang_guo_2025]
- [Zhang et al 2025][research_zhang_song_2025]
- [Zhang et al 2025][research_zhang_yang_2025]
- [Zhang et al 2026][research_zhang_2026]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhang et al 2026][research_zhang_pu_2026]
- [Zhang et al 2026][research_zhang_pu_2026_b]
- [Zhang et al 2026][research_zhang_yang_2026]
- [Zhang et al 2026][research_zhang_zhao_2026]
- [Zhao 1988][research_zhao_1988]
- [Zhao 1998][research_zhao_1998]
- [Zhao and Hu 2013][research_zhao_hu_2013]
- [Zhao and Hu 2013][research_zhao_hu_2013_b]
- [Zhao and Kapania 2017][research_zhao_kapania_2017]
- [Zhao and Zhu 2016][research_zhao_zhu_2016]
- [Zhao et al 2021][research_zhao_xi_2021]
- [Zhao et al 2022][research_zhao_luo_2022]
- [Zhao et al 2023][research_zhao_yang_2023]
- [Zhao et al 2026][research_zhao_guo_2026]
- [Zhao et al 2026][research_zhao_zhang_2026]
- [Zhen et al 2017][research_zhen_yingying_2017]
- [Zheng et al 2014][research_zheng_he_2014]
- [Zhou 2018][research_zhou_2018]
- [Zhou and Huang 2021][research_zhou_huang_2021]
- [Zhou and Huang 2021][research_zhou_huang_2021_b]
- [Zhou and Wu 2025][research_zhou_wu_2025]
- [Zhou et al 2018][research_zhou_plummer_2018]
- [Zhou et al 2022][research_zhou_plummer_2022]
- [Zhu 2018][research_zhu_2018]
- [Zhu and Breuer 2022][research_zhu_breuer_2022]
- [Zhu et al 2017][research_zhu_liu_2017]
- [Zhu et al 2019][research_zhu_li_2019]
- [Zhu et al 2019][research_zhu_liu_2019]
- [Zhu et al 2025][research_zhu_zhou_2025]
- [Zhu et al 2025][research_zhu_zhou_2025_b]
- [Zhu et al 2026][research_zhu_zhu_2026]
- [Zientarski et al 2015][research_zientarski_marks_2015]
- [Zimper and Rein 2014][research_zimper_rein_2014]
- [Zink et al 2000][research_zink_mavris_2000]
- [Zink et al 2001][research_zink_mavris_2001]
- [Zoppini et al 2022][research_zoppini_ragni_2022]
- [Zoppini et al 2022][research_zoppini_ragni_2022_b]
- [Zverkov et al 2012][research_zverkov_kozlov_2012]
- [Şahin and Yaman 2018][research_sahin_yaman_2018]
- [Şahin and Yaman 2018][research_sahin_yaman_2018_b]
- [Şahin et al 2018][research_sahin_cakir_2018]
- [Şahin et al 2018][research_sahin_cakir_2018_b]

### Related Post

- [A106 Two-Stage Flying Delta Wing Vehicles][related_post_a106_two_stage_delta_wing]
- [A118 Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_a118_propulsion_sizing]
- [A120 Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_a120_staged_boosted_propulsion]
- [A122 Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_a122_stability_configuration]
- [A123 Dynamic Stability and Control for Fixed-Wing UAVs][related_post_a123_dynamic_stability]
- [A127 Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_a127_structures_flight_envelope]
- [A217 Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217_rocket_propellant_chemistry]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A241 Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation]
- [A297 X-Planes, Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [A298 X-Planes, Bell X-1][related_post_a298_bell_x1]
- [A299 X-Planes, Bell X-2][related_post_a299_bell_x2]
- [A300 X-Planes, Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [A301 X-Planes, Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]

[book_anderson_1997_history_aerodynamics]: https://openlibrary.org/works/OL1993322W
[book_anderson_2001_fundamentals]: https://openlibrary.org/works/OL3232211W
[book_anderson_2002_modern_compressible]: https://openlibrary.org/works/OL1993329W
[book_anderson_2006_hypersonic]: https://openlibrary.org/works/OL1993330W
[book_anderson_2012_aircraft_performance]: https://openlibrary.org/works/OL1993317W
[book_ashley_landahl_1965]: https://openlibrary.org/works/OL42971075W
[book_baals_corliss_1981]: https://openlibrary.org/works/OL31504107W
[book_bertin_1994_hypersonic]: https://openlibrary.org/works/OL3287053W
[book_bertin_cummings_2013]: https://openlibrary.org/works/OL21437883W
[book_bevington_robinson_2002]: https://openlibrary.org/works/OL44935135W
[book_bilstein_1989_orders]: https://openlibrary.org/works/OL18823771W
[book_bisplinghoff_ashley_halfman_1955]: https://openlibrary.org/works/OL3240762W
[book_boley_weiner_1960]: https://openlibrary.org/works/OL19334049W
[book_box_hunter_hunter_2005]: https://openlibrary.org/works/OL28985605W
[book_bruhn_1973]: https://openlibrary.org/works/OL8796483W
[book_carslaw_jaeger_1959]: https://openlibrary.org/works/OL34686169W
[book_chambers_2008_radical_wings]: https://openlibrary.org/works/OL5834577W
[book_cover_thomas_2006]: https://openlibrary.org/works/OL21500808W
[book_dowell_2014]: https://openlibrary.org/works/OL20677670W
[book_etkin_reid_1996]: https://openlibrary.org/works/OL19844466W
[book_ferguson_1992]: https://openlibrary.org/works/OL4119982W
[book_fung_1955]: https://openlibrary.org/works/OL2655267W
[book_gelman_et_al_2013]: https://openlibrary.org/works/OL12630389W
[book_gorn_1992_universal_man]: https://openlibrary.org/works/OL4400575W
[book_gorn_2001_expanding_envelope]: https://openlibrary.org/works/OL4400572W
[book_gunston_1992_faster_than_sound]: https://openlibrary.org/works/OL774338W
[book_hallion_1972_supersonic_flight]: https://openlibrary.org/works/OL2688456W
[book_hallion_1981_test_pilots]: https://openlibrary.org/works/OL2688457W
[book_hansen_1987_engineer_in_charge]: https://openlibrary.org/works/OL37594565W
[book_heppenheimer_2007_heat_barrier]: https://openlibrary.org/works/OL39929219W
[book_hill_peterson_1991]: https://openlibrary.org/works/OL8229940W
[book_hurt_1965]: https://openlibrary.org/works/OL4297319W
[book_huzel_huang_1992]: https://openlibrary.org/works/OL27313820W
[book_incropera_heat_transfer]: https://openlibrary.org/works/OL2975219W
[book_jenkins_2000_hypersonics]: https://openlibrary.org/works/OL813290W
[book_jenkins_2007_x15]: https://ntrs.nasa.gov/citations/20080008340
[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_kimberlin_2003]: https://openlibrary.org/works/OL8874080W
[book_kuchemann_1978]: https://openlibrary.org/works/OL22640504W
[book_launius_jenkins_2012]: https://openlibrary.org/works/OL39998199W
[book_liepmann_roshko_1957]: https://openlibrary.org/works/OL13214987W
[book_mcruer_ashkenas_graham_1973]: https://openlibrary.org/works/OL13424815W
[book_megson_2016]: https://openlibrary.org/works/OL4809615W
[book_merlin_2009_blackbird]: https://openlibrary.org/works/OL11706498W
[book_miller_2001_x_planes]: https://openlibrary.org/works/OL7006680W
[book_nelson_1998]: https://openlibrary.org/works/OL11288560W
[book_nicolai_carichner_2010]: https://openlibrary.org/works/OL15909375W
[book_niu_1988_airframe]: https://openlibrary.org/works/OL19561185W
[book_peebles_2014_probing_the_sky]: https://openlibrary.org/works/OL23215820W
[book_perrow_1984]: https://openlibrary.org/works/OL4468929W
[book_petroski_1985]: https://openlibrary.org/works/OL112186W
[book_raymer_2018]: https://openlibrary.org/works/OL17855977W
[book_reason_1990_human_error]: https://openlibrary.org/works/OL9006915W
[book_roskam_1985]: https://openlibrary.org/works/OL6612019W
[book_sagan_1993]: https://openlibrary.org/works/OL3492159W
[book_schlichting_gersten_2017]: https://openlibrary.org/works/OL20524688W
[book_shapiro_1953]: https://openlibrary.org/works/OL5908243W
[book_stengel_2004]: https://openlibrary.org/works/OL3486012W
[book_stevens_lewis_2015]: https://openlibrary.org/works/OL21570717W
[book_stinton_2001]: https://openlibrary.org/works/OL1911152W
[book_sutton_biblarz_2016]: https://openlibrary.org/works/OL21470530W
[book_taylor_1997_error_analysis]: https://openlibrary.org/works/OL3232610W
[book_thompson_1992_edge_of_space]: https://openlibrary.org/works/OL1994111W
[book_torenbeek_1982]: https://openlibrary.org/works/OL9096469W
[book_truitt_1960]: https://openlibrary.org/works/OL178473W
[book_vaughan_1996]: https://openlibrary.org/works/OL2962391W
[book_vincenti_1990]: https://openlibrary.org/works/OL4805206W
[book_von_karman_edson_1967]: https://openlibrary.org/works/OL7117470W
[book_ward_strganac_niewoehner_2006]: https://openlibrary.org/works/OL19810630W
[book_white_2006_viscous]: https://openlibrary.org/works/OL1911849W
[book_whitford_1987]: https://openlibrary.org/works/OL5054670W
[book_winchester_2005_x_planes]: https://openlibrary.org/works/OL8492617W
[book_wolfe_1979_right_stuff]: https://openlibrary.org/works/OL1925474W
[ref_accelerometer]: https://en.wikipedia.org/wiki/Accelerometer
[ref_aerodynamic_center]: https://en.wikipedia.org/wiki/Aerodynamic_center
[ref_aeroelasticity]: https://en.wikipedia.org/wiki/Aeroelasticity
[ref_anp]: https://en.wikipedia.org/wiki/Aircraft_Nuclear_Propulsion
[ref_armstrong_frc]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_b1_lancer]: https://en.wikipedia.org/wiki/Rockwell_B-1_Lancer
[ref_bell_aircraft]: https://en.wikipedia.org/wiki/Bell_Aircraft
[ref_bell_x5]: https://en.wikipedia.org/wiki/Bell_X-5
[ref_boundary_layer]: https://en.wikipedia.org/wiki/Boundary_layer
[ref_buffeting]: https://en.wikipedia.org/wiki/Aeroelasticity#Buffeting
[ref_compliant_wing]: https://en.wikipedia.org/wiki/Adaptive_compliant_wing
[ref_convair_x6]: https://en.wikipedia.org/wiki/Convair_X-6
[ref_crossfield]: https://en.wikipedia.org/wiki/Scott_Crossfield
[ref_delta_wing]: https://en.wikipedia.org/wiki/Delta_wing
[ref_directional_stability]: https://en.wikipedia.org/wiki/Directional_stability
[ref_drag_coefficient]: https://en.wikipedia.org/wiki/Drag_coefficient
[ref_duralumin]: https://en.wikipedia.org/wiki/Duralumin
[ref_dutch_roll]: https://en.wikipedia.org/wiki/Dutch_roll
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_edwards_afb]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base
[ref_euler_equations_rigid]: https://en.wikipedia.org/wiki/Euler%27s_equations_(rigid_body_dynamics)
[ref_experimental_aircraft]: https://en.wikipedia.org/wiki/Experimental_aircraft
[ref_f111]: https://en.wikipedia.org/wiki/General_Dynamics_F-111_Aardvark
[ref_f14]: https://en.wikipedia.org/wiki/Grumman_F-14_Tomcat
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft)
[ref_flight_envelope]: https://en.wikipedia.org/wiki/Flight_envelope
[ref_flight_test]: https://en.wikipedia.org/wiki/Flight_test
[ref_flow_separation]: https://en.wikipedia.org/wiki/Flow_separation
[ref_inertia_coupling]: https://en.wikipedia.org/wiki/Inertia_coupling
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_j35]: https://en.wikipedia.org/wiki/Allison_J35
[ref_jackscrew]: https://en.wikipedia.org/wiki/Jackscrew
[ref_landing_gear]: https://en.wikipedia.org/wiki/Landing_gear
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_lift_to_drag]: https://en.wikipedia.org/wiki/Lift-to-drag_ratio
[ref_list_of_x_planes]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_load_factor]: https://en.wikipedia.org/wiki/Load_factor_(aeronautics)
[ref_longitudinal_static_stability]: https://en.wikipedia.org/wiki/Longitudinal_static_stability
[ref_mac]: https://en.wikipedia.org/wiki/Mean_aerodynamic_chord
[ref_mach_number]: https://en.wikipedia.org/wiki/Mach_number
[ref_measurement_uncertainty]: https://en.wikipedia.org/wiki/Measurement_uncertainty
[ref_mig23]: https://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-23
[ref_mig27]: https://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-27
[ref_moment_of_inertia]: https://en.wikipedia.org/wiki/Moment_of_inertia
[ref_na_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_naca]: https://en.wikipedia.org/wiki/National_Advisory_Committee_for_Aeronautics
[ref_naca_airfoil]: https://en.wikipedia.org/wiki/NACA_airfoil
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasa_x3_factsheet]: https://www.nasa.gov/history/
[ref_nasa_x5_factsheet]: https://www.nasa.gov/centers-and-facilities/armstrong/nasa-armstrong-fact-sheet-x-5-research-aircraft/
[ref_nmusaf]: https://en.wikipedia.org/wiki/National_Museum_of_the_United_States_Air_Force
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_oblique_wing]: https://en.wikipedia.org/wiki/Oblique_wing
[ref_operation_lusty]: https://en.wikipedia.org/wiki/Operation_Lusty
[ref_p1101]: https://en.wikipedia.org/wiki/Messerschmitt_P.1101
[ref_phugoid]: https://en.wikipedia.org/wiki/Phugoid
[ref_prandtl_number]: https://en.wikipedia.org/wiki/Prandtl_number
[ref_propagation_of_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[ref_rcs]: https://en.wikipedia.org/wiki/Reaction_control_system
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_shock_wave]: https://en.wikipedia.org/wiki/Shock_wave
[ref_slat]: https://en.wikipedia.org/wiki/Leading-edge_slat
[ref_sound_barrier]: https://en.wikipedia.org/wiki/Sound_barrier
[ref_speed_of_sound]: https://en.wikipedia.org/wiki/Speed_of_sound
[ref_spin]: https://en.wikipedia.org/wiki/Spin_(aerodynamics)
[ref_stabilator]: https://en.wikipedia.org/wiki/Stabilator
[ref_stability_augmentation]: https://en.wikipedia.org/wiki/Stability_augmentation_system
[ref_strain_gauge]: https://en.wikipedia.org/wiki/Strain_gauge
[ref_su17]: https://en.wikipedia.org/wiki/Sukhoi_Su-17
[ref_su24]: https://en.wikipedia.org/wiki/Sukhoi_Su-24
[ref_supersonic_speed]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_takeoff]: https://en.wikipedia.org/wiki/Takeoff
[ref_telemetry]: https://en.wikipedia.org/wiki/Telemetry
[ref_tornado]: https://en.wikipedia.org/wiki/Panavia_Tornado
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_tu160]: https://en.wikipedia.org/wiki/Tupolev_Tu-160
[ref_tu22m]: https://en.wikipedia.org/wiki/Tupolev_Tu-22M
[ref_us_standard_atmosphere]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[ref_wind_tunnel]: https://en.wikipedia.org/wiki/Wind_tunnel
[ref_wing_configuration]: https://en.wikipedia.org/wiki/Wing_configuration
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[ref_wing_root]: https://en.wikipedia.org/wiki/Wing_root
[ref_wing_twist]: https://en.wikipedia.org/wiki/Wing_twist
[ref_xb70]: https://en.wikipedia.org/wiki/North_American_XB-70_Valkyrie
[ref_yaw_damper]: https://en.wikipedia.org/wiki/Yaw_damper
[ref_yield_strength]: https://en.wikipedia.org/wiki/Yield_(engineering)
[related_post_a106_two_stage_delta_wing]: {% post_url 2026-03-12-two_stage_flying_delta_wing_vehicles_for_civil_and_national_security_applications %}
[related_post_a118_propulsion_sizing]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_a120_staged_boosted_propulsion]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[related_post_a122_stability_configuration]: {% post_url 2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs %}
[related_post_a123_dynamic_stability]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_a127_structures_flight_envelope]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
[related_post_a217_rocket_propellant_chemistry]: {% post_url 2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a241_aerospace_simulation]: {% post_url 2026-07-17-aerospace_simulation_and_real_time_systems %}
[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a299_bell_x2]: {% post_url 2025-10-08-x_planes_bell_x2 %}
[related_post_a300_douglas_x3]: {% post_url 2025-10-09-x_planes_douglas_x3 %}
[related_post_a301_northrop_x4]: {% post_url 2025-10-10-x_planes_northrop_x4 %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_a_7_transonic_1982]: https://doi.org/10.2514/5.9781600865558.0431.0450
[research_a_properties_2006]: https://doi.org/10.1002/9780470117859.app1
[research_abdelghany_khalil_2016]: https://doi.org/10.21608/amme.2016.35282
[research_abdelhamid_kandil_1998]: https://ntrs.nasa.gov/citations/19990041098
[research_abdessemed_yao_2018]: https://doi.org/10.2514/6.2018-3178
[research_abdullaeva_moralevi_2024]: https://doi.org/10.53954/9785605099659_3
[research_abdulrahim_2005]: https://doi.org/10.2514/6.2005-345
[research_abdulrahim_lind_2004]: https://doi.org/10.2514/6.2004-5113
[research_abegg_bippes_2000]: https://doi.org/10.1007/978-3-662-03997-7_94
[research_abel_1966]: https://ntrs.nasa.gov/citations/19660021918
[research_aboukhalil]: https://doi.org/10.70675/66b39910zfac2z4bb0za3edz063330634814
[research_abrahamdoman_merrett_2014]: https://doi.org/10.2514/6.2014-0194
[research_abrego_maier_1999]: https://doi.org/10.4050/vfs-f55-00009
[research_abzug_daros_1955]: https://doi.org/10.21236/ada003615
[research_ackeret_1925]: https://ntrs.nasa.gov/citations/19930087085
[research_ackeret_1951]: https://ntrs.nasa.gov/citations/19930093910
[research_acree_peyran_2004]: https://ntrs.nasa.gov/citations/20040081235
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_adams_1973]: https://doi.org/10.21236/ad0771962
[research_adams_hatchjr_1970]: https://doi.org/10.2514/6.1970-568
[research_adegbindin_love_2016]: https://doi.org/10.2514/6.2016-3361
[research_adhikari_loubimov_2022]: https://doi.org/10.1103/physrevfluids.7.044702
[research_adoghe]: https://doi.org/10.22215/etd/2022-15031
[research_advanced_aerodynamics_1981]: https://ntrs.nasa.gov/citations/19840019592
[research_advanced_aircraft_2026]: https://doi.org/10.1017/9781009399913.014
[research_aerodynamic_characteristics_of_2018]: https://doi.org/10.20535/2219-3804182018134713
[research_aerodynamic_design_1969]: https://doi.org/10.1108/eb034586
[research_aerodynamic_performance_2024]: https://doi.org/10.47176/jafm.17.6.2403
[research_aerodynamics_of_2010]: https://doi.org/10.2514/5.9781600867538.0745.0758
[research_aeroelasticity_problems_2010]: https://doi.org/10.2514/5.9781600867552.0335.0373
[research_afanasyev_yermolaev_2025]: https://doi.org/10.25205/2541-9447-2024-19-4-41-54
[research_agaponov_gyermolaev_2008]: https://doi.org/10.54362/1818-7919-2008-3-3-34-38
[research_agenbag_theron_2009]: https://doi.org/10.2514/1.39755
[research_agrawal_kinard_1991]: https://doi.org/10.2514/6.1991-3205
[research_aguirrebeitia_aviles_2012]: https://doi.org/10.1007/978-94-007-4902-3_1
[research_aharrah_1964]: https://doi.org/10.2514/3.43556
[research_ahmad_baig_2018]: https://doi.org/10.1063/1.5045437
[research_ahmad_gour_2024]: https://doi.org/10.1142/s1758825124500741
[research_ahmed_jave_1995]: https://doi.org/10.2514/6.1995-868
[research_ahmed_wentz_1989]: https://ntrs.nasa.gov/citations/19900025962
[research_ahmer_2026]: https://doi.org/10.1016/j.ast.2026.113186
[research_ai_weaver_2017]: https://doi.org/10.2514/6.2017-0055
[research_aiken_falarski_1979]: https://ntrs.nasa.gov/citations/19790020973
[research_aircraft_drag_2010]: https://doi.org/10.1017/cbo9780511844652.011
[research_aircraft_dynamic_2003]: https://doi.org/10.2514/5.9781600862069.0303.0388
[research_aircraft_dynamic_2014]: https://doi.org/10.2514/5.9781624102547.0331.0420
[research_aircraft_equations_2003]: https://doi.org/10.2514/5.9781600862069.0145.0172
[research_aircraft_flight_2014]: https://doi.org/10.1201/b17346-12
[research_aircraft_flutter_2011]: https://doi.org/10.1049/pbce074e_ch12
[research_aircraft_lateral_directional_2011]: https://doi.org/10.1049/pbce074e_ch9
[research_aircraft_load_2010]: https://doi.org/10.1017/cbo9780511844652.007
[research_aircraft_longitudinal_2011]: https://doi.org/10.1049/pbce074e_ch10
[research_aircraft_moments_1996]: https://doi.org/10.1016/b978-034063170-6/50016-5
[research_aircraft_non_linear_2014]: https://doi.org/10.1201/b17346-8
[research_aircraft_stability_2003]: https://doi.org/10.2514/5.9781600862069.0433.0472
[research_aircraft_stability_2014]: https://doi.org/10.2514/5.9781624102547.0465.0508
[research_aircraft_stability_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n42
[research_aircraft_stability_2026]: https://doi.org/10.1017/9781009399913.010
[research_aircraft_static_2003]: https://doi.org/10.2514/5.9781600862069.0173.0238
[research_aircraft_static_2014]: https://doi.org/10.2514/5.9781624102547.0195.0264
[research_aircraft_static_2024]: https://doi.org/10.2514/5.9781624107252.0197.0266
[research_aircraft_wing_2005]: https://doi.org/10.1002/0470855487.ch12
[research_airfoil_and_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00020-6
[research_airfoil_and_2024]: https://doi.org/10.2514/5.9781624107290.0055.0118
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320208
[research_airplane_spin_2003]: https://doi.org/10.2514/5.9781600861840.0383.0416
[research_airplane_trim_2012]: https://doi.org/10.1017/cbo9781139161893.010
[research_airplane_trim_2022]: https://doi.org/10.2514/5.9781624106408.0223.0240
[research_airspeed_vs_2003]: https://doi.org/10.2514/5.9781600861840.0169.0176
[research_ajaj_friswell_2016]: https://doi.org/10.1016/j.ast.2016.03.009
[research_ajaj_jankee_2018]: https://doi.org/10.1016/j.ast.2018.02.022
[research_ajaj_saavedraflores_2013]: https://doi.org/10.1016/j.ast.2012.12.002
[research_ajanic_feroskhan_2020]: https://doi.org/10.1126/scirobotics.abc2897
[research_alag_1987]: https://ntrs.nasa.gov/citations/19870063217
[research_alag_burken_1986]: https://ntrs.nasa.gov/citations/19860020396
[research_alag_burken_1987]: https://doi.org/10.2514/3.20253
[research_alag_kempel_1986]: https://ntrs.nasa.gov/citations/19860016867
[research_alag_kempel_1986_b]: https://ntrs.nasa.gov/citations/19860020395
[research_alam_kara_2022]: https://doi.org/10.2514/6.2022-3296
[research_alasty_alemohammad_2004]: https://doi.org/10.2514/6.2004-4831
[research_albayati_2026]: https://doi.org/10.1063/12.0046109
[research_albers_schroder_2020]: https://doi.org/10.1103/physrevfluids.5.064611
[research_alcorta_chouvion_2023]: https://doi.org/10.2139/ssrn.4412811
[research_aleisa_kontis_2023]: https://doi.org/10.2514/1.c037257
[research_alford_1959]: https://ntrs.nasa.gov/citations/19650014458
[research_alford_1959_2]: https://ntrs.nasa.gov/citations/19650014499
[research_alford_1962]: https://ntrs.nasa.gov/citations/19660025704
[research_alford_1966]: https://ntrs.nasa.gov/citations/19660022439
[research_alford_byrnes_1952]: https://ntrs.nasa.gov/citations/20050019264
[research_alford_luoma_1960]: https://ntrs.nasa.gov/citations/19660020171
[research_alford_polhamus_1962]: https://ntrs.nasa.gov/citations/19700023944
[research_ali_2017]: https://doi.org/10.31026/j.eng.2017.04.08
[research_alkhafaji_panatov_2023]: https://doi.org/10.18522/2311-3103-2023-3-212-223
[research_allen_bridges_2003]: https://doi.org/10.1111/1467-9590.00241
[research_allen_lizotte_2005]: https://doi.org/10.2514/6.2005-6313
[research_alley_phillips_2007]: https://doi.org/10.2514/6.2007-711
[research_alley_phillips_2010]: https://doi.org/10.2514/1.c001010
[research_allred_fleck_1992]: https://ntrs.nasa.gov/citations/19920015847
[research_almalki_fildes_2022]: https://doi.org/10.1063/5.0105788
[research_alpatskiy_2026]: https://doi.org/10.25205/2541-9447-2025-20-4-30-42
[research_alsaidi_joe_2019]: https://doi.org/10.3390/aerospace6080090
[research_alternative_methods_1989]: https://doi.org/10.2514/5.9781600865947.0349.0376
[research_alulema_2025]: https://doi.org/10.3390/aerospace12090825
[research_alulema_valencia_2020]: https://doi.org/10.2514/6.2020-3962
[research_alvarez_wissa_2021]: https://doi.org/10.1115/smasis2021-68299
[research_alviani_blaisdell_2022]: https://doi.org/10.2514/6.2022-2198
[research_alyanak_pendleton_2014]: https://doi.org/10.2514/6.2014-3158
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_amano_avdeev_2011]: https://doi.org/10.1115/power2011-55226
[research_ameduri_2025]: https://doi.org/10.3390/app15052529
[research_ameho_prempain_2011]: https://doi.org/10.1109/acc.2011.5991349
[research_amendola_dimino_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00018-6
[research_ameri_lowenberg_2007]: https://doi.org/10.2514/6.2007-6500
[research_ameri_lowenberg_2008]: https://doi.org/10.2514/6.2008-6966
[research_an_aeroelastic_2013]: https://doi.org/10.36884/jafm.6.01.19503
[research_an_analysis_1981]: https://doi.org/10.2514/6.1981-364
[research_an_experimental_1978]: https://doi.org/10.2514/6.1978-1200
[research_an_introduction_1966]: https://doi.org/10.1016/c2013-0-08104-2
[research_an_yan_1986]: https://doi.org/10.2514/6.1986-2234
[research_an_yan_1988]: https://doi.org/10.2514/3.45580
[research_ananthasayanam_2002]: https://doi.org/10.2514/6.2002-4877
[research_ananthkrishnan_2004]: https://doi.org/10.2514/6.2004-4950
[research_ananthkrishnan_sudhakar_1994]: https://doi.org/10.2514/3.46591
[research_ananthkrishnan_sudhakar_1995]: https://doi.org/10.2514/3.46807
[research_andersen_cowan_2007]: https://doi.org/10.2514/6.2007-1734
[research_anderson_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_anderson_1978]: https://ntrs.nasa.gov/citations/19780062605
[research_anderson_1979]: https://doi.org/10.2514/3.58548
[research_anderson_1984]: https://ntrs.nasa.gov/citations/19840059559
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_1988]: https://ntrs.nasa.gov/citations/19880020709
[research_anderson_1990]: https://ntrs.nasa.gov/citations/19910015242
[research_anderson_1990_2]: https://ntrs.nasa.gov/citations/19910015243
[research_anderson_bray_1951]: https://ntrs.nasa.gov/citations/19930086840
[research_anderson_enevoldson_1983]: https://ntrs.nasa.gov/citations/19830018575
[research_anderson_meyer_1991]: https://doi.org/10.2514/3.46074
[research_anderson_robertrmeyer_2012]: https://ntrs.nasa.gov/citations/19880051535
[research_ando_yamamoto_1976]: https://doi.org/10.1007/bf00539778
[research_andrews_1980]: https://ntrs.nasa.gov/citations/19800024830
[research_andrews_perez_2015]: https://doi.org/10.2514/6.2015-3291
[research_andrews_sim_1980]: https://ntrs.nasa.gov/citations/19810049789
[research_anglin_1965]: https://ntrs.nasa.gov/citations/19650011396
[research_anglin_1967]: https://ntrs.nasa.gov/citations/19670024128
[research_anglin_1978]: https://doi.org/10.2514/3.58445
[research_ankenbruck_1946]: https://ntrs.nasa.gov/citations/19930092559
[research_another_vertical_1932]: https://doi.org/10.1108/eb029569
[research_antaran_belete_1992]: https://ntrs.nasa.gov/citations/19930008977
[research_anto_2026]: https://doi.org/10.58445/rars.4002
[research_anwar_2025]: https://doi.org/10.32920/29078597
[research_anyoji_liu_2013]: https://doi.org/10.2514/6.2013-3180
[research_aouf_boulet_2002]: https://doi.org/10.1109/acc.2002.1025347
[research_aoyagi_cook_1965]: https://ntrs.nasa.gov/citations/19650014225
[research_aoyagi_hickey_1959]: https://ntrs.nasa.gov/citations/19980228317
[research_apostolyuk_2007]: https://doi.org/10.2514/1.30250
[research_appel_cooke_2021]: https://doi.org/10.1007/978-3-030-67902-6_30
[research_appendix_a_2011_b]: https://doi.org/10.1515/9781400839063-017
[research_appendix_a_2021]: https://doi.org/10.1002/9781118949818.app1
[research_appendix_b_2003]: https://doi.org/10.2514/5.9781600862069.0573.0576
[research_appendix_c_2016]: https://doi.org/10.1002/9781118823491.app3
[research_appendix_g_2003]: https://doi.org/10.2514/5.9781600862069.0609.0612
[research_appendix_h_2003]: https://doi.org/10.2514/5.9781600862069.0613.0622
[research_appendix_h_2010]: https://doi.org/10.2514/5.9781600867538.0745.0757
[research_application_of]: https://doi.org/10.1007/bfb0043104
[research_application_of_1982]: https://doi.org/10.2514/5.9781600865558.0405.0430
[research_application_status_2023]: https://doi.org/10.3901/jme.2023.19.001
[research_apuleo_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00002-2
[research_arabian_runckel_1961]: https://ntrs.nasa.gov/citations/19980236837
[research_arai_noto_2000]: https://doi.org/10.2514/6.2000-4327
[research_araujoestrada_gong_2016]: https://doi.org/10.2514/6.2016-2119
[research_araujoestrada_lowenberg_2015]: https://doi.org/10.2514/6.2015-0750
[research_archambaud_louis_2004]: https://doi.org/10.2514/6.2004-2245
[research_arcidiacono_carta_1970]: https://doi.org/10.21236/ad0869823
[research_arena_amoroso_2018]: https://doi.org/10.3390/aerospace6010001
[research_arena_nelson_1989]: https://ntrs.nasa.gov/citations/19890061682
[research_armstrong_lindberg_2006]: https://doi.org/10.21236/ada463491
[research_arnal_casalis_1990]: https://doi.org/10.1007/978-3-642-84103-3_28
[research_arnal_juillen_1990]: https://doi.org/10.1007/978-3-662-02643-4_25
[research_arnal_seraudie_2000]: https://doi.org/10.1007/978-3-662-03997-7_91
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnott_bernstein_1996]: https://doi.org/10.1017/s0001924000028918
[research_arnottt_bernstein_2000]: https://doi.org/10.1017/s0001924000017802
[research_arslan_carlson_1994]: https://doi.org/10.2514/6.1994-4400
[research_arunkumar_sravanthi_2023]: https://doi.org/10.1016/j.matpr.2023.06.353
[research_arunkumar_viswamurthy_2010]: https://doi.org/10.1108/00022661011082713
[research_asaro_vos_2026]: https://doi.org/10.2514/1.c038513
[research_ascani_mellin_1971]: https://doi.org/10.2514/6.1971-404
[research_ashenberg_weihs_1984]: https://doi.org/10.2514/3.56733
[research_asher_martuccelli_1957]: https://doi.org/10.21236/ad0142088
[research_ashkenas_1964]: https://doi.org/10.2514/3.59206
[research_ashkenas_1964_b]: https://doi.org/10.2514/3.59211
[research_ashkenas_1984]: https://doi.org/10.2514/3.44963
[research_ashworth_mouch_1988]: https://doi.org/10.2514/6.1988-563
[research_ashworth_waltrip_1986]: https://doi.org/10.2514/6.1986-1104
[research_assessment_of_1980]: https://ntrs.nasa.gov/citations/19810003508
[research_ataeiesfahani_qianwang_2006]: https://doi.org/10.1109/acc.2006.1655380
[research_atman_bambang_2015]: https://doi.org/10.1109/iceei.2015.7352504
[research_atmosphere_aerodynamics]: https://doi.org/10.1007/978-3-540-46573-7_3
[research_attar_gordnier_2008]: https://doi.org/10.2514/6.2008-617
[research_aubeelack]: https://doi.org/10.70675/fa207839z078cz4de3za09fz53641267d140
[research_aubeelack_botez_2017]: https://doi.org/10.2514/6.2017-3259
[research_august_kopsaftopoulos_2026]: https://doi.org/10.2514/6.2026-0040
[research_aungkowynn_caoyihua_2010]: https://doi.org/10.1109/icmet.2010.5598489
[research_averett_1966]: https://ntrs.nasa.gov/citations/19660010231
[research_avkhadiev_elizarov_2001]: https://doi.org/10.1017/s1446181100012232
[research_awadallaalihajahmed_2024]: https://doi.org/10.47191/etj/v9i10.08
[research_axelson_1959]: https://ntrs.nasa.gov/citations/19630003340
[research_ayers_1969]: https://ntrs.nasa.gov/citations/19810010498
[research_ayers_1973]: https://ntrs.nasa.gov/citations/19830002758
[research_azam_sulaeman_2014]: https://doi.org/10.31436/iiumej.v15i2.524
[research_b_34_u_1963]: https://doi.org/10.1016/0019-1035(63)90063-0
[research_baals_polhamus_1963]: https://ntrs.nasa.gov/citations/19630021495
[research_babister_1980]: https://doi.org/10.1016/b978-0-08-024768-7.50013-2
[research_bachelder_aponso_2020]: https://doi.org/10.4050/sm_2020_hq-915
[research_bachelder_aponso_2020_b]: https://doi.org/10.4050/sm_2020_hq-914
[research_badihi_2026]: https://doi.org/10.2514/1.c038688
[research_bae_seigler_2004]: https://doi.org/10.2514/6.2004-1726
[research_bae_seigler_2005]: https://doi.org/10.2514/1.4397
[research_bagheri_2025]: https://doi.org/10.1049/cth2.70018
[research_bagley_1962]: https://doi.org/10.1016/b978-1-4831-9984-9.50004-6
[research_bai_2025]: https://doi.org/10.1016/j.ast.2024.109771
[research_bai_ding_2022]: https://doi.org/10.1109/lra.2022.3149034
[research_bai_li_2025]: https://doi.org/10.1016/j.jmps.2025.106241
[research_bai_xing_2020]: https://doi.org/10.1109/aiam50918.2020.00013
[research_bai_yang_2024]: https://doi.org/10.1109/icmre60776.2024.10532186
[research_bai_yang_2024_b]: https://doi.org/10.1016/j.cja.2024.02.015
[research_bai_yang_2026]: https://doi.org/10.1016/j.tws.2025.114405
[research_bajaj_2019]: https://doi.org/10.31224/osf.io/bfjn3
[research_bajer_hrstka_2025]: https://doi.org/10.1201/9781003677895-155
[research_baker_1953]: https://ntrs.nasa.gov/citations/19930087804
[research_balabanov_haftka_1996]: https://doi.org/10.2514/3.46926
[research_balachandran_2014]: https://doi.org/10.21236/ada611076
[research_ballhaus_bailey_1972]: https://ntrs.nasa.gov/citations/19720050397
[research_ballin_1982]: https://ntrs.nasa.gov/citations/19820011350
[research_ballouz_chang]: https://doi.org/10.17918/etd-7772
[research_balon_benes_2021]: https://doi.org/10.1109/icmerr54363.2021.9680832
[research_bamber_house_1937]: https://ntrs.nasa.gov/citations/19930091682
[research_banerjee_taneja_2025]: https://doi.org/10.21203/rs.3.rs-5956020/v1
[research_banner_1955]: https://ntrs.nasa.gov/citations/19930088628
[research_barahona_weijer_2024]: https://doi.org/10.2514/6.2024-0695
[research_barbosa_2025]: https://doi.org/10.3390/aerospace12060557
[research_barbosa_bertolin_2018]: https://doi.org/10.2514/6.2018-1868
[research_bardin_2021]: https://doi.org/10.32920/ryerson.14635734.v1
[research_barger_wright_1966]: https://ntrs.nasa.gov/citations/19660019777
[research_barmby_cunningham_1951]: https://ntrs.nasa.gov/citations/19930092069
[research_barnard_1969]: https://doi.org/10.2514/6.1969-793
[research_barnes_visbal_2019]: https://doi.org/10.2514/6.2019-3538
[research_barnes_visbal_2019_b]: https://doi.org/10.2514/6.2019-0896
[research_barrows_2006]: https://ntrs.nasa.gov/citations/20070003495
[research_bartels_stanford_2019]: https://doi.org/10.2514/6.2019-2035
[research_barthelemy_bergen_1988]: https://doi.org/10.2514/6.1988-2301
[research_bartlett_1973]: https://ntrs.nasa.gov/citations/19830002762
[research_basaeri_yousefikoma_2014]: https://doi.org/10.1016/j.mechatronics.2014.10.010
[research_bashir_rajendran_2018]: https://doi.org/10.1088/1757-899x/370/1/012040
[research_basic_equations_1989]: https://doi.org/10.2514/5.9781600865947.0057.0073
[research_baskaran_bradshaw_1988]: https://doi.org/10.1007/bf00196510
[research_batina_bennett_1988]: https://ntrs.nasa.gov/citations/19880020394
[research_batina_seidel_1988]: https://ntrs.nasa.gov/citations/19880010885
[research_batina_seidel_1989]: https://ntrs.nasa.gov/citations/19890011575
[research_battaglia_riccio_2026]: https://doi.org/10.3390/act15080414
[research_bauer_grund_2016]: https://doi.org/10.20944/preprints201607.0061.v1
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_beatty_brooks_1977]: https://doi.org/10.21236/ada045951
[research_beaufrere_1988]: https://doi.org/10.2514/6.1988-4503
[research_beaverstock_woods_2015]: https://doi.org/10.3390/aerospace2030524
[research_becht_1950]: https://ntrs.nasa.gov/citations/19930086394
[research_becht_few_1950]: https://ntrs.nasa.gov/citations/19930086242
[research_beeler_1956]: https://ntrs.nasa.gov/citations/19930084521
[research_befus_nelson_1987]: https://doi.org/10.4271/871044
[research_begnini_bones_2018]: https://doi.org/10.2514/6.2018-3004
[research_beh_hofinger_2018]: https://doi.org/10.1201/9781315136820-15
[research_beissner_1984]: https://ntrs.nasa.gov/citations/19840015553
[research_belesiotiskataras_timme_2021]: https://doi.org/10.2514/6.2021-0611
[research_belisle_neale_2010]: https://doi.org/10.2514/6.2010-4381
[research_belisle_roberts_2012]: https://doi.org/10.2514/6.2012-2667
[research_bellman_1953]: https://ntrs.nasa.gov/citations/19930087480
[research_bellman_1959]: https://ntrs.nasa.gov/citations/19980228028
[research_belotserkovskii_nisht_1974]: https://doi.org/10.1007/bf01031317
[research_benaouali_kachel_2017]: https://doi.org/10.1109/icmae.2017.8038692
[research_benasher_raveh_2023]: https://doi.org/10.2514/6.2023-1309
[research_bender_westphal_2010]: https://doi.org/10.2514/6.2010-4360
[research_bendiksen_2008]: https://doi.org/10.2514/1.29547
[research_benepe_cunningham_1975]: https://ntrs.nasa.gov/citations/19750036197
[research_benepe_cunningham_1978]: https://ntrs.nasa.gov/citations/19780025173
[research_bengida_gurka_2019]: https://doi.org/10.2514/6.2019-3492
[research_bengida_gurka_2022]: https://doi.org/10.1088/1748-3190/ac9bb5
[research_benjamin_hesse_2021]: https://doi.org/10.2514/6.2021-2517
[research_bennett_1981]: https://ntrs.nasa.gov/citations/19810016531
[research_bennett_batina_1988]: https://ntrs.nasa.gov/citations/19880010035
[research_bennett_batina_1989]: https://ntrs.nasa.gov/citations/19900046299
[research_bennett_lawson_2017]: https://doi.org/10.2514/6.2017-3652
[research_bennett_lawson_2018]: https://doi.org/10.1016/j.paerosci.2018.06.001
[research_bennett_yates_1963]: https://ntrs.nasa.gov/citations/19630006419
[research_beppu_curtiss_1966]: https://doi.org/10.21236/ad0640945
[research_bera_1974]: https://doi.org/10.2514/3.44413
[research_berci_2017]: https://doi.org/10.1063/1.4992672
[research_bergman_1979]: https://doi.org/10.2514/6.1979-1812
[research_berman_1947]: https://ntrs.nasa.gov/citations/20050019623
[research_berman_1948]: https://ntrs.nasa.gov/citations/20050030037
[research_berman_1949]: https://ntrs.nasa.gov/citations/20090026468
[research_berman_1949_b]: https://ntrs.nasa.gov/citations/20090026525
[research_berman_pumphrey_1950]: https://ntrs.nasa.gov/citations/20050080688
[research_bernstein_hamid_1995]: https://doi.org/10.1017/s0001924000028475
[research_berrier_1980]: https://ntrs.nasa.gov/citations/19810010604
[research_bertelrud_1979]: https://doi.org/10.2514/3.58599
[research_bertelrud_1980]: https://doi.org/10.2514/6.1980-423
[research_bertelrud_1981]: https://doi.org/10.2514/6.1981-2418
[research_bertelrud_1981_b]: https://doi.org/10.2514/6.1981-1216
[research_bertelrud_graves_1994]: https://doi.org/10.2514/6.1994-2152
[research_bertelrud_nordstrom_1983]: https://doi.org/10.2514/6.1983-1762
[research_beyak_choudhari]: https://ntrs.nasa.gov/citations/20230016659
[research_beyak_choudhari_2024]: https://doi.org/10.2514/6.2024-2518
[research_beyers_brown_2006]: https://doi.org/10.2514/6.2006-6001
[research_beyers_ericsson_2002]: https://doi.org/10.2514/2.2989
[research_bhat_2018]: https://doi.org/10.1201/9781315370613-9
[research_biber_2016]: https://doi.org/10.2514/6.2016-0806
[research_bidwell_1991]: https://doi.org/10.2514/6.1991-447
[research_bidwell_2014]: https://doi.org/10.2514/6.2014-2200
[research_bidwell_mohleryrjr_1995]: https://doi.org/10.2514/6.1995-755
[research_bielat_1960]: https://ntrs.nasa.gov/citations/19650017034
[research_bielat_campbell_1953]: https://ntrs.nasa.gov/citations/19930087724
[research_bielat_wiley_1959]: https://ntrs.nasa.gov/citations/19980227088
[research_bihrle_1976]: https://ntrs.nasa.gov/citations/19760020126
[research_bihrlejr_1969]: https://doi.org/10.2514/6.1969-894
[research_bilgen_kochersberger_2007]: https://doi.org/10.2514/6.2007-2741
[research_binbai_chaoyangdong_2013]: https://doi.org/10.1109/iscid.2013.44
[research_bing_wei_2024]: https://doi.org/10.59782/sidr.v5i1.163
[research_bippes_1990]: https://doi.org/10.1007/978-3-642-84103-3_38
[research_bippes_lerche_1997]: https://doi.org/10.2514/6.1997-1906
[research_birchfield_1970]: https://doi.org/10.2514/6.1970-80
[research_bird_1949]: https://ntrs.nasa.gov/citations/19930082499
[research_bird_1951]: https://ntrs.nasa.gov/citations/19930092084
[research_bird_1951_2]: https://ntrs.nasa.gov/citations/19930083055
[research_bird_1952]: https://ntrs.nasa.gov/citations/19930083189
[research_bird_1973]: https://doi.org/10.1108/eb035002
[research_biriukov_1959]: https://doi.org/10.1016/0021-8928(59)90174-1
[research_birk_smith_1986]: https://ntrs.nasa.gov/citations/19870060565
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_bishay_2019]: https://doi.org/10.3390/designs3010012
[research_black_1956]: https://doi.org/10.1017/s0368393100132390
[research_black_beamish_1975]: https://ntrs.nasa.gov/citations/19800003809
[research_blair_robinson_2008]: https://doi.org/10.21236/ada482613
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_blanchard_1981]: https://ntrs.nasa.gov/citations/19810012555
[research_bland_1980]: https://doi.org/10.2514/3.44684
[research_blight_lanedailey_2018]: https://doi.org/10.1201/9781315136820-9
[research_blondeau_pines_2004]: https://doi.org/10.2514/6.2004-1808
[research_bloy_1996]: https://doi.org/10.1177/030641909602400305
[research_bobbitt_foughner_1985]: https://ntrs.nasa.gov/citations/19860053591
[research_boden_lanari_2013]: https://doi.org/10.1007/978-3-642-34738-2_5
[research_bodonyl_1994]: https://doi.org/10.21236/ada281526
[research_boehm_flick_2001]: https://doi.org/10.2514/6.2001-1372
[research_bohlmann_1989]: https://ntrs.nasa.gov/citations/19890009883
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmann_weisshaar_1988]: https://ntrs.nasa.gov/citations/19880044993
[research_bohnisch_braun_2024]: https://doi.org/10.2514/1.c037542
[research_bohon_dixon_1964]: https://doi.org/10.2514/3.43594
[research_boiko_2002]: https://doi.org/10.1023/a:1015126631538
[research_boiko_borodulin_2021]: https://doi.org/10.1088/1742-6596/2057/1/012081
[research_boiko_kirilovskiy_2024]: https://doi.org/10.3390/fluids9040095
[research_boiko_kirilovskiy_2024_b]: https://doi.org/10.1134/s0869864324020057
[research_boiko_kozlov_1995]: https://doi.org/10.1007/978-3-642-79765-1_34
[research_boisseau_paulson_1956]: https://ntrs.nasa.gov/citations/19660024811
[research_bolding_stearman_1976]: https://ntrs.nasa.gov/citations/19770014087
[research_boling_zha_2021]: https://doi.org/10.2514/6.2021-1732
[research_bolonkin_gilyard_1999]: https://ntrs.nasa.gov/citations/19990090019
[research_boltz_1960]: https://ntrs.nasa.gov/citations/19980227185
[research_boltz_pena_1977]: https://ntrs.nasa.gov/citations/19780007113
[research_bolzon_kelso_2016]: https://doi.org/10.1051/epjconf/201611402150
[research_bond_canfield_2010]: https://doi.org/10.2514/1.41140
[research_bonnema_lokos_1989]: https://ntrs.nasa.gov/citations/19910035087
[research_bonnema_smith_1988]: https://doi.org/10.2514/6.1988-2118
[research_boothe_fitzpatrick_2005]: https://doi.org/10.2514/6.2005-2374
[research_boppe_aidala_1980]: https://ntrs.nasa.gov/citations/19810007501
[research_borden_2004]: https://doi.org/10.21236/ada426342
[research_bore_boyd_1963]: https://doi.org/10.1017/s0368393100078408
[research_borglund_kroo_2002]: https://doi.org/10.2514/2.3038
[research_borodulin_2026]: https://doi.org/10.1134/s086986432504002x
[research_borodulin_ivanov_2015]: https://doi.org/10.1016/j.piutam.2015.03.051
[research_borodulin_ivanov_2016]: https://doi.org/10.1063/1.4964007
[research_borodulin_ivanov_2016_b]: https://doi.org/10.1063/1.4963996
[research_borodulin_ivanov_2017]: https://doi.org/10.1063/1.4999952
[research_borodulin_ivanov_2018]: https://doi.org/10.1088/1742-6596/1129/1/012008
[research_borodulin_ivanov_2019]: https://doi.org/10.1063/1.5094609
[research_borodulin_ivanov_2019_b]: https://doi.org/10.1063/1.5125812
[research_borodulin_ivanov_2020]: https://doi.org/10.1088/1742-6596/1677/1/012006
[research_borodulin_ivanov_2022]: https://doi.org/10.2139/ssrn.4269005
[research_borodulin_ivanov_2023]: https://doi.org/10.1016/j.euromechflu.2023.04.001
[research_borodulin_ivanov_2023_b]: https://doi.org/10.1016/j.euromechflu.2023.04.007
[research_borodulin_ivanov_2024]: https://doi.org/10.1134/s0021894424040114
[research_borodulin_ivanov_2026]: https://doi.org/10.1134/s0869864325050014
[research_borodulin_kachanov_2025]: https://doi.org/10.1134/s0021894425700671
[research_bosak_eric_2026]: https://doi.org/10.1109/icuas69441.2026.11598603
[research_boskovic_redding_2009]: https://doi.org/10.2514/6.2009-5759
[research_boston_arrieta_2021]: https://doi.org/10.2514/6.2021-0479
[research_boston_phillips_2022]: https://doi.org/10.2514/6.2022-0319
[research_boswinkle_smith_1958]: https://ntrs.nasa.gov/citations/19660027826
[research_bosworth_cox_1989]: https://doi.org/10.2514/6.1989-3428
[research_botez_grigorie_2011]: https://doi.org/10.2514/6.2011-7071
[research_botez_kammegne_2015]: https://doi.org/10.1017/s0001924000011131
[research_bottai_campbell_2022]: https://doi.org/10.2514/6.2022-2537
[research_botter]: https://doi.org/10.14393/ufu.di.2023.388
[research_bouadi]: https://doi.org/10.70675/aa62b2a6zce9ez41fcz95cdz6ebfead4b829
[research_boudreault_1983]: https://doi.org/10.2514/6.1983-2446
[research_boudreault_1983_b]: https://doi.org/10.2514/6.1983-2558
[research_boughou_batistic_2025]: https://doi.org/10.2514/6.2025-0283
[research_bourdin_2001]: https://doi.org/10.4271/2001-01-2978
[research_bourdin_2002]: https://doi.org/10.2514/6.2002-3151
[research_bourdin_gatto_2006]: https://doi.org/10.2514/6.2006-3660
[research_bourdin_gatto_2007]: https://doi.org/10.2514/6.2007-4443
[research_bourgaultcote_laurendeau_2015]: https://doi.org/10.2514/6.2015-0535
[research_bouton_1950]: https://doi.org/10.2514/8.1573
[research_bowers_murillo_2021]: https://ntrs.nasa.gov/citations/20210014683
[research_bowman_1955]: https://ntrs.nasa.gov/citations/20050029375
[research_bowman_1955_b]: https://ntrs.nasa.gov/citations/20050030035
[research_bowman_1956]: https://ntrs.nasa.gov/citations/20050028485
[research_bowman_1956_b]: https://ntrs.nasa.gov/citations/20050028470
[research_bowman_1957]: https://ntrs.nasa.gov/citations/20050028487
[research_bowman_1958]: https://ntrs.nasa.gov/citations/20050028501
[research_bowman_1959]: https://ntrs.nasa.gov/citations/19980228366
[research_bowman_1960]: https://ntrs.nasa.gov/citations/19980223580
[research_bowman_1965]: https://ntrs.nasa.gov/citations/19650021527
[research_bowman_1965_b]: https://ntrs.nasa.gov/citations/19980228384
[research_bowman_1966]: https://ntrs.nasa.gov/citations/19660043787
[research_bowman_1971]: https://ntrs.nasa.gov/citations/19720005341
[research_bowman_1974]: https://ntrs.nasa.gov/citations/20000021277
[research_bowman_2003]: https://doi.org/10.2514/6.2003-1713
[research_bowman_burk_1973]: https://ntrs.nasa.gov/citations/19730049876
[research_bowman_burk_1974]: https://ntrs.nasa.gov/citations/19740045984
[research_bowman_chambers_1970]: https://ntrs.nasa.gov/citations/19700052914
[research_bowman_healy_1958]: https://ntrs.nasa.gov/citations/19980228403
[research_bowman_healy_1959]: https://ntrs.nasa.gov/citations/19980227178
[research_bowman_sanders_2002]: https://doi.org/10.2514/6.2002-1631
[research_bowman_sanders_2007]: https://doi.org/10.2514/6.2007-1730
[research_bowman_whipple_1987]: https://ntrs.nasa.gov/citations/19870010807
[research_bowmanjr_stough_1978]: https://doi.org/10.2514/6.1978-1477
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boyden_1978]: https://ntrs.nasa.gov/citations/19780012118
[research_bradley_haughn_2026]: https://doi.org/10.2514/1.c038700
[research_bradley_honrath_1976]: https://ntrs.nasa.gov/citations/19770003103
[research_bradshaw_1980]: https://ntrs.nasa.gov/citations/19800011745
[research_bradshaw_pontikos_1985]: https://doi.org/10.1017/s0022112085003123
[research_brady_maier_1954]: https://doi.org/10.21236/ad0055205
[research_bragg_khodadoust_1991]: https://doi.org/10.2514/6.1991-442
[research_bragg_soltani_1990]: https://doi.org/10.2514/3.45928
[research_braginsky_2020]: https://doi.org/10.21203/rs.3.rs-51613/v1
[research_bramantya_nugroho_2025]: https://doi.org/10.14710/teknik.v46i3.54148
[research_brandon_brown_1995]: https://doi.org/10.2514/6.1995-3457
[research_brandt_bons_2023]: https://doi.org/10.2514/6.2023-4309
[research_brandt_bons_2024]: https://doi.org/10.2514/6.2024-0693
[research_brandt_fossum_2011]: https://doi.org/10.2514/6.2011-7039
[research_brandt_mcfadden_2022]: https://doi.org/10.2514/6.2022-3888
[research_brandt_mcfadden_2023]: https://doi.org/10.2514/6.2023-3285
[research_braslow_1999]: https://ntrs.nasa.gov/citations/19990078750
[research_bray_1953]: https://ntrs.nasa.gov/citations/19930087758
[research_breitsamter_laschka_2001]: https://doi.org/10.2514/2.2758
[research_brenner_2007]: https://ntrs.nasa.gov/citations/20090009351
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_brewer_1951]: https://ntrs.nasa.gov/citations/19930083083
[research_brewer_1953]: https://doi.org/10.21236/ad0009365
[research_brewer_lichtenstein_1950]: https://ntrs.nasa.gov/citations/19930082672
[research_bridges_1994]: https://ntrs.nasa.gov/citations/19950016863
[research_bridges_2005]: https://doi.org/10.2514/6.2005-4839
[research_bridges_2008]: https://doi.org/10.2514/1.34919
[research_briggs_1954]: https://ntrs.nasa.gov/citations/19930088191
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brigidogonzalez_rodriguezcortes_2014]: https://doi.org/10.1109/acc.2014.6859390
[research_brinza_2024]: https://doi.org/10.2514/6.2024-2351
[research_broeren_lee_2018]: https://doi.org/10.2514/6.2018-3492
[research_broeren_lee_2020]: https://doi.org/10.2514/6.2020-2846
[research_broeren_potapczuk_2013]: https://doi.org/10.2514/6.2013-2824
[research_broeren_potapczuk_2019]: https://doi.org/10.4271/2019-01-1987
[research_broeren_woodard_2017]: https://doi.org/10.2514/6.2017-4372
[research_broering_lian_2010]: https://doi.org/10.2514/6.2010-4385
[research_browman_healy_1959]: https://ntrs.nasa.gov/citations/19980237091
[research_brown_1961]: https://doi.org/10.4271/610096
[research_browne_maldonado_2024]: https://doi.org/10.2514/6.2024-0065
[research_brownjr_1970]: https://doi.org/10.2514/6.1970-947
[research_brownjr_price_1980]: https://doi.org/10.2514/6.1980-3046
[research_brune_bogataj_1990]: https://doi.org/10.4271/901934
[research_bryson_1954]: https://doi.org/10.2514/8.2916
[research_bryson_1954_b]: https://doi.org/10.2514/8.3135
[research_bryson_rumpfkeil_2016]: https://doi.org/10.2514/6.2016-0294
[research_buchnik_karpel_2014]: https://doi.org/10.2514/6.2014-0680
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_budd_1984]: https://ntrs.nasa.gov/citations/19860014095
[research_buddhamatya_miranda_2026]: https://doi.org/10.2514/6.2026-2116
[research_buell_1957]: https://ntrs.nasa.gov/citations/19930089929
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_bui_2013]: https://doi.org/10.2514/6.2013-3032
[research_bui_2015]: https://doi.org/10.2514/1.c032883
[research_bui_2016]: https://doi.org/10.2514/6.2016-3720
[research_bui_2018]: https://ntrs.nasa.gov/citations/20180004463
[research_bui_2018_b]: https://doi.org/10.2514/6.2018-3808
[research_bulekov_teryev_1972]: https://doi.org/10.1016/s1474-6670(17)68464-7
[research_bullens_traub_2021]: https://doi.org/10.2514/1.c035888
[research_bunge_alkurdi_2016]: https://doi.org/10.2514/6.2016-3652
[research_bunge_kroo_2012]: https://doi.org/10.2514/6.2012-2771
[research_bunge_munerasavino_2015]: https://doi.org/10.2514/6.2015-3225
[research_burchill_mcdonald_2002]: https://doi.org/10.1142/9789812777973_0020
[research_burdette_martins]: https://ntrs.nasa.gov/citations/26701961190518
[research_burk_1955]: https://ntrs.nasa.gov/citations/20050029372
[research_burk_1961]: https://ntrs.nasa.gov/citations/19720075828
[research_burk_1971]: https://ntrs.nasa.gov/citations/19710028127
[research_burk_1972]: https://ntrs.nasa.gov/citations/19720019383
[research_burk_1974]: https://ntrs.nasa.gov/citations/19740022308
[research_burk_1977]: https://ntrs.nasa.gov/citations/19770026167
[research_burk_wilson_1975]: https://ntrs.nasa.gov/citations/19790022002
[research_burke_2026]: https://doi.org/10.3390/aerospace13030297
[research_burke_gatto_2025]: https://doi.org/10.21203/rs.3.rs-8216629/v1
[research_burken_alag_1986]: https://ntrs.nasa.gov/citations/19860016868
[research_burkett_1989]: https://doi.org/10.1017/s0001924000022235
[research_burkhalter_1993]: https://doi.org/10.2514/3.46447
[research_burkhalter_spring_1992]: https://doi.org/10.2514/3.46183
[research_burkhart_1980]: https://doi.org/10.2514/6.1980-741
[research_burner_goad_2008]: https://doi.org/10.2514/6.2008-6921
[research_burner_martinson_1996]: https://doi.org/10.2514/6.1996-2253
[research_burris_hutchins_1970]: https://doi.org/10.2514/6.1970-904
[research_burton_kneelandjr_1981]: https://doi.org/10.2514/6.1981-2465
[research_busan_1998]: https://doi.org/10.21236/ada340820
[research_bushnell_1990]: https://doi.org/10.2514/6.1990-1596
[research_buter_rao_1984]: https://ntrs.nasa.gov/citations/19850002610
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_1983]: https://doi.org/10.1017/s0001924000051046
[research_butler_bons_2025]: https://doi.org/10.2514/6.2025-0260
[research_buzica_biswanger_2018]: https://doi.org/10.1016/j.trpro.2018.02.005
[research_buzica_debschutz_2018]: https://doi.org/10.3390/aerospace5030098
[research_cai_su_2024]: https://doi.org/10.3390/machines12070486
[research_cai_xie_2021]: https://doi.org/10.2514/6.2021-2448
[research_cai_yang_2022]: https://doi.org/10.1049/cth2.12380
[research_cai_zheng_2026]: https://doi.org/10.1061/jaeeez.aseng-6043
[research_calicojr_fuller_1981]: https://doi.org/10.2514/6.1981-1884
[research_camello_bragg_2017]: https://doi.org/10.2514/6.2017-4373
[research_camello_lee_2016]: https://doi.org/10.2514/6.2016-3737
[research_campbell_1949]: https://ntrs.nasa.gov/citations/19930082704
[research_campbell_lynde_2016]: https://doi.org/10.2514/6.2016-4326
[research_campbell_smith_1987]: https://doi.org/10.2514/6.1987-2552
[research_campion_1954]: https://doi.org/10.1017/s0001925900001232
[research_cancro_1953]: https://ntrs.nasa.gov/citations/19930087846
[research_candida_souzadepaula_2019]: https://doi.org/10.26678/abcm.diname2019.din2019-0103
[research_cangelosi_1963]: https://doi.org/10.1111/j.1749-6632.1963.tb13283.x
[research_cao_chen_2024]: https://doi.org/10.3390/app14199048
[research_cao_lin_2025]: https://doi.org/10.2139/ssrn.5375639
[research_cao_lu_2024]: https://doi.org/10.3390/biomimetics9050263
[research_cao_lyu_2024]: https://doi.org/10.3390/act13090369
[research_carafoli_1969_b]: https://doi.org/10.1016/b978-0-08-012330-1.50007-8
[research_cardoso_suleman_2013]: https://doi.org/10.2514/6.2013-1450
[research_carlson_mabli_1965]: https://doi.org/10.2514/6.1965-740
[research_carlson_weed_1985]: https://doi.org/10.2514/6.1985-4075
[research_carlsson_2005]: https://doi.org/10.2514/1.5440
[research_carlsson_kuttenkeuler_2003]: https://doi.org/10.2514/2.3079
[research_carnegie]: https://doi.org/10.22215/etd/1993-02455
[research_carpenter_2010]: https://ntrs.nasa.gov/citations/20100002885
[research_carpenter_saric_2008]: https://doi.org/10.2514/6.2008-7335
[research_carpenter_solomon_2018]: https://doi.org/10.2514/6.2018-3809
[research_carrillocorcoles_mertens_2023]: https://doi.org/10.2514/1.c037108
[research_carter_2016]: https://doi.org/10.2514/6.2016-0535
[research_carter_2017]: https://doi.org/10.2514/6.2017-4225
[research_carter_brandt_2011]: https://doi.org/10.2514/6.2011-7037
[research_carter_vicroy_2009]: https://doi.org/10.2514/6.2009-935
[research_caruso_mendenhall_1988]: https://doi.org/10.2514/6.1988-396
[research_casacuberta_groot_2022]: https://doi.org/10.2514/6.2022-2330
[research_casacuberta_groot_2026]: https://doi.org/10.1017/jfm.2026.11854
[research_casacuberta_hickel_2023]: https://doi.org/10.1007/978-3-031-47028-8_23
[research_casey_1988]: https://doi.org/10.21236/ada195699
[research_cassetti_re_1961]: https://ntrs.nasa.gov/citations/19980227081
[research_casteel_weyl_1970]: https://doi.org/10.2514/6.1970-928
[research_castellani_cooper_2016]: https://doi.org/10.1155/2016/4805817
[research_castile_herr_1949]: https://ntrs.nasa.gov/citations/19930082707
[research_castilloacero_delaescalera_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00019-8
[research_castillozuniga_giacobinisouza_2021]: https://doi.org/10.2514/6.2021-1389
[research_castrichini_hodigeresiddaramaiah_2016]: https://doi.org/10.2514/1.c033474
[research_catalano_diodati_2024]: https://doi.org/10.2514/6.2024-3502
[research_cattafesta_iyer_1995]: https://doi.org/10.2514/3.12944
[research_cavalieri_degaspari_2024]: https://doi.org/10.2514/6.2024-2113
[research_cebeci_1974]: https://doi.org/10.2514/3.49207
[research_celi_friedmann_1988]: https://doi.org/10.2514/6.1988-2297
[research_cella_biancolini_2012]: https://doi.org/10.2514/1.c031293
[research_cen_xu_2025]: https://doi.org/10.2139/ssrn.5759948
[research_cen_xu_2026]: https://doi.org/10.2139/ssrn.6797266
[research_cetinsoy_2015]: https://doi.org/10.1109/icuas.2015.7152278
[research_chai_smart_2018]: https://doi.org/10.2514/6.2018-5400
[research_chakravarthy_grant_2009]: https://doi.org/10.2514/6.2009-6304
[research_chakravarthy_grant_2012]: https://doi.org/10.2514/1.55078
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_chambers_1981]: https://ntrs.nasa.gov/citations/19810022570
[research_chambers_bowman_1971]: https://doi.org/10.2514/3.59136
[research_chambers_stough_1986]: https://ntrs.nasa.gov/citations/19870026758
[research_chana_2000]: https://doi.org/10.2514/6.2000-5515
[research_chang_2003]: https://doi.org/10.2514/6.2003-974
[research_chang_chin_2024]: https://doi.org/10.1126/scirobotics.ado4535
[research_changchuan_2022]: https://doi.org/10.2514/1.j061138
[research_chao_vandam_2004]: https://doi.org/10.2514/6.2004-5074
[research_chaparro_fujiwara_2017]: https://doi.org/10.2514/6.2017-4221
[research_chapman_1961]: https://ntrs.nasa.gov/citations/19980228265
[research_chapter_12_1994]: https://doi.org/10.1515/9781400880034-015
[research_chapter_2_1960]: https://doi.org/10.1515/9781400874941-003
[research_chapter_3_1960]: https://doi.org/10.1515/9781400874941-004
[research_chapter_3_2005]: https://doi.org/10.1515/9781400866816-004
[research_chapter_nine_1990]: https://doi.org/10.1515/9781400860777.159
[research_chapter_seven_1990]: https://doi.org/10.1515/9781400860777.105
[research_chapter_six_1990]: https://doi.org/10.1515/9781400860777.90
[research_chapter_ten_1990]: https://doi.org/10.1515/9781400860777.200
[research_characteristic_parameters_2021]: https://doi.org/10.1017/9781009105842.006
[research_characteristic_parameters_2025]: https://doi.org/10.1017/9781009501293.006
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_che_wu_2026]: https://doi.org/10.1016/j.engappai.2026.115978
[research_cheatham_1948]: https://ntrs.nasa.gov/citations/19930093786
[research_chellangi_santhanam_2025]: https://doi.org/10.1063/5.0263964
[research_chen_2010]: https://doi.org/10.21236/ada567851
[research_chen_2018]: https://doi.org/10.1063/1.5033619
[research_chen_2023]: https://doi.org/10.54254/2753-8818/9/20240719
[research_chen_2024]: https://doi.org/10.54097/e7h7td21
[research_chen_2026]: https://doi.org/10.1093/icb/icag069
[research_chen_2026_b]: https://doi.org/10.1038/s41598-026-59369-y
[research_chen_2026_c]: https://doi.org/10.1063/12.0043506
[research_chen_barlow_1995]: https://doi.org/10.2514/6.1995-1902
[research_chen_chang_1998]: https://doi.org/10.2514/6.1998-907
[research_chen_dong_2021]: https://doi.org/10.1063/5.0039901
[research_chen_gray_2026]: https://doi.org/10.2514/6.2026-1489
[research_chen_guo_2016]: https://doi.org/10.1051/matecconf/20166501004
[research_chen_khalid_2001]: https://doi.org/10.2514/6.2001-2485
[research_chen_meng_2025]: https://doi.org/10.1016/j.ast.2025.110043
[research_chen_sulaeman_2002]: https://doi.org/10.21236/ada399365
[research_chen_vassberg_1984]: https://doi.org/10.2514/6.1984-2157
[research_chen_xiao_2026]: https://doi.org/10.1109/icmcsi67283.2026.11412783
[research_chen_yue_2015]: https://doi.org/10.5028/jatm.v7i2.416
[research_chen_zhang_2015]: https://doi.org/10.1360/sspma2015-00338
[research_chen_zhang_2024]: https://doi.org/10.1088/1742-6596/2820/1/012024
[research_cheng_1978]: https://ntrs.nasa.gov/citations/19790029975
[research_cheng_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50010-3
[research_cheng_dong_2017]: https://doi.org/10.1177/0142331217708238
[research_cheng_dong_2017_b]: https://doi.org/10.1016/j.cja.2017.01.008
[research_cheng_li_2023]: https://doi.org/10.3390/aerospace10090786
[research_cheng_meng_1979]: https://ntrs.nasa.gov/citations/19790037507
[research_cheng_meng_1980]: https://ntrs.nasa.gov/citations/19800038581
[research_cheng_song_2024]: https://doi.org/10.1061/jaeeez.aseng-5708
[research_cheng_song_2025]: https://doi.org/10.2139/ssrn.5399002
[research_cheng_yu_2026]: https://doi.org/10.1109/access.2026.3706334
[research_cheng_zhang_2025]: https://doi.org/10.2139/ssrn.5129702
[research_chernoray_dovgal_2005]: https://doi.org/10.1017/s0022112005004386
[research_chernoray_dovgal_2010]: https://doi.org/10.1007/s12650-010-0035-0
[research_chernoray_dovgal_2013]: https://doi.org/10.1615/vismechproc.2013006967
[research_chernyshev_kuryachii_2015]: https://doi.org/10.1051/eucass/201507169
[research_chester_2002]: https://doi.org/10.1016/b978-008042699-0/50031-0
[research_chetty_lakshmi_1991]: https://doi.org/10.1016/s1474-6670(17)54311-6
[research_chetty_raol_1992]: https://doi.org/10.2514/6.1992-4423
[research_cheung_folding_2020]: https://doi.org/10.2514/1.c035732
[research_cheung_rezgui_2019]: https://doi.org/10.2514/6.2019-1863
[research_cheung_rezgui_2023]: https://doi.org/10.2514/6.2023-2458
[research_chiarelli_2019]: https://doi.org/10.1155/2019/8210235
[research_childs_1953]: https://ntrs.nasa.gov/citations/19930087404
[research_childs_1986]: https://doi.org/10.2514/6.1986-474
[research_chinvorarat_watjatrakul_2024]: https://doi.org/10.1063/5.0237061
[research_chipman_malone_1977]: https://doi.org/10.2514/6.1977-453
[research_chipman_rauch_1984]: https://ntrs.nasa.gov/citations/19840013485
[research_chipman_rauch_1985]: https://ntrs.nasa.gov/citations/19850048205
[research_chipman_zislin_1982]: https://doi.org/10.2514/6.1982-684
[research_cho_2009]: https://doi.org/10.1615/tsagiscij.v40.i6.80
[research_choi_jimenez_2015]: https://doi.org/10.1016/j.ast.2015.08.011
[research_choi_kang_2016]: https://doi.org/10.3795/ksme-b.2016.40.12.785
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_choi_park_2013]: https://doi.org/10.2514/6.2013-143
[research_choosakngaongam_rapeeujjin_2024]: https://doi.org/10.37934/cfdl.16.5.18
[research_choudhari_1996]: https://doi.org/10.2514/6.1996-2137
[research_choudhari_li_2016]: https://ntrs.nasa.gov/citations/20160010793
[research_chu_gu_2022]: https://doi.org/10.1109/robio55434.2022.10011957
[research_chung_cho_2019]: https://doi.org/10.2514/6.2019-3591
[research_chuprunjr_1980]: https://doi.org/10.2514/6.1980-3031
[research_cianciarulo_schmidt_2024]: https://doi.org/10.2514/6.2024-2346
[research_ciliberti_dellavecchia_2017]: https://doi.org/10.1016/j.paerosci.2017.11.001
[research_ciliberti_nicolosi_2025]: https://doi.org/10.1186/s42774-024-00189-x
[research_cinquegrana_iuliano_2017]: https://doi.org/10.2514/6.2017-3057
[research_citurs_1984]: https://doi.org/10.21236/ada153173
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_clark_letron_1989]: https://doi.org/10.2514/3.20392
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_clarke_1976]: https://doi.org/10.1017/s0001924000034382
[research_clarke_2005]: https://ntrs.nasa.gov/citations/20050212234
[research_clarkjr_hodappjr_1972]: https://doi.org/10.2514/6.1972-1032
[research_clayton]: https://doi.org/10.31274/etd-180810-3557
[research_clements_djidjeli_2024]: https://doi.org/10.1115/1.4066487
[research_clyde_bonner_1984]: https://doi.org/10.21236/ada148355
[research_coban_2020]: https://doi.org/10.5755/j01.itc.49.1.23275
[research_cobleigh_1994]: https://doi.org/10.2514/6.1994-1803
[research_coe_cunningham_1987]: https://ntrs.nasa.gov/citations/19880003836
[research_coe_kulla_1974]: https://doi.org/10.2514/3.60383
[research_coe_perkins_1990]: https://ntrs.nasa.gov/citations/19900058865
[research_coetzee_lowenberg_2023]: https://doi.org/10.2514/6.2023-1311
[research_cole_1986]: https://doi.org/10.2514/6.1986-9
[research_cole_1986_b]: https://doi.org/10.2514/3.45399
[research_cole_1988]: https://doi.org/10.2514/3.45609
[research_cole_1988_b]: https://doi.org/10.21236/ada196247
[research_cole_1990]: https://doi.org/10.2514/6.1990-981
[research_cole_1991]: https://ntrs.nasa.gov/citations/19920004240
[research_colella_bernadini_2012]: https://doi.org/10.2514/1.c031639
[research_collar_1946]: https://doi.org/10.1017/s0368393100120358
[research_collier_bartlett_1990]: https://ntrs.nasa.gov/citations/19910055306
[research_colorado_rossi_2015]: https://doi.org/10.1080/01691864.2015.1082501
[research_complete_model]: https://doi.org/10.1007/bfb0043101
[research_computational_methods_1989]: https://doi.org/10.2514/5.9781600865947.0211.0261
[research_concepts_and_2021]: https://doi.org/10.1017/9781139094672.005
[research_conner_foster_1947]: https://ntrs.nasa.gov/citations/19930085822
[research_control_allocation_2016]: https://doi.org/10.1002/9781118827789.ch8
[research_cook_1968]: https://ntrs.nasa.gov/citations/19680027893
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_cooke_mughal_2019]: https://doi.org/10.2514/6.2019-3533
[research_cooper_2023]: https://doi.org/10.52843/cassyni.czz9tq
[research_cooper_stroud_1972]: https://doi.org/10.2514/3.44341
[research_cornellaeronauticallabincbuffalony_1953]: https://doi.org/10.21236/ad0006796
[research_cornette_1961]: https://ntrs.nasa.gov/citations/20040003909
[research_correia_silva_2009]: https://doi.org/10.2514/6.2009-746
[research_cosenza_vos_2017]: https://doi.org/10.2514/6.2017-3763
[research_costello_2009]: https://doi.org/10.21236/ada590188
[research_costigan_calico_1989]: https://doi.org/10.2514/6.1989-17
[research_couillaud]: https://doi.org/10.31979/etd.r4b9-r6zv
[research_courchesne_popov_2010]: https://doi.org/10.2514/6.2010-56
[research_cousteix_pailhas_1983]: https://doi.org/10.1007/978-3-642-81991-9_21
[research_coutu_brailovski_2009]: https://doi.org/10.2514/1.40657
[research_coutu_brailovski_2011]: https://doi.org/10.2514/1.c000232
[research_covell_wood_1987]: https://doi.org/10.2514/6.1987-2475
[research_covert_1984]: https://doi.org/10.2514/6.1984-611
[research_coward_hall_1996]: https://doi.org/10.1017/s0022112096008919
[research_craig_1976]: https://ntrs.nasa.gov/citations/19760019133
[research_creel_1991]: https://doi.org/10.2514/6.1991-66
[research_creel_malik_1987]: https://doi.org/10.4271/871858
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_crittenden_weisshaar_1977]: https://ntrs.nasa.gov/citations/19770042959
[research_croom_1957]: https://ntrs.nasa.gov/citations/19930084891
[research_croom_1957_2]: https://ntrs.nasa.gov/citations/19930084918
[research_croom_huffman_1957]: https://ntrs.nasa.gov/citations/19930085060
[research_crossley_2005]: https://ntrs.nasa.gov/citations/20050238444
[research_crossley_cook_2001]: https://ntrs.nasa.gov/citations/20010069500
[research_crossley_skillen_2011]: https://doi.org/10.2514/1.c031180
[research_crouch_garbaruk_2018]: https://doi.org/10.2514/6.2018-3229
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_cui_2026]: https://doi.org/10.1016/j.ast.2026.112009
[research_cuji_garcia_2008]: https://doi.org/10.1115/smasis2008-424
[research_culler_farnsworth_2019]: https://doi.org/10.2514/6.2019-1394
[research_cummings_sandlin_1987]: https://doi.org/10.2514/6.1987-2497
[research_cumpsty_head_1967]: https://doi.org/10.1017/s0001925900004169
[research_cumpsty_head_1967_b]: https://doi.org/10.1017/s0001925900004066
[research_cunis]: https://doi.org/10.70675/5f4b14cez5181z4604zaf8dz27dc1744e316
[research_cunningham_1951]: https://ntrs.nasa.gov/citations/19930083178
[research_cunningham_batina_1987]: https://ntrs.nasa.gov/citations/19880064102
[research_cunningham_batina_1988]: https://ntrs.nasa.gov/citations/19880005583
[research_cunningham_coe_1990]: https://ntrs.nasa.gov/citations/19910005022
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_currao_yeh_2026]: https://doi.org/10.2139/ssrn.6450319
[research_curriston_white_2025]: https://doi.org/10.2514/1.c038081
[research_curry_sim_1982]: https://ntrs.nasa.gov/citations/19820055571
[research_curry_sim_1983]: https://doi.org/10.2514/3.44909
[research_curry_sim_1984]: https://ntrs.nasa.gov/citations/19870000670
[research_curtiss_hc_1967]: https://doi.org/10.21236/ad0663848
[research_cusher_gopalarathnam_2012]: https://doi.org/10.2514/1.c031454
[research_cvetkovi_radakovi_2012]: https://doi.org/10.5772/34715
[research_dag_ozgur_2026]: https://doi.org/10.30518/jav.1895788
[research_dagenhart_1989]: https://ntrs.nasa.gov/citations/19890054743
[research_dagenhart_1990]: https://ntrs.nasa.gov/citations/19910055309
[research_dagenhart_1992]: https://ntrs.nasa.gov/citations/19930012630
[research_dagenhart_saric_1999]: https://ntrs.nasa.gov/citations/19990056592
[research_daguanno_campspons_2022]: https://doi.org/10.2514/6.2022-1807
[research_daguanno_schrijer_2022]: https://doi.org/10.2514/1.j061974
[research_dai_mpc_2021]: https://doi.org/10.1109/access.2021.3074912
[research_dai_sweep_2020]: https://doi.org/10.1016/j.ast.2020.105703
[research_dai_yan_2020]: https://doi.org/10.1109/icmcce51767.2020.00165
[research_dalcarobo_fensterseifer_2010]: https://doi.org/10.4271/2010-36-0513
[research_dam_planform_2022]: https://doi.org/10.1108/aeat-10-2021-0311
[research_damstrom_mayes_1970]: https://doi.org/10.2514/6.1970-341
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandwani_bragadoaldana_2025]: https://doi.org/10.2514/6.2025-3426
[research_dannenberg_1950]: https://ntrs.nasa.gov/citations/19930082775
[research_dansberry_rivera_1990]: https://ntrs.nasa.gov/citations/19900013239
[research_dantsker_vahora_2018]: https://doi.org/10.2514/6.2018-4219
[research_darida_smrcek_1998]: https://doi.org/10.2514/6.1998-2532
[research_das_venkatraman_2021]: https://doi.org/10.2514/6.2021-0730
[research_das_wichmann_2004]: https://doi.org/10.1016/j.ast.2004.05.001
[research_david_seifert_2012]: https://doi.org/10.1016/j.ijheatfluidflow.2012.05.006
[research_davies_2020]: https://doi.org/10.1201/9780429261152-8
[research_davies_2025]: https://doi.org/10.1201/9781032692883-9
[research_davis_1952]: https://doi.org/10.2514/8.2275
[research_davis_1969]: https://doi.org/10.2514/6.1969-57
[research_davis_spedding_2015]: https://doi.org/10.2514/6.2015-0027
[research_dawson_fortin_1987]: https://ntrs.nasa.gov/citations/19880003104
[research_de_2020]: https://doi.org/10.22214/ijraset.2020.32388
[research_deandrea_roache_1991]: https://doi.org/10.2514/6.1991-5
[research_deangelis_1981]: https://doi.org/10.2514/6.1981-2450
[research_deangelis_1982]: https://doi.org/10.2514/3.44816
[research_debreuker_abdalla_2007]: https://doi.org/10.1117/12.716731
[research_decamp_hardy_1984]: https://doi.org/10.2514/6.1984-2088
[research_definition_of_1954]: https://doi.org/10.59161/cgpm1954res4e
[research_degaspari_ricci_2015]: https://doi.org/10.1155/2015/325724
[research_degaspari_riccobene_2018]: https://doi.org/10.2514/1.c034860
[research_dehaan_1990]: https://doi.org/10.2514/6.1990-3062
[research_dejarnette_jones_1978]: https://doi.org/10.21236/ada055846
[research_dejong_mulder_1987]: https://doi.org/10.2514/3.45454
[research_delfrate_1992]: https://doi.org/10.1007/978-3-642-84824-7_44
[research_delgado_datta_2026]: https://doi.org/10.2514/1.c038396
[research_delgadoregis_mattos_2004]: https://doi.org/10.2514/6.2004-5192
[research_delplanche_greil_2026]: https://doi.org/10.1098/rspb.2026.0187
[research_demasi_2007]: https://doi.org/10.2514/1.21884
[research_demasi_dipace_2014]: https://doi.org/10.2514/6.2014-0901
[research_demasi_dipace_2014_b]: https://doi.org/10.2514/1.j052837
[research_demasi_monegato_2016]: https://doi.org/10.2514/6.2016-0236
[research_demelo_bussamra_2024]: https://doi.org/10.21203/rs.3.rs-3761279/v1
[research_denegri_2009]: https://doi.org/10.2514/1.42777
[research_denegri_sharma_2021]: https://doi.org/10.2514/1.c035850
[research_deng_qin_2013]: https://doi.org/10.1007/s11431-013-5345-8
[research_deng_wang_2022]: https://doi.org/10.1016/j.ast.2022.107935
[research_denham_owens_2016]: https://ntrs.nasa.gov/citations/20160010112
[research_denison_garai_2019]: https://doi.org/10.2514/6.2019-3534
[research_derosa_donelli_2020]: https://doi.org/10.59972/0ju4twsp
[research_design_objectives]: https://doi.org/10.4271/arp4104
[research_design_objectives_b]: https://doi.org/10.4271/arp842a
[research_design_of_1979]: https://doi.org/10.2514/6.1979-1842
[research_designing_airplane_2025]: https://doi.org/10.11129/9783955536510-011
[research_desmarais_reediii_1980]: https://doi.org/10.2514/6.1980-792
[research_development_of_2014]: https://doi.org/10.2514/5.9781624102547.0661.0664
[research_devincentiis_henningson_2021]: https://doi.org/10.1017/jfm.2021.962
[research_devoogt_ganapathisubramani_2022]: https://doi.org/10.1017/flo.2022.11
[research_dewart_jr_1958]: https://doi.org/10.21236/ad0155543
[research_deyoung_1947]: https://ntrs.nasa.gov/citations/19930082544
[research_dicarlo_brown_1992]: https://doi.org/10.2514/6.1992-4094
[research_dicarlo_glover_1984]: https://ntrs.nasa.gov/citations/19840036474
[research_dicarlo_johnson_1979]: https://ntrs.nasa.gov/citations/19790063895
[research_dickey_1959]: https://ntrs.nasa.gov/citations/19980231999
[research_diebold_bragg_2015]: https://doi.org/10.2514/1.j053774
[research_diebold_broeren_2013]: https://doi.org/10.2514/6.2013-2825
[research_diebold_monastero_2012]: https://doi.org/10.2514/6.2012-2795
[research_diederich_budiansky_1948]: https://ntrs.nasa.gov/citations/19930082318
[research_diederich_zlotnick_1949]: https://ntrs.nasa.gov/citations/19930082642
[research_difranco_1969]: https://doi.org/10.2514/6.1969-768
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_dikbas_atik_2018]: https://doi.org/10.2514/6.2018-4127
[research_dillinger_abdalla_2019]: https://doi.org/10.1007/s13272-019-00397-y
[research_dimino_amendola_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00022-8
[research_dimino_ciminello_2015]: https://doi.org/10.1007/978-3-319-22413-8_9
[research_dimino_diodati_2016]: https://doi.org/10.1117/12.2219223
[research_dimino_flauto_2014]: https://doi.org/10.2174/2212797607666140429005538
[research_dimino_gallorini_2019]: https://doi.org/10.3390/act8020042
[research_ding_2023]: https://doi.org/10.1088/1742-6596/2457/1/012003
[research_dipalma_gandhi_2016]: https://doi.org/10.2514/6.2016-1315
[research_directional_control_2003]: https://doi.org/10.2514/5.9781600861840.0341.0358
[research_distributed_surface_vortex_receptivity_2025]: https://doi.org/10.15372/pmtf202415595
[research_distributed_surface_vortex_receptivity_2025_b]: https://doi.org/10.15372/pmtf202415596
[research_dive_testing_2003]: https://doi.org/10.2514/5.9781600861840.0417.0426
[research_dizdarevic_2013]: https://doi.org/10.2514/6.2013-4325
[research_djahid_elena_2022]: https://doi.org/10.3390/fluids7110340
[research_djojodihardjo_2023]: https://doi.org/10.1007/978-981-16-8078-6_19
[research_dobbs_miller_1985]: https://doi.org/10.2514/6.1985-739
[research_dodbele_plotkin_1985]: https://doi.org/10.2514/6.1985-1588
[research_doggett_farmer_1976]: https://ntrs.nasa.gov/citations/19770007045
[research_doggett_morgan_1959]: https://ntrs.nasa.gov/citations/19660024036
[research_doggettjr_ricketts_1977]: https://doi.org/10.2514/6.1977-422
[research_dollyhigh_1970]: https://doi.org/10.2514/6.1970-932
[research_donati_pacheco_2026]: https://doi.org/10.2514/1.c038845
[research_dong_choi_2022]: https://doi.org/10.1017/jfm.2022.451
[research_dong_li_2013]: https://doi.org/10.1016/j.proeng.2013.12.009
[research_dong_sun_2011]: https://doi.org/10.4028/www.scientific.net/amr.228-229.169
[research_dong_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9018914
[research_dongmo_2011]: https://doi.org/10.2514/6.2011-1562
[research_donlan_sleeman_1976]: https://ntrs.nasa.gov/citations/19770022130
[research_dovale_afonso_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00004-6
[research_dovejay_2014]: https://doi.org/10.64628/ab.h6atxjuyt
[research_dowell_1996]: https://doi.org/10.21236/ada325524
[research_dowell_1999]: https://doi.org/10.21236/ada362982
[research_dowell_hall_2003]: https://doi.org/10.21236/ada426408
[research_downs_1993]: https://ntrs.nasa.gov/citations/19940020492
[research_downs_prazenica_2022]: https://doi.org/10.2514/6.2022-1729
[research_downs_prazenica_2023]: https://doi.org/10.2514/6.2023-0130
[research_drachinsky_avin_2022]: https://doi.org/10.2514/6.2022-2186
[research_drag_reduction_2011]: https://doi.org/10.14741/ijcet/22774106/6.4.2016.3
[research_drake_solomon_2010]: https://doi.org/10.2514/6.2010-4571
[research_draper_1950]: https://ntrs.nasa.gov/citations/19930086383
[research_dryasov_yermolaev_2016]: https://doi.org/10.54362/1818-7919-2016-11-1-16-22
[research_du_2026]: https://doi.org/10.3390/aerospace13060562
[research_duan_choudhari_2013]: https://doi.org/10.2514/6.2013-2617
[research_duc_sesterhenn_2004]: https://doi.org/10.1007/978-3-540-45060-3_11
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dugundji_dowell_1962]: https://doi.org/10.21236/ad0278235
[research_dugundji_ghareeb_1965]: https://doi.org/10.2514/6.1965-113
[research_dumont_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00005-8
[research_duncan_crawford_2013]: https://doi.org/10.2514/6.2013-2412
[research_duranferreras_2009]: https://doi.org/10.2514/6.2009-5687
[research_durfee_1919]: https://doi.org/10.1038/scientificamerican12201919-367supp
[research_durmus_kaya_2021]: https://doi.org/10.23967/wccm-eccomas.2020.128
[research_durmus_kaya_2023]: https://doi.org/10.1007/978-3-031-37943-7_3
[research_dussart_roll_2019]: https://doi.org/10.3390/aerospace6060063
[research_dussart_xb70_2019]: https://doi.org/10.15394/ijaaa.2019.1343
[research_dussart_yusuf_2018]: https://doi.org/10.2514/6.2018-1683
[research_dynamic_lateral_directional_2003]: https://doi.org/10.2514/5.9781600861840.0311.0322
[research_dynamic_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0247.0254
[research_dynamic_longitudinal_2003_b]: https://doi.org/10.2514/5.9781600861840.0235.0246
[research_dynamic_stability]: https://doi.org/10.1007/978-3-540-46573-7_11
[research_dynamics_of_2015]: https://doi.org/10.2307/j.ctt1287kgx.6
[research_dynamics_of_2023]: https://doi.org/10.1017/9781108354868.010
[research_eckert_1973]: https://ntrs.nasa.gov/citations/19740004601
[research_eckert_maki_1973]: https://ntrs.nasa.gov/citations/19730023208
[research_economou_2025]: https://doi.org/10.32920/29170433.v1
[research_edwards_1992]: https://doi.org/10.2514/6.1992-4002
[research_edwards_1996]: https://ntrs.nasa.gov/citations/19960054470
[research_edwards_1998]: https://ntrs.nasa.gov/citations/19980202470
[research_effect_of_2019]: https://doi.org/10.35940/ijrte.b1184.0782s319
[research_efremov_ogloblin_1998]: https://doi.org/10.2514/6.1998-4145
[research_ekaterinaris_schiff_1994]: https://doi.org/10.2514/3.46608
[research_elakoury_aboukhalil_2026]: https://doi.org/10.2139/ssrn.6584548
[research_elelwi_calvet_2021]: https://doi.org/10.1017/aer.2021.29
[research_elelwi_span_2020]: https://doi.org/10.1017/aer.2020.19
[research_elelwi_topology_2021]: https://doi.org/10.3390/biomimetics6040055
[research_elelwi_weight_2022]: https://doi.org/10.3390/act11050121
[research_elements_of_2013]: https://doi.org/10.1002/9781118568101.ch10
[research_elham_timmer_2016]: https://doi.org/10.2514/6.2016-0160
[research_eliasson_2008]: https://doi.org/10.2514/1.34054
[research_elkhoury_nakad_2009]: https://doi.org/10.2514/1.42154
[research_ellis_2025]: https://doi.org/10.2514/1.c038141
[research_ellis_maris_1977]: https://doi.org/10.2514/6.1977-1210
[research_elramly]: https://doi.org/10.22215/etd/1975-00290
[research_elramly_rainbird_1977]: https://doi.org/10.2514/3.58783
[research_elsalamony_aziz_2020]: https://doi.org/10.1142/s2301385021500138
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_elsloo_rooij_2025]: https://doi.org/10.21203/rs.3.rs-6170299/v1
[research_enciu_2025]: https://doi.org/10.3390/math13101614
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_engelbrecht]: https://doi.org/10.31274/rtd-180813-14663
[research_engelbrecht_pauck_2012]: https://doi.org/10.2514/6.2012-4801
[research_england_1975]: https://doi.org/10.21236/ada018751
[research_englar_1975]: https://doi.org/10.2514/3.59824
[research_english_1953]: https://ntrs.nasa.gov/citations/19930081603
[research_enns_2015]: https://doi.org/10.1007/978-1-4471-5058-9_20
[research_enns_bugajski_1988]: https://doi.org/10.1109/37.1879
[research_eppink]: https://ntrs.nasa.gov/citations/20230005921
[research_eppink_2017]: https://doi.org/10.2514/6.2017-0306
[research_eppink_2023]: https://doi.org/10.2514/6.2023-3999
[research_eppink_wlezien_2012]: https://ntrs.nasa.gov/citations/20120011821
[research_eppink_wlezien_2015]: https://doi.org/10.2514/6.2015-2776
[research_eppink_wlezien_2019]: https://doi.org/10.2514/1.j057437
[research_eppink_yao_2017]: https://doi.org/10.2514/6.2017-0305
[research_eppink_yao_2017_b]: https://doi.org/10.2514/6.2017-4415
[research_eraslan_oktay_2023]: https://doi.org/10.5755/j01.itc.52.4.33527
[research_eraslan_oktay_2024]: https://doi.org/10.28948/ngumuh.1501418
[research_erel_1988]: https://doi.org/10.2514/3.45535
[research_erickson_1979]: https://doi.org/10.2514/6.1979-1859
[research_erickson_brandon_1987]: https://doi.org/10.2514/6.1987-2617
[research_ericsson_1980]: https://doi.org/10.2514/6.1980-1801
[research_ericsson_1983]: https://doi.org/10.2514/6.1983-1810
[research_ericsson_1984]: https://doi.org/10.2514/6.1984-2177
[research_ericsson_1985]: https://doi.org/10.2514/3.45136
[research_ericsson_1986]: https://doi.org/10.2514/6.1986-1773
[research_ericsson_1987]: https://doi.org/10.2514/3.45416
[research_ericsson_1996]: https://doi.org/10.2514/6.1996-788
[research_ericsson_1996_b]: https://doi.org/10.2514/6.1996-3405
[research_ericsson_1996_c]: https://doi.org/10.2514/6.1996-3404
[research_ericsson_1997]: https://doi.org/10.2514/2.2192
[research_ericsson_1997_b]: https://doi.org/10.2514/2.2233
[research_ericsson_1998]: https://doi.org/10.2514/2.2399
[research_ericsson_1998_b]: https://doi.org/10.2514/2.2410
[research_ericsson_2003]: https://doi.org/10.2514/2.3076
[research_ericsson_ericsson_1997]: https://doi.org/10.2514/6.1997-327
[research_ericsson_king_1990]: https://doi.org/10.2514/6.1990-3037
[research_ericsson_king_1993]: https://doi.org/10.2514/3.46414
[research_ericsson_reding_1976]: https://doi.org/10.2514/6.1976-19
[research_ericsson_reding_1977]: https://doi.org/10.2514/6.1977-667
[research_ericsson_reding_1978]: https://doi.org/10.2514/3.58370
[research_ermolaev_kosinov_2018]: https://doi.org/10.1134/s0869864318050025
[research_erturk_dogan_2017]: https://doi.org/10.2514/1.c034200
[research_erzberger_1975]: https://ntrs.nasa.gov/citations/19760005964
[research_esquieu_2003]: https://doi.org/10.2514/6.2003-3659
[research_essenhigh_2006]: https://doi.org/10.1021/ef050276y
[research_estevadeordal_ullah_2022]: https://doi.org/10.2514/6.2022-1959
[research_estimating_the_2010]: https://doi.org/10.2514/5.9781600867538.0151.0169
[research_estimating_wing_body_2010]: https://doi.org/10.2514/5.9781600867538.0323.0354
[research_estimation_and_2026]: https://doi.org/10.1017/9781009399913.017
[research_evaluation_of_1981]: https://doi.org/10.2514/6.1981-606
[research_evolution_of_1980]: https://doi.org/10.2514/6.1980-3037
[research_experience_gained_2010]: https://doi.org/10.2514/5.9781600867552.0443.0543
[research_experimental_and_2024]: https://doi.org/10.47176/jafm.17.12.2732
[research_experimental_testing_1982]: https://doi.org/10.2514/5.9781600865558.0189.0238
[research_exploratory_study_1979]: https://ntrs.nasa.gov/citations/19800004771
[research_f_nonsteady_1957]: https://doi.org/10.1515/9781400879908-015
[research_fagley_seidel_2016]: https://doi.org/10.2514/6.2016-3632
[research_fala_2022]: https://doi.org/10.3390/aerospace9040178
[research_fan_li_2019]: https://doi.org/10.2514/1.c034781
[research_fan_song_2017]: https://doi.org/10.2514/6.2017-3061
[research_fan_wu_2025]: https://doi.org/10.1109/fasta65681.2025.11138796
[research_fan_yu_2021]: https://doi.org/10.2514/1.c036138
[research_farcy_khrabrov_2020]: https://doi.org/10.2514/1.c035882
[research_farhat_1998]: https://doi.org/10.21236/ada361695
[research_farhat_2000]: https://doi.org/10.21236/ada389378
[research_farhat_2001]: https://doi.org/10.21236/ada387498
[research_farmer_hanson_1976]: https://doi.org/10.2514/6.1976-1560
[research_fasel_2020]: https://doi.org/10.52843/cassyni.tbr8qg
[research_faure_2020]: https://doi.org/10.1063/5.0025327
[research_fedorov_1988]: https://doi.org/10.1007/bf00857907
[research_fedorov_2012]: https://doi.org/10.2514/6.2012-920
[research_fedorov_egorov_2021]: https://doi.org/10.1017/jfm.2021.1077
[research_fedorov_novikov_2023]: https://doi.org/10.1007/s00162-023-00658-x
[research_feedback_flight_2026]: https://doi.org/10.1017/9781009399913.013
[research_fehrs_2025]: https://doi.org/10.1007/s13272-025-00856-9
[research_feistel_anderson_1978]: https://doi.org/10.2514/6.1978-1476
[research_fejtek_jones_2001]: https://doi.org/10.2514/6.2001-2443
[research_felicio_santos_2011]: https://doi.org/10.2514/6.2011-2074
[research_felix_2026]: https://doi.org/10.2514/1.c038369
[research_feng_2025]: https://doi.org/10.1108/aeat-03-2025-0099
[research_feng_guo_2023]: https://doi.org/10.2514/1.g007591
[research_feng_wang_2020]: https://doi.org/10.1007/978-3-030-23792-9_5
[research_feng_wu_2025]: https://doi.org/10.2139/ssrn.5372627
[research_fenwick_allen_2007]: https://doi.org/10.2514/6.2007-3805
[research_ferreroguillen_diezgonzalez_2022]: https://doi.org/10.1080/01969722.2022.2030010
[research_fichera_isnardi_2019]: https://doi.org/10.3390/aerospace6020013
[research_fielding_southworth_2001]: https://doi.org/10.2514/6.2001-4263
[research_figat_2022]: https://doi.org/10.1108/aeat-12-2021-0372
[research_figat_kwiek_2023]: https://doi.org/10.1108/aeat-11-2022-0328
[research_figge_bernhardt_1975]: https://doi.org/10.2514/3.59854
[research_filippone_2006]: https://doi.org/10.2514/4.478390
[research_filippou_kilimtzidis_2024]: https://doi.org/10.20944/preprints202401.0348.v1
[research_finch_1953]: https://ntrs.nasa.gov/citations/19930087476
[research_finch_1953_2]: https://ntrs.nasa.gov/citations/19930087479
[research_finch_1955]: https://ntrs.nasa.gov/citations/19930088810
[research_finch_walker_1956]: https://ntrs.nasa.gov/citations/19930090227
[research_finistauri_2021]: https://doi.org/10.32920/ryerson.14665278
[research_finistauri_xi_2011]: https://doi.org/10.2514/6.2011-1884
[research_finistauri_xi_2012]: https://doi.org/10.2514/1.c031382
[research_firouzabadi_askarian_2013]: https://doi.org/10.1016/j.jfluidstructs.2012.09.005
[research_fischel_naeseth_1952]: https://ntrs.nasa.gov/citations/19930092133
[research_fischel_ohare_1950]: https://ntrs.nasa.gov/citations/19930086295
[research_fischel_schneiter_1948]: https://ntrs.nasa.gov/citations/19930090362
[research_fischel_watson_1949]: https://ntrs.nasa.gov/citations/19930086151
[research_fischer_ehrenstein_1989]: https://doi.org/10.1007/978-3-642-83584-1_20
[research_fischer_wrightjr_1983]: https://doi.org/10.2514/6.1983-2508
[research_fisher_1951]: https://ntrs.nasa.gov/citations/19930086565
[research_fisher_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_fisher_1958_b]: https://ntrs.nasa.gov/citations/19930092344
[research_fixed_rigid_wing_2007]: https://doi.org/10.1017/cbo9780511551154.004
[research_flanagan_strutzenberg_2007]: https://doi.org/10.2514/6.2007-1707
[research_flat_spin_2001]: https://doi.org/10.1108/ir.2001.04928aad.007
[research_flat_wings_2020]: https://doi.org/10.1002/9781119667063.ch6
[research_fletcher_clarke_2022]: https://doi.org/10.2514/6.2022-1288
[research_flexible_wing_aerodynamics_2007]: https://doi.org/10.1017/cbo9780511551154.005
[research_flight_control_1999]: https://doi.org/10.1108/aeat.1999.12771aad.001
[research_flight_control_2011]: https://doi.org/10.1049/pbce074e_ch8
[research_flight_control_2015]: https://doi.org/10.1201/b19350-7
[research_flight_dynamics_2014]: https://doi.org/10.1201/b17346-14
[research_flight_envelope]: https://doi.org/10.4271/arp4104/1
[research_flores_vandalsem_1985]: https://doi.org/10.2514/6.1985-5004
[research_floros_kang_2017]: https://doi.org/10.4050/f-0073-2017-12057
[research_flying_qualities_2003]: https://doi.org/10.2514/5.9781600861840.0359.0363
[research_fonte_iannaccone_2018]: https://doi.org/10.1115/smasis2018-8167
[research_forster_kolonay_1996]: https://doi.org/10.2514/6.1996-4010
[research_forte_nguyen_2024]: https://doi.org/10.2514/6.2024-1782
[research_foster_1948]: https://ntrs.nasa.gov/citations/19930085540
[research_foster_1960]: https://ntrs.nasa.gov/citations/19660022441
[research_foster_1960_b]: https://ntrs.nasa.gov/citations/19630007574
[research_foster_morris_1960]: https://ntrs.nasa.gov/citations/19660011612
[research_foster_morris_1961]: https://ntrs.nasa.gov/citations/19660013086
[research_foster_spearman_1959]: https://ntrs.nasa.gov/citations/19650003085
[research_fouda_taha_2022]: https://doi.org/10.2514/6.2022-1161
[research_foughner_1989]: https://ntrs.nasa.gov/citations/19910014819
[research_fournier_1961]: https://ntrs.nasa.gov/citations/19980228000
[research_fournier_silvers_1958]: https://ntrs.nasa.gov/citations/19930089979
[research_franciolini_daronch_2018]: https://doi.org/10.1016/j.ast.2017.10.034
[research_francois_cooper_2016]: https://doi.org/10.2514/6.2016-0472
[research_frazier_1991]: https://doi.org/10.2514/6.1991-3173
[research_frederick_banks_2014]: https://ntrs.nasa.gov/citations/20140010358
[research_freidmann_2001]: https://doi.org/10.2514/6.2001-1534
[research_fremaux_1997]: https://ntrs.nasa.gov/citations/19970019598
[research_fremaux_vijgen_1990]: https://ntrs.nasa.gov/citations/19900062046
[research_freudinger_1990]: https://ntrs.nasa.gov/citations/19900015819
[research_friederich_kloker_2011]: https://doi.org/10.1007/978-3-642-15748-6_18
[research_friend_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_frink_2015]: https://doi.org/10.2514/6.2015-0288
[research_friswell_2014]: https://doi.org/10.1115/smasis2014-7754
[research_frolov_2021]: https://doi.org/10.5772/intechopen.89056
[research_from_steady_2011]: https://doi.org/10.2307/j.ctvcm4h26.18
[research_from_steady_2011_b]: https://doi.org/10.1515/9781400839063-016
[research_from_tube_2013]: https://doi.org/10.1002/9781118568101.ch5
[research_frost_rutherford_1963]: https://doi.org/10.2514/3.1680
[research_fu_sun_2025]: https://doi.org/10.3390/biomimetics10050280
[research_fuchs_1930]: https://ntrs.nasa.gov/citations/19930094825
[research_fuchs_schmidt_1931]: https://ntrs.nasa.gov/citations/19930094787
[research_fugate_nguyen_2019]: https://doi.org/10.2514/6.2019-3028
[research_fujii_obayashi_1986]: https://doi.org/10.2514/6.1986-1831
[research_fujimori_2004]: https://doi.org/10.2322/tjsass.47.138
[research_fujimori_lin_1973]: https://doi.org/10.2514/6.1973-181
[research_fujimori_nikiforuk_1999]: https://doi.org/10.1016/s1474-6670(17)57358-9
[research_fujimori_terui_2003]: https://doi.org/10.2514/6.2003-5414
[research_fujimori_terui_2005]: https://doi.org/10.2514/1.5144
[research_fujimori_wu_1997]: https://doi.org/10.2514/6.1997-3760
[research_fujimori_wu_1998]: https://doi.org/10.2514/6.1998-4486
[research_fujita_motoda_2014]: https://doi.org/10.2514/6.2014-0383
[research_fujiwara_nguyen_2018]: https://doi.org/10.2514/6.2018-3571
[research_fukumoto_kouchi_2023]: https://doi.org/10.2514/6.2023-1180
[research_fuller_1967]: https://ntrs.nasa.gov/citations/19670024546
[research_fundamentals_of_2007]: https://doi.org/10.1007/978-3-540-46573-7
[research_funk_1959]: https://ntrs.nasa.gov/citations/19980228407
[research_furey_1980]: https://doi.org/10.21236/ada112312
[research_furuya_fukuchi_2001]: https://doi.org/10.2514/6.2001-1631
[research_fusato_celi_2006]: https://doi.org/10.2514/1.7943
[research_gabor_koreanschi_2013]: https://doi.org/10.2514/6.2013-5164
[research_gabor_koreanschi_2016]: https://doi.org/10.1109/icuas.2016.7502530
[research_gagnon_zingg_2016]: https://doi.org/10.2514/1.c033591
[research_gain_scheduled_2004]: https://doi.org/10.5302/j.icros.2004.10.2.125
[research_gainer_1967]: https://ntrs.nasa.gov/citations/19670008821
[research_gainer_1984]: https://ntrs.nasa.gov/citations/19840018599
[research_gale_1948]: https://ntrs.nasa.gov/citations/19930082260
[research_gale_1950]: https://ntrs.nasa.gov/citations/19930086221
[research_gallagher_1971]: https://doi.org/10.2514/3.59189
[research_gallman_smith_1990]: https://doi.org/10.2514/6.1990-3197
[research_galloway_phillips_1996]: https://ntrs.nasa.gov/citations/19960023626
[research_gally_carlson_1987]: https://doi.org/10.2514/6.1987-2551
[research_gamble_inman_2016]: https://doi.org/10.4028/www.scientific.net/ast.101.127
[research_gamboa_santos_2016]: https://doi.org/10.2514/6.2016-0317
[research_gandhi_cooper_2009]: https://doi.org/10.2514/6.2009-5890
[research_gandhi_jha_2007]: https://doi.org/10.2514/6.2007-1716
[research_ganesh_paul_2022]: https://doi.org/10.47893/gret.2022.1090
[research_gangtao_shuhaochen]: https://doi.org/10.1109/cdc.2003.1272400
[research_gano_perez_2004]: https://doi.org/10.2514/6.2004-1763
[research_gano_renaud_2002]: https://doi.org/10.2514/6.2002-5668
[research_gao_2025]: https://doi.org/10.1017/aer.2025.41
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00008-5
[research_gao_jin_2018]: https://doi.org/10.1109/access.2018.2858293
[research_gao_kang_2016]: https://doi.org/10.1007/978-981-10-2875-5_66
[research_gao_pabon_2023]: https://doi.org/10.2514/6.2023-71704
[research_gao_tandem_2022]: https://doi.org/10.3390/aerospace9080463
[research_gao_tian_2026]: https://doi.org/10.2139/ssrn.6226759
[research_gao_tyrrell_2025]: https://doi.org/10.2514/6.2025-2022
[research_gao_zhao_2015]: https://doi.org/10.1109/icinfa.2015.7279705
[research_gao_zhu_2023]: https://doi.org/10.3390/drones7090552
[research_gapcynski_landrum_1958]: https://ntrs.nasa.gov/citations/19630002621
[research_gaponenko_ivanov_1995]: https://doi.org/10.1007/978-3-642-79765-1_44
[research_gaponenko_ivanov_2002]: https://doi.org/10.1017/s0022112002008297
[research_garcia_abdulrahim_2003]: https://doi.org/10.2514/6.2003-5347
[research_garcia_slingerland_2001]: https://doi.org/10.2514/6.2001-5237
[research_gardner_1951]: https://ntrs.nasa.gov/citations/20050029468
[research_gardner_merz_2018]: https://doi.org/10.4050/f-0074-2018-12689
[research_gardner_merz_2019]: https://doi.org/10.4050/jahs.64.032007
[research_garmann_visbal_2020]: https://doi.org/10.2514/6.2020-1759
[research_garmann_visbal_2021]: https://doi.org/10.2514/6.2021-1450
[research_garmann_visbal_2022]: https://doi.org/10.2514/1.j061332
[research_garmann_visbal_2022_b]: https://doi.org/10.2514/1.j062010
[research_garmann_visbal_2023]: https://doi.org/10.2514/6.2023-0861
[research_garre_2017]: https://doi.org/10.22214/ijraset.2017.2046
[research_garrick_reed_1981]: https://doi.org/10.2514/3.57579
[research_gaster_2008]: https://doi.org/10.2514/6.2008-3833
[research_gaylor_1984]: https://doi.org/10.2514/6.1984-2489
[research_gebhardt_2017]: https://doi.org/10.2514/6.2017-3244
[research_gego_bugaj_2023]: https://doi.org/10.26552/pas.z.2023.1.22
[research_generally_on]: https://doi.org/10.1007/bfb0043100
[research_gera_1986]: https://doi.org/10.2514/6.1986-167
[research_gera_wilson_1981]: https://ntrs.nasa.gov/citations/19820030371
[research_german_development_2010]: https://doi.org/10.2514/4.867552
[research_gerontakos_lee_2005]: https://doi.org/10.1007/s00348-005-0056-y
[research_gerontakos_lee_2006]: https://doi.org/10.1007/s00348-006-0242-6
[research_gertsen_shomber_1965]: https://doi.org/10.2514/6.1965-780
[research_geva_2019]: https://doi.org/10.3390/aerospace6080085
[research_ghaemi_lax_2019]: https://doi.org/10.2514/6.2019-3617
[research_ghanem_bicer_2023]: https://doi.org/10.1109/cdc49753.2023.10384125
[research_ghasemi_mosahebi_2014]: https://doi.org/10.2514/6.2014-0557
[research_ghoreyshi_aref_2022]: https://doi.org/10.2514/6.2022-0297
[research_ghoreyshi_aref_2024]: https://doi.org/10.2514/6.2024-4158
[research_ghoreyshi_aref_2025]: https://doi.org/10.2514/1.j064753
[research_ghoreyshi_fagley_2024]: https://doi.org/10.1016/j.ast.2024.109215
[research_ghoreyshi_nangia_2022]: https://doi.org/10.2514/6.2022-0296
[research_gibson_1990]: https://doi.org/10.2514/6.1990-2844
[research_gibson_ung_1995]: https://doi.org/10.2514/6.1995-1201
[research_gilani_2023]: https://doi.org/10.32920/23328197
[research_gilbert_1980]: https://doi.org/10.2514/6.1980-1886
[research_gilbert_1981]: https://doi.org/10.2514/3.57533
[research_gilbert_schmidt_1982]: https://doi.org/10.2514/6.1982-1544
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gilbert_silva_1987]: https://ntrs.nasa.gov/citations/19870018623
[research_giles_1970]: https://doi.org/10.2514/6.1970-569
[research_giles_1972]: https://doi.org/10.2514/3.58942
[research_giles_1986]: https://doi.org/10.2514/3.45393
[research_giles_1995]: https://doi.org/10.2514/6.1995-3945
[research_gillis_1956]: https://ntrs.nasa.gov/citations/20050019449
[research_gillis_1957]: https://ntrs.nasa.gov/citations/19930092326
[research_gilman_burdges_1967]: https://doi.org/10.2514/3.43894
[research_gilyard_1972]: https://ntrs.nasa.gov/citations/19720015377
[research_gilyard_1989]: https://ntrs.nasa.gov/citations/19890009882
[research_gimmestad_1981]: https://doi.org/10.2514/6.1981-1671
[research_giunta_narducci_1995]: https://doi.org/10.2514/6.1995-1886
[research_glauert_1928]: https://doi.org/10.1098/rspa.1928.0039
[research_glauser_saric_2011]: https://doi.org/10.2514/6.2011-3076
[research_glauser_saric_2014]: https://doi.org/10.2514/1.j052479
[research_go_ramnath_2001]: https://doi.org/10.2514/6.2001-4426
[research_goetz_1961]: https://ntrs.nasa.gov/citations/19660022440
[research_goetz_doggett_1974]: https://ntrs.nasa.gov/citations/19740026253
[research_goizueta_wynn_2022]: https://doi.org/10.2514/1.c036710
[research_goland_1945]: https://doi.org/10.1115/1.4009489
[research_goland_1952]: https://doi.org/10.21236/ad0004240
[research_goland_luke_1954]: https://doi.org/10.21236/ad0050212
[research_goldschmied_1990]: https://doi.org/10.2514/6.1990-3198
[research_golovkin_gorbunov_2019]: https://doi.org/10.1615/tsagiscij.2019032577
[research_gong_ma_2019]: https://doi.org/10.1177/0954410019836907
[research_gong_ma_2019_b]: https://doi.org/10.1007/s42405-018-0110-7
[research_gong_wang_2019]: https://doi.org/10.1007/s11071-019-04834-9
[research_gong_wang_2019_b]: https://doi.org/10.1177/0020294019830434
[research_gong_wang_2020]: https://doi.org/10.1016/j.cja.2019.10.005
[research_gonsalves_zacharias_1994]: https://doi.org/10.1109/fuzzy.1994.343863
[research_goodheart_dykas_2003]: https://doi.org/10.1002/pamm.200310171
[research_goodman_wolhart_1951]: https://ntrs.nasa.gov/citations/19930083410
[research_goodrich_sliwa_1987]: https://doi.org/10.2514/6.1987-2590
[research_goodson_1966]: https://ntrs.nasa.gov/citations/19660015322
[research_goorjian_guruswamy_1985]: https://ntrs.nasa.gov/citations/19850016892
[research_gopalarathnam_mcavoy_2001]: https://doi.org/10.2514/6.2001-2409
[research_goradia_bobbitt_1989]: https://ntrs.nasa.gov/citations/19910014825
[research_goraj_baron_2002]: https://doi.org/10.1108/00022660210427422
[research_gordnier_1991]: https://doi.org/10.21236/ada244320
[research_gordnier_1995]: https://doi.org/10.2514/6.1995-82
[research_gordnier_visbal_1994]: https://doi.org/10.2514/3.46480
[research_gordnier_visbal_2003]: https://doi.org/10.2514/6.2003-620
[research_gordnier_visbal_2005]: https://doi.org/10.2514/1.5403
[research_gordnier_visbal_2006]: https://doi.org/10.2514/6.2006-504
[research_gorev_katasonov_2007]: https://doi.org/10.1134/s0015462807050067
[research_goto_obayashi_2007]: https://doi.org/10.2514/1.23236
[research_govindarajan_narasimha_2000]: https://doi.org/10.1007/978-3-662-03997-7_27
[research_gowree_atkin_2017]: https://doi.org/10.1017/aer.2017.30
[research_grafton_1966]: https://ntrs.nasa.gov/citations/19660019276
[research_grafton_anglin_1972]: https://ntrs.nasa.gov/citations/19720024394
[research_grafton_chambers_1974]: https://ntrs.nasa.gov/citations/19740018330
[research_grafton_gilber_1982]: https://doi.org/10.2514/6.1982-1322
[research_grafton_grantham_1965]: https://ntrs.nasa.gov/citations/19650009675
[research_graham_1951]: https://ntrs.nasa.gov/citations/19930086854
[research_graham_1973]: https://ntrs.nasa.gov/citations/19730024241
[research_graham_1973_2]: https://ntrs.nasa.gov/citations/19730024193
[research_graham_jones_1972]: https://ntrs.nasa.gov/citations/19730024194
[research_grant_abdulrahim_2006]: https://doi.org/10.2514/6.2006-6505
[research_grant_abdulrahim_2010]: https://doi.org/10.1260/1756-8293.2.2.91
[research_grant_chakravarthy_2009]: https://doi.org/10.2514/6.2009-5848
[research_grant_lind_2007]: https://doi.org/10.2514/6.2007-6487
[research_grant_lind_2010]: https://doi.org/10.2514/6.2010-8203
[research_grant_sorley_2012]: https://doi.org/10.1002/9781119964032.ch7
[research_grantham_scher_1960]: https://ntrs.nasa.gov/citations/19630002682
[research_grantz_1985]: https://doi.org/10.2514/6.1985-5005
[research_grauer_hubbard_2012]: https://doi.org/10.1002/9781119964032.ch6
[research_graves_1975]: https://ntrs.nasa.gov/citations/19760009934
[research_grayjr_1964]: https://doi.org/10.2514/6.1964-192
[research_greatwood_waldock_2017]: https://doi.org/10.1016/j.ast.2017.09.034
[research_green_1987]: https://doi.org/10.2514/3.45525
[research_green_lee_1990]: https://ntrs.nasa.gov/citations/19900010771
[research_green_ott_2003]: https://doi.org/10.2514/6.2003-925
[research_green_ott_2005]: https://doi.org/10.2514/1.2895
[research_greenblatt_washburn_2007]: https://doi.org/10.2514/6.2007-4275
[research_greenman_cheung_1996]: https://doi.org/10.2514/6.1996-2486
[research_greff_1990]: https://doi.org/10.1017/s0001924000023186
[research_gregory_1985]: https://ntrs.nasa.gov/citations/19850053998
[research_gresham_simmons_2024]: https://doi.org/10.2514/1.c036835
[research_griffin]: https://doi.org/10.33915/etd.1826
[research_griffin_eastep_1981]: https://doi.org/10.2514/6.1981-637
[research_griffin_eastep_1982]: https://doi.org/10.2514/3.61570
[research_griffin_haerter_1983]: https://doi.org/10.21236/ada133188
[research_grigorie_botez_2009]: https://doi.org/10.2514/6.2009-5893
[research_grigorie_botez_2011]: https://doi.org/10.2514/6.2011-2133
[research_grigorie_botez_2012]: https://doi.org/10.1017/s0001924000006977
[research_grigorie_botez_2014]: https://doi.org/10.2514/6.2014-2187
[research_grigorie_botez_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00012-5
[research_grigorie_botez_2023]: https://doi.org/10.3390/act12090350
[research_grigorie_popov_2011]: https://doi.org/10.2514/6.2011-6460
[research_grigorie_popov_2011_b]: https://doi.org/10.1177/0954410011408226
[research_grigorie_popov_2012]: https://doi.org/10.2514/6.2012-4639
[research_grismer_nelson_1994]: https://doi.org/10.2514/6.1994-1855
[research_grogorie_popov_2013]: https://doi.org/10.2514/6.2013-4918
[research_grose_1979]: https://ntrs.nasa.gov/citations/19790009678
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_grosser_1982]: https://doi.org/10.2514/6.1982-642
[research_grossman_gurdal_1986]: https://doi.org/10.2514/6.1986-2623
[research_grovesraines_watkins_2026]: https://doi.org/10.1098/rsif.2025.0930
[research_grow_landrum_1967]: https://ntrs.nasa.gov/citations/19670009634
[research_gu_healy_2022]: https://doi.org/10.2514/6.2022-0723
[research_gu_healy_2024]: https://doi.org/10.2514/6.2024-0618
[research_gu_hong_2020]: https://doi.org/10.1088/1742-6596/1600/1/012013
[research_gu_shou_2025]: https://doi.org/10.1051/jnwpu/20254350936
[research_guan_zhuang_2026]: https://doi.org/10.1007/978-981-95-7641-8_45
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_gudmundsson_2014]: https://doi.org/10.1016/b978-0-12-397308-5.00009-x
[research_gudmundsson_2014_b]: https://doi.org/10.1016/b978-0-12-397308-5.00015-5
[research_gudmundsson_2022]: https://doi.org/10.1016/b978-0-12-818465-3.00009-4
[research_gudmundsson_2022_b]: https://doi.org/10.1016/b978-0-12-818465-3.00016-1
[research_guerreiro_hubbard_2006]: https://ntrs.nasa.gov/citations/20060009038
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_guiler_huebsch_2005]: https://doi.org/10.2514/6.2005-4981
[research_guiler_huebsch_2005_b]: https://doi.org/10.4271/2005-01-3391
[research_gul_datta_2021]: https://doi.org/10.4050/f-0077-2021-16762
[research_guler_nikbay_2026]: https://doi.org/10.2139/ssrn.6073386
[research_gunasekaran_mukherjee_2016]: https://doi.org/10.2514/6.2016-1779
[research_gunduz_2025]: https://doi.org/10.32920/29042732.v1
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012019
[research_guo_bai_2017]: https://doi.org/10.1360/n092016-00362
[research_guo_hou_2016]: https://doi.org/10.1109/robio.2016.7866653
[research_guo_hou_2017]: https://doi.org/10.1109/access.2017.2743059
[research_guo_hou_2017_b]: https://doi.org/10.1109/ccdc.2017.7978397
[research_guo_kloker_2026]: https://doi.org/10.1017/jfm.2026.11937
[research_guo_unsteady_2020]: https://doi.org/10.1142/s0217979220400731
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_guo_wang_2025]: https://doi.org/10.1016/j.ast.2025.109966
[research_gupta_1990]: https://doi.org/10.2514/6.1990-3041
[research_gupta_2012]: https://doi.org/10.2514/6.2012-2603
[research_gupta_kim_2025]: https://doi.org/10.1109/iros60139.2025.11247572
[research_gupta_kumar_2023]: https://doi.org/10.20944/preprints202309.1914.v1
[research_gurdal_2002]: https://doi.org/10.21236/ada402571
[research_gurdal_haftka_1999]: https://doi.org/10.21236/ada387245
[research_gurdamar_cete_2006]: https://doi.org/10.2514/6.2006-3170
[research_gurley_1962]: https://ntrs.nasa.gov/citations/19660025705
[research_guruswamy_2010]: https://doi.org/10.2514/1.45744
[research_guruswamy_goorjian_1985]: https://doi.org/10.2514/6.1985-690
[research_guruswamy_goorjian_1986]: https://ntrs.nasa.gov/citations/19860060148
[research_guruswamy_yang_1984]: https://ntrs.nasa.gov/citations/19840048898
[research_gwin_1974]: https://ntrs.nasa.gov/citations/19740045423
[research_gwin_1976]: https://doi.org/10.2514/3.58668
[research_haas_chopra_1987]: https://doi.org/10.2514/6.1987-920
[research_haas_hader_2021]: https://doi.org/10.2514/6.2021-2848
[research_haas_hader_2022]: https://doi.org/10.2514/6.2022-1074
[research_haftka_1977]: https://doi.org/10.2514/3.7400
[research_hahn_drikakis_2008]: https://doi.org/10.2514/6.2008-669
[research_hahn_drikakis_2009]: https://doi.org/10.2514/1.37806
[research_haider_ajaj_2023]: https://doi.org/10.3390/aerospace10010057
[research_haider_mansor_2022]: https://doi.org/10.1007/978-981-19-3923-5_2
[research_haider_mansor_2023]: https://doi.org/10.1108/aeat-03-2022-0092
[research_haines_1957]: https://doi.org/10.1017/s0368393100128986
[research_hale_1976]: https://ntrs.nasa.gov/citations/19770003437
[research_hall_1971]: https://doi.org/10.2514/3.59106
[research_hall_mohseni_2005]: https://doi.org/10.2514/6.2005-7171
[research_hall_weingarten_1974]: https://doi.org/10.2514/3.60377
[research_hall_woodson_2003]: https://doi.org/10.2514/6.2003-589
[research_hallion_1984]: https://ntrs.nasa.gov/citations/19850009625
[research_hallissy_ayers_1977]: https://ntrs.nasa.gov/citations/19770026171
[research_hallissy_harris_1974]: https://ntrs.nasa.gov/citations/19830002846
[research_hallissy_phillips_1989]: https://ntrs.nasa.gov/citations/19890017439
[research_ham_1981]: https://doi.org/10.2514/6.1981-409
[research_hamer_1961]: https://ntrs.nasa.gov/citations/20040027944
[research_hammer_garmann_2021]: https://doi.org/10.2514/6.2021-2948
[research_hammer_garmann_2023]: https://doi.org/10.2514/1.j063039
[research_hammer_garmann_2023_b]: https://doi.org/10.2514/6.2023-1979
[research_hammond_1961]: https://ntrs.nasa.gov/citations/19650014317
[research_hammond_1963]: https://ntrs.nasa.gov/citations/19640000708
[research_hammond_1965]: https://ntrs.nasa.gov/citations/19660025706
[research_hammond_1970]: https://ntrs.nasa.gov/citations/19710001566
[research_han_2016]: https://doi.org/10.20910/jase.2016.10.3.39
[research_han_2016_b]: https://doi.org/10.20910/jase.2016.10.4.11
[research_han_hong_2015]: https://doi.org/10.2514/6.2015-1133
[research_han_hu_2014]: https://doi.org/10.2514/6.2014-3130
[research_han_lee_2007]: https://doi.org/10.2514/1.26267
[research_hancock_1960]: https://doi.org/10.2514/8.8377
[research_hancock_1971]: https://doi.org/10.2514/3.59157
[research_hancock_1972]: https://doi.org/10.1017/s0001924000044055
[research_haney_johnson_1980]: https://doi.org/10.2514/3.57925
[research_haney_waggoner_1978]: https://doi.org/10.2514/3.58414
[research_hang_liu_2026]: https://doi.org/10.3390/aerospace13040305
[research_hanin_barsonynagy_1983]: https://doi.org/10.2514/3.8147
[research_hansen_2011]: https://doi.org/10.2514/6.2011-260
[research_hanson_1973]: https://ntrs.nasa.gov/citations/19730008178
[research_hargraves_1961]: https://doi.org/10.21236/ad0268350
[research_harms_kaufmann_2020]: https://doi.org/10.1109/icuas48674.2020.9214033
[research_harperjr_cooper_1984]: https://doi.org/10.2514/6.1984-2442
[research_harris_gautrey_2000]: https://doi.org/10.1017/s0001924000028098
[research_harrison_darragh_2016]: https://doi.org/10.2514/6.2016-4179
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_1968]: https://doi.org/10.2514/6.1968-817
[research_hartshorn_2011]: https://doi.org/10.2514/6.2011-3352
[research_harvey_1967]: https://doi.org/10.4271/670881
[research_harvey_2023]: https://doi.org/10.2514/6.2023-0827
[research_harvey_baliga_2019]: https://doi.org/10.1098/rsif.2018.0641
[research_harvey_gull_2021]: https://doi.org/10.1098/rsif.2021.0132
[research_harvey_harris_1990]: https://doi.org/10.1007/978-3-662-02643-4_24
[research_harvey_inman_2022]: https://doi.org/10.1073/pnas.2204847119
[research_hattasanjaya_2024]: https://doi.org/10.31274/cc-20240624-484
[research_hauptman_1987]: https://doi.org/10.2514/3.9776
[research_havenar_ilie_2025]: https://doi.org/10.2514/6.2025-3508
[research_hawley_1999]: https://ntrs.nasa.gov/citations/20080004521
[research_hayes_1959]: https://ntrs.nasa.gov/citations/19630010604
[research_hayes_1971]: https://ntrs.nasa.gov/citations/19710010651
[research_haynes_reed_1996]: https://doi.org/10.2514/6.1996-182
[research_haynes_reed_1997]: https://doi.org/10.4271/971479
[research_haynes_reed_2000]: https://doi.org/10.1017/s0022112099007260
[research_hayostek_amitay_2018]: https://doi.org/10.2514/6.2018-3729
[research_he_guo_2012]: https://doi.org/10.3901/cjme.2012.02.248
[research_he_guo_2021]: https://doi.org/10.1016/j.ast.2021.106689
[research_he_li_2017]: https://doi.org/10.14736/kyb-2016-6-0967
[research_he_yin_2015]: https://doi.org/10.1177/0954410015591835
[research_he_zhang_2015]: https://doi.org/10.1109/cyber.2015.7288192
[research_heath_1959]: https://ntrs.nasa.gov/citations/19980228240
[research_hebbar_leedy_1992]: https://doi.org/10.2514/3.46290
[research_heeb_woods_2024]: https://doi.org/10.1115/ssdm2024-121418
[research_helm_fehrs_2021]: https://doi.org/10.2514/6.2021-2503
[research_henderson_1960]: https://ntrs.nasa.gov/citations/19980228156
[research_henderson_1964]: https://ntrs.nasa.gov/citations/19670022816
[research_henderson_1965]: https://ntrs.nasa.gov/citations/19650024621
[research_henderson_1974]: https://ntrs.nasa.gov/citations/19740024299
[research_henderson_huffman_1975]: https://ntrs.nasa.gov/citations/19760002978
[research_henne_1981]: https://doi.org/10.2514/3.57472
[research_henning_1953]: https://ntrs.nasa.gov/citations/19930089146
[research_henry_molinari_2017]: https://doi.org/10.2514/6.2017-0294
[research_henry_molinari_2019]: https://doi.org/10.2514/1.j057254
[research_henry_pines_2007]: https://doi.org/10.2514/6.2007-1708
[research_herdiana_pinindriya_2024]: https://doi.org/10.4186/ej.2024.28.12.29
[research_heredia_ollero_2010]: https://doi.org/10.3390/s100302188
[research_herencia_weaver_2007]: https://doi.org/10.2514/6.2007-2214
[research_hermanutz_2020]: https://doi.org/10.3390/aerospace7040045
[research_heron_myose_2007]: https://doi.org/10.2514/6.2007-6725
[research_herrmann_1929]: https://ntrs.nasa.gov/citations/19930090821
[research_herrmann_nematnasser_1966]: https://ntrs.nasa.gov/citations/19660053477
[research_herrmann_nematnasser_1967]: https://ntrs.nasa.gov/citations/19670040131
[research_hertz_shirk_1982]: https://ntrs.nasa.gov/citations/19820035536
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hess_1984]: https://doi.org/10.2514/6.1984-236
[research_hess_1987]: https://doi.org/10.2514/6.1987-2537
[research_hess_2012]: https://doi.org/10.2514/1.c031805
[research_hess_hess_1997]: https://doi.org/10.2514/6.1997-454
[research_hess_joyce_2013]: https://doi.org/10.2514/6.2013-4505
[research_hewes_1951]: https://ntrs.nasa.gov/citations/19930082991
[research_hickey_aoyagi_1960]: https://ntrs.nasa.gov/citations/19980227096
[research_hicks_henne_1977]: https://doi.org/10.2514/6.1977-1247
[research_hicks_mendoza_1973]: https://ntrs.nasa.gov/citations/19730013195
[research_hicks_moulton_1988]: https://doi.org/10.2514/6.1988-2144
[research_hieser_kudlacik_1956]: https://ntrs.nasa.gov/citations/20050029376
[research_higgins_shomber_1964]: https://doi.org/10.2514/6.1964-603
[research_higgins_shomber_1965]: https://doi.org/10.2514/3.43684
[research_high_speed_flight_2010]: https://doi.org/10.2514/5.9781600867552.0069.0278
[research_hilger_ritter_2021]: https://doi.org/10.3390/aerospace8100308
[research_hill_1987]: https://doi.org/10.21236/ada186949
[research_hillenherms_schroeder_2001]: https://doi.org/10.2514/6.2001-2468
[research_hiller_2002]: https://doi.org/10.2514/6.2002-3495
[research_hilton_1955]: https://doi.org/10.2514/8.3300
[research_hintz_torno_2014]: https://doi.org/10.1109/icuas.2014.6842290
[research_hirschel_rizzi_2020]: https://doi.org/10.1007/978-3-662-61328-3_8
[research_hirschel_rizzi_2020_b]: https://doi.org/10.1007/978-3-662-61328-3_10
[research_historic_review_2010]: https://doi.org/10.2514/5.9781600867552.0001.0068
[research_hitch_1978]: https://doi.org/10.2514/3.58464
[research_hlckey_1969]: https://doi.org/10.2514/3.44110
[research_hoadley_mcgraw_1995]: https://doi.org/10.2514/3.46680
[research_hoang_bui_2019]: https://doi.org/10.1007/s12206-019-0120-9
[research_hoang_bui_2019_b]: https://doi.org/10.1007/s12206-019-0520-x
[research_hoang_nguyen_2014]: https://doi.org/10.4028/www.scientific.net/amr.1016.377
[research_hoang_rediniotis_1993]: https://doi.org/10.2514/6.1993-185
[research_hodgkinson_lamanna_1977]: https://doi.org/10.2514/6.1977-1122
[research_hodgkinson_potsdam_1990]: https://doi.org/10.2514/6.1990-2825
[research_hodson_hunsaker_2017]: https://doi.org/10.2514/6.2017-4222
[research_hoehler_1949]: https://ntrs.nasa.gov/citations/20050029434
[research_hoerner_1936]: https://doi.org/10.1108/eb030033
[research_hoerner_1952]: https://doi.org/10.21236/ada800374
[research_hoff_gratton_2013]: https://doi.org/10.1017/s0001924000008824
[research_hoh_mitchell_2018]: https://doi.org/10.1201/9781315136820-1
[research_holcomb_1979]: https://doi.org/10.2514/6.1979-1835
[research_holleman_1974]: https://ntrs.nasa.gov/citations/19740010558
[research_holmes_obara_1992]: https://doi.org/10.1007/978-1-4612-2872-1_3
[research_hong_roberts_1995]: https://doi.org/10.2514/6.1995-1842
[research_hooker_2023]: https://doi.org/10.2514/6.2023-0052
[research_hopkins_1951]: https://ntrs.nasa.gov/citations/19930082940
[research_hopkins_1964]: https://doi.org/10.2514/3.2321
[research_hopkins_1975]: https://ntrs.nasa.gov/citations/19750055435
[research_hopkins_1977]: https://doi.org/10.2514/3.58766
[research_hopkins_levin_1974]: https://ntrs.nasa.gov/citations/19740055046
[research_hopkins_levin_1975]: https://doi.org/10.2514/3.59850
[research_hopkins_lovette_1976]: https://ntrs.nasa.gov/citations/19760022153
[research_hopkins_lovette_1976_b]: https://ntrs.nasa.gov/citations/19770009125
[research_hopkins_lovette_1977]: https://ntrs.nasa.gov/citations/19770013088
[research_hopkins_nelson_1976]: https://ntrs.nasa.gov/citations/19760010984
[research_hopkins_yee_1977]: https://ntrs.nasa.gov/citations/19770014154
[research_hopkins_yee_1977_b]: https://ntrs.nasa.gov/citations/19770021142
[research_hord]: https://doi.org/10.18297/etd/634
[research_horstmann_2008]: https://doi.org/10.2514/6.2008-3985
[research_hosangadi_paul_2015]: https://doi.org/10.2514/6.2015-3159
[research_hosder_walters_2008]: https://doi.org/10.2514/6.2008-729
[research_hoshi_kuya_2020]: https://doi.org/10.2514/6.2020-0091
[research_hossain_wang_2020]: https://doi.org/10.13111/2066-8201.2020.12.4.7
[research_hosseini_tempelmann_2013]: https://doi.org/10.1017/jfm.2013.33
[research_hou_2025]: https://doi.org/10.1007/978-981-96-6235-7_5
[research_hou_cao_2024]: https://doi.org/10.23919/ccc63176.2024.10662835
[research_hou_satyanarayana_2000]: https://doi.org/10.2514/6.2000-4824
[research_housner_1974]: https://ntrs.nasa.gov/citations/19740024243
[research_hovelmann_breitsamter_2015]: https://doi.org/10.2514/1.c033014
[research_howe_2000]: https://doi.org/10.1002/9781118903094.ch5
[research_hu]: https://doi.org/10.17760/d20449615
[research_hu_2025]: https://doi.org/10.1016/j.ast.2025.110174
[research_hu_2026]: https://doi.org/10.2514/1.j066216
[research_hu_ge_2023]: https://doi.org/10.1016/j.ast.2022.108083
[research_hu_traisnel_2026]: https://doi.org/10.2139/ssrn.6790318
[research_hu_yang_2016]: https://doi.org/10.1016/j.jsv.2015.11.043
[research_hua_2025]: https://doi.org/10.3390/aerospace12040327
[research_huai_piomelli_1997]: https://doi.org/10.2514/6.1997-750
[research_huang_1990]: https://doi.org/10.2514/6.1990-3371
[research_huang_2003]: https://doi.org/10.2514/6.2003-3944
[research_huang_2026]: https://doi.org/10.2514/1.c038842
[research_huang_fu_2020]: https://doi.org/10.1115/detc2020-22008
[research_huang_fu_2021]: https://doi.org/10.1115/1.0001749v
[research_huang_fu_2021_b]: https://doi.org/10.1016/j.cnsns.2020.105625
[research_huang_guo_2023]: https://doi.org/10.3390/aerospace10090749
[research_huang_lin_2002]: https://doi.org/10.2514/6.2002-2721
[research_huang_liu_2023]: https://doi.org/10.1016/j.ast.2023.108727
[research_huang_qiu_2013]: https://doi.org/10.4028/www.scientific.net/amm.300-301.1136
[research_huang_qiu_2013_b]: https://doi.org/10.1016/j.cja.2013.07.047
[research_huang_wu_2006]: https://doi.org/10.2514/1.21144
[research_huang_wu_2017]: https://doi.org/10.2514/6.2017-0415
[research_huang_yang_2018]: https://doi.org/10.1016/j.cja.2017.12.014
[research_huatian_2018]: https://doi.org/10.1049/cp.2018.0175
[research_hubbard_fontenot_2014]: https://doi.org/10.2514/1.c032339
[research_huebsch_hamburg_2012]: https://doi.org/10.1533/9780857096098.1.37
[research_huehne_mahmood_2013]: https://doi.org/10.2514/6.2013-2798
[research_huffman_1972]: https://ntrs.nasa.gov/citations/19730003273
[research_huffman_jr_1977]: https://ntrs.nasa.gov/citations/19780005067
[research_huffschmid_1950]: https://ntrs.nasa.gov/citations/19990054421
[research_hui_chen_2023]: https://doi.org/10.2514/1.i011183
[research_hui_zhang_2019]: https://doi.org/10.1016/j.ast.2019.105419
[research_hui_zhang_2020]: https://doi.org/10.1063/1.5144432
[research_huijts_voskuijl_2015]: https://doi.org/10.1016/j.ast.2015.07.001
[research_human_powered_aircraft_2014]: https://doi.org/10.1002/9781118534748.ch12
[research_hunsaker_montgomery_2019]: https://doi.org/10.2514/6.2019-2040
[research_hunsaker_moorthamers_2019]: https://doi.org/10.2514/6.2019-2917
[research_hunt_gowadia_1981]: https://doi.org/10.2514/6.1981-1692
[research_hunt_saric_2011]: https://doi.org/10.2514/6.2011-3881
[research_hurst_wickenheiser_2008]: https://doi.org/10.1115/smasis2008-522
[research_hurst_wickenheiser_2009]: https://doi.org/10.2514/6.2009-2130
[research_hussain_bons_2019]: https://doi.org/10.2514/6.2019-3684
[research_hussain_pei_2025]: https://doi.org/10.1063/5.0304691
[research_hutchin_2019]: https://doi.org/10.2514/6.2019-0280
[research_hutchison_huang_1992]: https://doi.org/10.2514/6.1992-4695
[research_hutchison_unger_1992]: https://doi.org/10.2514/6.1992-212
[research_hutchison_unger_1994]: https://doi.org/10.2514/3.46462
[research_hwang_pi_1978]: https://doi.org/10.2514/6.1978-1456
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58518
[research_hwu_tsai_2002]: https://doi.org/10.2514/2.2945
[research_i_1938]: https://ntrs.nasa.gov/citations/19930092624
[research_iannelli_seiler_2019]: https://doi.org/10.2514/1.g004023
[research_iannuzzo_russo_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00020-4
[research_ichikawa_1996]: https://doi.org/10.2514/3.46995
[research_ichikawa_koike_2021]: https://doi.org/10.1007/s00348-021-03198-4
[research_ichikawa_nakagawa_2026]: https://doi.org/10.1007/978-981-96-9829-5_28
[research_igoe_1961]: https://ntrs.nasa.gov/citations/20040006370
[research_ilie_havenar_2022]: https://doi.org/10.2514/6.2022-1315
[research_iliff_1972]: https://ntrs.nasa.gov/citations/19720012009
[research_iliff_1977]: https://doi.org/10.2514/3.58911
[research_iliff_1980]: https://ntrs.nasa.gov/citations/19800061692
[research_imber_rogers_1996]: https://doi.org/10.2514/6.1996-558
[research_imbrie_1981]: https://doi.org/10.2514/3.44723
[research_inayat_amin_2018]: https://doi.org/10.1108/aeat-08-2017-0180
[research_inertia_coupling_2004]: https://doi.org/10.2514/5.9781600862274.0631.0676
[research_inertia_coupling_2015]: https://doi.org/10.2514/5.9781624102745.0681.0730
[research_inger_1994]: https://doi.org/10.2514/6.1994-2072
[research_inger_1995]: https://doi.org/10.2514/3.12735
[research_inman_perry_2024]: https://doi.org/10.1117/12.3010181
[research_inoyama_sanders_2007]: https://doi.org/10.2514/1.25535
[research_inoyama_sanders_2008]: https://doi.org/10.2514/1.29988
[research_international_standard_2010]: https://doi.org/10.1017/cbo9780511844652.021
[research_introduction_to]: https://doi.org/10.1007/978-3-540-46573-7_1
[research_introduction_to_2003]: https://doi.org/10.2514/5.9781600861840.0199.0208
[research_iosilevskii_2025]: https://doi.org/10.1007/978-3-031-73625-4_11
[research_iosilevskii_2025_b]: https://doi.org/10.1007/978-3-031-73625-4_8
[research_iosilevskii_2025_c]: https://doi.org/10.1007/978-3-031-73625-4_9
[research_iqbal_alfaruk_2025]: https://doi.org/10.2139/ssrn.5206425
[research_irani_amoozgar_2016]: https://doi.org/10.12989/aas.2016.3.4.447
[research_irving_1933]: https://doi.org/10.1108/eb029754
[research_irving_1966]: https://doi.org/10.1016/b978-1-4832-0019-4.50011-9
[research_irving_1966_b]: https://doi.org/10.1016/b978-1-4832-0019-4.50014-4
[research_isah_lawal_2022]: https://doi.org/10.21203/rs.3.rs-1194453/v1
[research_ishida_ueshima_2026]: https://doi.org/10.2514/1.c038925
[research_ishmael_wierzbanowski_1985]: https://ntrs.nasa.gov/citations/19860060204
[research_ishtiaq_israr_2013]: https://doi.org/10.1109/icase.2013.6785549
[research_islam_rahman_2025]: https://doi.org/10.31224/4605
[research_isogai_2013]: https://doi.org/10.2322/tjsass.56.303
[research_ito_takanashi_1991]: https://doi.org/10.2514/6.1991-3202
[research_itoh_kobayashi_1999]: https://doi.org/10.1016/b978-008043328-8/50067-9
[research_itoh_kobayashi_2000]: https://doi.org/10.1016/s0142-727x(00)00009-6
[research_ivanco_scott_2007]: https://ntrs.nasa.gov/citations/20070018202
[research_ivanov_mischenko_2018]: https://doi.org/10.1063/1.5065246
[research_ivanov_mischenko_2020]: https://doi.org/10.1134/s0021894420020108
[research_iyer_spall_1992]: https://doi.org/10.2514/6.1992-2630
[research_iyer_takahashi_2025]: https://doi.org/10.2514/6.2025-2622
[research_jackuliak_bugaj_2022]: https://doi.org/10.26552/pas.z.2022.1.08
[research_jackuliak_bugaj_2026]: https://doi.org/10.23919/ntca68808.2026.11524172
[research_jacobs_1983]: https://doi.org/10.2514/6.1983-94
[research_jacobsen_1953]: https://ntrs.nasa.gov/citations/20050028475
[research_jacobson_joshi_1977]: https://doi.org/10.2514/3.44591
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jahnke_culick_1990]: https://ntrs.nasa.gov/citations/19900035129
[research_jalil_hashim_2024]: https://doi.org/10.1063/5.0191632
[research_james_1957]: https://ntrs.nasa.gov/citations/19930089713
[research_jameson]: https://doi.org/10.1007/3-540-09119-x_97
[research_jameson_1977]: https://doi.org/10.2172/7093932
[research_jameson_caughey_1977]: https://doi.org/10.2172/7308750
[research_jamwal_hosangadi_2018]: https://doi.org/10.2514/6.2018-3956
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_janke_bertolotti_2001]: https://doi.org/10.1007/978-3-540-45359-8_19
[research_jansen_1980]: https://doi.org/10.2514/6.1980-1568
[research_jaquet_1952]: https://ntrs.nasa.gov/citations/19930087196
[research_jaramillo_cho_1995]: https://doi.org/10.2514/3.46896
[research_jasa_hwang_2018]: https://doi.org/10.2514/6.2018-1382
[research_jeger_wuest_2024]: https://doi.org/10.1038/s44182-024-00015-y
[research_jenkins_1977]: https://ntrs.nasa.gov/citations/19780032273
[research_jenkins_1977_2]: https://ntrs.nasa.gov/citations/20020086520
[research_jenkins_1986]: https://doi.org/10.4271/861767
[research_jenks_henry_1977]: https://ntrs.nasa.gov/citations/19770014139
[research_jentys_breitsamter_2023]: https://doi.org/10.1016/j.ast.2023.108652
[research_jeong_bae_2022]: https://doi.org/10.1109/icuas54217.2022.9836192
[research_jernell_mckinney_1965]: https://ntrs.nasa.gov/citations/19660017752
[research_ji_huang_2024]: https://doi.org/10.3390/aerospace11010080
[research_jian_keqin_2004]: https://doi.org/10.2514/1.5467
[research_jiang_dong_2015]: https://doi.org/10.1016/j.cja.2015.10.005
[research_jiang_wu_2020]: https://doi.org/10.1016/j.ast.2020.106242
[research_jiang_xu_2014]: https://doi.org/10.1360/132013-324
[research_jiang_yang_2026]: https://doi.org/10.1007/978-981-95-7840-5_15
[research_jianliangwang_weiqiangzhang]: https://doi.org/10.1109/iis.1997.645204
[research_jie_2018]: https://doi.org/10.1109/ccdc.2018.8408044
[research_jim_planform_2021]: https://doi.org/10.2514/1.j060225
[research_jin_2024]: https://doi.org/10.54097/xv395z51
[research_jin_song_2011]: https://doi.org/10.2514/1.c031493
[research_jing_huang_2017]: https://doi.org/10.1016/j.cja.2017.03.002
[research_jingeleski_schetz_2013]: https://doi.org/10.2514/6.2013-2403
[research_jinsong_junma_2012]: https://doi.org/10.1109/eeesym.2012.6258637
[research_jisheng_heng_1998]: https://doi.org/10.1007/bf02487744
[research_jo_choi_2016]: https://doi.org/10.2514/6.2016-3416
[research_jo_majid_2023]: https://doi.org/10.3390/biomimetics8010034
[research_johns_1960]: https://doi.org/10.1108/eb033275
[research_johnson_1953]: https://ntrs.nasa.gov/citations/19930087992
[research_johnson_1953_b]: https://doi.org/10.7249/rm1188
[research_johnson_1959]: https://ntrs.nasa.gov/citations/19980228239
[research_johnson_grafton_1980]: https://ntrs.nasa.gov/citations/19800042790
[research_johnson_hageman_1950]: https://ntrs.nasa.gov/citations/19930082781
[research_johnson_hagerman_1951]: https://ntrs.nasa.gov/citations/19930082998
[research_johnson_lind_2009]: https://doi.org/10.2514/6.2009-6151
[research_johnson_lind_2010]: https://doi.org/10.2514/1.45719
[research_johnson_willen_1976]: https://doi.org/10.2514/3.58672
[research_johnston_1998]: https://doi.org/10.2514/6.1998-2736
[research_jones_1947]: https://ntrs.nasa.gov/citations/19930091936
[research_jones_1948]: https://ntrs.nasa.gov/citations/19930091969
[research_jones_1976]: https://ntrs.nasa.gov/citations/19760064883
[research_jones_1976_2]: https://ntrs.nasa.gov/citations/19760012020
[research_jones_1976_b]: https://ntrs.nasa.gov/citations/19760011998
[research_jones_1976_c]: https://ntrs.nasa.gov/citations/19760011999
[research_jones_1976_d]: https://ntrs.nasa.gov/citations/19760022129
[research_jones_1976_e]: https://ntrs.nasa.gov/citations/19760064234
[research_jones_1977]: https://ntrs.nasa.gov/citations/19770047158
[research_jones_1980]: https://doi.org/10.2514/6.1980-3040
[research_jones_alksne_1951]: https://ntrs.nasa.gov/citations/19930092097
[research_jones_cohen_2011]: https://doi.org/10.2514/6.2011-1561
[research_jones_klinar_1950]: https://ntrs.nasa.gov/citations/19930082723
[research_jones_nakamura_2007]: https://doi.org/10.2514/6.2007-1284
[research_jones_nisbet_1974]: https://ntrs.nasa.gov/citations/19740034298
[research_jones_unangst_1963]: https://ntrs.nasa.gov/citations/19630002604
[research_joo_sanders_2006]: https://doi.org/10.1117/12.658830
[research_jordan_1971]: https://doi.org/10.2514/6.1971-10
[research_joseph_adamski_2021]: https://doi.org/10.2514/6.2021-0408
[research_joseph_golubev_2020]: https://doi.org/10.2514/6.2020-2766
[research_joshi_2026]: https://doi.org/10.1016/j.ast.2026.112927
[research_joshi_tidwell_2004]: https://doi.org/10.2514/6.2004-1722
[research_joshi_vazquez_2020]: https://doi.org/10.2514/6.2020-0333
[research_joshua_adams_2006]: https://doi.org/10.1115/imece2006-14116
[research_joslin_1995]: https://doi.org/10.2514/3.12551
[research_joslin_streett_1992]: https://doi.org/10.1007/978-1-4612-2956-8_28
[research_jouannet_lundstrom_2009]: https://doi.org/10.2514/6.2009-1619
[research_juillen_arnal_1995]: https://doi.org/10.1007/978-3-642-79765-1_20
[research_jung_kim_2013]: https://doi.org/10.4028/www.scientific.net/amm.284-287.442
[research_jung_kim_2022]: https://doi.org/10.2514/1.g005998
[research_jung_reimerdes_2003]: https://doi.org/10.1007/978-3-540-44866-2_10
[research_kabir_alobaidi_2023]: https://doi.org/10.1088/1742-6596/2523/1/012033
[research_kachanov_1996]: https://doi.org/10.1007/978-94-009-1700-2_12
[research_kachanov_borodulin_2016]: https://doi.org/10.1063/1.4963933
[research_kachanov_tararykin_1990]: https://doi.org/10.1007/978-3-642-84103-3_45
[research_kalaji_2023]: https://doi.org/10.32920/ryerson.14653803
[research_kalemaris_1980]: https://doi.org/10.4271/801176
[research_kamal_aly_2015]: https://doi.org/10.2514/6.2015-1595
[research_kambayashi_2025]: https://doi.org/10.2322/tjsass.68.19
[research_kameda_seki_2008]: https://doi.org/10.2514/6.2008-6418
[research_kamiya_nishi_1978]: https://doi.org/10.2514/6.1978-1221
[research_kammegne_botez_2016]: https://doi.org/10.2316/p.2016.830-031
[research_kammegne_botez_2019]: https://doi.org/10.1017/aer.2019.106
[research_kanamori_imamura_2009]: https://doi.org/10.2322/tstj.7.pe_1
[research_kanazaki_imamura_2008]: https://doi.org/10.2514/6.2008-175
[research_kandil_kalisch_1994]: https://doi.org/10.2514/6.1994-1887
[research_kandil_kandil_1993]: https://doi.org/10.2514/6.1993-3472
[research_kandil_kandil_1993_b]: https://doi.org/10.2514/6.1993-3688
[research_kang_2026]: https://doi.org/10.1109/tmech.2026.3651986
[research_kang_2026_2]: https://doi.org/10.1016/j.fmre.2025.12.025
[research_kang_lu_2026]: https://doi.org/10.1109/tmech.2025.3599439
[research_kannemans_1995]: https://doi.org/10.2514/6.1995-3434
[research_kapania_eldred_1991]: https://doi.org/10.2514/6.1991-1103
[research_kapuscinski_2020]: https://doi.org/10.3390/s20082401
[research_karahan_2026]: https://doi.org/10.70286/eoss-26.01.2026.001.15-23
[research_kargarnovin_sayrarfie_1995]: https://doi.org/10.1007/978-3-642-79654-8_171
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karow_2026]: https://doi.org/10.2514/6.2026-114637
[research_karpel_selitrennik_2008]: https://doi.org/10.2514/6.2008-1898
[research_karpouzian_librescu_1993]: https://doi.org/10.2514/6.1993-1535
[research_karthik_tulapurkara_1999]: https://doi.org/10.2514/2.2529
[research_kass_1970]: https://doi.org/10.2514/6.1970-875
[research_kasuga_yoshida_2017]: https://doi.org/10.2514/6.2017-0039
[research_katz_1989]: https://doi.org/10.2514/3.10231
[research_katz_feistel_1987]: https://doi.org/10.2514/3.45440
[research_kaul_2024]: https://doi.org/10.1016/j.ast.2024.109376
[research_kaul_nguyen_2017]: https://ntrs.nasa.gov/citations/20170011174
[research_kaushik_2018]: https://doi.org/10.1007/978-981-13-1678-4_6
[research_kaushik_2018_b]: https://doi.org/10.1007/978-981-13-1678-4_1
[research_kawazoe_kato_2005]: https://doi.org/10.1299/jsmeicjwsf.2005.583
[research_kaygan_ulusoy_2018]: https://doi.org/10.30518/jav.482507
[research_kayran_2004]: https://doi.org/10.1115/esda2004-58467
[research_kazhan_kazhan_2019]: https://doi.org/10.1615/tsagiscij.2019030597
[research_kearns_1962]: https://doi.org/10.21236/ad0650981
[research_keener_1984]: https://doi.org/10.2514/6.1984-2092
[research_kegelman_roos_1989]: https://doi.org/10.2514/6.1989-86
[research_kehoe_1987]: https://ntrs.nasa.gov/citations/19870018230
[research_keidel_2020]: https://doi.org/10.2514/1.c035606
[research_keidel_fasel_2019]: https://doi.org/10.2514/6.2019-0854
[research_keith_selberg_1984]: https://doi.org/10.2514/3.48244
[research_keller_2019]: https://doi.org/10.1007/s13272-019-00396-z
[research_keller_sandford_1991]: https://ntrs.nasa.gov/citations/19920003836
[research_kelley_shinar_1978]: https://doi.org/10.1016/s1474-6670(17)66061-0
[research_kelley_shinar_1979]: https://doi.org/10.1016/0005-1098(79)90014-1
[research_kemp_1950]: https://ntrs.nasa.gov/citations/19930086268
[research_kemp_1951]: https://ntrs.nasa.gov/citations/19930086901
[research_kempel_mcneill_1988]: https://ntrs.nasa.gov/citations/19880035069
[research_kempel_mcneill_1988_b]: https://ntrs.nasa.gov/citations/19890006559
[research_kempel_pahle_1992]: https://ntrs.nasa.gov/citations/19920000265
[research_kempel_phillips_1989]: https://ntrs.nasa.gov/citations/19910036370
[research_kendall_1984]: https://doi.org/10.2514/6.1984-2164
[research_kendall_1985]: https://doi.org/10.2514/3.45214
[research_kennedy_1951]: https://ntrs.nasa.gov/citations/19930086470
[research_kennelly_1990]: https://ntrs.nasa.gov/citations/19920022969
[research_kennelly_1999]: https://ntrs.nasa.gov/citations/20050243387
[research_kennelly_strong_1992]: https://ntrs.nasa.gov/citations/19920000759
[research_kentfield_2006]: https://doi.org/10.2514/1.16890
[research_kentfield_spragins_2004]: https://doi.org/10.2514/1.558
[research_kerr_1954]: https://doi.org/10.1108/eb032489
[research_khan_2008]: https://doi.org/10.21236/ada486742
[research_khan_deng_2012]: https://doi.org/10.1109/ibcast.2012.6177558
[research_khan_grigorie_2019]: https://doi.org/10.3390/biomimetics4040065
[research_khazaeekuhpar_seyedaghazadeh_2026]: https://doi.org/10.2514/6.2026-2705
[research_khodadoust_bragg_1990]: https://doi.org/10.2514/6.1990-490
[research_kida_1982]: https://doi.org/10.1515/9783112546963-011
[research_kilgore_1971]: https://ntrs.nasa.gov/citations/19710007950
[research_kilgore_1971_b]: https://ntrs.nasa.gov/citations/19710007940
[research_kilgore_adcock_1972]: https://ntrs.nasa.gov/citations/19720014377
[research_kim_kang_2024]: https://doi.org/10.2139/ssrn.4783504
[research_kim_lee_2001]: https://doi.org/10.2514/6.2001-1464
[research_kim_lee_2013]: https://doi.org/10.1109/isr.2013.6695648
[research_kim_lee_2020]: https://doi.org/10.1109/med48518.2020.9183206
[research_kim_marciniak_2002]: https://doi.org/10.2514/2.2936
[research_kim_oh_2017]: https://doi.org/10.2514/1.g001739
[research_kim_sung_1993]: https://doi.org/10.2514/6.1993-3474
[research_kimberlin_2003]: https://doi.org/10.2514/4.861840
[research_kimler_canfield_2006]: https://doi.org/10.2514/6.2006-7134
[research_kirilovskiy_boiko_2019]: https://doi.org/10.1088/1742-6596/1359/1/012070
[research_kirkman_takahashi_2017]: https://doi.org/10.2514/6.2017-0266
[research_kirmse_2016]: https://doi.org/10.1088/0957-0233/27/5/054001
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kishi_kitazaki_2017]: https://doi.org/10.2514/6.2017-4468
[research_kjelgaard_sellersiii_1986]: https://doi.org/10.2514/6.1986-1775
[research_klausmeyer_laflin_2023]: https://doi.org/10.2514/6.2023-4399
[research_klein_batterson_1981]: https://doi.org/10.2514/6.1981-1866
[research_klein_batterson_1983]: https://doi.org/10.2514/6.1983-2066
[research_klein_viswanathan_1973]: https://doi.org/10.1007/bf01590797
[research_klepl_1992]: https://doi.org/10.2514/6.1992-2098
[research_klimczyk_2019]: https://doi.org/10.1108/aeat-12-2017-0289
[research_klinar_1949]: https://ntrs.nasa.gov/citations/20050030060
[research_klinar_1950]: https://ntrs.nasa.gov/citations/20050029448
[research_klinar_healy_1952]: https://ntrs.nasa.gov/citations/20050029457
[research_klinar_jones_1948]: https://ntrs.nasa.gov/citations/20050030058
[research_klinar_lee_1954]: https://ntrs.nasa.gov/citations/20050029445
[research_klinar_lee_1955]: https://ntrs.nasa.gov/citations/20050030045
[research_klinar_snyder_1948]: https://ntrs.nasa.gov/citations/19930082437
[research_kloker_2008]: https://doi.org/10.2514/6.2008-3835
[research_klopfenstein_1965]: https://doi.org/10.2514/6.1965-211
[research_klug_ullah_2023]: https://doi.org/10.1007/s13272-023-00645-2
[research_klyde_harris_2004]: https://doi.org/10.21236/ada426452
[research_knight_1928]: https://ntrs.nasa.gov/citations/19930091341
[research_knight_braun_2011]: https://doi.org/10.2514/6.2011-3963
[research_knight_wenzinger_1930]: https://ntrs.nasa.gov/citations/19930091387
[research_ko_mason_2003]: https://doi.org/10.2514/6.2003-4062
[research_kodigaddi_2026]: https://doi.org/10.21203/rs.3.rs-10227402/v1
[research_kogiso_tsushima_2000]: https://doi.org/10.2514/6.2000-4739
[research_kohama_1987]: https://doi.org/10.1007/bf01184283
[research_kohama_1987_b]: https://doi.org/10.2514/6.1987-1340
[research_kohama_1991]: https://ntrs.nasa.gov/citations/19930033256
[research_kohama_kodashima_1995]: https://doi.org/10.1007/978-3-642-79765-1_54
[research_kohama_suda_1993]: https://doi.org/10.2514/3.11344
[research_kolar_lile_1971]: https://doi.org/10.21236/ada377254
[research_kolbakir_2016]: https://doi.org/10.20535/0203-377131201671109
[research_kolesar_1971]: https://doi.org/10.21236/ad0734236
[research_kolnick_kennedy_1952]: https://ntrs.nasa.gov/citations/19930087297
[research_kolonay_eastep_2004]: https://doi.org/10.2514/6.2004-4362
[research_kolosov_kosinov_2016]: https://doi.org/10.1088/1742-6596/754/2/022005
[research_kolosov_kosinov_2017]: https://doi.org/10.1063/1.5007527
[research_koltko_katz_1975]: https://ntrs.nasa.gov/citations/19770023163
[research_komp_hajek_2024]: https://doi.org/10.2514/1.c037505
[research_kong_1994]: https://ntrs.nasa.gov/citations/19950012715
[research_konrath_schroder_2006]: https://doi.org/10.2514/6.2006-3003
[research_koo_2001]: https://doi.org/10.2514/2.2767
[research_koohi_shahverdi_2014]: https://doi.org/10.1016/j.compstruct.2014.03.012
[research_kornev_ambrozhevich_2021]: https://doi.org/10.3103/s1068799821010049
[research_kornev_pimenov_2022]: https://doi.org/10.34759/trd-2022-123-07
[research_korpe_kanat_2019]: https://doi.org/10.1155/2019/3050824
[research_kosarev_seror_2016]: https://doi.org/10.2514/1.c033509
[research_kosinov_kolosov_2016]: https://doi.org/10.1063/1.4952999
[research_kosmatka_panza_2003]: https://doi.org/10.2514/6.2003-6501
[research_kotsabasis_1981]: https://ntrs.nasa.gov/citations/19810008519
[research_kozlov_chernoray_2006]: https://doi.org/10.1007/1-4020-4159-4_59
[research_kozlov_grek_2014]: https://doi.org/10.54362/1818-7919-2014-9-4-39-64
[research_kozlov_zverkov_2009]: https://doi.org/10.1007/978-90-481-3723-7_89
[research_krener_2001]: https://doi.org/10.21236/ada430327
[research_krengel_2024]: https://doi.org/10.23967/eccomas.2024.094
[research_krenz_1979]: https://doi.org/10.2514/6.1979-692
[research_kress_1983]: https://doi.org/10.2514/6.1983-1051
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_krienes_1941]: https://ntrs.nasa.gov/citations/19930094445
[research_krishna_2021]: https://doi.org/10.47893/gret.2021.1130
[research_krishnamurthi_gandhi_2016]: https://doi.org/10.4050/f-0072-2016-11499
[research_krishnan_mukund]: https://doi.org/10.1007/1-4020-4159-4_54
[research_krispin_portnoy_1988]: https://doi.org/10.2514/3.45537
[research_kroeger_feistel_1976]: https://ntrs.nasa.gov/citations/19990114322
[research_kronejr_1980]: https://doi.org/10.2514/6.1980-3047
[research_kronejr_1980_b]: https://doi.org/10.2514/6.1980-1882
[research_kroo_1982]: https://doi.org/10.2514/3.61557
[research_kroo_1986]: https://doi.org/10.2514/6.1986-2624
[research_kroo_1994]: https://ntrs.nasa.gov/citations/19960049782
[research_kroo_vandervelden_1990]: https://ntrs.nasa.gov/citations/19910027892
[research_kruger_klimmek_2014]: https://doi.org/10.1007/s13272-014-0117-0
[research_kruse_wunderlich_2012]: https://doi.org/10.2514/6.2012-3208
[research_kryvokhatko_2023]: https://doi.org/10.1007/978-3-031-23777-5_2
[research_kryvokhatko_2023_b]: https://doi.org/10.1007/978-3-031-23777-5_4
[research_kryvokhatko_2023_c]: https://doi.org/10.1007/978-3-031-23777-5_3
[research_kryvokhatko_2024]: https://doi.org/10.1007/978-3-031-74809-7_2
[research_kryvokhatko_2024_b]: https://doi.org/10.1007/978-3-031-74809-7_4
[research_kube_2026]: https://doi.org/10.21741/9781644904251-227
[research_kuhlman_brown_1989]: https://doi.org/10.2514/6.1989-644
[research_kuhlman_cerney_1988]: https://doi.org/10.2514/6.1988-7
[research_kulfan_1974]: https://ntrs.nasa.gov/citations/19740023392
[research_kulfan_1979]: https://doi.org/10.2514/6.1979-1872
[research_kulfan_neumann_1973]: https://ntrs.nasa.gov/citations/19740009637
[research_kulfan_vachal_1978]: https://doi.org/10.21236/ada056124
[research_kumar_aravindan_2014]: https://doi.org/10.3850/978-981-09-1139-3_452
[research_kumar_ghosh_2026]: https://doi.org/10.2514/6.2026-4276
[research_kumar_khalid_2014]: https://doi.org/10.2514/6.2014-3002
[research_kumar_mandal_2020]: https://doi.org/10.2514/6.2020-3064
[research_kumar_mathi_2026]: https://doi.org/10.2139/ssrn.6300265
[research_kumar_palanivel_2025]: https://doi.org/10.2514/6.2025-1076
[research_kumar_raghavendra_2004]: https://doi.org/10.2514/6.2004-378
[research_kumar_topology_2021]: https://doi.org/10.1016/j.mechmachtheory.2020.104135
[research_kumkam_suratemeekul_2025]: https://doi.org/10.3390/biomimetics10020110
[research_kunwar_mccormick_2025]: https://doi.org/10.2514/6.2025-3698
[research_kuo_hsu_1997]: https://doi.org/10.2514/2.2222
[research_kurita_koike_2013]: https://doi.org/10.2514/6.2013-967
[research_kurus_takahashi_2021]: https://doi.org/10.2514/6.2021-2432
[research_kuryachii_manuilovich_2014]: https://doi.org/10.1615/tsagiscij.2014012527
[research_kurz_kloker_2014]: https://doi.org/10.1017/jfm.2014.425
[research_kurz_kloker_2015]: https://doi.org/10.2514/6.2015-3079
[research_kurz_kloker_2016]: https://doi.org/10.1017/jfm.2016.240
[research_kurzke_halliwell_2018]: https://doi.org/10.1007/978-3-319-75979-1_14
[research_kurzke_halliwell_2025]: https://doi.org/10.1007/978-3-031-65026-0_20
[research_kusunose_2004]: https://doi.org/10.2514/1.6092
[research_kutzbach_lutz_2004]: https://doi.org/10.2514/6.2004-2702
[research_kwong_2021]: https://doi.org/10.32920/ryerson.14655543.v1
[research_kyser_willis_1973]: https://doi.org/10.2514/6.1973-394
[research_la_joe_2018]: https://doi.org/10.2514/6.2018-0315
[research_lacey_1979]: https://doi.org/10.21236/ada063819
[research_laitone_1978]: https://doi.org/10.2514/3.58339
[research_laitone_1978_b]: https://doi.org/10.2514/3.58457
[research_laitone_1989]: https://doi.org/10.2514/3.45841
[research_laitone_1994]: https://doi.org/10.2514/3.46516
[research_lam_maull_1993]: https://doi.org/10.2514/3.46387
[research_lamar_1968]: https://ntrs.nasa.gov/citations/19680019345
[research_lamar_1971]: https://ntrs.nasa.gov/citations/19710024300
[research_lamar_1980]: https://doi.org/10.2514/3.57870
[research_lamar_margason_1967]: https://ntrs.nasa.gov/citations/19670000665
[research_laminar_flow_1999]: https://doi.org/10.1108/aeat.1999.12771cab.004
[research_lampert_1951]: https://ntrs.nasa.gov/citations/19930082927
[research_lampropoulos_sarris_2025]: https://doi.org/10.3390/aerospace12100934
[research_lampropoulos_vouros_2025]: https://doi.org/10.3390/fluids10030054
[research_lan_1976]: https://ntrs.nasa.gov/citations/19760014067
[research_lan_1977]: https://ntrs.nasa.gov/citations/19770023140
[research_landfield_rajkovic_1984]: https://doi.org/10.2514/6.1984-2401
[research_landfield_rajkovic_1986]: https://doi.org/10.2514/3.45328
[research_landgraf_herring_1967]: https://doi.org/10.4271/670880
[research_landman_simpson_2005]: https://doi.org/10.2514/6.2005-7602
[research_lange_cahill_1974]: https://ntrs.nasa.gov/citations/19740026364
[research_lapin_crookshanks_1952]: https://doi.org/10.2514/8.2336
[research_larco_constatin_2018]: https://doi.org/10.19062/2247-3173.2018.20.24
[research_large_1981]: https://doi.org/10.1017/s0001924000029481
[research_larson_1986]: https://ntrs.nasa.gov/citations/19860020341
[research_larson_1987]: https://ntrs.nasa.gov/citations/19870007386
[research_larson_schweikhard_1971]: https://ntrs.nasa.gov/citations/19710009034
[research_lasauskas_2016]: https://doi.org/10.1017/aer.2016.99
[research_lateral_control_2003]: https://doi.org/10.2514/5.9781600861840.0323.0340
[research_lateral_directional_stability_2003]: https://doi.org/10.2514/5.9781600861840.0297.0310
[research_lauten_lundstrom_1954]: https://ntrs.nasa.gov/citations/19630003991
[research_lavoie_bourgaultcote_2018]: https://doi.org/10.1016/j.compfluid.2017.11.015
[research_lawrence_padfield_2005]: https://doi.org/10.2514/1.6091
[research_lawrence_padfield_2006]: https://doi.org/10.2514/1.19607
[research_laxmanhattalli_srivatsa_2018]: https://doi.org/10.1016/j.matpr.2018.06.553
[research_lebofsky_ting_2014]: https://doi.org/10.2514/6.2014-2443
[research_lebofsky_ting_2015]: https://doi.org/10.2514/6.2015-2723
[research_lee]: https://doi.org/10.32657/10356/75847
[research_lee_1952]: https://ntrs.nasa.gov/citations/20050029463
[research_lee_1963]: https://ntrs.nasa.gov/citations/19630002367
[research_lee_1964]: https://ntrs.nasa.gov/citations/19980236423
[research_lee_1964_2]: https://ntrs.nasa.gov/citations/19940040848
[research_lee_1964_b]: https://ntrs.nasa.gov/citations/20160000758
[research_lee_1969]: https://ntrs.nasa.gov/citations/19690025610
[research_lee_1969_b]: https://ntrs.nasa.gov/citations/19690028594
[research_lee_1970]: https://ntrs.nasa.gov/citations/19700031341
[research_lee_1975]: https://doi.org/10.2514/6.1975-1027
[research_lee_1994]: https://ntrs.nasa.gov/citations/19950006372
[research_lee_1994_b]: https://doi.org/10.2514/6.1994-1695
[research_lee_1995]: https://ntrs.nasa.gov/citations/19950020231
[research_lee_2004]: https://doi.org/10.2514/6.2004-4733
[research_lee_2006]: https://doi.org/10.2514/6.2006-3465
[research_lee_2013]: https://doi.org/10.2514/6.2013-250
[research_lee_batina_1991]: https://doi.org/10.2514/3.45996
[research_lee_broeren_2018]: https://doi.org/10.2514/6.2018-3493
[research_lee_broeren_2019]: https://doi.org/10.4271/2019-01-1986
[research_lee_broeren_2020]: https://doi.org/10.2514/6.2020-2847
[research_lee_chen_2004]: https://doi.org/10.2514/6.2004-1944
[research_lee_kim_2019]: https://doi.org/10.2514/6.2019-0106
[research_lee_kim_2020]: https://doi.org/10.1109/med48518.2020.9183024
[research_lee_kim_2020_b]: https://doi.org/10.1016/j.ifacol.2020.12.1943
[research_lee_ko_2009]: https://doi.org/10.2514/1.39352
[research_lee_lee_2023]: https://doi.org/10.1038/s41598-023-44936-4
[research_lee_libbey_1961]: https://ntrs.nasa.gov/citations/19980227452
[research_lee_marnineaumes_1996]: https://doi.org/10.2514/6.1996-2510
[research_lee_miura_1990]: https://ntrs.nasa.gov/citations/19910058088
[research_lee_nagati_2004]: https://doi.org/10.2514/1.4334
[research_lee_rodchenko_2003]: https://doi.org/10.2514/6.2003-5310
[research_lee_tavella_1986]: https://doi.org/10.2514/6.1986-1810
[research_lee_vankampen_2021]: https://doi.org/10.2514/6.2021-0392
[research_leerausch_batina_1993]: https://ntrs.nasa.gov/citations/19930013268
[research_leerausch_batina_1993_b]: https://ntrs.nasa.gov/citations/19930049978
[research_leerausch_batina_1993_c]: https://ntrs.nasa.gov/citations/20040129686
[research_lego_altman_2013]: https://doi.org/10.2514/6.2013-3053
[research_lehman_stearman_1977]: https://doi.org/10.21236/ada039245
[research_lei_an_2024]: https://doi.org/10.1016/j.ast.2024.109706
[research_lei_zha_2021]: https://doi.org/10.2514/6.2021-2559
[research_lei_zhang_2020]: https://doi.org/10.1088/1757-899x/751/1/012001
[research_leishman_2026]: https://doi.org/10.2514/1.c039163
[research_leitch_2025]: https://doi.org/10.1016/j.compstruct.2025.119706
[research_lekoudis_1980]: https://doi.org/10.1115/1.3240734
[research_lekoudis_1980_b]: https://doi.org/10.2514/3.50852
[research_lekoudis_1981]: https://doi.org/10.1115/1.3240770
[research_lemley_1968]: https://doi.org/10.21236/ad0840550
[research_lemley_mullans_1973]: https://doi.org/10.2514/6.1973-311
[research_lemley_mullans_1974]: https://doi.org/10.2514/3.60344
[research_lendraitis_2025]: https://doi.org/10.3390/act14100498
[research_leonard_prasetiyo_2023]: https://doi.org/10.11591/ijpeds.v14.i2.pp781-788
[research_leoviriyakit_jameson_2004]: https://doi.org/10.2514/6.2004-29
[research_leoviriyakit_jameson_2004_b]: https://doi.org/10.2514/6.2004-5372
[research_leoviriyakit_jameson_2005]: https://doi.org/10.2514/6.2005-450
[research_leoviriyakit_kim_2004]: https://doi.org/10.2514/6.2004-4479
[research_lesalli_cahyono_2020]: https://doi.org/10.28989/senatik.v6i0.402
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_letko_1956]: https://ntrs.nasa.gov/citations/19930084643
[research_letko_brewer_1949]: https://ntrs.nasa.gov/citations/19930085559
[research_letko_cowan_1948]: https://ntrs.nasa.gov/citations/19930082298
[research_letko_jaquet_1948]: https://ntrs.nasa.gov/citations/19930085555
[research_leung_zingg_2011]: https://doi.org/10.2514/6.2011-3178
[research_levchenko_scherbakov_1997]: https://doi.org/10.1007/bf02467835
[research_levesque_pigeon_2015]: https://doi.org/10.2514/6.2015-0912
[research_levinsky_palko_1982]: https://doi.org/10.2514/6.1982-599
[research_levison_1982]: https://doi.org/10.2514/3.57394
[research_leylek_costello_2010]: https://doi.org/10.2514/6.2010-7507
[research_leylek_costello_2013]: https://doi.org/10.2514/6.2013-4982
[research_li_2015]: https://doi.org/10.2514/6.2015-2581
[research_li_2023]: https://doi.org/10.54254/2755-2721/10/20230134
[research_li_2025]: https://doi.org/10.1063/5.0295770
[research_li_2025_2]: https://doi.org/10.1109/taes.2025.3574295
[research_li_2026]: https://doi.org/10.1007/s10409-026-51167-x
[research_li_cao_2025]: https://doi.org/10.1109/eei67650.2025.11334790
[research_li_choudhari_2010]: https://doi.org/10.2514/6.2010-4380
[research_li_choudhari_2011]: https://doi.org/10.2514/1.j050503
[research_li_guo_2012]: https://doi.org/10.1177/0954410012438341
[research_li_guo_2012_b]: https://doi.org/10.1142/s021812741250099x
[research_li_guo_2013]: https://doi.org/10.2514/6.2013-1934
[research_li_guo_2016]: https://doi.org/10.1109/cgncc.2016.7828963
[research_li_guo_2016_b]: https://doi.org/10.1108/aeat-12-2013-0234
[research_li_jin_2018]: https://doi.org/10.1016/j.jsv.2017.10.009
[research_li_leschziner_2007]: https://doi.org/10.2514/6.2007-1118
[research_li_li_2025]: https://doi.org/10.1109/icocta66834.2025.11337686
[research_li_liu_2024]: https://doi.org/10.1109/icocta64736.2024.00037
[research_li_qian_2019]: https://doi.org/10.1007/978-981-13-3305-7_108
[research_li_qiao_2023]: https://doi.org/10.3390/aerospace10070603
[research_li_seebass_1996]: https://doi.org/10.2514/6.1996-2120
[research_li_sobieczky_1999]: https://doi.org/10.2514/2.2547
[research_li_tu_2025]: https://doi.org/10.2139/ssrn.5292691
[research_li_tu_2026]: https://doi.org/10.1007/s42405-026-01140-8
[research_li_varsweep_2020]: https://doi.org/10.1088/1742-6596/1570/1/012073
[research_li_wang_2013]: https://doi.org/10.2514/6.2013-830
[research_li_wang_2025]: https://doi.org/10.23919/ccc64809.2025.11179130
[research_li_wei_2026]: https://doi.org/10.1016/j.measurement.2025.120038
[research_li_yang_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.738
[research_li_yu_2026]: https://doi.org/10.1007/978-981-95-7840-5_4
[research_li_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.608-609.708
[research_li_zhang_2024]: https://doi.org/10.1080/0305215x.2024.2420746
[research_liang_2024]: https://doi.org/10.54097/d1b0pg47
[research_liang_wang_2018]: https://doi.org/10.2991/mecae-18.2018.118
[research_liang_wang_2021]: https://doi.org/10.1007/s12555-020-0764-3
[research_librescu_khdeir_1988]: https://doi.org/10.2514/3.10050
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_thangjitham_1988]: https://doi.org/10.2514/6.1988-2209
[research_librescu_thangjitham_1989]: https://doi.org/10.4271/891056
[research_librescu_thangjitham_1991]: https://doi.org/10.2514/3.46004
[research_lichtenstein_1948]: https://ntrs.nasa.gov/citations/19930085454
[research_lichtenstein_1951]: https://ntrs.nasa.gov/citations/19930083304
[research_lichtenstein_1951_b]: https://ntrs.nasa.gov/citations/19930087864
[research_lichtenstein_1952]: https://ntrs.nasa.gov/citations/19930083215
[research_lichtenstein_1952_b]: https://ntrs.nasa.gov/citations/19930092137
[research_lichtenstein_williams_1958]: https://ntrs.nasa.gov/citations/19930090030
[research_lichtenstein_williams_1961]: https://ntrs.nasa.gov/citations/19980227800
[research_lichter_1974]: https://ntrs.nasa.gov/citations/19990046748
[research_liebrecht_neuwerth_2003]: https://doi.org/10.2514/6.2003-3931
[research_liersch_bishop_2018]: https://doi.org/10.2514/6.2018-2839
[research_lift_and_2017]: https://doi.org/10.1002/9781118534786.ch7
[research_lijewski_1987]: https://doi.org/10.2514/6.1987-2273
[research_lin]: https://doi.org/10.31274/rtd-180813-11950
[research_lin_2025]: https://doi.org/10.5220/0014773000004818
[research_lin_ng_1996]: https://doi.org/10.2514/6.1996-2413
[research_lin_reed_1993]: https://doi.org/10.2514/3.11822
[research_lin_song_2022]: https://doi.org/10.1109/ccdc55256.2022.10034145
[research_lin_yi_2026]: https://doi.org/10.1016/j.cja.2026.104423
[research_lina_moul_1965]: https://doi.org/10.2514/6.1965-781
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_lindner_2006]: https://doi.org/10.21236/ada480198
[research_lindsay_2021]: https://doi.org/10.32920/ryerson.14643990
[research_lindsley_2009]: https://doi.org/10.2514/6.2009-5710
[research_linear_quadratic_2026]: https://doi.org/10.1017/9781009399913.016
[research_liu_2006]: https://doi.org/10.2514/1.13234
[research_liu_2012]: https://doi.org/10.2991/iccasm.2012.352
[research_liu_2022]: https://doi.org/10.1007/978-981-19-4586-1_9
[research_liu_2022_b]: https://doi.org/10.1007/978-981-19-4586-1_11
[research_liu_2022_c]: https://doi.org/10.1007/978-981-19-4586-1_12
[research_liu_2022_d]: https://doi.org/10.1007/978-981-19-4586-1_13
[research_liu_2022_e]: https://doi.org/10.1007/978-981-19-4586-1_10
[research_liu_2024]: https://doi.org/10.1088/1742-6596/2691/1/012030
[research_liu_2026]: https://doi.org/10.3390/aerospace13010091
[research_liu_2026_2]: https://doi.org/10.1016/j.ast.2025.111042
[research_liu_2026_3]: https://doi.org/10.1016/j.ast.2026.111622
[research_liu_bai_2022]: https://doi.org/10.1017/aer.2022.26
[research_liu_fan_2026]: https://doi.org/10.1016/j.isatra.2026.06.042
[research_liu_gao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103098
[research_liu_hou_2016]: https://doi.org/10.1109/robio.2016.7866632
[research_liu_li_2012]: https://doi.org/10.2514/6.2012-4446
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_liang_2023]: https://doi.org/10.1007/s00158-023-03507-x
[research_liu_liou_2009]: https://doi.org/10.21236/ada590187
[research_liu_liu_2023]: https://doi.org/10.3390/aerospace10100903
[research_liu_ouyang_2019]: https://doi.org/10.1007/978-981-13-3305-7_119
[research_liu_qian_2022]: https://doi.org/10.3390/aerospace9120792
[research_liu_qian_2026]: https://doi.org/10.1016/j.ast.2026.112709
[research_liu_shan_2020]: https://doi.org/10.1109/icca51439.2020.9264361
[research_liu_shan_2022]: https://doi.org/10.1016/j.ast.2022.107959
[research_liu_wang_2025]: https://doi.org/10.1108/aeat-07-2024-0197
[research_liu_xu_2012]: https://doi.org/10.4028/www.scientific.net/amm.263-266.1880
[research_liu_xu_2020]: https://doi.org/10.1109/icus50048.2020.9274993
[research_liu_yan_2019]: https://doi.org/10.1109/icivc47709.2019.8980976
[research_liu_yang_2017]: https://doi.org/10.2514/6.2017-4362
[research_liu_zhang_2013]: https://doi.org/10.1109/jsee.2013.00035
[research_livne_li_1994]: https://doi.org/10.1115/imece1994-1443
[research_livne_li_1995]: https://doi.org/10.2514/3.12482
[research_livne_precup_2014]: https://doi.org/10.2514/6.2014-2442
[research_llewellyn_wolhart_1960]: https://ntrs.nasa.gov/citations/20040047052
[research_lock_1964]: https://doi.org/10.1007/978-3-642-88337-8_18
[research_lockhart]: https://doi.org/10.14264/b8e846c
[research_lockwood_1966]: https://ntrs.nasa.gov/citations/19660023730
[research_lockwood_1966_b]: https://ntrs.nasa.gov/citations/19660008600
[research_lockwood_1974]: https://ntrs.nasa.gov/citations/19740012539
[research_lockwood_thompson_1964]: https://ntrs.nasa.gov/citations/19670022811
[research_lockwood_watson_1948]: https://ntrs.nasa.gov/citations/19930082364
[research_loechert_huber_2018]: https://doi.org/10.2514/6.2018-3329
[research_loewy_1969]: https://doi.org/10.2514/6.1969-202
[research_lokos_lizotte_2005]: https://doi.org/10.2514/6.2005-6315
[research_lombardi_morelli_1994]: https://doi.org/10.2514/3.46517
[research_lombardi_morelli_1996]: https://doi.org/10.2514/3.47077
[research_lombardi_salvetti_1997]: https://doi.org/10.2514/6.1997-1838
[research_lombardi_vicini_1994]: https://doi.org/10.1017/s0001924000049733
[research_long_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.722.93
[research_longitudinal_control_2003]: https://doi.org/10.2514/5.9781600861840.0275.0284
[research_longitudinal_maneuvering_2003]: https://doi.org/10.2514/5.9781600861840.0255.0264
[research_lorber_1992_b]: https://doi.org/10.4050/vfs-f48-2033
[research_lorber_carta_1991]: https://ntrs.nasa.gov/citations/19910047382
[research_lorber_covinojr_1991]: https://doi.org/10.2514/6.1991-1795
[research_lorincz_1980]: https://ntrs.nasa.gov/citations/19800024842
[research_losee_willis_1980]: https://doi.org/10.1007/978-1-4684-1033-4_6
[research_lottati_1984]: https://doi.org/10.2514/3.45051
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lottati_1988]: https://doi.org/10.2514/3.45588
[research_louma_1961]: https://ntrs.nasa.gov/citations/19660020177
[research_love_zink_2004]: https://doi.org/10.2514/6.2004-1724
[research_lovell_2001]: https://doi.org/10.1007/978-3-540-45359-8_14
[research_loving_1961]: https://ntrs.nasa.gov/citations/19980227277
[research_loving_1961_b]: https://ntrs.nasa.gov/citations/20040008071
[research_lowe_1988]: https://doi.org/10.2514/3.45606
[research_lowenberg_2010]: https://doi.org/10.1002/9780470686652.eae255
[research_lowry_1957]: https://ntrs.nasa.gov/citations/19930084818
[research_lowry_axelson_1948]: https://ntrs.nasa.gov/citations/19930085373
[research_lowry_schneiter_1947]: https://ntrs.nasa.gov/citations/19930081900
[research_lowson_riley_1995]: https://doi.org/10.2514/3.46798
[research_lu_2025]: https://doi.org/10.2514/1.j064463
[research_lu_lin_2025]: https://doi.org/10.1109/eei67650.2025.11334845
[research_lu_lu_1997]: https://doi.org/10.2514/6.1997-324
[research_lu_luo_2017]: https://doi.org/10.1007/s10483-017-2214-6
[research_lu_wu_2004]: https://doi.org/10.2514/6.2004-4999
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_lucian_mihaela_2012]: https://doi.org/10.5772/48778
[research_lucy_1985]: https://ntrs.nasa.gov/citations/19850000253
[research_luderer_2025]: https://doi.org/10.2514/1.c037946
[research_lundry_1967]: https://doi.org/10.2514/3.43797
[research_lundry_1977]: https://doi.org/10.2514/3.44595
[research_luo_zhou_2000]: https://doi.org/10.1007/978-3-662-03997-7_98
[research_luochuanli_zhenghualiu_2016]: https://doi.org/10.1109/cgncc.2016.7828977
[research_luoma_1961]: https://ntrs.nasa.gov/citations/19660020176
[research_lutze_1977]: https://doi.org/10.2514/3.44610
[research_lutze_lluch_1996]: https://doi.org/10.2514/6.1996-3409
[research_lux_1978]: https://ntrs.nasa.gov/citations/19790011831
[research_lv_zhang_2017]: https://doi.org/10.1088/1742-6596/916/1/012005
[research_lyer_spall_1994]: https://doi.org/10.2514/3.46457
[research_lynch_crowell_2015]: https://doi.org/10.2514/6.2015-1504
[research_lynde_campbell_2017]: https://doi.org/10.2514/6.2017-3058
[research_lynde_campbell_2021]: https://doi.org/10.2514/6.2021-0173
[research_lyu_martins_2014]: https://doi.org/10.2514/6.2014-3275
[research_lyu_martins_2015]: https://doi.org/10.2514/1.c033116
[research_lyubomirov_yartsev_2015]: https://doi.org/10.1109/polyakhov.2015.7106750
[research_ma_1989]: https://doi.org/10.2514/3.45778
[research_ma_2025]: https://doi.org/10.5220/0014450700004861
[research_ma_alwi_2026]: https://doi.org/10.1109/vss69650.2026.11655817
[research_ma_bionic_2021]: https://doi.org/10.3390/app11198859
[research_ma_fan_2022]: https://doi.org/10.1007/s42401-021-00123-9
[research_ma_feng_2018]: https://doi.org/10.21595/jve.2017.18619
[research_ma_hui_2023]: https://doi.org/10.23919/ccc58697.2023.10241099
[research_ma_liu_2004]: https://doi.org/10.2514/1.8707
[research_ma_liu_2023]: https://doi.org/10.1007/978-981-19-6613-2_101
[research_ma_su_2017]: https://doi.org/10.2991/mecae-17.2017.72
[research_ma_zhou_2016]: https://doi.org/10.1115/detc2016-59111
[research_ma_zhou_2024]: https://doi.org/10.21203/rs.3.rs-3982826/v1
[research_macconochie_breiner_1989]: https://ntrs.nasa.gov/citations/19900007465
[research_macconochie_briener_1991]: https://ntrs.nasa.gov/citations/20080004393
[research_macdougall_lichtenstein_1946]: https://ntrs.nasa.gov/citations/20050019257
[research_machireddy_2025]: https://doi.org/10.36227/techrxiv.175695832.26728772/v1
[research_mack_1979]: https://doi.org/10.2514/6.1979-264
[research_mack_schmid_2009]: https://doi.org/10.1615/tsfp6.180
[research_maddalon_collier_1989]: https://ntrs.nasa.gov/citations/19890066459
[research_maddalon_collier_1990]: https://doi.org/10.1007/978-3-642-84103-3_4
[research_maddalon_wagner_1986]: https://ntrs.nasa.gov/citations/19880014364
[research_madhankumargetal_2019]: https://doi.org/10.24247/ijprjun20194
[research_maggin_bennett_1947]: https://ntrs.nasa.gov/citations/19930081902
[research_mahaffey_harding_1970]: https://doi.org/10.2514/6.1970-1511
[research_mahmad_emnasir_2018]: https://doi.org/10.14419/ijet.v7i4.13.21326
[research_mahmood_hashemi_2022]: https://doi.org/10.3390/aerospace9100532
[research_mahns_amitay_2025]: https://doi.org/10.2514/6.2025-1871
[research_mahzan_muhamad_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.3
[research_maikapar_2000]: https://doi.org/10.1023/a:1026611503563
[research_maine_1977]: https://ntrs.nasa.gov/citations/19770060314
[research_maine_1978]: https://ntrs.nasa.gov/citations/19780025111
[research_maines_ghee_2018]: https://doi.org/10.2514/6.2018-0325
[research_maji_pandi_2024]: https://doi.org/10.1063/5.0195947
[research_majji_rediniotis_2007]: https://doi.org/10.2514/6.2007-6310
[research_maki_1959]: https://ntrs.nasa.gov/citations/19980228300
[research_maki_2016]: https://doi.org/10.2514/6.2016-3849
[research_malcolm_1978]: https://ntrs.nasa.gov/citations/19780048477
[research_malcolm_1979]: https://doi.org/10.2514/3.58515
[research_malcolm_1985]: https://doi.org/10.2514/6.1985-1829
[research_malcolm_clarkson_1976]: https://ntrs.nasa.gov/citations/19760055676
[research_malcolm_davis_1978]: https://ntrs.nasa.gov/citations/19790006893
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malcom_husband_1976]: https://doi.org/10.2514/6.1976-1912
[research_malik_akhtar_2017]: https://doi.org/10.1080/02533839.2017.1347064
[research_malik_akhtar_2017_b]: https://doi.org/10.1177/0954410017718215
[research_malik_li_1993]: https://doi.org/10.2514/6.1993-77
[research_malik_li_1996]: https://doi.org/10.1007/978-94-009-1700-2_25
[research_malik_li_1999]: https://doi.org/10.1017/s0022112099006291
[research_malik_liao_2013]: https://doi.org/10.2514/6.2013-412
[research_malik_liao_2015]: https://doi.org/10.2514/1.j053637
[research_malik_masud_2020]: https://doi.org/10.1108/aeat-08-2019-0174
[research_malik_masud_2021]: https://doi.org/10.1108/aeat-04-2021-0136
[research_malvestuto_1946]: https://ntrs.nasa.gov/citations/19930092698
[research_malvestuto_1948]: https://ntrs.nasa.gov/citations/19930093751
[research_mamla_galinski_2009]: https://doi.org/10.2514/1.42084
[research_manan_cooper_2008]: https://doi.org/10.2514/6.2008-5868
[research_manchester_lipton_2017]: https://doi.org/10.2514/6.2017-0011
[research_mancini_matsuhiro_1976]: https://ntrs.nasa.gov/citations/19760021190
[research_mangalam_jutte_2010]: https://doi.org/10.2514/6.2010-8113
[research_mann_huffman_1987]: https://ntrs.nasa.gov/citations/19870017441
[research_mann_mercer_1985]: https://doi.org/10.2514/6.1985-4069
[research_mann_mercer_1986]: https://doi.org/10.2514/3.56774
[research_manoilo_2026]: https://doi.org/10.62717/3083-7057-2026-1-109
[research_manokaran_vidya_2006]: https://doi.org/10.2514/6.2006-3458
[research_manor_wentz_1985]: https://doi.org/10.2514/3.45083
[research_mansfield_1952]: https://doi.org/10.1108/eb032130
[research_manu_2026]: https://doi.org/10.1016/j.tws.2026.115059
[research_manuilovich_2014]: https://doi.org/10.1134/s001546281404005x
[research_manuilovich_2020]: https://doi.org/10.1134/s0015462820010097
[research_manuilovich_2021]: https://doi.org/10.1134/s0015462821050086
[research_manuilovich_2023]: https://doi.org/10.1134/s0015462823600700
[research_manzo_garcia_2010]: https://doi.org/10.1088/0964-1726/19/2/025012
[research_mao_xie_2019]: https://doi.org/10.1155/2019/5847627
[research_marchetti_2023]: https://doi.org/10.21741/9781644902813-8
[research_marchmaniii_donatelli_1983]: https://doi.org/10.2514/6.1983-2555
[research_mardanpour_hodges_2013]: https://doi.org/10.2514/6.2013-1570
[research_mardanpour_hodges_2013_b]: https://doi.org/10.1007/978-3-642-40371-2_50
[research_mardanpour_hodges_2013_c]: https://doi.org/10.2514/1.c031955
[research_mardanpour_hodges_2014]: https://doi.org/10.1016/j.jfluidstructs.2013.09.020
[research_mares_sureshbabu_2026]: https://doi.org/10.2514/6.2026-112608
[research_margaris_gursul_2004]: https://doi.org/10.2514/6.2004-2619
[research_margolis_1947]: https://ntrs.nasa.gov/citations/20050080700
[research_marino_2004]: https://doi.org/10.1017/s000192400000035x
[research_marouf_hoarau_2023]: https://doi.org/10.1108/hff-09-2022-0559
[research_marquart_1993]: https://doi.org/10.2514/6.1993-3457
[research_marschalk_luteijn_2021]: https://doi.org/10.2514/6.2021-0286
[research_marsden_price_2001]: https://doi.org/10.2514/6.2001-1590
[research_marske_1975]: https://doi.org/10.4271/750548
[research_martin_1953]: https://ntrs.nasa.gov/citations/19930087649
[research_martin_2008]: https://doi.org/10.2514/6.2008-7337
[research_martin_beissner_1988]: https://ntrs.nasa.gov/citations/19880064735
[research_martin_carpenter_2008]: https://doi.org/10.2514/6.2008-1636
[research_martin_crossley_2002]: https://doi.org/10.2514/6.2002-5859
[research_martin_hill_1989]: https://doi.org/10.2514/6.1989-3363
[research_martina_1956]: https://ntrs.nasa.gov/citations/19920075067
[research_martina_1956_b]: https://ntrs.nasa.gov/citations/19930089310
[research_martina_young_1955]: https://ntrs.nasa.gov/citations/19930088508
[research_martinez_1961]: https://doi.org/10.21236/ad0265941
[research_martins_2016]: https://doi.org/10.1002/9780470686652.eae1007
[research_marzocca_librescu_2001]: https://doi.org/10.2514/6.2001-714
[research_marzouk_2025_b]: https://doi.org/10.2139/ssrn.5067992
[research_masaoka_hashimoto_2024]: https://doi.org/10.1109/icrca60878.2024.10649279
[research_mason_1953]: https://ntrs.nasa.gov/citations/20050041783
[research_mason_1982]: https://doi.org/10.2514/6.1982-97
[research_mason_1983]: https://doi.org/10.2514/6.1983-1858
[research_masson_veilleux_1999]: https://doi.org/10.2514/6.1999-3187
[research_masud_malik_2016]: https://doi.org/10.2514/6.2016-1038
[research_matalla_scholz_2021]: https://doi.org/10.31224/osf.io/7fkaq
[research_mateer_bertelrud_1983]: https://doi.org/10.2514/6.1983-1725
[research_mateju_2019]: https://doi.org/10.13164/conf.read.2018.13
[research_mathioulakis_georgantopoulou_2025]: https://doi.org/10.1007/s00707-025-04597-y
[research_matsuno_esaki_2020]: https://doi.org/10.2514/6.2020-0826
[research_matsushima_takanashi_1996]: https://doi.org/10.2514/6.1996-2465
[research_matusu_prokop_2015]: https://doi.org/10.1016/j.ifacol.2015.09.468
[research_maughmer_1987]: https://doi.org/10.2514/6.1987-2937
[research_mavriplis_yang_2020]: https://doi.org/10.2514/6.2020-1292
[research_mayes_lores_1970]: https://doi.org/10.2514/3.44207
[research_mcclain_2022]: https://doi.org/10.2514/6.2022-4069
[research_mcconnell_2004]: https://doi.org/10.2514/6.2004-5048
[research_mccormick_1959]: https://doi.org/10.2514/8.8022
[research_mccuish_caldwell_2018]: https://doi.org/10.1201/9781315136820-12
[research_mccutchen_1989]: https://doi.org/10.2514/3.45790
[research_mcdaniel_wilks_2004]: https://doi.org/10.2514/6.2004-5194
[research_mcelroy_sharp_1971]: https://doi.org/10.2514/6.1971-772
[research_mcfadden_bons_2025]: https://doi.org/10.2514/6.2025-0481
[research_mcfadden_brandt_2022]: https://doi.org/10.2514/6.2022-3468
[research_mcfadden_brandt_2022_b]: https://doi.org/10.2514/6.2022-1546
[research_mcfadden_heinle_1954]: https://ntrs.nasa.gov/citations/19930088281
[research_mcfall_1964]: https://ntrs.nasa.gov/citations/19650025606
[research_mcfarlane_richardson_2008]: https://doi.org/10.2514/6.2008-7156
[research_mcgeer_1984]: https://doi.org/10.2514/3.45058
[research_mcgrath_1993]: https://doi.org/10.2514/6.1993-3505
[research_mcgurk_stodieck_2024]: https://doi.org/10.1016/j.compstruct.2023.117794
[research_mckenzie_1973]: https://doi.org/10.2514/6.1973-782
[research_mcklnney_dollyhlgh_1971]: https://doi.org/10.2514/3.59148
[research_mclachlan_bell_1995]: https://ntrs.nasa.gov/citations/19960016672
[research_mclaughlin_sawyer_1967]: https://ntrs.nasa.gov/citations/19670028345
[research_mclellan_cangelosi_1948]: https://ntrs.nasa.gov/citations/19930082243
[research_mclemore_1958]: https://ntrs.nasa.gov/citations/19980231988
[research_mclemore_parlett_1974]: https://ntrs.nasa.gov/citations/19740018344
[research_mclemore_parlett_1977]: https://ntrs.nasa.gov/citations/19770019126
[research_mcmaster_schenk_1973]: https://doi.org/10.2514/6.1973-822
[research_mcmurtry_sim_1981]: https://ntrs.nasa.gov/citations/19820030855
[research_mctavish]: https://doi.org/10.22215/etd/2008-08205
[research_medina_rockwood_2019]: https://doi.org/10.2514/6.2019-2324
[research_meheut_arntz_2012]: https://doi.org/10.2514/6.2012-3122
[research_mehndiratta_malhotra_2026]: https://doi.org/10.2139/ssrn.6879725
[research_mehrotra_lan_1978]: https://ntrs.nasa.gov/citations/19780010050
[research_mehrotra_lan_1978_b]: https://ntrs.nasa.gov/citations/19800017769
[research_mehta_1986]: https://ntrs.nasa.gov/citations/19880020390
[research_mehta_frecker_2008]: https://doi.org/10.1117/12.773599
[research_mei_striz_1992]: https://doi.org/10.2514/6.1992-4794
[research_mele_ostieri_2017]: https://doi.org/10.2514/1.c034288
[research_melton]: https://ntrs.nasa.gov/citations/20250003785
[research_melton_dudley_2016]: https://ntrs.nasa.gov/citations/20160007299
[research_melville_gordnier_1998]: https://doi.org/10.2514/6.1998-2657
[research_melvin_zhao_2023]: https://doi.org/10.1115/ssdm2023-106970
[research_melvin_zhao_2024]: https://doi.org/10.1115/1.4066309
[research_mendenhall_spangler_1979]: https://doi.org/10.2514/6.1979-120
[research_meneghello_schmid_2015]: https://doi.org/10.1017/jfm.2015.282
[research_meng_lei_2025]: https://doi.org/10.1063/5.0261841
[research_meng_wang_2024]: https://doi.org/10.2139/ssrn.4811594
[research_mennu_tran_2022]: https://doi.org/10.1177/1045389x221128570
[research_menon_chakravarthy_2018]: https://doi.org/10.2514/6.2018-0872
[research_menzies_kandil_1995]: https://doi.org/10.2514/6.1995-1771
[research_merrett_2015]: https://doi.org/10.2514/6.2015-0193
[research_mestrinho_gamboa_2011]: https://doi.org/10.2514/6.2011-2025
[research_methel_mery_2022]: https://doi.org/10.23967/eccomas.2022.160
[research_method_of_2020]: https://doi.org/10.15372/pmtf20200210
[research_methods_for_2003]: https://doi.org/10.2514/5.9781600861840.0019.0028
[research_methods_for_2003_b]: https://doi.org/10.2514/5.9781600861840.0285.0296
[research_meyer_trujillo_1987]: https://ntrs.nasa.gov/citations/19900003231
[research_michaud_dalir_2018]: https://doi.org/10.2514/1.c034340
[research_michel_arnal_1985]: https://doi.org/10.1007/978-3-642-82462-3_69
[research_midmer_bruecker_2024]: https://doi.org/10.2514/6.2024-4474
[research_mignosi_dor_1986]: https://doi.org/10.1007/978-3-642-82770-9_18
[research_mikhailov_2020]: https://doi.org/10.26467/2079-0619-2020-23-6-101-120
[research_miklosovic_perry_2014]: https://doi.org/10.2514/6.2014-2796
[research_miles_1949]: https://doi.org/10.2514/8.11836
[research_miles_1953]: https://doi.org/10.1017/s0001925900000901
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1983]: https://doi.org/10.2514/6.1983-2482
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_hadley_1983]: https://doi.org/10.2514/6.1983-1833
[research_miller_jacques_2003]: https://doi.org/10.2514/6.2003-5407
[research_miller_wykes_1982]: https://doi.org/10.2514/6.1982-683
[research_miller_wykes_1983]: https://doi.org/10.2514/3.44931
[research_millidere_karaman_2021]: https://doi.org/10.2514/6.2021-0411
[research_mir_maqsood_2018]: https://doi.org/10.1007/s42405-018-0086-3
[research_mishriky_walsh_2021]: https://doi.org/10.32920/14636265.v2
[research_mishriky_walsh_2023]: https://doi.org/10.32920/14636265.v1
[research_mistry_page_2012]: https://doi.org/10.2514/6.2012-2694
[research_mistry_page_2013]: https://doi.org/10.2514/6.2013-2842
[research_mitashova_2022]: https://doi.org/10.1007/978-3-030-85233-7_28
[research_mitcham_1957]: https://ntrs.nasa.gov/citations/19660010454
[research_mitcham_blanchard_1950]: https://ntrs.nasa.gov/citations/20050019416
[research_miwa_yoshimi_2022]: https://doi.org/10.1007/978-981-19-2689-1_56
[research_miyake_terashima_2026]: https://doi.org/10.2514/1.j066278
[research_mkhoyan_thakrar_2020]: https://doi.org/10.1115/smasis2020-2370
[research_mkhoyan_thakrar_2021]: https://doi.org/10.2514/6.2021-0477
[research_mkhoyan_thakrar_2022]: https://doi.org/10.1088/1361-665x/aca18b
[research_mo_kim_2019]: https://doi.org/10.5302/j.icros.2019.19.0035
[research_model_rotor_2006]: https://doi.org/10.2514/5.9781600862373.0557.0578
[research_modern_wing_1936]: https://doi.org/10.1108/eb030089
[research_modi_ananthkrishnan_1998]: https://doi.org/10.2514/2.2354
[research_moeckel_1948]: https://ntrs.nasa.gov/citations/19930082351
[research_moeller_rediniotis_2000]: https://doi.org/10.2514/6.2000-117
[research_moeller_rediniotis_2002]: https://doi.org/10.2514/2.3032
[research_moens_2019]: https://doi.org/10.3390/biomimetics4030064
[research_moens_2025]: https://doi.org/10.2514/1.c038496
[research_moghadam_ure_2018]: https://doi.org/10.2514/6.2018-1594
[research_mohammed_2007]: https://doi.org/10.30684/etj.25.6.5
[research_mohammed_2015]: https://doi.org/10.13111/2066-8201.2015.7.2.10
[research_mohdnasir_2026]: https://doi.org/10.24191/jmeche.v23i3.11599
[research_moigne_qin_2006]: https://doi.org/10.1017/s0001924000001457
[research_molent_jones_2018]: https://doi.org/10.1016/b978-0-08-100540-8.00010-8
[research_molton_dandois_2013]: https://doi.org/10.2514/1.j051000
[research_momodu_beg_2026]: https://doi.org/10.54709/joebs.1781579
[research_monaghan_1978]: https://ntrs.nasa.gov/citations/19780015113
[research_monfort_1975]: https://ntrs.nasa.gov/citations/19760019102
[research_monsch_figliola_2007]: https://doi.org/10.2514/6.2007-1079
[research_monstein_capone_2019]: https://doi.org/10.2514/1.c035171
[research_montgomery_hunsaker_2019]: https://doi.org/10.2514/6.2019-2041
[research_montgomery_hunsaker_2022]: https://doi.org/10.2514/6.2022-2531
[research_montgomery_moul_1966]: https://doi.org/10.2514/3.43777
[research_montoya_steers_1981]: https://ntrs.nasa.gov/citations/19840019594
[research_moon_1996]: https://doi.org/10.21236/ada361169
[research_moore_1965]: https://ntrs.nasa.gov/citations/19650026230
[research_moore_frei_1983]: https://doi.org/10.2514/6.1983-1834
[research_moore_skow_1980]: https://doi.org/10.2514/6.1980-173
[research_moored_bartsmith_2005]: https://doi.org/10.1115/imece2005-79706
[research_moorthamers_hunsaker_2019]: https://doi.org/10.2514/6.2019-0032
[research_moorthamers_wiberg_2021]: https://doi.org/10.2514/6.2021-1825
[research_moosavi_2025]: https://doi.org/10.2514/1.j065155
[research_moosavi_elasha_2022]: https://doi.org/10.3390/designs6020029
[research_moosavian_2021]: https://doi.org/10.32920/ryerson.14654676
[research_moosavian_xi_2013]: https://doi.org/10.2514/1.c032127
[research_moosavian_xi_2014]: https://doi.org/10.2514/1.c032451
[research_morehouse_1977]: https://ntrs.nasa.gov/citations/19780006055
[research_morelli_2021]: https://doi.org/10.2514/6.2021-1642
[research_morelli_2022]: https://doi.org/10.2514/1.g006072
[research_mori_yakeno_2024]: https://doi.org/10.2514/6.2024-1565
[research_mori_yakeno_2024_b]: https://doi.org/10.2514/6.2024-4486
[research_morphing_wing_2010]: https://doi.org/10.5220/0002885701140124
[research_morphing_wing_2018]: https://doi.org/10.1016/c2015-0-01317-x
[research_morris_1990]: https://ntrs.nasa.gov/citations/19930074026
[research_morris_kennedy_1950]: https://ntrs.nasa.gov/citations/19930086449
[research_morris_silsby_1952]: https://ntrs.nasa.gov/citations/19930087995
[research_morris_silsby_1954]: https://ntrs.nasa.gov/citations/19930088113
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_moseley_1951]: https://ntrs.nasa.gov/citations/19930086935
[research_moseley_gainer_1959]: https://ntrs.nasa.gov/citations/19980232889
[research_moskalenko_kosyrev_2019]: https://doi.org/10.18698/2308-6033-2019-7-1896
[research_mottershead_cooper_2012]: https://doi.org/10.21236/ada571493
[research_motycka_skowronek_1967]: https://doi.org/10.2514/3.43838
[research_moujie_1979]: https://doi.org/10.2514/6.1979-1877
[research_moulton_bolander_2026]: https://doi.org/10.2514/1.c038453
[research_moura_nepomuceno_2024]: https://doi.org/10.2514/6.2024-4585
[research_mousseux_1989]: https://ntrs.nasa.gov/citations/19900058397
[research_mouton_charpentier_2026]: https://doi.org/10.2514/1.c038763
[research_mughal_ashworth_2013]: https://doi.org/10.2514/6.2013-3106
[research_mugler_1958]: https://ntrs.nasa.gov/citations/19980232050
[research_mugler_1959]: https://ntrs.nasa.gov/citations/19650003091
[research_mugler_1959_b]: https://ntrs.nasa.gov/citations/19980228025
[research_mugler_woodall_1960]: https://ntrs.nasa.gov/citations/20040027968
[research_muhammadumer_maqsood_2020]: https://doi.org/10.1155/2020/4838632
[research_mukhopadhyay_1995]: https://doi.org/10.2514/6.1995-3943
[research_mukhtar_2023]: https://doi.org/10.32920/23328482.v1
[research_muller_lutz_2020]: https://doi.org/10.2514/6.2020-2778
[research_multiloop_flight_1990]: https://doi.org/10.1515/9781400855988.600
[research_munoz_garciafogeda_2022]: https://doi.org/10.3390/aerospace9120804
[research_munoz_garciafogeda_2023]: https://doi.org/10.20944/preprints202311.0323.v1
[research_muraoka_okada_2009]: https://doi.org/10.2514/6.2009-1834
[research_murch_foster_2007]: https://ntrs.nasa.gov/citations/20070005804
[research_murphy_klein_2004]: https://doi.org/10.2514/6.2004-5277
[research_murphy_peloubet_1976]: https://doi.org/10.21236/adb013257
[research_murphy_rogers_1983]: https://ntrs.nasa.gov/citations/19830048658
[research_murri_croom_1983]: https://doi.org/10.2514/6.1983-1837
[research_musa_mansor_2015]: https://doi.org/10.2514/6.2015-1498
[research_musa_mansor_2026]: https://doi.org/10.2139/ssrn.7319830
[research_mushitani_hiramoto_2019]: https://doi.org/10.1299/jsmehs.2019.56.k023
[research_musso_vo_2026]: https://doi.org/10.2514/6.2026-2763
[research_myers_guruswamy_1983]: https://doi.org/10.2514/6.1983-922
[research_naca_1135]: https://ntrs.nasa.gov/citations/19930091059
[research_naca_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_naca_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_naca_1966]: https://ntrs.nasa.gov/citations/20080013519
[research_naca_1966_2]: https://ntrs.nasa.gov/citations/20080013521
[research_naca_1973]: https://ntrs.nasa.gov/citations/19730009309
[research_naca_1977]: https://ntrs.nasa.gov/citations/19770010094
[research_naca_conference_1947]: https://ntrs.nasa.gov/citations/19790079919
[research_naeseth_1956]: https://ntrs.nasa.gov/citations/19930089309
[research_naeseth_1956_b]: https://ntrs.nasa.gov/citations/19930089265
[research_nagamatsu_ficarra_1985]: https://doi.org/10.2514/6.1985-207
[research_nagel_fiedler_2015]: https://doi.org/10.1007/978-3-319-22413-8_14
[research_nagornov_2020]: https://doi.org/10.34759/trd-2020-113-19
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_naik_ostowari_1987]: https://doi.org/10.2514/6.1987-588
[research_naik_ostowari_1988]: https://doi.org/10.2514/6.1988-2549
[research_naik_ostowari_1990]: https://doi.org/10.2514/3.45906
[research_nakagawa_ishida_2023]: https://doi.org/10.1016/j.ijheatfluidflow.2023.109161
[research_nakamura_uehara_2017]: https://doi.org/10.1007/978-3-319-67988-4_70
[research_nakhla_elruby_2021]: https://doi.org/10.32393/csme.2021.150
[research_nam_chattopadhyay_1998]: https://doi.org/10.2514/6.1998-4834
[research_nam_chattopadhyay_2000]: https://doi.org/10.2514/2.1123
[research_namdeo_bhattacharyya_2023]: https://doi.org/10.2514/6.2023-4244
[research_namura_shimoyama_2015]: https://doi.org/10.2514/6.2015-2726
[research_nangia_ghoreyshi_2023]: https://doi.org/10.2514/6.2023-0821
[research_nangia_palmer_2002]: https://doi.org/10.2514/6.2002-4616
[research_nangia_palmer_2003]: https://doi.org/10.2514/6.2003-605
[research_nangia_palmer_2003_b]: https://doi.org/10.2514/6.2003-3927
[research_nangia_palmer_2005]: https://doi.org/10.2514/6.2005-243
[research_nangia_palmer_2007]: https://doi.org/10.2514/6.2007-4569
[research_nardi_1970]: https://doi.org/10.2514/6.1970-515
[research_nasir_kuntjoro_2013]: https://doi.org/10.4028/www.scientific.net/amm.393.329
[research_nath_ana_2017]: https://doi.org/10.14445/22315381/ijett-v54p212
[research_nathan_2026]: https://doi.org/10.2139/ssrn.7045238
[research_navaratna_lowenberg_2022]: https://doi.org/10.2514/1.c036157
[research_navaratna_pontillo_2022]: https://doi.org/10.33424/futurum331
[research_nazeer_2021]: https://doi.org/10.3390/act10060107
[research_neechan_yazdiharmin_2018]: https://doi.org/10.14419/ijet.v7i4.13.21349
[research_neely_1943]: https://ntrs.nasa.gov/citations/19930092806
[research_neely_koven_1947]: https://ntrs.nasa.gov/citations/19930086040
[research_negahban_hallonet_2025]: https://doi.org/10.3390/aerospace12050381
[research_negahban_saci_2025]: https://doi.org/10.3390/app15105570
[research_neihouse_1940]: https://ntrs.nasa.gov/citations/19930081639
[research_neihouse_1949]: https://ntrs.nasa.gov/citations/19930082541
[research_neihouse_carmel_1942]: https://ntrs.nasa.gov/citations/20150013604
[research_neihouse_lee_1951]: https://ntrs.nasa.gov/citations/20090023711
[research_neihouse_lichtenstein_1946]: https://ntrs.nasa.gov/citations/19930081653
[research_nellner_1993]: https://doi.org/10.1007/bf01176866
[research_nellner_zierep_1993]: https://doi.org/10.1007/bf01175596
[research_nelms_1976]: https://ntrs.nasa.gov/citations/19760062451
[research_nelms_bailey_1974]: https://ntrs.nasa.gov/citations/19740020394
[research_nelson_1992]: https://doi.org/10.2514/6.1992-2629
[research_ness_1971]: https://doi.org/10.2514/3.44301
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_neuert_dinkler_2020]: https://doi.org/10.1007/s13272-020-00467-6
[research_neves_mariani_2024]: https://doi.org/10.2514/6.2024-0140
[research_newell_marsh_1967]: https://doi.org/10.4271/670884
[research_newey]: https://doi.org/10.15368/theses.2020.107
[research_newman_swaim_1986]: https://doi.org/10.2514/3.20113
[research_newsam_midmer_2024]: https://doi.org/10.2514/6.2024-4131
[research_neyland_filippov_2004]: https://doi.org/10.1134/1.1774070
[research_ng_crouch_1999]: https://doi.org/10.1063/1.869860
[research_ng_ray_2003]: https://doi.org/10.2514/6.2003-45
[research_ng_skaff_1993]: https://doi.org/10.2514/6.1993-3492
[research_ng_skaff_1994]: https://doi.org/10.2514/3.46674
[research_nguyen_gilbert_1980]: https://doi.org/10.2514/6.1980-1582
[research_nguyen_hashemi_2018]: https://doi.org/10.2514/6.2018-0622
[research_nguyen_livne_2014]: https://doi.org/10.2514/6.2014-2441
[research_nguyen_ting_2013]: https://ntrs.nasa.gov/citations/20140008923
[research_nguyen_ting_2014]: https://doi.org/10.2514/6.2014-0839
[research_nguyen_tran_2016]: https://doi.org/10.1109/icmae.2016.7549558
[research_ni_hou_2015]: https://doi.org/10.2991/ameii-15.2015.253
[research_nial_1972]: https://doi.org/10.2514/6.1972-787
[research_nicholas_naville_1984]: https://ntrs.nasa.gov/citations/19840062226
[research_nichols_reichert_1993]: https://doi.org/10.1109/87.238400
[research_nicholsjr_englar_1980]: https://doi.org/10.2514/6.1980-1825
[research_nicholson_duan_2019]: https://doi.org/10.2514/6.2019-0334
[research_nicholson_zhang_2018]: https://doi.org/10.2514/6.2018-3076
[research_nicks_1983]: https://doi.org/10.2514/6.1983-2556
[research_nicolas_sullivan_2016]: https://doi.org/10.3390/aerospace3030018
[research_niedling_1980]: https://doi.org/10.2514/6.1980-3044
[research_niel]: https://doi.org/10.70675/0a5746acz2780z42a1z83e4zb2dace818ceb
[research_nielsen_kaattari_1953]: https://ntrs.nasa.gov/citations/19930093732
[research_nietogomez_chimenomanguan_2025]: https://doi.org/10.3390/aerospace12090783
[research_nigam_tang_2020]: https://doi.org/10.1109/aero47225.2020.9172606
[research_nikbay_acar_2015]: https://doi.org/10.2514/6.2015-3441
[research_nikolic_2006]: https://doi.org/10.2514/6.2006-7705
[research_nikolic_2007]: https://doi.org/10.2514/6.2007-1270
[research_nikolic_2008]: https://doi.org/10.2514/6.2008-290
[research_nishino_shariff_2009]: https://doi.org/10.1007/978-90-481-3723-7_46
[research_nitschkekowsky_bippes_1988]: https://doi.org/10.1063/1.866814
[research_nixon_1992]: https://ntrs.nasa.gov/citations/19920051858
[research_nixon_2001]: https://doi.org/10.2514/6.2001-419
[research_nixon_2006]: https://doi.org/10.2514/6.2006-3653
[research_nobleheart_l_2012]: https://doi.org/10.2514/6.2012-4614
[research_nobleheart_shivanapuralakshmikanth_2013]: https://doi.org/10.2514/6.2013-5003
[research_noll_calico_1983]: https://doi.org/10.2514/6.1983-2220
[research_noll_eastep_1983]: https://doi.org/10.2514/6.1983-991
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_noll_huttsell_1978]: https://doi.org/10.2514/6.1978-1459
[research_nominal_aircraft]: https://doi.org/10.1007/bfb0043102
[research_nomura_2003]: https://doi.org/10.2514/6.2003-4145
[research_nomura_2006]: https://doi.org/10.2322/tjsass.48.193
[research_nonlinear_aerolasticity_2007]: https://doi.org/10.1201/9781420011159-15
[research_nonweiler_1960]: https://doi.org/10.1017/s0368393100072485
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_northropaircraftinchawthorneca_1953]: https://doi.org/10.21236/ad0022941
[research_noviello_dimino_2019]: https://doi.org/10.3390/aerospace6100104
[research_noviello_rea_2016]: https://doi.org/10.1109/icmae.2016.7549578
[research_novikov_obraz_2024]: https://doi.org/10.1134/s0015462824600202
[research_nowak_solies_2000]: https://doi.org/10.2514/2.2637
[research_nudson_stanfieldbrown_2025]: https://doi.org/10.2514/1.c038055
[research_nugent_1956]: https://ntrs.nasa.gov/citations/19930089404
[research_nugroho_2026]: https://doi.org/10.14203/widyariset.14.3.2011.633-642
[research_numerical_investigation_2023]: https://doi.org/10.1063/5.0141784
[research_nusyirwan_kung_2016]: https://doi.org/10.1088/1757-899x/152/1/012020
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_obayashi]: https://doi.org/10.1109/icsmc.1998.726486
[research_obayashi_yamaguchi_1997]: https://doi.org/10.2514/2.2231
[research_oblique_wing_1974]: https://ntrs.nasa.gov/citations/19740013546
[research_oblique_wing_2020]: https://doi.org/10.1002/9781119667063.ch10
[research_obradovic_subbarao_2009]: https://doi.org/10.2514/6.2009-6240
[research_obradovic_subbarao_2010]: https://doi.org/10.2514/6.2010-8236
[research_obradovic_subbarao_2011]: https://doi.org/10.2514/1.c000269
[research_obradovic_subbarao_2011_b]: https://doi.org/10.2514/1.c000313
[research_obradovic_subbarao_2011_c]: https://doi.org/10.2514/6.2011-6390
[research_obradovic_subbarao_2012]: https://doi.org/10.1002/9781119964032.ch5
[research_oggioni_riboldi_2026]: https://doi.org/10.3390/engproc2026142017
[research_ogrady_reich_2009]: https://doi.org/10.1115/smasis2009-1456
[research_oh_tavella_1986]: https://doi.org/10.2514/6.1986-1790
[research_ohira_kwak_2013]: https://doi.org/10.2514/6.2013-342
[research_ohmichi_ishida_2018]: https://doi.org/10.2514/1.j056855
[research_okelly_1955]: https://ntrs.nasa.gov/citations/20090023313
[research_okelly_lundstrom_1954]: https://ntrs.nasa.gov/citations/19930088204
[research_oktay_eraslan_2022]: https://doi.org/10.30518/jav.1073417
[research_oktay_eraslan_2024]: https://doi.org/10.1108/aeat-09-2022-0262
[research_oktay_ozen_2022]: https://doi.org/10.30518/jav.1080139
[research_oktay_sultan_2014]: https://doi.org/10.2514/1.c032494
[research_oland_kristiansen_2013]: https://doi.org/10.1109/aero.2013.6497180
[research_olivett_corrao_2020]: https://doi.org/10.1115/smasis2020-2355
[research_olivett_corrao_2021]: https://doi.org/10.1088/1361-665x/abd347
[research_olson_dvorak_1976]: https://doi.org/10.2514/6.1976-18
[research_olstad_fischetti_1958]: https://ntrs.nasa.gov/citations/19980232010
[research_olugbejijemitola_peterokonkwo_2021]: https://doi.org/10.11648/j.ijmea.20210905.12
[research_onewein_1967]: https://doi.org/10.4271/670883
[research_onofri_antonini_2026]: https://doi.org/10.2514/6.2026-0621
[research_oosterom_babuska]: https://doi.org/10.1109/fuzz.2001.1009055
[research_oosterom_babuska_2006]: https://doi.org/10.1016/j.conengprac.2005.03.012
[research_ordaz_geiselhart_2015]: https://doi.org/10.2514/1.c033160
[research_orloff_1978]: https://doi.org/10.2514/6.1978-1195
[research_orloff_ciffone_1974]: https://doi.org/10.2514/3.59259
[research_ortamevzi_2015]: https://doi.org/10.20535/2219-380413201569737
[research_ortiz_alley_2018]: https://ntrs.nasa.gov/citations/20180004640
[research_oshima_wygnanski_2022]: https://doi.org/10.2514/6.2022-2426
[research_otto_streett_1994]: https://doi.org/10.1007/978-94-011-1032-7_32
[research_outlaw_2011]: https://doi.org/10.15394/jaaer.2011.1348
[research_ouyang_zeng_2021]: https://doi.org/10.1155/2021/5535192
[research_owens_perkins_1996]: https://doi.org/10.2514/3.47079
[research_oyama_ito_2008]: https://doi.org/10.2514/6.2008-354
[research_oyibo_1984]: https://doi.org/10.2514/3.48423
[research_ozbek_ekici_2023]: https://doi.org/10.3390/drones7060379
[research_ozbek_ekici_2024]: https://doi.org/10.1108/aeat-04-2024-0096
[research_pabla_2021]: https://doi.org/10.32920/ryerson.14657811
[research_pagano_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00025-3
[research_page_1965]: https://doi.org/10.1108/eb034081
[research_paget_1967]: https://doi.org/10.4271/670882
[research_pahle_1990]: https://ntrs.nasa.gov/citations/19900009925
[research_painter_1978]: https://ntrs.nasa.gov/citations/19790005843
[research_painter_1983]: https://ntrs.nasa.gov/citations/19840027786
[research_pak_lung_2011]: https://doi.org/10.2514/1.c031257
[research_pak_truong_2015]: https://doi.org/10.2514/1.c033043
[research_palaia_salem_2025]: https://doi.org/10.2514/1.c038131
[research_pamadi_1988]: https://doi.org/10.2514/6.1988-4339
[research_pamadi_pai_1980]: https://doi.org/10.2514/3.44663
[research_pamadi_taylor_1982]: https://ntrs.nasa.gov/citations/19820055557
[research_pamnani_jeughale_2021]: https://doi.org/10.21275/sr21908201517
[research_pamnani_jeughale_2021_b]: https://doi.org/10.21275/sr21914185449
[research_pan_2026]: https://doi.org/10.1088/1742-6596/3207/1/012030
[research_pan_cheng_1994]: https://doi.org/10.2514/6.1994-284
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pande_2025]: https://doi.org/10.36948/ijfmr.2025.v07i05.58371
[research_pandi_kumar_2025]: https://doi.org/10.1063/5.0301408
[research_panel_flutter_1991]: https://doi.org/10.2514/6.1991-746
[research_panina_kosinov_2017]: https://doi.org/10.1063/1.5007538
[research_panina_yatskikh_2021]: https://doi.org/10.1063/5.0052064
[research_paniszczyn_1967]: https://doi.org/10.2514/6.1967-135
[research_pant_fielding_1999]: https://doi.org/10.1016/s1369-8869(99)00020-8
[research_pao_lan_1978]: https://ntrs.nasa.gov/citations/19780009059
[research_papadakis_yeong_2003]: https://doi.org/10.2514/6.2003-731
[research_papadakis_yeong_2004]: https://doi.org/10.2514/6.2004-734
[research_paranjape_2022]: https://doi.org/10.2514/6.2022-0137
[research_paranjape_2023]: https://doi.org/10.2514/6.2023-0983
[research_paranjape_ananthkrishnan_2010]: https://doi.org/10.2514/1.c031010
[research_paranjape_chung_2010]: https://doi.org/10.2514/6.2010-7633
[research_park_2007]: https://doi.org/10.21236/ada474610
[research_park_matuda_1996]: https://doi.org/10.2331/suisan.62.248
[research_parlett_shivers_1976]: https://ntrs.nasa.gov/citations/19760015099
[research_parra_2023]: https://doi.org/10.55592/icimesteam.2022.4600983
[research_parsons_1958]: https://doi.org/10.4095/324473
[research_pasamanick_sellers_1950]: https://ntrs.nasa.gov/citations/19930086172
[research_pashilkar_1996]: https://doi.org/10.2514/6.1996-3505
[research_passive_wing_store_1982]: https://doi.org/10.1121/1.387660
[research_pate_1964]: https://doi.org/10.21236/ad0450195
[research_pate_brillhart_1963]: https://doi.org/10.21236/ad0410130
[research_pate_deitering_1963]: https://doi.org/10.21236/ad0297204
[research_pate_deitering_1963_b]: https://doi.org/10.21236/ad0405150
[research_pate_german_2014]: https://doi.org/10.2514/6.2014-2868
[research_patierno_1980]: https://doi.org/10.2514/6.1980-3045
[research_patil_2003]: https://doi.org/10.2514/6.2003-1487
[research_patil_2004]: https://doi.org/10.2514/1.11482
[research_patterson_1984]: https://doi.org/10.2514/6.1984-2491
[research_patterson_loving_1961]: https://ntrs.nasa.gov/citations/19980223585
[research_pattinson_lowenberg_2013]: https://doi.org/10.2514/1.c032184
[research_pattinson_lowenberg_2013_b]: https://doi.org/10.2514/1.c031924
[research_patton_1980]: https://ntrs.nasa.gov/citations/19800024832
[research_patton_1980_b]: https://ntrs.nasa.gov/citations/19810035067
[research_patton_stough_1979]: https://ntrs.nasa.gov/citations/19790052693
[research_paudel_2021]: https://doi.org/10.32920/ryerson.14645931
[research_pavelka_tatum_1980]: https://doi.org/10.2514/6.1980-1620
[research_paziresh_nikseresht_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000704
[research_pearcey_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50021-1
[research_peck_groot_2024]: https://doi.org/10.1017/jfm.2024.299
[research_peck_hudson_1956]: https://doi.org/10.21236/ad0140230
[research_pecora_2018]: https://doi.org/10.1115/smasis2018-8108
[research_pecora_2021]: https://doi.org/10.1016/j.cja.2020.08.004
[research_pecora_amoroso_2012]: https://doi.org/10.2514/1.c000328
[research_pecora_pecora_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00014-9
[research_peele_1975]: https://ntrs.nasa.gov/citations/19750023957
[research_peltzer_wicke_2009]: https://doi.org/10.1007/978-90-481-3723-7_50
[research_pena_2018]: https://ntrs.nasa.gov/citations/20190033242
[research_pena_2020]: https://ntrs.nasa.gov/citations/20200001121
[research_peng_avallone_2022]: https://doi.org/10.1063/5.0124818
[research_peng_avallone_2024]: https://doi.org/10.1017/jfm.2024.714
[research_pengelley_wilson_1954]: https://doi.org/10.21236/ad0061591
[research_pengyuan_yanfei_2024]: https://doi.org/10.1117/12.3032471
[research_penner_sousa_2025]: https://doi.org/10.64631/zxtt6538
[research_pepoon_1944]: https://ntrs.nasa.gov/citations/19930092703
[research_perera_2021]: https://doi.org/10.32920/ryerson.14643981
[research_perera_guo_2008]: https://doi.org/10.2514/6.2008-5969
[research_perez_rodriguez_2011]: https://doi.org/10.2514/6.2011-3606
[research_perez_rodriguez_2012]: https://doi.org/10.1017/jfm.2012.354
[research_perezperez]: https://doi.org/10.20868/upm.thesis.14835
[research_perraud_moens_2003]: https://doi.org/10.2514/6.2003-3796
[research_perraud_seraudie_2004]: https://doi.org/10.2514/1.4297
[research_perry_1966]: https://doi.org/10.2514/6.1966-983
[research_perry_miklosovic_2012]: https://doi.org/10.1115/imece2012-85266
[research_peter_stumpf_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00003-4
[research_petersen_1979]: https://doi.org/10.2514/6.1979-1789
[research_peterson_grant_2011]: https://doi.org/10.2514/6.2011-6542
[research_peterson_menees_1961]: https://ntrs.nasa.gov/citations/20040008213
[research_peterson_menees_1961_b]: https://ntrs.nasa.gov/citations/20040008249
[research_petre_ashley_1975]: https://doi.org/10.2514/6.1975-775
[research_petre_ashley_1976]: https://doi.org/10.2514/3.58707
[research_petrov_1993]: https://doi.org/10.2514/6.1993-4836
[research_petrov_2009]: https://doi.org/10.1615/tsagiscij.v40.i5.20
[research_pettit_grandhi_2003]: https://doi.org/10.2514/2.7208
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfenninger_bacon_1961]: https://doi.org/10.1016/b978-1-4832-1323-1.50016-6
[research_pfenninger_bacon_1969]: https://doi.org/10.1007/978-1-4899-5579-1_4
[research_pfenninger_groth_1961]: https://doi.org/10.1016/b978-1-4832-1323-1.50014-2
[research_pfenninger_vemuru_1988]: https://doi.org/10.2514/6.1988-4471
[research_pfnur_breitsamter_2019]: https://doi.org/10.2514/1.c035491
[research_pfnur_oppelt_2018]: https://doi.org/10.1007/s13272-018-0340-1
[research_pham_perazahernandez_2021]: https://doi.org/10.2514/6.2021-0099
[research_philipsen_postma_2015]: https://doi.org/10.2514/6.2015-1561
[research_phillips_1948]: https://ntrs.nasa.gov/citations/19930082293
[research_phillips_1989]: https://ntrs.nasa.gov/citations/19890007474
[research_phillips_anderson_2002]: https://doi.org/10.2514/6.2002-830
[research_phillips_anderson_2002_b]: https://doi.org/10.2514/2.3041
[research_phillips_fugal_2006]: https://doi.org/10.2514/1.15089
[research_phillips_hunsaker_2008]: https://doi.org/10.2514/6.2008-192
[research_phillips_hunsaker_2019]: https://doi.org/10.2514/6.2019-3349
[research_phillips_hunsaker_2020]: https://doi.org/10.1017/aer.2020.24
[research_phillips_west_2017]: https://doi.org/10.2514/6.2017-3047
[research_phillips_west_2019]: https://doi.org/10.2514/1.c034932
[research_phillips_wygnanski_2019]: https://doi.org/10.2514/6.2019-3393
[research_phuekpan_2025]: https://doi.org/10.3390/aerospace12020101
[research_physical_phenomena_1989]: https://doi.org/10.2514/5.9781600865947.0001.0055
[research_pier_2003]: https://doi.org/10.1017/s0022112003004981
[research_pirrung_sorensen_2026]: https://doi.org/10.1088/1742-6596/3224/4/042020
[research_pisaneschi_2026]: https://doi.org/10.3390/act15080416
[research_pitcher_maple_2008]: https://doi.org/10.2514/6.2008-4057
[research_pitkin_1943]: https://ntrs.nasa.gov/citations/19930092699
[research_pitkin_gardner_1947]: https://ntrs.nasa.gov/citations/19930085761
[research_pitt_2004]: https://doi.org/10.2514/6.2004-1754
[research_placement_in_2026]: https://doi.org/10.1017/9781009399913.015
[research_planeaux_1991]: https://doi.org/10.2514/6.1991-2887
[research_plante_dandois_2017]: https://doi.org/10.2514/6.2017-3903
[research_podugu_ananthasuresh_2010]: https://doi.org/10.1115/imece2010-38159
[research_pogosyan_2025]: https://doi.org/10.1007/978-981-96-4599-2_16
[research_polhamus_1948]: https://ntrs.nasa.gov/citations/19930085787
[research_polhamus_1960]: https://ntrs.nasa.gov/citations/19670023743
[research_polhamus_1963]: https://ntrs.nasa.gov/citations/19700028695
[research_polhamus_1981]: https://ntrs.nasa.gov/citations/19810016532
[research_polhamus_1983]: https://ntrs.nasa.gov/citations/19830068378
[research_polhamus_1984]: https://doi.org/10.2514/3.45023
[research_polidoro_bhattacharya_2026]: https://doi.org/10.2514/6.2026-0681
[research_poll_1986]: https://doi.org/10.1017/s0001924000015670
[research_poll_danks_1995]: https://doi.org/10.1007/978-3-642-79765-1_16
[research_poll_paisley_1985]: https://doi.org/10.1017/s0001924000050983
[research_pongkorung_2026]: https://doi.org/10.2514/6.2026-105983
[research_pons_cirak_2023]: https://doi.org/10.2514/1.g006381
[research_poojari_2022]: https://doi.org/10.47893/gret.2022.1089
[research_poomadath_ajaj_2025]: https://doi.org/10.2514/6.2025-3472
[research_popescu_1999]: https://doi.org/10.2514/6.1999-1441
[research_popescu_2000]: https://doi.org/10.2514/6.2000-1624
[research_popescu_2002]: https://doi.org/10.2514/6.2002-1291
[research_poplingher_raveh_2023]: https://doi.org/10.2514/6.2023-0760
[research_poplingher_raveh_2024]: https://doi.org/10.2514/6.2024-0828
[research_popov_grigorie_2010]: https://doi.org/10.2514/1.47281
[research_popov_grigorie_2010_b]: https://doi.org/10.2514/1.47431
[research_popov_grigorie_2010_c]: https://doi.org/10.2514/1.46480
[research_popov_labib_2008]: https://doi.org/10.2514/1.37073
[research_potapczuk_bidwell_1990]: https://doi.org/10.2514/6.1990-756
[research_potapczuk_bidwell_1991]: https://doi.org/10.2514/6.1991-263
[research_potapczuk_papadakis_2003]: https://doi.org/10.2514/6.2003-730
[research_potential_equation_1982]: https://doi.org/10.2514/5.9781600865558.0239.0296
[research_powers_1977]: https://ntrs.nasa.gov/citations/19780004157
[research_powers_webb_1992]: https://ntrs.nasa.gov/citations/19930002675
[research_powers_webb_1997]: https://ntrs.nasa.gov/citations/19970023528
[research_prabhakar_2025]: https://doi.org/10.52843/cassyni.fjt1xn
[research_prabhakar_murugan_2022]: https://doi.org/10.1115/smasis2022-90198
[research_prabhakar_murugan_2024]: https://doi.org/10.1088/1361-665x/ad765a
[research_prabhakar_murugan_2026]: https://doi.org/10.1007/978-3-032-16528-2_26
[research_prabhakar_prazenica_2015]: https://doi.org/10.1109/aero.2015.7119089
[research_prabhakar_prazenica_2019]: https://doi.org/10.2514/6.2019-1921
[research_prajapati_kapania_2026]: https://doi.org/10.2514/6.2026-1649
[research_prakash_uthup_2009]: https://doi.org/10.2514/6.2009-3631
[research_prandtl_1928]: https://ntrs.nasa.gov/citations/19930090813
[research_prasad_raghavulu_2024]: https://doi.org/10.1063/5.0218493
[research_pratt_shields_1952]: https://ntrs.nasa.gov/citations/19930086963
[research_prediction_of_1981]: https://doi.org/10.2514/6.1981-609
[research_prediction_of_1994]: https://doi.org/10.2514/6.1994-1883
[research_pressures_and_2000]: https://doi.org/10.1016/b978-012257060-5/50023-x
[research_preston_fasel_2026]: https://doi.org/10.2514/1.j065846
[research_preston_palacios_2025]: https://doi.org/10.2514/6.2025-1662
[research_previati_gobbi_2012]: https://doi.org/10.2514/1.c031369
[research_previtali_arrieta_2013]: https://doi.org/10.2514/6.2013-1514
[research_previtali_arrieta_2014]: https://doi.org/10.2514/1.j052764
[research_priest_snyder_2023]: https://doi.org/10.2514/6.2023-2431
[research_prior_rozinka_2023]: https://doi.org/10.2514/6.2023-4398
[research_properties_of_2014]: https://doi.org/10.2514/5.9781624102547.0625.0632
[research_properties_of_2024]: https://doi.org/10.2514/5.9781624107252.0695.0702
[research_prudenzano_gand_2025]: https://doi.org/10.2514/6.2025-2211
[research_pruett_chang_2000]: https://doi.org/10.1016/s0045-7930(98)00056-5
[research_pu_zhang_2024]: https://doi.org/10.1016/j.apm.2024.06.024
[research_pugliese_englar_1979]: https://doi.org/10.2514/6.1979-1791
[research_purser_spearman_1947]: https://ntrs.nasa.gov/citations/19930082014
[research_purser_spearman_1951]: https://ntrs.nasa.gov/citations/19930083063
[research_purwanto_riyanto_2001]: https://doi.org/10.1299/jsmemovic.2001.7.498
[research_pusztai_lowenberg_2024]: https://doi.org/10.2514/6.2024-1497
[research_puthisikamani_sreenivasaraja_2023]: https://doi.org/10.61653/joast.v74i4.2022.47
[research_putman_1969]: https://doi.org/10.21236/ad0859807
[research_putnam_ayers_1988]: https://ntrs.nasa.gov/citations/19880016977
[research_putnam_ayers_1989]: https://ntrs.nasa.gov/citations/19890011556
[research_putro_junipitoyo_2025]: https://doi.org/10.1007/978-981-96-5063-7_24
[research_puyou_berard_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00085
[research_pyeon_bae_2026]: https://doi.org/10.3390/drones10090671
[research_qi_zhao_2023]: https://doi.org/10.2514/1.j062988
[research_qi_zong_2021]: https://doi.org/10.1007/s13272-021-00538-2
[research_qian_guan_2012]: https://doi.org/10.4028/www.scientific.net/amr.487.267
[research_qiao_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9018937
[research_qiao_zhou_2019]: https://doi.org/10.1109/aero.2019.8742016
[research_qin_2012]: https://doi.org/10.1007/978-3-642-25688-2_7
[research_qin_wang_2014]: https://doi.org/10.2514/6.2014-2992
[research_qingbao_hui_2026]: https://doi.org/10.1109/yac71005.2026.11615727
[research_qu_wang_2024]: https://doi.org/10.56028/aetr.10.1.276.2024
[research_qu_wang_2025]: https://doi.org/10.2514/1.g008503
[research_quan_deng_2026]: https://doi.org/10.1088/1742-6596/3326/1/012032
[research_quan_ye_2013]: https://doi.org/10.2514/6.2013-2410
[research_quantitative_design_2017]: https://doi.org/10.2514/5.9781624104435.0105.0170
[research_quast_henke_1990]: https://doi.org/10.2514/6.1990-3045
[research_queijo_1954]: https://ntrs.nasa.gov/citations/19930092215
[research_queijo_jaquet_1948]: https://ntrs.nasa.gov/citations/19930082294
[research_queijo_jaquet_1948_b]: https://ntrs.nasa.gov/citations/19930082427
[research_queijo_lichtenstein_1948]: https://ntrs.nasa.gov/citations/19930085527
[research_queijo_wolhart_1951]: https://ntrs.nasa.gov/citations/19930086818
[research_querry]: https://doi.org/10.70675/be362339z0dfez4119zaaedz4df05825ab93
[research_quigley_1960]: https://ntrs.nasa.gov/citations/19980223993
[research_rade_desouza_2016]: https://doi.org/10.21236/ad1009258
[research_radeztsky_reibert_1995]: https://doi.org/10.1007/978-3-642-79765-1_35
[research_radhakrishnanp_ramanang_2021]: https://doi.org/10.34293/acsjse.v1i1.5
[research_radzetskyjr_reibert_1994]: https://doi.org/10.2514/6.1994-2373
[research_raghavan_patil_2009]: https://doi.org/10.2514/1.36847
[research_raghavendra_sahai_2005]: https://doi.org/10.2514/1.12252
[research_raheel_toropov_2018]: https://doi.org/10.2514/6.2018-3885
[research_rahman_aljibory_2022]: https://doi.org/10.18280/mmep.090323
[research_rahn_reinertson_1986]: https://ntrs.nasa.gov/citations/19860022091
[research_rajamurthy_2002]: https://doi.org/10.2514/6.2002-4712
[research_rajeshsenthilkumar_venugopal_2020]: https://doi.org/10.5028/jatm.v12.1094
[research_rajeswari_prabhu_1987]: https://doi.org/10.2514/3.45461
[research_ralson_1983]: https://ntrs.nasa.gov/citations/19830060739
[research_ramachandran_wells_1974]: https://ntrs.nasa.gov/citations/19740055060
[research_ramachandran_wells_1975]: https://doi.org/10.2514/3.59883
[research_rambacher_bons_2023]: https://doi.org/10.2514/6.2023-1239
[research_rambacher_butler_2024]: https://doi.org/10.2514/6.2024-1936
[research_ramirezzeigler_avery_2026]: https://doi.org/10.2514/6.2026-4580
[research_ramprasadh_devanandh_2015]: https://doi.org/10.1260/1756-8293.7.3.361
[research_raney_1987]: https://ntrs.nasa.gov/citations/19870062350
[research_raney_batterson_1989]: https://ntrs.nasa.gov/citations/19890012431
[research_rao_1982]: https://ntrs.nasa.gov/citations/19820038517
[research_rao_1983]: https://ntrs.nasa.gov/citations/19840004061
[research_rao_1992]: https://doi.org/10.2514/6.1992-2637
[research_rao_2019]: https://doi.org/10.1109/indiancc.2019.8715608
[research_rao_huffman_1978]: https://ntrs.nasa.gov/citations/19780024105
[research_rao_sinha_2010]: https://doi.org/10.2514/1.50186
[research_rao_spin_2019]: https://doi.org/10.1016/j.ast.2019.04.046
[research_raol_singh_2023]: https://doi.org/10.1201/9781003293514-11
[research_rashad_elbadawy_2025]: https://doi.org/10.2514/6.2025-2080
[research_ratcliff_carlson_1989]: https://doi.org/10.2514/6.1989-2204
[research_rathert_1951]: https://ntrs.nasa.gov/citations/19930086490
[research_rausch_batina_1992]: https://ntrs.nasa.gov/citations/19920013873
[research_raveh_levy_2004]: https://doi.org/10.2514/6.2004-1515
[research_ray_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_razak_andrianne_2011]: https://doi.org/10.2514/1.j051041
[research_razi_ghadiri_2008]: https://doi.org/10.1243/09544100jaero224
[research_re_reubush_1979]: https://ntrs.nasa.gov/citations/19800001867
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_recktenwald_ahmed_2008]: https://doi.org/10.2514/6.2008-371
[research_redd_gilman_1974]: https://doi.org/10.2514/3.60401
[research_reddy_1981]: https://doi.org/10.2514/3.44730
[research_reddy_ghaffari_1982]: https://ntrs.nasa.gov/citations/19830004806
[research_redeker_wichmann_1988]: https://doi.org/10.2514/6.1988-4418
[research_redeker_wichmann_1991]: https://doi.org/10.2514/3.45997
[research_redin_1981]: https://ntrs.nasa.gov/citations/19810015513
[research_rediniotis_klute_1994]: https://doi.org/10.2514/3.12044
[research_reed_1955]: https://ntrs.nasa.gov/citations/19930088802
[research_reed_1975]: https://ntrs.nasa.gov/citations/19760003013
[research_reed_1984]: https://doi.org/10.2514/6.1984-1678
[research_reed_1985]: https://doi.org/10.1007/978-3-642-82462-3_57
[research_reed_1987]: https://doi.org/10.1063/1.866473
[research_reed_1989]: https://ntrs.nasa.gov/citations/19900004428
[research_reed_1991]: https://ntrs.nasa.gov/citations/19910012782
[research_reed_saric_2002]: https://doi.org/10.2514/6.2002-147
[research_reeh_weismuller_2013]: https://doi.org/10.2514/6.2013-994
[research_reeh_weismuller_2014]: https://doi.org/10.2514/1.j052818
[research_reibert_saric_1996]: https://doi.org/10.2514/6.1996-184
[research_reibert_saric_1997]: https://doi.org/10.2514/6.1997-1816
[research_reich_raveh_2002]: https://doi.org/10.2514/6.2002-1633
[research_reich_raveh_2004]: https://doi.org/10.2514/1.78
[research_reich_sanders_2007]: https://doi.org/10.2514/6.2007-1738
[research_reich_sanders_2007_b]: https://doi.org/10.2514/1.28287
[research_reid_rajagopal_1994]: https://doi.org/10.2514/3.46607
[research_reimer_braun]: https://doi.org/10.1007/978-3-540-36183-1_31
[research_rein_henne_2025]: https://doi.org/10.2514/1.j065181
[research_ren_2026]: https://doi.org/10.1016/j.ast.2025.111171
[research_ren_kan_2025]: https://doi.org/10.2139/ssrn.5320170
[research_ren_wei_2025]: https://doi.org/10.3390/drones9080562
[research_ren_wei_2025_b]: https://doi.org/10.3390/app15084380
[research_report_no_1927]: https://doi.org/10.1016/s0016-0032(27)91354-4
[research_report_no_1930]: https://doi.org/10.1016/s0016-0032(30)90271-2
[research_report_no_1935]: https://doi.org/10.1016/s0016-0032(35)90062-x
[research_reshotko_vargas_2000]: https://doi.org/10.1007/978-3-662-03997-7_89
[research_reubush_1977]: https://doi.org/10.2514/6.1977-884
[research_reubush_1978]: https://doi.org/10.2514/6.1978-1083
[research_reubush_1979]: https://doi.org/10.2514/3.58532
[research_reubush_mercer_1974]: https://ntrs.nasa.gov/citations/19740020411
[research_reubush_mercer_1975]: https://ntrs.nasa.gov/citations/19750010108
[research_review_of_1982]: https://doi.org/10.2514/5.9781600865558.0001.0001
[research_revivo_raveh_2025]: https://doi.org/10.2514/6.2025-1018
[research_rhoads_1952]: https://doi.org/10.21236/ad0014479
[research_rhoads_1970]: https://doi.org/10.21236/ad0876589
[research_rhodes_johns_1966]: https://doi.org/10.2514/3.59267
[research_rhudy_2016]: https://doi.org/10.2514/6.2016-4301
[research_riahi_vonderwell_1994]: https://doi.org/10.1007/978-94-011-1032-7_21
[research_ribeiro_yeh_2022]: https://doi.org/10.1017/jfm.2022.612
[research_ribner_1960]: https://doi.org/10.2514/8.8580
[research_richardson_1968]: https://ntrs.nasa.gov/citations/19680024197
[research_richardson_1968_b]: https://ntrs.nasa.gov/citations/19680027594
[research_richardson_1976]: https://doi.org/10.21236/adb012971
[research_richardson_davison_2003]: https://doi.org/10.2514/6.2003-5503
[research_rickard_1978]: https://doi.org/10.2514/6.1978-1371
[research_ricketts_1980]: https://ntrs.nasa.gov/citations/19800020786
[research_ricketts_1985]: https://ntrs.nasa.gov/citations/19850022052
[research_ricouard_davy_2004]: https://doi.org/10.2514/6.2004-2867
[research_riebe_watson_1950]: https://ntrs.nasa.gov/citations/19930082868
[research_rieber_allgower_2006]: https://doi.org/10.3182/20060705-3-fr-2907.00115
[research_rigid_body_flight_2026]: https://doi.org/10.1017/9781009399913.005
[research_rimer_chipman_1983]: https://doi.org/10.2514/6.1983-2125
[research_rimer_chipman_1984]: https://ntrs.nasa.gov/citations/19840060637
[research_rimer_chipman_1984_b]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_riou_garnier_2010]: https://doi.org/10.1063/1.3327286
[research_riso_cesnik_2022]: https://doi.org/10.2514/6.2022-2313
[research_riso_divincenzo_2018]: https://doi.org/10.2514/1.c034787
[research_ritchie_1973]: https://doi.org/10.4271/730330
[research_ritter_dillinger_2017]: https://doi.org/10.2514/6.2017-0637
[research_rivaspadilla_boston_2023]: https://doi.org/10.1177/00219983231155163
[research_rizzetta_visbal_2016]: https://doi.org/10.2514/6.2016-3930
[research_rizzi_1984]: https://doi.org/10.2514/6.1984-2142
[research_rizzo_serpieri_2019]: https://doi.org/10.2514/6.2019-1133
[research_ro_barlow_1992]: https://doi.org/10.2514/6.1992-46
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_robb_vuppala_2023]: https://doi.org/10.2514/6.2023-2610
[research_roberts_1965]: https://doi.org/10.21236/ad0615928
[research_roberts_reed_2012]: https://doi.org/10.2514/6.2012-2668
[research_robins_beissner_1983]: https://ntrs.nasa.gov/citations/19830010442
[research_robinson]: https://doi.org/10.22215/etd/2018-13315
[research_robinson_2004]: https://doi.org/10.21236/ada425641
[research_robinson_batina_1990]: https://ntrs.nasa.gov/citations/19900042321
[research_robinson_robinson_1980]: https://doi.org/10.2514/6.1980-1884
[research_rochadacosta]: https://doi.org/10.22215/etd/2017-11781
[research_rockwell_1994]: https://doi.org/10.21236/ada278988
[research_rockwood_medina_2019]: https://doi.org/10.2514/6.2019-3335
[research_rodden_1989]: https://doi.org/10.2514/3.45842
[research_rodden_1989_b]: https://doi.org/10.2514/3.45825
[research_rodgers_1964]: https://doi.org/10.2514/6.1964-167
[research_rodgers_1965]: https://doi.org/10.2514/3.43615
[research_rodriguez_2007]: https://doi.org/10.2514/6.2007-1258
[research_rogalski_rzucidlo_2020]: https://doi.org/10.1108/aeat-05-2019-0099
[research_rogers_1952]: https://ntrs.nasa.gov/citations/19930087176
[research_rogers_1970]: https://doi.org/10.21236/ada367071
[research_rokhsaz_selberg_1989]: https://doi.org/10.2514/6.1989-13
[research_rokhsaz_selberg_1990]: https://doi.org/10.2514/3.25271
[research_romano_derosa_2017]: https://doi.org/10.1007/bf03404738
[research_romberg_2003]: https://doi.org/10.2514/6.iac-03-i.2.09
[research_rongqi_jianmei_2013]: https://doi.org/10.1108/00022661311294094
[research_rongrong_zhengyin_2018]: https://doi.org/10.1177/0954410018807810
[research_rontsch_taubert_2016]: https://doi.org/10.2514/6.2016-3169
[research_roos_1985]: https://doi.org/10.2514/6.1985-1609
[research_rose_jr_1952]: https://doi.org/10.21236/ad0014890
[research_rosen_rand_1985]: https://doi.org/10.2514/3.45084
[research_rosin_mattos_2004]: https://doi.org/10.2514/6.2004-5191
[research_ross_1984]: https://doi.org/10.2514/6.1984-2402
[research_ross_matarazzo_1982]: https://doi.org/10.4271/821467
[research_rouaix]: https://doi.org/10.70675/eb558d08zed33z4b4bzbce3ze3b29a83561d
[research_roy_mukherjee_2020]: https://doi.org/10.2514/6.2020-1765
[research_roysdon_khalid_2010]: https://doi.org/10.2514/6.2010-9167
[research_roysdon_khalid_2011]: https://doi.org/10.2514/6.2011-1563
[research_rozendaal_1986]: https://ntrs.nasa.gov/citations/19880019510
[research_rozendaal_1987]: https://ntrs.nasa.gov/citations/19900003232
[research_rozendaal_behbehani_1990]: https://ntrs.nasa.gov/citations/19910014826
[research_rudenko_ryzhkova_1968]: https://doi.org/10.1007/bf01022888
[research_rudnickcohen_hodson_2020]: https://doi.org/10.2514/6.2020-3112
[research_rudnickcohen_hodson_2022]: https://doi.org/10.2514/1.c036440
[research_rudolph_1998]: https://ntrs.nasa.gov/citations/19980021287
[research_ruhlin_prattbarlow_1981]: https://doi.org/10.2514/6.1981-654
[research_runckel_henderson_1952]: https://ntrs.nasa.gov/citations/20050041843
[research_runckel_hieser_1961]: https://ntrs.nasa.gov/citations/20040047108
[research_runckel_schmeer_1960]: https://ntrs.nasa.gov/citations/19980228396
[research_runyan_georgefalvy_1979]: https://doi.org/10.2514/6.1979-267
[research_runyan_navran_1984]: https://ntrs.nasa.gov/citations/19860005835
[research_runyan_steers_1980]: https://ntrs.nasa.gov/citations/19810042099
[research_rusovici_haughey_2017]: https://doi.org/10.2316/p.2017.848-057
[research_russell_1996]: https://doi.org/10.1016/b978-034063170-6/50008-6
[research_russell_1996_b]: https://doi.org/10.1016/b978-034063170-6/50011-6
[research_russo_tognaccini_2020]: https://doi.org/10.2514/6.2020-0447
[research_russo_tognaccini_2020_b]: https://doi.org/10.2514/1.j059080
[research_rutkowski_1977]: https://ntrs.nasa.gov/citations/19780005094
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_ruxandramihaela_samuel_2012]: https://doi.org/10.13111/2066-8201.2012.4.2.2
[research_rymarz_ramaprian_1995]: https://doi.org/10.2514/6.1995-2161
[research_s_gangamkote_2023]: https://doi.org/10.21203/rs.3.rs-3200268/v1
[research_sabri_elzaabalawy_2022]: https://doi.org/10.1007/s00707-021-03138-7
[research_sacchi_sneddon_2026]: https://doi.org/10.2514/6.2026-1445
[research_sachs_1978]: https://doi.org/10.2514/3.58390
[research_sachs_1980]: https://doi.org/10.2514/3.44685
[research_sachs_gruter_2021]: https://doi.org/10.3390/aerospace8080229
[research_sachs_gruter_2021_b]: https://doi.org/10.2514/6.2021-0641
[research_sachs_moelyadi_2006]: https://doi.org/10.1016/j.jtbi.2005.07.016
[research_sacks_nielsen_1963]: https://doi.org/10.21236/ad0406705
[research_sadoff_matteson_1954]: https://ntrs.nasa.gov/citations/19650075959
[research_saeed_graham_2015]: https://doi.org/10.2514/1.c032862
[research_saeed_mughal_2016]: https://doi.org/10.2514/6.2016-2065
[research_saelman_1964]: https://doi.org/10.2514/3.43599
[research_sager_1993]: https://ntrs.nasa.gov/citations/19940020025
[research_sahin_cakir_2018]: https://doi.org/10.1051/matecconf/201818804002
[research_sahin_cakir_2018_b]: https://doi.org/10.1051/matecconf/201823300006
[research_sahin_yaman_2018]: https://doi.org/10.3390/aerospace5040127
[research_sahin_yaman_2018_b]: https://doi.org/10.1051/matecconf/201818804001
[research_saitoh_hashidate_1995]: https://doi.org/10.2514/6.1995-3926
[research_saitoh_tamayama_2012]: https://doi.org/10.2478/s13531-012-0008-2
[research_sakakibara_nimura_2021]: https://doi.org/10.2514/6.2021-1854
[research_salahudden_2021]: https://doi.org/10.1016/j.ast.2021.106823
[research_salahudden_2024]: https://doi.org/10.1016/j.conengprac.2024.105872
[research_salahudden_2025]: https://doi.org/10.1177/09544100251315878
[research_salahudden_2025_2]: https://doi.org/10.1109/taes.2024.3485604
[research_salahudden_2026]: https://doi.org/10.1007/s42405-026-01168-w
[research_salahudden_das_2022]: https://doi.org/10.1109/taes.2022.3146114
[research_salahudden_dwivedi_2020]: https://doi.org/10.1177/0954410020964674
[research_salahudden_dwivedi_2021]: https://doi.org/10.2514/6.2021-0717
[research_salahudden_ghosh_2022]: https://doi.org/10.1177/09544100221089055
[research_salahudden_ghosh_2022_b]: https://doi.org/10.2514/6.2022-1388
[research_salahudden_giri_2020]: https://doi.org/10.1109/icuas48674.2020.9213975
[research_salahudden_kumar_2025]: https://doi.org/10.2514/6.2025-1053
[research_salahudden_sanwale_2023]: https://doi.org/10.2514/6.2023-4456
[research_salahudden_singh_2024]: https://doi.org/10.2514/6.2024-4654
[research_salari_roache_1990]: https://doi.org/10.2514/6.1990-581
[research_salemsaid_ragab_2008]: https://doi.org/10.2514/6.2008-4326
[research_samareh_chwalowski_2007]: https://ntrs.nasa.gov/citations/20070018296
[research_samikkannu_2011]: https://doi.org/10.5772/21628
[research_sammonds_1960]: https://ntrs.nasa.gov/citations/19980227305
[research_samputh_moey_2024]: https://doi.org/10.3846/aviation.2024.21495
[research_samuel_mukherjee_2016]: https://doi.org/10.2514/6.2016-0306
[research_samuels_1982]: https://doi.org/10.2514/3.57418
[research_san_fei_2012]: https://doi.org/10.1007/s12206-012-0922-5
[research_sanchez_escamilla_2019]: https://doi.org/10.2514/6.2019-2094
[research_sanders_1965]: https://doi.org/10.2514/3.43662
[research_sanders_eastep_2003]: https://doi.org/10.2514/2.3062
[research_sandhu_soltani_2018]: https://ntrs.nasa.gov/citations/20180005228
[research_sandoz_ahuja_2018]: https://doi.org/10.2514/6.2018-2070
[research_sang]: https://doi.org/10.18130/v3q79n
[research_sanghi_cesnik_2024]: https://doi.org/10.2514/1.c037470
[research_sankar_malone_1985]: https://doi.org/10.2514/6.1985-4061
[research_santos_marques_2026]: https://doi.org/10.2514/6.2026-1247
[research_santos_mattos_2009]: https://doi.org/10.2514/6.2009-3776
[research_santos_sousa_2018]: https://doi.org/10.1016/j.ast.2018.07.033
[research_saric_1996]: https://ntrs.nasa.gov/citations/19960021105
[research_saric_1997]: https://doi.org/10.21236/ada388392
[research_saric_2010]: https://doi.org/10.21236/ada564004
[research_saric_dagenhart_1990]: https://doi.org/10.1007/978-3-662-02643-4_23
[research_saric_west_2015]: https://doi.org/10.2514/6.2015-0539
[research_saric_west_2019]: https://doi.org/10.2514/1.j056897
[research_saric_yeates_1985]: https://doi.org/10.2514/6.1985-493
[research_sartor_timme_2016]: https://doi.org/10.1108/hff-07-2015-0283
[research_sato_2013]: https://doi.org/10.1109/acc.2013.6580911
[research_sato_2014]: https://doi.org/10.1109/cca.2014.6981347
[research_sato_2018]: https://doi.org/10.1109/tcst.2017.2692750
[research_sato_2022]: https://doi.org/10.1016/j.ifacol.2022.11.293
[research_saussie_saydy_2011]: https://doi.org/10.2514/1.52178
[research_savage_1959]: https://ntrs.nasa.gov/citations/19980228310
[research_sawyer_kennedy_1951]: https://ntrs.nasa.gov/citations/19930086544
[research_sawyer_trant_1950]: https://ntrs.nasa.gov/citations/20050028471
[research_sboevd_2024]: https://doi.org/10.53954/9785605099659_25
[research_scallion_1952]: https://ntrs.nasa.gov/citations/19930087098
[research_scanlan_1948]: https://doi.org/10.21236/ada955900
[research_schade_1948]: https://ntrs.nasa.gov/citations/19930085338
[research_schaeffler_telionis_1998]: https://doi.org/10.2514/6.1998-673
[research_schairer_1941]: https://doi.org/10.2514/8.10709
[research_scher_1947]: https://ntrs.nasa.gov/citations/20050019396
[research_scher_1947_b]: https://ntrs.nasa.gov/citations/20050028509
[research_scher_1951]: https://ntrs.nasa.gov/citations/19930083052
[research_scher_1977]: https://ntrs.nasa.gov/citations/19980227417
[research_scher_draper_1950]: https://ntrs.nasa.gov/citations/19930082805
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schewe_mai_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.07.005
[research_schiavetta_boelens_2006]: https://doi.org/10.2514/6.2006-3171
[research_schmeer_cassetti_1960]: https://ntrs.nasa.gov/citations/19980223967
[research_schmidt_1983]: https://doi.org/10.2514/6.1983-2074
[research_schmidt_1991]: https://doi.org/10.2514/6.1991-3316
[research_schmidt_2016]: https://doi.org/10.2514/1.c033539
[research_schmidt_2016_b]: https://doi.org/10.2514/6.2016-2099
[research_schmidt_duren_2002]: https://doi.org/10.2514/6.2002-4878
[research_schmidt_moore_1988]: https://ntrs.nasa.gov/citations/19890009039
[research_schmitt_destarac_1983]: https://doi.org/10.2514/6.1983-1804
[research_schneider_1956]: https://ntrs.nasa.gov/citations/19930089158
[research_schneider_1976]: https://doi.org/10.21236/ada025795
[research_schneiter_fischel_1948]: https://ntrs.nasa.gov/citations/19930085479
[research_schneiter_watson_1948]: https://ntrs.nasa.gov/citations/19930082263
[research_schorsch_nagel_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00007-1
[research_schuelein_2008]: https://doi.org/10.2514/6.2008-4208
[research_schuette_hummel_2022]: https://doi.org/10.2514/6.2022-3437
[research_schuette_hummel_2024]: https://doi.org/10.2514/6.2024-3505
[research_schuette_vormweg_2018]: https://doi.org/10.2514/6.2018-2841
[research_schulderfrei_1951]: https://ntrs.nasa.gov/citations/19930083056
[research_schuster_byrd_2003]: https://doi.org/10.2514/6.2003-593
[research_schutte_huber_2018]: https://doi.org/10.2514/1.c033700
[research_schutte_hummel_2025]: https://doi.org/10.2514/1.c038163
[research_schweikert_patel_2022]: https://doi.org/10.2514/6.2022-3355
[research_scudder_1933]: https://ntrs.nasa.gov/citations/19930081239
[research_scudder_1937]: https://ntrs.nasa.gov/citations/19930091634
[research_scudder_seidman_1935]: https://ntrs.nasa.gov/citations/19930091602
[research_seacord_campbell_1945]: https://ntrs.nasa.gov/citations/19930092552
[research_sears_1974]: https://doi.org/10.2514/3.60348
[research_sears_1980]: https://doi.org/10.2514/6.1980-3036
[research_sears_1990]: https://doi.org/10.2514/3.45918
[research_secanell_suleman_2005]: https://doi.org/10.2514/6.2005-1891
[research_sefcovic_smith_2010]: https://doi.org/10.2514/6.2010-92
[research_segui_gabor_2017]: https://doi.org/10.2316/p.2017.848-048
[research_seidler_huebner_2023]: https://doi.org/10.2514/6.2023-4397
[research_seidman_1942]: https://ntrs.nasa.gov/citations/19930092625
[research_seidman_mcavoy_1940]: https://ntrs.nasa.gov/citations/19930081616
[research_seigler_neal_2007]: https://doi.org/10.2514/1.21439
[research_seigler_neal_2009]: https://doi.org/10.2514/1.44108
[research_seitz_kruse_2011]: https://doi.org/10.2514/6.2011-3526
[research_selangovanetal_2019]: https://doi.org/10.24247/ijmperdjun201968
[research_selberg_1990]: https://ntrs.nasa.gov/citations/19900011649
[research_selberg_vitt_1993]: https://doi.org/10.4271/931383
[research_selim_gowree_2021]: https://doi.org/10.2514/1.j060052
[research_semionov_kosinov_2006]: https://doi.org/10.1007/1-4020-4159-4_50
[research_semionov_kosinov_2007]: https://doi.org/10.1134/s0869864307030031
[research_semionov_kosinov_2009]: https://doi.org/10.1007/978-90-481-3723-7_61
[research_semionov_kosinov_2011]: https://doi.org/10.1615/tsagiscij.v42.i1.10
[research_semionov_kosinov_2011_b]: https://doi.org/10.1088/1742-6596/318/3/032018
[research_semionov_kosinov_2013]: https://doi.org/10.1051/eucass/201305081
[research_semionov_yermolaev_2017]: https://doi.org/10.1063/1.5007544
[research_semionov_yermolaev_2018]: https://doi.org/10.1063/1.5065250
[research_semionov_yermolaev_2022]: https://doi.org/10.53954/9785604788967_171
[research_sengupta_dipankar_2005]: https://doi.org/10.1017/s0022112004003246
[research_seraj_2025]: https://doi.org/10.2514/1.c037899
[research_seraj_martins_2023]: https://doi.org/10.2514/6.2023-3472
[research_seraudie_perraud_2003]: https://doi.org/10.1016/j.ast.2003.04.001
[research_sereez_abramov_2024]: https://doi.org/10.20944/preprints202402.1051.v1
[research_serpieri_kotsonis_2015]: https://doi.org/10.2514/6.2015-2576
[research_serpieri_kotsonis_2016]: https://doi.org/10.2514/6.2016-3791
[research_serpieri_kotsonis_2016_b]: https://doi.org/10.2514/6.2016-3792
[research_setoguchi_kanazaki_2020]: https://doi.org/10.2514/6.2020-0534
[research_setyohariyadi_sutardi_2021]: https://doi.org/10.1088/1742-6596/2117/1/012013
[research_sforza_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00005-x
[research_shafer_1975]: https://ntrs.nasa.gov/citations/19760007049
[research_shah_2014]: https://ntrs.nasa.gov/citations/20150003355
[research_shah_ang_2025]: https://doi.org/10.2514/6.2025-3516
[research_shah_unnikrishnan_2003]: https://doi.org/10.2514/6.2003-5304
[research_shahjahan_ahuja_2026]: https://doi.org/10.2514/6.2026-4665
[research_shahjahan_enriquez_2026]: https://doi.org/10.2514/6.2026-0891
[research_shahriari_kollert_2018]: https://doi.org/10.1017/jfm.2018.195
[research_shahzad_hamdani_2012]: https://doi.org/10.1109/ibcast.2012.6177557
[research_shamshurin_1974]: https://doi.org/10.1007/bf01092671
[research_shankar_2013]: https://doi.org/10.2514/6.2013-4924
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shanks_gale_2018]: https://doi.org/10.1201/9781315136820-6
[research_shanmugam_2025]: https://doi.org/10.3390/drones9060435
[research_shanmugam_raja_2016]: https://doi.org/10.2514/6.2016-3414
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shao_liu_2022]: https://doi.org/10.1109/isas55863.2022.9757298
[research_shao_zhang_2025]: https://doi.org/10.1063/5.0291353
[research_shao_zhou_2017]: https://doi.org/10.23919/chicc.2017.8027856
[research_sharif_abbas_2022]: https://doi.org/10.47893/gret.2022.1084
[research_sharifi_2025]: https://doi.org/10.1016/j.compstruct.2025.118839
[research_sharma_rana_2025]: https://doi.org/10.2514/6.2025-106588
[research_shcherbakov_1966]: https://doi.org/10.1007/bf01013812
[research_shen_2026]: https://doi.org/10.1051/matecconf/202642404023
[research_shen_mo_1996]: https://doi.org/10.2514/6.1996-2163
[research_sherman_1937]: https://ntrs.nasa.gov/citations/19930092656
[research_sherrow_hassen_2026]: https://doi.org/10.2514/6.2026-0697
[research_sheta_2004]: https://doi.org/10.2514/1.9327
[research_shevell_1978]: https://doi.org/10.2514/3.58419
[research_shi_peng_2014]: https://doi.org/10.1109/ccdc.2014.6852394
[research_shi_peng_2015]: https://doi.org/10.2514/6.2015-3002
[research_shi_song_2012]: https://doi.org/10.1109/wcica.2012.6358104
[research_shi_wan_2015]: https://doi.org/10.1108/aeat-01-2013-0004
[research_shields_mohseni_2012]: https://doi.org/10.2514/6.2012-3117
[research_shimomura]: https://doi.org/10.1109/acc.2003.1242455
[research_shipul_kosinov_2024]: https://doi.org/10.53954/9785604990148_158
[research_shitrit_2021]: https://doi.org/10.1017/aer.2021.78
[research_shivaji_basavaraju_2025]: https://doi.org/10.1063/5.0265477
[research_shmul_erenthal_2018]: https://doi.org/10.1201/9781315136820-10
[research_shomber_gertsen_1967]: https://doi.org/10.2514/3.43851
[research_shtin_savelyev_2022]: https://doi.org/10.53954/9785604788974_154
[research_shue_agarwal_1998]: https://doi.org/10.2514/6.1998-4299
[research_shue_sawan_1996]: https://doi.org/10.2514/6.1996-3779
[research_shumsky_2006]: https://doi.org/10.1109/ifost.2006.312262
[research_si_2025]: https://doi.org/10.1016/j.ast.2025.110120
[research_si_wu_2024]: https://doi.org/10.3390/drones8090474
[research_sibert_1943]: https://doi.org/10.2514/8.10986
[research_sibilski_wroblewski_2012]: https://doi.org/10.2514/6.2012-4799
[research_sidoryuk_khrabrov_2019]: https://doi.org/10.2514/1.c034936
[research_sihite_salagame_2023]: https://doi.org/10.1109/cdc49753.2023.10383886
[research_silsby_kennedy_1947]: https://ntrs.nasa.gov/citations/20050029399
[research_silsby_morris_1950]: https://ntrs.nasa.gov/citations/19930086179
[research_silsby_morris_1953]: https://ntrs.nasa.gov/citations/19930087375
[research_silva]: https://doi.org/10.14393/ufu.te.2022.345
[research_silva_b]: https://doi.org/10.11606/003273318
[research_silva_guimaraes_2023]: https://doi.org/10.2514/6.2023-1677
[research_sim_curry_1978]: https://ntrs.nasa.gov/citations/19790001897
[research_sim_curry_1984]: https://ntrs.nasa.gov/citations/19870001438
[research_sim_curry_1985]: https://ntrs.nasa.gov/citations/19870009137
[research_simmons_freund_2005]: https://doi.org/10.2514/6.2005-1017
[research_simpson_jacob_2005]: https://doi.org/10.2514/6.2005-5133
[research_sims_carter_1981]: https://ntrs.nasa.gov/citations/19820030858
[research_simulation_requirements_2017]: https://doi.org/10.2514/5.9781624104435.0171.0230
[research_singh_2024]: https://doi.org/10.32920/25822486.v1
[research_singh_chowdhury_2021]: https://doi.org/10.47531/mantech/ecc.2021.42
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singha_2025]: https://doi.org/10.52843/cassyni.rwpkvl
[research_singha_murugan_2022]: https://doi.org/10.2514/6.2022-1124
[research_singha_murugan_2023]: https://doi.org/10.2514/6.2023-3753
[research_singha_murugan_2026]: https://doi.org/10.1007/s00707-025-04623-z
[research_singha_murugan_2026_b]: https://doi.org/10.1016/j.ast.2026.112110
[research_sinha_yuan_2026]: https://doi.org/10.2514/6.2026-4586
[research_sinkovec_loshek_2015]: https://doi.org/10.2514/6.2015-1888
[research_siouris_qin_2007]: https://doi.org/10.1243/09544100jaero93
[research_sivanandi_gupta_2022]: https://doi.org/10.21203/rs.3.rs-2263166/v1
[research_skillen_crossley_2005]: https://doi.org/10.2514/6.2005-1960
[research_skillen_crossley_2007]: https://ntrs.nasa.gov/citations/20070017321
[research_skillen_crossley_2008]: https://ntrs.nasa.gov/citations/20080009777
[research_skillen_crossley_2008_b]: https://ntrs.nasa.gov/citations/20080009778
[research_skomorokhov_nikolay_2014]: https://doi.org/10.2514/6.2014-2994
[research_slater_1985]: https://doi.org/10.2514/6.1985-1965
[research_sleesongsom_bureerat_2011]: https://doi.org/10.4028/www.scientific.net/amm.52-54.308
[research_sleesongsom_bureerat_2013]: https://doi.org/10.1007/s00158-013-0944-3
[research_sliwa_1979]: https://doi.org/10.2514/6.1979-1802
[research_smith_1959]: https://ntrs.nasa.gov/citations/19630003098
[research_smith_1975_b]: https://ntrs.nasa.gov/citations/19760004017
[research_smith_1976]: https://ntrs.nasa.gov/citations/19760015098
[research_smith_1977]: https://doi.org/10.21236/ada069198
[research_smith_1990]: https://doi.org/10.2514/3.48881
[research_smith_butt_2007]: https://doi.org/10.2514/6.2007-4616
[research_smith_cliff_1987]: https://doi.org/10.2514/6.1987-2930
[research_smith_hammer_1971]: https://doi.org/10.21236/ad0730571
[research_smith_jones_1975]: https://ntrs.nasa.gov/citations/19760012054
[research_smith_kennelly_1999]: https://ntrs.nasa.gov/citations/20020023962
[research_smith_lebacqz_1973]: https://doi.org/10.21236/ad0754840
[research_smith_lock_1992]: https://ntrs.nasa.gov/citations/19920012951
[research_smith_lowenberg_2014]: https://doi.org/10.2514/1.c032262
[research_smith_nelson_1988]: https://doi.org/10.2514/6.1988-2556
[research_smith_schneider_1996]: https://doi.org/10.2514/3.47051
[research_smith_srokowski_1983]: https://doi.org/10.2514/6.1983-1832
[research_smith_zell_1990]: https://doi.org/10.2514/3.45924
[research_sneed_smith_2007]: https://doi.org/10.2514/6.2007-1702
[research_snyder_1947]: https://ntrs.nasa.gov/citations/20050019393
[research_snyder_1947_b]: https://ntrs.nasa.gov/citations/20050019397
[research_snyder_1948]: https://ntrs.nasa.gov/citations/20050019414
[research_snyder_sanders_2009]: https://doi.org/10.2514/1.34685
[research_snyder_weisshaar_2013]: https://doi.org/10.2514/1.c031978
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_sobieczky_hefer_1987]: https://doi.org/10.2514/6.1987-2485
[research_sofla_meguid_2010]: https://doi.org/10.1016/j.matdes.2009.09.011
[research_sofla_meguid_2010_b]: https://doi.org/10.1115/imece2010-38851
[research_sohail_muhammad_2011]: https://doi.org/10.1063/1.3651865
[research_sohn_chung_2006]: https://doi.org/10.2514/6.2006-3498
[research_soistmann_1992]: https://doi.org/10.2514/6.1992-2112
[research_sol_vos_2016]: https://doi.org/10.2514/6.2016-3285
[research_solies_1995]: https://doi.org/10.2514/6.1995-3912
[research_soneda_tsushima_2022]: https://doi.org/10.2514/6.2022-0242
[research_soneda_tsushima_2023]: https://doi.org/10.2514/6.2023-2407
[research_soneda_tsushima_2023_b]: https://doi.org/10.1115/ssdm2023-106523
[research_soneda_yokozeki_2020]: https://doi.org/10.2514/6.2020-0450
[research_soneda_yokozeki_2021]: https://doi.org/10.2514/6.2021-0953
[research_sonneveldt_chu_2011]: https://doi.org/10.5772/13839
[research_soontornpasatch_2025]: https://doi.org/10.55003/eth.420105
[research_sorbilli_dibianchi_2018]: https://doi.org/10.2514/6.2018-1653
[research_sorenson_1974]: https://doi.org/10.2514/6.1974-269
[research_sotoudeh_ferman_2019]: https://doi.org/10.2514/6.2019-0762
[research_sotoudeh_hodges_2010]: https://doi.org/10.2514/1.46974
[research_sotoudeh_hosking_2018]: https://doi.org/10.2514/6.2018-1203
[research_souahi_1983]: https://doi.org/10.1017/s0001924000019771
[research_sousa_silva_2004]: https://doi.org/10.1016/j.compstruc.2004.03.051
[research_space_environment]: https://doi.org/10.3403/30237419
[research_spacht_1980]: https://doi.org/10.2514/6.1980-1885
[research_spain_soistmann_1990]: https://ntrs.nasa.gov/citations/19910029821
[research_spearman_1948]: https://ntrs.nasa.gov/citations/19930085498
[research_spearman_1980]: https://doi.org/10.2514/6.1980-1623
[research_spearman_2012]: https://doi.org/10.2514/6.2012-956
[research_spearman_comisarow_1948]: https://ntrs.nasa.gov/citations/19930085510
[research_spearman_driver_1959]: https://ntrs.nasa.gov/citations/19980228222
[research_speer_zhong_2004]: https://doi.org/10.2514/6.2004-252
[research_spencer_1960]: https://ntrs.nasa.gov/citations/19660024029
[research_spencer_1961]: https://ntrs.nasa.gov/citations/19980228059
[research_spencer_1981]: https://ntrs.nasa.gov/citations/19980235628
[research_spens_bons_2022]: https://doi.org/10.2514/6.2022-3466
[research_spens_mcfadden_2023]: https://doi.org/10.2514/6.2023-1238
[research_spreemann_1951]: https://ntrs.nasa.gov/citations/19930086543
[research_spreiter_stahara_1970]: https://doi.org/10.2514/6.1970-798
[research_springer_1996]: https://doi.org/10.2514/6.1996-196
[research_squire_1975]: https://doi.org/10.1017/s0001925900007149
[research_squires_2002]: https://doi.org/10.21236/ada410100
[research_srichitturi_2026]: https://doi.org/10.21203/rs.3.rs-11247822/v1
[research_srigrarom_kurosaka_2000]: https://doi.org/10.2514/2.939
[research_srinathkumar_2011]: https://doi.org/10.1049/pbce074e
[research_srinivas_potti_2014]: https://doi.org/10.4028/www.scientific.net/amm.592-594.1020
[research_srivastava_patel_2025]: https://doi.org/10.56025/ijaresm.2025.1305251294
[research_srokowski_orszag_1977]: https://doi.org/10.2514/6.1977-1222
[research_stability_characteristics_2014]: https://doi.org/10.2514/5.9781624102547.0665.0680
[research_stability_control_2024]: https://doi.org/10.2514/5.9781624107290.0619.0672
[research_stacey_2024]: https://doi.org/10.2514/6.2024-1126
[research_stacey_thomas_2019]: https://doi.org/10.1115/smasis2019-5567
[research_stacey_thomas_2022]: https://doi.org/10.2514/6.2022-1986
[research_stall_characteristics_2003]: https://doi.org/10.2514/5.9781600861840.0365.0382
[research_stall_speed_2003]: https://doi.org/10.2514/5.9781600861840.0039.0052
[research_stallingsjr_lamb_1981]: https://doi.org/10.2514/6.1981-8
[research_stanbrook_1954]: https://doi.org/10.1108/eb032455
[research_standard_atmosphere_1927]: https://doi.org/10.6028/nbs.mp.78
[research_standard_atmosphere_1927_b]: https://doi.org/10.6028/nbs.mp.82
[research_standard_atmosphere_2005]: https://doi.org/10.1017/cbo9780511807138.014
[research_standard_atmosphere_2023]: https://doi.org/10.1017/9781009043076.015
[research_standard_atmosphere_2024]: https://doi.org/10.2514/5.9781624107290.1007.1012
[research_stanford_ifju_2008]: https://doi.org/10.2514/6.2008-5989
[research_stanford_jacobson_2023]: https://doi.org/10.2514/6.2023-0589
[research_stark_1985]: https://doi.org/10.2514/3.56760
[research_starn]: https://doi.org/10.33915/etd.1466
[research_starossek_2021]: https://doi.org/10.1201/9780429279119-440
[research_static_flight_2026]: https://doi.org/10.1017/9781009399913.011
[research_static_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0223.0234
[research_static_longitudinal_2003_b]: https://doi.org/10.2514/5.9781600861840.0209.0221
[research_static_stability]: https://doi.org/10.1007/978-3-540-46573-7_9
[research_static_stability_2010]: https://doi.org/10.2514/5.9781600867538.0575.0600
[research_stebbins_loth_2019]: https://doi.org/10.2514/6.2019-0328
[research_stebbins_loth_2022]: https://doi.org/10.2514/6.2022-1170
[research_stebbins_loth_2023]: https://doi.org/10.1007/978-3-031-33845-8_6
[research_steer_2003]: https://doi.org/10.2514/6.2003-5308
[research_steers_1981]: https://ntrs.nasa.gov/citations/19810010484
[research_stegmuller_haybock_2026]: https://doi.org/10.2514/1.c038577
[research_stegmuller_katzenmeier_2022]: https://doi.org/10.1007/s13272-022-00593-3
[research_steimle_karhoff_2012]: https://doi.org/10.2514/1.j051187
[research_steimle_schroder_2008]: https://doi.org/10.2514/6.2008-6908
[research_steimle_schroder_2010]: https://doi.org/10.1007/978-3-642-04088-7_13
[research_stenfelt_ringertz_2013]: https://doi.org/10.2514/1.c031868
[research_stepanyan_nguyen]: https://ntrs.nasa.gov/citations/20240006609
[research_stephen_1995]: https://doi.org/10.2514/3.46826
[research_stephen_sopirak_1994]: https://doi.org/10.2514/6.1994-1885
[research_stephenson_1956]: https://ntrs.nasa.gov/citations/19930090107
[research_stevens_1955]: https://ntrs.nasa.gov/citations/20050029377
[research_stewart_paulsonjr_1984]: https://doi.org/10.2514/6.1984-2396
[research_stewartson_1981]: https://doi.org/10.1115/1.3240769
[research_stifel_1979]: https://doi.org/10.21236/ada085873
[research_stock_2005]: https://doi.org/10.2514/1.12487
[research_stojakovic]: https://doi.org/10.2298/bg20120711stojakovic
[research_stone_1947]: https://ntrs.nasa.gov/citations/19930081964
[research_stone_1948]: https://ntrs.nasa.gov/citations/19930082194
[research_stone_berman_1946]: https://ntrs.nasa.gov/citations/19930093799
[research_stone_daughtridge_1948]: https://ntrs.nasa.gov/citations/20050019380
[research_stough_1979]: https://ntrs.nasa.gov/citations/19790063863
[research_stough_1987]: https://ntrs.nasa.gov/citations/19870007382
[research_stough_1990]: https://ntrs.nasa.gov/citations/19900046871
[research_stough_1991]: https://ntrs.nasa.gov/citations/19910069118
[research_stough_1993]: https://ntrs.nasa.gov/citations/19940016083
[research_stough_dicarlo_1984]: https://ntrs.nasa.gov/citations/19840056491
[research_stough_dicarlo_1985]: https://ntrs.nasa.gov/citations/19850016937
[research_stough_jordan_1985]: https://ntrs.nasa.gov/citations/19860053587
[research_strayer_manoharan_2025]: https://doi.org/10.1115/imece2025-166753
[research_streitenberger_feldwisch_2025]: https://doi.org/10.2514/6.2025-1663
[research_strickland_tadios_1990]: https://doi.org/10.2172/6839285
[research_stringfield_1984]: https://doi.org/10.21236/ada139933
[research_striz_1991]: https://doi.org/10.21236/ada248487
[research_study_on_2022]: https://doi.org/10.47939/et.v3i2.274
[research_sturm_achleitner_2019]: https://doi.org/10.2514/6.2019-2817
[research_su_2026]: https://doi.org/10.1088/1742-6596/3304/1/012044
[research_su_swei_2016]: https://doi.org/10.2514/1.c033490
[research_su_wang_2018]: https://doi.org/10.1145/3208833.3208850
[research_suardi_pinelli_2020]: https://doi.org/10.1007/978-3-030-42822-8_42
[research_suarez_kramer_1992]: https://doi.org/10.2514/6.1992-2716
[research_suarez_smith_1993]: https://doi.org/10.2514/6.1993-187
[research_subaschandar_prabhu_2002]: https://doi.org/10.2514/2.2926
[research_subramanian_2026]: https://doi.org/10.31224/7158
[research_sudhi_radespiel_2021]: https://doi.org/10.2514/6.2021-2606
[research_sugimoto_1992]: https://doi.org/10.2514/3.46234
[research_sugiura_yoshida_2001]: https://doi.org/10.2514/6.2001-2782
[research_sui_2022]: https://doi.org/10.22541/au.165416416.64807284/v1
[research_suleman_2007]: https://doi.org/10.21236/ada525877
[research_summers_1953]: https://doi.org/10.2514/8.2886
[research_sun_2026]: https://doi.org/10.1016/j.ast.2025.110841
[research_sun_li_2022]: https://doi.org/10.3390/machines10100930
[research_sun_zhou_2024]: https://doi.org/10.3390/aerospace11121045
[research_sundaram_viswanath_1999]: https://doi.org/10.2514/2.7533
[research_sutherland_1893]: https://doi.org/10.1080/14786449308620508
[research_sutton_1959]: https://ntrs.nasa.gov/citations/19980230678
[research_suzuki_yonezawa_1993]: https://doi.org/10.2514/3.48276
[research_svoboda_1999]: https://doi.org/10.1016/s1369-8869(99)00019-1
[research_svoboda_hengstermovric_2023]: https://doi.org/10.1016/j.ast.2023.108415
[research_svoboda_hromcik_2018]: https://doi.org/10.1109/med.2018.8442815
[research_svoboda_rozehnal_2015]: https://doi.org/10.1109/miltechs.2015.7153724
[research_swaim_1961]: https://doi.org/10.2514/8.9241
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swihart_goodman_1965]: https://doi.org/10.1108/eb034082
[research_swihart_goodmanson_1964]: https://doi.org/10.4271/640249
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/6.2022-2557
[research_syed_moshtaghzadeh_2022_b]: https://doi.org/10.2514/1.j061574
[research_syverud_farokhi_1993]: https://doi.org/10.2514/6.1993-3446
[research_szema_shankar_1984]: https://doi.org/10.2514/6.1984-427
[research_szilder_lozowski_2018]: https://doi.org/10.2514/1.c034879
[research_szmelter_1999]: https://doi.org/10.2514/6.1999-550
[research_szodruch_1991]: https://doi.org/10.2514/6.1991-685
[research_szodruch_hilbig_1988]: https://doi.org/10.1016/0376-0421(88)90003-6
[research_szymanski_ghazi_2025]: https://doi.org/10.2514/6.2025-2228
[research_tagai_nakakita_2016]: https://doi.org/10.2514/6.2016-3355
[research_tai_1991]: https://doi.org/10.2514/3.46104
[research_tai_wang_2023]: https://doi.org/10.3390/aerospace10040350
[research_taira_rowley_2010]: https://doi.org/10.2514/6.2010-357
[research_taisulahn_hyoungjinkim]: https://doi.org/10.1109/icsmc.1999.812449
[research_takahashi_barchfeld_2016]: https://doi.org/10.2514/6.2016-2038
[research_takahashi_boccieri_2019]: https://doi.org/10.2514/6.2019-0813
[research_takahashi_donovan_2011]: https://doi.org/10.2514/6.2011-639
[research_takahashi_dulin_2014]: https://doi.org/10.2514/6.2014-3172
[research_takanashi_1984]: https://doi.org/10.2514/6.1984-2155
[research_takarics_mocsanyi_2020]: https://doi.org/10.1109/gpmc50267.2020.9333823
[research_takeda_1970]: https://doi.org/10.5100/jje.6.137
[research_tal_nguyen_2015]: https://doi.org/10.2514/6.2015-2722
[research_tamayo]: https://doi.org/10.22215/etd/2023-15474
[research_tamura_yumitori_2024]: https://doi.org/10.2514/6.2024-2446
[research_tan]: https://doi.org/10.32657/10356/41778
[research_tan_wang_2017]: https://doi.org/10.2514/6.2017-3960
[research_tancredi_corraro_2012]: https://doi.org/10.5772/30845
[research_tandale_rong_2004]: https://doi.org/10.2514/6.2004-5358
[research_tang_che_2023]: https://doi.org/10.1088/1674-1056/aca201
[research_tang_dowell_2008]: https://doi.org/10.2514/1.32754
[research_tang_liu_2007]: https://doi.org/10.2514/1.21194
[research_tang_shi_2024]: https://doi.org/10.1371/journal.pone.0299982
[research_tao_sun_2019]: https://doi.org/10.1016/j.ast.2019.06.041
[research_tapolcai_omran_2012]: https://doi.org/10.2514/6.2012-4401
[research_tarabi_ghasemloo_2015]: https://doi.org/10.1007/s40430-015-0405-6
[research_tarabi_ghasemloo_2016]: https://doi.org/10.24200/sci.2016.3978
[research_tarnowski_2017]: https://doi.org/10.1108/aeat-11-2016-0208
[research_tasci_ozdemir_2025]: https://doi.org/10.3390/sym17091516
[research_taufik_qasem_2025]: https://doi.org/10.1016/j.trpro.2025.03.120
[research_tavoularis_1999]: https://doi.org/10.2514/2.2526
[research_taylor_1952]: https://doi.org/10.1108/eb032201
[research_taylor_1953]: https://doi.org/10.1017/s0001924000121918
[research_taylor_1959]: https://ntrs.nasa.gov/citations/19980235623
[research_taylor_gursul_2004]: https://doi.org/10.2514/6.2004-1066
[research_taylor_gursul_2004_b]: https://doi.org/10.2514/1.5391
[research_taylor_hunsaker_2023]: https://doi.org/10.2514/6.2023-0038
[research_taylor_jackson_1982]: https://doi.org/10.2514/6.1982-231
[research_taylor_miller_1982]: https://ntrs.nasa.gov/citations/19820036251
[research_taylor_peake_1997]: https://doi.org/10.2514/6.1997-1777
[research_tchatchuengkammegne_botez_2016]: https://doi.org/10.2514/6.2016-3390
[research_teel_1999]: https://doi.org/10.21236/ada367415
[research_teel_1999_b]: https://doi.org/10.21236/ada367012
[research_telionis_1990]: https://doi.org/10.21236/ada231946
[research_telionis_1995]: https://doi.org/10.21236/ada299820
[research_telionis_2001]: https://doi.org/10.21236/ada398139
[research_telionis_vlachos_2003]: https://doi.org/10.21236/ada419486
[research_temgouadongmo_kwatny]: https://doi.org/10.17918/etd-3252
[research_tempelmann_hanifi_2012]: https://doi.org/10.1017/jfm.2012.152
[research_tempelmann_schrader_2011]: https://doi.org/10.2514/6.2011-3294
[research_tempelmann_schrader_2012]: https://doi.org/10.1017/jfm.2012.405
[research_tempelmeyer_osborne_1954]: https://ntrs.nasa.gov/citations/20050030054
[research_teofilatto_2001]: https://doi.org/10.1016/s1369-8869(00)00025-2
[research_teper_stapleford_1965]: https://doi.org/10.2514/6.1965-1237
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_test_techniques_2021]: https://doi.org/10.1016/c2018-0-00829-4
[research_tewes_taubert_2015]: https://doi.org/10.2514/6.2015-0783
[research_the_effects_1988]: https://doi.org/10.2514/6.1988-2514
[research_the_effects_1989]: https://doi.org/10.2514/6.1989-836
[research_the_flight_2021]: https://doi.org/10.1002/9781118949818.ch2
[research_the_international_2017]: https://doi.org/10.1016/b978-0-08-100194-3.00017-1
[research_the_international_2026]: https://doi.org/10.1016/b978-0-32-399544-3.00016-5
[research_the_mission_1986]: https://doi.org/10.1108/eb036213
[research_the_stability_1979]: https://doi.org/10.2514/6.1979-1495
[research_the_stability_1997]: https://doi.org/10.1016/s0301-9322(97)80092-4
[research_the_standard_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50033-6
[research_the_standard_1976]: https://doi.org/10.1016/b978-0-08-020414-7.50016-2
[research_the_sweep_angle_2018]: https://doi.org/10.18698/2308-6033-2018-2-1735
[research_the_swept_2021]: https://doi.org/10.5040/9798216408659.ch-019
[research_the_tapered_1937]: https://doi.org/10.1108/eb030156
[research_the_wing_2013]: https://doi.org/10.1002/9781118568101.ch11
[research_thelander_1965]: https://doi.org/10.21236/ad0617354
[research_theodorsen_1935]: https://ntrs.nasa.gov/citations/19800006788
[research_theofilis_1998]: https://doi.org/10.1017/s0022112097007660
[research_theofilis_dallmann_1997]: https://doi.org/10.1007/978-3-322-86573-1_45
[research_theofilis_duck_1990]: https://doi.org/10.1007/978-3-642-84103-3_35
[research_thomas_mughal_2016]: https://doi.org/10.2514/1.j054755
[research_thomas_mughal_2017]: https://doi.org/10.1063/1.4977092
[research_thomas_wolhart_1957]: https://ntrs.nasa.gov/citations/19930085077
[research_thompson_1965]: https://doi.org/10.2514/3.55147
[research_thornton_1993]: https://ntrs.nasa.gov/citations/19940019822
[research_three_dimensional_boundary_layer_1994]: https://doi.org/10.2514/6.1994-2375
[research_three_dimensional_wing_2014]: https://doi.org/10.1002/9781118534748.ch9
[research_thrust_induced_effects_1994]: https://doi.org/10.2514/6.1994-1856
[research_thurber_1965]: https://doi.org/10.1002/cpa.3160180410
[research_thurston_1934]: https://doi.org/10.1017/s0368393100112258
[research_tian_huang_2025]: https://doi.org/10.1007/978-981-96-1464-6_51
[research_tian_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000652
[research_tian_zhang_2024]: https://doi.org/10.2139/ssrn.4733419
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_ting_nguyen_2014]: https://doi.org/10.2514/6.2014-0837
[research_tiniakov_2026]: https://doi.org/10.3390/aerospace13060547
[research_tischler_2018]: https://doi.org/10.1201/9781315136820-2
[research_tischler_2018_b]: https://doi.org/10.1201/9781315136820
[research_tischler_barlow_1979]: https://ntrs.nasa.gov/citations/19790061294
[research_tischler_barlow_1980]: https://ntrs.nasa.gov/citations/19800034181
[research_tischler_barlow_1980_b]: https://doi.org/10.2514/6.1980-1565
[research_tischler_barlow_1981]: https://doi.org/10.2514/3.57487
[research_tischler_barlow_1982]: https://doi.org/10.2514/3.57376
[research_tjatra_kapania_1992]: https://doi.org/10.1016/0956-0521(92)90100-w
[research_todorov_2015]: https://doi.org/10.1109/miltechs.2015.7153648
[research_tokugawa_yoshida_2006]: https://doi.org/10.2514/6.2006-3165
[research_tolkachev_baranov_2024]: https://doi.org/10.53954/9785604990131_159
[research_tolkachev_kiselev_2022]: https://doi.org/10.53954/9785604788967_193
[research_toll_1962]: https://ntrs.nasa.gov/citations/19700023955
[research_toll_queijo_1948]: https://ntrs.nasa.gov/citations/19930082233
[research_tomczyk_2001]: https://doi.org/10.2514/6.2001-4264
[research_tomczyk_2002]: https://doi.org/10.1108/00022660210448456
[research_tomczyk_2008]: https://doi.org/10.2514/6.2008-6352
[research_tomczyk_2008_b]: https://doi.org/10.1108/00022660810873683
[research_tomek_ullah_2020]: https://doi.org/10.2514/6.2020-1980
[research_tong_ji_2013]: https://doi.org/10.1109/icca.2013.6564901
[research_tong_ji_2014]: https://doi.org/10.1017/s000192400000943x
[research_torenbeek_1972]: https://doi.org/10.1108/eb034867
[research_torenbeek_1976]: https://doi.org/10.1007/978-94-009-9580-2_7
[research_torenbeek_1982]: https://doi.org/10.1007/978-94-017-3202-4_7
[research_tormalm_leroy_2018]: https://doi.org/10.2514/1.c033820
[research_torrigiani_berci_2021]: https://doi.org/10.2514/6.2021-1911
[research_tosti_1947]: https://ntrs.nasa.gov/citations/19930082106
[research_touzani_1987]: https://doi.org/10.1007/bf00948294
[research_townsend_stanford_2018]: https://doi.org/10.2514/6.2018-3878
[research_toyoda_kwak_2015]: https://doi.org/10.1016/j.proeng.2015.06.050
[research_transfer_of_2010]: https://doi.org/10.2514/5.9781600867552.0615.0689
[research_transonic_aerodynamics_1982]: https://doi.org/10.2514/4.865558
[research_transonic_aerodynamics_history_1982]: https://doi.org/10.2514/5.9781600865558.0003.0079
[research_transonic_computational_1982]: https://doi.org/10.2514/5.9781600865558.0451.0465
[research_transonic_design_1982]: https://doi.org/10.2514/5.9781600865558.0377.0402
[research_transonic_flight_1994]: https://doi.org/10.2514/6.1994-2142
[research_transonic_wing_2015]: https://doi.org/10.1142/9781783266296_0011
[research_traub_1994]: https://doi.org/10.2514/3.46626
[research_traub_1995]: https://doi.org/10.2514/3.46856
[research_traub_1997]: https://doi.org/10.2514/2.2193
[research_traub_1997_b]: https://doi.org/10.1017/s0001924000066756
[research_traub_1997_c]: https://doi.org/10.2514/2.2177
[research_traub_2000]: https://doi.org/10.2514/2.2594
[research_traub_2009]: https://doi.org/10.2514/1.43952
[research_traub_2019]: https://doi.org/10.2514/1.c035600
[research_traub_2021]: https://doi.org/10.2514/1.c036445
[research_traub_2023]: https://doi.org/10.3390/aerospace10070597
[research_traub_campbell_2019]: https://doi.org/10.2514/1.c035183
[research_traub_chandrashekar_2016]: https://doi.org/10.1016/j.ast.2016.05.015
[research_traub_galls_1999]: https://doi.org/10.2514/2.2549
[research_travassos_gupta_1980]: https://ntrs.nasa.gov/citations/19800061748
[research_trenka_white_1963]: https://doi.org/10.21236/ad0408668
[research_trim_drag_2010]: https://doi.org/10.2514/5.9781600867538.0601.0612
[research_triplett_1980]: https://doi.org/10.2514/6.1980-794
[research_triplett_kappus_1973]: https://doi.org/10.2514/6.1973-194
[research_trussa_whitfield_2021]: https://doi.org/10.2514/6.2021-2536
[research_trussa_whitfield_2022]: https://doi.org/10.2514/6.2022-3297
[research_trussa_whitfield_2026]: https://doi.org/10.2514/1.c038565
[research_tsao_vargas_2009]: https://doi.org/10.2514/6.2009-4125
[research_tseng_1990]: https://doi.org/10.1007/978-3-642-84238-2_4
[research_tsushima_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_tsushima_arizono_2019]: https://doi.org/10.1299/transjsme.18-00506
[research_tsushima_arizono_2020]: https://doi.org/10.2514/6.2020-0215
[research_tsushima_tamayama_2020]: https://doi.org/10.2514/6.2020-2189
[research_tsushima_yokozeki_2018]: https://doi.org/10.12783/asc33/26174
[research_tu_1992]: https://doi.org/10.2514/6.1992-4632
[research_tu_1992_b]: https://doi.org/10.2514/6.1992-2602
[research_tucker_saric_2014]: https://doi.org/10.2514/6.2014-1117
[research_tufts_reed_2013]: https://doi.org/10.2514/6.2013-2411
[research_tufts_reed_2014]: https://doi.org/10.2514/1.c032490
[research_tufts_reed_2015]: https://doi.org/10.2514/6.2015-2775
[research_tufts_suffixjrsuffix_2014]: https://doi.org/10.1504/ijesms.2014.063123
[research_tumlinson_holcomb_1981]: https://doi.org/10.2514/6.1981-1667
[research_tupy_zelinka_2008]: https://doi.org/10.1109/dexa.2008.98
[research_turbeville_schneider_2018]: https://doi.org/10.2514/6.2018-3070
[research_turner_1950]: https://ntrs.nasa.gov/citations/19930082849
[research_turner_1981]: https://doi.org/10.2514/6.1981-604
[research_turns_kraige]: https://doi.org/10.1017/cbo9780511813696.014
[research_tursi_2003]: https://doi.org/10.2514/6.2003-3787
[research_tzong_sikes_1992]: https://doi.org/10.2514/6.1992-1002
[research_udin_anderson_1992]: https://doi.org/10.2514/3.46232
[research_ueno_matsuno_1998]: https://doi.org/10.2514/6.1998-2520
[research_ukolov_gamboa_2026]: https://doi.org/10.2514/1.c038506
[research_ullah_devi_1973]: https://doi.org/10.1103/physrevc.8.1167
[research_ullah_fabijanic_2021]: https://doi.org/10.2514/6.2021-1733
[research_ullah_fabijanic_2022]: https://doi.org/10.2514/6.2022-3392
[research_ullah_tomek_2021]: https://doi.org/10.3390/fluids6120457
[research_unangst_1959]: https://ntrs.nasa.gov/citations/19980236841
[research_unger_coen_1993]: https://doi.org/10.4271/932632
[research_unsteady_aerodynamics_2006]: https://doi.org/10.2514/5.9781600862373.0447.0528
[research_unsteady_transonic_1989]: https://doi.org/10.2514/4.865947
[research_uribequintero_takahashi_2024]: https://doi.org/10.2514/6.2024-4048
[research_us_standard_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00019-x
[research_use_of_2022]: https://doi.org/10.1002/9781119988281.ch1
[research_ustinov_2001]: https://doi.org/10.1023/a:1019240102926
[research_ustinov_2013]: https://doi.org/10.1615/tsagiscij.2013007932
[research_ustinov_2017]: https://doi.org/10.1134/s0015462817010070
[research_ustinov_2018]: https://doi.org/10.1134/s001546281806023x
[research_ustinov_2018_b]: https://doi.org/10.31857/s056852810002299-9
[research_ustinov_2021]: https://doi.org/10.1007/978-3-030-67902-6_5
[research_utaka_2004]: https://doi.org/10.2514/6.2004-1271
[research_utsch_rockwell_1990]: https://doi.org/10.2514/3.25324
[research_uzun_2025]: https://doi.org/10.30518/jav.1583881
[research_uzun_bilgic_2023]: https://doi.org/10.1017/aer.2023.73
[research_uzun_oktay_2023]: https://doi.org/10.1108/aeat-09-2022-0259
[research_valasek_kirkpatrick_2012]: https://doi.org/10.1002/9781119964032.ch4
[research_valasek_lampton_2009]: https://doi.org/10.2514/6.2009-1827
[research_vale_albuquerque_2025]: https://doi.org/10.7862/tiam.2025.4.2
[research_vale_lau_2013]: https://doi.org/10.2514/6.2013-1453
[research_vale_leite_2011]: https://doi.org/10.1177/1045389x11416031
[research_valenti_stanton_2024]: https://doi.org/10.2514/6.2024-85365
[research_vandam_1985]: https://doi.org/10.4271/851770
[research_vandam_1986]: https://doi.org/10.2514/6.1986-1824
[research_vandam_holmes_1980]: https://doi.org/10.2514/6.1980-1870
[research_vandam_holmes_1981]: https://doi.org/10.2514/3.57531
[research_vandam_vijgen_1990]: https://doi.org/10.2514/6.1990-300
[research_vandenberg_elsenaar_1975]: https://doi.org/10.1017/s0022112075001930
[research_vandervelden_1987]: https://ntrs.nasa.gov/citations/19880013507
[research_vandervelden_1989]: https://ntrs.nasa.gov/citations/19890015862
[research_vandervelden_1992]: https://ntrs.nasa.gov/citations/19920000044
[research_vandervelden_kroo_1990]: https://ntrs.nasa.gov/citations/19900019224
[research_vandervelden_kroo_1994]: https://doi.org/10.2514/3.46450
[research_vandervelden_torenbeek_1989]: https://doi.org/10.2514/3.45745
[research_vandierendonck_1973]: https://doi.org/10.2514/6.1973-159
[research_vandommelen_dsilva_2019]: https://doi.org/10.2514/6.2019-3569
[research_vanes_2002]: https://doi.org/10.2514/2.2997
[research_vanthullenar_1957]: https://doi.org/10.1080/00431672.1957.9924976
[research_vargas_2007]: https://doi.org/10.4271/2007-01-3332
[research_vargas_kreeger_2009]: https://doi.org/10.2514/6.2009-4123
[research_vargas_ratvasky_2002]: https://doi.org/10.2514/6.2002-244
[research_variable_sweep_1965]: https://doi.org/10.1108/eb034080
[research_variable_sweep_1980]: https://doi.org/10.2514/6.1980-3043
[research_vasile_elimelech_2010]: https://doi.org/10.2514/6.2010-4584
[research_vasista_degaspari_2016]: https://doi.org/10.1108/aeat-02-2015-0067
[research_vasista_riemenschneider_2017]: https://doi.org/10.2514/1.c033909
[research_vatandas_2010]: https://doi.org/10.2514/6.2010-2915
[research_vaughan_2003]: https://doi.org/10.1016/b0-12-227090-8/00379-1
[research_vaughan_wood_1995]: https://doi.org/10.2514/6.1995-1874
[research_vavra_solomon_2005]: https://doi.org/10.2514/6.2005-1030
[research_vazquez_joshi_2020]: https://doi.org/10.2514/6.2020-2009
[research_veerman_kannemans_2013]: https://doi.org/10.1007/978-3-642-34738-2_3
[research_velkova_todorov_2015]: https://doi.org/10.19062/1842-9238.2015.13.3.6
[research_venkatakrishnan_sundaram_2006]: https://doi.org/10.2514/1.17397
[research_vepa_2008]: https://doi.org/10.2514/1.34928
[research_vepa_2023]: https://doi.org/10.1201/9781003266310-10
[research_vepa_2023_b]: https://doi.org/10.1201/9781003266310-8
[research_vepa_2023_c]: https://doi.org/10.1201/9781003266310-7
[research_vepa_2023_d]: https://doi.org/10.1201/9781003266310-4
[research_vermeersch_yoshida_2015]: https://doi.org/10.1016/j.paerosci.2015.07.003
[research_verrastro_metge_2015]: https://doi.org/10.1007/978-3-319-22413-8_2
[research_videan_1955]: https://ntrs.nasa.gov/citations/19930089024
[research_viglietti_zappino_2019]: https://doi.org/10.2514/1.c034795
[research_vigliotti_pasini_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00008-3
[research_viken_collier_1990]: https://doi.org/10.1007/978-3-642-84103-3_34
[research_vinayagamurthy_parammasivam_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.3500
[research_vincent_1991]: https://ntrs.nasa.gov/citations/19910020817
[research_vindigni_2023]: https://doi.org/10.21741/9781644902677-31
[research_visbal_garmann_2018]: https://doi.org/10.2514/6.2018-0357
[research_visbal_garmann_2019]: https://doi.org/10.2514/1.j058206
[research_visbal_gordnier_1995]: https://doi.org/10.2514/3.46821
[research_vishwanathan]: https://doi.org/10.33915/etd.1816
[research_visonneau_guilmineau_2015]: https://doi.org/10.2514/6.2015-0065
[research_visonneau_guilmineau_2022]: https://doi.org/10.2514/6.2022-0027
[research_vocke_kothera_2011]: https://doi.org/10.1177/1045389x11411121
[research_vockeiii_s_2012]: https://doi.org/10.5772/37333
[research_vogeltanz_2016]: https://doi.org/10.1063/1.4951901
[research_vogler_1956]: https://ntrs.nasa.gov/citations/19930088964
[research_vogler_1976]: https://ntrs.nasa.gov/citations/19770005052
[research_vonderwell_riahi_1998]: https://doi.org/10.1016/s0020-7225(97)00098-0
[research_vonglahn_groesbeck_1976]: https://doi.org/10.2514/6.1976-622
[research_voracek_2007]: https://ntrs.nasa.gov/citations/20070024435
[research_vos_debreuker_2007]: https://doi.org/10.2514/1.21292
[research_vos_farokhi_2015]: https://doi.org/10.1007/978-94-017-9747-4_8
[research_vos_gurdal_2010]: https://doi.org/10.2514/1.39328
[research_voss_2018]: https://doi.org/10.2514/6.2018-3326
[research_vu]: https://doi.org/10.31274/rtd-20200803-400
[research_waggoner_1986]: https://ntrs.nasa.gov/citations/19880014356
[research_waggoner_allison_1987]: https://doi.org/10.2514/6.1987-2360
[research_waggoner_campbell_1985]: https://ntrs.nasa.gov/citations/19860026301
[research_waggoner_campbell_1986]: https://ntrs.nasa.gov/citations/19880005566
[research_waggoner_campbell_1987]: https://ntrs.nasa.gov/citations/19900003228
[research_waggoner_phillips_1985]: https://ntrs.nasa.gov/citations/19850037590
[research_wagner_bartlett_1988]: https://ntrs.nasa.gov/citations/19880033712
[research_wagner_fisher_1986]: https://ntrs.nasa.gov/citations/19880005570
[research_wagner_maddalon_1988]: https://ntrs.nasa.gov/citations/19890063984
[research_wagner_maddalon_1992]: https://ntrs.nasa.gov/citations/19930057781
[research_wakayama_kroo_1995]: https://doi.org/10.2514/3.46786
[research_wakimoto_chiba_2021]: https://doi.org/10.3390/aerospace8080217
[research_walchli_1994]: https://ntrs.nasa.gov/citations/19950007845
[research_walchli_guyton_1992]: https://doi.org/10.2514/6.1992-4427
[research_waldmann_ehrle_2023]: https://doi.org/10.1007/s00348-023-03642-7
[research_wales_cheung_2015]: https://doi.org/10.2514/6.2015-1053
[research_walker_bons_2018]: https://doi.org/10.2514/6.2018-0793
[research_walker_hipp_2016]: https://doi.org/10.2514/6.2016-3120
[research_walkley_1986]: https://doi.org/10.2514/6.1986-2627
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_wallis_ellis_1982]: https://doi.org/10.2514/6.1982-1323
[research_wan_2024]: https://doi.org/10.54097/w5p7gb19
[research_wan_yang_2003]: https://doi.org/10.2514/6.2003-1416
[research_wang]: https://doi.org/10.23889/suthesis.40876
[research_wang_1979]: https://doi.org/10.21236/ada074260
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2024]: https://doi.org/10.2316/j.2024.201-0461
[research_wang_2024_b]: https://doi.org/10.54097/hverx006
[research_wang_2025]: https://doi.org/10.2316/j.2025.201-0461
[research_wang_2025_b]: https://doi.org/10.54254/2755-2721/2026.ka27405
[research_wang_2026]: https://doi.org/10.1017/jfm.2026.11425
[research_wang_2026_2]: https://doi.org/10.1063/5.0312279
[research_wang_2026_3]: https://doi.org/10.1007/s11431-025-3198-1
[research_wang_2026_4]: https://doi.org/10.3390/ma19122678
[research_wang_2026_b]: https://doi.org/10.1590/jatm.v18.1450
[research_wang_bai_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.1277
[research_wang_chen_2023]: https://doi.org/10.1016/j.tws.2023.111266
[research_wang_dong_2015]: https://doi.org/10.1016/j.ijleo.2015.08.040
[research_wang_dong_2016]: https://doi.org/10.1016/j.cja.2016.02.011
[research_wang_duan_2025]: https://doi.org/10.1134/s0015462825601792
[research_wang_gong_2019]: https://doi.org/10.1016/j.ast.2019.105325
[research_wang_guo_2024]: https://doi.org/10.1109/meae62008.2024.11026361
[research_wang_guo_2024_b]: https://doi.org/10.1016/j.ast.2024.109685
[research_wang_herbert_1994]: https://doi.org/10.2514/6.1994-2374
[research_wang_herbert_1994_b]: https://doi.org/10.2514/6.1994-180
[research_wang_hou_2021]: https://doi.org/10.1109/cac53003.2021.9727458
[research_wang_hou_2023]: https://doi.org/10.1007/978-981-19-6613-2_132
[research_wang_jia_2026]: https://doi.org/10.1007/978-981-95-3031-1_7
[research_wang_liu_2026]: https://doi.org/10.1016/j.biosystemseng.2026.104447
[research_wang_qian_2023]: https://doi.org/10.3390/aerospace10100854
[research_wang_qin_2013]: https://doi.org/10.1016/j.proeng.2013.12.034
[research_wang_su_2018]: https://doi.org/10.1088/1757-899x/452/4/042048
[research_wang_sun_2024]: https://doi.org/10.3390/aerospace11050366
[research_wang_sun_2025]: https://doi.org/10.3390/app15179759
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_tu_2010]: https://doi.org/10.1007/s11434-009-0643-z
[research_wang_tu_2025]: https://doi.org/10.2139/ssrn.5292423
[research_wang_tu_2026]: https://doi.org/10.2514/1.c038759
[research_wang_wang_2024]: https://doi.org/10.3390/app14051953
[research_wang_xu_2016]: https://doi.org/10.1016/j.cja.2016.10.010
[research_wang_yu_2023]: https://doi.org/10.1177/00202940221145971
[research_wang_zeng_2025]: https://doi.org/10.1109/aaac66612.2025.11427827
[research_wang_zha_2019]: https://doi.org/10.2514/6.2019-0034
[research_wang_zhan_2005]: https://doi.org/10.2514/1.9929
[research_wang_zhao_2024]: https://doi.org/10.2139/ssrn.5001796
[research_ward_1949]: https://doi.org/10.1017/s0001925900000056
[research_ward_bennett_1976]: https://doi.org/10.2514/3.58689
[research_warren_hassan_1997]: https://doi.org/10.2514/6.1997-2245
[research_warwick_bras_2019]: https://doi.org/10.2514/6.2019-1116
[research_wasserman_mitchell_1973]: https://doi.org/10.21236/ad0761120
[research_waszak_buttrill_1991]: https://doi.org/10.2514/6.1991-3111
[research_waszak_srinathkumar_1992]: https://doi.org/10.2514/6.1992-2097
[research_watanabe_sunada_2021]: https://doi.org/10.2514/6.2021-1932
[research_waters_ardema_1992]: https://ntrs.nasa.gov/citations/19930029339
[research_weatherill_ehlers_1989]: https://ntrs.nasa.gov/citations/19890010722
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_webb_mccain_1988]: https://ntrs.nasa.gov/citations/19890006537
[research_weber_1990]: https://doi.org/10.21236/ada228713
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_weed_carlson_1984]: https://doi.org/10.2514/6.1984-2156
[research_wei_new_2019]: https://doi.org/10.1016/j.oceaneng.2019.04.018
[research_wei_tong_2026]: https://doi.org/10.4271/2026-99-1860
[research_weil_1953]: https://ntrs.nasa.gov/citations/19930087927
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weisshaar_1974]: https://ntrs.nasa.gov/citations/19740047649
[research_weisshaar_1975]: https://ntrs.nasa.gov/citations/19760008948
[research_weisshaar_1976]: https://ntrs.nasa.gov/citations/19760023069
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1979_b]: https://doi.org/10.2514/6.1979-722
[research_weisshaar_1980]: https://doi.org/10.2514/6.1980-795
[research_weisshaar_1981]: https://doi.org/10.2514/3.57542
[research_weisshaar_1983]: https://ntrs.nasa.gov/citations/19840055636
[research_weisshaar_1985]: https://doi.org/10.2514/3.48607
[research_weisshaar_1990]: https://doi.org/10.2514/3.25276
[research_weisshaar_1994]: https://doi.org/10.2514/3.46463
[research_weisshaar_2013]: https://doi.org/10.2514/1.c031456
[research_weisshaar_ashley_1973]: https://doi.org/10.2514/3.60265
[research_weisshaar_ashley_1974]: https://doi.org/10.2514/3.44409
[research_weisshaar_crittenden_1976]: https://ntrs.nasa.gov/citations/19760014076
[research_weisshaar_schmidt_1981]: https://ntrs.nasa.gov/citations/19820005277
[research_weisshaar_zeiler_1982]: https://ntrs.nasa.gov/citations/19820055567
[research_weisshaar_zeiler_1983]: https://doi.org/10.2514/3.48205
[research_weissman_1969]: https://doi.org/10.2514/6.1969-188
[research_weissman_1973]: https://doi.org/10.2514/3.60216
[research_weissman_1975]: https://doi.org/10.2514/3.59904
[research_wells_olson_2011]: https://doi.org/10.2514/6.2011-360
[research_wen_deng_2013]: https://doi.org/10.1016/j.proeng.2013.12.032
[research_wentz_ahmed_1985]: https://ntrs.nasa.gov/citations/19860053766
[research_wentzjr_nyenhuis_1984]: https://doi.org/10.2514/6.1984-2189
[research_wenzinger_harris_1931]: https://ntrs.nasa.gov/citations/19930091086
[research_werner_henne_2024]: https://doi.org/10.2514/6.2024-2333
[research_werner_schutte_2022]: https://doi.org/10.2514/6.2022-0295
[research_werter_debreuker_2015]: https://doi.org/10.2514/6.2015-0268
[research_west_1960]: https://ntrs.nasa.gov/citations/20040020128
[research_westfall_canfield_2007]: https://doi.org/10.2514/6.2007-1715
[research_westin_defreitaspinto_2008]: https://doi.org/10.4271/2008-36-0247
[research_whipple_1980]: https://ntrs.nasa.gov/citations/19800020866
[research_whipple_1982]: https://ntrs.nasa.gov/citations/19820059729
[research_whipple_1984]: https://ntrs.nasa.gov/citations/19870000608
[research_whitcomb_1956]: https://ntrs.nasa.gov/citations/19650070830
[research_whitcomb_1961]: https://ntrs.nasa.gov/citations/20040027948
[research_whitcomb_1983]: https://ntrs.nasa.gov/citations/19840004011
[research_whitcomb_critzos_1961]: https://ntrs.nasa.gov/citations/20040006450
[research_white_1947]: https://ntrs.nasa.gov/citations/20050019312
[research_white_1970]: https://doi.org/10.2514/6.1970-877
[research_white_1985]: https://ntrs.nasa.gov/citations/19840000357
[research_white_1985_b]: https://ntrs.nasa.gov/citations/19850026887
[research_white_bowman_1982]: https://ntrs.nasa.gov/citations/19820010309
[research_white_crimi_1961]: https://doi.org/10.21236/ad0275102
[research_white_kapania_2015]: https://ntrs.nasa.gov/citations/20150017734
[research_white_saric_2001]: https://doi.org/10.2514/6.2001-271
[research_whitlow_1993]: https://ntrs.nasa.gov/citations/19930055501
[research_whittle_lipson_1953]: https://ntrs.nasa.gov/citations/19930087818
[research_whittle_lipson_1954]: https://ntrs.nasa.gov/citations/19930088177
[research_wickenheiser_garcia_2012]: https://doi.org/10.1002/9781119964032.ch8
[research_widowati_riyanto_2012]: https://doi.org/10.5614/itbj.eng.sci.2012.44.2.5
[research_wieszala_kolodziej_2022]: https://doi.org/10.1109/ntad57912.2022.10013540
[research_wiggins_kuhn_1953]: https://ntrs.nasa.gov/citations/19930088296
[research_wiggins_stubbs_2004]: https://doi.org/10.2514/6.2004-1885
[research_wilbur_mistry_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00024-1
[research_wild_2013]: https://doi.org/10.2514/1.c032138
[research_wildschek_2014]: https://doi.org/10.2514/6.2014-0599
[research_wildschek_judas_2008]: https://doi.org/10.2514/6.2008-8956
[research_wildschek_maier_2009]: https://doi.org/10.2514/6.2009-6118
[research_wiler_white_1984]: https://doi.org/10.2514/6.1984-2474
[research_wiler_white_1985]: https://doi.org/10.2514/3.45221
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_willen_1975]: https://doi.org/10.2514/6.1975-33
[research_williams_dicamillo_1959]: https://ntrs.nasa.gov/citations/19980228225
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_wilmott_1986]: https://doi.org/10.1017/s0001924000015347
[research_wind_tunnel_2004]: https://doi.org/10.3795/ksme-b.2004.28.7.800
[research_wing_design_2012]: https://doi.org/10.1002/9781118352700.ch5
[research_wing_design_2021]: https://doi.org/10.1017/9781139094672.011
[research_wing_design_2025]: https://doi.org/10.1002/9781394313990.ch9
[research_wing_loads_1996]: https://doi.org/10.2514/5.9781600862465.0163.0190
[research_wing_morphing_2013]: https://doi.org/10.1201/b16257-11
[research_wing_shapes_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n20
[research_wing_tunnel_1998]: https://doi.org/10.1108/aeat.1998.12770ead.003
[research_wings_2017]: https://doi.org/10.1002/9781119406303.ch3
[research_winkelman_barlow_1980]: https://doi.org/10.2514/3.50846
[research_winkelmann_1989]: https://doi.org/10.2514/6.1989-570
[research_winski_langston]: https://ntrs.nasa.gov/citations/20240013222
[research_winski_langston_2025]: https://doi.org/10.2514/6.2025-0249
[research_wintzer_sturdza_2006]: https://doi.org/10.2514/6.2006-930
[research_wise_1992]: https://doi.org/10.23919/acc.1992.4792318
[research_witkowski_williams_2022]: https://doi.org/10.2514/6.2022-2737
[research_wittmann_steiner_2009]: https://doi.org/10.2514/6.2009-2129
[research_wlezien_horner_1998]: https://doi.org/10.2514/6.1998-1927
[research_woan_chakravarthy_1988]: https://doi.org/10.2514/6.1988-2547
[research_woldhuis_asaro_2026]: https://doi.org/10.2514/1.g008985
[research_wolhart_1951]: https://ntrs.nasa.gov/citations/19930083409
[research_wolkovitch_1984]: https://ntrs.nasa.gov/citations/19850031402
[research_wong_bil_2022]: https://doi.org/10.2514/6.2022-1298
[research_wong_rock_1993]: https://doi.org/10.2514/6.1993-56
[research_wong_va_1995]: https://doi.org/10.2514/6.1995-42
[research_woo_1992]: https://doi.org/10.2514/6.1992-4765
[research_wood_1946]: https://ntrs.nasa.gov/citations/19930093514
[research_woodard_bragg_2020]: https://doi.org/10.2514/6.2020-2848
[research_wooden_smith_2007]: https://doi.org/10.2514/6.2007-4433
[research_woodruff_saric_2011]: https://doi.org/10.2514/6.2011-3882
[research_woods_gilbert_1989]: https://ntrs.nasa.gov/citations/19890014953
[research_woods_spooner_1948]: https://ntrs.nasa.gov/citations/19930085435
[research_woods_wereley_2013]: https://doi.org/10.2514/6.2013-1513
[research_woods_wood_2000]: https://doi.org/10.2514/2.2704
[research_wortman_1999]: https://doi.org/10.2514/2.2484
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_wright_loving_1953]: https://ntrs.nasa.gov/citations/20050019302
[research_wu_cai_2026]: https://doi.org/10.1049/cth2.70181
[research_wu_cai_2026_b]: https://doi.org/10.1109/jmass.2026.3725681
[research_wu_dai_2013]: https://doi.org/10.2514/1.c031618
[research_wu_hu_2023]: https://doi.org/10.1063/5.0168549
[research_wu_huang_2024]: https://doi.org/10.3390/aerospace11020143
[research_wu_lu_2016]: https://doi.org/10.1007/s11071-016-3196-0
[research_wu_lu_2017]: https://doi.org/10.1109/ccdc.2017.7978057
[research_wu_squires_1995]: https://doi.org/10.1115/1.2817310
[research_wu_tan_2021]: https://doi.org/10.1109/cac53003.2021.9728193
[research_wu_xiao_2017]: https://doi.org/10.2514/1.c034356
[research_wu_xiao_2018]: https://doi.org/10.2514/1.g003000
[research_wu_xu_2023]: https://doi.org/10.1016/j.measurement.2023.113214
[research_wunderlich_dahne_2017]: https://doi.org/10.1007/s13272-017-0251-6
[research_wunderlich_dahne_2017_b]: https://doi.org/10.1007/s13272-017-0266-z
[research_xi_dai_2025]: https://doi.org/10.1063/5.0255492
[research_xia_ajaj_2014]: https://doi.org/10.2514/6.2014-0762
[research_xia_jing_2023]: https://doi.org/10.3390/aerospace10050448
[research_xia_zhu_1993]: https://doi.org/10.2514/6.1993-3482
[research_xiang_liu_2018]: https://doi.org/10.1108/aeat-04-2017-0101
[research_xiao_chen_2019]: https://doi.org/10.1109/icras.2019.8808959
[research_xiao_guo_2023]: https://doi.org/10.1155/2023/7078091
[research_xiaolonghe_junqiangbai_2017]: https://doi.org/10.1109/icmimt.2017.7917465
[research_xie_cai_2026]: https://doi.org/10.2514/1.c038668
[research_xie_chen_2022]: https://doi.org/10.2514/6.2022-0849
[research_xijuan_qiang_2016]: https://doi.org/10.2514/1.c033252
[research_xin_li_2025]: https://doi.org/10.1038/s41598-025-08792-8
[research_xinbing_wen_2019]: https://doi.org/10.1088/1757-899x/685/1/012016
[research_xinbing_wen_2020]: https://doi.org/10.1088/1742-6596/1605/1/012075
[research_xiong_bartels_2021]: https://doi.org/10.2514/6.2021-2528
[research_xiong_liu_2013]: https://doi.org/10.2514/6.2013-3205
[research_xiong_nguyen_2022]: https://doi.org/10.2514/6.2022-0016
[research_xiong_nguyen_2022_b]: https://doi.org/10.2514/6.2022-4150
[research_xiong_nguyen_2022_c]: https://doi.org/10.2514/6.2022-0300
[research_xiong_nguyen_2023]: https://doi.org/10.2514/6.2023-1575
[research_xiong_nguyen_2023_b]: https://doi.org/10.2514/6.2023-4528
[research_xiong_nguyen_2024]: https://doi.org/10.2514/6.2024-2668
[research_xiong_nguyen_2026]: https://doi.org/10.2514/6.2026-1111
[research_xiong_yang_2001]: https://doi.org/10.2514/6.2001-1463
[research_xu_2012]: https://doi.org/10.4028/www.scientific.net/amr.538-541.2627
[research_xu_2026]: https://doi.org/10.1016/j.ast.2026.112293
[research_xu_amano_2004]: https://doi.org/10.1115/gt2004-53008
[research_xu_chen_2019]: https://doi.org/10.1017/jfm.2019.397
[research_xu_deng_2013]: https://doi.org/10.1016/j.proeng.2013.12.024
[research_xu_han_2019]: https://doi.org/10.1155/2019/9362629
[research_xu_han_2019_b]: https://doi.org/10.2514/6.2019-3291
[research_xu_han_2021]: https://doi.org/10.2514/1.j059971
[research_xu_he_2021]: https://doi.org/10.1007/978-3-030-67902-6_72
[research_xu_lessis_2026]: https://doi.org/10.21203/rs.3.rs-9884412/v1
[research_xu_li_2022]: https://doi.org/10.1016/j.ast.2022.107898
[research_xu_li_2022_b]: https://doi.org/10.1016/j.ast.2022.107349
[research_xu_li_2023]: https://doi.org/10.3390/aerospace10010049
[research_xu_lu_2018]: https://doi.org/10.1109/yac.2018.8406387
[research_xu_song_2023]: https://doi.org/10.2139/ssrn.4549793
[research_xu_song_2025]: https://doi.org/10.1063/5.0275245
[research_xu_song_2026]: https://doi.org/10.1063/5.0321695
[research_xu_wu_2022]: https://doi.org/10.2514/1.j061211
[research_xu_yang_2012]: https://doi.org/10.4028/www.scientific.net/amm.197.159
[research_xu_yang_2012_b]: https://doi.org/10.4028/www.scientific.net/amr.542-543.873
[research_xu_yue_2016]: https://doi.org/10.1109/cgncc.2016.7828930
[research_xu_zhang_2018]: https://doi.org/10.12783/dtcse/mmsta2017/19666
[research_xu_zhang_2025]: https://doi.org/10.1016/j.cja.2024.103332
[research_xu_zhou_2015]: https://doi.org/10.1016/j.ast.2015.07.022
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_yadalavenkata_hehner_2018]: https://doi.org/10.2514/6.2018-3215
[research_yajnik_subbaiah_1976]: https://doi.org/10.2514/3.44515
[research_yakeno_obayashi_2021]: https://doi.org/10.1063/5.0063936
[research_yamada_nakamura_2002]: https://doi.org/10.2514/6.2002-97
[research_yamamoto_1992]: https://doi.org/10.2514/3.11227
[research_yamamoto_tanaka_2012]: https://doi.org/10.2514/6.2012-2895
[research_yaman_2017]: https://doi.org/10.1007/978-3-319-60702-3_1
[research_yaman_dalmis_2026]: https://doi.org/10.21278/tof.502080725
[research_yan_dai_2019]: https://doi.org/10.1016/j.ast.2019.05.063
[research_yan_han_2025]: https://doi.org/10.2174/0118722121302573240527051750
[research_yan_li_2019]: https://doi.org/10.1051/jnwpu/20193740656
[research_yan_li_2019_b]: https://doi.org/10.1061/(asce)as.1943-5525.0001047
[research_yan_mccrink_2025]: https://doi.org/10.2514/6.2025-3319
[research_yang]: https://doi.org/10.31274/td-20260812-346
[research_yang_2026]: https://doi.org/10.1016/j.cja.2026.104412
[research_yang_an_2017]: https://doi.org/10.2514/6.2017-3268
[research_yang_cai_2022]: https://doi.org/10.23919/ccc55666.2022.9902261
[research_yang_chen_2023]: https://doi.org/10.1109/isas59543.2023.10164379
[research_yang_guo_2019]: https://doi.org/10.1109/robio49542.2019.8961843
[research_yang_guo_2021]: https://doi.org/10.1109/robio54168.2021.9739269
[research_yang_guo_2021_b]: https://doi.org/10.1007/s10443-021-09926-7
[research_yang_guo_2022]: https://doi.org/10.1007/s10443-022-10044-1
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_li_2022]: https://doi.org/10.3390/aerospace9090515
[research_yang_li_2025]: https://doi.org/10.1088/1742-6596/3085/1/012017
[research_yang_lu_2023]: https://doi.org/10.1109/iscsic60498.2023.00015
[research_yang_przekwas_1993_b]: https://doi.org/10.2514/6.1993-2976
[research_yang_sartor_2015]: https://doi.org/10.2514/6.2015-0441
[research_yang_tan_2023]: https://doi.org/10.23919/acc55779.2023.10155880
[research_yang_tang_2015]: https://doi.org/10.2495/csse140671
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wang_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001475
[research_yang_xiao_2024]: https://doi.org/10.2514/1.c037399
[research_yang_xu_2024]: https://doi.org/10.1007/s11071-024-09764-9
[research_yang_zhao_2026]: https://doi.org/10.3390/inventions11050087
[research_yang_zhong_2021]: https://doi.org/10.1016/j.cja.2020.12.042
[research_yaniktepe_rockwell_2004]: https://doi.org/10.2514/1.1207
[research_yao_song_2023]: https://doi.org/10.1016/j.ast.2023.108436
[research_yao_wu_2019]: https://doi.org/10.1109/access.2019.2905628
[research_yasuaki_egami_1999]: https://doi.org/10.2514/6.1999-921
[research_yates_1960]: https://ntrs.nasa.gov/citations/19630003038
[research_yates_1960_b]: https://ntrs.nasa.gov/citations/19630004021
[research_yates_1963]: https://doi.org/10.2514/6.1963-205
[research_yates_1967]: https://ntrs.nasa.gov/citations/20040047107
[research_yates_chu_1987]: https://ntrs.nasa.gov/citations/19870012837
[research_yates_cunningham_1982]: https://ntrs.nasa.gov/citations/19820046658
[research_yatskikh_rumenskikh_2017]: https://doi.org/10.1051/matecconf/201711502015
[research_yavuz_2012]: https://doi.org/10.1016/j.jfluidstructs.2012.05.006
[research_ye_2025]: https://doi.org/10.54254/2753-8818/2026.ch30896
[research_ye_peng_2026]: https://doi.org/10.1109/csis-iac70275.2026.11585035
[research_ye_xu_2025]: https://doi.org/10.1109/fasta65681.2025.11138926
[research_yechout_oelschlaeger_1976]: https://doi.org/10.2514/6.1976-1913
[research_yen_2011]: https://doi.org/10.51400/2709-6998.2151
[research_yen_hsu_2006]: https://doi.org/10.1115/1.2734212
[research_yen_hsu_2007]: https://doi.org/10.2514/1.24045
[research_yen_huang_2011]: https://doi.org/10.1016/j.ast.2010.10.005
[research_yen_san_2013]: https://doi.org/10.1016/j.expthermflusci.2012.09.015
[research_yeo_atkins_2015]: https://doi.org/10.2514/1.c032682
[research_yermolaev_kosinov_2014]: https://doi.org/10.1134/s0021894414050058
[research_yermolaev_yatskikh_2017]: https://doi.org/10.1063/1.5007445
[research_yermolaev_yatskikh_2020]: https://doi.org/10.1063/5.0028398
[research_yigit_millidere_2021]: https://doi.org/10.2514/6.2021-2999
[research_yildirim_tuncer_2021]: https://doi.org/10.2514/6.2021-2564
[research_yip_ross_1992]: https://doi.org/10.2514/3.46248
[research_yip_shubert_1977]: https://ntrs.nasa.gov/citations/19770026159
[research_yip_vijgen_1992]: https://ntrs.nasa.gov/citations/19930027278
[research_yip_vijgen_1993]: https://ntrs.nasa.gov/citations/19940013962
[research_yoo_2018]: https://doi.org/10.2514/6.2018-3009
[research_yoshida_bragg_2021]: https://doi.org/10.2514/6.2021-2680
[research_you_2026]: https://doi.org/10.2139/ssrn.6802803
[research_you_kim_2019]: https://doi.org/10.2514/1.j058102
[research_you_skin_2020]: https://doi.org/10.2514/1.j058002
[research_young_1974]: https://ntrs.nasa.gov/citations/19740025340
[research_young_2026]: https://doi.org/10.2139/ssrn.6790560
[research_young_adams_1972]: https://ntrs.nasa.gov/citations/19720058663
[research_yu_2026]: https://doi.org/10.1109/access.2026.3668314
[research_yu_campbell_1992]: https://doi.org/10.2514/6.1992-2651
[research_yu_he_2016]: https://doi.org/10.1109/chicc.2016.7553228
[research_yu_hornung_2026]: https://doi.org/10.2139/ssrn.7180118
[research_yu_liu_2009]: https://doi.org/10.1117/12.815675
[research_yu_ma_2022]: https://doi.org/10.3390/app12063092
[research_yu_yan_2026]: https://doi.org/10.2139/ssrn.6580127
[research_yu_yang_2019]: https://doi.org/10.2514/6.2019-3348
[research_yu_zhou_2024]: https://doi.org/10.2514/1.j063544
[research_yuan_friedman_1994]: https://doi.org/10.2514/6.1994-1309
[research_yuan_sandhu_2016]: https://doi.org/10.2514/6.2016-1550
[research_yue_oblique_2019]: https://doi.org/10.1016/j.cja.2018.11.002
[research_yue_wang_2009]: https://doi.org/10.2514/6.2009-6155
[research_yue_wang_2013]: https://doi.org/10.2514/6.2013-623
[research_yue_wang_2013_b]: https://doi.org/10.2514/1.c031316
[research_yue_wang_2013_c]: https://doi.org/10.1016/j.cja.2013.06.004
[research_yue_wang_2013_d]: https://doi.org/10.2514/6.2013-624
[research_yue_wang_2017]: https://doi.org/10.2514/6.2017-3396
[research_yue_zhang_2017]: https://doi.org/10.1016/j.ast.2017.08.013
[research_yuhong_guanxin_2017]: https://doi.org/10.1109/icmae.2017.8038694
[research_yukish_valenti_2020]: https://doi.org/10.2514/1.c035586
[research_yurkovich_1996]: https://doi.org/10.2514/6.1996-1447
[research_yurkovich_2008]: https://doi.org/10.2514/6.2008-1899
[research_yurkovich_2009]: https://doi.org/10.2514/6.2009-2514
[research_yutong_ying_2025]: https://doi.org/10.1016/j.ast.2024.109905
[research_zangeneh_2021]: https://doi.org/10.1063/5.0065686
[research_zangeneh_2022]: https://doi.org/10.2514/6.2022-0306
[research_zarutskaya_arieli_2005]: https://doi.org/10.2514/6.2005-4913
[research_ze_shen_2024]: https://doi.org/10.1109/iciea61579.2024.10665085
[research_zebedee_mohammed_2019]: https://doi.org/10.1109/nigeriacomputconf45974.2019.8949627
[research_zeiger_gerlach_2002]: https://doi.org/10.2514/6.2002-414
[research_zeng_kukreja_2013]: https://doi.org/10.2514/1.c031710
[research_zeng_liu_2023]: https://doi.org/10.1016/j.cja.2023.01.002
[research_zhan_wang_2007]: https://doi.org/10.1007/978-3-540-75995-9_66
[research_zhang_2026]: https://doi.org/10.1109/tmech.2026.3708549
[research_zhang_deng_2026]: https://doi.org/10.3390/aerospace13010098
[research_zhang_guo_2025]: https://doi.org/10.23919/ccc64809.2025.11179440
[research_zhang_hua_2014]: https://doi.org/10.1007/s11431-014-5702-2
[research_zhang_liu_2017]: https://doi.org/10.2514/1.c033511
[research_zhang_lu_2026]: https://doi.org/10.21203/rs.3.rs-8972451/v1
[research_zhang_pu_2026]: https://doi.org/10.3390/aerospace13050441
[research_zhang_pu_2026_b]: https://doi.org/10.1016/j.ast.2026.113413
[research_zhang_shaw_2018]: https://doi.org/10.1115/detc2018-85640
[research_zhang_shaw_2021]: https://doi.org/10.1016/j.ast.2021.106534
[research_zhang_song_2025]: https://doi.org/10.1177/00202940251325745
[research_zhang_taira_2022]: https://doi.org/10.2514/6.2022-0730
[research_zhang_wang_2017]: https://doi.org/10.1504/ijmic.2017.083785
[research_zhang_wang_2019]: https://doi.org/10.2514/1.c035182
[research_zhang_wei_2017]: https://doi.org/10.21595/vp.2017.19152
[research_zhang_wen_2024]: https://doi.org/10.1109/cac63892.2024.10865076
[research_zhang_wu_2014]: https://doi.org/10.1109/ccdc.2014.6852767
[research_zhang_wu_2014_b]: https://doi.org/10.1109/ccdc.2014.6852195
[research_zhang_yan_2020]: https://doi.org/10.1016/j.cja.2020.05.015
[research_zhang_yang_2016]: https://doi.org/10.2514/6.2016-1783
[research_zhang_yang_2025]: https://doi.org/10.2514/1.c038158
[research_zhang_yang_2026]: https://doi.org/10.1016/j.ast.2026.111776
[research_zhang_yu_2012]: https://doi.org/10.2514/1.c031652
[research_zhang_yu_2013]: https://doi.org/10.2514/1.c031740
[research_zhang_zhang_2024]: https://doi.org/10.2139/ssrn.4819074
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10020197
[research_zhang_zhao_2026]: https://doi.org/10.1007/s42405-026-01144-4
[research_zhang_zhou_2015]: https://doi.org/10.2514/1.c032739
[research_zhang_zhou_2018]: https://doi.org/10.2514/6.2018-3574
[research_zhang_zhou_2022]: https://doi.org/10.54097/hset.v16i.2537
[research_zhao_1988]: https://doi.org/10.2514/6.1988-3735
[research_zhao_1998]: https://doi.org/10.1007/bf02883808
[research_zhao_guo_2026]: https://doi.org/10.2139/ssrn.6802804
[research_zhao_hu_2013]: https://doi.org/10.4028/www.scientific.net/amr.709.257
[research_zhao_hu_2013_b]: https://doi.org/10.1016/j.ast.2011.09.001
[research_zhao_kapania_2017]: https://doi.org/10.2514/6.2017-4320
[research_zhao_luo_2022]: https://doi.org/10.1063/5.0132080
[research_zhao_xi_2021]: https://doi.org/10.1016/j.mechmachtheory.2021.104439
[research_zhao_yang_2023]: https://doi.org/10.1016/j.cja.2022.06.016
[research_zhao_zhang_2026]: https://doi.org/10.1016/j.array.2026.100997
[research_zhao_zhu_2016]: https://doi.org/10.1109/icuas.2016.7502671
[research_zhen_yingying_2017]: https://doi.org/10.1109/ccdc.2017.7978398
[research_zheng_he_2014]: https://doi.org/10.1109/cgncc.2014.7007454
[research_zhou_2018]: https://doi.org/10.2991/snce-18.2018.241
[research_zhou_huang_2021]: https://doi.org/10.1007/s11071-021-06577-y
[research_zhou_huang_2021_b]: https://doi.org/10.1016/j.cnsns.2021.105946
[research_zhou_plummer_2018]: https://doi.org/10.1115/fpmc2018-8863
[research_zhou_plummer_2022]: https://doi.org/10.1109/tmech.2021.3058074
[research_zhou_wu_2025]: https://doi.org/10.1109/comea66280.2025.11241841
[research_zhu_2018]: https://doi.org/10.3901/jme.2018.14.028
[research_zhu_breuer_2022]: https://doi.org/10.2514/6.2022-2328
[research_zhu_li_2019]: https://doi.org/10.2514/1.j058011
[research_zhu_liu_2017]: https://doi.org/10.1109/ccdc.2017.7978791
[research_zhu_liu_2019]: https://doi.org/10.1109/icus48101.2019.8996021
[research_zhu_zhou_2025]: https://doi.org/10.2514/1.g008194
[research_zhu_zhou_2025_b]: https://doi.org/10.1007/s13272-025-00852-z
[research_zhu_zhu_2026]: https://doi.org/10.2514/1.c038900
[research_zientarski_marks_2015]: https://doi.org/10.2514/6.2015-3007
[research_zimper_rein_2014]: https://doi.org/10.2514/6.2014-2005
[research_zink_mavris_2000]: https://doi.org/10.2514/6.2000-4827
[research_zink_mavris_2001]: https://doi.org/10.2514/2.2884
[research_zoppini_ragni_2022]: https://doi.org/10.2139/ssrn.4036119
[research_zoppini_ragni_2022_b]: https://doi.org/10.2514/6.2022-1213
[research_zverkov_kozlov_2012]: https://doi.org/10.54362/1818-7919-2012-7-4-57-67
