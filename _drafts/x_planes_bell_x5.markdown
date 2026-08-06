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

The [Bell X-5][ref_bell_x5] was the first aircraft to change the sweep of its wing in flight. That sentence states the achievement and conceals the difficulty, because sweeping a wing moves the place where its lift acts, and an aircraft whose lift moves is an aircraft out of trim. This article is the sixth in the [X-Planes series][related_post_a297_xplanes_framing] and the fifth per-aircraft treatment, following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], and the [X-4][related_post_a301_northrop_x4]. The National Advisory Committee for Aeronautics, abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, supplied the research programme. The Air Force supplied the requirement. [Bell][ref_bell_aircraft] supplied an aircraft built around a captured German one.

The X-5 worked, and it killed a pilot, and the reason for both is the same piece of geometry.

## The Research Question

The keystone is whether wing sweep can be a variable rather than a choice.

Sweep is the central compromise of transonic design and it cannot be resolved in a fixed wing. Sweeping a wing back delays the onset of compressibility drag, because only the velocity component normal to the leading edge does the compressing. Resolving the free-stream velocity into components along and across the leading edge,

$$V_n = V \cos \Lambda, \qquad V_s = V \sin \Lambda, \qquad M_n = M \cos \Lambda$$

with $V_n$ the component that must be accelerated over the section and $V_s$ the spanwise component that must not. At Mach 0.9 and 60 degrees of sweep the section sees an effective Mach number of 0.45, which is subcritical by a wide margin, while the spanwise component reaches Mach 0.78 and drags boundary layer toward the tip. The simple sweep relation states the benefit,

$$M_{dd}(\Lambda) \approx \frac{M_{dd}(0)}{\cos^{k} \Lambda}, \qquad 0.5 \le k \le 1$$

with $k$ nearer one half than one in practice, since the flow does not obey the infinite-yawed-wing idealization at a real wing root or tip.

A pivoting wing collects a second benefit that a fixed swept wing does not, and it is worth separating because it is purely geometric. The physical section is fixed in the panel frame, so sweeping lengthens the chord measured in the flow direction while leaving the thickness alone,

$$c_{\text{stream}} = \frac{c_n}{\cos \Lambda} \quad \Longrightarrow \quad \left( \frac{t}{c} \right)_{\text{stream}} = \left( \frac{t}{c} \right)_n \cos \Lambda$$

so that a wing quoted at 11 percent thick streamwise at the low sweep setting presents

$$\left( \frac{t}{c} \right)_{\text{stream}} (60^\circ) = 0.11 \times \frac{\cos 60^\circ}{\cos 20^\circ} = 0.059$$

or 5.9 percent, at the high setting. **Sweeping the wing makes the aeroplane thinner as well as more swept**, and both act on the same drag-rise Mach number. Against that benefit stands a penalty on everything slow. Sweep reduces the lift-curve slope, reduces the maximum lift coefficient, promotes spanwise flow toward the tip and therefore tip stall, and it does all of this at precisely the flight condition where an aircraft needs lift most. The [swept wing][ref_swept_wing] is not a free improvement but a trade, and a fixed wing must buy one point on the trade and live at it.

The idea of refusing to choose is old and obvious. Set the sweep low for takeoff, climb, and landing, and set it high for the dash. The objection is equally obvious once stated, and it is geometric rather than aerodynamic. A wing that rotates about a pivot carries its lift with it. Let the panel pivot about a point at spanwise station $y_p$, and let the panel aerodynamic centre lie a distance $s_{ac}$ from that pivot measured along the panel. The streamwise position of that aerodynamic centre is then

$$x_{ac}(\Lambda) = x_p + s_{ac} \sin \Lambda$$

so that changing sweep from $\Lambda_1$ to $\Lambda_2$ translates the aerodynamic centre aft by

$$\Delta x_{ac} = s_{ac} \left( \sin \Lambda_2 - \sin \Lambda_1 \right)$$

This is the whole problem in one line. It contains no aerodynamics at all beyond the location of the aerodynamic centre on the panel, and it says that the trim consequence of variable sweep is set by where the pivot is put. That is the binding unknown the X-5 was built to address. Whether sweep helps was not in doubt, since [DeYoung 1947][research_deyoung_1947] had already supplied the span loading of wings of arbitrary sweep, aspect ratio, and taper, and the swept-wing fleet was flying. What was in doubt was whether an aircraft could absorb the consequence.

The NACA had been assembling the surrounding evidence for years. High-lift and stall-control devices on a 52 degree sweptback wing appear in [Foster and Fitzpatrick 1948][research_foster_1948], tip treatments in [Spearman and Becht 1948][research_spearman_1948], and the whole transonic design problem was gathered in the conference proceedings of [NACA 1949][research_naca_1949]. The question was live and the answer was mechanical.

## Programme Origin

The aircraft begins with a captured one.

The [Messerschmitt P.1101][ref_p1101] was taken by American troops in April 1945 from the experimental facility at Oberammergau, as part of the technical exploitation effort recorded under [Operation Lusty][ref_operation_lusty], and shipped to the Bell Aircraft factory at Buffalo. It arrived incomplete and damaged. Its wing sweep was adjustable on the ground between 30, 40, and 45 degrees, which was a convenience for testing rather than an operational feature, and the aircraft was never intended to change sweep in the air.

Bell proposed to make the adjustment continuous and airborne. The Air Force ordered two aircraft, serials 50-1838 and 50-1839. The first was completed on 15 February 1951, and the two made their first flights on 20 June and 10 December 1951.

The configuration is small. A single [Allison J35-A-17A][ref_j35] turbojet of 4900 pounds thrust sits in the fuselage, giving

$$T = 4900 \times 4.4482 = 2.18 \times 10^{4} \ \text{newtons}, \qquad \frac{T}{W} = \frac{2.18 \times 10^{4}}{4479 \times 9.80665} = 0.50$$

against a gross weight of 9875 pounds, or 4479 kilograms. The wing area is 175 square feet, or 16.26 square metres, and the wing sweeps to three detented positions at 20, 40, and 60 degrees. The wing section is a [NACA 64A011][ref_naca_airfoil] at the root thinning to a 64A08.28 at the tip. Span at the low setting is 33 feet 6 inches, or 10.21 metres, and at the high setting 20 feet 9 inches, or 6.32 metres.

The mass fractions follow from the empty weight of 6350 pounds,

$$\frac{m_{\text{empty}}}{m_{\text{gross}}} = \frac{2880}{4479} = 0.643, \qquad \frac{m_{\text{fuel}} + m_{\text{payload}}}{m_{\text{gross}}} = 0.357$$

which is a heavy empty fraction for a small jet and is where the pivot, its carry-through, and the translation mechanism are hiding. The wing loading follows,

$$\frac{W}{S} = \frac{4479 \times 9.80665}{16.26} = 2702 \ \text{newtons per square metre}$$

which is unremarkable and deliberately so. The aircraft was not built to go fast. It reached about Mach 0.9 and 40,000 feet, which is enough to make the sweep question meaningful and not enough to add a second question on top of it. That restraint is the same judgement the [X-4][related_post_a301_northrop_x4] shows and the [X-3][related_post_a300_douglas_x3] does not.

## Sizing From First Principles

The keystone relationship is the aerodynamic centre travel, and the X-5's own published dimensions are enough to compute it.

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

or **18.7 percent of the semi-span**. That is an inboard pivot, close against the fuselage, and it is the design decision that determines everything that follows. The number is not quoted from a source. It is recovered from two spans and a cosine, and it can be checked by anyone with the same two spans.

### What the Inboard Pivot Costs

The aerodynamic centre of a tapered panel lies near the spanwise station of its mean aerodynamic chord, which for a straight-tapered panel of taper ratio $\lambda$ is

$$\frac{y_{\text{mac}}}{L} = \frac{1}{3} \, \frac{1 + 2\lambda}{1 + \lambda}$$

returning 0.41 at a taper ratio of 0.3 and 0.44 at 0.5. This article uses forty percent, which is slightly inboard of that range and therefore slightly conservative, so

$$s_{ac} \approx 0.40 \, L = 0.40 \times 4.42 = 1.77 \ \text{metres}$$

and the travel between the extreme sweep settings follows from the relation derived above,

$$\Delta x_{ac} = 1.77 \times \left( \sin 60^\circ - \sin 20^\circ \right) = 1.77 \times \left( 0.8660 - 0.3420 \right) = 0.93 \ \text{metres}$$

The estimate is worth a sensitivity statement, since $s_{ac}$ is the one assumed quantity in the chain. The travel is linear in it,

$$\frac{\partial \left( \Delta x_{ac} \right)}{\Delta x_{ac}} = \frac{\partial s_{ac}}{s_{ac}}$$

so the seven percent spread in the taper-ratio relation above propagates to $0.93 \pm 0.07$ metres. Nothing in the argument turns on the difference. That figure means nothing until it is referred to a chord. The mean chord follows from the area and the unswept span,

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

which for an uncompensated aerodynamic centre travel of 0.58 chords is empty. **There is no single centre-of-gravity position at which an uncompensated X-5 is flyable at both sweep extremes.** That is the formal statement of why a mechanism was unavoidable given the pivot Bell had chosen.

### The Fix, and Why It Is Not a Fix

Bell's answer was to translate the wing forward as it swept aft. A [jackscrew][ref_jackscrew] assembly drove the pivot along short horizontal rails, with disc brakes locking the wing at each detent. The required translation to null the aerodynamic centre travel exactly is, by construction,

$$\Delta x_{\text{translate}} = -\Delta x_{ac} = -0.93 \ \text{metres}$$

which is three feet of fore-and-aft motion of the entire wing, through a structure that must simultaneously carry the wing bending moment. The rails were short and the compensation was partial. The residual is what the flight programme had to measure, and it is why [Finch and Walker 1953][research_finch_1953_2] is a report about the *boundaries* of static longitudinal stability rather than about a single value.

There is a cleaner way to state what Bell got wrong, and the whole subsequent history of variable sweep is contained in it. Suppose the pivot is moved outboard, so that a fixed inboard glove carries a fraction $f$ of the wing lift and does not move at all. The wing's aerodynamic centre is then an average weighted by lift share,

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

taking the X-5's 0.58 chords of travel down to 0.19, which is a large static margin change but no longer an impossible one, and that is the difference between a mechanism and a design. Nobody knew this in 1948. It was found at Langley in the decade that followed, and the finding is the subject of [Henderson and Ray 1964][research_henderson_1964], which varies pivot location explicitly and reports what it does to the longitudinal characteristics.

### Everything Else That Sweep Changes

The aerodynamic centre is the binding problem but it is not the only one. Sweeping the X-5's wing also shortens the span, and since the reference area is fixed, the aspect ratio collapses,

$$A(\Lambda) = \frac{b(\Lambda)^2}{S} = \frac{4 \left( y_p + L \cos \Lambda \right)^2}{S}$$

Evaluating at the three detents,

$$A(20^\circ) = 6.41, \qquad A(40^\circ) = 4.63, \qquad A(60^\circ) = 2.46$$

so the aircraft's aspect ratio falls by a factor of 2.6 across the sweep range. The lift-curve slope responds to both changes together, since the standard estimate depends on aspect ratio and sweep jointly,

$$C_{L\alpha} = \frac{2 \pi A}{2 + \sqrt{ \dfrac{A^2 \beta_s^2}{\kappa^2} \left( 1 + \dfrac{\tan^2 \Lambda_{c/2}}{\beta_s^2} \right) + 4 }}, \qquad \beta_s = \sqrt{1 - M^2}$$

Taking the quoted sweep angles as half-chord sweep, which is an approximation and is stated as one, and evaluating at low Mach number,

$$C_{L\alpha}(20^\circ) = 4.42, \qquad C_{L\alpha}(40^\circ) = 3.48, \qquad C_{L\alpha}(60^\circ) = 2.11 \ \text{per radian}$$

giving a ratio across the range of

$$\frac{C_{L\alpha}(20^\circ)}{C_{L\alpha}(60^\circ)} = \frac{4.42}{2.11} = 2.09$$

**The pilot can halve his own lift-curve slope with a lever.** Every derivative that contains $C_{L\alpha}$ moves with it, which is to say almost every derivative the aircraft has.

The benefit appears at the slow end. Maximum lift coefficient falls roughly with the cosine of sweep, so

$$C_{L,\max}(\Lambda) \approx C_{L,\max}(0) \cos \Lambda$$

and the stall speed follows,

$$V_{\text{stall}} = \sqrt{\frac{2 W}{\rho S C_{L,\max}}}$$

Evaluating with a maximum lift coefficient of 1.20 at the low sweep setting and scaling by cosine,

$$V_{\text{stall}}(20^\circ) = 60.6 \ \text{metres per second}, \qquad V_{\text{stall}}(60^\circ) = 83.1 \ \text{metres per second}$$

a rise of 37 percent. The drag-divergence side of the trade can be evaluated on the same footing using the Korn relation, which carries sweep, thickness, and lift coefficient together,

$$M_{dd} = \frac{\kappa_A}{\cos \Lambda} - \frac{\left( t/c \right)_{\text{stream}}}{\cos^2 \Lambda} - \frac{C_L}{10 \cos^3 \Lambda}$$

with $\kappa_A$ near 0.87 for a conventional section. Evaluating at a lift coefficient of 0.3 with the streamwise thickness ratios derived above,

$$M_{dd}(20^\circ) = 0.765, \qquad M_{dd}(40^\circ) = 0.916, \qquad M_{dd}(60^\circ) = 1.27$$

The last figure is beyond the relation's range of validity and is quoted only to show the sense of the trend. The first two are the interesting ones. **The X-5 reached about Mach 0.9, which is above the drag-rise Mach number of its own unswept setting and at the drag-rise Mach number of its middle one.** The aircraft could not have reached its top speed at low sweep. Sweeping was not a refinement of the performance. It was the performance.

Stated the other way at the slow end, which is the way the designer cares about, unsweeping the wing for the approach reduces the landing speed by more than a quarter. That is the entire commercial argument for variable sweep, and it is worth what it is worth because landing speed drives runway length, tyre and brake energy, and the survivability of an approach flown badly. The energy a brake must absorb scales as the square of the touchdown speed,

$$E_{\text{brake}} \approx \frac{1}{2} m V_{\text{td}}^2$$

so a 27 percent reduction in speed is a 47 percent reduction in the energy the aircraft arrives with.

The bill for all of this arrives in induced drag, which depends on the span and therefore on the sweep,

$$C_{D,i} = \frac{C_L^2}{\pi A e} = \frac{C_L^2 S}{\pi b^2 e}$$

Evaluating at a lift coefficient of 0.3 and a span efficiency of 0.85,

$$C_{D,i}(20^\circ) = 0.0053, \qquad C_{D,i}(60^\circ) = 0.0137$$

a factor of 2.61. That number should look familiar, and it will appear again in the section on the spin. **The induced drag penalty and the spin-recovery penalty of sweeping this wing are numerically identical, because both quantities carry the span squared in a denominator and the sweep lever is a span lever.** One geometric fact produces a performance cost and a safety cost of exactly the same size.

### Sweep Is a Trim Problem, Not a Dynamics Problem

One number decides how the pilot experiences all of this, and it is the rate. The X-5 moved from full extension to full sweep in less than thirty seconds, so

$$\dot{\Lambda} \approx \frac{40^\circ}{30 \ \text{s}} = 1.33 \ \text{degrees per second}$$

and the aerodynamic centre therefore drifts at

$$\dot{x}_{ac} = \frac{0.93 \ \text{m}}{30 \ \text{s}} = 3.1 \ \text{centimetres per second}$$

Compare that with the timescale of the aircraft's own longitudinal response. The short period frequency and damping are

$$\omega_{sp} \approx \sqrt{-M_\alpha}, \qquad M_\alpha = \frac{q S \bar{c} \, C_{m\alpha}}{I_y}, \qquad \zeta_{sp} = -\frac{M_q + M_{\dot\alpha} + Z_\alpha / V}{2 \omega_{sp}}$$

and for an aircraft of this class at its test condition the short period sits near 3 radians per second, giving a period near two seconds. The ratio of timescales is therefore

$$\frac{\tau_{\text{sweep}}}{T_{sp}} \approx \frac{30}{2} = 15$$

The comparison can be made a criterion rather than an observation. The aircraft experiences the geometry change as quasi-static when the stability perturbation the sweep produces in one short-period cycle is small against the margin itself,

$$\epsilon_{qs} = \frac{1}{SM} \frac{\partial \left( x_{ac} / \bar{c} \right)}{\partial \Lambda} \dot{\Lambda} \, \frac{2\pi}{\omega_{sp}} \ll 1$$

and with the X-5's numbers, a margin of 0.05, a sensitivity of 0.58 chords over 40 degrees, a rate of 1.33 degrees per second, and a period of 2.1 seconds,

$$\epsilon_{qs} = \frac{1}{0.05} \times 0.0145 \times 1.33 \times 2.1 = 0.81$$

which is below unity but not comfortably, and which says the pilot was retrimming continuously rather than ignoring the change. **The sweep transient is fifteen times slower than the mode it perturbs.** That inequality is the reason the X-5 was flyable at all. The aircraft never experiences a step change in its own stability. It experiences a slow drift that the pilot trims out continuously, in the same way he trims out a fuel burn, and the formal statement is that the sweep change is quasi-static with respect to the rigid-body dynamics. Had the mechanism been ten times faster the aircraft would have needed a control system nobody could have built in 1951.

This is worth stating as a general result because it is the one part of the X-5's answer that transferred without modification. Variable geometry is tractable when the geometry changes slowly compared with the vehicle's own modes, and it is a control problem of a different and harder kind when it does not. The modern treatments cited below are largely about the harder case.

## Dependent Systems

### The Pivot and What Passes Through It

Every pound of lift on the movable panel is carried to the fuselage through one bearing.

The panel root bending moment at load factor $n$ is the panel lift acting at its centre of pressure,

$$M_{\text{pivot}} = n \, L_{\text{panel}} \, s_{cp}$$

with $L_{\text{panel}}$ the lift carried by one movable panel and $s_{cp}$ the spanwise distance from pivot to panel centre of pressure. Taking the panels to carry about sixty percent of the total lift between them, one panel at a design load factor of seven carries

$$L_{\text{panel}} = 0.5 \times 0.60 \times 43{,}926 \times 7 = 9.22 \times 10^{4} \ \text{newtons}$$

and with the centre of pressure at the same forty percent of panel length used above,

$$M_{\text{pivot}} = 9.22 \times 10^{4} \times 1.77 = 1.63 \times 10^{5} \ \text{newton metres}$$

That moment must pass through a joint that also has to rotate under load. A fixed wing carries its root moment through a continuous spar carry-through, which is the most efficient structure available, a beam in bending. A pivoting wing must replace that beam with a pin, and the pin must be sized for the moment while the surrounding structure must be sized for the reaction couple the pin imposes. The reaction on the bearing separated by a structural depth $h$ is

$$F_{\text{bearing}} = \frac{M_{\text{pivot}}}{h}$$

so a shallow fuselage multiplies the load. With a structural depth of half a metre the reaction is

$$F_{\text{bearing}} = \frac{1.63 \times 10^{5}}{0.5} = 3.26 \times 10^{5} \ \text{newtons}$$

which a lug of 0.10 metre pin diameter and 0.05 metre thickness carries at a bearing stress of

$$\sigma_{br} = \frac{F}{d \, t} = \frac{3.26 \times 10^{5}}{0.10 \times 0.05} = 65 \ \text{megapascals}$$

with the pin itself in double shear at

$$\tau = \frac{F}{2 \left( \pi d^2 / 4 \right)} = 21 \ \text{megapascals}$$

Neither figure is alarming for steel, which is the point worth making. **The pivot is not hard because the stresses are high. It is hard because the joint must carry them while rotating, repeatedly, without developing the free play that would turn a stiffness into a mechanism.** A bearing clearance $\delta$ at radius $s_{ac}$ registers as a sweep error,

$$\Delta \Lambda_{\text{slop}} \approx \frac{\delta}{s_{ac}}$$

so a millimetre of wear is 0.03 degrees of asymmetry between the panels, and asymmetric sweep is a rolling moment the pilot did not command. The bearing must also be stiff, because a joint that deflects under load changes the effective sweep and therefore the aerodynamics, which is the aeroelastic coupling treated in [Goetz and Stonesifer 1961][research_goetz_1961] and [Gurley and Ruhlin 1962][research_gurley_1962] and pursued in the component studies of [Abel et al 1966][research_abel_1966].

The mass penalty follows from the same argument and it is the reason variable sweep is now rare. Writing the structural mass fraction as a baseline plus a variable-geometry increment,

$$\frac{m_{\text{struct}}}{m_{\text{gross}}} = \left( \frac{m_{\text{struct}}}{m_{\text{gross}}} \right)_{\text{fixed}} + \Delta_{\text{VG}}$$

the increment is conventionally quoted at a few percent of gross mass, which for an aircraft of the X-5's size is of order

$$\Delta m = 0.03 \times 4479 = 134 \ \text{kilograms}$$

and it buys nothing at any single flight condition. It buys the ability to be at two flight conditions well, and whether that is worth carrying depends entirely on how much of the mission is spent at each. The break-even condition can be written down. Let $\phi_i$ be the fraction of the mission flown at condition $i$ and $\Delta \left( L/D \right)_i$ the improvement variable sweep buys there. The configuration pays for itself when the weighted aerodynamic gain exceeds the mass penalty expressed as an equivalent range loss,

$$\sum_i \phi_i \frac{\Delta \left( L/D \right)_i}{\left( L/D \right)_i} > \frac{\Delta m_{\text{VG}}}{m_{\text{fuel}}}$$

which follows from the Breguet form,

$$R = \frac{V}{c_t} \frac{L}{D} \ln \frac{m_i}{m_f}$$

and which is a mission question rather than an aerodynamic one. **A vehicle that spends most of its life at one condition can never justify a mechanism that helps at two.** That inequality, and not any aerodynamic discovery, is what eventually retired the variable-sweep fighter. The [aeroelastic][ref_aeroelasticity] and flutter consequences are a separate charge on the same account, treated for swept wings generally by [Housner and Stein 1974][research_housner_1974].

### Trim, and the Longitudinal Consequences of Moving the Wing

The translating mechanism converts a stability problem into a trim problem, imperfectly.

With partial compensation the residual aerodynamic centre travel is some fraction $\eta_c$ of the uncompensated value,

$$\Delta x_{ac,\text{residual}} = \left( 1 - \eta_c \right) \Delta x_{ac}$$

and the trim moment the tail must absorb at lift coefficient $C_L$ is

$$\Delta C_m = C_L \frac{\Delta x_{ac,\text{residual}}}{\bar{c}}$$

which the elevator must supply through its control power,

$$\delta_e = \frac{\Delta C_m}{\left| C_{m \delta_e} \right|}$$

Even a mechanism achieving eighty percent compensation leaves 0.19 metres, or 12 percent of chord, of residual travel, which at a cruise lift coefficient of 0.3 demands a trim moment increment of 0.035 and several degrees of elevator. That moment is carried by a tail load, and the load is worth putting a number on,

$$L_t = \frac{\Delta C_m \, q \, S \, \bar{c}}{l_t}$$

At Mach 0.9 and 40,000 feet the dynamic pressure is 10,633 pascals, so with a tail arm of 4.5 metres

$$L_t = \frac{0.035 \times 10{,}633 \times 16.26 \times 1.592}{4.5} = 2.14 \times 10^{3} \ \text{newtons}$$

or **4.9 percent of the aircraft's weight carried by the tail purely to trim out what the mechanism failed to cancel**. That load is not free either, since a trimming tail load induces its own drag,

$$\Delta C_{D,\text{trim}} = \frac{C_{L_t}^2}{\pi A_t e_t} \frac{S_t}{S}$$

The horizontal tail is therefore working continuously against the wing position, and it is no accident that a large fraction of the X-5's primary literature is tail load measurement. [Rogers and Dunn 1952][research_rogers_1952] give preliminary horizontal tail loads and [Reed 1955][research_reed_1955] the measurements at 58.7 degrees of sweep, with the corresponding wing loads in [Banner et al 1955][research_banner_1955]. The same measurement problem on a fixed-wing research aircraft appears in [Stephenson 1956][research_stephenson_1956] for the [X-3][related_post_a300_douglas_x3], which makes a useful comparison because the X-3's tail loads are a function of one variable and the X-5's are a function of two.

The neutral point itself is the sum of wing and tail contributions,

$$\frac{x_{np}}{\bar{c}} = \frac{x_{ac,\text{wing}}}{\bar{c}} + V_H \frac{C_{L\alpha_t}}{C_{L\alpha_w}} \left( 1 - \frac{d\varepsilon}{d\alpha} \right), \qquad V_H = \frac{S_t l_t}{S \bar{c}}$$

and every term on the right is a function of sweep. The wing aerodynamic centre moves, as derived. The wing lift-curve slope in the denominator falls by a factor of two, which *increases* the tail's relative contribution. The downwash derivative depends on wing aspect ratio,

$$\frac{d\varepsilon}{d\alpha} \approx \frac{2 C_{L\alpha_w}}{\pi A}$$

and at the three sweep settings this returns 0.44, 0.48, and 0.55, so the tail loses incidence as the wing sweeps even as it gains relative authority. These effects do not cancel and there is no reason they should. The static longitudinal stability the aircraft actually exhibited across the range is the subject of [Finch and Walker 1953][research_finch_1953_2], with the broader stability and control picture in [Finch and Briggs 1953][research_finch_1953] and the dynamic behaviour at high sweep in [Videan 1955][research_videan_1955].

Ground testing had prepared the ground. The quarter-scale model work of [Kemp and Becht 1950][research_kemp_1950] covers lateral and directional characteristics, [Becht 1950][research_becht_1950] the landing configuration, and [Kemp and Few 1951][research_kemp_1951] the pressure distribution, which is the measurement from which an aerodynamic centre is actually obtained rather than assumed.

### Sweep as a Scheduling Variable

An aircraft whose derivatives are functions of a commanded parameter is an aircraft with a family of dynamics rather than one set.

Write the linearized longitudinal system in the usual state-space form,

$$\dot{\mathbf{x}} = \mathbf{A}(\Lambda) \, \mathbf{x} + \mathbf{B}(\Lambda) \, \mathbf{u}$$

in which the plant matrices depend on sweep because the derivatives do. The short period frequency scales with the square root of the stability derivative,

$$\omega_{sp}(\Lambda) \propto \sqrt{ C_{L\alpha}(\Lambda) \, SM(\Lambda) }$$

and since both factors move with sweep, and in opposite senses under partial compensation, the frequency traverses a range rather than sitting at a point. Even granting the mechanism perfect compensation, so that the static margin is held at 0.05 throughout, the lift-curve slope alone moves the frequency by

$$\frac{\omega_{sp}(20^\circ)}{\omega_{sp}(60^\circ)} = \sqrt{\frac{C_{L\alpha}(20^\circ)}{C_{L\alpha}(60^\circ)}} = \sqrt{2.09} = 1.45$$

so the aircraft's natural frequency spans a factor of nearly one and a half across the sweep range with the trim problem entirely solved. A controller holding constant closed-loop behaviour across that range must vary its gains,

$$k(\Lambda) = k_0 \left( \frac{\omega_{sp}(\Lambda_0)}{\omega_{sp}(\Lambda)} \right)^2$$

which is gain scheduling written down, and which the X-5 implemented by carrying a pilot. The X-5 handled this the way 1951 handled everything, by putting a human in the loop and letting him adapt. The formal apparatus for the problem, in which a controller is scheduled against a measured configuration parameter, did not exist yet and is now routine. It is what makes the modern variable-geometry vehicles cited below tractable.

The lateral set moves too. Directional stiffness and yaw damping come from the fin,

$$C_{n\beta} = V_V \, C_{L\alpha_v} \, \eta_v, \qquad V_V = \frac{S_v l_v}{S b}, \qquad C_{n r, \text{fin}} = -2 \, \eta_v \, C_{L\alpha_v} V_V \frac{l_v}{b}$$

and the vertical tail volume coefficient contains the span in its denominator. **Sweeping the wing shortens the span and therefore increases the vertical tail volume coefficient**, which sounds like good news and is, in isolation. The [Dutch roll][ref_dutch_roll] frequency and the roll mode follow,

$$\omega_{dr} \approx \sqrt{\frac{q S b \, C_{n\beta}}{I_z}}, \qquad \tau_r = -\frac{2 I_x V}{q S b^2 C_{lp}}$$

both of which contain the span explicitly and therefore both of which the sweep lever moves. The dihedral effect $C_{l\beta}$ grows with sweep, since a swept wing in sideslip presents a smaller effective sweep to the advancing panel, and the standard first-order statement is

$$C_{l\beta,\text{sweep}} \approx -C_L \frac{\tan \Lambda}{2}$$

so that the rolling moment due to sideslip nearly quintuples between 20 and 60 degrees at fixed lift coefficient. An aircraft with strong dihedral effect and a fin of fixed area is an aircraft prone to a lightly damped Dutch roll, and the sideslip behaviour at high sweep is exactly what [Childs 1953][research_childs_1953] set out to measure. The lateral characteristics of variable-sweep configurations generally are treated in [Eckert and Maki 1973][research_eckert_1973], the rolling derivatives in [Gainer et al 1967][research_gainer_1967], and the dynamic derivatives across the transonic and supersonic range in [Kilgore 1971][research_kilgore_1971] and [Averett and Wright 1966][research_averett_1966].

### The Spin, and the Term With the Span Squared in It

The second aircraft was lost in a spin at 60 degrees of sweep, and the reason is derivable from the geometry already established.

A [spin][ref_spin] is an equilibrium, not a departure. The aircraft rotates about a vertical axis at a steady rate with one wing stalled more deeply than the other, and the equilibrium is set by a balance between aerodynamic and inertial moments. The inertial coupling terms in the Euler equations are the ones that matter,

$$I_x \dot{p} = \left( I_y - I_z \right) q r + L_{\text{aero}}$$

$$I_y \dot{q} = \left( I_z - I_x \right) r p + M_{\text{aero}}$$

$$I_z \dot{r} = \left( I_x - I_y \right) p q + N_{\text{aero}}$$

and in a developed spin the products $qr$, $rp$, and $pq$ are large. The NACA correlated spin and recovery behaviour against a non-dimensional grouping of the inertia differences, the natural one being

$$I_{\text{param}} = \frac{I_x - I_y}{m \, b^2}$$

which is negative for an aircraft carrying its mass along the fuselage rather than along the span. The equilibrium the parameter governs is a balance in which the aerodynamic yawing moment must cancel the inertial one,

$$N_{\text{aero}} = -\left( I_x - I_y \right) p q$$

and recovery requires the rudder to break that balance, so the criterion for a recoverable spin is that the available control moment exceed the inertial term,

$$\left| N_{\delta_r} \right| \delta_{r,\max} \, q S b > \left| I_x - I_y \right| p q$$

**The left side is aerodynamic and the right side is inertial, and sweeping the wing acts on both sides in the unfavourable direction**, since the span appears once on the left and the inertia difference is unchanged while the span it is normalized against has shrunk. Aircraft that are strongly fuselage-heavy in this parameter spin flat, spin fast, and recover poorly, because the inertial yawing moment that sustains the rotation grows while the aerodynamic moment available to oppose it does not. This correlation is the accumulated product of two decades of free-spinning-tunnel work, running from [Scudder and Seidman 1935][research_scudder_1935] through the wartime and postwar fleet in [Berman 1947][research_berman_1947], [Snyder 1947][research_snyder_1947], [Scher 1947][research_scher_1947], [Berman 1949][research_berman_1949], [Klinar and Jones 1949][research_klinar_1949], [Klinar and Wilson 1950][research_klinar_1950], and [Lee 1952][research_lee_1952], and continuing through [Burk and Healy 1955][research_burk_1955], [Bowman 1956][research_bowman_1956], and [Bowman and Healy 1959][research_bowman_1959].

Now apply it to the X-5. The moments of inertia are properties of the mass distribution and change only slightly with sweep, since the wing is a small part of the total mass and it moves only a metre. The span is not slightly changed. It falls from 10.21 metres to 6.32 metres. Since the span enters the parameter squared,

$$\frac{I_{\text{param}}(60^\circ)}{I_{\text{param}}(20^\circ)} = \left( \frac{b(20^\circ)}{b(60^\circ)} \right)^2 = \left( \frac{10.21}{6.32} \right)^2 = 2.61$$

Taking representative values for an aircraft of this class, a pitch inertia of $1.2 \times 10^{4}$ and a roll inertia of $4.0 \times 10^{3}$ kilogram square metres,

$$I_{\text{param}}(20^\circ) = -0.0171, \qquad I_{\text{param}}(60^\circ) = -0.0447$$

**Sweeping the wing back moves the aircraft a factor of 2.6 deeper into the fuselage-heavy regime, and it does so through the span alone.** The mass has not moved. The aerodynamics have not been consulted. The aircraft becomes harder to recover from a spin because the denominator of the correlating parameter is the square of a length the pilot is shortening.

The time available is not the constraint. A spinning aircraft descends at roughly the speed at which its high-incidence normal force balances weight,

$$V_d \approx \sqrt{\frac{2W}{\rho S C_N}} = \sqrt{\frac{2 \times 43{,}926}{1.225 \times 16.26 \times 1.2}} = 60.6 \ \text{metres per second}$$

and loses altitude per turn of

$$\Delta h_{\text{turn}} = V_d \frac{2\pi}{\Omega} = 60.6 \times \frac{2\pi}{2.0} = 190 \ \text{metres}$$

so an entry at 12,000 metres offers something like sixty turns before ground impact. **An irrecoverable spin is not one that runs out of altitude. It is one in which no control input available breaks the equilibrium**, and the extra turns simply confirm it.

The aerodynamic side of the recovery problem degrades in the same direction at the same time. Recovery requires the rudder to generate an anti-spin yawing moment, and at spin attitudes the fin sits in the wake of the horizontal tail. The NACA quantified this with the tail damping power factor, the product of a tail damping ratio and an unshielded rudder volume coefficient,

$$\text{TDPF} = \text{TDR} \times \text{URVC}$$

in which the unshielded rudder volume coefficient counts only the rudder area outside the horizontal tail's wake shadow. The dependence of rudder effectiveness on horizontal tail position in spin attitudes is precisely what [Stone and Burk 1947][research_stone_1947] measured, and the case of an aircraft with the horizontal surface placed badly is [Gale and Pumphrey 1950][research_gale_1950]. The X-5's tail was, by the accounts, poorly placed. Whether the specific spin that killed the second aircraft was predicted is treated below.

The remedy of last resort, a spin-recovery rocket, was itself a subject of NACA investigation in [Burk and Healy 1955][research_burk_1955], which is the sort of document whose existence tells you how seriously the problem was taken.

### Propulsion and Envelope

The single Allison J35 is the least interesting component and it is adequate.

Thrust lapses with altitude roughly as ambient pressure, with a ram recovery term,

$$\frac{T(h, M)}{T_{SL}} \approx \frac{p(h)}{p_{SL}} \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

and the atmosphere is the standard troposphere model,

$$T(h) = T_0 - \lambda h, \qquad p(h) = p_0 \left( \frac{T(h)}{T_0} \right)^{g / \lambda R}, \qquad a = \sqrt{\gamma R T}$$

The level-flight maximum follows from the thrust and drag balance,

$$M_{\max}^2 = \frac{2 T}{\gamma \, p \, S \, C_D}$$

and specific excess power governs the climb,

$$P_s = \frac{V \left( T - D \right)}{W}, \qquad h_e = h + \frac{V^2}{2g}$$

The aircraft reached about Mach 0.9 at 40,000 feet. The interesting propulsion observation is not about the engine but about the wing, since the drag polar itself is a function of sweep,

$$C_D(\Lambda) = C_{D0}(\Lambda) + \frac{C_L^2}{\pi A(\Lambda) e(\Lambda)}$$

with the aspect ratio in the induced term falling by a factor of 2.6 as the wing sweeps. **Sweeping back to reduce wave drag increases induced drag at the same time**, and the crossover between the two is what determines whether a given sweep setting is the right one at a given speed and altitude. The optimum sweep schedule is the locus where the derivative of total drag with respect to sweep vanishes,

$$\frac{\partial C_D}{\partial \Lambda} = 0$$

Carrying out the differentiation on the two-term polar makes the balance explicit, since the wave-drag term falls with sweep and the induced term rises,

$$\frac{\partial C_D}{\partial \Lambda} = \frac{\partial C_{D0}}{\partial \Lambda} + \frac{C_L^2}{\pi e} \frac{\partial}{\partial \Lambda} \left( \frac{1}{A(\Lambda)} \right) = 0$$

which is a curve in the Mach and lift coefficient plane rather than a set of three detents. The X-5's three positions are a coarse sampling of a continuous optimum, and the lift and drag actually achieved at the high setting are reported in [Bellman 1953][research_bellman_1953], with the fleet-wide comparison in [Bellman 1959][research_bellman_1959].

### Instrumentation

The programme measured loads and derivatives as functions of two independent variables rather than one, and that changes the size of the experiment.

A conventional flight test programme maps a derivative against Mach number and altitude. The X-5 must map every derivative against Mach number, altitude, and sweep, so the test matrix acquires a dimension. If a fixed-wing programme requires $N$ conditions to characterize a derivative to a given accuracy, then the variable-sweep programme requires

$$N_{\text{total}} = N \times n_\Lambda$$

conditions, with $n_\Lambda$ the number of sweep settings, which for the X-5 is three at minimum and more if intermediate positions are of interest. That is the honest reason the programme flew about two hundred times to answer one question.

The measurements themselves are strain-gauge based. Wing and tail loads are obtained by calibrating a set of bridges against known applied loads and then inverting the calibration in flight,

$$\mathbf{L} = \mathbf{C}^{-1} \boldsymbol{\varepsilon}$$

with $\boldsymbol{\varepsilon}$ the measured strains and $\mathbf{C}$ the calibration matrix. The accuracy of the result depends on the conditioning of that matrix as much as on the gauges, since the relative error in the recovered loads is bounded by the condition number times the relative error in the strains,

$$\frac{\left\| \delta \mathbf{L} \right\|}{\left\| \mathbf{L} \right\|} \le \kappa(\mathbf{C}) \, \frac{\left\| \delta \boldsymbol{\varepsilon} \right\|}{\left\| \boldsymbol{\varepsilon} \right\|}, \qquad \kappa(\mathbf{C}) = \left\| \mathbf{C} \right\| \left\| \mathbf{C}^{-1} \right\|$$

A badly conditioned calibration turns a one percent strain measurement into a ten percent load. For a pivoting wing the calibration must be repeated at each sweep setting, because the load path changes when the geometry does. Sweep angle itself becomes a measured quantity with an error budget, and its error propagates into every derivative through the geometry. Differentiating the lift-curve slope relation,

$$\frac{\partial C_{L\alpha}}{\partial \Lambda} \approx \frac{C_{L\alpha}(20^\circ) - C_{L\alpha}(60^\circ)}{\Lambda_2 - \Lambda_1} = \frac{4.42 - 2.11}{0.698} = 3.31 \ \text{per radian squared}$$

so a one degree error in recorded sweep is an error of between 1.3 and 2.7 percent in the lift-curve slope attributed to that point, the spread depending on where in the sweep range the point lies, and all of that before any aerodynamic uncertainty is considered. Uncertainty propagates in the standard way,

$$u_c^2(y) = \sum_i \left( \frac{\partial y}{\partial x_i} \right)^2 u^2(x_i)$$

Derivative extraction from the flight records used the methods of the period, with [Bird and Jaquet 1951][research_bird_1951] representative of the practice of computing lateral motions from measured derivatives, and the modern descendants beginning with the maximum likelihood and Newton-Raphson approaches of [Iliff and Taylor 1972][research_iliff_1972] and applied to a full aircraft in [Gilyard 1972][research_gilyard_1972]. Manoeuvre and buffet characterization of the sort the programme also required is described in [Ray et al 1972][research_ray_1972], and the buffet boundary practice of the era in [Rathert et al 1951][research_rathert_1951]. Loads statistics and their treatment appear in [Hamer et al 1961][research_hamer_1961] and the institutional gathering of the whole subject in the conference proceedings of [NACA 1957][research_naca_1957].

## The Flight Test Record

Two aircraft were built and about two hundred flights were made, to Mach 0.9 and 40,000 feet.

The first aircraft proved mechanically unreliable and made only ten flights. Walter Williams, who ran the NACA unit at Muroc, is quoted in the secondary literature calling it a lemon. The second aircraft was delivered during the resulting pause, proved far more reliable, and made twenty contractor flights. Both were turned over to the Air Force and the NACA in February 1950 by one account and 1952 by the chronology of the flights themselves, which is one of several dating inconsistencies in the secondary record. Air Force pilots including [Chuck Yeager][ref_yeager] flew a short evaluation series, and the NACA programme followed with [Scott Crossfield][ref_crossfield] among the pilots.

The aircraft demonstrated what it was built to demonstrate. Sweep could be changed in flight, the trim consequence was absorbable, and the low-speed benefit was real. [Finch and Briggs 1953][research_finch_1953] report the stability and control investigation, [Finch and Walker 1953][research_finch_1953_2] the static longitudinal stability boundaries at 59 degrees, [Childs 1953][research_childs_1953] the sideslip behaviour, [Bellman 1953][research_bellman_1953] the lift and drag, and [Videan 1955][research_videan_1955] the dynamic lateral and longitudinal stability, with the load measurements of [Rogers and Dunn 1952][research_rogers_1952], [Reed 1955][research_reed_1955], and [Banner et al 1955][research_banner_1955] alongside. That is a dense and complete primary record for an aircraft that flew two hundred times, and it is denser than the [X-4][related_post_a301_northrop_x4]'s.

On 13 October 1953 the second aircraft failed to recover from a spin at 60 degrees of sweep and was destroyed. The pilot, an Air Force major named Raymond Popson, was killed. The surviving aircraft continued flying at Edwards until 1955 and served as a chase aircraft until 1958, when it went to the National Museum of the United States Air Force, where it remains.

The accident ended more than the aircraft. Tentative Air Force interest in developing the configuration into a low-cost tactical fighter for allied air forces did not survive it, which is a reasonable response to an aircraft with an irrecoverable spin mode and an unreasonable one to variable sweep as an idea. The distinction between the two is the subject of the next two sections.

## Comparison With Ground Prediction

The X-5 is the case in this series where the ground facilities had the most complete prior picture and the flight programme still found something they had not.

The low-speed aerodynamics were predicted well. Quarter-scale model results in [Kemp and Becht 1950][research_kemp_1950] and [Becht 1950][research_becht_1950] anticipated the lateral, directional, and landing behaviour, and the pressure work of [Kemp and Few 1951][research_kemp_1951] supplied the aerodynamic centre location directly rather than by inference. The influence of fuselage and tail surfaces on low-speed static stability had been mapped generally in [Bird et al 1952][research_bird_1952], the role of horizontal tail area and wing sweep in [Hayes and Sleeman 1959][research_hayes_1959], and tail height effects in [Fisher and Williams 1958][research_fisher_1958]. Chordwise fences and tail position, which are the standard remedies for the swept-wing pitch-up the X-5 also had to contend with, appear in [Queijo et al 1954][research_queijo_1954], with the flight evaluation of the pitch-up itself in [Anderson and Bray 1955][research_anderson_1955]. Boundary-layer stability as a function of sweep angle, which governs where the spanwise flow turns into transition, was measured by [Boltz et al 1960][research_boltz_1960].

The spin is the uncomfortable case. Free-spinning-tunnel technique was mature by 1951 and had been applied to essentially every American fighter prototype of the preceding decade, as the record above shows. A spin-tunnel investigation of the X-5 configuration would have been ordinary practice. No such report was located in the search behind this article, which is not evidence that none was performed. The most that can be said honestly is that the technique existed, the fleet-wide practice existed, the correlating parameter that this article uses to explain the accident was in use at the time, and the aircraft was nonetheless flown to a sweep setting at which the parameter had degraded by a factor of two and a half. Whether that was known and accepted, or not computed, the sources consulted do not say.

What ground facilities could not supply was the thing the programme actually delivered, which is not a number but a demonstration. The trim consequence of variable sweep was computable in 1948 by the same one-line relation used at the top of this article. What was not computable was whether an aircraft carrying that mechanism would be an aeroplane or a contraption, and that judgement is what a flying article settles. The same argument appears in the [X-4][related_post_a301_northrop_x4] treatment and it is the recurring answer to why programmes fly aircraft whose central numbers are already known.

## What the Data Changed

The X-5 validated the concept and invalidated the mechanization, and both halves mattered.

The concept propagated immediately. Langley took up variable sweep as a research subject and pursued it for a decade, and the resulting body of work is the reason the idea entered service. [Alford and Henderson 1959][research_alford_1959_2] is an exploratory low-speed investigation of variable-sweep configurations, with the multi-mission study of [Alford et al 1959][research_alford_1959] alongside it. The programme is summarized in progress by [Polhamus and Hammond 1960][research_polhamus_1960] and pursued through the configuration studies of [Spencer 1960][research_spencer_1960], [Foster and Morris 1960][research_foster_1960] at Mach 1.97, and [Bielat and Pierpont 1960][research_bielat_1960] at transonic speeds. The double-pivot variant appears in [Alford et al 1962][research_alford_1962] and the low-level supersonic configurations in [Alford et al 1966][research_alford_1966].

The decisive result is the pivot. **Moving the pivot outboard and leaving a fixed glove inboard reduces the aerodynamic centre travel by the product of two factors, as derived above, and it does so without any mechanism at all.** The design problem becomes a minimization over a single variable subject to a structural floor, since the pivot cannot be moved so far outboard that the panel it carries has no useful area,

$$\min_{y_p} \ \left| \Delta x_{ac}(y_p) \right| \quad \text{subject to} \quad S_{\text{movable}}(y_p) \ge S_{\min}$$

and the interior optimum exists because the travel falls quadratically with pivot station while the useful movable area falls only linearly. [Hammond and Henderson 1961][research_hammond_1961] investigate high-lift and lateral control on a semispan variable-sweep wing with an outboard pivot, [Henderson and Ray 1964][research_henderson_1964] vary the pivot location explicitly and report the longitudinal consequences, [Henderson and Ray 1965][research_henderson_1965] extend it to planform modification, and [Huffman 1972][research_huffman_1972] treats pivot location together with forewing configuration. [Hammond and Polhamus 1965][research_hammond_1965] and [Lamar and McKinney 1971][research_lamar_1971] fill in the surrounding aerodynamics. The idea was considered novel enough to patent, and both [Toll 1962][research_toll_1962] and [Hammond and Polhamus 1970][research_hammond_1970] hold patents on variable-sweep aircraft arising from this work.

Bell's translating mechanism therefore turned out to be the answer to a question that did not have to be asked. Bell had accepted an inboard pivot, inherited from the [P.1101][ref_p1101], and then engineered around the consequence. Langley moved the pivot and the consequence largely disappeared. That is a clean example of a design problem being dissolved rather than solved, and it is the most transferable lesson of the programme.

The consolidated statement of the whole arc is [NACA 1966][research_naca_1966], which is explicitly a summary of the research and development leading to the [F-111][ref_f111], with the development support recorded in [NACA 1966][research_naca_1966_2] and the spin behaviour of the resulting aircraft in [Bowman and White 1974][research_bowman_1974]. The retrospective by two of the principals is [Polhamus and Toll 1981][research_polhamus_1981], which is the document to read if only one is to be read.

The service aircraft followed. The [F-111][ref_f111], the [F-14][ref_f14], the [Panavia Tornado][ref_tornado], the [B-1][ref_b1_lancer], the [MiG-23][ref_mig23] and [MiG-27][ref_mig27], the [Su-17][ref_su17] and [Su-24][ref_su24], and the [Tu-22M][ref_tu22m] and [Tu-160][ref_tu160] all carry outboard-pivot variable sweep. The supersonic transport application, which did not proceed, is represented by [Lockwood 1966][research_lockwood_1966] on pitch-up with a high-aspect-ratio variable-sweep wing.

Then it stopped. No new variable-sweep combat aircraft has entered development since the 1980s, and the reason is that every term in the inequality above moved.

The approach speed the mechanism existed to reduce is set by wing loading and maximum lift together, and both were attacked directly. A [leading-edge slat][ref_slat] and a manoeuvre flap recover the lift that sweep costs without moving the wing,

$$C_{L,\max} = C_{L,\max}^{\text{clean}} \cos \Lambda + \Delta C_{L,\text{slat}} + \Delta C_{L,\text{flap}}$$

and increments of 0.5 to 0.8 from such devices restore at 45 degrees of fixed sweep most of what the X-5 bought by unsweeping to 20. Engine thrust removed the rest of the pressure, since the approach itself can be flown at higher wing loading when thrust is available to arrest a sink rate, and the field length that wing loading drives scales as

$$s_{\text{field}} \propto \frac{W/S}{\sigma \, C_{L,\max} \left( T/W \right)}$$

so a thrust-to-weight ratio that rose from the X-5's 0.50 toward unity halves the field length at fixed wing loading and buys back the whole of the variable-sweep argument. Digital flight control then removed the handling penalties that had made highly swept fixed wings unpleasant, which is to say it made the numerator of the mass-penalty inequality smaller by making a fixed compromise acceptable rather than by improving the compromise. Substituting into the break-even condition, a configuration whose aerodynamic gain has been halved while its structural penalty is unchanged fails the test,

$$\sum_i \phi_i \frac{\Delta \left( L/D \right)_i}{\left( L/D \right)_i} \ \longrightarrow \ \text{halved}, \qquad \frac{\Delta m_{\text{VG}}}{m_{\text{fuel}}} \ \longrightarrow \ \text{unchanged}$$

The variable-sweep wing was a mechanical solution to a problem later solved aerodynamically and electronically, and it was abandoned for the reason good engineering solutions usually are, which is that the problem changed.

## The Contemporary Literature

Variable geometry did not die. It changed scale and it changed name, and the modern literature is large.

The direct descendant is the variable-sweep morphing unmanned aircraft, small enough that the mass penalty of a pivot is affordable and autonomous enough that the changing dynamics can be scheduled rather than flown. [Dai et al 2020][research_dai_sweep_2020] design and analyse such a configuration, and [Dai et al 2021][research_dai_mpc_2021] close a nonlinear model predictive controller around it, which is the modern answer to the scheduling problem the X-5 handed to its pilot. [Li et al 2020][research_li_varsweep_2020] simulate the aerodynamics of the same class of vehicle and [Guo et al 2020][research_guo_unsteady_2020] treat the unsteady flow during the sweep transient itself, which is the regime the X-5 avoided by moving slowly. [Ma et al 2021][research_ma_bionic_2021] analyse the stability of a multi-section variable-sweep wing and design augmentation for it, and [Gao et al 2022][research_gao_tandem_2022] treat the mode transition of a tandem-wing vehicle with variable sweep, where the configuration change is large enough that the transition is itself a flight phase.

The transient is where the modern work departs from the X-5 entirely. The quasi-static inequality derived above fails when the geometry changes on the timescale of the vehicle's own modes, and then the equations of motion acquire terms the fixed-geometry treatment does not have. Both the inertia tensor and the aerodynamic coefficients become explicit functions of time through the shape parameter,

$$\frac{d}{dt} \left( \mathbf{I}(\Lambda) \, \boldsymbol{\omega} \right) = \mathbf{I}(\Lambda) \dot{\boldsymbol{\omega}} + \frac{\partial \mathbf{I}}{\partial \Lambda} \dot{\Lambda} \, \boldsymbol{\omega} + \boldsymbol{\omega} \times \mathbf{I}(\Lambda) \boldsymbol{\omega}$$

in which the middle term exists only while the wing is moving and vanishes at every detent. That term is exactly what the X-5's thirty-second transit made negligible and what a fast morphing vehicle cannot ignore. The actuation is not free either, since the hinge must work against the aerodynamic moment about the pivot,

$$P_{\text{act}} = M_{\text{hinge}} \dot{\Lambda}, \qquad E_{\text{act}} = \int_{\Lambda_1}^{\Lambda_2} M_{\text{hinge}}(\Lambda) \, d\Lambda$$

so speed costs power linearly and the energy is set by the load, which is why fast morphing is easy on a small vehicle and hard on a large one. The aeroelastic and dynamic response during the change must then be solved rather than assumed. [Changchuan et al 2022][research_changchuan_2022] compute the aeroelastic response of a folding wing *during* the morphing process, [Zhou and Huang 2021][research_zhou_huang_2021] build reduced-order models for nonlinear aeroelastic analysis of a morphing wing, and [Tsushima et al 2019][research_tsushima_2019] treat geometrically nonlinear static aeroelasticity of composite morphing wings. [Chiarelli and Bonomo 2019][research_chiarelli_2019] examine flutter and flutter-buffet on a swept wing, which is the failure mode a pivot joint most threatens.

Span change is the other axis, and it is the one the X-5 got for free as a side effect. [Elelwi et al 2020][research_elelwi_span_2020] compare variable span-morphing of a tapered wing, with the structural sizing in [Elelwi et al 2021][research_elelwi_topology_2021] and the weight optimization in [Elelwi et al 2022][research_elelwi_weight_2022], which is the direct modern treatment of the mass penalty computed above. [Bishay et al 2019][research_bishay_2019] and [Geva et al 2019][research_geva_2019] develop span-morphing cores and combined span and aerofoil adjustment. Folding wingtips are a partial variable geometry with an explicit historical debt, and [Dussart et al 2019][research_dussart_xb70_2019] take their inspiration from the [XB-70][ref_xb70] directly, with the roll consequences in [Dussart et al 2019][research_dussart_roll_2019] and the gust load alleviation application in [Cheung et al 2020][research_cheung_folding_2020].

The mechanism problem has been reformulated. Where Bell used a jackscrew, rails, and disc brakes, the modern approach is to eliminate the joint. Compliant mechanisms deform rather than articulate, and [Kumar et al 2021][research_kumar_topology_2021] optimize the topology of contact-aided shape morphing compliant mechanisms while [You et al 2020][research_you_skin_2020] set design criteria for the skin such a wing needs. [Nazeer et al 2021][research_nazeer_2021] report sensing, actuation, and control of a complete morphing wing prototype in the tunnel, and [Keidel et al 2020][research_keidel_2020] measure the control authority a camber-morphing flying wing actually achieves, which is the question that decides whether morphing is a control system or a trim system. The aerodynamic optimization framing is [Klimczyk and Goraj 2019][research_klimczyk_2019] and [Traub 2019][research_traub_2019] supplies an experimental morphing annular wing. The [adaptive compliant wing][ref_compliant_wing] is the configuration these lines converge on.

The most striking modern result belongs to biology and it closes the circle exactly. Gulls change the sweep of their wings at the elbow and wrist, and in doing so they move the position of their own aerodynamic centre. [Harvey et al 2021][research_harvey_gull_2021] show that gull-inspired joint-driven wing morphing allows adaptive longitudinal flight control, and [Harvey and Inman 2022][research_harvey_inman_2022] establish that gull dynamic pitch stability is *controlled* by wing morphing. The aerodynamic centre travel that Bell spent a jackscrew, a set of rails, and three feet of translation trying to cancel is the quantity a gull uses as its longitudinal control input. **The X-5 treated the aerodynamic centre shift as the cost of variable sweep. The bird treats it as the point of it.**

That inversion can be given a number, and doing so is the cleanest way to see both its promise and its difficulty. Treat sweep as a control effector and give it a control derivative in the same form as an elevator's,

$$C_{m \Lambda} = \frac{\partial C_m}{\partial \Lambda} = -C_L \frac{s_{ac} \cos \Lambda}{\bar{c}}$$

which for the X-5 at mid sweep and a lift coefficient of 0.3 returns

$$C_{m \Lambda}(40^\circ) = -0.3 \times \frac{1.768 \times 0.766}{1.592} = -0.26 \ \text{per radian}$$

against a conventional elevator control power near $-0.7$ per radian. **Sweep is worth roughly a third of an elevator as a pitch effector**, which is a great deal of authority for a surface not intended as one. The obstacle is entirely rate. Producing the moment of a five degree elevator deflection requires

$$\Delta \Lambda = \frac{\left| C_{m \delta_e} \right| \delta_e}{\left| C_{m \Lambda} \right|} = \frac{0.7 \times 0.0873}{0.26} = 0.24 \ \text{radians}$$

or 13.7 degrees of sweep, and delivering it inside one short-period time constant of about 0.33 seconds demands

$$\dot{\Lambda}_{\text{required}} = \frac{13.7}{0.33} = 42 \ \text{degrees per second}$$

against the X-5's 1.33, **a factor of thirty-one**. A gull closes that gap with a wing weighing a few hundred grams and a joint driven by muscle. Whether an aircraft can be built on the same principle is an open question and the papers do not claim otherwise, but the gap is a rate gap rather than an authority gap, and that is a more tractable thing to be short of.

The other historical alternative also survives in the literature. An [oblique wing][ref_oblique_wing] pivots as a single panel about the fuselage centreline, which keeps the total lift distribution far more nearly fixed and avoids the paired-panel problem entirely at the cost of asymmetry in every other axis. [Hopkins 1975][research_hopkins_1975] examines wing bend on a low aspect ratio oblique wing, and [Yue et al 2019][research_yue_oblique_2019] design sliding mode control for an oblique wing aircraft during the skewing process, which is the same transient problem in a different geometry.

Spin research continued and has been reformulated as an optimal control problem. [Venkateswara Rao and Go 2019][research_rao_spin_2019] optimize spin recovery manoeuvres, [Salahudden and Ghosh 2021][research_salahudden_2021] design robust flat-spin recovery using optimally deflected surfaces, and [Kapuscinski et al 2020][research_kapuscinski_2020] address the measurement problem of determining aircraft state during recovery. High angle-of-attack aerodynamics of finite-span wings, which is the flow regime the X-5's accident occurred in, is treated by [Faure and Leogrande 2020][research_faure_2020]. Planform optimization as a design activity rather than a mechanism appears in [Jim et al 2021][research_jim_planform_2021] and [Dam et al 2022][research_dam_planform_2022], and aeroelastic planform design in [Hermanutz and Hornung 2020][research_hermanutz_2020]. The modern view is that if the planform can be chosen well enough by computation, the need to change it in flight recedes, which is the quiet reason variable sweep left the fighter fleet.

## Where the Framing Breaks Down

The keystone framework fits the X-5 awkwardly in three ways.

The central number was computable before the aircraft was built. The aerodynamic centre travel derived at the top of this article requires a pivot location and a panel geometry, and both were fixed the moment Bell chose to work from the [P.1101][ref_p1101] layout. An instrument model that treats a research aircraft as reducing uncertainty about a physical quantity struggles when the quantity was arithmetic. What the aircraft reduced uncertainty about was whether the resulting machine would be flyable, which is a different kind of proposition and one the framework prices badly.

The programme's most valuable output was a negative finding about its own solution. The X-5 demonstrated that in-flight sweep change works and that Bell's way of doing it was the wrong way. A framework that scores a programme by what it settled must handle the case where the settled thing is the programme's own approach, and where the eventual answer came from a wind tunnel at a different institution five years later. The X-5 is best understood as having established the value of a problem rather than the value of a solution.

The fatal accident sits outside the keystone entirely. The spin that destroyed the second aircraft is attributable to tail placement and inertia distribution, and the sweep-dependence derived above sharpens it without originating it. An aircraft with the same tail and the same inertias and a fixed short-span wing would have had a similar problem. Variable sweep made it worse by a computable factor and did not cause it. A framework organized around a single research question will tend to absorb an accident into that question, and here that would be wrong.

## The Source Base

The primary record is unusually good for an aircraft that flew two hundred times. The flight reports are [Finch and Briggs 1953][research_finch_1953], [Finch and Walker 1953][research_finch_1953_2], [Childs 1953][research_childs_1953], [Bellman 1953][research_bellman_1953], and [Videan 1955][research_videan_1955], with the load measurements in [Rogers and Dunn 1952][research_rogers_1952], [Reed 1955][research_reed_1955], and [Banner et al 1955][research_banner_1955]. The model work that preceded flight is [Kemp and Becht 1950][research_kemp_1950], [Becht 1950][research_becht_1950], and [Kemp and Few 1951][research_kemp_1951], with the later gust-alleviation study of [Croom and Huffman 1957][research_croom_1957] using the same model. The variable-sweep development literature that followed is large and is cited at length above, with [Polhamus and Toll 1981][research_polhamus_1981] and [NACA 1966][research_naca_1966] the two summary documents.

The secondary literature treats the aircraft briefly. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment, with [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1981][book_hallion_1981_on_the_frontier], [Hallion 1981][book_hallion_1981_test_pilots], [Gorn 2001][book_gorn_2001_expanding_envelope], and [Bilstein 1989][book_bilstein_1989_orders] supplying programme and institutional context, and [Gunston 1992][book_gunston_1992_faster_than_sound] and [Wolfe 1979][book_wolfe_1979_right_stuff] the wider and popular framing. [Chambers and Chambers 2008][book_chambers_2008_radical_wings] covers the unconventional configuration lineage.

The engineering texts behind the relations are [Etkin and Reid 1996][book_etkin_reid_1996], [Nelson 1998][book_nelson_1998], [Stengel 2004][book_stengel_2004], [Stevens and Lewis 2015][book_stevens_lewis_2015], [McRuer Ashkenas and Graham 1973][book_mcruer_ashkenas_graham_1973], and [Hurt 1965][book_hurt_1965] for flight dynamics, with [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2002][book_anderson_2002_modern_compressible], [Anderson 2012][book_anderson_2012_aircraft_performance], [Anderson 1997][book_anderson_1997_history_aerodynamics], [Bertin and Cummings 2013][book_bertin_cummings_2013], [Shapiro 1953][book_shapiro_1953], [Liepmann and Roshko 1957][book_liepmann_roshko_1957], [Ashley and Landahl 1965][book_ashley_landahl_1965], [Kuchemann 1978][book_kuchemann_1978], [Schlichting and Gersten 2017][book_schlichting_gersten_2017], and [White 2006][book_white_2006_viscous] for the aerodynamics. Design method is [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], [Roskam 1985][book_roskam_1985], [Stinton 2001][book_stinton_2001], and [Whitford 1987][book_whitford_1987], the last of which is the standard treatment of fighter configuration evolution and therefore of variable sweep as a design choice. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016], aeroelasticity [Bisplinghoff Ashley and Halfman 1955][book_bisplinghoff_ashley_halfman_1955], [Fung 1955][book_fung_1955], and [Dowell 2014][book_dowell_2014], and propulsion [Sutton and Biblarz 2016][book_sutton_biblarz_2016], [Hill and Peterson 1991][book_hill_peterson_1991], and [Huzel and Huang 1992][book_huzel_huang_1992]. Flight test practice is [Kimberlin 2003][book_kimberlin_2003] and [Ward Strganac and Niewoehner 2006][book_ward_strganac_niewoehner_2006], with error analysis in [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], the organizational reading [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error], and the information accounting [Cover and Thomas 2006][book_cover_thomas_2006] with design of experiments in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005], [Gelman et al 2013][book_gelman_et_al_2013], [Lindley 1956][research_lindley_1956], and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]. Sampling and channel capacity are [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948]. Tunnel and institutional histories are [Baals and Corliss 1981][book_baals_corliss_1981] and [Hansen 1987][book_hansen_1987_engineer_in_charge], the theoretical lineage [von Karman and Edson 1967][book_von_karman_edson_1967] and [Gorn 1992][book_gorn_1992_universal_man], and the thermal thread [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier], [Truitt 1960][book_truitt_1960], [Bertin 1994][book_bertin_1994_hypersonic], [Anderson 2006][book_anderson_2006_hypersonic], [Incropera and DeWitt][book_incropera_heat_transfer], [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and [Boley and Weiner 1960][book_boley_weiner_1960], with the X-15 and successor works [Jenkins 2007][book_jenkins_2007_x15], [Jenkins 2000][book_jenkins_2000_hypersonics], [Thompson 1992][book_thompson_1992_edge_of_space], [Launius and Jenkins 2012][book_launius_jenkins_2012], and [Merlin 2009][book_merlin_2009_blackbird].

Foundational primaries bearing on the arguments include [Williams and Drake][research_williams_drake_1948] on the research airplane rationale, [Buckingham 1914][research_buckingham_1914] on similarity, [Sutherland 1893][research_sutherland_1893] on viscosity, [Glauert 1928][research_glauert_1928] and [Prandtl 1928][research_prandtl_1928] on compressibility and the boundary layer, [Jones 1947][research_jones_1947] on planform, [Ackeret 1925][research_ackeret_1925] on supersonic lift, [NACA Report 1135][research_naca_1135] for the compressible relations, [Theodorsen 1935][research_theodorsen_1935], [Collar 1946][research_collar_1946], and [Garrick and Reed 1981][research_garrick_reed_1981] on aeroelasticity, [Phillips 1948][research_phillips_1948] on rolling coupling, [Beeler Bellman and Saltzman 1956][research_beeler_1956] on drag measurement, and [Wright 1936][research_wright_1936] on unit cost at these quantities. The wider configuration context appears in [James and Maki 1957][research_james_1957], [Quigley et al 1960][research_quigley_1960], [Whitcomb and Norton 1961][research_whitcomb_1961], [Cornette 1961][research_cornette_1961], [Funk and Cooney 1959][research_funk_1959], [Burk and Libbey 1961][research_burk_1961], [Lee 1964][research_lee_1964], [Lee and Healy 1964][research_lee_1964_2], [Hanson 1973][research_hanson_1973], [Bartlett et al 1973][research_bartlett_1973], and [Monfort and Whitcomb 1975][research_monfort_1975]. The equivalent problems at model scale are worked on this blog in [A118][related_post_a118_propulsion_sizing], [A120][related_post_a120_staged_boosted_propulsion], [A122][related_post_a122_stability_configuration], [A123][related_post_a123_dynamic_stability], and [A127][related_post_a127_structures_flight_envelope], the rocketplane lineage in [A96][related_post_a96_history_rocketplanes], large high-speed configurations in [A106][related_post_a106_two_stage_delta_wing], propellant chemistry in [A217][related_post_a217_rocket_propellant_chemistry], the computing and simulation infrastructure in [A237][related_post_a237_aerospace_framing] and [A241][related_post_a241_aerospace_simulation], and space policy in [A90][related_post_a90_intro_space_studies]. The [NASA Technical Reports Server][ref_ntrs] and the [NASA History Office][ref_nasa_x3_factsheet] hold the record, with the [Armstrong Flight Research Center][ref_nasa_armstrong] the institutional successor and the [wind tunnel][ref_wind_tunnel] and [flight test][ref_flight_test] literatures the methodological background.

## Epistemic State

Established historical fact includes the capture of the P.1101 in April 1945 and its delivery to Bell, its ground-adjustable sweep, the order for two aircraft with serials 50-1838 and 50-1839, the completion of the first on 15 February 1951, the first flights on 20 June and 10 December 1951, the three sweep detents at 20, 40, and 60 degrees, the jackscrew and rail mechanism with disc brake locking, the sweep transit time of under thirty seconds, the approximate flight total near two hundred, the maximum conditions near Mach 0.9 and 40,000 feet, the loss of the second aircraft in a spin at 60 degrees sweep on 13 October 1953 with the death of its pilot, the continued use of the first aircraft to 1955 and as a chase aircraft to 1958, and its preservation at the National Museum of the United States Air Force.

Established engineering analysis includes every relation in the sizing sections. The pivot recovery from two spans, the aerodynamic centre travel relation, the aspect ratio and lift-curve slope variation with sweep, the stall speed relation, the neutral point decomposition, the spin inertia parameter, the tail volume coefficients, and the drag polar decomposition are standard results applied to published dimensions.

**Derived here and not taken from a source** are the pivot station of 0.95 metres and 18.7 percent of semi-span, the movable panel length of 4.42 metres, the aerodynamic centre travel of 0.93 metres or 58 percent of mean chord, the lift-curve slope ratio of 2.09 across the sweep range, the stall speed pair of 60.6 and 83.1 metres per second, the pivot bending moment of $1.63 \times 10^{5}$ newton metres, and the factor of 2.61 by which the spin inertia parameter degrades between the sweep extremes. These follow by arithmetic from published spans, area, and weight, and any reader with those inputs can reproduce or refute them.

Inference includes the central claim that the sweep-dependence of the spin inertia parameter contributed to the loss of the second aircraft. The factor of 2.61 is arithmetic, but the attribution of the accident to it is an interpretation. The sources consulted attribute the spin to tail placement and to the aerodynamic layout generally, and this article's contribution is to observe that the correlating parameter the NACA itself used degrades sharply with sweep and that the accident occurred at the sweep setting where it is worst. That is consistent with the record rather than established by it.

Weakly supported are the representative values. The moments of inertia used in the spin parameter are plausible for an aircraft of this class rather than measured properties of this airframe, and the ratio between the two sweep settings is far more trustworthy than either absolute value, since the inertias cancel. The panel lift fraction of sixty percent, the aerodynamic centre at forty percent of panel length, the maximum lift coefficient of 1.20, and the structural mass increment of three percent are all representative figures. The taking of the quoted sweep angles as half-chord sweep in the lift-curve slope estimate is an approximation of unknown size.

Contested or unresolved in the sources consulted is the date on which the aircraft passed to the Air Force and the NACA, the pilot's rank, which appears variously, the exact flight total, given as approximately two hundred without a counting rule, and whether a spin-tunnel investigation of the X-5 configuration was performed before the loss. No such report was located, which is not the same as none existing.

A note on temporal position. This article carries an editorial date of 2025-10-11 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the [X-1][related_post_a298_bell_x1], [X-2][related_post_a299_bell_x2], [X-3][related_post_a300_douglas_x3], or [X-4][related_post_a301_northrop_x4] beyond the comparisons drawn, all of which have their own articles, nor the [X-15][ref_na_x15], which appears later. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficients, [lift-to-drag][ref_lift_to_drag], [Reynolds][ref_reynolds_number] and [Prandtl][ref_prandtl_number] numbers, [measurement uncertainty][ref_measurement_uncertainty] and its [propagation][ref_propagation_of_uncertainty], and the [standard atmosphere][ref_isa] in its [tabulated form][ref_us_standard_atmosphere].

It does not attempt a history of the [F-111][ref_f111] or the other production variable-sweep aircraft, which are named only as inheritors, nor of the [P.1101][ref_p1101] except as ancestor. It does not cover [shock waves][ref_shock_wave] and [oblique shocks][ref_oblique_shock], [wave drag][ref_wave_drag], [supersonic][ref_supersonic_speed] flow, [boundary layer][ref_boundary_layer] and [separation][ref_flow_separation] behaviour, [buffeting][ref_buffeting], [aerodynamic centre][ref_aerodynamic_center] and [mean aerodynamic chord][ref_mac] theory, [longitudinal][ref_longitudinal_static_stability] and [directional][ref_directional_stability] stability as general subjects, the [phugoid][ref_phugoid], [flight dynamics][ref_flight_dynamics] generally, [inertia coupling][ref_inertia_coupling] and [Euler's equations][ref_euler_equations_rigid], [moments of inertia][ref_moment_of_inertia] as a subject, [reaction control][ref_rcs], [stabilators][ref_stabilator], [yaw dampers][ref_yaw_damper], [stability augmentation][ref_stability_augmentation], [duralumin][ref_duralumin], [yield][ref_yield_strength], [telemetry][ref_telemetry], [strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], the [sound barrier][ref_sound_barrier], [transonic][ref_transonic] flow, the [aspect ratio][ref_aspect_ratio], [wing twist][ref_wing_twist], [wing root][ref_wing_root] structure, [wing configuration][ref_wing_configuration] as a taxonomy, [delta wings][ref_delta_wing], [Mach][ref_mach_number] and [dynamic pressure][ref_dynamic_pressure] as quantities, the [speed of sound][ref_speed_of_sound], [takeoff][ref_takeoff] and [landing gear][ref_landing_gear], [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, the [National Museum of the United States Air Force][ref_nmusaf], the [list of X-planes][ref_list_of_x_planes], or [experimental aircraft][ref_experimental_aircraft] as a category, all of which are treated where they belong.

## Conclusion

The Bell X-5 was built to find out whether a wing could change its sweep in flight, and it found out, and the answer has a number attached to it.

Sweeping a pivoting wing translates its aerodynamic centre by the panel arm times the change in the sine of the sweep angle. For the X-5 that is 0.93 metres, or 58 percent of the mean chord, which is four to eleven times the entire static margin of a conventional aeroplane. Bell absorbed it by translating the wing forward on rails as it swept back, which worked partially, cost mass, and put the full wing bending moment through a moving joint. Langley later found that moving the pivot outboard and leaving a fixed glove inboard shrinks the same travel by the product of two factors and needs no mechanism at all. That is the finding that put variable sweep into the F-111, the F-14, the Tornado, the B-1, and their Soviet contemporaries, and it is a design problem dissolved rather than solved.

The programme also carried a hazard that the same geometry explains. The NACA's spin-recovery correlating parameter carries the square of the span in its denominator, and sweeping the X-5's wing back shortens the span from 10.21 metres to 6.32. The parameter degrades by a factor of 2.61 with no change in mass distribution at all, and the aircraft that was lost was lost in a spin at the sweep setting where that factor is worst. The mass had not moved. The lever had.

One inequality made the whole thing flyable. The sweep took thirty seconds and the aircraft's short period took two, so the geometry change was fifteen times slower than the dynamics it perturbed and the pilot met a slow drift rather than a step. Modern morphing aircraft do not always enjoy that margin, which is why so much of the contemporary literature is about the transient rather than the endpoints.

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
- [Hallion 1981 On the Frontier, Flight Research at Dryden][book_hallion_1981_on_the_frontier]
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
- [Wikipedia Article on Aeroelasticity][ref_aeroelasticity]
- [Wikipedia Article on Aircraft Nuclear Propulsion][ref_anp]
- [Wikipedia Article on Bell Aircraft][ref_bell_aircraft]
- [Wikipedia Article on Chuck Yeager][ref_yeager]
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

- [Abel et al 1966 Flutter studies of simplified component models of a variable-sweep-wing airplane at Mach numbers up to 3.0][research_abel_1966]
- [Ackeret 1925 Air Forces on Airfoils Moving Faster Than Sound][research_ackeret_1925]
- [Alford and Henderson 1959 An exploratory investigation of the low-speed aerodynamic characteristics of variable-wing- sweep airplane configurations][research_alford_1959_2]
- [Alford et al 1959 Wind-tunnel Studies at Subsonic and Transonic Speeds of a Multiple-mission Variable-wing-sweep Airplane Configuration][research_alford_1959]
- [Alford et al 1962 Subsonic and supersonic aerodynamic characteristics of an airplane configuration utilizing double-pivot variable-sweep wings][research_alford_1962]
- [Alford et al 1966 The Transonic Aerodynamic Characteristics of Two Variable-sweep Airplane Configurations Capable of Low-level Supersonic Attack][research_alford_1966]
- [Anderson and Bray 1955 A Flight Evaluation of the Longitudinal Stability Characteristics Associated with the Pitch-up of a Swept-Wing Airplane in Maneuvering Flight at][research_anderson_1955]
- [Averett and Wright 1966 Transonic aerodynamic damping and oscillatory stability in yaw and pitch for a model of a variable-sweep supersonic transport airplane][research_averett_1966]
- [Banner et al 1955 Wing-load Measurements of the Bell X-5 Research Airplane at a Sweep Angle of 58.7 Degrees][research_banner_1955]
- [Bartlett et al 1973 Wind-tunnel development of underwing leading-edge vortex generators on a NASA supercritical-wing research airplane configuration][research_bartlett_1973]
- [Becht 1950 Stability and Control Characteristics of a 1/4-scale Bell X-5 Airplane Model in the Landing Configuration][research_becht_1950]
- [Beeler Bellman and Saltzman 1956 Flight Techniques for Determining Airplane Drag at High Mach Numbers][research_beeler_1956]
- [Bellman 1953 Lift and Drag Characteristics of the Bell X-5 Research Airplane at 59 Degrees Sweepback for Mach Numbers from 0.60 to 1.03][research_bellman_1953]
- [Bellman 1959 A Summary of Flight-Determined Transonic Lift and Drag Characteristics of Several Research Airplane Configurations][research_bellman_1959]
- [Berman 1947 Spin and Recovery Characteristics of the Curtiss-Wright XP-87 Airplane][research_berman_1947]
- [Berman 1949 Spin and Recovery Characteristics of the Northrop XF-89 Airplane][research_berman_1949]
- [Bielat and Pierpont 1960 Transonic aerodynamic characteristics of a variable-sweep airplane configuration having a 12-percent-thick wing and an inboard pivot location][research_bielat_1960]
- [Bird and Jaquet 1951 A study of the use of experimental stability derivatives in the calculation of the lateral disturbed motions of a swept-wing airplane and][research_bird_1951]
- [Bird et al 1952 Investigation of the Influence of Fuselage and Tail Surfaces on Low-speed Static Stability and Rolling Characteristics of a Swept-wing Model][research_bird_1952]
- [Bishay et al 2019 Development of a New Span-Morphing Wing Core Design][research_bishay_2019]
- [Boltz et al 1960 Effects of Sweep Angle on the Boundary-Layer Stability Characteristics of an Untapered Wing at Low Speeds][research_boltz_1960]
- [Bowman 1956 Concluding Report on Free-Spinning and Recovery Characteristics of a 1/24-Scale Model of the Grumman F11F-1 Airplane, TED No. NACA AD 395][research_bowman_1956]
- [Bowman and Healy 1959 Free-Spinning-Tunnel Investigation of a 1/40-Scale Model of the McConnell F-101A Airplane][research_bowman_1959]
- [Buckingham 1914 On Physically Similar Systems][research_buckingham_1914]
- [Burk and Healy 1955 Free-Spinning-Tunnel Investigation to Determine the Effect of Spin-Recovery Rockets and Thrust Simulation on the Recovery Characteristics of a][research_burk_1955]
- [Chaloner and Verdinelli 1995 Bayesian Experimental Design, A Review][research_chaloner_verdinelli_1995]
- [Changchuan et al 2022 Aeroelastic Response of a Z-Shaped Folding Wing During the Morphing Process][research_changchuan_2022]
- [Cheung et al 2020 Testing of a Folding Wingtip for Gust Load Alleviation of a Flexible High-Aspect-Ratio Wing][research_cheung_folding_2020]
- [Chiarelli and Bonomo 2019 Numerical Investigation into Flutter and Flutter-Buffet Phenomena for a Swept Wing][research_chiarelli_2019]
- [Childs 1953 Flight Measurements of the Stability Characteristics of the Bell X-5 Research Airplane in Sideslips at 59 Deg Sweepback][research_childs_1953]
- [Collar 1946 The Expanding Domain of Aeroelasticity][research_collar_1946]
- [Cornette 1961 Wind-Tunnel Investigation of the Effects of Wing Bodies, Fences, Flaps, and a Fuselage Addition on the Wing Buffet Response of a][research_cornette_1961]
- [Croom and Huffman 1957 Investigation at Low Speeds of Deflectors and Spoilers as Gust Alleviators on a Model of the Bell X-5 Airplane with 35 Degree Swept Wings and on a][research_croom_1957]
- [Dai et al 2020 Design and Aerodynamic Performance Analysis of a Variable-Sweep-Wing Morphing Aircraft][research_dai_sweep_2020]
- [Dai et al 2021 Modeling and Nonlinear Model Predictive Control of a Variable-Sweep-Wing Morphing Aircraft][research_dai_mpc_2021]
- [Dam et al 2022 Artificial Neural Network Based Wing Planform Aerodynamic Optimization][research_dam_planform_2022]
- [Deyoung 1947 Theoretical Additional Span Loading Characteristics of Wings with Arbitrary Sweep, Aspect Ratio, and Taper Ratio][research_deyoung_1947]
- [Dussart et al 2019 Identification of In-Flight Wingtip Folding Effects on the Roll Characteristics of a Flexible Aircraft][research_dussart_roll_2019]
- [Dussart et al 2019 In-Flight Wingtip Folding, Inspiration from the XB-70 Valkyrie][research_dussart_xb70_2019]
- [Eckert and Maki 1973 Low-speed wind tunnel investigation of the lateral-directional characterisitcs of a large-scale variable wing-sweep fighter model in the high-lift][research_eckert_1973]
- [Elelwi et al 2020 Comparison and Analyses of a Variable Span-Morphing of the Tapered Wing][research_elelwi_span_2020]
- [Elelwi et al 2021 Structural Sizing and Topology Optimization Based on Weight Minimization of a Variable Tapered Span Morphing Wing][research_elelwi_topology_2021]
- [Elelwi et al 2022 Multidisciplinary Optimization for Weight Saving in a Variable Tapered Span-Morphing Wing][research_elelwi_weight_2022]
- [Faure and Leogrande 2020 High Angle-of-Attack Aerodynamics of a Straight Wing with Finite Span][research_faure_2020]
- [Finch and Briggs 1953 Preliminary Results of Stability and Control Investigation of the Bell X-5 Research Airplane][research_finch_1953]
- [Finch and Walker 1953 Flight Determination of the Static Longitudinal Stability Boundaries of the Bell X-5 Research Airplane with 59 Deg Sweepback][research_finch_1953_2]
- [Fisher and Williams 1958 Wind-Tunnel Investigation of Some Effects of Wing Sweep and Horizontal-Tail Height on the Static Stability of an Airplane Model at Transonic Speeds][research_fisher_1958]
- [Foster and Fitzpatrick 1948 Longitudinal-stability Investigation of High-lift and Stall-control Devices on a 52 Degree Sweptback Wing with and Without Fuselage and Horizontal][research_foster_1948]
- [Foster and Morris 1960 Stability and Control Characteristics at a Mach Number of 1.97 of an Airplane Configuration Having Two Types of Variable-sweep Wings][research_foster_1960]
- [Funk and Cooney 1959 Some Effects of Yaw Damping on Airplane Motions and Vertical-Tail Loads in Turbulent Air][research_funk_1959]
- [Gainer et al 1967 Rolling stability derivatives of a variable- sweep tactical fighter model at subsonic and transonic speeds][research_gainer_1967]
- [Gale and Pumphrey 1950 Spin and recovery characteristics of a model of a fighter type of airplane without a horizontal tail having either a single vertical tail or twin][research_gale_1950]
- [Gao et al 2022 Analysis and Control for the Mode Transition of Tandem-Wing Aircraft with Variable Sweep][research_gao_tandem_2022]
- [Garrick and Reed 1981 Historical Development of Aircraft Flutter][research_garrick_reed_1981]
- [Geva et al 2019 Investigation of a Morphing Wing Capable of Airfoil and Span Adjustment][research_geva_2019]
- [Gilyard 1972 Flight-determined derivatives and dynamic characteristics of the CV-990 airplane][research_gilyard_1972]
- [Glauert 1928 The Effect of Compressibility on the Lift of an Aerofoil][research_glauert_1928]
- [Goetz and Stonesifer 1961 Transonic and Supersonic Flutter Trend Investigation of a Variable-sweep Wing][research_goetz_1961]
- [Guo et al 2020 Unsteady Flow Simulation of a Variable-Sweep Morphing Aircraft Coupled with Dynamic Deformation][research_guo_unsteady_2020]
- [Gurley and Ruhlin 1962 Transonic flutter investigation of models of a proposed variable-sweep wing][research_gurley_1962]
- [Hamer et al 1961 Application of Monte Carlo Technique for Determining Maneuvering Loads from Statistical Information on Airplane Motions][research_hamer_1961]
- [Hammond and Henderson 1961 Low-speed Investigation of High-lift and Lateral Control Devices on a Semispan Variable-sweep Wing Having an Outboard Pivot Location][research_hammond_1961]
- [Hammond and Polhamus 1965 Subsonic aerodynamic characteristics of an airplane configuration utilizing a variable- sweep wing having a free-floating apex][research_hammond_1965]
- [Hammond and Polhamus 1970 Variable sweep aircraft Patent][research_hammond_1970]
- [Hanson 1973 Evaluation of an aeroelastic model technique for predicting airplane buffet loads][research_hanson_1973]
- [Harvey and Inman 2022 Gull Dynamic Pitch Stability Is Controlled by Wing Morphing][research_harvey_inman_2022]
- [Harvey et al 2021 Gull-Inspired Joint-Driven Wing Morphing Allows Adaptive Longitudinal Flight Control][research_harvey_gull_2021]
- [Hayes and Sleeman 1959 Low-Speed Investigation Of The Effects Of Horizontal-Tail Area And Wing Sweep On The Static Longitudinal Stability And Control Characteristics Of][research_hayes_1959]
- [Henderson and Ray 1964 Effect of wing pivot location on longitudinal aerodynamic characteristics of a variable sweep wing having an M planform][research_henderson_1964]
- [Henderson and Ray 1965 Effect of wing planform modification on longitudinal characteristics of a variable- sweep m wing][research_henderson_1965]
- [Hermanutz and Hornung 2020 Aeroelastic Wing Planform Design Optimization of a Flutter Demonstrator][research_hermanutz_2020]
- [Hopkins 1975 Effects of wing bend on the aerodynamic characteristics of a low aspect ratio oblique wing][research_hopkins_1975]
- [Housner and Stein 1974 Flutter analysis of swept-wing subsonic aircraft with parameter studies of composite wings][research_housner_1974]
- [Huffman 1972 Effects of wing-pivot location and forewing configuration on the low-speed aerodynamic characteristics of a variable-sweep airplane model][research_huffman_1972]
- [Iliff and Taylor 1972 Determination of stability derivatives from flight data using a Newton-Raphson minimization technique][research_iliff_1972]
- [James and Maki 1957 Wind-tunnel Tests of the Static Longitudinal Characteristics at Low Speed of a Swept-wing Airplane with Blowing Flaps and Leading-edge Slats][research_james_1957]
- [James S Bowman and White 1974 Spin-Tunnel Investigation of a 1/40-Scale Model of the F-111A Airplane with Store Loadings and with Supplementary Spin-Recovery Devices][research_bowman_1974]
- [Jim et al 2021 Bayesian Optimization of a Low-Boom Supersonic Wing Planform][research_jim_planform_2021]
- [Jones 1947 Wing Plan Forms for High-Speed Flight][research_jones_1947]
- [Kapuscinski et al 2020 A Vision-Based Method for Determining Aircraft State during Spin Recovery][research_kapuscinski_2020]
- [Keidel et al 2020 Control Authority of a Camber Morphing Flying Wing][research_keidel_2020]
- [Kemp and Becht 1950 Stability and control characteristics at low speed of a 1/4-scale Bell X-5 airplane model, lateral and directional stability and control][research_kemp_1950]
- [Kemp and Few 1951 Pressure Distribution at Low Speed on a 1/4-scale Bell X-5 Airplane Model][research_kemp_1951]
- [Kilgore 1971 Some transonic and supersonic dynamic stability characteristics of a variable-sweep-wing tactical fighter model][research_kilgore_1971]
- [Klimczyk and Goraj 2019 Analysis and Optimization of Morphing Wing Aerodynamics][research_klimczyk_2019]
- [Klinar and Jones 1949 Spin Investigation of a 1/29-Scale Model of the Republic XF-91 Airplane with a Conventional Tail Installed][research_klinar_1949]
- [Klinar and Wilson 1950 Free-Spinning-Tunnel Investigation of a 1/24-Scale Model of the Grumman AF-2S, -2W Airplane][research_klinar_1950]
- [Kumar et al 2021 On Topology Optimization of Large Deformation Contact-Aided Shape Morphing Compliant Mechanisms][research_kumar_topology_2021]
- [Lamar and Mc Kinney 1971 Low-speed static wind-tunnel investigation of a half-span fuselage and variable sweep pressure wing model][research_lamar_1971]
- [Lee 1952 Investigation of Spinning and Tumbling Characteristics of a 1/20-Scale Model of the Consolidated Vultee XFY-1 Airplane in the Free-Spinning][research_lee_1952]
- [Lee 1964 Spin Tunnel Investigation of a 1/30 Scale Model of the North American A-5A Airplane][research_lee_1964]
- [Lee and Healy 1964 Spin-Tunnel Investigation of a 1/28-Scale Model of a Subsonic Attack Airplane][research_lee_1964_2]
- [Li et al 2020 Simulation Analysis of the Aerodynamic Characteristics of a Variable Sweep Wing Morphing Aircraft][research_li_varsweep_2020]
- [Lindley 1956 On a Measure of the Information Provided by an Experiment][research_lindley_1956]
- [Lockwood 1966 Low-speed wind-tunnel studies relating to pitch-up on a supersonic transport model with a high-aspect-ratio variable-sweep wing][research_lockwood_1966]
- [Ma et al 2021 Stability Analysis and Augmentation Design of a Bionic Multi-Section Variable-Sweep-Wing UAV][research_ma_bionic_2021]
- [Monfort and Whitcomb 1975 High-attitude low-speed static aerodynamic characteristics of an F-4D fighter airplane model with leading edge slats][research_monfort_1975]
- [NACA 1949 NACA Conference on Aerodynamic Problems of Transonic Airplane Design][research_naca_1949]
- [NACA 1953 Equations, Tables, and Charts for Compressible Flow][research_naca_1135]
- [NACA 1957 NACA Conference on Aircraft Loads, Structures, and Flutter][research_naca_1957]
- [NACA 1966 Summary of NACA/NASA Variable-Sweep Research and Development Leading to the F-111 (TFX)][research_naca_1966]
- [NACA 1966 Summary of NASA Support of the F-111 Development Program, December 1962 - December 1965 - Part 1][research_naca_1966_2]
- [Nazeer et al 2021 Sensing, Actuation, and Control of the SmartX Prototype Morphing Wing in the Wind Tunnel][research_nazeer_2021]
- [Nyquist 1928 Certain Topics in Telegraph Transmission Theory][research_nyquist_1928]
- [Phillips 1948 Effect of Steady Rolling on Longitudinal and Directional Stability][research_phillips_1948]
- [Polhamus and Hammond 1960 II. Aerodynamic research relative to variable-sweep multimission aircraft][research_polhamus_1960]
- [Polhamus and Toll 1981 Research related to variable sweep aircraft development][research_polhamus_1981]
- [Prandtl 1928 Motion of Fluids with Very Little Viscosity][research_prandtl_1928]
- [Queijo et al 1954 Wind-Tunnel Investigation at Low Speed of the Effects of Chordwise Wing Fences and Horizontal-Tail Position on the Static Longitudinal Stability][research_queijo_1954]
- [Quigley et al 1960 Flight Investigation of the Low-Speed Characteristics of a 45 deg Swept-Wing Fighter-Type Airplane with Blowing Boundary-Layer Control Applied to][research_quigley_1960]
- [Rathert et al 1951 Preliminary Flight Investigation of the Maneuvering Accelerations and Buffet Boundary of a 35 Degree Swept-wing Airplane at High Altitude and][research_rathert_1951]
- [Ray et al 1972 Maneuver and buffet characteristics of fighter aircraft][research_ray_1972]
- [Reed 1955 Flight Measurements of Horizontal-Tail Loads on the Bell X-5 Research Airplane at a Sweep Angle of 58.7 Deg][research_reed_1955]
- [Rogers and Dunn 1952 Preliminary Results of Horizontal-tail Load Measurements of the Bell X-5 Research Airplane][research_rogers_1952]
- [Salahudden and Ghosh 2021 Robust Control Design Based Aircraft Flat-Spin Recovery Using Optimally Deflected Surfaces][research_salahudden_2021]
- [Sanger M Burk and Libbey 1961 Large-Angle Motion Tests, Including Spins, of A Free-Flying Radio-Controlled 0.13-Scale Model of A Twin Jet Swept Wing Fighter Airplane][research_burk_1961]
- [Scher 1947 Preliminary Evaluation of the Spin and Recovery Characteristics of the Douglas XF3D-1 Airplane][research_scher_1947]
- [Scudder and Seidman 1935 A Flight Investigation of the Spinning of the F4B-2 Biplane with Various Loads and Tail Surfaces][research_scudder_1935]
- [Shannon 1948 A Mathematical Theory of Communication][research_shannon_1948]
- [Snyder 1947 Estimation of the Spin and Recovery Characteristics of the North American XSN2J-1 Airplane][research_snyder_1947]
- [Spearman and Becht 1948 The Effect of Negative Dihedral, Tip Droop, and Wing-tip Shape on the Low-speed Aerodynamic Characteristics of a Complete Model Having a 45][research_spearman_1948]
- [Spencer 1960 Stability and control characteristics at low subsonic speeds of an airplane configuration having two types of variable-sweep wings][research_spencer_1960]
- [Stephenson 1956 Flight Measurements of Horizontal-tail Loads on the Douglas X-3 Research Airplane][research_stephenson_1956]
- [Stone and Burk 1947 Effect of Horizontal-tail Position on the Hinge Moments of an Unbalanced Rudder in Attitudes Simulating Spin Conditions][research_stone_1947]
- [Sutherland 1893 The Viscosity of Gases and Molecular Force][research_sutherland_1893]
- [Theodorsen, General Theory of Aerodynamic Instability and the Mechanism of Flutter][research_theodorsen_1935]
- [Toll 1962 Variable sweep wing aircraft Patent][research_toll_1962]
- [Traub 2019 Experimental Study of a Morphing Annular Wing][research_traub_2019]
- [Tsushima et al 2019 Geometrically Nonlinear Static Aeroelastic Analysis of Composite Morphing Wings][research_tsushima_2019]
- [Venkateswara Rao and Go 2019 Optimization of Aircraft Spin Recovery Maneuvers][research_rao_spin_2019]
- [Videan 1955 Flight Measurements of the Dynamic Lateral and Longitudinal Stability of the Bell X-5 Research Airplane at 58.7 Degrees Sweepback][research_videan_1955]
- [Whitcomb and Norton 1961 Transonic Investigation of Aerodynamic Characteristics of a Swept-Wing Fighter-Airplane Model with Leading-Edge Droop in Combination with Outboard][research_whitcomb_1961]
- [Williams and Drake, The Research Airplane, Past, Present, and Future][research_williams_drake_1948]
- [Wright 1936 Factors Affecting the Cost of Airplanes][research_wright_1936]
- [You et al 2020 Design Criteria for Variable Camber Compliant Wing Aircraft Morphing Wing Skin][research_you_skin_2020]
- [Yue et al 2019 Sliding Mode Control Design for Oblique Wing Aircraft in the Wing Skewing Process][research_yue_oblique_2019]
- [Zhou and Huang 2021 Efficient Nonlinear Aeroelastic Analysis of a Morphing Wing via Parameterized Reduced Order Modelling][research_zhou_huang_2021]

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

[book_anderson_1997_history_aerodynamics]: https://openlibrary.org/search?q=Anderson+A+History+of+Aerodynamics
[book_anderson_2001_fundamentals]: https://openlibrary.org/search?q=Anderson+Fundamentals+of+Aerodynamics
[book_anderson_2002_modern_compressible]: https://openlibrary.org/search?q=Anderson+Modern+Compressible+Flow
[book_anderson_2006_hypersonic]: https://openlibrary.org/search?q=Anderson+Hypersonic+and+High+Temperature+Gas+Dynamics
[book_anderson_2012_aircraft_performance]: https://openlibrary.org/search?q=Anderson+Aircraft+Performance+and+Design
[book_ashley_landahl_1965]: https://openlibrary.org/search?q=Ashley+Landahl+Aerodynamics+of+Wings+and+Bodies
[book_baals_corliss_1981]: https://openlibrary.org/search?q=Baals+Corliss+Wind+Tunnels+of+NASA
[book_bertin_1994_hypersonic]: https://openlibrary.org/search?q=Bertin+Hypersonic+Aerothermodynamics
[book_bertin_cummings_2013]: https://openlibrary.org/search?q=Bertin+Cummings+Aerodynamics+for+Engineers
[book_bevington_robinson_2002]: https://openlibrary.org/search?q=Bevington+Robinson+Data+Reduction+and+Error+Analysis
[book_bilstein_1989_orders]: https://openlibrary.org/search?q=Bilstein+Orders+of+Magnitude+NACA+NASA
[book_bisplinghoff_ashley_halfman_1955]: https://openlibrary.org/search?q=Bisplinghoff+Ashley+Halfman+Aeroelasticity
[book_boley_weiner_1960]: https://openlibrary.org/search?q=Boley+Weiner+Theory+of+Thermal+Stresses
[book_box_hunter_hunter_2005]: https://openlibrary.org/search?q=Box+Hunter+Statistics+for+Experimenters
[book_bruhn_1973]: https://openlibrary.org/search?q=Bruhn+Analysis+and+Design+of+Flight+Vehicle+Structures
[book_carslaw_jaeger_1959]: https://openlibrary.org/search?q=Carslaw+Jaeger+Conduction+of+Heat+in+Solids
[book_chambers_2008_radical_wings]: https://openlibrary.org/search?q=Chambers+Radical+Wings+and+Wind+Tunnels
[book_cover_thomas_2006]: https://openlibrary.org/search?q=Cover+Thomas+Elements+of+Information+Theory
[book_dowell_2014]: https://openlibrary.org/search?q=Dowell+A+Modern+Course+in+Aeroelasticity
[book_etkin_reid_1996]: https://openlibrary.org/search?q=Etkin+Reid+Dynamics+of+Flight+Stability+and+Control
[book_ferguson_1992]: https://openlibrary.org/search?q=Ferguson+Engineering+and+the+Mind+s+Eye
[book_fung_1955]: https://openlibrary.org/search?q=Fung+Introduction+to+the+Theory+of+Aeroelasticity
[book_gelman_et_al_2013]: https://openlibrary.org/search?q=Gelman+Bayesian+Data+Analysis
[book_gorn_1992_universal_man]: https://openlibrary.org/search?q=Gorn+The+Universal+Man+von+Karman
[book_gorn_2001_expanding_envelope]: https://openlibrary.org/search?q=Gorn+Expanding+the+Envelope+Flight+Research
[book_gunston_1992_faster_than_sound]: https://openlibrary.org/search?q=Gunston+Faster+Than+Sound
[book_hallion_1972_supersonic_flight]: https://openlibrary.org/search?q=Hallion+Supersonic+Flight+Breaking+the+Sound+Barrier
[book_hallion_1981_on_the_frontier]: https://openlibrary.org/search?q=Hallion+On+the+Frontier+Flight+Research+Dryden
[book_hallion_1981_test_pilots]: https://openlibrary.org/search?q=Hallion+Test+Pilots+The+Frontiersmen+of+Flight
[book_hansen_1987_engineer_in_charge]: https://openlibrary.org/search?q=Hansen+Engineer+in+Charge+Langley
[book_heppenheimer_2007_heat_barrier]: https://openlibrary.org/search?q=Heppenheimer+Facing+the+Heat+Barrier+Hypersonics
[book_hill_peterson_1991]: https://openlibrary.org/search?q=Hill+Peterson+Mechanics+and+Thermodynamics+of+Propulsion
[book_hurt_1965]: https://openlibrary.org/search?q=Hurt+Aerodynamics+for+Naval+Aviators
[book_huzel_huang_1992]: https://openlibrary.org/search?q=Huzel+Huang+Design+of+Liquid+Propellant+Rocket+Engines
[book_incropera_heat_transfer]: https://openlibrary.org/search?q=Incropera+Fundamentals+of+Heat+and+Mass+Transfer
[book_jenkins_2000_hypersonics]: https://openlibrary.org/search?q=Jenkins+Hypersonics+Before+the+Shuttle+X-15
[book_jenkins_2007_x15]: https://openlibrary.org/search?q=Jenkins+X-15+Extending+the+Frontiers+of+Flight
[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X-Vehicles+Inventory
[book_kimberlin_2003]: https://openlibrary.org/search?q=Kimberlin+Flight+Testing+of+Fixed+Wing+Aircraft
[book_kuchemann_1978]: https://openlibrary.org/search?q=Kuchemann+The+Aerodynamic+Design+of+Aircraft
[book_launius_jenkins_2012]: https://openlibrary.org/search?q=Launius+Jenkins+Coming+Home+Reentry+and+Recovery+from+Space
[book_liepmann_roshko_1957]: https://openlibrary.org/search?q=Liepmann+Roshko+Elements+of+Gasdynamics
[book_mcruer_ashkenas_graham_1973]: https://openlibrary.org/search?q=McRuer+Ashkenas+Graham+Aircraft+Dynamics+and+Automatic+Control
[book_megson_2016]: https://openlibrary.org/search?q=Megson+Aircraft+Structures+for+Engineering+Students
[book_merlin_2009_blackbird]: https://openlibrary.org/search?q=Merlin+Design+and+Development+of+the+Blackbird
[book_miller_2001_x_planes]: https://openlibrary.org/search?q=Jay+Miller+The+X-Planes+X-1+to+X-45
[book_nelson_1998]: https://openlibrary.org/search?q=Nelson+Flight+Stability+and+Automatic+Control
[book_nicolai_carichner_2010]: https://openlibrary.org/search?q=Nicolai+Carichner+Fundamentals+of+Aircraft+and+Airship+Design
[book_niu_1988_airframe]: https://openlibrary.org/search?q=Niu+Airframe+Structural+Design
[book_peebles_2014_probing_the_sky]: https://openlibrary.org/search?q=Peebles+Probing+the+Sky+NACA+Research+Airplanes
[book_perrow_1984]: https://openlibrary.org/search?q=Perrow+Normal+Accidents
[book_petroski_1985]: https://openlibrary.org/search?q=Petroski+To+Engineer+Is+Human
[book_raymer_2018]: https://openlibrary.org/search?q=Raymer+Aircraft+Design+A+Conceptual+Approach
[book_reason_1990_human_error]: https://openlibrary.org/search?q=James+Reason+Human+Error
[book_roskam_1985]: https://openlibrary.org/search?q=Roskam+Airplane+Design
[book_sagan_1993]: https://openlibrary.org/search?q=Sagan+The+Limits+of+Safety
[book_schlichting_gersten_2017]: https://openlibrary.org/search?q=Schlichting+Gersten+Boundary+Layer+Theory
[book_shapiro_1953]: https://openlibrary.org/search?q=Shapiro+Dynamics+and+Thermodynamics+of+Compressible+Fluid+Flow
[book_stengel_2004]: https://openlibrary.org/search?q=Stengel+Flight+Dynamics
[book_stevens_lewis_2015]: https://openlibrary.org/search?q=Stevens+Lewis+Aircraft+Control+and+Simulation
[book_stinton_2001]: https://openlibrary.org/search?q=Stinton+The+Design+of+the+Aeroplane
[book_sutton_biblarz_2016]: https://openlibrary.org/search?q=Sutton+Biblarz+Rocket+Propulsion+Elements
[book_taylor_1997_error_analysis]: https://openlibrary.org/search?q=Taylor+An+Introduction+to+Error+Analysis
[book_thompson_1992_edge_of_space]: https://openlibrary.org/search?q=Milton+Thompson+At+the+Edge+of+Space+X-15
[book_torenbeek_1982]: https://openlibrary.org/search?q=Torenbeek+Synthesis+of+Subsonic+Airplane+Design
[book_truitt_1960]: https://openlibrary.org/search?q=Truitt+Fundamentals+of+Aerodynamic+Heating
[book_vaughan_1996]: https://openlibrary.org/search?q=Vaughan+The+Challenger+Launch+Decision
[book_vincenti_1990]: https://openlibrary.org/search?q=Vincenti+What+Engineers+Know+and+How+They+Know+It
[book_von_karman_edson_1967]: https://openlibrary.org/search?q=von+Karman+The+Wind+and+Beyond
[book_ward_strganac_niewoehner_2006]: https://openlibrary.org/search?q=Ward+Strganac+Introduction+to+Flight+Test+Engineering
[book_white_2006_viscous]: https://openlibrary.org/search?q=Frank+White+Viscous+Fluid+Flow
[book_whitford_1987]: https://openlibrary.org/search?q=Whitford+Design+for+Air+Combat
[book_winchester_2005_x_planes]: https://openlibrary.org/search?q=Winchester+X-Planes+and+Prototypes
[book_wolfe_1979_right_stuff]: https://openlibrary.org/search?q=Tom+Wolfe+The+Right+Stuff
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
[ref_yeager]: https://en.wikipedia.org/wiki/Chuck_Yeager
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
[research_abel_1966]: https://ntrs.nasa.gov/citations/19660021918
[research_ackeret_1925]: https://ntrs.nasa.gov/citations/19930087085
[research_alford_1959]: https://ntrs.nasa.gov/citations/19650014458
[research_alford_1959_2]: https://ntrs.nasa.gov/citations/19650014499
[research_alford_1962]: https://ntrs.nasa.gov/citations/19660025704
[research_alford_1966]: https://ntrs.nasa.gov/citations/19660022439
[research_anderson_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_averett_1966]: https://ntrs.nasa.gov/citations/19660010231
[research_banner_1955]: https://ntrs.nasa.gov/citations/19930088628
[research_bartlett_1973]: https://ntrs.nasa.gov/citations/19830002762
[research_becht_1950]: https://ntrs.nasa.gov/citations/19930086394
[research_beeler_1956]: https://ntrs.nasa.gov/citations/19930084521
[research_bellman_1953]: https://ntrs.nasa.gov/citations/19930087480
[research_bellman_1959]: https://ntrs.nasa.gov/citations/19980228028
[research_berman_1947]: https://ntrs.nasa.gov/citations/20050019623
[research_berman_1949]: https://ntrs.nasa.gov/citations/20090026468
[research_bielat_1960]: https://ntrs.nasa.gov/citations/19650017034
[research_bird_1951]: https://ntrs.nasa.gov/citations/19930092084
[research_bird_1952]: https://ntrs.nasa.gov/citations/19930083189
[research_bishay_2019]: https://doi.org/10.3390/designs3010012
[research_boltz_1960]: https://ntrs.nasa.gov/citations/19980227185
[research_bowman_1956]: https://ntrs.nasa.gov/citations/20050028485
[research_bowman_1959]: https://ntrs.nasa.gov/citations/19980228366
[research_bowman_1974]: https://ntrs.nasa.gov/citations/20000021277
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_burk_1955]: https://ntrs.nasa.gov/citations/20050029372
[research_burk_1961]: https://ntrs.nasa.gov/citations/19720075828
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_changchuan_2022]: https://doi.org/10.2514/1.j061138
[research_cheung_folding_2020]: https://doi.org/10.2514/1.c035732
[research_chiarelli_2019]: https://doi.org/10.1155/2019/8210235
[research_childs_1953]: https://ntrs.nasa.gov/citations/19930087404
[research_collar_1946]: https://doi.org/10.1017/s0368393100120358
[research_cornette_1961]: https://ntrs.nasa.gov/citations/20040003909
[research_croom_1957]: https://ntrs.nasa.gov/citations/19930084891
[research_dai_mpc_2021]: https://doi.org/10.1109/access.2021.3074912
[research_dai_sweep_2020]: https://doi.org/10.1016/j.ast.2020.105703
[research_dam_planform_2022]: https://doi.org/10.1108/aeat-10-2021-0311
[research_deyoung_1947]: https://ntrs.nasa.gov/citations/19930082544
[research_dussart_roll_2019]: https://doi.org/10.3390/aerospace6060063
[research_dussart_xb70_2019]: https://doi.org/10.15394/ijaaa.2019.1343
[research_eckert_1973]: https://ntrs.nasa.gov/citations/19740004601
[research_elelwi_span_2020]: https://doi.org/10.1017/aer.2020.19
[research_elelwi_topology_2021]: https://doi.org/10.3390/biomimetics6040055
[research_elelwi_weight_2022]: https://doi.org/10.3390/act11050121
[research_faure_2020]: https://doi.org/10.1063/5.0025327
[research_finch_1953]: https://ntrs.nasa.gov/citations/19930087476
[research_finch_1953_2]: https://ntrs.nasa.gov/citations/19930087479
[research_fisher_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_foster_1948]: https://ntrs.nasa.gov/citations/19930085540
[research_foster_1960]: https://ntrs.nasa.gov/citations/19660022441
[research_funk_1959]: https://ntrs.nasa.gov/citations/19980228407
[research_gainer_1967]: https://ntrs.nasa.gov/citations/19670008821
[research_gale_1950]: https://ntrs.nasa.gov/citations/19930086221
[research_gao_tandem_2022]: https://doi.org/10.3390/aerospace9080463
[research_garrick_reed_1981]: https://doi.org/10.2514/3.57579
[research_geva_2019]: https://doi.org/10.3390/aerospace6080085
[research_gilyard_1972]: https://ntrs.nasa.gov/citations/19720015377
[research_glauert_1928]: https://doi.org/10.1098/rspa.1928.0039
[research_goetz_1961]: https://ntrs.nasa.gov/citations/19660022440
[research_guo_unsteady_2020]: https://doi.org/10.1142/s0217979220400731
[research_gurley_1962]: https://ntrs.nasa.gov/citations/19660025705
[research_hamer_1961]: https://ntrs.nasa.gov/citations/20040027944
[research_hammond_1961]: https://ntrs.nasa.gov/citations/19650014317
[research_hammond_1965]: https://ntrs.nasa.gov/citations/19660025706
[research_hammond_1970]: https://ntrs.nasa.gov/citations/19710001566
[research_hanson_1973]: https://ntrs.nasa.gov/citations/19730008178
[research_harvey_gull_2021]: https://doi.org/10.1098/rsif.2021.0132
[research_harvey_inman_2022]: https://doi.org/10.1073/pnas.2204847119
[research_hayes_1959]: https://ntrs.nasa.gov/citations/19630010604
[research_henderson_1964]: https://ntrs.nasa.gov/citations/19670022816
[research_henderson_1965]: https://ntrs.nasa.gov/citations/19650024621
[research_hermanutz_2020]: https://doi.org/10.3390/aerospace7040045
[research_hopkins_1975]: https://ntrs.nasa.gov/citations/19750055435
[research_housner_1974]: https://ntrs.nasa.gov/citations/19740024243
[research_huffman_1972]: https://ntrs.nasa.gov/citations/19730003273
[research_iliff_1972]: https://ntrs.nasa.gov/citations/19720012009
[research_james_1957]: https://ntrs.nasa.gov/citations/19930089713
[research_jim_planform_2021]: https://doi.org/10.2514/1.j060225
[research_jones_1947]: https://ntrs.nasa.gov/citations/19930091936
[research_kapuscinski_2020]: https://doi.org/10.3390/s20082401
[research_keidel_2020]: https://doi.org/10.2514/1.c035606
[research_kemp_1950]: https://ntrs.nasa.gov/citations/19930086268
[research_kemp_1951]: https://ntrs.nasa.gov/citations/19930086901
[research_kilgore_1971]: https://ntrs.nasa.gov/citations/19710007950
[research_klimczyk_2019]: https://doi.org/10.1108/aeat-12-2017-0289
[research_klinar_1949]: https://ntrs.nasa.gov/citations/20050030060
[research_klinar_1950]: https://ntrs.nasa.gov/citations/20050029448
[research_kumar_topology_2021]: https://doi.org/10.1016/j.mechmachtheory.2020.104135
[research_lamar_1971]: https://ntrs.nasa.gov/citations/19710024300
[research_lee_1952]: https://ntrs.nasa.gov/citations/20050029463
[research_lee_1964]: https://ntrs.nasa.gov/citations/19980236423
[research_lee_1964_2]: https://ntrs.nasa.gov/citations/19940040848
[research_li_varsweep_2020]: https://doi.org/10.1088/1742-6596/1570/1/012073
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_lockwood_1966]: https://ntrs.nasa.gov/citations/19660023730
[research_ma_bionic_2021]: https://doi.org/10.3390/app11198859
[research_monfort_1975]: https://ntrs.nasa.gov/citations/19760019102
[research_naca_1135]: https://ntrs.nasa.gov/citations/19930091059
[research_naca_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_naca_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_naca_1966]: https://ntrs.nasa.gov/citations/20080013519
[research_naca_1966_2]: https://ntrs.nasa.gov/citations/20080013521
[research_nazeer_2021]: https://doi.org/10.3390/act10060107
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_phillips_1948]: https://ntrs.nasa.gov/citations/19930082293
[research_polhamus_1960]: https://ntrs.nasa.gov/citations/19670023743
[research_polhamus_1981]: https://ntrs.nasa.gov/citations/19810016532
[research_prandtl_1928]: https://ntrs.nasa.gov/citations/19930090813
[research_queijo_1954]: https://ntrs.nasa.gov/citations/19930092215
[research_quigley_1960]: https://ntrs.nasa.gov/citations/19980223993
[research_rao_spin_2019]: https://doi.org/10.1016/j.ast.2019.04.046
[research_rathert_1951]: https://ntrs.nasa.gov/citations/19930086490
[research_ray_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_reed_1955]: https://ntrs.nasa.gov/citations/19930088802
[research_rogers_1952]: https://ntrs.nasa.gov/citations/19930087176
[research_salahudden_2021]: https://doi.org/10.1016/j.ast.2021.106823
[research_scher_1947]: https://ntrs.nasa.gov/citations/20050019396
[research_scudder_1935]: https://ntrs.nasa.gov/citations/19930091602
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_snyder_1947]: https://ntrs.nasa.gov/citations/20050019393
[research_spearman_1948]: https://ntrs.nasa.gov/citations/19930085498
[research_spencer_1960]: https://ntrs.nasa.gov/citations/19660024029
[research_stephenson_1956]: https://ntrs.nasa.gov/citations/19930090107
[research_stone_1947]: https://ntrs.nasa.gov/citations/19930081964
[research_sutherland_1893]: https://doi.org/10.1080/14786449308620508
[research_theodorsen_1935]: https://ntrs.nasa.gov/citations/19800006788
[research_toll_1962]: https://ntrs.nasa.gov/citations/19700023955
[research_traub_2019]: https://doi.org/10.2514/1.c035600
[research_tsushima_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_videan_1955]: https://ntrs.nasa.gov/citations/19930089024
[research_whitcomb_1961]: https://ntrs.nasa.gov/citations/20040027948
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_you_skin_2020]: https://doi.org/10.2514/1.j058002
[research_yue_oblique_2019]: https://doi.org/10.1016/j.cja.2018.11.002
[research_zhou_huang_2021]: https://doi.org/10.1007/s11071-021-06577-y
