---
layout: post
mathjax: true
comments: true
title: "X-Planes: Northrop X-4 Bantam"
date: 2025-10-10 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 5
---

<!-- A301 -->
<script>console.log("A301");</script>

The [Northrop X-4 Bantam][ref_northrop_x4] was built to answer one question with a yes or a no. At transonic speed the interference between the wing wake and the horizontal tail was suspected of causing the loss of pitch control that had killed pilots through the 1940s. If that suspicion was correct, then removing the horizontal tail should remove the problem. The X-4 removed it. This article is the fifth in the [X-Planes series][related_post_a297_xplanes_framing] and the fourth per-aircraft treatment, following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], and the [X-3][related_post_a300_douglas_x3]. The National Advisory Committee for Aeronautics, abbreviated NACA throughout and reconstituted in 1958 as the National Aeronautics and Space Administration, abbreviated NASA, supplied the research programme. The Air Force supplied the requirement. [Northrop][ref_northrop_corp], whose founder had spent two decades arguing that tails were unnecessary, supplied an aircraft with which to test the proposition.

The answer was no, and the reason is worth deriving, because it is not the reason anyone expected.

## The Research Question

The keystone is whether a horizontal tail can be dispensed with on a transonic aircraft.

The hypothesis was reasonable and it came from two directions. The first was diagnostic. Aircraft in high-speed dives lost pitch control, and one candidate mechanism was that the shock system on the wing threw a disturbed wake onto the tail, so that the surface the pilot was relying on was operating in flow that the wing had already ruined. Removing the tail removes that coupling by construction. The mechanism the hypothesis blamed is real and quantifiable. A tail immersed in the wing wake sees a dynamic pressure reduced by the tail efficiency factor,

$$\eta_t = \frac{q_t}{q_\infty} < 1$$

and an incidence reduced by the downwash,

$$\alpha_t = \alpha \left( 1 - \frac{d\varepsilon}{d\alpha} \right) + i_t - \varepsilon_0, \qquad \frac{d\varepsilon}{d\alpha} \approx \frac{2 C_{L\alpha_w}}{\pi A}$$

so that everything the tail contributes is scaled by two factors the wing controls. When a shock forms on the wing and the wake thickens, both degrade, and the tail loses authority through no fault of its own geometry. At an aspect ratio of 3.60 and a wing lift-curve slope of 4.0 per radian the downwash derivative is

$$\frac{d\varepsilon}{d\alpha} = \frac{2 \times 4.0}{\pi \times 3.60} = 0.71$$

which means a conventional aircraft of this planform already loses 71 percent of its tail incidence to downwash before any transonic effect is considered. The hypothesis was not foolish. The second was constructive. [Northrop][ref_northrop_corp] had been building [tailless][ref_tailless] and [flying wing][ref_flying_wing] aircraft since the 1920s and had a body of practice arguing that the tail was drag and mass without compensating benefit, a position the [YB-49][ref_yb49] represented at large scale and the wartime German [Me 163][ref_me163] at small.

The transient form of the mechanism had been written down before the war. [Jones and Fehlner 1940][research_jones_fehlner_1940] treat the wake arriving at the horizontal tail as a time-dependent problem and not a steady one, which is the correct framing when the disturbance is a shock system that forms, moves, and collapses, not a fixed deflection of the flow. Steady downwash behind a sharply swept wing at transonic speed was later measured by placing a tail in it and weighing the result, which is the method of [Coppolino 1952][research_coppolino_1952], while the trim and dynamic response of a tail so placed were obtained by [Luoma 1953][research_luoma_1953]. Considered as turbulence and not as a mean deflection, the wake is characterized by [Campbell 1957][research_campbell_1957]. What this body of work eventually established is that tail height relative to the wake is the governing geometric variable, a result reached from transonic wind-tunnel measurements by [Fisher and Williams 1958][research_fisher_williams_1958] and again by [Wakefield 1959][research_wakefield_1959]. A conventional layout can therefore escape the mechanism by moving the surface out of the wake. That is the remedy the X-4 forgoes, since it has no surface to move. The measurement has not gone away, and [Hoang and Bui 2019][research_hoang_bui_2019] report experimental and numerical work on wingtip and downwash effects at a horizontal tail that would be recognizable to the authors of the wartime reports, conducted with instrumentation they did not have.

The NACA had been studying the configuration for years before the X-4 flew. [Donlan 1944][research_tailless_interim_1944] is an interim report on the stability and control of tailless airplanes that predates the X-4 by four years, with the high-speed model work of [Laitone 1943][research_tailless_highspeed_1943] and the all-wing investigations of [Seacord and Campbell 1945][research_allwing_stability_1945] and [Ankenbruck 1945][research_allwing_modifications_1945] alongside it. The case for the configuration had been in print for over a decade, [Dufaure De Lajarte 1936][research_delajarte_1936] setting out its claimed advantages in a paper the NACA thought worth translating, and the lateral consequences of accepting it had been calculated by [Harper and Jones 1947][research_harper_jones_1947] the year before the X-4 flew. Model work ran alongside, from the free-flight tunnel study of a tailless glider by [Johnson 1949][research_johnson_glider_1949] to the low-aspect-ratio swept fighter model of [Smith 1953][research_smith_tailless_1953]. The question was live and the answer was not known.

What the hypothesis omitted is that a horizontal tail does two jobs, and the debate had been conducted almost entirely about the first. The tail trims the aircraft and it provides pitch control, which is the job everyone discussed. It also provides pitch damping, which is the job nobody weighed, and Sizing From First Principles shows that the second contribution is the larger one by an order of magnitude.

## Programme Origin

The Air Force ordered two aircraft from Northrop in 1946 under a contract for a semitailless transonic research aeroplane, serials 46-676 and 46-677. The first flew on 15 December 1948 with Northrop pilot Charles Tucker at the controls.

The configuration is small and clean. A swept wing of 18.58 square metres and 8.18 metres span carries [elevons][ref_elevon] for combined pitch and roll control, a vertical fin and rudder provide directional control, and there is no horizontal surface at all. The aircraft is 7.09 metres long and grosses 3547 kilograms. Two [Westinghouse J30][ref_j30] turbojets of about 1600 pounds thrust each are buried in the fuselage, giving

$$T = 2 \times 1600 \times 4.448 = 1.42 \times 10^{4} \ \text{newtons}, \qquad \frac{T}{W} = \frac{1.42 \times 10^{4}}{3547 \times 9.80665} = 0.41$$

which is low, and the X-4 was never expected to exceed about Mach 0.95 in level flight. That is a deliberate choice, not a limitation the programme regretted. The research question lives between Mach 0.85 and Mach 0.95, so an aircraft that reaches that band and no further is adequate to it, and the [X-3][related_post_a300_douglas_x3] demonstrates what happens when a research aircraft is asked to do something its engines cannot.

The aspect ratio and wing loading follow as

$$A = \frac{b^2}{S} = \frac{8.18^2}{18.58} = 3.60, \qquad \frac{W}{S} = \frac{3547 \times 9.80665}{18.58} = 1872 \ \text{newtons per square metre}$$

which is a modest wing loading by the standards of this series and reflects an aircraft sized for a flight regime and not for a speed record. The stall and approach speeds that follow are correspondingly gentle,

$$V_{\text{stall}} = \sqrt{\frac{2 W}{\rho S C_{L,\max}}}, \qquad V_{\text{app}} = 1.3 \, V_{\text{stall}}$$

and at a maximum lift coefficient near 1.0 for a swept planform without high-lift devices the stall speed is 55 metres per second, giving an approach near 72. That is unremarkable, and it is a deliberate contrast with the [X-3][related_post_a300_douglas_x3], whose configuration made every landing an event. A research aircraft whose purpose is to be flown repeatedly at a particular condition benefits from being easy to bring home. The qualification a tailless planform attaches to that statement is ground effect, which alters the pitching moment as well as the lift and therefore acts on the axis that has no surface to trim it. [Buell and Tinling 1957][research_buell_tinling_1957] measured the longitudinal consequences for low aspect ratio wings with pointed tips, and [Drinkwater et al 1970][research_drinkwater_1970] later put a pilot in a simulator to examine the landing manoeuvre of a large tailless delta in the same regime.

The aircraft carried split flaps that doubled as speed brakes, a device whose aerodynamic design had been worked out for other airframes by [Purser and Turner 1941][research_purser_turner_1941]. That fitting matters more than it appears, and it gave the programme a second research role treated below.

The manoeuvre envelope follows from the same wing loading,

$$n(V) = \frac{\rho V^2 C_{L,\max}}{2 \left( W / S \right)}, \qquad V_A = \sqrt{\frac{2 n_{\max} W}{\rho S C_{L,\max}}}$$

with the corner speed low enough that the aircraft could reach useful load factors throughout its envelope.

## Sizing From First Principles

The keystone relationship is the pitch damping derivative, and the derivation explains the entire outcome of the programme.

Pitch damping resists a pitch rate. A surface at distance $l_t$ behind the centre of gravity, when the aircraft pitches at rate $q_r$, sees an incremental angle of attack

$$\Delta \alpha_t = \frac{q_r \, l_t}{V}$$

because the surface is moving downward through the air at $q_r l_t$ while the aircraft translates at $V$. That incremental angle produces an incremental lift, which produces a moment opposing the rotation. Non-dimensionalizing gives the tail contribution to the pitch damping derivative,

$$C_{m q, \text{tail}} = -2 \, \eta_t \, C_{L \alpha_t} \, V_H \, \frac{l_t}{\bar{c}}, \qquad V_H = \frac{S_t \, l_t}{S \, \bar{c}}$$

with $V_H$ the horizontal tail volume coefficient, $\eta_t$ the tail efficiency, and $C_{L\alpha_t}$ the tail lift-curve slope. The crucial feature is that $l_t$ appears **twice**, once in the tail volume coefficient and once in the incremental angle of attack, so the tail contribution scales as the square of tail length. Writing it out in geometric terms makes the dependence explicit,

$$C_{m q, \text{tail}} = -2 \, \eta_t \, C_{L \alpha_t} \, \frac{S_t}{S} \left( \frac{l_t}{\bar{c}} \right)^2$$

which shows that doubling the tail arm at constant tail area quadruples the damping contribution while only doubling the control contribution. The two jobs of a tail therefore scale differently with the same geometric parameter, which is precisely why a debate conducted about control reached the wrong conclusion about damping.

The wing contributes damping too, but weakly, and the two ways in which it can are worth separating.

The first is a parallel-axis term, which is the relation derived above applied to the wing's own lift acting at its aerodynamic centre. Setting the area ratio to unity and the arm to the static margin gives

$$C_{m q, \text{wing, offset}} = -2 \, C_{L\alpha_w} \left( \frac{x_{ac} - x_{cg}}{\bar{c}} \right)^2 = -2 \times 4.0 \times 0.05^2 = -0.02$$

which is negligible, because the arm is a few percent of a chord where the tail's is a few chords and the dependence is quadratic. This term vanishes entirely when the centre of gravity sits at the aerodynamic centre.

The second does not vanish there. A wing pitching at rate $q_r$ sees an incidence that varies linearly along its chord, and the resulting load distribution produces a moment about the rotation point even though the incremental incidence largely cancels in the net. Quasi-steady thin aerofoil theory returns a quantity of order unity for rotation about the quarter chord, and a low aspect ratio swept planform returns rather less. It is this second contribution, larger than the first by a factor of roughly forty, that supplies the wing-alone figure used below, and it is adopted as representative, not derived from this airframe. Both terms together remain small against a tail, which is the point.

Evaluate for a conventional configuration with $\eta_t = 0.9$, $C_{L\alpha_t} = 4.0$ per radian, $V_H = 0.6$, and $l_t / \bar{c} = 3.0$,

$$C_{m q, \text{tail}} = -2 \times 4.0 \times 0.9 \times 0.6 \times 3.0 = -13.0$$

against a wing-alone contribution for a swept planform of order

$$C_{m q, \text{wing}} \approx -0.8$$

so that a conventional aircraft draws about

$$\frac{13.0}{13.0 + 0.8} = 94 \ \text{percent}$$

of its pitch damping from the tail. Remove the tail and 94 percent of the damping goes with it. That is the finding of the X-4 programme, available on paper before the X-4 was built, and it is not what the debate had been about.

That the moment of inertia in pitch and the damping available jointly fix the character of the mode was among the first things flight research established, in [Norton and Carroll 1922][research_norton_carroll_1922] and the flight study of [Norton 1924][research_norton_1924]. [Soule and Wheatley 1934][research_soule_wheatley_1934] set calculated longitudinal stability against measurement on a real airframe, and [Soule 1937][research_soule_1937] took the further step of correlating measured dynamic longitudinal stability with what pilots said about the aircraft, which is the intellectual ancestor of everything the X-4 programme later reported. By the time the X-4 was designed the free-control complications had been treated theoretically by [Greenberg and Sternfield 1944][research_greenberg_sternfield_1944] and in flight by [Phillips 1942][research_phillips_shortperiod_1942], with a control-feel remedy demonstrated on a fighter by [Johnson 1946][research_johnson_p63_1946]. None of that literature contemplated removing the damping surface altogether.

The consequence appears in the short period mode. The dimensional derivatives are

$$M_\alpha = \frac{q S \bar{c} \, C_{m\alpha}}{I_y}, \qquad M_q = \frac{q S \bar{c}^2 \, C_{mq}}{2 I_y V}, \qquad Z_\alpha = -\frac{q S \, C_{L\alpha}}{m}$$

and the short period frequency and damping ratio are

$$\omega_{sp} \approx \sqrt{-M_\alpha}, \qquad \zeta_{sp} = -\frac{M_q + M_{\dot\alpha} + Z_\alpha / V}{2 \omega_{sp}}$$

The atmosphere used throughout is the troposphere model,

$$T(h) = T_0 - \lambda h, \qquad p(h) = p_0 \left( \frac{T(h)}{T_0} \right)^{g / \lambda R}, \qquad \rho = \frac{p}{R T}$$

with $\lambda = 0.0065$ kelvin per metre, and the speed of sound follows as

$$a = \sqrt{\gamma R T}$$

Take the X-4 at Mach 0.9 and 9144 metres, where this gives a static pressure of 30,089 pascals, a temperature of 228.7 kelvin, a speed of sound of 303.1 metres per second, and therefore

$$q = \frac{\gamma}{2} p M^2 = 0.7 \times 30{,}089 \times 0.81 = 1.71 \times 10^{4} \ \text{pascals}$$

With a radius of gyration in pitch of 2.13 metres, giving $I_y = 1.60 \times 10^{4}$ kilogram square metres, a lift-curve slope of 4.0 per radian, and a static margin of 5 percent so that $C_{m\alpha} = -0.20$,

$$M_\alpha = -8.99 \ \text{per second squared}, \qquad \omega_{sp} = 3.00 \ \text{radians per second}$$

which is a period of

$$T_{sp} = \frac{2 \pi}{\omega_{sp}} = 2.1 \ \text{seconds}$$

and a damped frequency of

$$\omega_d = \omega_{sp} \sqrt{1 - \zeta^2}$$

which differs from the undamped value by less than three percent at the tailless damping ratio derived below, though by about a third at the tailed value, so the undamped frequency is used for both and the half-amplitude count that follows carries the damped factor explicitly. The damping term is where the configurations part company. For the tailless case, with $C_{mq} = -0.8$ and $M_{\dot\alpha} \approx 0$ because the downwash lag that produces $M_{\dot\alpha}$ acts on a tail that does not exist,

$$\zeta_{sp, \text{tailless}} = 0.244$$

For an otherwise identical aircraft with a tail, taking $C_{mq} = -13$ and $M_{\dot\alpha}$ corresponding to a downwash lag term of $-4$,

$$\zeta_{sp, \text{tailed}} = 0.749$$

a factor of 3.1. Both figures are stable. Neither is a prediction of disaster. The same calculation is still performed on tailless configurations, and [Kwiek 2019][research_kwiek_2019] is a numerical study of exactly this quantity for a tailless layout, arriving by computation at the class of result the X-4 established by flying. The static margin on which it depends turns out to be less straightforward for a three-dimensional configuration than the one-dimensional definition used here suggests, a point [Schmidt et al 2025][research_schmidt_static_margin_2025] develop. The X-4 was not an aircraft that oscillated uncontrollably at every condition, and any account claiming it was has overstated the case.

It is worth writing the mode down properly and not through its summary parameters. Retaining the two-degree-of-freedom short period approximation, the characteristic equation is

$$\lambda^2 - \left( M_q + M_{\dot\alpha} + \frac{Z_\alpha}{V} \right) \lambda + \left( \frac{Z_\alpha M_q}{V} - M_\alpha \right) = 0$$

whose roots are

$$\lambda_{1,2} = -\zeta_{sp} \omega_{sp} \pm i \, \omega_{sp} \sqrt{1 - \zeta_{sp}^2}$$

so the real part is the decay rate and the imaginary part the oscillation frequency. The time to half amplitude follows directly,

$$t_{1/2} = \frac{\ln 2}{\zeta_{sp} \omega_{sp}}$$

which for the tailless case is 0.95 seconds and for the tailed case 0.31. A pilot making a correction every second is inside the settling time of his own aircraft in the first case and outside it in the second, and that is the difference between an aircraft that responds and one that hunts.

There is a second way to state the result, in the language the discipline eventually adopted, and it is worth doing because it closes the argument.

Short-period handling qualities are now specified by a pair of numbers. The first is the damping ratio itself. The second is the control anticipation parameter, which relates the initial pitch acceleration a pilot commands to the steady load factor he eventually gets,

$$\text{CAP} = \frac{\omega_{sp}^2}{n / \alpha}, \qquad \frac{n}{\alpha} = \frac{C_{L\alpha} \, q \, S}{W}$$

with $n/\alpha$ in units of load factor per radian. For the X-4 at the condition above,

$$\frac{n}{\alpha} = \frac{4.0 \times 17{,}061 \times 18.58}{34{,}784} = 36.5 \ \text{per radian}, \qquad \text{CAP} = \frac{3.00^2}{36.5} = 0.247$$

The criteria place Level 1, meaning handling adequate for the mission without pilot compensation, at a damping ratio between roughly 0.35 and 1.30 with the control anticipation parameter between roughly 0.28 and 3.6 for a precision-tracking task. **The X-4 computes to a damping ratio of 0.244, which is below the Level 1 floor and at the boundary between Level 2 and Level 3, with a control anticipation parameter of 0.247, marginally below its Level 1 band as well.** The tailed comparison at 0.749 sits comfortably inside Level 1 on both counts.

Those criteria postdate the aircraft by two decades and are quoted here as a restatement, not as a standard the programme was judged against. What they establish is that the pilots who called the X-4 unsatisfactory were not being fastidious. The configuration lands outside the band the discipline later drew, and it does so on the axis the tail would have supplied.

The retrospective character of that comparison can be reduced, and it is worth reducing. A criterion of the same kind existed at the time. [Sternfield and Gates 1949][research_sternfield_gates_1949] give a method for constructing a boundary in the plane of period against damping that separates satisfactory from unsatisfactory oscillatory behaviour, published the year before the NACA began flying this aircraft. The construction is cruder than the later work and is stated in terms of period and time to damp and not of frequency and damping ratio, but it is a numerical acceptability boundary contemporaneous with the programme rather than a standard imported from the following generation. The X-4 result is therefore not merely unsatisfactory by a rule invented afterward. It was measurable against a rule that existed while the X-4 was flying, which supports the reading that the pilot reports were describing something the discipline already knew how to name.

The finding is about **margin** rather than about stability, and it can be stated exactly. Transonic flight degrades every aerodynamic derivative, through shock-induced separation, through aerodynamic centre migration, and through the collapse of control effectiveness described at length in the [X-1 article][related_post_a298_bell_x1]. Ask how much degradation each configuration tolerates before the damping ratio falls to a nominal 0.05, at which point the aircraft is effectively undamped. Writing $f$ for the fraction of nominal damping remaining,

$$\zeta = f \, \zeta_{\text{nominal}} = 0.05 \quad \Longrightarrow \quad f = \frac{0.05}{\zeta_{\text{nominal}}}$$

$$f_{\text{tailless}} = \frac{0.05}{0.244} = 0.205, \qquad f_{\text{tailed}} = \frac{0.05}{0.749} = 0.067$$

so the tailless configuration becomes effectively undamped once its damping derivatives have fallen to 21 percent of their nominal value, while the tailed aircraft tolerates a fall to 7 percent. **The tailless configuration has no damping margin to spend, and the transonic band is exactly where margin gets spent.** That is the answer to the keystone, and it is a quantitative answer rather than a verdict.

The oscillation that results is characterized by the number of cycles to half amplitude,

$$N_{1/2} = \frac{\ln 2}{2 \pi} \cdot \frac{\sqrt{1 - \zeta^2}}{\zeta}$$

which for the nominal tailless value is 0.44 cycles and for the tailed value 0.10, and which grows without bound as $\zeta$ approaches zero. An aircraft taking many cycles to damp a disturbance is one a pilot describes as hunting or porpoising, and that is the word the X-4 pilots used.

The description is closed-loop rather than open-loop, and that distinction matters. A pilot correcting a lightly damped oscillation introduces his own lag, and the crossover model represents the combined pilot and aircraft as

$$Y_p Y_c \approx \frac{\omega_c \, e^{-\tau_e s}}{s}$$

near the crossover frequency $\omega_c$, with $\tau_e$ the effective pilot time delay. The phase margin available is

$$\phi_m = \frac{\pi}{2} - \omega_c \tau_e$$

and it vanishes when $\omega_c \tau_e$ approaches ninety degrees. The delay itself is conveniently represented for analysis by a first-order Pade approximation,

$$e^{-\tau_e s} \approx \frac{1 - \tau_e s / 2}{1 + \tau_e s / 2}$$

whose right-half-plane zero is the formal statement of why a delay cannot be compensated away. A pilot delay near 0.25 seconds and a crossover frequency near 3 radians per second consume

$$\omega_c \tau_e = 0.75 \ \text{radians} = 43 \ \text{degrees}$$

of phase before any aircraft dynamics are considered, which leaves under fifty degrees of margin for everything else. An aircraft that will not settle forces the pilot to raise his gain, which raises $\omega_c$, which consumes phase margin, which is the mechanism of pilot-induced oscillation. A lightly damped short period is therefore not merely uncomfortable. It invites the pilot into an instability that neither he nor the aircraft has alone. The modern treatment of exactly this is [Efremov et al 2020][research_efremov_2020] and [Bidinotto et al 2021][research_bidinotto_2021].

## Dependent Systems

### The Wing and the Absent Tail

Everything about the configuration follows from having no horizontal surface.

The lift-curve slope of a swept low aspect ratio wing is not the two-dimensional value and must be estimated from the planform. The standard form is

$$C_{L\alpha} = \frac{2 \pi A}{2 + \sqrt{ \dfrac{A^2 \beta_s^2}{\kappa^2} \left( 1 + \dfrac{\tan^2 \Lambda_{c/2}}{\beta_s^2} \right) + 4 }}, \qquad \beta_s = \sqrt{1 - M^2}$$

with $\Lambda_{c/2}$ the half-chord sweep and $\kappa$ the ratio of the section lift-curve slope to $2\pi$. At an aspect ratio of 3.60 this returns a value near 4.0 per radian at low Mach number, rising with the compressibility factor as Mach number increases, which is the figure used throughout. Longitudinal stability must come from the wing alone, so the aerodynamic centre and the centre of gravity relationship is the whole of the static margin,

$$SM = \frac{x_{np} - x_{cg}}{\bar{c}}, \qquad C_{m\alpha} = -C_{L\alpha} SM$$

There are two such margins and the distinction matters for a tailless design. The static margin governs response to a change of angle of attack at constant speed. The manoeuvre margin governs response in a pull-up, where the aircraft is also rotating and the pitch damping therefore contributes a restoring moment of its own,

$$MM = SM - \frac{C_{mq}}{2 \mu}, \qquad \mu = \frac{2m}{\rho S \bar{c}}$$

with $\mu$ the relative density parameter. At the flight condition $\mu = 367$, so the tailless case has

$$MM_{\text{tailless}} = 0.05 + \frac{0.8}{734} = 0.0511$$

against

$$MM_{\text{tailed}} = 0.05 + \frac{13.0}{734} = 0.0677$$

The tail contributes 1.7 points of manoeuvre margin that the tailless configuration simply does not have, which is a second and independent consequence of the same missing damping term. The stick force per unit load factor follows the manoeuvre margin directly,

$$\frac{F_s}{n} \propto MM$$

so a tailless design is also lighter in pitch than its static margin suggests, which compounds the tendency of a pilot to over-control it.

For a tailless layout the neutral point is essentially the wing aerodynamic centre, since the term that a tail would contribute,

$$\Delta \frac{x_{np}}{\bar{c}} = V_H \frac{C_{L\alpha_t}}{C_{L\alpha_w}} \left( 1 - \frac{d\varepsilon}{d\alpha} \right)$$

is zero. A conventional aircraft can place its centre of gravity over a wide range and recover stability with tail volume. A tailless one cannot, and the constraint can be written down. The aft limit is set by stability,

$$x_{cg, \text{aft}} = x_{np} - SM_{\min} \bar{c}$$

and the forward limit by the control power available to trim at maximum lift,

$$x_{cg, \text{fwd}} = x_{ac} - \frac{\left| C_{m \delta_e} \right| \delta_{e, \max}}{C_{L, \max}} \bar{c}$$

so the usable range is the difference,

$$\Delta x_{cg} = \left[ \frac{\left| C_{m \delta_e} \right| \delta_{e, \max}}{C_{L, \max}} - SM_{\min} \right] \bar{c} + \left( x_{np} - x_{ac} \right)$$

in which the final term is the tail contribution and is zero for a tailless layout. Both bounds therefore collapse toward the wing aerodynamic centre, and the range is set entirely by how much control power the elevons can supply against how much stability is demanded. Fuel burn or store release that moves the centre of gravity a few percent of chord is a large fraction of that range. Sweep supplies what tail volume otherwise would, since a swept wing places its outboard sections aft and washout at the tip generates the nose-up moment at zero lift that trim requires,

$$C_{m0} > 0$$

which a conventional aircraft obtains from tail incidence and a tailless design must build into the wing itself. The twist distribution that supplies it is conventionally linear in span,

$$\varepsilon_t(y) = \varepsilon_{\text{tip}} \frac{2y}{b}$$

and the pitching moment it generates on a wing of sweep $\Lambda$ is approximately

$$C_{m0} \approx -\frac{C_{L\alpha} \, \varepsilon_{\text{tip}} \tan \Lambda}{6}$$

so the required washout scales inversely with sweep, and a lightly swept tailless wing needs a great deal of it. The span efficiency that the resulting non-elliptic loading costs can be estimated from

$$e \approx 1.78 \left( 1 - 0.045 A^{0.68} \right) - 0.64$$

which at an aspect ratio of 3.60 returns 0.95 before the trim penalty is applied, against 0.84 for an aspect ratio of seven, so that the induced drag at a given lift coefficient exceeds the higher aspect ratio case by

$$\frac{C_{D,i}(A = 3.6)}{C_{D,i}(A = 7)} = \frac{7 \times 0.84}{3.6 \times 0.95} = 1.7$$

a penalty the configuration pays permanently. The efficiency factor used here is the one [Oswald 1932][research_oswald_1932] introduced for this purpose, a single multiplier absorbing every departure of the spanwise loading from elliptic, and the correlation above is a later fit to the quantity he defined. Reflexed or washed-out sections generate the trimming moment by carrying negative lift outboard, so the loading departs from elliptic in exactly the manner the factor is meant to absorb, and the induced drag rises above the minimum,

$$C_{D,i} = \frac{C_L^2}{\pi A e}, \qquad e < 1$$

with the efficiency factor $e$ degraded in proportion to the departure. The trim penalty can be written as an equivalent drag increment,

$$\Delta C_{D, \text{trim}} = \frac{C_{m0}^2}{\pi A e} \left( \frac{\bar{c}}{\ell_{\text{eff}}} \right)^2$$

with $\ell_{\text{eff}}$ the effective moment arm over which the trim load acts, which for a tailless layout is a fraction of a chord and for a conventional one is several chords. The penalty therefore scales as the inverse square of the available arm, and it is the permanent cost of the configuration. That cost is real and permanent. The wing modification studies of [Ankenbruck 1945][research_allwing_modifications_1945] are largely about paying it as cheaply as possible.

The aerodynamic centre migrates aft through the transonic band, typically from the quarter chord to near the half chord,

$$\frac{x_{ac}}{\bar{c}} : 0.25 \longrightarrow 0.50$$

and for a tailless design this migration is the entire change in static margin, unmoderated by a tail. The trim change that results must be absorbed by the elevons, and the trim moment increment at lift coefficient $C_L$ is

$$\Delta C_m = C_L \frac{\Delta x_{ac}}{\bar{c}}$$

which at a cruise lift coefficient of 0.3 and a quarter-chord migration is 0.075. Tailless aircraft therefore experience a large trim change through Mach one with a control surface that is simultaneously losing effectiveness, and the elevon deflection needed to absorb it is

$$\delta_e = \frac{\Delta C_m}{\left| C_{m \delta_e} \right|}$$

which for a tailless aircraft with a control power of order 0.5 per radian requires 0.15 radians, or nearly nine degrees, of the available deflection consumed by trim alone before any manoeuvring. This is a worse version of the problem the [X-1][related_post_a298_bell_x1] met and solved with an all-moving tail the X-4 does not have.

### Elevons and the Sharing of Authority

An [elevon][ref_elevon] is an aileron and an elevator in the same surface, and the two functions compete for the same deflection.

Symmetric deflection produces pitch and differential deflection produces roll, so for a left and right surface

$$\delta_L = \delta_e + \delta_a, \qquad \delta_R = \delta_e - \delta_a$$

and each surface is bounded by its mechanical limit,

$$\left| \delta_e \right| + \left| \delta_a \right| \le \delta_{\max}$$

The pitch authority available at any instant is therefore

$$\delta_{e, \text{available}} = \delta_{\max} - \left| \delta_a \right|$$

so a full roll input consumes the entire pitch authority. A conventional layout has independent surfaces and no such coupling. This matters most in exactly the situation where it is least welcome, since a pilot correcting a roll disturbance in the transonic band gives away the pitch authority he may need in the next second.

Differential deflection also produces yaw, and on a swept wing the sign is unfavourable. The down-going elevon adds lift and therefore induced drag on the rising wing, yawing the aircraft away from the intended turn,

$$C_{n \delta_a} \approx -K \, C_L \, C_{l \delta_a}$$

with $K$ of order 0.1 to 0.2 and the negative sign denoting adverse yaw. A tailless aircraft with a small fin has little directional stiffness with which to resist that yaw, so roll and yaw are coupled more strongly than on a conventional configuration, and the sideslip that results feeds back into roll through the dihedral effect $C_{l\beta}$.

Rolling effectiveness through the transonic band was among the better-mapped quantities of the period, because rocket-propelled free-flight models could supply it cheaply. [Sandahl 1948][research_sandahl_delta_1948] covers delta planforms, and a companion study by the same author treats a forty-two degree sweptback wing with partial-span ailerons in [Sandahl 1948][research_sandahl_swept_1948]. Those studies established that effectiveness falls sharply and can reverse, and the reversal mechanism is structural rather than aerodynamic. [Harman 1944][research_harman_1944] had already determined the effect of wing flexibility on lateral manoeuvrability and compared calculated rolling effectiveness against flight, which is the calculation that predicts aileron reversal. A related failure appears at the wing rather than at the control surface. Wing dropping on straight and swept planforms was measured with rocket models by [Stone 1950][research_stone_1950], and the same tendency was recorded in flight on a thirty-five degree swept aircraft, together with its lateral-control consequences, by [Winograd Cooper Rathert and Rolls 1950][research_winograd_1950]. A tailless aircraft meets all of this with elevons that are simultaneously its elevator.

The swept planform brings its own longitudinal hazard. Tip stall on a swept wing removes lift from the aft-most part of the surface, moving the centre of pressure forward and generating a nose-up increment. The pitch-up boundary is conventionally located where

$$\frac{\partial C_m}{\partial C_L} > 0$$

which for a swept wing occurs at moderate lift coefficients and which a tail would ordinarily counter. The phenomenon was documented across the swept-wing fleet of the period. [Spooner and Martina 1948][research_spooner_martina_1948] measured it on a forty-two degree sweptback wing and tail combination at a Reynolds number high enough to be credible, [Anderson and Bray 1955][research_anderson_bray_1955] recorded it in flight during manoeuvres at transonic speed, and [Queijo et al 1954][research_queijo_fences_1954] established that chordwise fences and tail position both bear on it, which are two remedies a tailless design cannot use. Downwash and longitudinal stability were mapped together on a triangular planform by [Allen 1951][research_allen_1951]. Stall behaviour on this aircraft was measured for exactly that reason in [Sadoff and Sisk 1950][research_x4_stall_1950], and the automatic intervention that later programmes adopted appears in [Hurt and Whitten 1960][research_pitchup_control_1960].

The control power itself is

$$C_{m \delta_e} = -\frac{\partial C_L}{\partial \delta_e} \cdot \frac{x_{cp} - x_{cg}}{\bar{c}}$$

and for a tailless configuration the moment arm $x_{cp} - x_{cg}$ is a fraction of a chord rather than several chords, so the elevon must generate a large force to produce a modest moment. That is the second structural disadvantage of the configuration, and it compounds the first, since a large force from a short arm means large hinge moments,

$$H = q \, S_e \, c_e \, C_h$$

and correspondingly large stick forces,

$$F_s = G \, H = G \, q \, S_e \, c_e \, C_h, \qquad C_h = C_{h_0} + C_{h\alpha} \alpha + C_{h\delta} \delta_e$$

with $G$ the control system gearing. The effectiveness parameter relating surface deflection to an equivalent change of incidence follows thin-airfoil theory,

$$\tau = 1 - \frac{\theta_h - \sin \theta_h}{\pi}, \qquad \cos \theta_h = 2 \frac{c_e}{c} - 1$$

and aerodynamic balance, in which part of the surface projects ahead of the hinge line, reduces the hinge moment without reducing the effectiveness,

$$C_{h\delta, \text{balanced}} = C_{h\delta} \left[ 1 - \left( \frac{c_b}{c_e} \right)^2 \right]$$

with $c_b$ the balance chord. That relation is why the blunt trailing edge experiment of [Saltzman 1955][research_x4_blunt_elevons_1955] was worth trying, since it attacks the same coefficient from the other end of the surface. Because $H$ scales with dynamic pressure while the required moment scales with the same quantity, the stick force per unit load factor is roughly constant, but the hinge moment derivatives themselves change sign through the transonic band as the shock crosses the hinge line, so the force the pilot feels ceases to be a reliable indication of what the surface is doing. That is the same failure the [X-1][related_post_a298_bell_x1] met, and a tailless aircraft cannot escape it by moving the whole surface, because the whole surface is the wing. The X-4 was fitted at one point with blunt trailing edge elevons intended to modify the hinge moment characteristics, an experiment reported in [Saltzman 1955][research_x4_blunt_elevons_1955]. The idea was not peculiar to this aircraft. [Underwood 1942][research_underwood_1942] had noted a decade earlier that trailing-edge shape bears on profile drag and on the trim and balance of control surfaces together, and [Sadoff et al 1954][research_sadoff_blunt_te_1954] applied blunt trailing edge modifications to a swept-wing fighter and measured the high-speed stability and control consequences, which is the same experiment performed on a conventional airframe. Elevon effectiveness at transonic speed remained a research subject long afterward, as [Transonic control effectiveness for 1977][research_elevon_transonic_1977] shows.

### Directional Stability and the Fin

The vertical fin is the only tail surface, and it carries the whole directional problem,

$$C_{n\beta} = V_V \, C_{L\alpha_v} \, \eta_v, \qquad V_V = \frac{S_v \, l_v}{S \, b}$$

with the same square-of-arm sensitivity that governs pitch damping, since the yaw damping derivative is

$$C_{n r, \text{fin}} = -2 \, \eta_v \, C_{L\alpha_v} \, V_V \, \frac{l_v}{b}$$

A short aircraft has a short $l_v$, so a tailless design must buy directional stability with fin area rather than with arm, and area is drag. The fin location and area tradeoff was studied directly in [NACA 1951][research_vertical_fin_location_1951], with the interaction between fuselage and tail surfaces in [Bird et al 1951][research_fuselage_tail_yawing_1951]. The interference among wing, fuselage, and fin that complicates any such sizing had been measured systematically by [House and Wallace 1941][research_house_wallace_1941], and the dependence of the static lateral and directional characteristics on aspect ratio for swept midwing configurations by [Thomas and Wolhart 1957][research_thomas_wolhart_1957]. Fin placement forward of the usual station was examined under both steady and oscillatory conditions by [Queijo and Wells 1956][research_queijo_wells_1956], a distinction that matters because the damping-in-yaw derivative and the static derivative need not scale together. A swept configuration close to the X-4 in planform, though carrying a horizontal tail, is characterized in [Schuldenfrei et al 1947][research_schuldenfrei_1947]. Modern tailless aircraft, which have no fin at all, must generate yaw by other means entirely, and that literature is treated below.

The long-period longitudinal mode completes the set. The [phugoid][ref_phugoid] is an exchange of altitude and speed at nearly constant angle of attack, with frequency and damping

$$\omega_{ph} \approx \frac{g \sqrt{2}}{V}, \qquad \zeta_{ph} \approx \frac{1}{\sqrt{2}} \frac{1}{L / D}$$

which at 273 metres per second gives a period near 124 seconds. That is long enough to be irrelevant to the hunting problem and long enough for a pilot to manage without effort, so the tailless configuration costs nothing here. The absence of a penalty is worth stating, because it locates the damage precisely in the short period rather than in longitudinal behaviour generally.

The [Dutch roll][ref_dutch_roll] mode that results has frequency and damping

$$\omega_{dr} \approx \sqrt{\frac{q S b \, C_{n\beta}}{I_z}}, \qquad \zeta_{dr} \propto -C_{nr}$$

with the damping ratio

$$\zeta_{dr} \approx -\frac{1}{2} \left( \frac{C_{nr}}{\sqrt{ \left( q S b \, C_{n\beta} / I_z \right)}} \right) \frac{q S b^2}{2 I_z V}$$

and it inherits the same margin problem as the short period, since a configuration short of $C_{nr}$ has nothing to lose when the transonic band takes some away. The roll mode and spiral complete the lateral set,

$$\tau_r = -\frac{2 I_x V}{q S b^2 C_{lp}}, \qquad L_\beta N_r - L_r N_\beta > 0$$

the last being the spiral stability condition, which a swept wing with strong dihedral effect and a small fin tends to violate. Extracting these derivatives from flight records rather than assuming them is a discipline of its own, and the method of [Klawans and White 1957][research_klawans_white_1957] uses the spiral, roll-subsidence, and Dutch roll modes together to determine the lateral derivatives from measured motion, which is the lateral counterpart of the logarithmic decrement treatment given below. The coupling that arises when a rolling manoeuvre drives an aircraft across its inertia axes was studied on an analogue computer by [Gillis 1957][research_gillis_1957], and it is the same phenomenon that dominated the [X-3][related_post_a300_douglas_x3] programme.

### Propulsion and Envelope

The two buried [Westinghouse J30][ref_j30] engines are the least remarkable part of the aircraft and are adequate to its purpose. The thrust available at altitude lapses roughly with ambient pressure and ram recovery,

$$\frac{T(h, M)}{T_{SL}} \approx \frac{p(h)}{p_{SL}} \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\frac{\gamma}{\gamma - 1}}$$

and the level-flight maximum Mach number follows from the thrust-drag balance,

$$M_{\max}^2 = \frac{2 T}{\gamma \, p \, S \, C_D}$$

The X-4 reached about Mach 0.92 in level flight and slightly more in a shallow dive, which places it squarely in the band the research question occupies. Where that figure sits among its contemporaries can be read from [Bellman 1959][research_bellman_1959], which collects flight-determined transonic lift and drag for several research airplane configurations and is the natural document against which to place any single aircraft of the group. The drag rise itself was under attack by reshaping during the same years, and [Holdaway 1954][research_holdaway_1954] reports an experimental reduction obtained by adding volume to a fuselage, compared against theory, which is the area rule stated as a measurement. The compressible behaviour of a flapped section underlying all of this is documented in [Lindsey 1946][research_lindsey_1946], and a calculation method spanning subsonic through supersonic speeds for complete configurations in [Nielsen et al 1953][research_nielsen_1953]. Specific excess power,

$$P_s = \frac{V \left( T - D \right)}{W}$$

falls to zero at the ceiling, and the climb angle available follows from the same excess,

$$\sin \gamma = \frac{T - D}{W}, \qquad \frac{dh_e}{dt} = P_s$$

with the energy height the natural coordinate,

$$h_e = h + \frac{V^2}{2 g}$$

With a thrust-to-weight of 0.41 the aircraft had modest but sufficient climb performance. Nothing about the propulsion installation constrains the answer to the keystone, which is a favourable contrast with the [X-3][related_post_a300_douglas_x3].

### Instrumentation

The programme measured a dynamic quantity rather than a static one, which changes the instrumentation requirement.

Static derivatives are obtained from trimmed points and averaging. Damping is obtained from the decay of a deliberately excited oscillation, so the aircraft must be disturbed in a repeatable way and the response recorded with enough bandwidth to resolve it. The standard excitation is a doublet, a paired control input of duration matched to the mode,

$$t_{\text{pulse}} \approx \frac{\pi}{2 \omega_{sp}} = 0.52 \ \text{seconds}$$

which concentrates the input energy near the natural frequency and leaves the aircraft to respond freely afterward. In the frequency domain the response is

$$\left| \frac{\theta(i\omega)}{\delta_e(i\omega)} \right| = \frac{\left| M_{\delta_e} \right|}{\sqrt{\left( \omega_{sp}^2 - \omega^2 \right)^2 + \left( 2 \zeta \omega_{sp} \omega \right)^2}}$$

whose peak amplitude at resonance is inversely proportional to the damping ratio,

$$\left| \frac{\theta}{\delta_e} \right|_{\max} \approx \frac{\left| M_{\delta_e} \right|}{2 \zeta \omega_{sp}^2}$$

so a lightly damped aircraft is easy to excite and hard to measure, which is the same asymmetry that appears in the decrement estimate below. For a short period at 3.0 radians per second, the frequency is

$$f_{sp} = \frac{\omega_{sp}}{2 \pi} = 0.48 \ \text{hertz}$$

and the [Nyquist criterion][ref_flight_test] requires

$$f_s > 2 f_{sp}$$

with practical rates an order of magnitude higher to resolve the decay envelope rather than merely detect the oscillation. Estimating a damping ratio from a decaying record uses the logarithmic decrement,

$$\delta_{\ln} = \frac{1}{n} \ln \frac{x_0}{x_n}, \qquad \zeta = \frac{\delta_{\ln}}{\sqrt{4 \pi^2 + \delta_{\ln}^2}}$$

and the uncertainty in $\zeta$ grows sharply as $\zeta$ falls, because a lightly damped record supplies little amplitude change per cycle to measure. Propagating through the relation gives

$$\frac{u(\zeta)}{\zeta} \approx \frac{1}{n \, \delta_{\ln}} \sqrt{ \left( \frac{u(x_0)}{x_0} \right)^2 + \left( \frac{u(x_n)}{x_n} \right)^2 }$$

so measuring exactly the quantity the programme cared about becomes harder precisely where the answer becomes interesting. That is an uncomfortable property of the experiment and it is why the flight records were reduced with unusual care.

Everything above presumes the flight condition is known, and at transonic speed that presumption is not free. Airspeed and altitude are inferred from pressures measured on a body that is itself disturbing the flow, and the error grows exactly where the shock system forms. The accuracy attainable and the calibration procedures available at the time are set out by [Huston 1948][research_huston_1948], the behaviour of a wing installation during dives to transonic speed by [Goodman 1949][research_goodman_1949], and the atmospheric complication that the temperature method must confront near the tropopause by [Lina and Ricker 1952][research_lina_ricker_1952]. An error in Mach number propagates into every derivative extracted at that condition, so this is not a peripheral concern for a programme whose finding is a function of Mach number. Angular measurement has its own instrument, and the air-flow-direction pickup developed for telemetering use by [Ikard 1956][research_ikard_1956] is representative of the class, with loads instrumentation of the same generation described by [Cooney and Schott 1956][research_cooney_schott_1956].

The general uncertainty relation is the usual

$$u_c^2(y) = \sum_i \left( \frac{\partial y}{\partial x_i} \right)^2 u^2(x_i)$$

and the modern descendants of this whole discipline, in which derivatives are extracted from flight data by maximum likelihood rather than from hand-reduced oscillation traces, appear in work on the design of optimal flight-test inputs in [Morelli 2021][research_morelli_2021], on the identification of an unstable tilt-rotor from flight data in [Lichota 2023][research_lichota_2023], and on maximum likelihood estimation of longitudinal and lateral derivatives in [Kumar and Ghosh 2023][research_kumar_ghosh_2023]. Longitudinal stability determined from flight test by system identification is treated by [Dias 2023][research_dias_2023], and the techniques as they now apply to small and inexpensive airframes by [Simmons et al 2023][research_simmons_sysid_2023]. The logarithmic decrement has not been abandoned so much as absorbed, since a maximum likelihood estimator fitted to a full response record uses every sample rather than the peaks alone and therefore recovers a lightly damped mode from data that would defeat a decrement taken by hand.

## The Flight Test Record

Two aircraft were built. 46-676 proved troublesome, suffered persistent mechanical problems, and was retired after about ten flights, its parts going to support the second machine. 46-677 flew the programme.

The Air Force phase established the envelope and the NACA phase measured it. The demonstration tests closing the acceptance phase are summarized by [Sadoff and Sisk 1950][research_sadoff_sisk_1950], the earliest consolidated statement of what the aircraft did. Longitudinal stability characteristics are reported in [Sadoff and Sisk 1950][research_x4_longitudinal_1950], stall behaviour in [Sadoff and Sisk 1950][research_x4_stall_1950], maximum lift and buffeting in [Baker 1953][research_x4_buffet_1953], and the consolidated flight evaluation of stability and control in [Sadoff and Crossfield 1954][research_x4_flight_evaluation_1954], which is the document that answers the keystone and should be read by anyone who wants the result rather than the summary.

The aircraft reached about Mach 0.92 and behaved acceptably through most of its envelope. Above roughly Mach 0.88 the longitudinal short period became progressively less damped and the X-4 developed a persistent low-amplitude oscillation in pitch that the pilots described as hunting or porpoising. It did not diverge. It did not need to. An aircraft that will not settle is an aircraft in which precise flying is impossible, and precise flying is what a transonic research aircraft exists to do.

The total flight count is reported inconsistently. Figures near 82 and near 102 both appear in reputable sources, and the difference is most plausibly whether the Air Force acceptance phase and the short career of the first airframe are counted, but no source consulted states its counting rule. The programme ended in 1953. The surviving aircraft is preserved at the National Museum of the United States Air Force.

The flight count matters less here than in most articles in this series, because the answer did not require statistical accumulation. The oscillation was reproducible, it appeared at a predictable condition, and its character was the same on every flight that reached it. A single well-instrumented flight established it and the remainder confirmed and bounded it.

Buffeting deserves to be separated from the damping question, because the two were easily confused in the cockpit and are distinct in origin. Buffet is a forced response to separated flow and does not require the aircraft to be lightly damped, whereas the hunting the X-4 pilots reported was a lightly damped free response to a disturbance. The buffet boundary of a comparable swept-wing aircraft at high altitude was established in flight by [Rathert et al 1951][research_rathert_1951], and the loads accompanying it were measured with strain gauges on a jet bomber by [Aiken and See 1951][research_aiken_see_1951] and on rocket-propelled models by [Mason 1953][research_mason_1953]. [Crabill 1956][research_crabill_1956] mapped lift, drag, static stability, and buffet boundaries together on a fighter model across the transonic range. The mechanism behind those empirical boundaries was not settled at the time and has since been reformulated as a question about the stability of the mean flow itself, with [Crouch et al 2019][research_crouch_2019] and [Timme 2020][research_timme_2020] locating buffet onset as a global instability rather than as a threshold in a correlation. That reframing is worth noting here because it is the same intellectual move the X-4 argument makes, replacing a boundary observed in flight with a quantity that can be computed before flying. The measurement bearing most directly on the X-4's founding hypothesis is [Rainey and Igoe 1958][research_rainey_igoe_1958], which recorded buffeting loads on the wing and on the horizontal tail of a scale model separately, and so quantifies the very coupling the tailless configuration was built to eliminate.

The programme also acquired a second purpose that the keystone does not cover, and it is a positive contribution rather than a negative result. Opening the split flap speed brakes spoiled the lift-to-drag ratio deliberately, reportedly below three to one, and the X-4 then flew a long series of approaches in that condition to generate landing data for future rocket-powered aircraft, which would arrive at the runway unpowered and steep. That problem was worked in its own right by [Matranga and Menard 1959][research_matranga_menard_1959] on a delta-wing interceptor, and the same author subsequently analysed the approach and flare characteristics of the [X-15][ref_na_x15] over its first thirty flights in [Matranga 1961][research_matranga_1961]. The thread continues through the unpowered approach experience reported by [Hoag and Schofield 1970][research_hoag_schofield_1970] and the transport-scale investigation of [Kock et al 1972][research_kock_1972], and it terminates in routine practice for every gliding re-entry vehicle since. An aircraft built to answer a question about horizontal tails therefore also supplied an early data point on how to land a vehicle that cannot go around.

## Comparison With Ground Prediction

The X-4 is the case in this series where ground prediction performed best, and the reason is that the quantity in question is a linear derivative rather than a separated flow phenomenon.

Pitch damping is computable from geometry to useful accuracy, and the tail contribution derived above requires no more than a lift-curve slope and a moment arm. The NACA had characterized the effect of tail size, tail length, and vertical location experimentally in [Lichtenstein 1952][research_tail_size_effect_1952], and the tailless configuration specifically in the interim report of [Donlan 1944][research_tailless_interim_1944] and the model work of [Laitone 1943][research_tailless_highspeed_1943]. Free-flight models supplied an independent route, reported in [Arbic 1956][research_tailless_freeflight_1956] and with the reduction method in [Gillis and Mitchell 1957][research_freeflight_longitudinal_1957]. Rocket-propelled models extended that route to structural questions, with [Lauten et al 1954][research_lauten_1954] measuring first-bending-mode damping on swept wings while looking for transonic flutter, and [Vitale Press and Shufflebarger 1954][research_vitale_1954] applying the technique to gust loads on a tailless swept model specifically. The aeroelastic side of the ground base is [Boswinkle and Smith 1958][research_boswinkle_smith_1958] on transonic flutter of a fighter wing, [Yates 1960][research_yates_1960] on the use of measured steady-flow parameters in flutter calculation, and [Brown 1959][research_brown_1959] on predicted static aeroelastic effects. Boundary-layer transition, which governs where separation begins and therefore where the degradation starts, was measured in full-scale flight by [Banner et al 1958][research_banner_1958], with the sensitivity of thick low-drag sections to leading-edge roughness established earlier by [Jacobs Abbott and Davidson 1942][research_jacobs_1942] and the scale and turbulence dependence by [Tucker and Quinn 1944][research_tucker_quinn_1944].

The ground base was broader than the tailless work alone. The NACA had by then accumulated flight measurements of flying qualities across a range of contemporary aircraft against which any new configuration could be read, including the two-part Lockheed P-80A evaluation of [Anderson and Christofferson 1947][research_anderson_christofferson_1947] and [Anderson and Cooper 1947][research_anderson_cooper_1947], the Chance Vought F4U-4 measurements of [Liddell et al 1947][research_liddell_1947], and the longitudinal and stalling characteristics of an F-47D-30 reported by [Kraft et al 1953][research_kraft_1953]. Pilot opinion had itself begun to be treated as data rather than as commentary, and [Creer et al 1959][research_creer_1959] is a study of lateral control requirements conducted on that basis. A tailless design entering this literature was being read against a well-populated baseline rather than against nothing.

The prediction was substantially correct. What the ground work could not supply was the transonic degradation, since that depends on shock position and separation, and it could not supply the pilot's assessment, since handling quality is a judgement about a coupled human and machine system rather than a derivative. A model investigation can tell you the damping ratio. It cannot tell you that a pilot will call the result unacceptable, and the estimated transonic flying qualities work of [Donlan and Kuhn 1976][research_tailless_transonic_est_1976] is an attempt, decades later, to close exactly that gap.

That distinction matters for the series argument. The [X-2][related_post_a299_bell_x2] and [X-3][related_post_a300_douglas_x3] found phenomena that ground facilities could not represent. The X-4 found a phenomenon that ground facilities predicted correctly, and flew anyway because the prediction concerned a judgement nobody was willing to make on paper.

## What the Data Changed

The X-4 answered its question in the negative and the answer held for thirty years. That is the primary consequence and it is a large one, since a negative result that is trusted saves the cost of the programmes it prevents.

The specific finding propagated as a design rule. A transonic or supersonic aircraft carries a horizontal tail, and the tail is sized for damping as well as for control and trim. The tail size and length study of [Lichtenstein 1952][research_tail_size_effect_1952] became a design tool rather than a research result. Where a tailless configuration was pursued anyway, it was pursued at low speed, and the tailless delta fighters of the 1950s, characterized in [Mitcham et al 1956][research_tailless_triangular_1956] and [White and Innis 1959][research_tailless_delta_lowspeed_1959], accepted the handling penalty in exchange for supersonic wave drag benefits and were flown by trained crews within limits.

The second consequence is the more interesting one and it took longer to arrive. If the problem is insufficient damping, and damping can be manufactured, then the objection dissolves. A pitch damper feeds pitch rate back to the elevator or elevon,

$$\delta_e = \delta_{e, \text{pilot}} - k_q \, q_r$$

which augments the damping derivative to

$$C_{mq, \text{aug}} = C_{mq} + k_q \, C_{m \delta_e} \frac{2V}{\bar{c}}$$

The gain required follows directly. Setting the augmented damping ratio to a target value,

$$\zeta_{\text{target}} = -\frac{M_q + k_q M_{\delta_e} + M_{\dot\alpha} + Z_\alpha / V}{2 \omega_{sp}}$$

and solving,

$$k_q = \frac{-2 \zeta_{\text{target}} \omega_{sp} - \left( M_q + M_{\dot\alpha} + Z_\alpha / V \right)}{M_{\delta_e}}$$

so with the X-4 values and a target of 0.7, the feedback must supply an additional damping term of

$$\Delta \left( \frac{1}{s} \right) = -2 \left( 0.7 - 0.244 \right) \times 3.00 = -2.74 \ \text{per second}$$

which is comparable in magnitude to the $M_q$ a tail would have provided. A gain chosen to hold $\zeta_{sp}$ near 0.7 across the envelope therefore restores by feedback almost exactly what the missing tail removed, which is the sense in which the augmentation is a substitute rather than a palliative. A rate limit is the more common practical constraint, since a surface that cannot slew fast enough introduces an effective delay that grows with commanded amplitude,

$$\tau_{\text{eff}} \approx \frac{A_{\text{cmd}} \, \omega}{\dot{\delta}_{\max}}$$

which is amplitude-dependent and therefore nonlinear, and which is a well-known route into pilot-induced oscillation. The actuator must also be fast enough not to introduce its own lag, requiring a bandwidth

$$\omega_{\text{act}} \gg \omega_{sp}$$

and the failure of that inequality is the mechanism by which a badly implemented damper makes an aircraft worse rather than better. [Moul and Brown 1959][research_artificial_pitch_damping_1959] investigated this directly, five years after the X-4 programme ended, and the technology matured into the [stability augmentation systems][ref_stability_augmentation] that every high-performance aircraft now carries. The bandwidth inequality above is the constraint that still governs those systems, and [Ozer 2025][research_ozer_2025] treats delay effects in longitudinal augmentation as a stability problem in its own right, which is the formal statement of why a slow actuator makes matters worse. Augmentation of a flexible airframe, where the structural modes intrude on the band the augmenter occupies, is the subject of [Bertolin et al 2021][research_bertolin_2021], and augmentation scheduled against flying qualities requirements rather than against a fixed target of [Wang et al 2024][research_wang_tvsas_2024]. The [XB-70][research_xb70_review_1965] flight programme and the automatic pitch-up control of [Hurt and Whitten 1960][research_pitchup_control_1960] belong to the same lineage, as does the control feel research of [Faber and Crane 1961][research_feel_system_1961].

Once that technology existed, the X-4's answer expired. The [McDonnell Douglas X-36][ref_mcdonnell_x36] flew in 1997 as a tailless fighter demonstrator with no vertical surface either, and the test pilot account in [Walker 1997][research_x36_test_pilot_1997] describes an aircraft that handles well because the flight control system makes it so. The [B-2][ref_b2_spirit] is a flying wing that entered service. The blended wing body work of [Carter et al 2006][research_bwb_bli_2006] and the oblique flying wing study of [Vandervelden 1989][research_oblique_flying_wing_1989] extend the same idea further.

The correct summary is therefore not that the X-4 proved tailless aircraft impossible. It is that the X-4 measured how much damping a tail supplies, established that an unaugmented tailless aircraft cannot afford to lose it in the transonic band, and thereby specified the size of the problem that stability augmentation later had to solve. A negative result that quantifies its own remedy is a better result than a positive one that does not.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Transonic aerodynamics, buffet and drag | 477 |
| Stability augmentation and flight control | 465 |
| Tailless, flying wing and blended wing body configurations | 433 |
| Handling qualities and flying qualities criteria | 398 |
| Control effectors, elevons, drag rudders and allocation | 321 |
| Lateral-directional stability and the fin | 258 |
| Stall, pitch-up, departure, wing rock and tumbling | 237 |
| Wing planform aerodynamics and the swept wing | 199 |
| Longitudinal stability, trim and the short-period mode | 196 |
| Flight test, measurement and parameter identification | 190 |
| The horizontal tail, downwash and the wing wake | 166 |
| Pilot-induced oscillation and the pilot in the loop | 165 |
| Pitch damping and the dynamic stability derivatives | 154 |
| Aeroelasticity, flutter and control reversal | 76 |
| Approach, landing, ground effect and the low lift-to-drag glide | 61 |
| Flight mechanics texts and chapters | 45 |
| Information, similarity, the atmosphere and cost | 13 |
| **Total** | **3,854** |

### The Tailless Configuration Since the X-4

The tailless configuration is now mainstream and its literature is correspondingly large, which is the strongest evidence that the X-4's finding was about a missing technology rather than a physical impossibility.

The single most useful entry point is [Hu et al 2024][research_hu_tailless_review_2024], a review of control methods for tailless aircraft, whose existence as a review is itself the evidence, since a configuration does not acquire a review literature until it has acquired a practice.

Stability and control of flying wing layouts is now an ordinary design subject, treated by [Wang et al 2020][research_wang_tang_2020], [Zhang et al 2024][research_zhang_liu_2024], [Pan and Huang 2019][research_pan_huang_2019], and [Lyu et al 2023][research_lyu_zhang_2023], the last of these designing aerodynamic shape and control law together, which is precisely the coupling the X-4 could not exploit. The blended wing body is the configuration in which the commercial case is being made, and its longitudinal static stability is the recurring difficulty, addressed by [Qi et al 2021][research_qi_bwb_2021] and set against certification requirements by [Wang et al 2022][research_wang_bwb_airworthiness_2022]. That last paper is worth dwelling on, because airworthiness requirements are where the X-4's finding would have to be argued today, and a configuration that could not meet them unaugmented must now demonstrate that its augmentation is as reliable as the aerodynamics it replaces. Fault-tolerant attitude control for exactly this class of airframe is treated by [Yu et al 2023][research_yu_tailless_2023]. Handling qualities assessments of such aircraft appear in [Humphreys-Jennings et al 2020][research_humphreys_2020] and [Campos and Marques 2021][research_campos_marques_2021], with pilot-in-the-loop evaluation in [Portapas and Cooke 2020][research_portapas_2020].

The directional problem the X-4 solved with a fin is now solved without one. The mechanism is a split surface that opens symmetrically on one wing to produce drag without net lift, generating yaw from a drag differential rather than from a side force,

$$N = \Delta D \cdot y_{\text{eff}}, \qquad C_n = \Delta C_D \frac{y_{\text{eff}}}{b}$$

with $y_{\text{eff}}$ the spanwise station of the device. Because drag rises with the square of deflection while the associated lift change is small, such a device is nonlinear and single-signed, so it must be paired across the span and biased open to allow deflection in both directions, which costs drag continuously. That standing penalty is the price a finless aircraft pays for directional control, and it is why the configuration only became attractive once the drag budget could absorb it. [Shearwood et al 2020][research_shearwood_2020] present a control allocation method for yaw on a finless aircraft, [Liu and Zhang 2022][research_liu_zhang_rudder_2022] investigate a flow-coupling rudder, and [Zhang and He 2026][research_zhang_he_2026] treat yaw stabilization and manoeuvring on a tailless configuration directly. The device is still being improved, with [Guo et al 2026][research_guo_split_rudder_2026] enhancing its effectiveness using synthetic jets, and it brings a failure mode of its own that the fin it replaces did not have, since a surface held open in separated flow can flutter in stall, which [Li et al 2022][research_li_split_rudder_2022] examine. Control by fluid injection rather than by moving surfaces at all is the further extension, demonstrated across three axes in virtual flight by [Zhang and He 2026][research_zhang_he_fluidic_2026] and applied to trim on a tailless model with sweeping jets by [Jentzsch et al 2019][research_jentzsch_2019]. The elevon itself is likewise being augmented rather than retired, and [Xin et al 2019][research_xin_blown_elevon_2019] blow a jet over one to recover the longitudinal control power a blended wing body cannot obtain from geometry. Control allocation across redundant effectors is what makes all of this possible, and it is worth stating in form. A modern tailless aircraft has more effectors than axes, so the mapping from deflections to moments,

$$\mathbf{m} = \mathbf{B} \, \boldsymbol{\delta}, \qquad \mathbf{m} \in \mathbb{R}^3, \quad \boldsymbol{\delta} \in \mathbb{R}^p, \quad p > 3$$

is underdetermined, and the allocator chooses among the solutions. The minimum-effort choice is the pseudo-inverse,

$$\boldsymbol{\delta} = \mathbf{B}^{+} \mathbf{m}_{\text{des}} = \mathbf{B}^{\top} \left( \mathbf{B} \mathbf{B}^{\top} \right)^{-1} \mathbf{m}_{\text{des}}$$

subject to position and rate limits on every surface,

$$\left| \delta_i \right| \le \delta_{i, \max}, \qquad \left| \dot{\delta}_i \right| \le \dot{\delta}_{i, \max}$$

The X-4's elevon constraint derived above is the degenerate case of this with $p = 2$ and no redundancy at all, which is why its pitch and roll authority had to be traded rather than allocated. Redundancy converts a hard tradeoff into an optimization, and that is the structural difference between the X-4 and its successors. The subject is treated by [Cong et al 2023][research_cong_hu_2023] and [Dong et al 2025][research_dong_zhou_2025], and the failure case that a redundant system must survive by [Zhou et al 2025][research_zhou_liu_2025].

Relaxed static stability, which is the deliberate acceptance of the condition the X-4 suffered accidentally, is now a design choice, treated by [Cui et al 2026][research_cui_zhang_2026] and implemented through the control architectures of [He et al 2022][research_he_hu_2022]. Unmanned combat aircraft have adopted the configuration wholesale, as [Khalid 2023][research_khalid_2023] describes.

The damping derivative itself is still being estimated and still matters, as [Khan et al 2025][research_khan_shaikh_2025] show, and the flying qualities criteria that turn a damping ratio into a pilot rating have been refined continuously, with [Efremov et al 2020][research_efremov_2020] advancing the prediction of both flying qualities and pilot-induced oscillation and [Bidinotto et al 2021][research_bidinotto_2021] surveying the pilot models on which such predictions rest. The step the X-4 programme could not take, from a criterion that judges a finished aircraft to one that bounds the configuration before it is built, is what [Wang et al 2021][research_wang_criteria_2021] attempt by deriving configuration parameter boundaries from closed-loop flying qualities requirements. Had such a method existed in 1946 the X-4 would have been an expensive confirmation rather than a discovery, which is the sense in which the aircraft's own result eventually made aircraft like it unnecessary. Structural flexibility complicates the same judgement on a modern airframe, as [Cavalcanti et al 2026][research_cavalcanti_2026] show.

The pilot-induced oscillation thread has advanced in the specific direction the crossover argument above predicts. [Nguyen et al 2021][research_nguyen_saturation_pio_2021] analyse actuator saturation as a nonlinear bifurcation, which is the rigorous form of the amplitude-dependent effective delay written down earlier, and it establishes that the transition into oscillation is a change of qualitative behaviour rather than a gradual degradation. [Xu et al 2019][research_xu_pio_2019] predict the nonlinear case using a pilot model rather than a describing function, and [Newton and Kroo 2025][research_newton_kroo_2025] attack the problem from the control law by shaping the aircraft the pilot perceives. A pilot who cannot excite the mode cannot be trapped in it. That last thread is the direct descendant of what the X-4 pilots reported, since hunting is a closed-loop phenomenon involving the pilot and not merely an open-loop damping ratio.

Configuration details that a tailless design must get right are still being worked, including leading-edge cranks in [Veismann et al 2023][research_veismann_2023] and forward-swept vortex behaviour in [Kanazaki and Setoguchi 2023][research_kanazaki_2023] and, with a chine forebody, in [Saheby et al 2026][research_saheby_2026]. The vortex system over a very low aspect ratio wing, which is the flow the X-4 lived in, is characterized by [Dong et al 2022][research_dong_low_ar_2022]. Wingtip devices, which supply a yawing moment arm the configuration otherwise lacks, are evaluated for a tailless layout by [Kania et al 2025][research_kania_2025], and made to rotate in flight by [Wang et al 2025][research_wang_rotating_wingtip_2025]. Aeroelasticity and flight dynamics, which the X-4 could treat as separate subjects, are now solved together for a flying wing by [Liu et al 2026][research_liu_flying_wing_aero_2026].

Wing rock deserves naming alongside tumbling, since it is the lateral member of the same family and it afflicts precisely this planform. A slender or highly swept wing at moderate incidence sheds an asymmetric vortex system whose reattachment lags the motion, and the lag converts roll damping into roll driving over a band of angle of attack. [Li et al 2023][research_li_wing_rock_2023] identify the mode and its mechanism on a flying wing, and [Tahir et al 2026][research_tahir_wing_rock_2026] suppress it with active flow control on a blended wing body. The X-4's reported tendency to hunt about all three axes rather than in pitch alone is consistent with a configuration sitting near the edge of this behaviour, though no source consulted makes that identification and it is offered here as a possibility rather than a finding.

Ground effect closes the set, since it is the one flight condition every aircraft must enter and the one in which a tailless configuration has no independent surface to trim the moment change. [Xun et al 2026][research_xun_ground_effect_2026] extend the aerodynamics across subsonic, transonic, and supersonic conditions, which is a wider envelope than the problem was ever posed in when the X-4 flew its approach series. The tumbling mode, which is a tailless failure mode with no conventional analogue, deserves its own statement. A conventional design driven past stall pitches nose-down because the tail restores it. A tailless aircraft has no such restoring surface once the wing itself has stalled, and if the inertia in pitch is low enough relative to the available aerodynamic moment the aircraft can enter a continuous rotation about the pitch axis. The condition depends on the balance between the residual aerodynamic moment and the rotational inertia,

$$\ddot{\theta} = \frac{q S \bar{c} \, C_m(\alpha)}{I_y}$$

with $C_m(\alpha)$ evaluated well beyond the linear range, where it need not change sign at all. Tumbling is therefore possible when

$$C_m(\alpha) > 0 \quad \text{for all } \alpha \text{ in the post-stall range}$$

which is a condition on the whole post-stall moment curve rather than on any single derivative. Geometry, static stability, and mass distribution jointly determine it, as [Fremaux et al 1993][research_tumbling_characteristics_1993] characterizes, and it is why tailless configurations receive spin and departure attention out of proportion to their numbers, as [Patton et al 1979][research_spin_research_summary_1979] reflects.

### Transonic aerodynamics, buffet and drag

**The flow regime the X-4 was built to enter.** Transonic flow over wings and aerofoils and its computation, drag rise and the area rule, transonic flutter and buffet. **173 of these titles name buffet**, and from 2016 onward a run of them treats buffet onset as a global instability of the flow, which is the reformulation the flight test record above describes.

**477 records.** \[[A Comparison of Different 2022][research_a_comparison_2022]\] \[[A New Steady Approach 2006][research_a_new_2006]\] \[[Abramova et al 2016][research_abramova_petrov_2016]\] \[[Abramova et al 2020][research_abramova_petrov_2020]\] \[[Aeroelasticity Problems in Compressible 2010][research_aeroelasticity_problems_2010]\] \[[Agarwal and Deese 1983][research_agarwal_deese_1983]\] \[[Agarwal and Deese 1984][research_agarwal_deese_1984]\] \[[Agrawal et al 1991][research_agrawal_kinard_1991]\] \[[Agrell and Elmeland 1984][research_agrell_elmeland_1984]\] \[[Agrell and Elmeland 1985][research_agrell_elmeland_1985]\] \[[Aiken and See 1951][research_aiken_see_1951]\] \[[Andrew and Stenton 1967][research_andrew_stenton_1967]\] \[[Arif et al 2023][research_arif_singh_2023]\] \[[Armenta and Takahashi 2021][research_armenta_takahashi_2021]\] \[[Asada and Kawai 2024][research_asada_kawai_2024]\] \[[Asai 2022][research_asai_2022]\] \[[Ashley 1980][research_ashley_1980]\] \[[Aul'chenko and Zamuraev 2012][research_aulchenko_zamuraev_2012]\] \[[Ayers and Hallissy 1981][research_ayers_hallissy_1981]\] \[[Babinsky and Ogawa 2006][research_babinsky_ogawa_2006]\] \[[Baker and Johnson 1955][research_baker_johnson_1955]\] \[[Balleur et al 2002][research_balleur_girodrouxlavigne_2002]\] \[[Barakos and Drikakis 1999][research_barakos_drikakis_1999]\] \[[Barbut et al 2010][research_barbut_braza_2010]\] \[[Barinov et al 2016][research_barinov_pavlenko_2016]\] \[[Barnard 1969][research_barnard_1969]\] \[[Barnes and Visbal 2020][research_barnes_visbal_2020]\] \[[Barnwell 1974][research_barnwell_1974]\] \[[Batina 1986][research_batina_1986]\] \[[Batina 1986][research_batina_1986_b]\] \[[Batina 1986][research_batina_1986_c]\] \[[Batina 1988][research_batina_1988]\] \[[Batina 1989][research_batina_1989]\] \[[Batina et al 1989][research_batina_seidel_1989]\] \[[Beeler et al 1956][research_beeler_1956]\] \[[Begnini et al 2018][research_begnini_bones_2018]\] \[[Belesiotis-Kataras and Timme 2020][research_belesiotiskataras_timme_2020]\] \[[Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]\] \[[Belisle et al 2010][research_belisle_neale_2010]\] \[[Bellman 1959][research_bellman_1959]\] \[[Bendiksen 2008][research_bendiksen_2008]\] \[[Bendiksen 2009][research_bendiksen_2009]\] \[[Benepe et al 1974][research_benepe_cunningham_1974]\] \[[Benepe et al 1978][research_benepe_cunningham_1978]\] \[[Bertelrud and Graves 1994][research_bertelrud_graves_1994]\] \[[Bielat and Pierpont 1960][research_bielat_pierpont_1960]\] \[[Black][research_black]\] \[[Bobbitt 1980][research_bobbitt_1980]\] \[[Boelens 2017][research_boelens_2017]\] \[[Bonnifet et al 2017][research_bonnifet_gerolymos_2017]\] \[[Boppe 1977][research_boppe_1977]\] \[[Boppe 1978][research_boppe_1978]\] \[[Boswinkle and Smith 1958][research_boswinkle_smith_1958]\] \[[Bragin 2018][research_bragin_2018]\] \[[Browne et al 2024][research_browne_maldonado_2024]\] \[[Browne et al 2025][research_browne_maldonado_2025]\] \[[Brunet and Deck 2008][research_brunet_deck_2008]\] \[[Bui 2018][research_bui_2018]\] \[[Burdges 1973][research_burdges_1973]\] \[[Byreddy et al 2003][research_byreddy_grandhi_2003]\] \[[Candon et al 2019][research_candon_levinski_2019]\] \[[Carlsen 1995][research_carlsen_1995]\] \[[Carrese et al 2016][research_carrese_marzocca_2016]\] \[[Caughey 1976][research_caughey_1976]\] \[[Caughey 1982][research_caughey_1982]\] \[[Caughey and Jameson 1977][research_caughey_jameson_1977]\] \[[Cenko and Madson 1993][research_cenko_madson_1993]\] \[[Chan et al 1976][research_chan_chen_1976]\] \[[Chaparro et al 2016][research_chaparro_fujiwara_2016]\] \[[Chen 1982][research_chen_1982]\] \[[Chen and Bui 1990][research_chen_bui_1990]\] \[[Cheng 1982][research_cheng_1982]\] \[[Cheng 2009][research_cheng_2009]\] \[[Cheng et al 1980][research_cheng_meng_1980]\] \[[Christison Gray and Martins 2026][research_christisongray_martins_2026]\] \[[Chung 2007][research_chung_2007]\] \[[Chung 2017][research_chung_2017]\] \[[Chung et al 2002][research_chung_lee_2002]\] \[[Chung et al 2003][research_chung_lee_2003]\] \[[Chyczewski 2017][research_chyczewski_2017]\] \[[Cleary and Gray 1947][research_cleary_gray_1947]\] \[[Cole et al 2003][research_cole_noll_2003]\] \[[Cosenza and Kummeth 1974][research_cosenza_kummeth_1974]\] \[[Crisalli et al 1979][research_crisalli_stahara_1979]\] \[[Crouch et al 2008][research_crouch_garbaruk_2008]\] \[[Crouch et al 2018][research_crouch_garbaruk_2018]\] \[[Crouch et al 2019][research_crouch_2019]\] \[[Currao and Yeh 2026][research_currao_yeh_2026]\] \[[D'Aguanno et al 2021][research_daguanno_schrijer_2021]\] \[[D'Aguanno et al 2022][research_daguanno_campspons_2022]\] \[[D'Aguanno et al 2022][research_daguanno_schrijer_2022]\] \[[D'Ewart et al 1958][research_dewart_jr_1958]\] \[[Dai and Zhang 2023][research_dai_zhang_2023]\] \[[Damstrom and Mayes 1970][research_damstrom_mayes_1970]\] \[[Damstrom and Mayes 1971][research_damstrom_mayes_1971]\] \[[Dandois 2016][research_dandois_2016]\] \[[Danforth and O'Bryan 1951][research_danforth_obryan_1951]\] \[[Dang and Yang 2010][research_dang_yang_2010]\] \[[Dang et al 2019][research_dang_zhao_2019]\] \[[Davies 2020][research_davies_2020]\] \[[Davies 2025][research_davies_2025]\] \[[Deck 2004][research_deck_2004]\] \[[Deck 2005][research_deck_2005]\] \[[Deng et al 2023][research_deng_zhang_2023]\] \[[Desai et al 1977][research_desai_viswanathan_1977]\] \[[Di Fabbio et al 2022][research_difabbio_tangermann_2022]\] \[[Di Pasquale 2024][research_dipasquale_2024]\] \[[Di Pasquale and Prince 2023][research_dipasquale_prince_2023]\] \[[Dias et al 2023][research_dias_budisic_2023]\] \[[Dodbele and Plotkin 1985][research_dodbele_plotkin_1985]\] \[[Donegan 1984][research_donegan_1984]\] \[[Drake et al 1948][research_drake_mclaughlin_1948]\] \[[Duncan 1934][research_duncan_1934]\] \[[Dvorak and Choi 1982][research_dvorak_choi_1982]\] \[[Edwards 2008][research_edwards_2008]\] \[[Edwards et al 2009][research_edwards_spain_2009]\] \[[Eldridge-Allegra et al 2024][research_eldridgeallegra_roseman_2024]\] \[[Epstein et al 1989][research_epstein_luntz_1989]\] \[[Erickson 1987][research_erickson_1987]\] \[[Erickson et al 1989][research_erickson_schreiner_1989]\] \[[Ericsson and Reding 1977][research_ericsson_reding_1977]\] \[[Extension of FLO Codes 1982][research_extension_of_1982]\] \[[Farhangnia et al 1996][research_farhangnia_guruswamy_1996]\] \[[Firsov et al 2017][research_firsov_isaenkov_2017]\] \[[Florio et al 2019][research_florio_mckibbin_2019]\] \[[Fluid Dynamics Research on 1998][research_fluid_dynamics_1998]\] \[[Foster 1959][research_foster_1959]\] \[[Fournis 2022][research_fournis_2022]\] \[[Fox et al 1991][research_fox_donegan_1991]\] \[[Friend and Sakamoto 1978][research_friend_sakamoto_1978]\] \[[Friend and Sefic 1972][research_friend_sefic_1972]\] \[[Fujii and Obayashi 1986][research_fujii_obayashi_1986]\] \[[Fujino and Suzuki 2024][research_fujino_suzuki_2024]\] \[[Fukumoto et al 2023][research_fukumoto_kouchi_2023]\] \[[Fukushima and Kawai 2019][research_fukushima_kawai_2019]\] \[[Fung 1982][research_fung_1982]\] \[[G. The Experimental Aerodynamics 1957][research_g_the_1957]\] \[[Gallman et al 1988][research_gallman_batina_1988]\] \[[Gao et al 2018][research_gao_zhang_2018]\] \[[Gao et al 2019][research_gao_zhang_2019]\] \[[Gao et al 2025][research_gao_tyrrell_2025]\] \[[Garbaruk et al 2021][research_garbaruk_strelets_2021]\] \[[Geoghegan et al 2020][research_geoghegan_giannelis_2020]\] \[[Gibbings 1966][research_gibbings_1966]\] \[[Gillan 1993][research_gillan_1993]\] \[[Glauert 1928][research_glauert_1928]\] \[[Gloss and Washburn 1977][research_gloss_washburn_1977]\] \[[Goc et al 2023][research_goc_agrawal_2023]\] \[[Godavarthi et al 2026][research_godavarthi_seo_2026]\] \[[Gong et al 2024][research_gong_gao_2024]\] \[[Goodman 1949][research_goodman_1949]\] \[[Goorjian et al 1985][research_goorjian_guruswamy_1985]\] \[[Gordnier and Melville 2000][research_gordnier_melville_2000]\] \[[Goushcha and Sekula 2025][research_goushcha_sekula_2025]\] \[[Green and Mineck 1991][research_green_mineck_1991]\] \[[Grossman and Volpe 1977][research_grossman_volpe_1977]\] \[[Guruswamy and Goorjian 1983][research_guruswamy_goorjian_1983]\] \[[Guruswamy and Goorjian 1985][research_guruswamy_goorjian_1985]\] \[[Guruswamy and Tu 1994][research_guruswamy_tu_1994]\] \[[Guruswamy et al 1986][research_guruswamy_goorjian_1986]\] \[[Guy and Hadaway 1955][research_guy_hadaway_1955]\] \[[Habel and Steinberg 1953][research_habel_steinberg_1953]\] \[[Hagerman and Hofstetter 1969][research_hagerman_hofstetter_1969]\] \[[Hasan and Alam 2013][research_hasan_alam_2013]\] \[[Hayabe and Kwak 2025][research_hayabe_kwak_2025]\] \[[Heeg and Chwalowski 2017][research_heeg_chwalowski_2017]\] \[[Heiss et al 1992][research_heiss_eberle_1992]\] \[[Heltsley and Cline 1979][research_heltsley_cline_1979]\] \[[Heltsley et al 1981][research_heltsley_crosswy_1981]\] \[[Henne and Hicks 1978][research_henne_hicks_1978]\] \[[Herr et al 2023][research_herr_spinner_2023]\] \[[Hieser et al 1956][research_hieser_kudlacik_1956]\] \[[Hillenherms et al 2003][research_hillenherms_schroder_2003]\] \[[Hitzel 2017][research_hitzel_2017]\] \[[Holdaway 1954][research_holdaway_1954]\] \[[Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]\] \[[Holst 1988][research_holst_1988]\] \[[Holst and Thomas 1982][research_holst_thomas_1982]\] \[[Hopkins et al 1998][research_hopkins_henderson_1998]\] \[[Hoshi et al 2020][research_hoshi_kuya_2020]\] \[[Houtman et al 2023][research_houtman_timme_2023]\] \[[Houtman et al 2023][research_houtman_vevek_2023]\] \[[Howell and Korst 1971][research_howell_korst_1971]\] \[[Hu 1992][research_hu_1992]\] \[[Hu 1995][research_hu_1995]\] \[[Hwang and Pi 1975][research_hwang_pi_1975]\] \[[Hwang and Pi 1975][research_hwang_pi_1975_b]\] \[[Ide et al 2019][research_ide_ishida_2019]\] \[[Illi et al 2013][research_illi_fingskes_2013]\] \[[Imai 1964][research_imai_1964]\] \[[Immordino et al 2025][research_immordino_vaiuso_2025]\] \[[Iovnovich et al 2017][research_iovnovich_raveh_2017]\] \[[Ishida et al 2017][research_ishida_hashimoto_2017]\] \[[Iwatani et al 2022][research_iwatani_asada_2022]\] \[[Izumi et al 2015][research_izumi_ogino_2015]\] \[[Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]\] \[[Jameson][research_jameson]\] \[[Jameson 1977][research_jameson_1977]\] \[[Jameson and Caughey 1977][research_jameson_caughey_1977]\] \[[Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]\] \[[Janardhan et al 2003][research_janardhan_grandhi_2003_b]\] \[[Janardhan et al 2005][research_janardhan_grandhi_2005]\] \[[Jiang et al 2018][research_jiang_tian_2018]\] \[[Jiang et al 2019][research_jiang_tian_2019]\] \[[Jinli and Zhichun 2013][research_jinli_zhichun_2013]\] \[[Lamar et al 2001][research_johnelamar_cliffordjobara_2001]\] \[[Johnson 1982][research_johnson_1982]\] \[[Johnston 1992][research_johnston_1992]\] \[[Johnston 1998][research_johnston_1998]\] \[[Jones 1947][research_jones_1947]\] \[[Jones and Farmer 1959][research_jones_farmer_1959]\] \[[Jou and Mueller 1985][research_jou_mueller_1985]\] \[[Jumper 1983][research_jumper_1983]\] \[[Kanchi et al 2026][research_kanchi_he_2026]\] \[[Kandil 1992][research_kandil_1992]\] \[[Kandil 1993][research_kandil_1993]\] \[[Kandil et al 1993][research_kandil_kandil_1993_b]\] \[[Katzenmeier et al 2021][research_katzenmeier_vidy_2021]\] \[[Kaups et al 1989][research_kaups_mehta_1989]\] \[[Keenan and Kuhlman 1991][research_keenan_kuhlman_1991]\] \[[Keener 1984][research_keener_1984]\] \[[Keener 1985][research_keener_1985]\] \[[Kehlet 1954][research_kehlet_1954]\] \[[Kennelly et al 1990][research_kennelly_kroo_1990]\] \[[Kholodar et al 2004][research_kholodar_dowell_2004]\] \[[Kikuchi et al 2024][research_kikuchi_kouchi_2024]\] \[[Kim et al 2005][research_kim_rockwell_2005]\] \[[Kirkham et al 1974][research_kirkham_jackson_1974]\] \[[Klausmeyer 2004][research_klausmeyer_2004]\] \[[Knapp et al 1953][research_knapp_jordan_1953]\] \[[Koike et al 2016][research_koike_ueno_2016]\] \[[Kojima and Hashimoto 2023][research_kojima_hashimoto_2023]\] \[[Kojima et al 2019][research_kojima_kameda_2019]\] \[[Kolonay and Yang 1998][research_kolonay_yang_1998]\] \[[Korthäuer et al 2023][research_korthauer_accorinti_2023]\] \[[Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]\] \[[Kumada and Sawada 2016][research_kumada_sawada_2016]\] \[[Kusunose et al 1987][research_kusunose_marcum_1987]\] \[[Kutney and Piszkin 1963][research_kutney_piszkin_1963]\] \[[Kutney and Piszkin 1964][research_kutney_piszkin_1964]\] \[[Kuz'min 2010][research_kuzmin_2010]\] \[[Kuz'min and Shilkin 2009][research_kuzmin_shilkin_2009]\] \[[Lacey 1979][research_lacey_1979]\] \[[Lagemann 2024][research_lagemann_2024]\] \[[Lamar 2001][research_lamar_2001]\] \[[Lamar 2003][research_lamar_2003]\] \[[Lan et al 1995][research_lan_hsu_1995]\] \[[Lauten et al 1954][research_lauten_1954]\] \[[Lee 1985][research_lee_1985]\] \[[Lee 1990][research_lee_1990]\] \[[Lei et al 2025][research_lei_zhang_2025]\] \[[Lemley and Mullans 1974][research_lemley_mullans_1974]\] \[[Lijewski 1987][research_lijewski_1987]\] \[[Lindsey 1946][research_lindsey_1946]\] \[[Liu 2022][research_liu_2022]\] \[[Liu et al 2016][research_liu_wang_2016]\] \[[Lock and Rogers 1962][research_lock_rogers_1962]\] \[[Lokos et al 2005][research_lokos_lizotte_2005]\] \[[Lomax et al 1973][research_lomax_bailey_1973]\] \[[Lombardi et al 1997][research_lombardi_salvetti_1997]\] \[[Luckring 2003][research_luckring_2003]\] \[[Luo and Wang 1998][research_luo_wang_1998]\] \[[Syed Haseeb 2026][research_m_2026]\] \[[Mace and Cosner 1983][research_mace_cosner_1983]\] \[[Mack 1979][research_mack_1979]\] \[[Malmuth et al 1983][research_malmuth_wu_1983]\] \[[Mann and Mercer 1985][research_mann_mercer_1985]\] \[[Mansour 1984][research_mansour_1984]\] \[[Marion and Sharma 2025][research_marion_sharma_2025]\] \[[Masini et al 2019][research_masini_timme_2019]\] \[[Masini et al 2020][research_masini_timme_2020]\] \[[Mason 1953][research_mason_1953]\] \[[Mason 1982][research_mason_1982]\] \[[Matheny and Gatlin 1978][research_matheny_gatlin_1978]\] \[[Mavriplis and Levy 2002][research_mavriplis_levy_2002]\] \[[Mayer et al 2019][research_mayer_lutz_2019]\] \[[Mayes et al 1970][research_mayes_lores_1970]\] \[[Mayya et al 2022][research_mayya_karnick_2022]\] \[[Mazumder 2024][research_mazumder_2024]\] \[[Medved 1990][research_medved_1990]\] \[[Meijer and Cunningham 1992][research_meijer_cunningham_1992]\] \[[Menzies 1996][research_menzies_1996]\] \[[Mertens et al 1986][research_mertens_klevenhusen_1986]\] \[[Milholen and Chokani 1994][research_milholen_chokani_1994]\] \[[Miyaji and Takegawa 2022][research_miyaji_2022]\] \[[Molton et al 2013][research_molton_dandois_2013]\] \[[Monaghan 1978][research_monaghan_1978]\] \[[Monaghan and Friend 1973][research_monaghan_friend_1973]\] \[[Moorthamers et al 2021][research_moorthamers_wiberg_2021]\] \[[Mori et al 2024][research_mori_yakeno_2024]\] \[[Murray et al 2020][research_murray_giannellis_2020]\] \[[Baker 1953][research_x4_buffet_1953]\] \[[Equations, tables, and charts 1953][research_naca_1135]\] \[[Nahom Jidovetski et al 2025][research_nahomjidovetski_raveh_2025]\] \[[Nash et al 2025][research_nash_timme_2025]\] \[[Nguyen and Xiong 2021][research_nguyen_xiong_2021]\] \[[Nguyen and Xiong 2022][research_nguyen_xiong_2022]\] \[[Nguyen and Xiong 2023][research_nguyen_xiong_2023]\] \[[Nguyen et al 2019][research_nguyen_fugate_2019]\] \[[Nguyen and Xiong][research_nhannguyen_juntaoxiong_b]\] \[[Nielsen et al 1953][research_nielsen_1953]\] \[[Nixon 1974][research_nixon_1974]\] \[[Nixon 2020][research_nixon_2020]\] \[[Nugent 1959][research_nugent_1959]\] \[[Nävert and Sedin 1992][research_navert_sedin_1992]\] \[[O'Kelly 1954][research_okelly_1954]\] \[[O'Kelly 1955][research_okelly_1955]\] \[[Oertel and Stank 1999][research_oertel_stank_1999]\] \[[Ohmichi et al 2017][research_ohmichi_ishida_2017]\] \[[Ohmichi et al 2018][research_ohmichi_ishida_2018]\] \[[Olsen 1966][research_olsen_1966]\] \[[Painter and Caw 1978][research_painter_caw_1978]\] \[[Patel and Lefas 2026][research_patel_lefas_2026]\] \[[Perkins et al 1977][research_perkins_jr_1977]\] \[[Petrocchi and Barakos 2023][research_petrocchi_barakos_2023]\] \[[Physics-assisted reduced-order modeling for 2023][research_physics_assisted_reduced_order_2023]\] \[[Plante and Laurendeau 2019][research_plante_laurendeau_2019]\] \[[Plante et al 2017][research_plante_dandois_2017]\] \[[Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026]\] \[[Poplingher and Raveh 2018][research_poplingher_raveh_2018]\] \[[Poplingher and Raveh 2022][research_poplingher_raveh_2022]\] \[[Poplingher et al 2022][research_poplingher_mallik_2022]\] \[[Pototzky and Moses 2005][research_pototzky_moses_2005]\] \[[Pounds and Walker 1980][research_pounds_walker_1980]\] \[[Prediction of transonic flutter 1981][research_prediction_of_1981]\] \[[Puentes and Takahashi 2024][research_puentes_takahashi_2024]\] \[[Qi et al 2026][research_qi_gao_2026]\] \[[Rahman et al 2025][research_rahman_vowotor_2025]\] \[[Raj 1983][research_raj_1983]\] \[[Raj 1984][research_raj_1984]\] \[[Rajanna et al 2024][research_rajanna_jaiswal_2024]\] \[[Rajanna et al 2026][research_rajanna_lua_2026]\] \[[Ramm 1990][research_ramm_1990_b]\] \[[Rathert et al 1951][research_rathert_1951]\] \[[Raveh 2011][research_raveh_2011]\] \[[Ray et al 1972][research_ray_mckinney_1972]\] \[[Ray et al 1973][research_ray_mckinney_1973]\] \[[Ren et al 2022][research_ren_gao_2022]\] \[[Riebe and MacLeod 1950][research_riebe_macleod_1950]\] \[[Rivera and Florance 2000][research_rivera_florance_2000]\] \[[Rizzetta 1977][research_rizzetta_1977]\] \[[Rizzetta 1977][research_rizzetta_1977_b]\] \[[Rizzi 1984][research_rizzi_1984]\] \[[Rizzi 1985][research_rizzi_1985]\] \[[Rizzi 1995][research_rizzi_1995]\] \[[Robinson et al 2020][research_robinson_yuan_2020]\] \[[Rodemich and Andrew 1965][research_rodemich_andrew_1965]\] \[[Rogers and Walter K. 1953][research_rogers_walterk_1953]\] \[[Rogers and Walter K. 1958][research_rogers_walterk_1958]\] \[[Rokoni and Hasan 2013][research_rokoni_hasan_2013]\] \[[Roohani and Skews 2009][research_roohani_skews_2009]\] \[[Roos 1980][research_roos_1980]\] \[[Roos 1985][research_roos_1985]\] \[[Rose and Seginer 1978][research_rose_seginer_1978]\] \[[Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]\] \[[Ruhlin and Murphy 1981][research_ruhlin_murphy_1981]\] \[[Sanghi et al 2024][research_sanghi_cesnik_2024]\] \[[Schauerte and Schreyer 2023][research_schauerte_schreyer_2023]\] \[[Schauerte and Schreyer 2025][research_schauerte_schreyer_2025]\] \[[Schiavetta et al 2006][research_schiavetta_boelens_2006]\] \[[Schmitt et al 1983][research_schmitt_destarac_1983]\] \[[Seider and Haenel 1991][research_seider_haenel_1991]\] \[[Semaan et al 2013][research_semaan_scholz_2013]\] \[[Shankar and Goebel 1983][research_shankar_goebel_1983]\] \[[Shankar and Goebel 1985][research_shankar_goebel_1985]\] \[[Shankar and Malmuth 1980][research_shankar_malmuth_1980]\] \[[Shankar and Malmuth 1982][research_shankar_malmuth_1982]\] \[[Shankar and Malmuth 1983][research_shankar_malmuth_1983]\] \[[Shankar et al 1979][research_shankar_malmuth_1979]\] \[[Sheta 2003][research_sheta_2003]\] \[[Shiqi et al 2018][research_shiqi_tian_2018]\] \[[Sinclair 1988][research_sinclair_1988]\] \[[Singh and Venkatraman 2023][research_singh_venkatraman_2023]\] \[[Singh and Venkatraman 2026][research_singh_venkatraman_2026]\] \[[Singh et al 2022][research_singh_karnick_2022]\] \[[Skujins and Cesnik 2011][research_skujins_cesnik_2011]\] \[[Smetana and Knepper 1973][research_smetana_knepper_1973]\] \[[Soemarwoto et al 2000][research_soemarwoto_labrujere_2000]\] \[[Song et al 2025][research_song_wong_2025]\] \[[Soudakov et al 2017][research_soudakov_petrov_2017]\] \[[Spaid 1984][research_spaid_1984]\] \[[Spearman 1983][research_spearman_1983]\] \[[Spearman and Driver 1959][research_spearman_driver_1959]\] \[[Spearman et al 1955][research_spearman_driver_1955]\] \[[Srinivasan et al 1986][research_srinivasan_mccroskey_1986]\] \[[Stancil 1979][research_stancil_1979]\] \[[Stanewsky and Little 1971][research_stanewsky_little_1971]\] \[[Stanford and Jacobson 2023][research_stanford_jacobson_2023]\] \[[Stanford and Jacobson 2024][research_stanford_jacobson_2024]\] \[[Stanford et al 2020][research_stanford_jacobson_2020]\] \[[Stargill 1983][research_stargill_1983]\] \[[Stegmüller et al 2026][research_stegmuller_haybock_2026]\] \[[Steimle et al 2008][research_steimle_schroder_2008]\] \[[Steimle et al 2010][research_steimle_schroder_2010]\] \[[Stickan et al 2014][research_stickan_dillinger_2014]\] \[[Streett 1981][research_streett_1981]\] \[[Streett 1982][research_streett_1982]\] \[[Strutz 1972][research_strutz_1972]\] \[[Studwell and Wu 1973][research_studwell_wu_1973]\] \[[Su and Chow 1993][research_su_chow_1993]\] \[[Su and Chow 1995][research_su_chow_1995]\] \[[Sugioka et al 2015][research_sugioka_numata_2015]\] \[[Sugioka et al 2018][research_sugioka_koike_2018]\] \[[Sugioka et al 2021][research_sugioka_nakakita_2021]\] \[[Sundaram and Wu 1983][research_sundaram_wu_1983]\] \[[Szwabowski and Baker 2023][research_szwabowski_baker_2023]\] \[[Tamaki and Kawai 2023][research_tamaki_kawai_2023]\] \[[Taylor et al 1997][research_taylor_peake_1997]\] \[[Thomas and Dowell 2015][research_thomas_dowell_2015]\] \[[Thomas and Dowell 2020][research_thomas_dowell_2020]\] \[[Thomas and Holst 1983][research_thomas_holst_1983]\] \[[Thomas et al 2001][research_thomas_dowell_2001]\] \[[Thompson et al 1950][research_thompson_bray_1950]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]\] \[[Timme 2020][research_timme_2020]\] \[[Timme and Thormann 2016][research_timme_thormann_2016]\] \[[Tomek and Boyden 2000][research_tomek_boyden_2000]\] \[[Tourrette 1996][research_tourrette_1996]\] \[[Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]\] \[[Transonic Airfoil Theory 1986][research_transonic_airfoil_1986]\] \[[Transonic and supersonic flight 1992][research_transonic_and_1992]\] \[[Transonic Computational Experience for 1982][research_transonic_computational_1982]\] \[[Transonic flight test of 1994][research_transonic_flight_1994]\] \[[Transonic Navier-Stokes flow computations 1972][research_transonic_navier_stokes_1972]\] \[[Ueno et al 2004][research_ueno_sarae_2004]\] \[[Vatsa 1987][research_vatsa_1987]\] \[[Vatsa and Wedan 1988][research_vatsa_wedan_1988]\] \[[Velkova 2017][research_velkova_2017]\] \[[Volpe and Grossman 1978][research_volpe_grossman_1978]\] \[[Volpe and Jameson 1990][research_volpe_jameson_1990]\] \[[Völkl and Breitsamter 2026][research_volkl_breitsamter_2026]\] \[[Völkl et al 2026][research_volkl_weiner_2026]\] \[[Waggoner 1980][research_waggoner_1980]\] \[[Waggoner 1982][research_waggoner_1982]\] \[[Waldmann et al 2023][research_waldmann_ehrle_2023]\] \[[Walker and Ballantyne 1950][research_walker_ballantyne_1950]\] \[[Walkley 1986][research_walkley_1986]\] \[[Walkley and Smith 1987][research_walkley_smith_1987]\] \[[Wang and Caughey 1992][research_wang_caughey_1992]\] \[[Wang et al 1994][research_wang_herbert_1994]\] \[[Ward 1968][research_ward_1968]\] \[[Wei et al 2024][research_wei_zheng_2024]\] \[[Werner et al 2024][research_werner_henne_2024]\] \[[Wing Buffet Control by 2021][research_wing_buffet_2021]\] \[[Woods and Wood 1998][research_woods_wood_1998]\] \[[Woolard 1980][research_woolard_1980]\] \[[Wright and Loving 1953][research_wright_loving_1953]\] \[[Xiao et al 2004][research_xiao_tsai_2004]\] \[[Xiong and Liu 2013][research_xiong_liu_2013]\] \[[Xiong and Nguyen 2024][research_xiong_nguyen_2024]\] \[[Xu and Dowell 2026][research_xu_dowell_2026]\] \[[Xun et al 2026][research_xun_ground_effect_2026]\] \[[Yamasaki and Lele 2024][research_yamasaki_lele_2024]\] \[[Yan et al 2026][research_yan_dai_2026]\] \[[Yang et al 1980][research_yang_guruswamy_1980]\] \[[Yates 1960][research_yates_1960]\] \[[Young et al 1992][research_young_hergert_1992]\] \[[Yu 1981][research_yu_1981]\] \[[Yuan et al 2024][research_yuan_kou_2024]\] \[[Yüksel et al 2023][research_yuksel_kandemir_2023]\] \[[Zahn and Breitsamter 2022][research_zahn_breitsamter_2022]\] \[[Zahn et al 2025][research_zahn_zieher_2025]\] \[[Zauner and Sandham 2020][research_zauner_sandham_2020]\] \[[Zauner et al 2023][research_zauner_moise_2023]\] \[[Zhang 1988][research_zhang_1988]\] \[[Zhang and Qu 2015][research_zhang_qu_2015]\] \[[Zhang et al 2026][research_zhang_deng_2026]\] \[[Zhao 1988][research_zhao_1988]\] \[[Zhao et al 2020][research_zhao_dai_2020]\] \[[Zhao et al 2024][research_zhao_zhang_2024]\] \[[Zheng et al 2012][research_zheng_feng_2012]\] \[[Zhou et al 2017][research_zhou_chen_2017]\] \[[Zhu et al 2025][research_zhu_yang_2025]\] \[[Zierep 1988][research_zierep_1988]\] \[[Zierep 1993][research_zierep_1993]\] \[[Zimmerman et al 1989][research_zimmerman_ferman_1989]\]

### Stability augmentation and flight control

**The technology that retired the X-4's answer.** Pitch and yaw dampers, stability and command augmentation, fly-by-wire, envelope protection and reconfigurable control. **From the late 1990s the tailless fighter and the flying wing become the test cases of choice for reconfigurable and fault-tolerant control**, from the X-36 flight tests to the small unmanned flying wings of the 2020s.

**465 records.** \[[Ackerman et al 2016][research_ackerman_xargay_2016]\] \[[Adams et al 1970][research_adams_schy_1970]\] \[[Ahn et al 2017][research_ahn_kim_2017]\] \[[Aircraft Flight Control 2014][research_aircraft_flight_2014]\] \[[Aircraft Stability and Control 2003][research_aircraft_stability_2003]\] \[[Aircraft Stability and Control 2014][research_aircraft_stability_2014]\] \[[Aircraft Stability and Control 2024][research_aircraft_stability_2024]\] \[[Alwi and Edwards 2007][research_alwi_edwards_2007]\] \[[An investigation of separate 1974][research_an_investigation_1974]\] \[[Analytical synthesis of the 2024][research_analytical_synthesis_2024]\] \[[Anderson et al 1972][research_anderson_berger_1972]\] \[[Anderson et al 1973][research_anderson_berger_1973]\] \[[Ansell et al 2010][research_ansell_bragg_2010]\] \[[Ansell et al 2014][research_ansell_kerho_2014]\] \[[Antonakis and Biannic 2024][research_antonakis_biannic_2024]\] \[[Application of dynamic flight][research_application_of]\] \[[Araujo and Singh 1998][research_araujo_singh_1998]\] \[[Arnold 1968][research_arnold_1968]\] \[[Asadi et al 2013][research_asadi_sabzehparvar_2013]\] \[[Ashkenas and Klyde 1989][research_ashkenas_klyde_1989]\] \[[Aslam et al 2025][research_aslam_islam_2025]\] \[[Atmaca and Van Kampen 2025][research_atmaca_vankampen_2025]\] \[[Atzhorn and Stengel 1981][research_atzhorn_stengel_1981]\] \[[Atzhorn and Stengel 1984][research_atzhorn_stengel_1984]\] \[[Bahri 2018][research_bahri_2018]\] \[[Baker and Farrell 1991][research_baker_farrell_1991]\] \[[Ballouz and Chang][research_ballouz_chang]\] \[[Barbosa et al 2019][research_barbosa_bertolin_2019]\] \[[Barker and Balas 1999][research_barker_balas_1999]\] \[[Barnwell et al 2003][research_barnwell_heinzen_2003]\] \[[Bass et al 1966][research_bass_stoner_1966]\] \[[Bateman et al 2004][research_bateman_argrow_2004]\] \[[Bateman et al 2008][research_bateman_noura_2008]\] \[[Beaufrere 1988][research_beaufrere_1988]\] \[[Beh et al 2018][research_beh_hofinger_2018]\] \[[Benchaita and Ladaci 2021][research_benchaita_ladaci_2021]\] \[[Bengtson et al 1975][research_bengtson_dickovich_1975]\] \[[Berg 1991][research_berg_1991]\] \[[Bertolin et al 2021][research_bertolin_2021]\] \[[Bertoni et al 2010][research_bertoni_bertozzi_2010]\] \[[Bian et al 2019][research_bian_nener_2019]\] \[[Binwen Lu et al 2016][research_binwenlu_jianjunma_2016]\] \[[Blight et al 1986][research_blight_gangsaas_1986]\] \[[Blight et al 2018][research_blight_lanedailey_2018]\] \[[Bodson 2000][research_bodson_2000]\] \[[Bodur and Ucun 2023][research_bodur_ucun_2023]\] \[[Bogdan et al 2010][research_bogdan_radu_2010]\] \[[Bolton and Collins 1974][research_bolton_collins_1974]\] \[[Bosch and Kuehl 1976][research_bosch_kuehl_1976]\] \[[Boskovic and Mehra 1999][research_boskovic_mehra_1999]\] \[[Boskovic and Mehra 2000][research_boskovic_mehra_2000]\] \[[Boskovic et al][research_boskovic_saimingli]\] \[[Bosworth and Williams-Hayes 2007][research_bosworth_williamshayes_2007]\] \[[Bosworth and Williams-Hayes 2010][research_bosworth_williamshayes_2010]\] \[[Bouadi][research_bouadi]\] \[[Bowling and Key 1976][research_bowling_key_1976]\] \[[Bradshaw et al 1985][research_bradshaw_davis_1985]\] \[[Brinker and Wise 1998][research_brinker_wise_1998]\] \[[Brinker and Wise 1999][research_brinker_wise_1999]\] \[[Brinker and Wise 2000][research_brinker_wise_2000]\] \[[Brinker and Wise 2001][research_brinker_wise_2001]\] \[[Buffington 1999][research_buffington_1999_b]\] \[[Buffington and Sparks 1998][research_buffington_sparks_1998_b]\] \[[Buffington et al 1993][research_buffington_sparks_1993]\] \[[Buffington et al 1994][research_buffington_sparks_1994]\] \[[Buffington et al 1998][research_buffington_sparks_1998]\] \[[Burcham and Burken 1994][research_burcham_burken_1994]\] \[[Burcham et al 1992][research_burcham_maine_1992]\] \[[Burken et al 2006][research_burken_williamshayes_2006]\] \[[Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]\] \[[Calise][research_calise]\] \[[Calise 2000][research_calise_2000]\] \[[Calise et al 1998][research_calise_lee_1998]\] \[[Calise et al 2001][research_calise_lee_2001]\] \[[Castaldi et al 2020][research_castaldi_mimmo_2020]\] \[[Chai Xue et al 2010][research_chaixue_wangganglin_2010]\] \[[Chakravarty 1987][research_chakravarty_1987]\] \[[Chavez and Vogel 2003][research_chavez_vogel_2003]\] \[[Chen and Lin 2021][research_chen_lin_2021]\] \[[Chen and Xie 2024][research_chen_xie_2024]\] \[[Chen et al 2019][research_chen_sun_2019]\] \[[ChunSheng Liu et al 2012][research_chunshengliu_xinzhongzhu_2012]\] \[[Citurs 1984][research_citurs_1984]\] \[[Clarke et al 2018][research_clarke_burken_2018]\] \[[Conceptual and Preliminary Design 2017][research_conceptual_and_2017]\] \[[Cong et al 2023][research_cong_hu_2023]\] \[[Control Allocation and Flight 2016][research_control_allocation_2016]\] \[[Cook 1997][research_cook_1997_d]\] \[[Cook 2007][research_cook_2007_d]\] \[[Cook 2013][research_cook_2013_d]\] \[[Corraro et al 2011][research_corraro_morani_2011]\] \[[Cui et al 2026][research_cui_zhang_2026]\] \[[Cui et al 2016][research_cui_yang_2016]\] \[[Dahiya 2017][research_dahiya_2017]\] \[[Dallery 1987][research_dallery_1987]\] \[[Davenport and Leggett 1993][research_davenport_leggett_1993]\] \[[de Araujo et al 1997][research_dearaujo_singh_1997]\] \[[de Carvalho Pereira and Júnior 2003][research_decarvalhopereira_junior_2003]\] \[[Demarchi and Haning 1978][research_demarchi_haning_1978]\] \[[Demourant and Ferreres 2013][research_demourant_ferreres_2013]\] \[[Dempster and Arnold 1969][research_dempster_arnold_1969]\] \[[Deshpande and Zhang 2021][research_deshpande_zhang_2021]\] \[[Development and flight evaluation 1980][research_development_and_1980]\] \[[Devi 2019][research_devi_2019]\] \[[Dixon 1972][research_dixon_1972]\] \[[Dong et al 2022][research_dong_liu_2022]\] \[[Dou et al 2025][research_dou_li_2025]\] \[[Doubrava et al 2008][research_doubrava_waszniowski_2008]\] \[[Driscoll 1966][research_driscoll_1966]\] \[[Duran 2026][research_duran_2026]\] \[[Eberhardt and Ward 1999][research_eberhardt_ward_1999]\] \[[Enns 1990][research_enns_1990]\] \[[Enns 2003][research_enns_2003]\] \[[Enns 2015][research_enns_2015]\] \[[Esfandabadi and Djavareshkian 2026][research_esfandabadi_djavareshkian_2026]\] \[[Esposito and Orlando 2020][research_esposito_orlando_2020]\] \[[Estimation and Sensitivity in 2026][research_estimation_and_2026]\] \[[Favre 2018][research_favre_2018]\] \[[Feedback Flight Control 2026][research_feedback_flight_2026]\] \[[Feedback Stability Augmentation 2023][research_feedback_stability_2023]\] \[[Flight Control 2015][research_flight_control_2015]\] \[[Flight Control Design 2015][research_flight_control_2015_b]\] \[[Flight control of an 2000][research_flight_control_of_2000]\] \[[Flight control system for 1999][research_flight_control_1999]\] \[[Fonterose and Hall 1996][research_fonterose_hall_1996]\] \[[Fosdick 1970][research_fosdick_1970]\] \[[Gal-Or 1994][research_galor_1994]\] \[[Gal-Or 2001][research_galor_2001]\] \[[Gandhi et al 2009][research_gandhi_cooper_2009]\] \[[Gao and Cai 2016][research_gao_cai_2016]\] \[[Gao and Liu 2021][research_gao_liu_2021]\] \[[Gao et al 2021][research_gao_an_2021]\] \[[Gao et al 2021][research_gao_an_2021_b]\] \[[Gao et al 2021][research_gao_an_2021_c]\] \[[Gao et al 2021][research_gao_an_2021_e]\] \[[Garrec and Kubica 2005][research_garrec_kubica_2005]\] \[[Garren and Kelley 1970][research_garren_kelley_1970]\] \[[Gavilan et al 2015][research_gavilan_vazquez_2015]\] \[[Gaylor 1984][research_gaylor_1984]\] \[[General Electric Co Schenectady Ny 1952][research_generalelectriccoschenectadyny_1952]\] \[[Generally on automatic flight][research_generally_on]\] \[[Gerren 1995][research_gerren_1995]\] \[[Getsov 2018][research_getsov_2018]\] \[[Goslin and Ho 1989][research_goslin_ho_1989]\] \[[Graffstein and Maslowski 2019][research_graffstein_maslowski_2019]\] \[[Gregory et al 2007][research_gregory_cao_2007]\] \[[Gregory et al 2011][research_gregory_gadient_2011]\] \[[Gu et al 2008][research_gu_natesan_2008]\] \[[Gumusboga and Iftar 2019][research_gumusboga_iftar_2019]\] \[[Gunnarsson 1997][research_gunnarsson_1997]\] \[[Gümüşboğa and İftar 2020][research_gumusboga_iftar_2020]\] \[[Ha 1990][research_ha_1990]\] \[[Haiping et al 2021][research_haiping_yanjun_2021]\] \[[Hall 1992][research_hall_1992]\] \[[Hammett et al][research_hammett_reigelsperger]\] \[[Hamza and Samir 2020][research_hamza_samir_2020]\] \[[Han et al 2025][research_han_zhang_2025]\] \[[Hardwick and Panella 2017][research_hardwick_panella_2017]\] \[[Hart 1956][research_hart_1956]\] \[[Hart 1968][research_hart_1968]\] \[[Hatch and Montgomery 1968][research_hatch_montgomery_1968]\] \[[Hatch and Montgomery 1969][research_hatch_montgomery_1969]\] \[[Hess and Peng 2018][research_hess_peng_2018]\] \[[Hgo and Ly 1995][research_hgo_ly_1995]\] \[[Hill 1987][research_hill_1987]\] \[[Holzapfel et al 2006][research_holzapfel_dacosta_2006]\] \[[Hou et al 2022][research_hou_lv_2022]\] \[[Hougui et al 1995][research_hougui_balas_1995]\] \[[Howell][research_howell]\] \[[Huber 1995][research_huber_1995]\] \[[Huber and Holdridge 1979][research_huber_holdridge_1979]\] \[[Ijaz et al 2019][research_ijaz_hamayun_2019_b]\] \[[Introduction The Flight Control 2017][research_introduction_the_2017]\] \[[Ito et al 2016][research_ito_endo_2016]\] \[[Jacobson and Lapins 1975][research_jacobson_lapins_1975]\] \[[Jang et al 1994][research_jang_kim_1994]\] \[[Grauer 2018][research_jaredagrauer_2018]\] \[[Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]\] \[[Jenks et al 1977][research_jenks_henry_1977]\] \[[Jiang et al 2019][research_jiang_zhang_2019]\] \[[Jiang et al 2026][research_jiang_li_2026]\] \[[Jiayu et al 2024][research_jiayu_yuchao_2024]\] \[[Johnson and Weir 1968][research_johnson_weir_1968]\] \[[Johnson and Weir 1969][research_johnson_weir_1969]\] \[[Johnson and Yang 1985][research_johnson_yang_1985]\] \[[Juhasz et al 2015][research_juhasz_tischler_2015]\] \[[Kannan and Bhat 2005][research_kannan_bhat_2005]\] \[[Karagiannis and Astolfi 2007][research_karagiannis_astolfi_2007]\] \[[Karr et al 2005][research_karr_nishita_2005]\] \[[Kass 1970][research_kass_1970]\] \[[Kefayat and Kamali 2024][research_kefayat_kamali_2024]\] \[[Keidel et al 2019][research_keidel_fasel_2019]\] \[[Kempel et al 1988][research_kempel_mcneill_1988]\] \[[Kendall and Morgan 2010][research_kendall_morgan_2010]\] \[[Kharisov and Hovakimyan 2010][research_kharisov_hovakimyan_2010]\] \[[Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]\] \[[Kitsios et al 2020][research_kitsios_dimopoulos_2020]\] \[[Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]\] \[[Klein et al 1982][research_klein_lapins_1982]\] \[[Knight and Wykes 1966][research_knight_wykes_1966]\] \[[Kolesnikov 2005][research_kolesnikov_2005]\] \[[Konar et al 1974][research_konar_mahesh_1974]\] \[[Kotfila and Painter 1969][research_kotfila_painter_1969]\] \[[Kownacki 2013][research_kownacki_2013]\] \[[Krishnaswamy et al][research_krishnaswamy_papageorgiou]\] \[[Kubica and Livet 1994][research_kubica_livet_1994]\] \[[Kucera and Hromčík 2013][research_kucera_hromcik_2013]\] \[[Kwatny et al 1991][research_kwatny_bennett_1991]\] \[[Köprücü and Öztürk 2024][research_koprucu_ozturk_2024]\] \[[Lapins et al 1982][research_lapins_klein_1982]\] \[[Larson 1986][research_larson_1986]\] \[[Larson 1987][research_larson_1987]\] \[[Lee and Singh 2013][research_lee_singh_2013]\] \[[Lee et al 2008][research_lee_byoungmunmin_2008]\] \[[Li et al 2013][research_li_yang_2013]\] \[[Li et al 2018][research_li_dong_2018]\] \[[Li et al 2018][research_li_zhang_2018]\] \[[Li et al 2019][research_li_sun_2019]\] \[[Li et al 2021][research_li_chen_2021]\] \[[Li et al 2023][research_li_han_2023]\] \[[Li et al 2023][research_li_liu_2023]\] \[[Li et al 2023][research_li_sun_2023]\] \[[Li et al 2024][research_li_han_2024]\] \[[Liao et al 2002][research_liao_wang_2002]\] \[[Lin et al 2017][research_lin_wang_2017]\] \[[Linear Quadratic Flight Control 2026][research_linear_quadratic_2026]\] \[[Lisoski and Kendall 2007][research_lisoski_kendall_2007]\] \[[Liu and Wang 2012][research_liu_wang_2012]\] \[[Liu and Whidborne 2021][research_liu_whidborne_2021]\] \[[Liu et al 2018][research_liu_zhang_2018]\] \[[Liu et al 2022][research_liu_wang_2022]\] \[[Liu et al 2026][research_liu_li_2026]\] \[[Liu et al 2026][research_liu_lyu_2026]\] \[[Lotze et al 1975][research_lotze_sensburg_1975]\] \[[Lu et al 2019][research_lu_ma_2019]\] \[[Lungu et al 2022][research_lungu_flores_2022]\] \[[Ly 1984][research_ly_1984]\] \[[Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]\] \[[Ma et al 2008][research_ma_li_2008]\] \[[Ma et al 2025][research_ma_alwi_2025]\] \[[Malcom and Husband 1976][research_malcom_husband_1976]\] \[[Maria-Agneta and Stef 2011][research_mariaagneta_stef_2011]\] \[[Marx 1977][research_marx_1977]\] \[[Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]\] \[[McCuish and Caldwell 2018][research_mccuish_caldwell_2018]\] \[[McKelvey 1993][research_mckelvey_1993]\] \[[McKenzie 1973][research_mckenzie_1973]\] \[[McLean 1994][research_mclean_1994]\] \[[McMaster and Schenk 1973][research_mcmaster_schenk_1973]\] \[[McNeill et al 1961][research_mcneill_mclean_1961]\] \[[Ming-Zhou et al 2016][research_mingzhou_guoping_2016]\] \[[Modern Aircraft Flight Control 1988][research_modern_aircraft_1988]\] \[[Moes et al 2006][research_moes_smith_2006]\] \[[Mohamed et al 2026][research_mohamed_abdullah_2026]\] \[[Molinari et al 2015][research_molinari_arrieta_2015]\] \[[Molinari et al 2018][research_molinari_arrieta_2018]\] \[[Montgomery and Price 1974][research_montgomery_price_1974]\] \[[Mooij 1985][research_mooij_1985_e]\] \[[Moore et al 2024][research_moore_rahimi_2024]\] \[[Moorhouse and Fielding 1998][research_moorhouse_fielding_1998]\] \[[Moreines et al 1965][research_moreines_sellite_1965]\] \[[Moreira et al 2022][research_moreira_gripp_2022]\] \[[Mulder 1988][research_mulder_1988]\] \[[Mulder et al 2009][research_mulder_lubbers_2009]\] \[[Muller 1967][research_muller_1967]\] \[[Multiloop Flight Control Systems 1990][research_multiloop_flight_1990]\] \[[Myala et al 2019][research_myala_borra_2019]\] \[[Myers and Walsh 1988][research_myers_walsh_1988]\] \[[Abdulwahab 2009][research_nabdulwahab_2009]\] \[[Nagabhushan and Lutze 1983][research_nagabhushan_lutze_1983]\] \[[Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]\] \[[Napolitano and Swaim 1989][research_napolitano_swaim_1989]\] \[[Narayanan et al 2026][research_narayanan_kumar_2026]\] \[[Nardi 1970][research_nardi_1970]\] \[[Nasir and Kuntjoro 2013][research_nasir_kuntjoro_2013]\] \[[Natesan and Bhat 2005][research_natesan_bhat_2005]\] \[[Newman and Buttrill 1995][research_newman_buttrill_1995]\] \[[Ngo et al][research_ngo_reigelsperger]\] \[[Ngo et al 1996][research_ngo_reigelsperger_1996]\] \[[Nguyen et al 2006][research_nguyen_krishnakumar_2006]\] \[[Nieto-Wire and Sobel 2009][research_nietowire_sobel_2009]\] \[[Nieto-Wire and Sobel 2011][research_nietowire_sobel_2011]\] \[[Nieto-Wire and Sobel 2014][research_nietowire_sobel_2014]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]\] \[[Obryan et al 1979][research_obryan_glover_1979]\] \[[Ogren et al 1974][research_ogren_sotanski_1974]\] \[[Okada et al 1987][research_okada_bando_1987]\] \[[Oki 1960][research_oki_1960]\] \[[Orhan and Subbarao 2021][research_orhan_subbarao_2021]\] \[[Ossmann 2015][research_ossmann_2015]\] \[[Osterhuber et al 2004][research_osterhuber_hanel_2004]\] \[[Owashi et al 2017][research_owashi_tanaka_2017]\] \[[Ozcan et al 2025][research_ozcan_tekyurt_2025]\] \[[Ozer 2025][research_ozer_2025]\] \[[Painter and Sitterle 1972][research_painter_sitterle_1972]\] \[[Park and Ohtsu 1998][research_park_ohtsu_1998]\] \[[Pasley et al 1973][research_pasley_rohling_1973]\] \[[Patel et al 2007][research_patel_cao_2007]\] \[[Patel et al 2007][research_patel_cao_2007_b]\] \[[Patterson 1984][research_patterson_1984]\] \[[Pedro and Tshabalala 2017][research_pedro_tshabalala_2017]\] \[[Pedro and Tshabalala 2017][research_pedro_tshabalala_2017_b]\] \[[Pei et al 2025][research_pei_huang_2025]\] \[[Peng et al 2014][research_peng_wang_2014]\] \[[Perez et al 2006][research_perez_liu_2006]\] \[[Petersen 1979][research_petersen_1979]\] \[[Petersen 1981][research_petersen_1981]\] \[[Phillips][research_phillips]\] \[[Phillips et al 2010][research_phillips_gururajan_2010]\] \[[PI control of a 1999][research_pi_control_1999]\] \[[Placement in Flight Control 2026][research_placement_in_2026]\] \[[Posingies 1968][research_posingies_1968]\] \[[Powell and Katz 1974][research_powell_katz_1974]\] \[[Prochazka et al 2018][research_prochazka_eduardo_2018]\] \[[Qu et al 2011][research_qu_li_2011]\] \[[Qu et al 2013][research_qu_li_2013]\] \[[Quantitative Design Requirements for 2017][research_quantitative_design_2017]\] \[[Querry][research_querry]\] \[[Raj and Mohan 2015][research_raj_mohan_2015]\] \[[Rajput et al 2015][research_rajput_zhangweiguo_2015]\] \[[Rao 1984][research_rao_1984]\] \[[Rastgoftar et al 2017][research_rastgoftar_ni_2017]\] \[[Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]\] \[[Reigelsperger et al 1995][research_reigelsperger_hammett_1995]\] \[[Rezazadeh Movahhed and Hamed 2025][research_rezazadehmovahhed_hamed_2025]\] \[[Rezazadeh Movahhed and Hamed 2026][research_rezazadehmovahhed_hamed_2026]\] \[[Rickard 1978][research_rickard_1978]\] \[[Rising 1982][research_rising_1982]\] \[[Rising et al 1984][research_rising_davis_1984]\] \[[Ro et al 1992][research_ro_barlow_1992]\] \[[Robbins et al 2023][research_robbins_stansbury_2023]\] \[[Roberts et al 2006][research_roberts_yang_2006]\] \[[Rogalski 2018][research_rogalski_2018]\] \[[Rogalski et al 2021][research_rogalski_rzucidlo_2021]\] \[[Rolek 1974][research_rolek_1974]\] \[[Rooney et al 1982][research_rooney_chung_1982]\] \[[Roskam 1977][research_roskam_1977]\] \[[Sadoff 1962][research_sadoff_1962]\] \[[Sanders et al 2018][research_sanders_tischler_2018]\] \[[Sanfilippo 1970][research_sanfilippo_1970]\] \[[Sang][research_sang]\] \[[Saussie et al 2011][research_saussie_akhrif_2011]\] \[[Schmidt 1986][research_schmidt_1986]\] \[[Schmidt 2016][research_schmidt_2016]\] \[[Schwanz 1972][research_schwanz_1972]\] \[[Sevart 1971][research_sevart_1971]\] \[[Sevart and Patel 1973][research_sevart_patel_1973]\] \[[Sevart et al 1972][research_sevart_patel_1972]\] \[[Shayan and Van Kampen 2021][research_shayan_vankampen_2021]\] \[[Shen and Chen 2025][research_shen_chen_2025]\] \[[Shen et al 2021][research_shen_huang_2021]\] \[[Shi and Ma 2023][research_shi_ma_2023]\] \[[Shin 2010][research_shin_2010]\] \[[Shin 2011][research_shin_2011]\] \[[Shmul et al 2018][research_shmul_erenthal_2018]\] \[[Shrivastava 1987][research_shrivastava_1987]\] \[[Shtessel et al 1999][research_shtessel_buffington_1999]\] \[[Shtessel et al 2002][research_shtessel_buffington_2002]\] \[[Shuang et al 2016][research_shuang_zhang_2016]\] \[[Shuang et al 2017][research_shuang_zhang_2017]\] \[[Simon 2014][research_simon_2014]\] \[[Simulation Requirements for Flight 2017][research_simulation_requirements_2017]\] \[[Singh 2016][research_singh_2016]\] \[[Singh and Chowdhury 2021][research_singh_chowdhury_2021]\] \[[Singh and Raol 2000][research_singh_raol_2000]\] \[[Siwakosit et al 2000][research_siwakosit_hess_2000]\] \[[Sizlo et al 1979][research_sizlo_berg_1979]\] \[[Smith and Taylor 1967][research_smith_taylor_1967]\] \[[Snell 1998][research_snell_1998]\] \[[Snyder et al 1972][research_snyder_fry_1972]\] \[[Sobel 1982][research_sobel_1982]\] \[[Sobel et al 1986][research_sobel_lee_1986]\] \[[Sonneveldt et al 2011][research_sonneveldt_chu_2011]\] \[[Sparks][research_sparks]\] \[[Srour et al 2021][research_srour_noura_2021]\] \[[Stengel 1973][research_stengel_1973]\] \[[Su et al 2023][research_su_hu_2023]\] \[[Sun and Hu 2005][research_sun_hu_2005]\] \[[Sun and Xu 2021][research_sun_xu_2021]\] \[[Taylor and Yoo 2011][research_taylor_yoo_2011]\] \[[Terrell and Zein-Sabatto 2017][research_terrell_zeinsabatto_2017]\] \[[Test Techniques for Flight 2021][research_test_techniques_2021]\] \[[Tingting and Aijun 2014][research_tingting_aijun_2014]\] \[[Tischler 2018][research_tischler_2018]\] \[[Tischler 2018][research_tischler_2018_b]\] \[[Toffol et al 2025][research_toffol_paolini_2025]\] \[[Tonon and Belluati 2018][research_tonon_belluati_2018]\] \[[Traas et al 2026][research_traas_atmaca_2026]\] \[[Ul Haq et al 2026][research_ulhaq_atmaca_2026]\] \[[Urbano][research_urbano]\] \[[Urnes 2012][research_urnes_2012]\] \[[Urnes and Yeager 1991][research_urnes_yeager_1991]\] \[[Vandierendonck 1973][research_vandierendonck_1973]\] \[[Vepa 2023][research_vepa_2023]\] \[[Vetter 2002][research_vetter_2002]\] \[[Vile et al 2019][research_vile_alwi_2019]\] \[[Vile et al 2019][research_vile_alwi_2019_b]\] \[[Vile et al 2020][research_vile_alwi_2020]\] \[[Vile et al 2021][research_vile_alwi_2021]\] \[[Vos et al 2002][research_vos_brown_2002]\] \[[Wakayama 2008][research_wakayama_2008]\] \[[Wang and Guo 2012][research_wang_guo_2012]\] \[[Wang and Qi 2021][research_wang_qi_2021]\] \[[Wang and Wang 2012][research_wang_wang_2012]\] \[[Wang and Wang 2012][research_wang_wang_2012_b]\] \[[Wang et al 2020][research_wang_zhang_2020]\] \[[Wang et al 2024][research_wang_sun_2024]\] \[[Wang et al 2024][research_wang_zhang_2024_b]\] \[[Wang et al 2026][research_wang_li_2026]\] \[[Wawrzyniak 1970][research_wawrzyniak_1970]\] \[[Weinstein et al 2018][research_weinstein_hubbard_2018]\] \[[Wells 2002][research_wells_2002]\] \[[Wells and Hess 2002][research_wells_hess_2002]\] \[[Wen-qiang et al 2008][research_wenqiang_jianjun_2008]\] \[[Wilson et al 2014][research_wilson_peters_2014]\] \[[Wise 1992][research_wise_1992]\] \[[Wise et al 1999][research_wise_brinker_1999]\] \[[Wittenmark 1990][research_wittenmark_1990]\] \[[Wu and Zheng 2022][research_wu_zheng_2022]\] \[[Wykes 1968][research_wykes_1968]\] \[[Xi and Zhao 2017][research_xi_zhao_2017]\] \[[Xiaoxiao and Zhu 2025][research_xiaoxiao_zhu_2025]\] \[[Xu et al 2013][research_xu_zhu_2013]\] \[[Xu et al 2022][research_xu_yang_2022]\] \[[Xu et al 2026][research_xu_gao_2026]\] \[[Yan et al 2025][research_yan_sun_2025]\] \[[Yang][research_yang]\] \[[Yang and Gao 2020][research_yang_gao_2020]\] \[[Yang et al 2024][research_yang_wen_2024]\] \[[Ye et al 2009][research_ye_zhang_2009]\] \[[Yechout and Oelschlaeger 1976][research_yechout_oelschlaeger_1976]\] \[[Yingsong et al 2015][research_yingsong_zhichun_2015]\] \[[Yong et al 2020][research_yong_wu_2020]\] \[[yu et al 2022][research_yu_li_2022]\] \[[Yu et al 2023][research_yu_li_2023]\] \[[Yu et al 2023][research_yu_li_2023_b]\] \[[Yu et al 2023][research_yu_tailless_2023]\] \[[Yu et al 2024][research_yu_li_2024]\] \[[Yu et al 2024][research_yu_li_2024_b]\] \[[Yuwei et al 2021][research_yuwei_aijun_2021]\] \[[Zhang 2021][research_zhang_2021]\] \[[Zhang and He 2026][research_zhang_he_fluidic_2026]\] \[[Zhang and Ma 2021][research_zhang_ma_2021]\] \[[Zhang and Meng 2019][research_zhang_meng_2019]\] \[[Zhang et al 2007][research_zhang_suresh_2007]\] \[[Zhang et al 2008][research_zhang_rabbath_2008]\] \[[Zhang et al 2013][research_zhang_zhu_2013]\] \[[Zhang et al 2015][research_zhang_wang_2015]\] \[[Zhang et al 2018][research_zhang_liu_2018]\] \[[Zhang et al 2025][research_zhang_zhao_2025]\] \[[Zhao et al 2023][research_zhao_deng_2023]\] \[[Zhao et al 2025][research_zhao_wang_2025]\] \[[Zheng and Xu 2013][research_zheng_xu_2013]\] \[[Zhijie et al 2025][research_zhijie_taiyu_2025]\] \[[Zhishuai and Lingling 2022][research_zhishuai_lingling_2022]\] \[[Zhong et al 2009][research_zhong_yang_2009]\] \[[Zhou 1994][research_zhou_1994]\] \[[Zhou et al 2025][research_zhou_liu_2025]\] \[[Zilong et al 2024][research_zilong_jie_2024]\] \[[Zogopoulos-Papaliakos et al 2020][research_zogopoulospapaliakos_karras_2020]\] \[[Zou][research_zou]\] \[[Zou et al 2012][research_zou_yang_2012]\] \[[Zou et al 2017][research_zou_yin_2017]\] \[[Zou et al 2026][research_zou_zhen_2026]\] \[[Zweig and Ben-Asher 1995][research_zweig_benasher_1995]\]

### Tailless, flying wing and blended wing body configurations

**The configuration itself, in every aspect the titles name.** The record runs from the all-wing and tailless studies of the 1940s through the oblique flying wing to the blended wing body and the unmanned flying wing, and it includes the structural, acoustic and design-optimisation work on those configurations as well as their stability and control.

**433 records.** \[[Adamo 2023][research_adamo_2023]\] \[[Adegbindin et al 2016][research_adegbindin_love_2016]\] \[[Adler and Martins 2023][research_adler_martins_2023]\] \[[Ahmed et al 2024][research_ahmed_zakaria_2024]\] \[[Alex 2014][research_alex_2014]\] \[[Ali et al 2025][research_ali_okasha_2025]\] \[[Ali et al 2026][research_ali_rasani_2026]\] \[[Alsahlani et al 2017][research_alsahlani_johnston_2017]\] \[[Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]\] \[[Ammar and Trépanier 2014][research_ammar_trepanier_2014]\] \[[Ammar et al 2017][research_ammar_legros_2017]\] \[[Ando and Kajita 1992][research_ando_kajita_1992]\] \[[Ankenbruck 1946][research_ankenbruck_1946]\] \[[Ankenbruck and McKinney 1947][research_ankenbruck_mckinney_1947]\] \[[Antoniou et al 2025][research_antoniou_antoniou_2025]\] \[[Atmaca et al 2026][research_atmaca_stroosma_2026]\] \[[Aubeelack][research_aubeelack]\] \[[Bainsla et al 2021][research_bainsla_singari_2021]\] \[[Balasubramanian et al 2024][research_balasubramanian_ahuja_2024]\] \[[Balasubramanian et al 2026][research_balasubramanian_n_2026]\] \[[Banerjee 1984][research_banerjee_1984]\] \[[Banerjee 1988][research_banerjee_1988]\] \[[Banerjee 1988][research_banerjee_1988_b]\] \[[Bennett 1947][research_bennett_1947]\] \[[Bishop 1961][research_bishop_1961]\] \[[Bosworth and Stoliker 1996][research_bosworth_stoliker_1996]\] \[[Bourdin et al 2007][research_bourdin_gatto_2007]\] \[[Bowlus et al 1997][research_bowlus_multhopp_1997]\] \[[Brewer and May 1948][research_brewer_may_1948]\] \[[Brown and Vos 2018][research_brown_vos_2018]\] \[[Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]\] \[[Buch and George M. 2010][research_buch_georgem_2010]\] \[[Buddhamatya et al 2026][research_buddhamatya_miranda_2026]\] \[[Buffington 1997][research_buffington_1997]\] \[[Buffington 1999][research_buffington_1999]\] \[[Cai et al 2021][research_cai_xie_2021]\] \[[Cameron and Cameron 1997][research_cameron_cameron_1997]\] \[[Cameron and Princen 2000][research_cameron_princen_2000]\] \[[Campbell et al 2005][research_campbell_carter_2005]\] \[[Carlsson 2003][research_carlsson_2003]\] \[[Carlsson 2005][research_carlsson_2005]\] \[[Carter et al 2008][research_carter_campbell_2008]\] \[[Chan et al 2017][research_chan_hooker_2017]\] \[[Chao et al 2017][research_chao_flanagan_2017]\] \[[Chaudhuri et al 2018][research_chaudhuri_jasa_2018]\] \[[Chen et al 2026][research_chen_gray_2026]\] \[[Chung et al 2010][research_chung_hallberg_2010]\] \[[Chung et al 2019][research_chung_ma_2019]\] \[[Clark and Gerhold 1999][research_clark_gerhold_1999]\] \[[Colgren and Loschke 2008][research_colgren_loschke_2008]\] \[[Cong et al 2023][research_cong_hu_2023_b]\] \[[Contreras-Torres et al 2022][research_contrerastorres_garciarodriguez_2022]\] \[[Costa et al 1994][research_costa_koopman_1994]\] \[[Covell 1985][research_covell_1985]\] \[[Cox et al 1949][research_cox_siddall_1949]\] \[[Cusher and Gopalarathnam 2006][research_cusher_gopalarathnam_2006]\] \[[Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]\] \[[Danowsky et al 2017][research_danowsky_schmidt_2017]\] \[[Danowsky et al 2018][research_danowsky_kotikalpudi_2018]\] \[[de Becdelievre and Kroo 2021][research_debecdelievre_kroo_2021]\] \[[Deb et al 2006][research_deb_gangtao_2006]\] \[[DeLaurier 2022][research_delaurier_2022]\] \[[Denieul et al 2015][research_denieul_alazard_2015]\] \[[Deslich et al 2021][research_deslich_flick_2021]\] \[[Development of Neo-Ptero Tailless 2018][research_development_of_2018]\] \[[DiMaggio et al 2023][research_dimaggio_hartfield_2023]\] \[[Dimopoulos et al 2019][research_dimopoulos_panagiotou_2019]\] \[[Dong et al 2020][research_dong_shi_2020]\] \[[Drinkwater et al 1970][research_drinkwater_1970]\] \[[Dufaure De Lajarte 1936][research_delajarte_1936]\] \[[Elenin 2021][research_elenin_2021]\] \[[Ericsson 1997][research_ericsson_1997_c]\] \[[Ericsson and Beyers 2002][research_ericsson_beyers_2002]\] \[[Esteban 2001][research_esteban_2001]\] \[[Experimental investigation of synthetic 2023][research_experimental_investigation_2023]\] \[[Fairuz Izzuddin Romli et al 2023][research_fairuzizzuddinromli_muhammadaimanmohammadsabri_2023]\] \[[Fan et al 2006][research_fan_zhu_2006]\] \[[Fears et al 1995][research_fears_ross_1995]\] \[[Fernandes and Maldonado 2024][research_fernandes_maldonado_2024]\] \[[Flanagan et al 2019][research_flanagan_chao_2019]\] \[[Flow Control and High-Lift 2016][research_flow_control_2016]\] \[[Flow Field Investigation of 2023][research_flow_field_2023]\] \[[Fremaux et al 1995][research_fremaux_vairo_1995]\] \[[Friehmelt 1996][research_friehmelt_1996]\] \[[From Tube and Wing 2013][research_from_tube_2013]\] \[[Fukuda and Takimoto 2014][research_fukuda_takimoto_2014]\] \[[Gal-Or 2003][research_galor_2003]\] \[[Gamble and Inman 2016][research_gamble_inman_2016]\] \[[Ganesh et al 2021][research_ganesh_keerthi_2021]\] \[[Gao and Smith 2020][research_gao_smith_2020]\] \[[Garbell 1946][research_garbell_1946]\] \[[Garmendia and Mavris 2015][research_garmendia_mavris_2015]\] \[[Gillard et al 1997][research_gillard_dorsett_1997]\] \[[Gilmore et al 2002][research_gilmore_wakayama_2002]\] \[[Goodson and King 1949][research_goodson_king_1949]\] \[[Grismer et al 1997][research_grismer_myatt_1997]\] \[[Ground testing of X-48B 2007][research_ground_testing_2007]\] \[[Guo et al 2014][research_guo_burley_2014]\] \[[Gupta et al 2016][research_gupta_seiler_2016]\] \[[Guruswamy 1991][research_guruswamy_1991]\] \[[Hall et al 2006][research_hall_lawrence_2006]\] \[[Hansmann and Stumpf 2025][research_hansmann_stumpf_2025]\] \[[Hansmann and Stumpf 2026][research_hansmann_stumpf_2026]\] \[[Hao et al 2023][research_hao_ma_2023]\] \[[Harley et al 2009][research_harley_wilde_2009]\] \[[Harper and Jones 1947][research_harper_jones_1947]\] \[[Harris and Harris 1997][research_harris_harris_1997]\] \[[Hauser 1999][research_hauser_1999]\] \[[He et al 2022][research_he_hu_2022]\] \[[He et al 2018][research_he_aljiboory_2018]\] \[[He et al 2022][research_he_hu_2022_b]\] \[[He et al 2023][research_he_hu_2023]\] \[[Hefazi et al 2013][research_hefazi_vore_2013]\] \[[Heinze 1932][research_heinze_1932]\] \[[Hoffler et al 1988][research_hoffler_rao_1988]\] \[[Hong and Ma 2016][research_hong_ma_2016]\] \[[Howard et al 2002][research_howard_demoss_2002]\] \[[Hu][research_hu]\] \[[Hu et al 2024][research_hu_tailless_review_2024]\] \[[Hu et al 2025][research_hu_zhao_2025]\] \[[Huang and Zhang 2020][research_huang_zhang_2020]\] \[[Huber 2022][research_huber_2022]\] \[[Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]\] \[[Ibrahim et al 2023][research_ibrahim_kamal_2023]\] \[[Iniguez de Heredia and Friehmelt 2005][research_iniguezdeheredia_friehmelt_2005]\] \[[Izquierdo][research_izquierdo]\] \[[Jackson 2023][research_jackson_2023]\] \[[Jagtap et al 2025][research_jagtap_childs_2025]\] \[[Jentzsch et al 2017][research_jentzsch_taubert_2017]\] \[[Jentzsch et al 2019][research_jentzsch_2019]\] \[[Jernell 1978][research_jernell_1978]\] \[[Jiguang Li et al 2016][research_jiguangli_xinchen_2016]\] \[[Jo et al 2015][research_jo_park_2015]\] \[[Jo et al 2016][research_jo_park_2016]\] \[[Johnson 1949][research_johnson_glider_1949]\] \[[Jones et al 2006][research_jones_franke_2006]\] \[[Jun 2023][research_jun_2023]\] \[[Jung and Lowenberg 2005][research_jung_lowenberg_2005]\] \[[Justin James Matt et al 2025][research_justinjamesmatt_haiyangchao_2025]\] \[[Jyothi et al 2006][research_jyothi_bindu_2006]\] \[[Kale and Pendharkar 2021][research_kale_pendharkar_2021]\] \[[Kalyankar et al 2024][research_kalyankar_pompe_2024]\] \[[Kalyankar et al 2025][research_kalyankar_urreiztieta_2025]\] \[[Kang and Choi 2022][research_kang_choi_2022]\] \[[Kania et al 2025][research_kania_2025]\] \[[Karimi Kelayeh and Djavareshkian 2021][research_karimikelayeh_djavareshkian_2021]\] \[[Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]\] \[[Kashiwagura and Shimoyama 2018][research_kashiwagura_shimoyama_2018]\] \[[Keidel et al 2017][research_keidel_fasel_2017]\] \[[Keidel et al 2020][research_keidel_fasel_2020]\] \[[Kim et al 2013][research_kim_ahn_2013]\] \[[Kim et al 2025][research_kim_koh_2025]\] \[[Kotikalpudi et al 2018][research_kotikalpudi_danowsky_2018]\] \[[Kroo 1994][research_kroo_1994]\] \[[Kumar et al 2020][research_kumar_mandal_2020]\] \[[Kumar et al 2023][research_kumar_okasha_2023]\] \[[Kwiek 2019][research_kwiek_2019]\] \[[Kwiek and Figat 2016][research_kwiek_figat_2016]\] \[[Laar et al 2024][research_laar_atherstone_2024]\] \[[Lee 1946][research_lee_1946]\] \[[Lee 1947][research_lee_1947]\] \[[Lee et al 2023][research_lee_nam_2023]\] \[[Legriffon et al 2023][research_legriffon_bertsch_2023]\] \[[Leishman 2026][research_leishman_2026]\] \[[Lemko and Molodchyk 2015][research_lemko_molodchyk_2015]\] \[[Li 2024][research_li_2024]\] \[[Li et al 2017][research_li_chen_2017]\] \[[Li et al 2017][research_li_yong_2017]\] \[[Li et al 2022][research_li_sun_2022]\] \[[Li et al 2023][research_li_wing_rock_2023]\] \[[Li et al 2026][research_li_shu_2026]\] \[[Li Peng et al 2009][research_lipeng_qinweiwei_2009]\] \[[Liebeck 2002][research_liebeck_2002]\] \[[Liebeck 2003][research_liebeck_2003]\] \[[Liebeck 2008][research_liebeck_2008]\] \[[Liebeck et al 1998][research_liebeck_page_1998]\] \[[Liersch and Bishop 2018][research_liersch_bishop_2018]\] \[[Lim et al 2025][research_lim_hur_2025]\] \[[Lin et al 2026][research_lin_zong_2026]\] \[[Liu and Hu 2014][research_liu_hu_2014]\] \[[Liu and Wang 2025][research_liu_wang_2025]\] \[[Liu and Zhang 2022][research_liu_zhang_rudder_2022]\] \[[Liu et al 2021][research_liu_luo_2021]\] \[[Liu et al 2026][research_liu_flying_wing_aero_2026]\] \[[Luckring and Hiller 2025][research_luckring_hiller_2025]\] \[[Lucky Bose et al 2024][research_luckybose_isfaqahmedrafsun_2024]\] \[[Luu 2025][research_luu_2025]\] \[[Lyu et al 2023][research_lyu_zhang_2023]\] \[[Ma and Wang 2009][research_ma_wang_2009]\] \[[Maggin 1944][research_maggin_1944]\] \[[Mahmood 2025][research_mahmood_2025]\] \[[Mahmood et al 2025][research_mahmood_aasim_2025]\] \[[Maimako et al 2026][research_maimako_mintah_2026]\] \[[Marques 2013][research_marques_2013]\] \[[Mastin et al 1996][research_mastin_smith_1996]\] \[[Matamoros and de Visser 2018][research_matamoros_devisser_2018]\] \[[McKeehen 1998][research_mckeehen_1998]\] \[[McKeehen et al 1997][research_mckeehen_myatt_1997]\] \[[Meckstroth and Blake 2015][research_meckstroth_blake_2015]\] \[[Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]\] \[[Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020_b]\] \[[Meheut et al 2012][research_meheut_arntz_2012]\] \[[Michal 1998][research_michal_1998]\] \[[Milenković-Babić et al 2024][research_milenkovicbabic_ivkovic_2024]\] \[[Miller and Forster 2025][research_miller_forster_2025]\] \[[Minghang and Hu 2014][research_minghang_hu_2014]\] \[[Modeling and Control for 2015][research_modeling_and_2015]\] \[[Mohan and Kumar 2023][research_mohan_kumar_2023]\] \[[Mohd. Nasir 2026][research_mohdnasir_2026]\] \[[Moitra 1985][research_moitra_1985]\] \[[Morris 1992][research_morris_1992]\] \[[Morris and Tigner 1995][research_morris_tigner_1995]\] \[[Morris et al 2012][research_morris_allison_2012]\] \[[Morris et al 2014][research_morris_allison_2014]\] \[[Murray 1949][research_murray_1949]\] \[[Muñoz][research_munoz]\] \[[Myatt et al 1998][research_myatt_schumacher_1998]\] \[[Laitone 1943][research_tailless_highspeed_1943]\] \[[Donlan 1944][research_tailless_interim_1944]\] \[[Ankenbruck 1945][research_allwing_modifications_1945]\] \[[Seacord and Campbell 1945][research_allwing_stability_1945]\] \[[Sawyer and Trant 1947][research_xf7u_semispan_1947]\] \[[Sadoff and Crossfield 1954][research_x4_flight_evaluation_1954]\] \[[Arbic 1956][research_tailless_freeflight_1956]\] \[[Nangia and Palmer 2002][research_nangia_palmer_2002]\] \[[Vandervelden 1989][research_oblique_flying_wing_1989]\] \[[Fremaux et al 1993][research_tumbling_characteristics_1993]\] \[[Carter et al 2006][research_bwb_bli_2006]\] \[[NASA advanced design program 1993][research_nasa_advanced_1993]\] \[[Nasir et al 2012][research_nasir_kuntjoro_2012]\] \[[Nie et al 2021][research_nie_liu_2021]\] \[[Niestroy 2025][research_niestroy_2025]\] \[[Niestroy et al 2017][research_niestroy_dorsett_2017]\] \[[Niestroy et al 2019][research_niestroy_williams_2019]\] \[[Nieto-Wire and Sobel 2007][research_nietowire_sobel_2007]\] \[[Nieto-Wire and Sobel 2013][research_nietowire_sobel_2013]\] \[[Nikbay et al 2025][research_nikbay_yildiz_2025]\] \[[Niu et al 2023][research_niu_yan_2023]\] \[[Okolo et al 2014][research_okolo_dogan_2014]\] \[[Okonkwo and Jemitola 2022][research_okonkwo_jemitola_2022]\] \[[Oyama 2021][research_oyama_2021]\] \[[Nishanth et al 2019][research_p_arokkiaswamy_2019]\] \[[Pambagjo et al 2001][research_pambagjo_nakahashi_2001]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Panagiotou et al 2022][research_panagiotou_antoniou_2022]\] \[[Papamoschou and Mayoral 2014][research_papamoschou_mayoral_2014]\] \[[Paranjape and Chung 2010][research_paranjape_chung_2010]\] \[[Paranjape et al 2011][research_paranjape_chung_2011]\] \[[Parello][research_parello]\] \[[Park et al 2016][research_park_jo_2016]\] \[[Park et al 2017][research_park_choi_2017]\] \[[Park et al 2017][research_park_jo_2017]\] \[[Paudel 2016][research_paudel_2016]\] \[[Paul and Rein 2016][research_paul_rein_2016]\] \[[Paul and Rein 2017][research_paul_rein_2017]\] \[[Paul et al 1997][research_paul_garrard_1997]\] \[[Paulus et al 2013][research_paulus_wirth_2013]\] \[[Peigin and Epstein 2006][research_peigin_epstein_2006]\] \[[Pena and Voulgaris 2001][research_pena_voulgaris_2001]\] \[[Peng et al 2013][research_peng_xuefeng_2013]\] \[[Petrenko and Gašparovič 2025][research_petrenko_gasparovic_2025]\] \[[Phillips et al 2019][research_phillips_jentzsch_2019]\] \[[Potsdam et al 1997][research_potsdam_page_1997]\] \[[Protz and Sparks 1998][research_protz_sparks_1998]\] \[[Qi et al 2017][research_qi_wang_2017]\] \[[Qi et al 2018][research_qi_zhao_2018]\] \[[Qi et al 2018][research_qi_zhao_2018_b]\] \[[Qi et al 2021][research_qi_bwb_2021]\] \[[Qian and Alonso 2018][research_qian_alonso_2018]\] \[[Qian and Alonso 2021][research_qian_alonso_2021]\] \[[Qin 2002][research_qin_2002]\] \[[Qin et al 2007][research_qin_wong_2007]\] \[[Raghavan and Patil 2009][research_raghavan_patil_2009]\] \[[Rajput et al 2014][research_rajput_zhang_2014]\] \[[Rao and Huffman 1978][research_rao_huffman_1978]\] \[[Razon et al 2023][research_razon_maher_2023]\] \[[Regan 2008][research_regan_2008]\] \[[Reimann et al 2005][research_reimann_tinetti_2005]\] \[[Reist and Zingg 2014][research_reist_zingg_2014]\] \[[Reist and Zingg 2015][research_reist_zingg_2015]\] \[[Reist and Zingg 2016][research_reist_zingg_2016]\] \[[Rickey 1946][research_rickey_1946]\] \[[Riethausen 2026][research_riethausen_2026]\] \[[Robb et al 2023][research_robb_vuppala_2023]\] \[[Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]\] \[[Rojas Carvajal and Amitay 2025][research_rojascarvajal_amitay_2025]\] \[[Rojas Carvajal et al 2022][research_rojascarvajal_guha_2022]\] \[[Rojas Carvajal et al 2024][research_rojascarvajal_kumarguha_2024]\] \[[Rolls and Wingrove 1958][research_rolls_wingrove_1958]\] \[[Roman et al 2000][research_roman_allen_2000]\] \[[Roman et al 2003][research_roman_gilmore_2003]\] \[[Rossetti and Beblo 2022][research_rossetti_beblo_2022]\] \[[Roy 2009][research_roy_2009]\] \[[Roy and Ghosh 2010][research_roy_ghosh_2010]\] \[[Roysdon and Khalid 2010][research_roysdon_khalid_2010]\] \[[Roysdon and Khalid 2011][research_roysdon_khalid_2011]\] \[[Rui et al 2007][research_rui_zhou_2007]\] \[[Ruseno 2021][research_ruseno_2021]\] \[[Rustagi et al 2018][research_rustagi_kothari_2018]\] \[[Sudhakar et al 2025][research_s_c_2025]\] \[[Saephan and van Dam 2006][research_saephan_vandam_2006]\] \[[Saephan and van Dam 2006][research_saephan_vandam_2006_b]\] \[[Saheby et al 2026][research_saheby_2026]\] \[[Saucez and Boiffier 2012][research_saucez_boiffier_2012]\] \[[Sawyer and Trant 1950][research_sawyer_trant_1950]\] \[[Schirrer et al 2013][research_schirrer_kozek_2013]\] \[[Schmidt et al 2016][research_schmidt_zhao_2016]\] \[[Schmidt et al 2019][research_schmidt_danowsky_2019]\] \[[Sears 1980][research_sears_1980]\] \[[Seebass 1997][research_seebass_1997]\] \[[Sgueglia][research_sgueglia]\] \[[Shao et al 2024][research_shao_guo_2024]\] \[[Sharma and Hosder 2024][research_sharma_hosder_2024]\] \[[Shearwood et al 2020][research_shearwood_2020]\] \[[Shearwood et al 2020][research_shearwood_nabawy_2020]\] \[[Shearwood et al 2021][research_shearwood_nabawy_2021]\] \[[Shearwood et al 2021][research_shearwood_nabawy_2021_b]\] \[[Shearwood et al 2023][research_shearwood_nabawy_2023]\] \[[Shekar et al 2026][research_shekar_molloy_2026]\] \[[Sheneshen and kamal 2025][research_sheneshen_kamal_2025]\] \[[Sherman et al 2021][research_sherman_tirona_2021]\] \[[Shi and Wu 2022][research_shi_wu_2022]\] \[[Siddiqui et al 2025][research_siddiqui_maqsood_2025]\] \[[Silva][research_silva_b]\] \[[Silva et al 2019][research_silva_grinet_2019]\] \[[Silvers and Spreemann 1950][research_silvers_spreemann_1950]\] \[[Simon et al 1993][research_simon_blake_1993]\] \[[Simon et al 2023][research_simon_williams_2023]\] \[[Simon et al 2024][research_simon_williams_2024]\] \[[Singh et al 2016][research_singh_toropov_2016]\] \[[Smith 1953][research_smith_tailless_1953]\] \[[Song et al 2014][research_song_yang_2014]\] \[[Sparks and Sparks 1997][research_sparks_sparks_1997]\] \[[Staelens et al 2007][research_staelens_blackwelder_2007]\] \[[Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]\] \[[Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]\] \[[Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]\] \[[Stevens and McCormack 1944][research_stevens_mccormack_1944]\] \[[Stone and Daughtridge 1948][research_stone_daughtridge_1948]\] \[[Su et al 2014][research_su_zhou_2014]\] \[[Su et al 2022][research_su_hu_2022]\] \[[Sudhakar et al 2026][research_sudhakar_prem_2026]\] \[[Sun et al 2024][research_sun_zhou_2024]\] \[[Suresh et al 2012][research_suresh_siddesh_2012]\] \[[Suresh et al 2013][research_suresh_radhakrishnan_2013]\] \[[Susanto 2022][research_susanto_2022]\] \[[Tahir et al 2026][research_tahir_wing_rock_2026]\] \[[Tan et al 2014][research_tan_zhou_2014]\] \[[Taylor and Ratnayake 2011][research_taylor_ratnayake_2011]\] \[[Teel 1999][research_teel_1999]\] \[[Teel 1999][research_teel_1999_b]\] \[[Thomas et al 2010][research_thomas_burley_2010]\] \[[Tigner et al 1998][research_tigner_holden_1998]\] \[[Tipton and Smith 1995][research_tipton_smith_1995]\] \[[Tipton et al 1996][research_tipton_smith_1996]\] \[[Tomac and Stenfelt 2014][research_tomac_stenfelt_2014]\] \[[Torenbeek 2016][research_torenbeek_2016]\] \[[Torvik 1990][research_torvik_1990]\] \[[Tournes and Johnson 1999][research_tournes_johnson_1999]\] \[[Tournes et al 1997][research_tournes_shtessel_1997]\] \[[Tsuchiya et al 2022][research_tsuchiya_takahashi_2022]\] \[[Vale J 2013][research_valej_2013]\] \[[Van der Velden 1987][research_vandervelden_1987]\] \[[Veismann et al 2023][research_veismann_2023]\] \[[Velden 1997][research_velden_1997]\] \[[Velicki and Thrash 2010][research_velicki_thrash_2010]\] \[[Vitale Press and Shufflebarger 1954][research_vitale_1954]\] \[[Voss et al 2026][research_voss_frohler_2026]\] \[[Wakayama 1998][research_wakayama_1998]\] \[[Wakayama 2000][research_wakayama_2000]\] \[[Wakayama and Kroo 1998][research_wakayama_kroo_1998]\] \[[Wang and Feng 2025][research_wang_feng_2025]\] \[[Wang and Feng 2026][research_wang_feng_2026]\] \[[Wang et al 2020][research_wang_tang_2020]\] \[[Wang and Zhao 2025][research_wang_zhao_2025]\] \[[Wang et al 2019][research_wang_wan_2019]\] \[[Wang et al 2022][research_wang_bwb_airworthiness_2022]\] \[[Wang et al 2022][research_wang_tai_2022]\] \[[Wang et al 2023][research_wang_hu_2023]\] \[[Wang et al 2023][research_wang_zhou_2023]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Wang et al 2024][research_wang_zhang_2024]\] \[[Wang et al 2024][research_wang_zhao_2024]\] \[[Wang et al 2025][research_wang_rotating_wingtip_2025]\] \[[Wang et al 2025][research_wang_zhang_2025]\] \[[Wang et al 2026][research_wang_liu_2026]\] \[[Waters et al 2013][research_waters_voskuijl_2013]\] \[[Wells and Hess 2003][research_wells_hess_2003]\] \[[Westermayer et al 2010][research_westermayer_schirrer_2010]\] \[[Weyl 1944][research_weyl_1944]\] \[[Weyl 1945][research_weyl_1945]\] \[[Weyl 1945][research_weyl_1945_b]\] \[[Weyl 1945][research_weyl_1945_c]\] \[[Weyl 1945][research_weyl_1945_d]\] \[[Weyl 1945][research_weyl_1945_e]\] \[[Wienke et al 2023][research_wienke_bertsch_2023]\] \[[Wildschek 2014][research_wildschek_2014]\] \[[Williams et al 2025][research_williams_niestroy_2025]\] \[[Wong et al 2007][research_wong_moigne_2007]\] \[[Wu et al 2012][research_wu_chen_2012]\] \[[Xie et al 2010][research_xie_yang_2010]\] \[[Xie et al 2011][research_xie_yang_2011]\] \[[Xie et al 2026][research_xie_cai_2026]\] \[[Xin et al 2019][research_xin_blown_elevon_2019]\] \[[Xu and Feng 2025][research_xu_feng_2025]\] \[[Xu and Yu 2025][research_xu_yu_2025]\] \[[Xu and Zhou 2015][research_xu_zhou_2015]\] \[[Xu et al 2019][research_xu_xu_2019]\] \[[Yan and Shi 2024][research_yan_shi_2024]\] \[[Yang et al 2022][research_yang_zhong_2022]\] \[[Yerly et al 2016][research_yerly_deluca_2016]\] \[[Yi et al 2017][research_yi_dong_2017]\] \[[Yi Zhu et al 2016][research_yizhu_xinchen_2016]\] \[[Yingyang et al 2025][research_yingyang_peng_2025]\] \[[You 2026][research_you_2026]\] \[[Yu et al 2024][research_yu_tao_2024]\] \[[Yuan et al 2023][research_yuan_ma_2023]\] \[[Yuan et al 2024][research_yuan_ma_2024]\] \[[Yue et al 2009][research_yue_wang_2009]\] \[[Yue et al 2013][research_yue_wang_2013]\] \[[Yue et al 2013][research_yue_wang_2013_b]\] \[[Zhang and He 2026][research_zhang_he_2026]\] \[[Zhang and Jia 2013][research_zhang_jia_2013]\] \[[Zhang et al 2024][research_zhang_liu_2024]\] \[[Zhang and Zhao 2023][research_zhang_zhao_2023]\] \[[Zhang et al 2018][research_zhang_shuang_2018]\] \[[Zhang et al 2018][research_zhang_zhou_2018]\] \[[Zhang et al 2021][research_zhang_su_2021]\] \[[Zhang et al 2023][research_zhang_huang_2023]\] \[[Zhou et al 2022][research_zhou_dong_2022]\] \[[Zhu et al 2016][research_zhu_gao_2016]\] \[[Zięba et al 2026][research_zieba_rzucidlo_2026]\] \[[Zou et al 2022][research_zou_huang_2022]\]

### Handling qualities and flying qualities criteria

**How a damping ratio becomes a pilot's verdict.** Flight measurements of flying qualities, rating scales, specifications, equivalent systems and criteria. **The cluster begins with the NACA measurements of individual aircraft in the 1940s and moves to general criteria**, which is the transition from describing an aeroplane to specifying one that this article's use of later criteria depends on.

**398 records.** \[[A'Harrah and Lockenour 1971][research_aharrah_lockenour_1971]\] \[[Abu-Elola et al 2024][research_abuelola_alqaisia_2024]\] \[[Abzug and Larrabee][research_abzug_larrabee]\] \[[Abzug and Larrabee][research_abzug_larrabee_b]\] \[[Adams and Hatch 1970][research_adams_hatch_1970]\] \[[Adams and Hatch 1971][research_adams_hatch_1971]\] \[[Agenbag et al 2009][research_agenbag_theron_2009]\] \[[Aharrah and Lockenour 1969][research_aharrah_lockenour_1969]\] \[[Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]\] \[[Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_e]\] \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]\] \[[Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]\] \[[Aircraft longitudinal handling qualities 2011][research_aircraft_longitudinal_2011]\] \[[Al-Gilani et al 2009][research_algilani_abdunabi_2009]\] \[[Alberghini and Lee 2018][research_alberghini_lee_2018]\] \[[Anderson 1949][research_anderson_1949]\] \[[Anderson 1970][research_anderson_1970]\] \[[Anderson 1986][research_anderson_1986]\] \[[Anderson and Christofferson 1947][research_anderson_christofferson_1947]\] \[[Anderson and Cooper 1947][research_anderson_cooper_1947]\] \[[Andrianantara et al 2025][research_andrianantara_ghazi_2025]\] \[[Ashkenas 1965][research_ashkenas_1965]\] \[[Ashkenas 1965][research_ashkenas_1965_b]\] \[[Ashkenas 1965][research_ashkenas_1965_c]\] \[[Ashkenas 1969][research_ashkenas_1969]\] \[[Ashkenas 1971][research_ashkenas_1971]\] \[[Ashkenas 1982][research_ashkenas_1982]\] \[[Atmospheric disturbance models and 1981][research_atmospheric_disturbance_1981]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]\] \[[Bachelder et al 2023][research_bachelder_aponso_2023]\] \[[Bachelder et al 2023][research_bachelder_aponso_2023_b]\] \[[Bailey and Smith 1981][research_bailey_smith_1981]\] \[[Bailey et al 1987][research_bailey_knotts_1987]\] \[[Bailey et al 1988][research_bailey_powers_1988]\] \[[Balas and Hodgkinson 2009][research_balas_hodgkinson_2009]\] \[[Bar-Gill and Stengel 1983][research_bargill_stengel_1983]\] \[[Barber et al 1966][research_barber_haise_1966]\] \[[Barren et al][research_barren_larson]\] \[[Baughman and Longeauay 2015][research_baughman_longeauay_2015]\] \[[Berger et al 2012][research_berger_tischler_2012]\] \[[Berger et al 2013][research_berger_tischler_2013]\] \[[Berger et al 2025][research_berger_christensen_2025]\] \[[Berry 1981][research_berry_1981]\] \[[Berry 1982][research_berry_1982]\] \[[Berry 1986][research_berry_1986]\] \[[Berry and Powers 1970][research_berry_powers_1970]\] \[[Berry et al 1976][research_berry_mallick_1976]\] \[[Biezad and Bole 2001][research_biezad_bole_2001]\] \[[Bihrle 1969][research_bihrle_1969]\] \[[Bingaman 2012][research_bingaman_2012]\] \[[Bischoff 1983][research_bischoff_1983]\] \[[Bise and Black][research_bise_black]\] \[[Black 2009][research_black_2009]\] \[[Black and Moorhouse 1979][research_black_moorhouse_1979]\] \[[Black and Thomas][research_black_thomas]\] \[[Boothe et al 1974][research_boothe_chen_1974]\] \[[Booz 1988][research_booz_1988]\] \[[Botez and Rotaru 2007][research_botez_rotaru_2007]\] \[[Bowes and Miller 1976][research_bowes_miller_1976]\] \[[Brandon et al 1995][research_brandon_brown_1995]\] \[[Bray 1963][research_bray_1963]\] \[[Breneman and Lower 1992][research_breneman_lower_1992]\] \[[Breul et al 1985][research_breul_keller_1985]\] \[[Breul et al 1987][research_breul_keller_1987]\] \[[Brewer 1946][research_brewer_1946]\] \[[Brinker and Wise 1996][research_brinker_wise_1996]\] \[[Callaghan and Kunz 2019][research_callaghan_kunz_2019]\] \[[Callaghan and Kunz 2021][research_callaghan_kunz_2021]\] \[[Campos and Marques 2021][research_campos_marques_2021]\] \[[Capello et al 2011][research_capello_guglieri_2011]\] \[[Cathey 1979][research_cathey_1979]\] \[[Cavalcanti et al 2026][research_cavalcanti_2026]\] \[[Chalk 1963][research_chalk_1963]\] \[[Chalk 1964][research_chalk_1964]\] \[[Chalk 1986][research_chalk_1986]\] \[[Chalk and Wilson 1968][research_chalk_wilson_1968]\] \[[Chalk and Wilson 1969][research_chalk_wilson_1969]\] \[[Chalk et al 1969][research_chalk_neal_1969]\] \[[Chang et al 2009][research_chang_ye_2009]\] \[[Chen and Boothe 1974][research_chen_boothe_1974]\] \[[Chevalier and Burke 1972][research_chevalier_burke_1972]\] \[[Chiu][research_chiu]\] \[[Choe et al 2010][research_choe_xargay_2010]\] \[[Chowhan et al 2019][research_chowhan_arya_2019]\] \[[Configuration Development and Flying 2021][research_configuration_development_2021]\] \[[Cook 1997][research_cook_1997]\] \[[Cook 2007][research_cook_2007]\] \[[Cook 2013][research_cook_2013]\] \[[Cook and de Castro 2004][research_cook_decastro_2004]\] \[[Cord 1981][research_cord_1981]\] \[[Cord 1994][research_cord_1994]\] \[[Cotting 2010][research_cotting_2010]\] \[[Cotting et al 2008][research_cotting_cao_2008]\] \[[Cotting et al 2019][research_cotting_alt_2019]\] \[[Cox and Jackson 1997][research_cox_jackson_1997]\] \[[Cox and Jackson 1997][research_cox_jackson_1997_b]\] \[[Cox and Marshall 2000][research_cox_marshall_2000]\] \[[Crane and Sommer 1961][research_crane_sommer_1961]\] \[[Creer et al 1959][research_creer_1959]\] \[[Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]\] \[[Cromwell and Koven 1965][research_cromwell_koven_1965]\] \[[Crother et al 1973][research_crother_gabelman_1973]\] \[[Cárdenas et al 2009][research_cardenas_boschetti_2009]\] \[[Dander 1962][research_dander_1962]\] \[[Deodhare and Vidyasagar][research_deodhare_vidyasagar]\] \[[Didomenico and Biezad 1985][research_didomenico_biezad_1985]\] \[[Difranco 1969][research_difranco_1969]\] \[[Difranco 1970][research_difranco_1970]\] \[[Donaldson 1986][research_donaldson_1986]\] \[[Drewiacki et al 2016][research_drewiacki_silvestre_2016]\] \[[Drewiacki et al 2020][research_drewiacki_josesilvestre_2020]\] \[[Edwards et al 1997][research_edwards_fittante_1997]\] \[[Ehlers et al 2011][research_ehlers_niedermeier_2011]\] \[[Eney 1967][research_eney_1967]\] \[[Eney 1968][research_eney_1968]\] \[[Erturk and Dogan 2015][research_erturk_dogan_2015]\] \[[Evangelou 1998][research_evangelou_1998]\] \[[Faber 1958][research_faber_1958]\] \[[Field et al 2002][research_field_armor_2002]\] \[[Field et al 2004][research_field_rossitto_2004]\] \[[Fischel et al 1957][research_fischel_holleman_1957]\] \[[Flying Qualities 2003][research_flying_qualities_2003]\] \[[Flying Qualities and Flight 1998][research_flying_qualities_1998]\] \[[Flying Qualities Through Variable 2010][research_flying_qualities_2010]\] \[[Franklin 1970][research_franklin_1970]\] \[[Franklin 1971][research_franklin_1971]\] \[[Franklin 1971][research_franklin_1971_b]\] \[[Franklin 1972][research_franklin_1972]\] \[[Franklin and Miller 1967][research_franklin_miller_1967]\] \[[Fraser 1986][research_fraser_1986]\] \[[Fuller and Moorhouse 1982][research_fuller_moorhouse_1982]\] \[[Gao et al 2021][research_gao_an_2021_d]\] \[[Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]\] \[[Garris 1943][research_garris_1943]\] \[[Gautrey and Cook 1998][research_gautrey_cook_1998]\] \[[Gertsen and Shomber 1965][research_gertsen_shomber_1965]\] \[[Gibson 1990][research_gibson_1990]\] \[[Giles 1970][research_giles_1970]\] \[[Giles 1972][research_giles_1972]\] \[[Gillette et al 1993][research_gillette_page_1993]\] \[[Goetzendorf-Grabowski and Antoniewski 2016][research_goetzendorfgrabowski_antoniewski_2016]\] \[[Gonzalez and Bazile 2011][research_gonzalez_bazile_2011]\] \[[Grantham and Williams 1987][research_grantham_williams_1987]\] \[[Grantham et al 1976][research_grantham_nguyen_1976]\] \[[Gratton 2018][research_gratton_2018]\] \[[Gray 2009][research_gray_2009]\] \[[Gray and Kemper 2009][research_gray_kemper_2009]\] \[[Greene et al 2014][research_greene_kunz_2014]\] \[[Hall et al 1973][research_hall_weingarten_1973]\] \[[Hamidani and Kunz 2018][research_hamidani_kunz_2018]\] \[[Hammond et al 1984][research_hammond_downing_1984]\] \[[Handling qualities 2000][research_handling_qualities_2000]\] \[[Handling Qualities Analysis 2008][research_handling_qualities_2008]\] \[[Handling Qualities and Control 2017][research_handling_qualities_2017]\] \[[Harper and Cooper 1984][research_harper_cooper_1984]\] \[[Harper and Cooper 1986][research_harper_cooper_1986]\] \[[Harper and Robert P. 1955][research_harper_robertp_1955]\] \[[Harris 2000][research_harris_2000]\] \[[Harris and Black 1996][research_harris_black_1996]\] \[[Harris et al 2000][research_harris_gautrey_2000]\] \[[Hensley et al 1987][research_hensley_creighton_1987]\] \[[Hess 1981][research_hess_1981]\] \[[Hess 1984][research_hess_1984]\] \[[Hess 2009][research_hess_2009]\] \[[Hess 2016][research_hess_2016]\] \[[Hodgkinson 2005][research_hodgkinson_2005]\] \[[Hodgkinson et al 1982][research_hodgkinson_wood_1982]\] \[[Hodgkinson et al 1988][research_hodgkinson_skow_1988]\] \[[Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]\] \[[Hoh 1988][research_hoh_1988]\] \[[Hoh and Mitchell 2018][research_hoh_mitchell_2018]\] \[[Holleman and Gilyard 1972][research_holleman_gilyard_1972]\] \[[Hoover 1943][research_hoover_1943]\] \[[Howard et al 1996][research_howard_bray_1996]\] \[[Huff 1949][research_huff_ww_1949]\] \[[Humphreys-Jennings et al 2020][research_humphreys_2020]\] \[[Humphreys-Jennings et al 2019][research_humphreysjennings_lappas_2019]\] \[[Hunter 1948][research_hunter_1948]\] \[[Huo et al 2006][research_huo_ioannou_2006]\] \[[Integrated Application of Active 1983][research_integrated_application_1983]\] \[[Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]\] \[[Ionita 1996][research_ionita_1996]\] \[[Jackson and Snyder 1966][research_jackson_snyder_1966]\] \[[Jackson et al 1993][research_jackson_rivers_1993]\] \[[Jansen 1980][research_jansen_1980]\] \[[Jansen and Van Kampen 2025][research_jansen_vankampen_2025]\] \[[Ji et al 2021][research_ji_kim_2021]\] \[[jingwei and jiaming 2020][research_jingwei_jiaming_2020]\] \[[Funk et al 1993][research_johndfunk_corinpbeck_1993]\] \[[Johnson 1946][research_johnson_p63_1946]\] \[[Johnston et al 1974][research_johnston_ashkenas_1974]\] \[[Jones et al 2023][research_jones_klyde_2023]\] \[[Joshi and Rickard 1981][research_joshi_rickard_1981]\] \[[Junfeng et al 2020][research_junfeng_wuzhou_2020]\] \[[Kahveci and Ioannou 2010][research_kahveci_ioannou_2010]\] \[[Wichman et al 1996][research_keithdwichman_josephwpahle_1996]\] \[[Kempel et al 1975][research_kempel_dana_1975]\] \[[Kendall 2018][research_kendall_2018]\] \[[Kidd and Bull 1963][research_kidd_bull_1963]\] \[[Kim and Kunz 2016][research_kim_kunz_2016]\] \[[Klyde et al 2007][research_klyde_bachelder_2007]\] \[[Klyde et al 2020][research_klyde_schulze_2020_b]\] \[[Kraft et al 1948][research_kraft_goranson_1948]\] \[[Kraft et al 1953][research_kraft_1953]\] \[[Krekeler et al 1990][research_krekeler_wilson_1990]\] \[[Kun et al 2011][research_kun_lixin_2011]\] \[[Larrabee and Tymczyszyn 1968][research_larrabee_tymczyszyn_1968]\] \[[Lee et al 2001][research_lee_tischler_2001]\] \[[Leggett and Cord 1994][research_leggett_cord_1994]\] \[[Lesiário and Hagström 2010][research_lesiario_hagstrom_2010]\] \[[Levison and Rickard 1981][research_levison_rickard_1981]\] \[[Liddell et al 1947][research_liddell_1947]\] \[[Loranchet et al 2025][research_loranchet_tiako_2025]\] \[[Lusardi et al 2012][research_lusardi_blanken_2012]\] \[[Macdonald 1984][research_macdonald_1984]\] \[[Malaek and Karimi 2008][research_malaek_karimi_2008]\] \[[Malcom 1969][research_malcom_1969]\] \[[Malpica and Lusardi 2013][research_malpica_lusardi_2013]\] \[[Manning and Gleason 1992][research_manning_gleason_1992]\] \[[Mansor et al 2015][research_mansor_nogoud_2015]\] \[[Martin 2007][research_martin_2007]\] \[[Martz et al 1987][research_martz_biezad_1987]\] \[[Martz et al 1988][research_martz_biezad_1988]\] \[[McCarley and Lindak 2016][research_mccarley_lindak_2016]\] \[[McFarlane et al 2008][research_mcfarlane_richardson_2008]\] \[[Meyer 1983][research_meyer_1983]\] \[[Meyer and Husband 1990][research_meyer_husband_1990]\] \[[Miller 1969][research_miller_1969]\] \[[Miller 1970][research_miller_1970]\] \[[Miller and Franklin 1968][research_miller_franklin_1968]\] \[[Mitcham 1949][research_mitcham_1949]\] \[[Mitcham and Blanchard 1950][research_mitcham_blanchard_1950]\] \[[Mitchell and Hoh 1982][research_mitchell_hoh_1982]\] \[[Mitchell and Hoh 1984][research_mitchell_hoh_1984]\] \[[Mitchell et al 1995][research_mitchell_aponso_1995]\] \[[Mitchell et al 2003][research_mitchell_doman_2003]\] \[[Moennich and Dalldorff 1993][research_moennich_dalldorff_1993]\] \[[Montgomery 1971][research_montgomery_1971]\] \[[Mooij 1985][research_mooij_1985]\] \[[Mooij 1985][research_mooij_1985_b]\] \[[Mooij 1985][research_mooij_1985_d]\] \[[Moorhouse 1979][research_moorhouse_1979]\] \[[Moorhouse 1990][research_moorhouse_1990]\] \[[Moorhouse 1995][research_moorhouse_1995]\] \[[Morris et al 2013][research_morris_sultan_2013]\] \[[Moulton et al 2024][research_moulton_abraham_2024]\] \[[Mudd 1969][research_mudd_1969]\] \[[Mullins et al 1996][research_mullins_tipton_1996]\] \[[Myers et al 1982][research_myers_mcruer_1982]\] \[[Myers et al 1983][research_myers_johnston_1983]\] \[[Saltzman 1955][research_x4_blunt_elevons_1955]\] \[[Mitcham et al 1956][research_tailless_triangular_1956]\] \[[Nardi et al 1976][research_nardi_kawana_1976]\] \[[White and Innis 1959][research_tailless_delta_lowspeed_1959]\] \[[Faber and Crane 1961][research_feel_system_1961]\] \[[Donlan and Kuhn 1976][research_tailless_transonic_est_1976]\] \[[Nasir et al 2014][research_nasir_kuntjoro_2014]\] \[[Neal and Smith 1970][research_neal_smith_1970]\] \[[Neal and Smith 1971][research_neal_smith_1971]\] \[[Neighbor and Wiler 1978][research_neighbor_wiler_1978]\] \[[Newton 2025][research_newton_2025]\] \[[Nicolosi et al 2010][research_nicolosi_demarco_2010]\] \[[Nicolosi et al 2013][research_nicolosi_demarco_2013]\] \[[Nie et al 2020][research_nie_liu_2020]\] \[[Ohara 1964][research_ohara_1964]\] \[[Oliva 2000][research_oliva_2000]\] \[[Page and Gillette 1994][research_page_gillette_1994]\] \[[Pahle et al 1996][research_pahle_wichman_1996]\] \[[Papa and Stoliker 1988][research_papa_stoliker_1988]\] \[[Peahl et al 1986][research_peahl_kolkailah_1986]\] \[[Peters et al 1997][research_peters_andrisani_1997]\] \[[Peterson and Grant 2011][research_peterson_grant_2011]\] \[[Phillips 1942][research_phillips_1942]\] \[[Phillips 1988][research_phillips_1988]\] \[[Phillips 1989][research_phillips_1989]\] \[[Phillips and Crane 1943][research_phillips_crane_1943]\] \[[Phillips et al 1944][research_phillips_williams_1944]\] \[[Place et al 1974][research_place_altmann_1974]\] \[[Potvin and Grant 2026][research_potvin_grant_2026]\] \[[Powers 1968][research_powers_1968]\] \[[Powers 1972][research_powers_1972]\] \[[Powers 1986][research_powers_1986]\] \[[Pujara 1988][research_pujara_1988]\] \[[Quinn and Cutchins 1984][research_quinn_cutchins_1984]\] \[[Raffel et al 2021][research_raffel_wienke_2021]\] \[[Reeder 1944][research_reeder_1944]\] \[[Reeder 1945][research_reeder_1945]\] \[[Reeder 1945][research_reeder_1945_b]\] \[[Reeder 1945][research_reeder_1945_c]\] \[[Rhoads 1967][research_rhoads_1967]\] \[[Richards et al 2014][research_richards_adams_2014]\] \[[Rickard and Levison 1981][research_rickard_levison_1981]\] \[[Riley and Drajeske 1991][research_riley_drajeske_1991]\] \[[Risse et al 2010][research_risse_anton_2010]\] \[[Rodchenko et al 2003][research_rodchenko_zaichik_2003]\] \[[Rogalski and Dołęga 2006][research_rogalski_dolega_2006]\] \[[Rohling 1968][research_rohling_1968]\] \[[Rohling 1969][research_rohling_1969]\] \[[Rossitto and Hodgkinson 1993][research_rossitto_hodgkinson_1993]\] \[[Rowan and Dogan 2023][research_rowan_dogan_2023]\] \[[Rynaski 1985][research_rynaski_1985]\] \[[Rynaski 1994][research_rynaski_1994]\] \[[Rynaski et al 1986][research_rynaski_weingarten_1986]\] \[[Ryu and Andrisani 2000][research_ryu_andrisani_2000]\] \[[Ryu and Andrisani 2000][research_ryu_andrisani_2000_b]\] \[[Ryu and Andrisani 2003][research_ryu_andrisani_2003]\] \[[Sachs 1990][research_sachs_1990]\] \[[Sachs 1999][research_sachs_1999]\] \[[Sachs et al 1994][research_sachs_knoll_1994]\] \[[Sadoff 1958][research_sadoff_1958]\] \[[Sammonds and Bunnell 1980][research_sammonds_bunnell_1980]\] \[[Sammonds and Bunnell 1981][research_sammonds_bunnell_1981]\] \[[Sanghi et al 2025][research_sanghi_riso_2025]\] \[[Saporito et al 2021][research_saporito_daronch_2021]\] \[[Sarrafian and Powers 1985][research_sarrafian_powers_1985]\] \[[Sarrafian and Powers 1988][research_sarrafian_powers_1988]\] \[[Saucez][research_saucez]\] \[[Schuck et al 2013][research_schuck_heller_2013]\] \[[Schuler 1983][research_schuler_1983]\] \[[Schy 1972][research_schy_1972]\] \[[Shafer et al 1989][research_shafer_koehler_1989]\] \[[Shevchuk 2014][research_shevchuk_2014]\] \[[Shibata et al 1987][research_shibata_nakao_1987]\] \[[Shomber and Gertsen 1967][research_shomber_gertsen_1967]\] \[[Siqueira et al 2007][research_siqueira_moreira_2007]\] \[[Sisk and Mataeny 1980][research_sisk_mataeny_1980]\] \[[Sisk and Matheny 1979][research_sisk_matheny_1979]\] \[[Sissingh 2015][research_sissingh_2015]\] \[[Sliwa 1980][research_sliwa_1980]\] \[[Smetana et al 1972][research_smetana_summery_1972]\] \[[Smith 1977][research_smith_1977]\] \[[Smith 1986][research_smith_1986]\] \[[Smith and Geddes 1979][research_smith_geddes_1979]\] \[[Solies 1994][research_solies_1994_c]\] \[[Soule 1940][research_soule_1940]\] \[[Steer 2003][research_steer_2003]\] \[[Stengel 1981][research_stengel_1981]\] \[[Stengel 1983][research_stengel_1983]\] \[[Stengel 1985][research_stengel_1985]\] \[[Stengel and Miller 1978][research_stengel_miller_1978]\] \[[Sternfield and Gates 1949][research_sternfield_gates_1949]\] \[[Stone and Naylor 1972][research_stone_naylor_1972]\] \[[Suchomel 1987][research_suchomel_1987]\] \[[Sudderth and McNeill 1976][research_sudderth_mcneill_1976]\] \[[Sudderth et al 1975][research_sudderth_bohn_1975]\] \[[Suikat et al 1987][research_suikat_donaldson_1987]\] \[[Suikat et al 1989][research_suikat_donaldson_1989]\] \[[Sun et al 2020][research_sun_shi_2020]\] \[[Swaim 1978][research_swaim_1978]\] \[[Taylor et al 1965][research_taylor_robinson_1965]\] \[[Teofilatto 2001][research_teofilatto_2001]\] \[[The effects of sustained 1977][research_the_effects_1977]\] \[[Theodore et al 2014][research_theodore_malpica_2014]\] \[[Tokutake and Itoh][research_tokutake_itoh]\] \[[Tokutake et al 2003][research_tokutake_sato_2003]\] \[[Tomczyk 2008][research_tomczyk_2008]\] \[[Tseng et al 2006][research_tseng_gupta_2006]\] \[[Turner and Cooper 1947][research_turner_cooper_1947]\] \[[Umm-e-Aymon et al 2016][research_ummeaymon_shah_2016]\] \[[Uybarreta et al 2025][research_uybarreta_grant_2025]\] \[[Vensel 1942][research_vensel_1942]\] \[[Wahler et al 2023][research_wahler_varriale_2023]\] \[[Walsh 1992][research_walsh_1992]\] \[[Walsh 1993][research_walsh_1993]\] \[[Wang et al 2017][research_wang_guo_2017]\] \[[Wang et al 2021][research_wang_criteria_2021]\] \[[Wang et al 2024][research_wang_tvsas_2024]\] \[[Wanner 1973][research_wanner_1973]\] \[[Warner and Onstott 1986][research_warner_onstott_1986]\] \[[Wasicko 1972][research_wasicko_1972]\] \[[Wei 1985][research_wei_1985]\] \[[Weil and Spear 1947][research_weil_spear_1947]\] \[[Weingarten and Chalk 1982][research_weingarten_chalk_1982]\] \[[Weingarten and Chalk 1984][research_weingarten_chalk_1984]\] \[[Wendel 1987][research_wendel_1987]\] \[[Westbrook 1965][research_westbrook_1965]\] \[[Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Wilson et al 1990][research_wilson_buckley_1990]\] \[[Wilson et al 1991][research_wilson_hall_1991]\] \[[Wilson et al 1993][research_wilson_riley_1993]\] \[[Wilson et al 1994][research_wilson_citurs_1994]\] \[[Wolowicz and Yancey 1973][research_wolowicz_yancey_1973]\] \[[Wood 1984][research_wood_1984]\] \[[Woodcock and Browne 1986][research_woodcock_browne_1986]\] \[[Woodcock and George 1976][research_woodcock_george_1976]\] \[[Sisk et al 1965][research_xb70_review_1965]\] \[[Zhang et al 2012][research_zhang_li_2012]\]

### Control effectors, elevons, drag rudders and allocation

**The surfaces a tailless aircraft has instead of a tail.** Ailerons, elevons, spoilers, split drag rudders, hinge moments, control reversal, circulation and fluidic control, and the allocation of redundant effectors.

**321 records.** \[[Abdulrahim 2004][research_abdulrahim_2004]\] \[[Addington and Myatt 2000][research_addington_myatt_2000]\] \[[Ajaj and Djidjeli 2022][research_ajaj_djidjeli_2022]\] \[[Al Aian et al 2014][research_alaian_basuno_2014]\] \[[Alighanbari 2002][research_alighanbari_2002]\] \[[Allen 1976][research_allen_1976]\] \[[Allen and Tuttle 1973][research_allen_tuttle_1973]\] \[[Altman 1952][research_altman_1952]\] \[[Alwi and Edwards 2009][research_alwi_edwards_2009]\] \[[Amendola et al 2018][research_amendola_dimino_2018]\] \[[An analysis of gap 1981][research_an_analysis_1981]\] \[[Andersen et al 1997][research_andersen_kolonay_1997]\] \[[Andersen et al 1998][research_andersen_kolonay_1998]\] \[[Andersen et al 1998][research_andersen_kolonay_1998_b]\] \[[Anglin and Byrdsong 1982][research_anglin_byrdsong_1982]\] \[[Ansell et al 2011][research_ansell_bragg_2011]\] \[[Arnold 1942][research_arnold_1942]\] \[[Atesoglu and Ozgoren 2011][research_atesoglu_ozgoren_2011]\] \[[Atesoglu and Özgören 2006][research_atesoglu_ozgoren_2006]\] \[[Atkinson 2016][research_atkinson_2016]\] \[[Axelson 1947][research_axelson_1947]\] \[[Ayele et al 2023][research_ayele_maldonado_2023]\] \[[Ba Zuhair 2019][research_bazuhair_2019]\] \[[Baggi et al 2020][research_baggi_franco_2020]\] \[[Baggi et al 2022][research_baggi_serrani_2022]\] \[[Ball 1978][research_ball_1978]\] \[[Ball 1979][research_ball_1979]\] \[[Bandettini 1952][research_bandettini_1952]\] \[[Bartlett 1975][research_bartlett_1975]\] \[[Bartlett and Sangiorgio 1975][research_bartlett_sangiorgio_1975]\] \[[Bazuhair 2018][research_bazuhair_2018]\] \[[Berthold 1977][research_berthold_1977]\] \[[Bharadvaj 1990][research_bharadvaj_1990]\] \[[Bharadvaj 1991][research_bharadvaj_1991]\] \[[Bian et al 2018][research_bian_nener_2018]\] \[[Bogatyrev 2017][research_bogatyrev_2017]\] \[[Boothe 1971][research_boothe_1971]\] \[[Boskovic et al][research_boskovic_ling]\] \[[Brandt et al 2022][research_brandt_mcfadden_2022]\] \[[Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]\] \[[Brincklow et al 2021][research_brincklow_montgomery_2021]\] \[[Brincklow et al 2024][research_brincklow_montgomery_2024]\] \[[Bronz et al 2019][research_bronz_aydin_2019]\] \[[Bruno Santos et al 2020][research_brunosantos_oliveira_2020]\] \[[Butler and Bons 2025][research_butler_bons_2025]\] \[[Cao and Lyu 2024][research_cao_lyu_2024]\] \[[Cao et al 2025][research_cao_lin_2025]\] \[[Capello et al 2019][research_capello_ferrero_2019]\] \[[Capone and Mason 1986][research_capone_mason_1986]\] \[[Chen et al 2025][research_chen_zhang_2025]\] \[[Chevalier 1982][research_chevalier_1982]\] \[[Chin 1992][research_chin_1992]\] \[[Chin and Lentink 2019][research_chin_lentink_2019]\] \[[Chng and Tsai 2008][research_chng_tsai_2008]\] \[[Christophersen and Spahr 1944][research_christophersen_spahr_1944]\] \[[Church 1954][research_church_1954]\] \[[Claudia Alice 2010][research_claudiaalice_2010]\] \[[Clevenson and Thompson 1957][research_clevenson_thompson_1957]\] \[[Cole 1990][research_cole_1990]\] \[[Coletti and Faruque 2022][research_coletti_faruque_2022]\] \[[Consigny et al 1983][research_consigny_gravelle_1983]\] \[[Costes 1988][research_costes_1988]\] \[[Crandall and Swanson 1944][research_crandall_swanson_1944]\] \[[Croom and Huffman 1957][research_croom_huffman_1957]\] \[[Cruz and Ware 1995][research_cruz_ware_1995]\] \[[Cunningham 1972][research_cunningham_1972]\] \[[de Melo et al 2024][research_demelo_bussamra_2024]\] \[[de Vries and Van Kampen 2019][research_devries_vankampen_2019]\] \[[Deere 2003][research_deere_2003]\] \[[Denieul][research_denieul]\] \[[Design of Control Surfaces 2012][research_design_of_2012]\] \[[Deters and Russell 1947][research_deters_russell_1947]\] \[[Doman and Oppenheimer 2002][research_doman_oppenheimer_2002]\] \[[Dong et al 2025][research_dong_zhou_2025]\] \[[Dong et al 2016][research_dong_lu_2016]\] \[[Dowell and Assael 2025][research_dowell_assael_2025]\] \[[Drake and McKay 1953][research_drake_mckay_1953]\] \[[Duffy 1989][research_duffy_1989]\] \[[Duncan 1950][research_duncan_1950]\] \[[Durham et al 2016][research_durham_bordignon_2016]\] \[[Dvorak and Choi 1983][research_dvorak_choi_1983]\] \[[Eastep et al 1998][research_eastep_andersen_1998]\] \[[Eastep et al 2001][research_eastep_andersen_2001]\] \[[Englar 1970][research_englar_1970]\] \[[Englar 1996][research_englar_1996]\] \[[English 1954][research_english_1954]\] \[[Fairbanks 1927][research_fairbanks_1927]\] \[[Fields 1952][research_fields_1952]\] \[[Filzek 1949][research_filzek_1949]\] \[[Forster and Steijl 2015][research_forster_steijl_2015]\] \[[Forster et al 2016][research_forster_biava_2016]\] \[[Foster et al 1993][research_foster_ross_1993]\] \[[Franze et al 2013][research_franze_mattei_2013]\] \[[Fu et al 2009][research_fu_kirtikar_2009]\] \[[Furey 1980][research_furey_1980]\] \[[Gal-Or 1992][research_galor_1992]\] \[[Gardner and Curfman 1947][research_gardner_curfman_1947]\] \[[Garmendia and Mavris 2014][research_garmendia_mavris_2014]\] \[[Garmendia and Mavris 2016][research_garmendia_mavris_2016]\] \[[Ghalandari et al 2022][research_ghalandari_2022]\] \[[Giannelis et al 2019][research_giannelis_murray_2019]\] \[[Gibson et al 1957][research_gibson_igoe_1957]\] \[[Gibson et al 1958][research_gibson_herr_1958]\] \[[Goland 1952][research_goland_1952]\] \[[Gopinath 1982][research_gopinath_1982]\] \[[Granasy 1995][research_granasy_1995]\] \[[Green and Fernandez 1994][research_green_fernandez_1994]\] \[[Greer et al 2021][research_greer_sardahi_2021]\] \[[Grismer et al 2000][research_grismer_kinsey_2000]\] \[[Gross et al 1986][research_gross_chandler_1986]\] \[[Grosser 1965][research_grosser_1965]\] \[[Guo et al 2026][research_guo_split_rudder_2026]\] \[[Guruswamy and Tu 1989][research_guruswamy_tu_1989]\] \[[Haas and Chopra 1988][research_haas_chopra_1988]\] \[[Haas and Chopra 1990][research_haas_chopra_1990]\] \[[Hansen et al 2022][research_hansen_duan_2022]\] \[[Haoyun Fu et al 2009][research_haoyunfu_jinyan_2009]\] \[[Harkegard][research_harkegard]\] \[[He et al 2016][research_he_yang_2016]\] \[[He et al 2018][research_he_leprovost_2018]\] \[[He et al 2020][research_he_song_2020]\] \[[He et al 2021][research_he_wang_2021]\] \[[Henderson and Lavretsky 1999][research_henderson_lavretsky_1999]\] \[[Hooker 2023][research_hooker_2023]\] \[[Hopkins and Lovette 1977][research_hopkins_lovette_1977]\] \[[Huehne et al 2013][research_huehne_mahmood_2013]\] \[[Hughes and Mennell 1974][research_hughes_mennell_1974]\] \[[Hunn 1953][research_hunn_1953]\] \[[Hwang et al 1991][research_hwang_chen_1991]\] \[[Ijaz et al 2019][research_ijaz_hamayun_2019]\] \[[Invernizzi and Lovera 2018][research_invernizzi_lovera_2018]\] \[[Irfan et al 2026][research_irfan_nanangburhan_2026]\] \[[Pratheepan and Bruce Ralphin Rose 2015][research_j_j_2015]\] \[[Jabbar et al 2026][research_jabbar_setiawan_2026]\] \[[Jacobs 1983][research_jacobs_1983]\] \[[Jacobsen 2006][research_jacobsen_2006]\] \[[Jategaonkar et al 1997][research_jategaonkar_monnich_1997]\] \[[Jiang 1999][research_jiang_1999]\] \[[Jiang et al 2000][research_jiang_an_2000]\] \[[Jianjun Ma et al 2008][research_jianjunma_pengli_2008]\] \[[Jingping et al 2011][research_jingping_weiguo_2011]\] \[[Jones and Cohen 1976][research_jones_cohen_1976]\] \[[Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]\] \[[Kazarin et al 2017][research_kazarin_mackunis_2017]\] \[[Keener et al 1958][research_keener_mcleod_1958]\] \[[Kehlet 1957][research_kehlet_1957]\] \[[Khan et al 2012][research_khan_weiguo_2012]\] \[[Khot et al 1997][research_khot_eastep_1997]\] \[[Kim and Song 2013][research_kim_song_2013]\] \[[Koreanschi et al 2014][research_koreanschi_oliviu_2014]\] \[[Koreanschi et al 2016][research_koreanschi_oliviu_2016]\] \[[Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]\] \[[Kumar et al 2021][research_kumar_sunil_2021]\] \[[Lai et al 2014][research_lai_zhang_2014]\] \[[Lateral Control Power Rolling 2003][research_lateral_control_2003]\] \[[Lauchle 1974][research_lauchle_1974]\] \[[Lei and Zha 2023][research_lei_zha_2023]\] \[[Lesoinne 2007][research_lesoinne_2007]\] \[[Levy 1992][research_levy_1992]\] \[[Li and Ma 2014][research_li_ma_2014]\] \[[Li et al 1999][research_li_zhu_1999]\] \[[Li et al 2011][research_li_yu_2011]\] \[[Li et al 2012][research_li_yu_2012]\] \[[Li et al 2022][research_li_split_rudder_2022]\] \[[Li et al 2025][research_li_dai_2025]\] \[[Li et al 2025][research_li_wang_2025]\] \[[Lin et al 2019][research_lin_zhang_2019]\] \[[Lindsay 2021][research_lindsay_2021]\] \[[Lingyu et al 2006][research_lingyu_youwu_2006]\] \[[Liu et al 2023][research_liu_zhang_2023]\] \[[Lu et al 2026][research_lu_lan_2026]\] \[[Maughmer et al 1990][research_maughmer_ozoroski_1990]\] \[[McFall and Hollinger 1953][research_mcfall_hollinger_1953]\] \[[Mennell 1976][research_mennell_1976]\] \[[Menshchikov and Somov 2019][research_menshchikov_somov_2019]\] \[[Merceruio][research_merceruio]\] \[[Mertins et al 2005][research_mertins_elsholz_2005]\] \[[Miklosovic and Perry 2014][research_miklosovic_perry_2014]\] \[[Miklosovic et al 2012][research_miklosovic_imber_2012]\] \[[Miller 1983][research_miller_1983]\] \[[Mitikiri and Mohseni 2018][research_mitikiri_mohseni_2018]\] \[[Mohamed et al 2021][research_mohamed_abdelhady_2021]\] \[[Molland and Turnock 2007][research_molland_turnock_2007]\] \[[Molland and Turnock 2022][research_molland_turnock_2022]\] \[[Moseley and Taylor 1954][research_moseley_taylor_1954]\] \[[Moseley and Thompson 1957][research_moseley_thompson_1957]\] \[[Moulin and Karpel 2007][research_moulin_karpel_2007]\] \[[Muchamad Bayu Sakti Pratama et al 2022][research_muchamadbayusaktipratama_erwinsulaeman_2022]\] \[[Mungall 1946][research_mungall_1946]\] \[[Transonic control effectiveness for 1977][research_elevon_transonic_1977]\] \[[Nelson and Durham 2002][research_nelson_durham_2002]\] \[[Nurohman et al 2018][research_nurohman_arifianto_2018]\] \[[O'Donnell and Mohseni 2017][research_odonnell_mohseni_2017]\] \[[O'Donnell and Mohseni 2019][research_odonnell_mohseni_2019]\] \[[Obayashi and Guruswamy 1994][research_obayashi_guruswamy_1994]\] \[[Oggioni et al 2026][research_oggioni_riboldi_2026]\] \[[Olcott et al 1981][research_olcott_sackel_1981]\] \[[Olson and Mead 1950][research_olson_mead_1950]\] \[[Olson and Mead 1951][research_olson_mead_1951]\] \[[Pabla 2021][research_pabla_2021]\] \[[Park and Chung 2012][research_park_chung_2012]\] \[[Park and Rokhsaz 2003][research_park_rokhsaz_2003]\] \[[Parker et al 1991][research_parker_spain_1991]\] \[[Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]\] \[[Pearson and Aiken 1944][research_pearson_aiken_1944]\] \[[Pedreiro et al 1998][research_pedreiro_takahara_1998]\] \[[Pedreiro et al 1999][research_pedreiro_takahara_1999]\] \[[Perry 1978][research_perry_1978]\] \[[Perry and Miklosovic 2012][research_perry_miklosovic_2012]\] \[[Persoon et al 1980][research_persoon_roos_1980]\] \[[Petrocchi and Barakos 2023][research_petrocchi_barakos_2023_b]\] \[[Pettit and Grandhi 2003][research_pettit_grandhi_2003]\] \[[Pfnür et al 2018][research_pfnur_oppelt_2018]\] \[[Phillips 1942][research_phillips_1942_b]\] \[[Polonsky 2026][research_polonsky_2026]\] \[[Prudente and Cavalieri 2007][research_prudente_cavalieri_2007]\] \[[Purser and Turner 1941][research_purser_turner_1941]\] \[[Purwadi et al 2023][research_purwadi_hidayat_2023]\] \[[Pushtaev 1989][research_pushtaev_1989]\] \[[Qin et al 2023][research_qin_wei_2023]\] \[[Qiu and Ang 2019][research_qiu_ang_2019]\] \[[Re 1974][research_re_1974]\] \[[2017][research_rea_pecora_2017]\] \[[Rea et al 2018][research_rea_pecora_2018]\] \[[Reynolds and Smith 1948][research_reynolds_smith_1948]\] \[[Rosenberg 1944][research_rosenberg_1944]\] \[[Rosenow et al 2022][research_rosenow_sachwitz_2022]\] \[[Saghafi and Banazadeh 2006][research_saghafi_banazadeh_2006]\] \[[Sahyoun et al 2026][research_sahyoun_boose_2026]\] \[[Sandahl 1948][research_sandahl_1948]\] \[[Sandahl 1948][research_sandahl_delta_1948]\] \[[Sandahl 1948][research_sandahl_swept_1948]\] \[[Sandahl and Strass 1950][research_sandahl_strass_1950_b]\] \[[Sandahl et al 1949][research_sandahl_bland_1949]\] \[[Sandahl et al 1950][research_sandahl_strass_1950]\] \[[Sanders et al 2003][research_sanders_eastep_2003]\] \[[Sandlin and Swanson 1990][research_sandlin_swanson_1990]\] \[[Sanghi et al 2020][research_sanghi_riso_2020]\] \[[Scalera and Durham 1999][research_scalera_durham_1999]\] \[[Schult 1954][research_schult_1954]\] \[[Schult and Fields 1952][research_schult_fields_1952]\] \[[Schult and Fields 1954][research_schult_fields_1954]\] \[[Schütte et al 2018][research_schutte_huber_2018]\] \[[Scordamaglia et al 2025][research_scordamaglia_mattei_2025]\] \[[Sebastia and Hornung 2023][research_sebastia_hornung_2023]\] \[[Sebastia et al 2024][research_sebastia_wurz_2024]\] \[[Seidel et al 1985][research_seidel_sandford_1985]\] \[[Shao et al 2026][research_shao_he_2026]\] \[[Shmilovich et al 2023][research_shmilovich_yadlin_2023]\] \[[Shmilovich et al 2026][research_shmilovich_yadlin_2026]\] \[[Sieradzki 2016][research_sieradzki_2016]\] \[[Simbuerger et al 2022][research_simbuerger_raveh_2022]\] \[[Singh et al 2014][research_singh_mcdonough_2014]\] \[[Singh et al 2016][research_singh_brown_2016]\] \[[Soinne 1999][research_soinne_1999]\] \[[Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]\] \[[Stam and de Visser 2025][research_stam_devisser_2025]\] \[[Stanford 2016][research_stanford_2016]\] \[[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014]\] \[[Steer 2000][research_steer_2000]\] \[[Steger and Bailey 1979][research_steger_bailey_1979]\] \[[Strass 1948][research_strass_1948]\] \[[Strass 1954][research_strass_1954]\] \[[Strass and Tucker 1954][research_strass_tucker_1954]\] \[[Strass et al 1951][research_strass_fields_1951]\] \[[Strass et al 1952][research_strass_fields_1952]\] \[[Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]\] \[[Suleman et al 2000][research_suleman_crawford_2000]\] \[[Suleman et al 2002][research_suleman_crawford_2002]\] \[[Sun et al 2021][research_sun_zhou_2021]\] \[[Tamayama et al 2003][research_tamayama_kheirandish_2003]\] \[[Tang 1971][research_tang_1971]\] \[[Tang and Pearson 1971][research_tang_pearson_1971]\] \[[Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]\] \[[Tanveer and Ahmad 2023][research_tanveer_ahmad_2023_b]\] \[[Taraborrelli 2023][research_taraborrelli_2023]\] \[[Tewes and Taubert 2015][research_tewes_taubert_2015]\] \[[Harris 1935][research_thomasaharris_1935]\] \[[Thompson and Moseley 1956][research_thompson_moseley_1956]\] \[[Thomson 1946][research_thomson_1946]\] \[[Tian et al 2017][research_tian_feng_2017]\] \[[Tleulinov and Jafarzade 2019][research_tleulinov_jafarzade_2019]\] \[[Trailing Edge Circulation Control 2006][research_trailing_edge_2006]\] \[[Underwood 1942][research_underwood_1942]\] \[[Vincent and Botez 2015][research_vincent_botez_2015]\] \[[Vindigni 2024][research_vindigni_2024]\] \[[Vindigni et al 2024][research_vindigni_mantegna_2024]\] \[[Vindigni et al 2024][research_vindigni_mantegna_2024_b]\] \[[Walchli and Langan 1999][research_walchli_langan_1999]\] \[[Walker 1940][research_walker_1940]\] \[[Wang et al 2018][research_wang_zhang_2018]\] \[[Wang et al 2021][research_wang_hou_2021]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Warsop et al 2019][research_warsop_crowther_2019]\] \[[Weick and Harris 1934][research_weick_harris_1934]\] \[[Weick and Wenzinger 1932][research_weick_wenzinger_1932]\] \[[Weisshaar 1977][research_weisshaar_1977]\] \[[Wetmore 1939][research_wetmore_1939]\] \[[Xiang and Wang 2026][research_xiang_wang_2026]\] \[[Xie et al 2019][research_xie_zhao_2019]\] \[[Xu and Qiu 2011][research_xu_qiu_2011]\] \[[Xu and Zha 2019][research_xu_zha_2019]\] \[[Xu and Zha 2021][research_xu_zha_2021]\] \[[Xue et al 2021][research_xue_yunsong_2021]\] \[[Yang and Chao 1996][research_yang_chao_1996]\] \[[Yang and Shen 2007][research_yang_shen_2007]\] \[[Yang et al 2009][research_yang_zhong_2009]\] \[[Yang et al 2010][research_yang_fan_2010]\] \[[Yates and Schneiter 1946][research_yates_schneiter_1946]\] \[[Yiming et al 2019][research_yiming_mei_2019]\] \[[Zeiler 1998][research_zeiler_1998]\] \[[Zhang and Ye 2010][research_zhang_ye_2010]\] \[[Zhang and Zhang 2013][research_zhang_zhang_2013]\] \[[Zhang et al 2013][research_zhang_yu_2013]\] \[[Zhang et al 2018][research_zhang_xu_2018]\] \[[Zhang et al 2024][research_zhang_zhao_2024]\] \[[Zhang et al 2025][research_zhang_xiang_2025]\] \[[Zheng-hong 1992][research_zhenghong_1992]\] \[[Zhong et al 2025][research_zhong_xia_2025]\] \[[Zhu et al 2026][research_zhu_yang_2026]\] \[[Zolghadri et al 2016][research_zolghadri_leberre_2016]\]

### Lateral-directional stability and the fin

**The axis the X-4 kept a surface for.** Directional stability and vertical tail sizing, the Dutch roll, sideslip, inertia coupling and vertical tail buffet. Vertical tail buffet on twin-tailed fighters is a distinct thread from the 1990s on.

**258 records.** \[[R.Yass et al 2009][research_aryass_hfarhood_2009]\] \[[Abramov et al 2005][research_abramov_goman_2005]\] \[[Addendum 3 Lateral Control 2000][research_addendum_3_2000]\] \[[Ahmed and Worley 2008][research_ahmed_worley_2008]\] \[[Appendix G Development of 2003][research_appendix_g_2003]\] \[[Arabian and Schmeer 1955][research_arabian_schmeer_1955]\] \[[Arik et al 2018][research_arik_turkmen_2018]\] \[[Ashkenas 1946][research_ashkenas_1946]\] \[[Azor 1995][research_azor_1995]\] \[[Bazile and Calderara 2012][research_bazile_calderara_2012]\] \[[Bean and Lee 1994][research_bean_lee_1994]\] \[[Bird et al 1953][research_bird_fisher_1953]\] \[[Bischoff and Palmer 1983][research_bischoff_palmer_1983]\] \[[Blake et al 2009][research_blake_gotwald_2009]\] \[[Bohlmann et al 1988][research_bohlmann_weisshaar_1988]\] \[[Bohlmann et al 1990][research_bohlmann_eckstrom_1990]\] \[[Boyden 1974][research_boyden_1974]\] \[[Brandon 1986][research_brandon_1986]\] \[[Brandt et al 2011][research_brandt_fossum_2011]\] \[[Bruner 1983][research_bruner_1983]\] \[[Burton and Lamour 1971][research_burton_lamour_1971]\] \[[Cassaro et al 2018][research_cassaro_roos_2018]\] \[[Cavallaro and Bombardieri 2019][research_cavallaro_bombardieri_2019]\] \[[Chapter 13. Control of 1994][research_chapter_13_1994]\] \[[Chapter 6. Lateral-Directional Motions 2005][research_chapter_6_2005]\] \[[Chapter 7. Coupled Longitudinal 2005][research_chapter_7_2005]\] \[[Chen et al 2021][research_chen_shi_2021]\] \[[Chen et al 2026][research_chen_zhang_2026]\] \[[Chowdhury et al 2021][research_chowdhury_keshmiri_2021]\] \[[Chuan et al 2016][research_chuan_feng_2016]\] \[[Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]\] \[[Coe et al 1975][research_coe_graham_1975]\] \[[Colgren and Martin 2000][research_colgren_martin_2000]\] \[[Cook 1997][research_cook_1997_b]\] \[[Cook 2007][research_cook_2007_b]\] \[[Cook 2013][research_cook_2013_b]\] \[[Coupled Longitudinal and Lateral-Directional 2015][research_coupled_longitudinal_2015]\] \[[Crane and Reeder 1945][research_crane_reeder_1945]\] \[[Crider 2004][research_crider_2004]\] \[[de Padua et al 2026][research_depadua_preisigheviana_2026]\] \[[Development of Longitudinal and 2014][research_development_of_2014]\] \[[Development of Longitudinal and 2024][research_development_of_2024]\] \[[Directional Control 2003][research_directional_control_2003]\] \[[Donlan 1976][research_donlan_1976]\] \[[Drake et al 1955][research_drake_finch_1955]\] \[[Driver 1958][research_driver_1958]\] \[[Dunning 1957][research_dunning_1957]\] \[[Dynamic Lateral-Directional Stability Theory 2003][research_dynamic_lateral_directional_2003]\] \[[Eggleston 1956][research_eggleston_1956]\] \[[English 1953][research_english_1953]\] \[[Ericsson 1996][research_ericsson_1996_b]\] \[[Ericsson 1997][research_ericsson_1997_b]\] \[[Ericsson and Ericsson 1997][research_ericsson_ericsson_1997]\] \[[Ericsson and Hanff 1993][research_ericsson_hanff_1993]\] \[[Esteban et al 2015][research_esteban_gavilan_2015]\] \[[Ferman and Turner 1999][research_ferman_turner_1999]\] \[[Ferman and Turner 1999][research_ferman_turner_1999_b]\] \[[Findlay and Findlay 1997][research_findlay_findlay_1997]\] \[[Frazier 1991][research_frazier_1991]\] \[[Funk and Rhyne 1956][research_funk_rhyne_1956]\] \[[Garcia-Baquero et al 2018][research_garciabaquero_esteban_2018]\] \[[Gebhardt 2017][research_gebhardt_2017]\] \[[Gillis 1957][research_gillis_1957]\] \[[Gillis and Chapman 1956][research_gillis_chapman_1956]\] \[[Gilyard et al 1972][research_gilyard_berry_1972]\] \[[Goud and Dwivedi 2022][research_goud_dwivedi_2022]\] \[[Graham and McCaskill 1950][research_graham_mccaskill_1950]\] \[[Grantz 1984][research_grantz_1984]\] \[[Gratton 2014][research_gratton_2014]\] \[[Gratton 2018][research_gratton_2018_b]\] \[[Grismer and Jenkins 1996][research_grismer_jenkins_1996]\] \[[Guillaume et al 2011][research_guillaume_gehri_2011]\] \[[Soule and McAvoy 1934][research_hasoule_whmcavoy_1934]\] \[[Hancock 1972][research_hancock_1972]\] \[[Harman 1944][research_harman_1944]\] \[[Hauch et al 1995][research_hauch_jacobs_1995]\] \[[Hebbar et al 1992][research_hebbar_platzer_1992]\] \[[Henderson and Huffman 1974][research_henderson_huffman_1974]\] \[[Hoot 1924][research_hoot_1924]\] \[[House and Wallace 1941][research_house_wallace_1941]\] \[[Huang and Hanff 1999][research_huang_hanff_1999]\] \[[Huang et al 2000][research_huang_lou_2000]\] \[[Huffman 1975][research_huffman_1975]\] \[[Hunsaker et al 2019][research_hunsaker_montgomery_2019]\] \[[Hunsaker et al 2020][research_hunsaker_montgomery_2020]\] \[[Hunter 1959][research_hunter_1959]\] \[[Hwang et al 2002][research_hwang_park_2002]\] \[[Inertia Coupling and Spin 2004][research_inertia_coupling_2004]\] \[[Inertia Coupling and Spin 2015][research_inertia_coupling_2015]\] \[[James and Meyn 1994][research_james_meyn_1994]\] \[[Jameson 1973][research_jameson_1973]\] \[[Javed and Shafi Khan 2019][research_javed_shafikhan_2019]\] \[[Jenkins et al 1993][research_jenkins_myatt_1993]\] \[[Johnson 1946][research_johnson_1946]\] \[[Johnson 1950][research_johnson_1950]\] \[[Johnson and Hayes 1953][research_johnson_hayes_1953]\] \[[Johnson and Lind 2009][research_johnson_lind_2009]\] \[[Kandil and Flanagan 1994][research_kandil_flanagan_1994]\] \[[Kandil et al 1993][research_kandil_kandil_1993]\] \[[Kandil et al 1994][research_kandil_kalisch_1994]\] \[[Kandil et al 1995][research_kandil_sheta_1995]\] \[[Karasu 2015][research_karasu_2015]\] \[[Katz and Levin 1991][research_katz_levin_1991]\] \[[Kawazoe and Morita 2003][research_kawazoe_morita_2003]\] \[[Kawazoe et al 2001][research_kawazoe_yorikane_2001]\] \[[Kim and Marciniak 1998][research_kim_marciniak_1998]\] \[[Kim and Marciniak 2000][research_kim_marciniak_2000]\] \[[Klunk and Freeman 2018][research_klunk_freeman_2018]\] \[[Kowal and Vakili 1998][research_kowal_vakili_1998]\] \[[Kraft and Reeder 1948][research_kraft_reeder_1948]\] \[[Lamb et al 1981][research_lamb_sawyer_1981]\] \[[Lamb et al 1981][research_lamb_sawyer_1981_b]\] \[[Lan and Hsu 1982][research_lan_hsu_1982]\] \[[Lan et al 2002][research_lan_li_2002]\] \[[Lange 1945][research_lange_1945]\] \[[Lange 1947][research_lange_1947]\] \[[Langston et al 2016][research_langston_nelson_2016]\] \[[Lateral-Directional Dynamic Modes 2016][research_lateral_directional_dynamic_2016]\] \[[Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]\] \[[Lateral-Directional Motion 2016][research_lateral_directional_motion_2016]\] \[[Lateral-Directional Motions 2015][research_lateral_directional_motions_2015]\] \[[Lateral-Directional Stability Theory and 2003][research_lateral_directional_stability_2003]\] \[[Le Provost et al 2018][research_leprovost_williams_2018]\] \[[Lee 2000][research_lee_2000]\] \[[LeMay and Lovato 1994][research_lemay_lovato_1994]\] \[[Lemon et al 2011][research_lemon_litt_2011]\] \[[Letko 1951][research_letko_1951]\] \[[Levinski and Hill 2006][research_levinski_hill_2006]\] \[[Li et al 2025][research_li_zhang_2025]\] \[[Li et al 2026][research_li_wei_2026]\] \[[Liang et al 2025][research_liang_feng_2025]\] \[[Licini et al 2024][research_licini_white_2024]\] \[[Lockwood 1974][research_lockwood_1974]\] \[[Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]\] \[[Lowenberg 2010][research_lowenberg_2010]\] \[[Lu][research_lu]\] \[[Lu and Turkoglu 2016][research_lu_turkoglu_2016]\] \[[Lu and Turkoglu 2018][research_lu_turkoglu_2018]\] \[[Lutze et al 1993][research_lutze_durham_1993]\] \[[Ma et al 2019][research_ma_zhu_2019]\] \[[Mann et al 1987][research_mann_huffman_1987]\] \[[Marino and Mastrocola 1948][research_marino_mastrocola_1948]\] \[[Marino and Mastrocola 1952][research_marino_mastrocola_1952]\] \[[Massey and Kandil 1998][research_massey_kandil_1998]\] \[[McKinney 1946][research_mckinney_1946]\] \[[McKinney 1946][research_mckinney_1946_b]\] \[[McKinney and Shanks 1948][research_mckinney_shanks_1948]\] \[[Meng et al 2007][research_meng_jia_2007]\] \[[Menzies and Kandil 1996][research_menzies_kandil_1996]\] \[[Menzies et al 1995][research_menzies_kandil_1995]\] \[[Mitcham et al 1952][research_mitcham_blanchard_1952]\] \[[Mohamed and Dongare 2021][research_mohamed_dongare_2021]\] \[[Mohammed 2007][research_mohammed_2007]\] \[[Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]\] \[[Moses 1997][research_moses_1997]\] \[[Moses and Ashley 1998][research_moses_ashley_1998]\] \[[Moses and Huttsell 2000][research_moses_huttsell_2000]\] \[[Moss et al 1991][research_moss_cole_1991]\] \[[Murphy and Klein 2010][research_murphy_klein_2010]\] \[[Myatt and Jenkins 1996][research_myatt_jenkins_1996]\] \[[Myatt and Myatt 1997][research_myatt_myatt_1997]\] \[[NACA 1951][research_vertical_fin_location_1951]\] \[[Napolitano et al 1996][research_napolitano_paris_1996]\] \[[Chambers and Hall 2003][research_uncommanded_lateral_2003]\] \[[Nguyen 1974][research_nguyen_1974]\] \[[Nguyen and Stepanyan 2010][research_nguyen_stepanyan_2010]\] \[[Oehman and Suddath 1964][research_oehman_suddath_1964]\] \[[Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]\] \[[Palazzo and Spearman 1954][research_palazzo_spearman_1954]\] \[[Paris][research_paris]\] \[[Paulson 1948][research_paulson_1948]\] \[[Pedreiro et al 1996][research_pedreiro_rock_1996]\] \[[Pepper and Foster 1947][research_pepper_foster_1947]\] \[[Peristy et al 2019][research_peristy_perez_2019]\] \[[Peterson 1961][research_peterson_1961]\] \[[Peterson 2024][research_peterson_2024]\] \[[Peterson and Menees 1961][research_peterson_menees_1961]\] \[[Peterson and Menees 1961][research_peterson_menees_1961_b]\] \[[Phillips 1948][research_phillips_1948]\] \[[Poojari 2022][research_poojari_2022]\] \[[Prediction of vortex breakdown 1994][research_prediction_of_1994]\] \[[Purser and Spear 1946][research_purser_spear_1946]\] \[[Raney 1987][research_raney_1987]\] \[[Raney and Batterson 1989][research_raney_batterson_1989]\] \[[Report No. 379. Rolling 1931][research_report_no_1931]\] \[[Rizzetta 1996][research_rizzetta_1996]\] \[[Roberts and Lind 2009][research_roberts_lind_2009]\] \[[Romberg 2003][research_romberg_2003]\] \[[Rotaru et al 2016][research_rotaru_circiu_2016]\] \[[Sadraey 2022][research_sadraey_2022_c]\] \[[Sadraey 2022][research_sadraey_2022_d]\] \[[Schairer 1941][research_schairer_1941]\] \[[Schmidt and Wright 1991][research_schmidt_wright_1991]\] \[[Schnoebelen and Yechout 2003][research_schnoebelen_yechout_2003]\] \[[Schweiger et al 2000][research_schweiger_weiss_2000]\] \[[Seaver et al 2023][research_seaver_bennett_2023]\] \[[Seckel 1964][research_seckel_1964_c]\] \[[Seckel 1964][research_seckel_1964_d]\] \[[Seckel 1964][research_seckel_1964_e]\] \[[Seckel 1964][research_seckel_1964_f]\] \[[Shah and Granda 1998][research_shah_granda_1998]\] \[[Shen et al 2019][research_shen_huang_2019]\] \[[Sheta 2004][research_sheta_2004]\] \[[Sheta and Huttsell 2001][research_sheta_huttsell_2001]\] \[[Sheta and Huttsell 2002][research_sheta_huttsell_2002]\] \[[Sheta and Huttsell 2003][research_sheta_huttsell_2003]\] \[[Sheta et al 2001][research_sheta_rock_2001]\] \[[Sheta et al 2003][research_sheta_moses_2003]\] \[[Silva et al 2022][research_silva_nunes_2022]\] \[[Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]\] \[[Singh and Scholz 2018][research_singh_scholz_2018]\] \[[Sinha and Ananthkrishnan 2017][research_sinha_ananthkrishnan_2017]\] \[[Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021_b]\] \[[Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021_c]\] \[[Siu et al 2013][research_siu_martos_2013]\] \[[Sivan 1971][research_sivan_1971]\] \[[Sjoberg 1945][research_sjoberg_1945]\] \[[Sleeman 1957][research_sleeman_1957]\] \[[Sleeman and Morrison 1953][research_sleeman_morrison_1953]\] \[[Soehne 1956][research_soehne_1956]\] \[[Soule and Wetmore 1933][research_soule_wetmore_1933]\] \[[Spreemann and Few 1954][research_spreemann_few_1954]\] \[[Stalford 1979][research_stalford_1979]\] \[[Stepanyan et al 2010][research_stepanyan_kalmanje_2010]\] \[[Stephenson et al 1990][research_stephenson_jeske_1990]\] \[[Stough and Kauffman 1950][research_stough_kauffman_1950]\] \[[Strass and Marley 1952][research_strass_marley_1952]\] \[[Suplisson et al 2011][research_suplisson_brandt_2011]\] \[[Szema and Shankar 1984][research_szema_shankar_1984]\] \[[Tai et al 2023][research_tai_wang_2023]\] \[[Tang 2019][research_tang_2019]\] \[[Taufik et al 2024][research_taufik_zaidaan_2024]\] \[[Tewari 2000][research_tewari_2000]\] \[[Thacker and Lan 1993][research_thacker_lan_1993]\] \[[Thomas and Wolhart 1957][research_thomas_wolhart_1957]\] \[[Ueno et al 1998][research_ueno_matsuno_1998]\] \[[Ulbrich 2006][research_ulbrich_2006]\] \[[Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]\] \[[van der Maas 1959][research_vandermaas_1959]\] \[[Vardaki and Gursul 2004][research_vardaki_gursul_2004]\] \[[Velger and Shinar 1983][research_velger_shinar_1983]\] \[[Wallace 1942][research_wallace_1942]\] \[[Wallace 1944][research_wallace_1944]\] \[[Wallace and Recant 1943][research_wallace_recant_1943]\] \[[Williams and Hoover 1945][research_waltercwilliams_herberthhoover_1945]\] \[[Wang et al 2022][research_wang_zhao_latdir_2022]\] \[[Wang et al 1999][research_wang_lan_1999]\] \[[Wang et al 2002][research_wang_lan_2002]\] \[[Weick and Noyes 1933][research_weick_noyes_1933]\] \[[Wen et al 2013][research_wen_deng_2013]\] \[[Winograd Cooper Rathert and Rolls 1950][research_winograd_1950]\] \[[Wollner and Cooney 1948][research_wollner_cooney_1948]\] \[[Wolowicz 1945][research_wolowicz_1945]\] \[[Yeo et al 2015][research_yeo_atkins_2015]\] \[[Zanette and Almeida 2015][research_zanette_almeida_2015]\] \[[Zhang and Ye 2015][research_zhang_ye_2015]\] \[[Zhao and Hu 2009][research_zhao_hu_2009]\] \[[Zou et al 2016][research_zou_li_2016]\]

### Stall, pitch-up, departure, wing rock and tumbling

**What happens past the linear range.** Stall, pitch-up, departure and spin, abrupt wing stall, wing rock and tumbling. **98 of these titles name wing rock, and 65 of those name a slender or delta wing**, the planform family whose vortex flow the Contemporary Literature review above connects to the X-4's reported hunting.

**237 records.** \[[A General Theory of 2010][research_a_general_2010]\] \[[Altunkaya and Catak 2025][research_altunkaya_2025]\] \[[Anderson and Bray 1955][research_anderson_bray_1955]\] \[[Arena and Nelson 1989][research_arena_nelson_1989]\] \[[Arena and Nelson 1991][research_arena_nelson_1991]\] \[[Arena and Nelson 1992][research_arena_nelson_1992]\] \[[Arena and Nelson 1994][research_arena_nelson_1994]\] \[[Arena et al 1990][research_arena_nelson_1990]\] \[[Axelson 1975][research_axelson_1975]\] \[[Axelson 1977][research_axelson_1977]\] \[[Ayoub and McLachlan 1987][research_ayoub_mclachlan_1987]\] \[[Bakaul et al 2012][research_bakaul_wang_2012]\] \[[Bakaul et al 2014][research_bakaul_yankui_2014]\] \[[Bakaul et al 2015][research_bakaul_wang_2015]\] \[[Bakaul et al 2015][research_bakaul_wang_2015_b]\] \[[Beyers and Brown 2006][research_beyers_brown_2006]\] \[[Birch and Lee 2005][research_birch_lee_2005]\] \[[Black 1956][research_black_1956]\] \[[Bobbitt and Foughner 1985][research_bobbitt_foughner_1985]\] \[[Bowman et al 1978][research_bowman_stough_1978]\] \[[Bragg and Soltani 1990][research_bragg_soltani_1990]\] \[[Bramantya and Nugroho 2025][research_bramantya_nugroho_2025]\] \[[Briggs et al 1982][research_briggs_reed_1982]\] \[[Bui 2013][research_bui_2013]\] \[[Bui 2015][research_bui_2015]\] \[[Bui 2016][research_bui_2016]\] \[[Celik and Roberts 1992][research_celik_roberts_1992]\] \[[Cen et al 2020][research_cen_li_2020]\] \[[Chaderjian 1992][research_chaderjian_1992]\] \[[Chapter 8 The Aircraft 2025][research_chapter_8_2025]\] \[[Chavatzopoulos et al 2012][research_chavatzopoulos_giotis_2012]\] \[[Croom et al 1988][research_croom_whipple_1988]\] \[[Culler and Farnsworth 2019][research_culler_farnsworth_2019]\] \[[Cunningham et al 2019][research_cunningham_shah_2019]\] \[[Currao and Jiang 2026][research_currao_jiang_2026]\] \[[Dong et al 2022][research_dong_low_ar_2022]\] \[[Dongmo 2011][research_dongmo_2011]\] \[[Ekaterinaris 1995][research_ekaterinaris_1995]\] \[[Eldredge et al 2009][research_eldredge_wang_2009]\] \[[Elkhoury 2008][research_elkhoury_2008]\] \[[Elkhoury 2016][research_elkhoury_2016]\] \[[Elzebda et al 1987][research_elzebda_mook_1987]\] \[[Elzebda et al 1989][research_elzebda_mook_1989]\] \[[Elzebda et al 1989][research_elzebda_nayfeh_1989]\] \[[Ericsson 1983][research_ericsson_1983]\] \[[Ericsson 1984][research_ericsson_1984]\] \[[Ericsson 1987][research_ericsson_1987]\] \[[Ericsson 1987][research_ericsson_1987_b]\] \[[Ericsson 1988][research_ericsson_1988]\] \[[Ericsson 1988][research_ericsson_1988_b]\] \[[Ericsson 1989][research_ericsson_1989]\] \[[Ericsson 1991][research_ericsson_1991]\] \[[Ericsson 1993][research_ericsson_1993]\] \[[Ericsson 1995][research_ericsson_1995]\] \[[Ericsson 1996][research_ericsson_1996_c]\] \[[Ericsson 1998][research_ericsson_1998]\] \[[Ericsson 1998][research_ericsson_1998_b]\] \[[Ericsson 1999][research_ericsson_1999]\] \[[Ericsson 2000][research_ericsson_2000]\] \[[Ericsson 2000][research_ericsson_2000_b]\] \[[Ericsson 2002][research_ericsson_2002]\] \[[Ericsson and Mendenhall 1994][research_ericsson_mendenhall_1994]\] \[[Ericsson and Reding 1985][research_ericsson_reding_1985]\] \[[Estevadeordal et al 2022][research_estevadeordal_ullah_2022]\] \[[Favier et al 1988][research_favier_agnes_1988]\] \[[Fernand and Downing 1994][research_fernand_downing_1994]\] \[[Foa 1942][research_foa_1942]\] \[[Gainer 2002][research_gainer_2002]\] \[[Garmann and Visbal 2020][research_garmann_visbal_2020]\] \[[Garmann and Visbal 2021][research_garmann_visbal_2021]\] \[[Garmann and Visbal 2022][research_garmann_visbal_2022]\] \[[Garmann and Visbal 2022][research_garmann_visbal_2022_b]\] \[[Garmann and Visbal 2023][research_garmann_visbal_2023]\] \[[Gera et al 1981][research_gera_wilson_1981]\] \[[Goman et al 1992][research_goman_khrabrov_1992]\] \[[Green and Ott 2003][research_green_ott_2003]\] \[[Guglieri 2012][research_guglieri_2012]\] \[[Hahne 1985][research_hahne_1985]\] \[[Hall et al 2003][research_hall_woodson_2003]\] \[[Hammer et al 2021][research_hammer_garmann_2021]\] \[[Hammer et al 2023][research_hammer_garmann_2023_b]\] \[[Hebbar et al 1993][research_hebbar_platzer_1993]\] \[[Helin and Walker 1985][research_helin_walker_1985]\] \[[Hemsch 1989][research_hemsch_1989]\] \[[Heron and Myose 2007][research_heron_myose_2007]\] \[[Hirose et al 2007][research_hirose_nagai_2007]\] \[[Hoadley and Vanderbok 1986][research_hoadley_vanderbok_1986]\] \[[Hoadley and VanderBok 1988][research_hoadley_vanderbok_1988]\] \[[Hoang et al 1993][research_hoang_rediniotis_1993]\] \[[Hong 1993][research_hong_1993]\] \[[Hosangadi et al 2015][research_hosangadi_paul_2015]\] \[[Hsu and Lan 1984][research_hsu_lan_1984]\] \[[Hsu and Lan 1985][research_hsu_lan_1985]\] \[[Hui and Tobak 1985][research_hui_tobak_1985]\] \[[Humayun et al 2013][research_humayun_wang_2013]\] \[[Hwang and Pi 1978][research_hwang_pi_1978]\] \[[Hwang and Pi 1978][research_hwang_pi_1978_b]\] \[[Hwang and Pi 1979][research_hwang_pi_1979_b]\] \[[Isogai 2013][research_isogai_2013]\] \[[Itty and Leith 1992][research_itty_leith_1992]\] \[[Jahnke and Culick 1990][research_jahnke_culick_1990]\] \[[Jamwal et al 2018][research_jamwal_hosangadi_2018]\] \[[Jarrah 1989][research_jarrah_1989]\] \[[Jordan et al 1987][research_jordan_hahne_1987]\] \[[Joshi et al 1998][research_joshi_sreenatha_1998]\] \[[Jun and Nelson 1987][research_jun_nelson_1987]\] \[[Kanazaki and Setoguchi 2023][research_kanazaki_2023]\] \[[Kandil and Menzies 1997][research_kandil_menzies_1997]\] \[[Kandil and Salman 1992][research_kandil_salman_1992]\] \[[Kandil and Salman 1992][research_kandil_salman_1992_b]\] \[[Katz 1999][research_katz_1999]\] \[[Kawazoe and Morita 2004][research_kawazoe_morita_2004]\] \[[Khan and Deng 2012][research_khan_deng_2012]\] \[[Klein and Batterson 1983][research_klein_batterson_1983]\] \[[Klein et al 1981][research_klein_batterson_1981]\] \[[Klinar and Jones 1948][research_klinar_jones_1948]\] \[[Konstadinopoulos et al 1985][research_konstadinopoulos_mook_1985]\] \[[Kumar et al 2025][research_kumar_palanivel_2025]\] \[[Kuz'min 2007][research_kuzmin_2007]\] \[[Kuz'min 2009][research_kuzmin_2009]\] \[[Lee and Batina 1990][research_lee_batina_1990]\] \[[Lee and Batina 1990][research_lee_batina_1990_b]\] \[[Lee and Batina 1991][research_lee_batina_1991]\] \[[Lee and Gross 2024][research_lee_gross_2024]\] \[[Liebst and Nolan 1993][research_liebst_nolan_1993]\] \[[Lin and Hsu 2004][research_lin_hsu_2004]\] \[[Liu et al 2005][research_liu_zhang_2005]\] \[[Liu et al 2006][research_liu_zhang_2006]\] \[[Lockwood 1966][research_lockwood_1966]\] \[[Lorber and Carta 1988][research_lorber_carta_1988]\] \[[Lorber et al 1991][research_lorber_covino_1991]\] \[[Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]\] \[[Luo and Lan 1993][research_luo_lan_1993]\] \[[Ma et al 2016][research_ma_deng_2016]\] \[[Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]\] \[[Marschalk et al 2021][research_marschalk_luteijn_2021]\] \[[Matsuno et al 2003][research_matsuno_yokouchi_2003]\] \[[Medina et al 2019][research_medina_rockwood_2019]\] \[[Meyer et al 1989][research_meyer_yip_1989]\] \[[Midhat 2017][research_midhat_2017]\] \[[Mizoguchi et al 2014][research_mizoguchi_kajikawa_2014]\] \[[Mohamed et al 2009][research_mohamed_nadarajah_2009]\] \[[Mohamed et al 2009][research_mohamed_nadarajah_2009_b]\] \[[Monahemi et al 1995][research_monahemi_barlow_1995]\] \[[Moosavi 2025][research_moosavi_2025]\] \[[Morris and Ward 1989][research_morris_ward_1989]\] \[[Murri et al 1983][research_murri_croom_1983]\] \[[Sadoff and Sisk 1950][research_x4_stall_1950]\] \[[Hurt and Whitten 1960][research_pitchup_control_1960]\] \[[Patton et al 1979][research_spin_research_summary_1979]\] \[[Fourth High Alpha Conference 1994][research_high_alpha_conf_1994]\] \[[Nayfeh et al 1989][research_nayfeh_elzebda_1989]\] \[[Nelson and Arena 1993][research_nelson_arena_1993]\] \[[Ng and Malcolm 1990][research_ng_malcolm_1990]\] \[[Ng et al 1989][research_ng_malcolm_1989]\] \[[Ng et al 1991][research_ng_ong_1991]\] \[[Ng et al 1992][research_ng_malcolm_1992]\] \[[Ng et al 1993][research_ng_skaff_1993]\] \[[Ng et al 1994][research_ng_skaff_1994]\] \[[Nguyen et al 2021][research_nguyen_lowenberg_2021]\] \[[Nguyen et al 1981][research_nguyen_yip_1981]\] \[[Nguyen et al 1985][research_nguyen_whipple_1985]\] \[[Niranjana et al 1993][research_niranjana_rao_1993]\] \[[Ostroff 1998][research_ostroff_1998]\] \[[Owens et al 2003][research_owens_capone_2003]\] \[[Pattinson et al 2013][research_pattinson_lowenberg_2013]\] \[[Pavelka and Tatum 1980][research_pavelka_tatum_1980]\] \[[Pitch-down dynamic stall characteristics 1994][research_pitch_down_dynamic_1994]\] \[[Plante][research_plante]\] \[[Prakash et al 2009][research_prakash_uthup_2009]\] \[[Prudnikov et al 1993][research_prudnikov_karavayev_1993]\] \[[Quast et al 1991][research_quast_nelson_1991]\] \[[Qureshi et al 2014][research_qureshi_wang_2014]\] \[[Rainey 1957][research_rainey_1957]\] \[[Ramirez Zeigler and Avery 2026][research_ramirezzeigler_avery_2026]\] \[[Rao and Johnson 1982][research_rao_johnson_1982]\] \[[Rao and Johnson 1983][research_rao_johnson_1983]\] \[[Ray 1965][research_ray_1965]\] \[[Rediniotis et al 1994][research_rediniotis_klute_1994]\] \[[Reu and Ying 1991][research_reu_ying_1991]\] \[[Rockwood et al 2019][research_rockwood_medina_2019]\] \[[Rong et al 2016][research_rong_deng_2016]\] \[[Saephan and Van Dam 2008][research_saephan_vandam_2008]\] \[[Salahudden et al 2020][research_salahudden_giri_2020]\] \[[Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]\] \[[Shao et al 2022][research_shao_liu_2022]\] \[[Shumsky 2006][research_shumsky_2006]\] \[[Siddiqui et al 2023][research_siddiqui_sultan_2023]\] \[[Singh et al 1994][research_singh_yim_1994]\] \[[Singh et al 1995][research_singh_yirn_1995]\] \[[Sjoberg and Reeder 1948][research_sjoberg_reeder_1948]\] \[[Sjoberg and Reeder 1948][research_sjoberg_reeder_1948_b]\] \[[Spreemann 1959][research_spreemann_1959]\] \[[Stalford 1980][research_stalford_1980]\] \[[Stall Characteristics 2003][research_stall_characteristics_2003]\] \[[Stall Speed Measurement 2003][research_stall_speed_2003]\] \[[Stengel 1976][research_stengel_1976]\] \[[Stengel and Berry 1976][research_stengel_berry_1976]\] \[[Stengel and Berry 1977][research_stengel_berry_1977]\] \[[Stone 1950][research_stone_1950]\] \[[Stough et al 1987][research_stough_dicarlo_1987]\] \[[Suarez et al 1992][research_suarez_kramer_1992]\] \[[Suarez et al 1993][research_suarez_smith_1993]\] \[[Suarez et al 1993][research_suarez_smith_1993_b]\] \[[Sun et al 2026][research_sun_wang_2026]\] \[[Tang and Dowell 1995][research_tang_dowell_1995]\] \[[Tarn and Hsu][research_tarn_hsu]\] \[[Tarn and Hsu 1993][research_tarn_hsu_1993]\] \[[Taylor and Pamadi 1983][research_taylor_pamadi_1983]\] \[[Telionis 1995][research_telionis_1995]\] \[[Telionis 2001][research_telionis_2001]\] \[[The effects of canard-wing 1988][research_the_effects_1988]\] \[[Tomek et al 2020][research_tomek_ullah_2020]\] \[[Tu et al 2024][research_tu_yan_2024]\] \[[Tu et al 2019][research_tu_marzanek_2019]\] \[[Ullah et al 2021][research_ullah_tomek_2021]\] \[[Ullah et al 2022][research_ullah_fabijanic_2022]\] \[[Van Dommelen 1995][research_vandommelen_1995]\] \[[Walker 1987][research_walker_1987]\] \[[Walton and Katz 1992][research_walton_katz_1992]\] \[[Walton and Katz 1993][research_walton_katz_1993]\] \[[Wang 1979][research_wang_1979]\] \[[Wang et al 2012][research_wang_zhang_2012]\] \[[Williams et al 1995][research_williams_inelson_1995]\] \[[Winkelmann 1989][research_winkelmann_1989]\] \[[Wong et al 1993][research_wong_rock_1993]\] \[[Xu and Deng 2014][research_xu_deng_2014]\] \[[Xu et al 2013][research_xu_deng_2013]\] \[[Yang and Przekwas 1993][research_yang_przekwas_1993_b]\] \[[YanKui Wang and Qian Li 2015][research_yankuiwang_qianli_2015]\] \[[Yavuz 2012][research_yavuz_2012]\] \[[Yildiz et al 2019][research_yildiz_akcal_2019]\] \[[Yoo and Bowers 2018][research_yoo_bowers_2018]\] \[[Yoshinaga et al 2004][research_yoshinaga_nakaji_2004]\] \[[Young 2026][research_young_2026]\] \[[Zohar and Er-El 1988][research_zohar_erel_1988]\] \[[Zverkov et al 2012][research_zverkov_kozlov_2012]\]

### Wing planform aerodynamics and the swept wing

**The wing that has to do the tail's work.** Swept, delta and low aspect ratio wings, induced drag and twist, vortex flows and swept-wing boundary layer transition.

**199 records.** \[[Abdelhamid and Kandil 1998][research_abdelhamid_kandil_1998]\] \[[Ackeret 1925][research_ackeret_1925]\] \[[Aerodynamics of arbitrary wing 1976][research_aerodynamics_of_1976]\] \[[Amprikidis and Cooper 2004][research_amprikidis_cooper_2004]\] \[[An experimental and computational 1978][research_an_experimental_1978]\] \[[Arai et al 2000][research_arai_noto_2000]\] \[[Araujo-Estrada et al 2022][research_araujoestrada_lowenberg_2022]\] \[[Archambaud et al 2004][research_archambaud_louis_2004]\] \[[Ashworth et al 1988][research_ashworth_mouch_1988]\] \[[Aso and Tanaka 2017][research_aso_tanaka_2017]\] \[[Aso et al 2018][research_aso_tanaka_2018]\] \[[Ayoub and McLachlan 1988][research_ayoub_mclachlan_1988]\] \[[Balogun et al 2026][research_balogun_khan_2026]\] \[[Banner et al 1958][research_banner_1958]\] \[[Barsby 1973][research_barsby_1973]\] \[[Bera 1974][research_bera_1974]\] \[[Bera 1974][research_bera_1974_b]\] \[[Bernal 2016][research_bernal_2016]\] \[[Bertelrud 1981][research_bertelrud_1981]\] \[[Bertelsen 2006][research_bertelsen_2006]\] \[[Bihrle and Mulcay 1979][research_bihrle_mulcay_1979]\] \[[Bippes 1990][research_bippes_1990]\] \[[Bodonyl 1994][research_bodonyl_1994]\] \[[Bollech and Furlong 1948][research_bollech_furlong_1948]\] \[[Bourdin 2002][research_bourdin_2002]\] \[[Brandt and Bons 2024][research_brandt_bons_2024]\] \[[Brody et al 2025][research_brody_fagley_2025]\] \[[Buell and Johnson 1959][research_buell_johnson_1959]\] \[[Buter and Rao 1984][research_buter_rao_1984]\] \[[Calculation of Low Aspect 2008][research_calculation_of_2008]\] \[[Campbell 1957][research_campbell_1957]\] \[[Campbell 1958][research_campbell_1958]\] \[[Campbell 1959][research_campbell_1959]\] \[[Carnduff et al 2009][research_carnduff_erbsloeh_2009]\] \[[Carpenter et al 2008][research_carpenter_saric_2008]\] \[[Chaderjian and Schiff 1993][research_chaderjian_schiff_1993]\] \[[Chen 2018][research_chen_2018]\] \[[Chen et al 2001][research_chen_khalid_2001]\] \[[Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]\] \[[Cole 1986][research_cole_1986]\] \[[Cole 1988][research_cole_1988]\] \[[Cousteix and Pailhas 1983][research_cousteix_pailhas_1983]\] \[[Craig 1991][research_craig_1991]\] \[[Dehaan 1990][research_dehaan_1990]\] \[[Deneke et al 2026][research_deneke_carter_2026]\] \[[Deyoung 1979][research_deyoung_1979]\] \[[Duncan et al 2013][research_duncan_crawford_2013]\] \[[El Mobaraky et al 2025][research_elmobaraky_kouiss_2025]\] \[[ElRamly][research_elramly]\] \[[Elsayed et al 2007][research_elsayed_scarano_2007]\] \[[Engelbrecht][research_engelbrecht]\] \[[Eppink 2023][research_eppink_2023]\] \[[Er-El et al 1989][research_erel_seter_1989]\] \[[Ericsson 1986][research_ericsson_1986]\] \[[Ericsson 1996][research_ericsson_1996]\] \[[Ericsson 1997][research_ericsson_1997]\] \[[Ericsson and King 1990][research_ericsson_king_1990]\] \[[Ericsson and King 1990][research_ericsson_king_1990_b]\] \[[Experience Gained During Development 2010][research_experience_gained_2010]\] \[[Fink and Lastinger 1961][research_fink_lastinger_1961]\] \[[Finn 1944][research_finn_1944]\] \[[Furlong and Bollech 1951][research_furlong_bollech_1951]\] \[[Furlong and Bollech 1955][research_furlong_bollech_1955]\] \[[German Development of the 2010][research_german_development_2010]\] \[[Gerontakos and Lee 2005][research_gerontakos_lee_2005]\] \[[Ghaffari et al 2002][research_ghaffari_biedron_2002]\] \[[Ghaffari et al 2002][research_ghaffari_biedron_2002_b]\] \[[Ghasemi et al 2014][research_ghasemi_mosahebi_2014]\] \[[Ghee et al 1999][research_ghee_gonzalez_1999]\] \[[Gonzalez and Winkelmann 1993][research_gonzalez_winkelmann_1993]\] \[[Gopalarathnam et al 1997][research_gopalarathnam_selig_1997]\] \[[Gordnier 1991][research_gordnier_1991]\] \[[Govindarajan and Narasimha 2000][research_govindarajan_narasimha_2000]\] \[[Gresham et al 2009][research_gresham_wang_2009_b]\] \[[Griffin and Jonas 1983][research_griffin_jonas_1983]\] \[[Gülsaçan et al 2018][research_gulsacan_sencan_2018]\] \[[Hammer and Garmann 2023][research_hammer_garmann_2023]\] \[[Hanin and Barsony-Nagy 1983][research_hanin_barsonynagy_1983]\] \[[Hargrove 1976][research_hargrove_1976]\] \[[Hayostek and Amitay 2018][research_hayostek_amitay_2018]\] \[[Heron and Myose 2003][research_heron_myose_2003]\] \[[Hicks and Moulton 1988][research_hicks_moulton_1988]\] \[[Huang and Chow 1996][research_huang_chow_1996]\] \[[Hussain and Bons 2019][research_hussain_bons_2019]\] \[[Iosilevskii 2025][research_iosilevskii_2025]\] \[[Iyer et al 1992][research_iyer_spall_1992]\] \[[Jacobs Abbott and Davidson 1942][research_jacobs_1942]\] \[[Kandil and Salman 1991][research_kandil_salman_1991]\] \[[Katz 1989][research_katz_1989]\] \[[Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]\] \[[Khalid 2023][research_khalid_2023]\] \[[Kloker 2008][research_kloker_2008]\] \[[Krone 1980][research_krone_1980]\] \[[Krone 1980][research_krone_1980_b]\] \[[Kroo 1982][research_kroo_1982]\] \[[Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]\] \[[Kurz and Kloker 2015][research_kurz_kloker_2015]\] \[[Kuzmina et al 2004][research_kuzmina_ishmuratov_2004]\] \[[Laiq-Ur Rehman 2013][research_laiqurrehman_2013]\] \[[Lampropoulos and Sarris 2025][research_lampropoulos_sarris_2025]\] \[[Lee and Pereira 2013][research_lee_pereira_2013]\] \[[Lee and Pereira 2013][research_lee_pereira_2013_b]\] \[[Leylek and Costello 2013][research_leylek_costello_2013]\] \[[Li et al 2019][research_li_qian_2019]\] \[[Lin and Lee 2023][research_lin_lee_2023]\] \[[Liu and Weng 2007][research_liu_weng_2007]\] \[[Lowry and Schneiter 1948][research_lowry_schneiter_1948]\] \[[Magill et al 1994][research_magill_darden_1994]\] \[[Magness et al 1992][research_magness_robinson_1992]\] \[[Malik and Li 1993][research_malik_li_1993]\] \[[Mamla and Galinski 2009][research_mamla_galinski_2009]\] \[[Mansour 1985][research_mansour_1985]\] \[[Martin 2008][research_martin_2008]\] \[[Matsuno and Nakamura 2000][research_matsuno_nakamura_2000]\] \[[McLemore and Peterson 1960][research_mclemore_peterson_1960]\] \[[Midmer and Bruecker 2024][research_midmer_bruecker_2024]\] \[[Miles 1952][research_miles_1952]\] \[[Mirels 1953][research_mirels_1953]\] \[[Mistry et al 2013][research_mistry_page_2013]\] \[[Moore and Frei 1983][research_moore_frei_1983]\] \[[Moore and Pullin 1995][research_moore_pullin_1995]\] \[[Morton 1956][research_morton_1956]\] \[[Morton et al 2002][research_morton_mitchell_2002]\] \[[Naigle et al 2022][research_naigle_hiltner_2022]\] \[[Nangia et al 2003][research_nangia_palmer_2003]\] \[[Nelson et al 1991][research_nelson_arena_1991]\] \[[Neves and Mariani 2024][research_neves_mariani_2024]\] \[[Newey][research_newey]\] \[[Nomura 2003][research_nomura_2003]\] \[[Nonweiler 1960][research_nonweiler_1960]\] \[[Ohira et al 2013][research_ohira_kwak_2013]\] \[[Olsen and Seegmiller 1992][research_olsen_seegmiller_1992]\] \[[Olsen and Seegmiller 1993][research_olsen_seegmiller_1993]\] \[[Oswald 1932][research_oswald_1932]\] \[[Pakmehr et al][research_pakmehr_gordon]\] \[[Pakmehr et al 2005][research_pakmehr_gordon_2005]\] \[[Pelletier and Nelson 1994][research_pelletier_nelson_1994]\] \[[Perraud et al 2003][research_perraud_moens_2003]\] \[[Pfaff 1965][research_pfaff_1965]\] \[[Popescu 1999][research_popescu_1999]\] \[[Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]\] \[[Radzetsky et al 1994][research_radzetsky_reibert_1994]\] \[[Rambacher et al 2024][research_rambacher_butler_2024]\] \[[Reed 1984][research_reed_1984]\] \[[Reed 1985][research_reed_1985]\] \[[Reed 1987][research_reed_1987]\] \[[Reibert et al 1997][research_reibert_saric_1997]\] \[[Rimer et al 1983][research_rimer_chipman_1983]\] \[[Rivers et al 2012][research_rivers_hunter_2012]\] \[[Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]\] \[[Robinson and Robinson 1980][research_robinson_robinson_1980]\] \[[Rockwell 1994][research_rockwell_1994]\] \[[Rodden 1989][research_rodden_1989]\] \[[Runyan and George-Falvy 1979][research_runyan_georgefalvy_1979]\] \[[Rymarz and Ramaprian 1995][research_rymarz_ramaprian_1995]\] \[[Sanders 1965][research_sanders_1965]\] \[[Saric 1997][research_saric_1997]\] \[[Saric 2010][research_saric_2010]\] \[[Saric and Yeates 1985][research_saric_yeates_1985]\] \[[Sboev D 2024][research_sboevd_2024]\] \[[Schauerhamer and Robinson 2017][research_schauerhamer_robinson_2017]\] \[[Schuelein 2008][research_schuelein_2008]\] \[[Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]\] \[[Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016]\] \[[Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016_b]\] \[[Sharif et al 2022][research_sharif_abbas_2022]\] \[[Spacht 1980][research_spacht_1980]\] \[[Spreiter and Stahara 1971][research_spreiter_stahara_1971]\] \[[Stebbins and Loth 2022][research_stebbins_loth_2022]\] \[[Telionis 1990][research_telionis_1990]\] \[[Teplitz et al 1946][research_teplitz_kayten_1946]\] \[[The stability of the 1979][research_the_stability_1979]\] \[[Three-dimensional boundary-layer transition on 1994][research_three_dimensional_boundary_layer_1994]\] \[[Tucker and Quinn 1944][research_tucker_quinn_1944]\] \[[Tufts et al 2013][research_tufts_reed_2013]\] \[[Ulrich et al 2001][research_ulrich_roche_2001]\] \[[van Dam 1985][research_vandam_1985]\] \[[Van Dam 1986][research_vandam_1986]\] \[[Verma and Kulkarni 2024][research_verma_kulkarni_2024]\] \[[Vey et al 2010][research_vey_greenblatt_2010]\] \[[Visbal 2017][research_visbal_2017]\] \[[Visbal and Garmann 2012][research_visbal_garmann_2012]\] \[[Vishwanathan][research_vishwanathan]\] \[[Visonneau et al 2022][research_visonneau_guilmineau_2022]\] \[[Wallace 1952][research_wallace_1952]\] \[[Wang et al 1994][research_wang_herbert_1994_b]\] \[[Warren et al 1997][research_warren_hassan_1997]\] \[[Wentz and Nyenhuis 1984][research_wentz_nyenhuis_1984]\] \[[White et al 2001][research_white_saric_2001]\] \[[Wing tunnel model for 1998][research_wing_tunnel_1998]\] \[[Wing twist control and 1998][research_wing_twist_1998]\] \[[Woodruff et al 2011][research_woodruff_saric_2011]\] \[[Yang and Przekwas 1993][research_yang_przekwas_1993]\] \[[Yasuaki and Egami 1999][research_yasuaki_egami_1999]\] \[[Young and Martin 1992][research_young_martin_1992]\] \[[Yu and Bernal 2016][research_yu_bernal_2016]\] \[[Yu et al 2013][research_yu_bernal_2013]\] \[[Ziff et al 1953][research_ziff_rathert_1953]\] \[[Zoppini et al 2022][research_zoppini_ragni_2022]\]

### Longitudinal stability, trim and the short-period mode

**The axis the tail governs.** Static and dynamic longitudinal stability, neutral and manoeuvre points, trim and its drag, and the short-period and phugoid modes.

**196 records.** \[[Abualigah et al 2024][research_abualigah_ekinci_2024]\] \[[Addendum 2 Longitudinal Control 2000][research_addendum_2_2000]\] \[[Aircraft Cruise in Steady 2011][research_aircraft_cruise_2011]\] \[[Aircraft Cruise in Steady 2011][research_aircraft_cruise_2011_b]\] \[[Aircraft Static Stability 2003][research_aircraft_static_2003]\] \[[Aircraft Static Stability 2014][research_aircraft_static_2014]\] \[[Aircraft Static Stability 2024][research_aircraft_static_2024]\] \[[Aircraft Steady Gliding Longitudinal 2011][research_aircraft_steady_2011_c]\] \[[Aircraft Steady Gliding Longitudinal 2011][research_aircraft_steady_2011_d]\] \[[Aircraft Steady Longitudinal Flight 2011][research_aircraft_steady_2011]\] \[[Aircraft Steady Longitudinal Flight 2011][research_aircraft_steady_2011_b]\] \[[Airplane Trim 2012][research_airplane_trim_2012]\] \[[Airplane Trim 2022][research_airplane_trim_2022]\] \[[Al-Hiddabi and McClamroch 2002][research_alhiddabi_mcclamroch_2002]\] \[[Altunkaya and Ozkol 2022][research_altunkaya_ozkol_2022_b]\] \[[Altunkaya and Ozkol 2023][research_altunkaya_ozkol_2023]\] \[[Ameho and Prempain 2011][research_ameho_prempain_2011]\] \[[An Introduction to the 1966][research_an_introduction_1966]\] \[[Anandakumar et al 2022][research_anandakumar_bernstein_2022]\] \[[Ananthkrishnan 2004][research_ananthkrishnan_2004]\] \[[Ananthkrishnan and Ramadevi 2002][research_ananthkrishnan_ramadevi_2002]\] \[[Argyle and Beard 2016][research_argyle_beard_2016]\] \[[Assadourian and Reeder 1948][research_assadourian_reeder_1948]\] \[[Avanzini et al 2017][research_avanzini_nicassio_2017]\] \[[Babister 1980][research_babister_1980]\] \[[Bajpai and Chang][research_bajpai_chang]\] \[[Balakrishna and Niranjana 1987][research_balakrishna_niranjana_1987]\] \[[Becht and Few 1950][research_becht_few_1950]\] \[[Bielat 1959][research_bielat_1959]\] \[[Blodgett and Lagor 2022][research_blodgett_lagor_2022]\] \[[Bloy 1996][research_bloy_1996]\] \[[Bloy 1998][research_bloy_1998]\] \[[Boisseau 1955][research_boisseau_1955]\] \[[Bordei and Halanay 2018][research_bordei_halanay_2018]\] \[[Borri and Trainelli 2003][research_borri_trainelli_2003]\] \[[Boschetti and Cardenas 2012][research_boschetti_cardenas_2012]\] \[[Boschetti et al 2010][research_boschetti_cardenas_2010]\] \[[Bouadi et al 2012][research_bouadi_choukroun_2012]\] \[[Brigido-Gonzalez and Rodriguez-Cortes 2014][research_brigidogonzalez_rodriguezcortes_2014]\] \[[Buell and Tinling 1957][research_buell_tinling_1957]\] \[[Burlion et al 2014][research_burlion_poussotvassal_2014]\] \[[Cadwell][research_cadwell]\] \[[Campos et al 1995][research_campos_fonseca_1995]\] \[[Chapter 12. Control of 1994][research_chapter_12_1994]\] \[[Cheng et al 2025][research_cheng_cea_2025]\] \[[Ciliberti and Nicolosi 2026][research_ciliberti_nicolosi_2026]\] \[[Clark and Hodapp 1972][research_clark_hodapp_1972]\] \[[Conrad et al 2025][research_conrad_michalka_2025]\] \[[Crabill 1956][research_crabill_1956]\] \[[Crane 1948][research_crane_1948]\] \[[Crane and Beckhardt 1948][research_crane_beckhardt_1948]\] \[[Crowe 1937][research_crowe_1937]\] \[[Danek 2002][research_danek_2002]\] \[[Deepa and Sudha 2016][research_deepa_sudha_2016]\] \[[Delany 1942][research_delany_1942]\] \[[Dias 2022][research_dias_2022]\] \[[Dias 2023][research_dias_2023]\] \[[Doko and Sasongko 2026][research_doko_sasongko_2026]\] \[[Dollyhigh 1970][research_dollyhigh_1970]\] \[[Donlan et al 1976][research_donlan_kemp_1976]\] \[[Dugan 1959][research_dugan_1959]\] \[[Duraffourg et al 2013][research_duraffourg_burlion_2013]\] \[[Dynamic Longitudinal Stability Flight 2003][research_dynamic_longitudinal_2003]\] \[[Dynamic Longitudinal Stability Theory 2003][research_dynamic_longitudinal_2003_b]\] \[[Eney 1969][research_eney_1969]\] \[[Eshelby 1982][research_eshelby_1982]\] \[[Eulrich and Mesiah 1974][research_eulrich_mesiah_1974]\] \[[Figat and Kwiek 2021][research_figat_kwiek_2021]\] \[[Fischel and Nugent 1953][research_fischel_nugent_1953]\] \[[González et al 2010][research_gonzalez_boschetti_2010]\] \[[Gosmann et al 2020][research_gosmann_gabrys_2020]\] \[[Greenberg and Sternfield 1944][research_greenberg_sternfield_1944]\] \[[Gunes et al 2025][research_gunes_sel_2025]\] \[[Gunes et al 2025][research_gunes_sel_2025_b]\] \[[Guo et al 1988][research_guo_wang_1988]\] \[[Harry and Trobaugh 1966][research_harry_trobaugh_1966]\] \[[Hunter and Reeder 1946][research_hunter_reeder_1946]\] \[[Irving 1966][research_irving_1966]\] \[[Irving 1966][research_irving_1966_b]\] \[[Ishihara et al 2010][research_ishihara_benmenahem_2010]\] \[[Ishola et al 2024][research_ishola_whidborne_2024]\] \[[Iskrenovic-Momcilovic 2018][research_iskrenovicmomcilovic_2018]\] \[[Jaiswal and Prakash 2022][research_jaiswal_prakash_2022]\] \[[Jansen and Vos 2016][research_jansen_vos_2016]\] \[[Jarmark and Speyer 1988][research_jarmark_speyer_1988]\] \[[Jenney 1935][research_jenney_1935]\] \[[Jiang et al 2025][research_jiang_guo_2025]\] \[[Johnson 1935][research_johnson_1935]\] \[[Johnson 1951][research_johnson_1951]\] \[[Johnson 1959][research_johnson_1959]\] \[[Johnson and Boisseau 1953][research_johnson_boisseau_1953]\] \[[Karahan 2026][research_karahan_2026]\] \[[Katzoff 1940][research_katzoff_1940]\] \[[Kemp et al 1950][research_kemp_becht_1950]\] \[[Khan and Bandyopadhyay][research_khan_bandyopadhyay]\] \[[Kimler and Canfield 2006][research_kimler_canfield_2006]\] \[[Kjelgaard and Paulson 1981][research_kjelgaard_paulson_1981]\] \[[Klausmeyer and Laflin 2023][research_klausmeyer_laflin_2023]\] \[[Kobayashi 2002][research_kobayashi_2002]\] \[[Laitone and Vinh 1970][research_laitone_vinh_1970]\] \[[Longitudinal Aircraft Dynamics and 2011][research_longitudinal_aircraft_2011]\] \[[Longitudinal Control and Trim 2003][research_longitudinal_control_2003]\] \[[Longitudinal Dynamics 1990][research_longitudinal_dynamics_1990]\] \[[Longitudinal Dynamics 1998][research_longitudinal_dynamics_1998]\] \[[Longitudinal Maneuvering Stability Theory 2003][research_longitudinal_maneuvering_2003]\] \[[Longitudinal Stability 2021][research_longitudinal_stability_2021]\] \[[Longitudinal Stability Fore 2014][research_longitudinal_stability_2014]\] \[[Longitudinal Trim and Stability 2016][research_longitudinal_trim_2016]\] \[[Maqsood and Go 2011][research_maqsood_go_2011]\] \[[McClelland and Woolsey 2020][research_mcclelland_woolsey_2020]\] \[[McFall 1954][research_mcfall_1954]\] \[[McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]\] \[[Mengali 2003][research_mengali_2003]\] \[[Mercer and Maiden 1972][research_mercer_maiden_1972]\] \[[Metcalf 1936][research_metcalf_1936]\] \[[Methods for Improving Longitudinal 2003][research_methods_for_2003]\] \[[Metodiev 2024][research_metodiev_2024]\] \[[Milenković-Babić 2018][research_milenkovicbabic_2018]\] \[[Milenković-Babić et al 2017][research_milenkovicbabic_samardzic_2017]\] \[[Mitcham et al 1951][research_mitcham_blanchard_1951]\] \[[Mitchell and Peck 1950][research_mitchell_peck_1950]\] \[[Mitiku et al 2024][research_mitiku_salau_2024]\] \[[Mohamed and Dongare 2021][research_mohamed_dongare_2021_b]\] \[[Mohammed et al 2013][research_mohammed_wu_2013]\] \[[Mohanty and swain 2025][research_mohanty_swain_2025]\] \[[Mooij 1985][research_mooij_1985_c]\] \[[Moseley and Taylor 1953][research_moseley_taylor_1953]\] \[[Sadoff and Sisk 1950][research_x4_longitudinal_1950]\] \[[Gillis and Mitchell 1957][research_freeflight_longitudinal_1957]\] \[[Neumark 1950][research_neumark_1950]\] \[[Newell and Campbell 1954][research_newell_campbell_1954]\] \[[Norton 1924][research_norton_1924]\] \[[Norton and Carroll 1922][research_norton_carroll_1922]\] \[[Nuthi and Subbarao 2014][research_nuthi_subbarao_2014]\] \[[Paranjape and Ananthkrishan 2005][research_paranjape_ananthkrishan_2005]\] \[[Paul O and Paul P 2019][research_paulo_paulp_2019]\] \[[Perkins 1959][research_perkins_1959]\] \[[Phillips 1942][research_phillips_shortperiod_1942]\] \[[Phunpeng et al 2023][research_phunpeng_khaengkarn_2023]\] \[[Predachenko and Lemko 2017][research_predachenko_lemko_2017]\] \[[Predachenko and Lemko 2019][research_predachenko_lemko_2019]\] \[[Prediction and Verification of 1985][research_prediction_and_1985]\] \[[Quitter et al 2023][research_quitter_marino_2023]\] \[[Rashad et al 2025][research_rashad_elbadawy_2025]\] \[[Rhudy 2016][research_rhudy_2016]\] \[[Roache 1965][research_roache_1965]\] \[[Rodgers 1964][research_rodgers_1964]\] \[[Rodgers 1965][research_rodgers_1965]\] \[[Rodgers 1966][research_rodgers_1966]\] \[[Rogers 2007][research_rogers_2007]\] \[[Romere and Chambliss 1972][research_romere_chambliss_1972]\] \[[Rosario-Gabriel and Cortes 2018][research_rosariogabriel_cortes_2018]\] \[[Russell 1996][research_russell_1996]\] \[[Sachs 1969][research_sachs_1969]\] \[[Sachs 1977][research_sachs_1977]\] \[[Sadoff et al 1961][research_sadoff_mcfadden_1961]\] \[[Sadoff et al 1954][research_sadoff_blunt_te_1954]\] \[[Sadraey 2022][research_sadraey_2022]\] \[[Sadraey 2022][research_sadraey_2022_b]\] \[[Schmidt et al 2025][research_schmidt_static_margin_2025]\] \[[Seckel 1964][research_seckel_1964]\] \[[Seckel 1964][research_seckel_1964_b]\] \[[Seraj and Martins 2025][research_seraj_martins_2025]\] \[[Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021]\] \[[Sisk and Mooney 1953][research_sisk_mooney_1953]\] \[[Skoog 1951][research_skoog_1951]\] \[[Sleeman and Byrnes 1953][research_sleeman_byrnes_1953]\] \[[Smith 1959][research_smith_1959]\] \[[Solies 1994][research_solies_1994]\] \[[Solies 1994][research_solies_1994_b]\] \[[Soule 1937][research_soule_1937]\] \[[Soule and Wheatley 1934][research_soule_wheatley_1934]\] \[[Spooner and Martina 1948][research_spooner_martina_1948]\] \[[Srinathkumar et al 1993][research_srinathkumar_madhuranath_1993]\] \[[Srinathkumar et al 1995][research_srinathkumar_parameswaran_1995]\] \[[Static Longitudinal Stability Flight 2003][research_static_longitudinal_2003]\] \[[Static Longitudinal Stability Theory 2003][research_static_longitudinal_2003_b]\] \[[Stephenson and Hardy 1989][research_stephenson_hardy_1989]\] \[[Swaim and Fullman 1977][research_swaim_fullman_1977]\] \[[Taboada et al 2018][research_taboada_boschetti_2018]\] \[[Tan et al 2025][research_tan_yang_2025]\] \[[Taylor 1952][research_taylor_1952]\] \[[The effects of aft-loaded 1989][research_the_effects_1989]\] \[[Ting and Ayoubi 2012][research_ting_ayoubi_2012]\] \[[Ting and Ayoubi 2013][research_ting_ayoubi_2013]\] \[[Trim and Longitudinal Static 2017][research_trim_and_2017]\] \[[Turn Performance and Maneuver 2021][research_turn_performance_2021]\] \[[Wang 2019][research_wang_aeroelastic_2019]\] \[[Wang et al 2025][research_wang_liu_2025]\] \[[Washizu and Osuga 1960][research_washizu_osuga_1960]\] \[[Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]\] \[[Whoric 1973][research_whoric_1973]\] \[[Xu 2012][research_xu_2012]\] \[[Zhang et al 2018][research_zhang_zhou_2018_b]\] \[[Zink et al 2000][research_zink_mavris_2000]\] \[[Zink et al 2001][research_zink_raveh_2001]\]

### Flight test, measurement and parameter identification

**How derivatives are got out of an aeroplane.** Flight test technique and its management, airspeed calibration, and the estimation of stability and control parameters from flight data, which has largely absorbed the hand-reduced decrement.

**190 records.** \[[Abbott et al 1977][research_abbott_boirun_1977]\] \[[Accelerated development and flight 1979][research_accelerated_development_1979]\] \[[Adams][research_adams]\] \[[Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]\] \[[Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]\] \[[Ahmed and Kandagal 2016][research_ahmed_kandagal_2016]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]\] \[[Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]\] \[[Aircraft instrument for indicating 1998][research_aircraft_instrument_1998]\] \[[Airspeed Calibration 2011][research_airspeed_calibration_2011]\] \[[Airspeed Calibration 2021][research_airspeed_calibration_2021]\] \[[Airspeed Calibration of a 2008][research_airspeed_calibration_2008]\] \[[Airspeed Definitions and Airspeed 2022][research_airspeed_definitions_2022]\] \[[Airspeed Systems Theory and 2003][research_airspeed_systems_2003]\] \[[Alatorre et al 2021][research_alatorre_castillo_2021]\] \[[Anderson and Vincent 1985][research_anderson_vincent_1985]\] \[[Ankenbruck et al 1951][research_ankenbruck_sadoff_1951]\] \[[Batterson and Klein 1984][research_batterson_klein_1984]\] \[[Berry 1985][research_berry_1985]\] \[[Berry 1986][research_berry_1986_b]\] \[[Bleimeyer 1981][research_bleimeyer_1981]\] \[[Brand 1981][research_brand_1981]\] \[[Brandon et al 1996][research_brandon_simon_1996]\] \[[Brandon et al 2001][research_brandon_lan_2001]\] \[[Brooks 1986][research_brooks_1986]\] \[[Brown and Bradley 1981][research_brown_bradley_1981]\] \[[Burton and Bischoff 1976][research_burton_bischoff_1976]\] \[[Campos 1989][research_campos_1989]\] \[[Carpenter et al 2018][research_carpenter_solomon_2018]\] \[[Chen and Valasek 1999][research_chen_valasek_1999]\] \[[Chen et al 2024][research_chen_li_2024]\] \[[Cooke 1980][research_cooke_1980]\] \[[Corda et al 1994][research_corda_stephenson_1994]\] \[[Crassidis 2005][research_crassidis_2005]\] \[[Curry and Sim 1982][research_curry_sim_1982]\] \[[Curry et al 1989][research_curry_moulton_1989]\] \[[Curry et al 1990][research_curry_moulton_1990]\] \[[Dabney 2012][research_dabney_2012]\] \[[Dawson and Maxwell 2003][research_dawson_maxwell_2003]\] \[[Dawson and Maxwell 2005][research_dawson_maxwell_2005]\] \[[Dean et al 2008][research_dean_morton_2008]\] \[[DeBusk et al 2009][research_debusk_johnson_2009]\] \[[Deepa and Gupta 2023][research_deepa_gupta_2023]\] \[[Denegri 2000][research_denegri_2000]\] \[[Development of a Continuous 2012][research_development_of_2012]\] \[[Devesa et al 2004][research_devesa_jourdan_2004]\] \[[Dicarlo et al 1992][research_dicarlo_brown_1992]\] \[[Effect of wind shear 1990][research_effect_of_1990]\] \[[Eulrich et al 1978][research_eulrich_govindaraj_1978]\] \[[Fechter and Mills 1988][research_fechter_mills_1988]\] \[[Finch and Matranga 1959][research_finch_matranga_1959]\] \[[Fisher et al 1976][research_fisher_stough_1976]\] \[[Fletcher 1994][research_fletcher_1994]\] \[[Flight TEST Manual 1959][research_flight_test_1959]\] \[[Flight test results for 1977][research_flight_test_1977]\] \[[Flight Test Results Pertaining 1970][research_flight_test_1970]\] \[[Foch 1992][research_foch_1992]\] \[[Freuler and Hoffmann 1977][research_freuler_hoffmann_1977]\] \[[Gardner 1951][research_gardner_1951]\] \[[Garman and Andrisani 2003][research_garman_andrisani_2003]\] \[[Gee 1978][research_gee_1978]\] \[[Gera 1986][research_gera_1986]\] \[[Gilyard 1972][research_gilyard_1972]\] \[[Gratton 2007][research_gratton_2007]\] \[[Grauer and Morelli 2023][research_grauer_morelli_2023]\] \[[Hall 1971][research_hall_1971]\] \[[Hamel and Jategaonkar 1996][research_hamel_jategaonkar_1996]\] \[[Harris et al 2016][research_harris_arthurs_2016]\] \[[Hart 1992][research_hart_1992]\] \[[Hockman and Eisiminger 1948][research_hockman_eisiminger_1948]\] \[[Hollister 1990][research_hollister_1990]\] \[[Hosseini et al 2025][research_hosseini_hofmann_2025]\] \[[Huang and Cummings 2021][research_huang_cummings_2021]\] \[[Hull and Roger 1975][research_hull_roger_1975]\] \[[Hulshoff et al 1996][research_hulshoff_mulder_1996]\] \[[Huston 1948][research_huston_1948]\] \[[Ikard 1956][research_ikard_1956]\] \[[Iliff and Maine 1982][research_iliff_maine_1982]\] \[[Introduction to Stability and 2003][research_introduction_to_2003]\] \[[Iwakawa et al 2015][research_iwakawa_furukawa_2015]\] \[[Jategaonkar 2005][research_jategaonkar_2005]\] \[[Jategaonkar et al 2004][research_jategaonkar_fischenberg_2004]\] \[[Johnson 1937][research_johnson_1937]\] \[[Jurado and McGehee 2019][research_jurado_mcgehee_2019]\] \[[Kaletka and Fu 1993][research_kaletka_fu_1993]\] \[[Kamal et al 2015][research_kamal_aly_2015]\] \[[Kelly 1988][research_kelly_1988]\] \[[Kimberlin and Sims 1992][research_kimberlin_sims_1992]\] \[[Klein 1979][research_klein_1979]\] \[[Kong et al 2023][research_kong_pan_2023]\] \[[Koven and Kayten 1946][research_koven_kayten_1946]\] \[[Kuehme et al 2014][research_kuehme_alley_2014]\] \[[Kurtz et al 2016][research_kurtz_wittig_2016]\] \[[Lawrence and Draper-Donley 2005][research_lawrence_draperdonley_2005]\] \[[Lichota 2016][research_lichota_2016]\] \[[Lichota 2023][research_lichota_2023]\] \[[Lichota et al 2016][research_lichota_ohme_2016]\] \[[Lichter et al 2009][research_lichter_bateman_2009]\] \[[Lina and Ricker 1952][research_lina_ricker_1952]\] \[[Long 1968][research_long_1968]\] \[[Lu and Van Kampen 2015][research_lu_vankampen_2015]\] \[[Maine and Iliff 1979][research_maine_iliff_1979]\] \[[Martinez 1961][research_martinez_1961]\] \[[Martos et al 2011][research_martos_kiszely_2011]\] \[[Marwaha et al 2008][research_marwaha_valasek_2008]\] \[[Matranga 1961][research_matranga_1961_b]\] \[[McCarty 1982][research_mccarty_1982]\] \[[McCracken and Jorris 2011][research_mccracken_jorris_2011]\] \[[Measuring Airspeed 2021][research_measuring_airspeed_2021]\] \[[Milne and Martos 2012][research_milne_martos_2012]\] \[[Moes et al 2000][research_moes_noffz_2000]\] \[[Moes et al 2003][research_moes_smith_2003]\] \[[Mohamed and Dongare 2021][research_mohamed_dongare_2021_c]\] \[[Morelli 2000][research_morelli_2000]\] \[[Morelli 2002][research_morelli_2002]\] \[[Morelli 2021][research_morelli_2021]\] \[[Morelli 2021][research_morelli_2021_b]\] \[[Morelli and Grauer 2018][research_morelli_grauer_2018]\] \[[Moszczynski and Grant 2017][research_moszczynski_grant_2017]\] \[[Munger et al 1983][research_munger_carlin_1983]\] \[[Murphy and Klein 2008][research_murphy_klein_2008]\] \[[Murri et al 1984][research_murri_nguyen_1984]\] \[[Muzzey and Kidd 1959][research_muzzey_kidd_1959]\] \[[Walker 1997][research_x36_test_pilot_1997]\] \[[Nelson][research_nelson]\] \[[Newell et al 1963][research_newell_dolbin_1963]\] \[[Nusrath et al 2014][research_nusrath_sarmah_2014]\] \[[Owens et al 2019][research_owens_beeler_2019]\] \[[Paris and Alaverdi 1998][research_paris_alaverdi_1998]\] \[[Park 2017][research_park_2017]\] \[[Parks and Wingrove 1980][research_parks_wingrove_1980]\] \[[Pawlak 1994][research_pawlak_1994]\] \[[Plaetschke and Weiss 1988][research_plaetschke_weiss_1988]\] \[[Putnam and Ayers 1989][research_putnam_ayers_1989]\] \[[Quigley et al 1960][research_quigley_anderson_1960]\] \[[Raol and Singh 2023][research_raol_singh_2023]\] \[[Redeker and Voersmann 1988][research_redeker_voersmann_1988]\] \[[Rediess and Melton 1994][research_rediess_melton_1994]\] \[[Reed and Clay 1937][research_reed_clay_1937]\] \[[Rhoads 1970][research_rhoads_1970]\] \[[Day 1953][research_richardeday_1953]\] \[[Roberts 1963][research_roberts_1963]\] \[[Roberts 1988][research_roberts_1988_b]\] \[[Ross 1972][research_ross_1972]\] \[[Ross 1972][research_ross_1972_b]\] \[[Row and Fischel 1963][research_row_fischel_1963]\] \[[Rubio-Sierra et al 2022][research_rubiosierra_delgado_2022]\] \[[Runckel and Henderson 1952][research_runckel_henderson_1952]\] \[[Sadoff and Sisk 1950][research_sadoff_sisk_1950]\] \[[Sanderson 1965][research_sanderson_1965]\] \[[Sarkar and Panneerselvam 1998][research_sarkar_panneerselvam_1998]\] \[[Sarkar et al 2009][research_sarkar_ananthasayanam_2009]\] \[[Schierbrock and Takahashi 2021][research_schierbrock_takahashi_2021]\] \[[Schumacher 1952][research_schumacher_1952]\] \[[Schweikhard 1966][research_schweikhard_1966]\] \[[Schweikhard 1967][research_schweikhard_1967]\] \[[Anderson 1992][research_sethbanderson_1992]\] \[[Shafer 1991][research_shafer_1991]\] \[[Shafer 1992][research_shafer_1992]\] \[[Shafer 1994][research_shafer_1994]\] \[[Sim 1973][research_sim_1973]\] \[[Sim 1997][research_sim_1997]\] \[[Simmons et al 2023][research_simmons_sysid_2023]\] \[[Simulation in support of 1988][research_simulation_in_1988]\] \[[Sklenář and Matějů 2022][research_sklenar_mateju_2022]\] \[[Song et al 1995][research_song_jeon_1995]\] \[[Talmage and Reeder 1947][research_talmage_reeder_1947]\] \[[Taylor 2012][research_taylor_2012]\] \[[Trankle and Rabin 1983][research_trankle_rabin_1983]\] \[[Vallone][research_vallone]\] \[[Van Pelt 1981][research_vanpelt_1981]\] \[[Van Thullenar 1957][research_vanthullenar_1957]\] \[[Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]\] \[[Vincent and Franklin 1981][research_vincent_franklin_1981]\] \[[Wang et al 2020][research_wang_yin_2020]\] \[[Wheldon and Whites 1966][research_wheldon_whites_1966]\] \[[Drake and Williams 1958][research_williams_drake_1948]\] \[[Willig 1968][research_willig_1968]\] \[[Winn and Kishi 1972][research_winn_kishi_1972]\] \[[Wolkovitch 1984][research_wolkovitch_1984]\] \[[Wu and Liu 2021][research_wu_liu_2021]\] \[[Yavuztürk et al 2017][research_yavuzturk_topbas_2017]\] \[[Zaheer and Ajmal 2019][research_zaheer_ajmal_2019]\] \[[Zhang and Yang 2024][research_zhang_yang_2024]\] \[[Zhubin and Ruikun 2023][research_zhubin_ruikun_2023]\] \[[Zou and Li 2005][research_zou_li_2005]\]

### The horizontal tail, downwash and the wing wake

**The surface the X-4 left off.** Downwash and the wing wake at the tail, tail loads and buffet, tail sizing and tail effectiveness. **The titles measure the tail's flow and its loads far more often than its share of the damping**, which Thin Subjects below counts.

**166 records.** \[[Faraj and Mohammed 2008][research_afaraj_mmohammed_2008]\] \[[Adams and Silsby 1947][research_adams_silsby_1947]\] \[[Aircraft Stability Characteristics in 2021][research_aircraft_stability_2021]\] \[[Allen 1951][research_allen_1951]\] \[[Altunkaya and Ozkol 2022][research_altunkaya_ozkol_2022]\] \[[Asher et al 1957][research_asher_martuccelli_1957]\] \[[Bare et al 1981][research_bare_berrier_1981]\] \[[Benjamin et al 2021][research_benjamin_hesse_2021]\] \[[Benyamen et al 2020][research_benyamen_mckinnis_2020]\] \[[Biriukov 1959][research_biriukov_1959]\] \[[Blaesser and Frederick 2020][research_blaesser_frederick_2020]\] \[[Bland and Young 1961][research_bland_young_1961]\] \[[Bon 2021][research_bon_2021]\] \[[Bryant 1950][research_bryant_1950]\] \[[Burkhalter 1993][research_burkhalter_1993]\] \[[Burkhalter et al 1992][research_burkhalter_spring_1992]\] \[[Burnham 1995][research_burnham_1995]\] \[[Butler 1982][research_butler_1982]\] \[[Calderon et al 2012][research_calderon_aupoix_2012]\] \[[Capone et al 1983][research_capone_mason_1983]\] \[[Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]\] \[[Chen and Lee 2008][research_chen_lee_2008]\] \[[Chen et al 2025][research_chen_zhang_2025_b]\] \[[Cooney and Schott 1956][research_cooney_schott_1956]\] \[[Coppolino 1952][research_coppolino_1952]\] \[[Correia et al 2009][research_correia_silva_2009]\] \[[Dandwani et al 2025][research_dandwani_bragadoaldana_2025]\] \[[Davis 1952][research_davis_1952]\] \[[Davis 1969][research_davis_1969]\] \[[Decker 1951][research_decker_1951]\] \[[Decker 1952][research_decker_1952]\] \[[Dingeldein 1944][research_dingeldein_1944]\] \[[Dodd and Pratt 1970][research_dodd_pratt_1970]\] \[[Dodd and Pratt 1971][research_dodd_pratt_1971]\] \[[Draper 1943][research_draper_1943]\] \[[Driver and Spearman 1959][research_driver_spearman_1959]\] \[[English 1955][research_english_1955]\] \[[English 1955][research_english_1955_b]\] \[[English 1957][research_english_1957]\] \[[Etkin 1952][research_etkin_1952]\] \[[Fisher 1954][research_fisher_1954]\] \[[Fisher and Williams 1958][research_fisher_williams_1958]\] \[[Furlong 1948][research_furlong_1948]\] \[[Gamble and Inman 2018][research_gamble_inman_2018]\] \[[Garcia et al 2001][research_garcia_slingerland_2001]\] \[[Gomec et al 2020][research_gomec_unver_2020]\] \[[Guiler][research_guiler]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]\] \[[Hallissy 1956][research_hallissy_1956]\] \[[Han et al 2023][research_han_liu_2023]\] \[[Herdiana et al 2024][research_herdiana_pinindriya_2024]\] \[[Hitachi and Liu 2010][research_hitachi_liu_2010]\] \[[Hoang and Bui 2019][research_hoang_bui_2019]\] \[[Hoang and Bui 2019][research_hoang_bui_2019_b]\] \[[Hoff and Gratton 2013][research_hoff_gratton_2013]\] \[[Horizontal Tail Loads 1996][research_horizontal_tail_1996]\] \[[Hwang and Pi 1979][research_hwang_pi_1979]\] \[[Initial Tail Sizing 2013][research_initial_tail_2013]\] \[[Irving 1966][research_irving_1966_c]\] \[[Ishida and Ueshima 2026][research_ishida_ueshima_2026]\] \[[Isogai 2016][research_isogai_2016]\] \[[Jacobs and Bartlett 1981][research_jacobs_bartlett_1981]\] \[[Johnson 1948][research_johnson_1948]\] \[[Jones and Fehlner 1940][research_jones_fehlner_1940]\] \[[Kaminer et al 1996][research_kaminer_howard_1996]\] \[[Karthik et al 1999][research_karthik_tulapurkara_1999]\] \[[Karunanidhi et al 2022][research_karunanidhi_scholz_2022]\] \[[Katzoff and Sweberg 1942][research_katzoff_sweberg_1942]\] \[[Kentfield 2006][research_kentfield_2006]\] \[[Kentfield 2009][research_kentfield_2009]\] \[[Kentfield and Spragins 2004][research_kentfield_spragins_2004]\] \[[Khan 2019][research_khan_2019]\] \[[Khan et al 2026][research_khan_masud_2026]\] \[[Kidd 1988][research_kidd_1988]\] \[[Kier et al 2020][research_kier_muller_2020]\] \[[Kim and Marciniak 1999][research_kim_marciniak_1999]\] \[[Kim and Marciniak 2002][research_kim_marciniak_2002]\] \[[Kleckner 1943][research_kleckner_1943]\] \[[Kleckner 1943][research_kleckner_1943_b]\] \[[Klein 1999][research_klein_1999]\] \[[Kleinert et al 2023][research_kleinert_ehrle_2023]\] \[[Kornev and Pimenov 2022][research_kornev_pimenov_2022]\] \[[Kroo 1983][research_kroo_1983]\] \[[Laitone 1978][research_laitone_1978]\] \[[Laitone 1978][research_laitone_1978_b]\] \[[Lapin et al 1952][research_lapin_crookshanks_1952]\] \[[Laurence Le Page 1925][research_laurencelepage_1925]\] \[[Liu 2024][research_liu_2024]\] \[[Liu and Elham 2019][research_liu_elham_2019]\] \[[Loechert et al 2018][research_loechert_huber_2018]\] \[[Luoma 1953][research_luoma_1953]\] \[[Mohammed 2015][research_mohammed_2015]\] \[[Montano et al 2024][research_montano_dimino_2024]\] \[[Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]\] \[[Morra and Nicolosi 2025][research_morra_nicolosi_2025]\] \[[Musa et al 2015][research_musa_mansor_2015]\] \[[Musa et al 2026][research_musa_mansor_2026]\] \[[Bird et al 1951][research_fuselage_tail_yawing_1951]\] \[[Lichtenstein 1952][research_tail_size_effect_1952]\] \[[Nallapula et al 2012][research_nallapula_schade_2012]\] \[[Neely and Griner 1959][research_neely_griner_1959]\] \[[Ness 1971][research_ness_1971]\] \[[Nicholas et al 1984][research_nicholas_naville_1984]\] \[[Nie et al 2026][research_nie_zhang_2026]\] \[[Nie et al 2026][research_nie_zhang_2026_b]\] \[[Nissen 1943][research_nissen_1943]\] \[[OBrien and Takahashi 2024][research_obrien_takahashi_2024]\] \[[Park and Abla 1982][research_park_abla_1982]\] \[[Park and Abla 1983][research_park_abla_1983]\] \[[Paziresh et al 2017][research_paziresh_nikseresht_2017]\] \[[Perry 1976][research_perry_1976]\] \[[Phillips et al 2002][research_phillips_anderson_2002]\] \[[Polamus and Spreemann 1961][research_polamus_spreemann_1961]\] \[[Preliminary Sizing of the 2010][research_preliminary_sizing_2010]\] \[[Prior et al 2023][research_prior_rozinka_2023]\] \[[Purser and Spear 1947][research_purser_spear_1947]\] \[[Qiu and Sun 2009][research_qiu_sun_2009]\] \[[Queijo and Wolhart 1951][research_queijo_wolhart_1951]\] \[[Queijo et al 1954][research_queijo_fences_1954]\] \[[Rainey and Igoe 1958][research_rainey_igoe_1958]\] \[[Reed 1955][research_reed_1955]\] \[[Rhoads 1952][research_rhoads_1952]\] \[[Rostami et al 2021][research_rostami_chung_2021]\] \[[Schauerte and Schreyer 2024][research_schauerte_schreyer_2024]\] \[[Schmitt et al 1990][research_schmitt_reneaux_1990]\] \[[Schnurbusch 1944][research_schnurbusch_1944]\] \[[Schnurbusch 1945][research_schnurbusch_1945]\] \[[Scholz 2021][research_scholz_2021]\] \[[Schuldenfrei et al 1947][research_schuldenfrei_1947]\] \[[Shamikh 2013][research_shamikh_2013]\] \[[Shams Taleghani et al 2020][research_shamstaleghani_ghajar_2020]\] \[[Shao et al 2026][research_shao_meng_2026]\] \[[Shevell 1978][research_shevell_1978]\] \[[Shmilovich and Caughey][research_shmilovich_caughey]\] \[[Shmilovich and Caughey 1985][research_shmilovich_caughey_1985]\] \[[Silvers et al 1958][research_silvers_fournier_1958]\] \[[Singhasenee et al 2026][research_singhasenee_lamon_2026]\] \[[Slingerland 2002][research_slingerland_2002]\] \[[Slingerland 2005][research_slingerland_2005]\] \[[Spearman et al 1956][research_spearman_robinson_1956]\] \[[Stability and control of 1986][research_stability_and_1986]\] \[[Stegmüller et al 2022][research_stegmuller_katzenmeier_2022]\] \[[Stephenson et al 1955][research_stephenson_selan_1955]\] \[[Summey and Smetana 1977][research_summey_smetana_1977]\] \[[Swaim 1980][research_swaim_1980]\] \[[Sweberg 1942][research_sweberg_1942]\] \[[Sweberg 1945][research_sweberg_1945]\] \[[Tan et al 2017][research_tan_wang_2017]\] \[[Tan et al 2018][research_tan_wang_2018]\] \[[Tang and Dowell 2013][research_tang_dowell_2013]\] \[[Teperin et al 2018][research_teperin_teperina_2018]\] \[[Thompson and Gilruth 1940][research_thompson_gilruth_1940]\] \[[Urie and Reaser 1979][research_urie_reaser_1979]\] \[[van Arnhem et al 2019][research_vanarnhem_devries_2019]\] \[[Vertical Tail Loads 1996][research_vertical_tail_1996]\] \[[Vianto et al 2021][research_vianto_tobing_2021]\] \[[Wakefield 1959][research_wakefield_1959]\] \[[Waldmann et al 2019][research_waldmann_lutz_2019]\] \[[Ward 1949][research_ward_1949]\] \[[Wetzel 1954][research_wetzel_1954]\] \[[Wilmott 1986][research_wilmott_1986]\] \[[Xie et al 2023][research_xie_cai_2023]\] \[[Xie et al 2022][research_xie_cai_2022]\] \[[Young 1961][research_young_1961]\] \[[Yurkovich 1996][research_yurkovich_1996]\]

### Pilot-induced oscillation and the pilot in the loop

**The closed loop that turns light damping into hunting.** Pilot models, pilot-induced oscillation and its prediction, detection and suppression. **Actuator rate limiting is the recurring named cause from the 1990s on**, which is the nonlinear route into oscillation this article's augmentation section writes down.

**165 records.** \[[A comparative study of 2015][research_a_comparative_2015]\] \[[Adams 1972][research_adams_1972]\] \[[Adams 1978][research_adams_1978]\] \[[Adams 1980][research_adams_1980]\] \[[Ali 1997][research_ali_1997]\] \[[Andreea-Irina and Achim 2014][research_andreeairina_achim_2014]\] \[[Bachelder and Aponso 2022][research_bachelder_aponso_2022]\] \[[Bachelder and Aponso 2023][research_bachelder_aponso_2023_c]\] \[[Bailey and Smith 1982][research_bailey_smith_1982]\] \[[Bechelder et al 2025][research_bechelder_bjorkman_2025]\] \[[Benoit et al 2014][research_benoit_verbeke_2014]\] \[[Bidinotto et al 2021][research_bidinotto_2021]\] \[[Boskovic and Mehra][research_boskovic_mehra]\] \[[Brauser 1982][research_brauser_1982]\] \[[Brauser 1983][research_brauser_1983]\] \[[Broussard and Stengel 1977][research_broussard_stengel_1977]\] \[[Brutch and Moncayo 2024][research_brutch_moncayo_2024]\] \[[Cameron et al 2003][research_cameron_thomson_2003]\] \[[Control Characteristics of the 2023][research_control_characteristics_2023]\] \[[Cooper et al 2021][research_cooper_klyde_2021]\] \[[Craun et al 2013][research_craun_acosta_2013]\] \[[Craun et al 2013][research_craun_acosta_2013_b]\] \[[Dantzig 1975][research_dantzig_1975]\] \[[Deppe et al 1996][research_deppe_chalk_1996]\] \[[DiFranco 1967][research_difranco_1967]\] \[[Dogan and Kaewchay 2007][research_dogan_kaewchay_2007]\] \[[Doman 1995][research_doman_1995]\] \[[Efremov et al 2020][research_efremov_2020]\] \[[Efremov et al 2022][research_efremov_shcherbakov_2022]\] \[[Eichler 1970][research_eichler_1970]\] \[[Ema et al 1997][research_ema_mizukura_1997]\] \[[Erturk et al 2022][research_erturk_ozkan_2022]\] \[[Fasiello et al 2019][research_fasiello_lu_2019]\] \[[Fu et al 2021][research_fu_yu_2021]\] \[[Gatley et al 2006][research_gatley_turner_2006]\] \[[Gilbreath and Markofski 2001][research_gilbreath_markofski_2001]\] \[[Green 1988][research_green_1988]\] \[[Habboush and Yildiz 2022][research_habboush_yildiz_2022]\] \[[Han and Liu 2026][research_han_liu_2026]\] \[[Hanke 2003][research_hanke_2003]\] \[[Hart and Hartzell 1984][research_hart_hartzell_1984]\] \[[Hess][research_hess]\] \[[Hess 1977][research_hess_1977]\] \[[Hess 1979][research_hess_1979]\] \[[Hess 1980][research_hess_1980]\] \[[Hess 1982][research_hess_1982]\] \[[Hess 1987][research_hess_1987]\] \[[Hess 1994][research_hess_1994]\] \[[Hess 1995][research_hess_1995]\] \[[Hess 1997][research_hess_1997]\] \[[Hess 2011][research_hess_2011]\] \[[Hess 2016][research_hess_2016_b]\] \[[Hess and Hess 1997][research_hess_hess_1997]\] \[[Hess and Stout 1997][research_hess_stout_1997]\] \[[Hirsch and McCormick 1965][research_hirsch_mccormick_1965]\] \[[Hirsch and McCORMICK 1966][research_hirsch_mccormick_1966]\] \[[Iloputaife and Iloputaife 1997][research_iloputaife_iloputaife_1997]\] \[[Jado-Puente et al 2025][research_jadopuente_brutch_2025]\] \[[Jalovecký and Janů 2010][research_jalovecky_janu_2010]\] \[[Jeram and Prasad 2003][research_jeram_prasad_2003]\] \[[Jeram and Prasad 2003][research_jeram_prasad_2003_b]\] \[[Karasinski and Robinson 2022][research_karasinski_robinson_2022]\] \[[Katayanagi 2001][research_katayanagi_2001]\] \[[Katayanagi 2004][research_katayanagi_2004]\] \[[Kempel 1971][research_kempel_1971]\] \[[Kendall 2005][research_kendall_2005]\] \[[Kish et al 1996][research_kish_leggett_1996]\] \[[Kish et al 1997][research_kish_mosle_1997]\] \[[Kish et al 1997][research_kish_mosle_1997_b]\] \[[Klyde and Mitchell 1999][research_klyde_mitchell_1999]\] \[[Klyde and Mitchell 2003][research_klyde_mitchell_2003]\] \[[Klyde and Mitchell 2004][research_klyde_mitchell_2004]\] \[[Klyde et al 1996][research_klyde_mcruer_1996]\] \[[Klyde et al 1997][research_klyde_mcruer_1997]\] \[[Klyde et al 2002][research_klyde_smith_2002]\] \[[Klyde et al 2020][research_klyde_schulze_2020]\] \[[Lee and Vining 2018][research_lee_vining_2018]\] \[[Legouis et al 1986][research_legouis_laneville_1986]\] \[[Leonard 2013][research_leonard_2013]\] \[[Levi and Nelson 1963][research_levi_nelson_1963]\] \[[Levi and Nelson 1964][research_levi_nelson_1964]\] \[[Li et al 2013][research_li_xu_2013]\] \[[Li et al 2014][research_li_qu_2014]\] \[[Liang Qu et al 2016][research_liangqu_yinghui_2016]\] \[[Liebst et al 2002][research_liebst_chapa_2002]\] \[[Liu and Gao 2010][research_liu_gao_2010]\] \[[Liu and Lone 2013][research_liu_lone_2013]\] \[[Lu and Jump 2014][research_lu_jump_2014]\] \[[Malaek and Sajjadi Kia 2004][research_malaek_sajjadikia_2004]\] \[[Mandal][research_mandal]\] \[[Mandal and Gu 2016][research_mandal_gu_2016]\] \[[Markofski and Bailey 1999][research_markofski_bailey_1999]\] \[[Martinez-Garcia et al 2017][research_martinezgarcia_gordon_2017]\] \[[McKay 1994][research_mckay_1994]\] \[[McRuer 1965][research_mcruer_1965]\] \[[McRuer 1995][research_mcruer_1995]\] \[[Mitchell 2000][research_mitchell_2000]\] \[[Mitchell and Klyde 2008][research_mitchell_klyde_2008]\] \[[Mitchell et al][research_mitchell_kish]\] \[[Mitchell et al 1992][research_mitchell_aponso_1992]\] \[[Mooij 1985][research_mooij_1985_f]\] \[[Muralidharan et al 1979][research_muralidharan_baron_1979]\] \[[Newton and Kroo 2023][research_newton_kroo_2023]\] \[[Newton and Kroo 2024][research_newton_kroo_2024]\] \[[Newton and Kroo 2025][research_newton_kroo_2025]\] \[[Nguyen and Cord 1999][research_nguyen_cord_1999]\] \[[Nguyen et al 1997][research_nguyen_cord_1997]\] \[[Nguyen et al 2021][research_nguyen_saturation_pio_2021]\] \[[Onstott and Faulkner 1978][research_onstott_faulkner_1978]\] \[[Portapas and Cooke 2020][research_portapas_2020]\] \[[Powers 1980][research_powers_1980]\] \[[Powers 1982][research_powers_1982]\] \[[Powers 1984][research_powers_1984]\] \[[Powers 1986][research_powers_1986_b]\] \[[Quan 2013][research_quan_2013]\] \[[Aharrah 1995][research_ralphaaharrah_1995]\] \[[Repperger et al 1997][research_repperger_koivo_1997]\] \[[Rezaei and Khosravi 2023][research_rezaei_khosravi_2023]\] \[[Rzucidlo and Tomczyk 2007][research_rzucidlo_tomczyk_2007]\] \[[Saetti and Rogers 2020][research_saetti_rogers_2020]\] \[[Schmidt 1983][research_schmidt_1983]\] \[[Schroeder 2001][research_schroeder_2001]\] \[[Schroeder and Chung 2000][research_schroeder_chung_2000]\] \[[Schroeder et al 1998][research_schroeder_chung_1998]\] \[[Schroeder et al 2001][research_schroeder_chung_2001]\] \[[Schwithal et al 2025][research_schwithal_wallace_2025]\] \[[Shafer and Steinmetz 2001][research_shafer_steinmetz_2001]\] \[[Shafer and Steinmetz 2001][research_shafer_steinmetz_2001_b]\] \[[Shafer et al 1983][research_shafer_smith_1983]\] \[[Shafer et al 1984][research_shafer_smith_1984]\] \[[Shams][research_shams]\] \[[Shams et al 2026][research_shams_khouli_2026]\] \[[Shams et al 2023][research_shams_khouli_2023]\] \[[Sinacori 1986][research_sinacori_1986]\] \[[Smith 1979][research_smith_1979]\] \[[Smith 1981][research_smith_1981]\] \[[Smith 1982][research_smith_1982]\] \[[Smith and Berry 1975][research_smith_berry_1975]\] \[[Smith and Edwards 1980][research_smith_edwards_1980]\] \[[Tan et al 2014][research_tan_wu_2014]\] \[[Tohidi and Yildiz 2019][research_tohidi_yildiz_2019]\] \[[Tohidi et al 2018][research_tohidi_yildiz_2018]\] \[[Tokutake et al 2006][research_tokutake_fujinaga_2006]\] \[[Tokutake et al 2008][research_tokutake_fujinaga_2008]\] \[[Tousi et al 1988][research_tousi_bajaj_1988]\] \[[Tran et al 2017][research_tran_sakamoto_2017]\] \[[Twisdale and Kirsten 1984][research_twisdale_kirsten_1984]\] \[[Uybarreta et al 2024][research_uybarreta_kabaliuk_2024]\] \[[Valentin 2011][research_valentin_2011]\] \[[Wang et al 2012][research_wang_santone_2012]\] \[[Weltz et al 2007][research_weltz_shweyk_2007]\] \[[Wenqian et al 2010][research_wenqian_efremov_2010]\] \[[Witte et al 2003][research_witte_monson_2003]\] \[[Wu and Perng 2004][research_wu_perng_2004]\] \[[Xu et al 2019][research_xu_pio_2019]\] \[[Yildiz and Kolmanovsky 2010][research_yildiz_kolmanovsky_2010]\] \[[Yildiz et al 2011][research_yildiz_kolmanovsky_2011]\] \[[Yin and Wang 2017][research_yin_wang_2017]\] \[[Yin et al 2019][research_yin_wang_2019]\] \[[Yu and Liu 2013][research_yu_liu_2013]\] \[[Zaal 2016][research_zaal_2016]\] \[[Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]\] \[[Zeyada et al 1998][research_zeyada_hess_1998]\] \[[Zeyada et al 1999][research_zeyada_hess_1999]\] \[[Ünen and Yıldız 2025][research_unen_yildiz_2025]\]

### Pitch damping and the dynamic stability derivatives

**The keystone derivative and its relatives.** Damping in pitch, roll and yaw and the estimation of stability derivatives from tunnel and flight. **The titles measure or estimate the derivative for a whole configuration and seldom divide it between wing and tail**, which is the division this article's argument rests on.

**154 records.** \[[Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]\] \[[Albisser et al 2014][research_albisser_dobre_2014]\] \[[Anton et al 2009][research_anton_botez_2009]\] \[[APPENDICES A. Stability Derivatives 1990][research_appendices_a_1990]\] \[[Appendix C Stability and 2021][research_appendix_c_2021]\] \[[Approximate Expressions for the 1997][research_approximate_expressions_1997]\] \[[Approximate Expressions for the 2007][research_approximate_expressions_2007]\] \[[Approximate Expressions for the 2013][research_approximate_expressions_2013]\] \[[Averett and Wright 1966][research_averett_wright_1966]\] \[[Babcock and Arena 2004][research_babcock_arena_2004]\] \[[Babister 1980][research_babister_1980_b]\] \[[Beldica and Hilton 1999][research_beldica_hilton_1999]\] \[[Bennett and Johnson 1947][research_bennett_johnson_1947]\] \[[Biber 2017][research_biber_2017]\] \[[Bielat and Wiley 1959][research_bielat_wiley_1959]\] \[[Bird and Jaquet 1951][research_bird_jaquet_1951]\] \[[Blake 1993][research_blake_1993]\] \[[Brower and Wright 1966][research_brower_wright_1966]\] \[[Brown and Adams 1948][research_brown_adams_1948]\] \[[Bryson 1954][research_bryson_1954]\] \[[Buenz et al 1975][research_buenz_brooks_1975]\] \[[Bull and Kidd 1955][research_bull_kidd_1955]\] \[[Bunescu et al 2024][research_bunescu_stoican_2024]\] \[[Butler 1976][research_butler_1976]\] \[[Cavanaugh 2003][research_cavanaugh_2003]\] \[[Chalk 1983][research_chalk_1983]\] \[[Champine et al 1958][research_champine_kraft_1958]\] \[[Chang et al 2004][research_chang_cho_2004]\] \[[Cook 1997][research_cook_1997_c]\] \[[Cook 2007][research_cook_2007_c]\] \[[Cook 2013][research_cook_2013_c]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]\] \[[Cotter 1946][research_cotter_1946]\] \[[D'Aiutolo 1954][research_daiutolo_1954]\] \[[D'Aiutolo and Parker 1952][research_daiutolo_parker_1952]\] \[[Damveld 2004][research_damveld_2004]\] \[[Danowsky et al 2008][research_danowsky_thompson_2008]\] \[[Definitions of Aerodynamic Stability 1997][research_definitions_of_1997]\] \[[Definitions of Aerodynamic Stability 2007][research_definitions_of_2007]\] \[[Definitions of Aerodynamic Stability 2013][research_definitions_of_2013]\] \[[Effect of sting plunging 1978][research_effect_of_1978]\] \[[Emerson and Robinson 1958][research_emerson_robinson_1958]\] \[[Ericsson 1980][research_ericsson_1980]\] \[[Falkner 1951][research_falkner_1951]\] \[[Favaregh and Landman 2006][research_favaregh_landman_2006]\] \[[Franzmann et al 2021][research_franzmann_leopold_2021]\] \[[Franzmann et al 2022][research_franzmann_leopold_2022]\] \[[Franzmann et al 2022][research_franzmann_leopold_2022_b]\] \[[Gatto 2009][research_gatto_2009]\] \[[Gatto and Lowenberg 2006][research_gatto_lowenberg_2006]\] \[[Gillard 1998][research_gillard_1998]\] \[[Gilyard 1973][research_gilyard_1973]\] \[[Green 2008][research_green_2008]\] \[[Guglieri and Quagliotti 1993][research_guglieri_quagliotti_1993]\] \[[Guo and Ren 2015][research_guo_ren_2015]\] \[[Hall et al 1972][research_hall_sholar_1972]\] \[[Hanson et al 2011][research_hanson_schaefer_2011]\] \[[Holgate and Roskam 1968][research_holgate_roskam_1968]\] \[[Holowicz and Holleman 1958][research_holowicz_holleman_1958]\] \[[Iliff and Powers 1969][research_iliff_powers_1969]\] \[[Iliff and Wang 1996][research_iliff_wang_1996]\] \[[Iliff and Wang 1997][research_iliff_wang_1997]\] \[[Iliff and Wang 1999][research_iliff_wang_1999]\] \[[Jenkins 1989][research_jenkins_1989]\] \[[Kaattari 1959][research_kaattari_1959]\] \[[Kaye][research_kaye]\] \[[Kemp and Becht 1953][research_kemp_becht_1953]\] \[[Khan et al 2025][research_khan_shaikh_2025]\] \[[Kilgore and Adcock 1972][research_kilgore_adcock_1972]\] \[[Kirschstein and Alles 2004][research_kirschstein_alles_2004]\] \[[Klausmeyer 2018][research_klausmeyer_2018]\] \[[Klausmeyer 2026][research_klausmeyer_2026]\] \[[Klawans and White 1957][research_klawans_white_1957]\] \[[Kumar and Ghosh 2014][research_kumar_ghosh_2014]\] \[[Kumar and Ghosh 2023][research_kumar_ghosh_2023]\] \[[Kumar and Rao 2004][research_kumar_rao_2004]\] \[[Kuzina][research_kuzina]\] \[[Lan et al 1978][research_lan_mehrotra_1978]\] \[[Landahl 1959][research_landahl_1959]\] \[[Langham 1979][research_langham_1979]\] \[[Lee and Yoon 2008][research_lee_yoon_2008]\] \[[Lensi 2000][research_lensi_2000]\] \[[Letko and Riley 1950][research_letko_riley_1950]\] \[[Levin 1981][research_levin_1981]\] \[[Lichoń 2016][research_lichon_2016]\] \[[Limache and Cliff 1999][research_limache_cliff_1999]\] \[[Loeser and Rohlf 2016][research_loeser_rohlf_2016]\] \[[Lopez et al 1959][research_lopez_buell_1959]\] \[[Lundstrom 1949][research_lundstrom_1949]\] \[[Lutze 1980][research_lutze_1980]\] \[[Lutze and Fan 1998][research_lutze_fan_1998]\] \[[Luu and Ochi 2023][research_luu_ochi_2023]\] \[[Ma et al 2019][research_ma_huang_2019]\] \[[Maine 1977][research_maine_1977]\] \[[Maine 1978][research_maine_1978]\] \[[Maine and Iliff 1982][research_maine_iliff_1982]\] \[[Marchetti 1968][research_marchetti_1968]\] \[[Maricic 2006][research_maricic_2006]\] \[[Matějů 2019][research_mateju_2019]\] \[[Mehra et al 1972][research_mehra_stepner_1972]\] \[[Mehra et al 1974][research_mehra_stepner_1974]\] \[[Mialon et al 2010][research_mialon_khrabov_2010]\] \[[Moore 1957][research_moore_1957]\] \[[Moore and Moore 2008][research_moore_moore_2008]\] \[[Morris 1966][research_morris_1966]\] \[[Mulder 1985][research_mulder_1985]\] \[[Nagy and Kirsten 1976][research_nagy_kirsten_1976]\] \[[Napolitano and Spagnuolo 1993][research_napolitano_spagnuolo_1993]\] \[[Moul and Brown 1959][research_artificial_pitch_damping_1959]\] \[[Nguyen and Xiong 2026][research_nguyen_xiong_2026]\] \[[Nguyen et al 2025][research_nguyen_xiong_2025]\] \[[Park et al 2001][research_park_lee_2001]\] \[[Park et al 2015][research_park_ocheltree_2015]\] \[[Park et al 2016][research_park_choi_2016]\] \[[Parrish and Steinmetz 1972][research_parrish_steinmetz_1972]\] \[[Paulson 1944][research_paulson_1944]\] \[[Pototzky 2014][research_pototzky_2014]\] \[[Pototzky 2018][research_pototzky_2018]\] \[[Queijo and Wells 1956][research_queijo_wells_1956]\] \[[Raghavan and Ananthkrishnan 2005][research_raghavan_ananthkrishnan_2005]\] \[[Ramachandran and Wells 1974][research_ramachandran_wells_1974]\] \[[Ribner 1950][research_ribner_1950]\] \[[Kempel et al 1970][research_robertwkempel_larrywstrutz_1970]\] \[[Rudesh et al 2025][research_rudesh_singh_2025]\] \[[Samardžić 2023][research_samardzic_2023]\] \[[Samardžić et al 2013][research_samardzic_isakovic_2013]\] \[[Saraswathi 2000][research_saraswathi_2000]\] \[[Sarigul-Klijn et al 2008][research_sarigulklijn_nespeca_2008]\] \[[Schade and Hassell 1953][research_schade_hassell_1953]\] \[[Schiess 1986][research_schiess_1986]\] \[[Schiess 1988][research_schiess_1988]\] \[[Schiff and Tobak 1981][research_schiff_tobak_1981]\] \[[Shafer 1975][research_shafer_1975]\] \[[Sim and Curry 1978][research_sim_curry_1978]\] \[[Smith 1975][research_smith_1975]\] \[[Sorensen et al 1972][research_sorensen_tyler_1972]\] \[[Speyer and Crues 1985][research_speyer_crues_1985]\] \[[Speyer and Crues 1987][research_speyer_crues_1987]\] \[[Steers and Iliff 1975][research_steers_iliff_1975]\] \[[Sundar 1978][research_sundar_1978]\] \[[Tanner and Montgomery 1979][research_tanner_montgomery_1979]\] \[[Tatar and Masdari 2019][research_tatar_masdari_2019]\] \[[The Transformation of Aerodynamic 1997][research_the_transformation_1997]\] \[[The Transformation of Aerodynamic 2007][research_the_transformation_2007]\] \[[Tobak 1953][research_tobak_1953]\] \[[Tobak et al 1950][research_tobak_reese_1950]\] \[[Tran and Lind 2010][research_tran_lind_2010]\] \[[Transformation of Aerodynamic Stability 2013][research_transformation_of_2013]\] \[[Uselton 1978][research_uselton_1978]\] \[[Weil 1981][research_weil_1981]\] \[[Yanagihara et al 1991][research_yanagihara_suzuki_1991]\] \[[Yancey 1964][research_yancey_1964]\] \[[Yazawa 1977][research_yazawa_1977]\] \[[Yu et al 2026][research_yu_bose_2026]\]

### Aeroelasticity, flutter and control reversal

**Where the structure enters the control problem.** Flutter, divergence, control reversal and the flight dynamics of flexible aircraft.

**76 records.** \[[Allen et al 2005][research_allen_lizotte_2005]\] \[[Banerjee et al 2014][research_banerjee_liu_2014]\] \[[Brown 1959][research_brown_1959]\] \[[Bugała et al 2023][research_bugala_sznajder_2023]\] \[[Burner and Martinson 1996][research_burner_martinson_1996]\] \[[Castellani et al 2016][research_castellani_cooper_2016]\] \[[Chaudhuri and Nagaraja 1958][research_chaudhuri_nagaraja_1958]\] \[[Cheney 1988][research_cheney_1988]\] \[[Chipman et al 1984][research_chipman_rauch_1984]\] \[[Clarke et al 2005][research_clarke_allen_2005]\] \[[Collar 1946][research_collar_1946]\] \[[Comments, with reply, on 1992][research_comments_with_1992]\] \[[Diederich 1954][research_diederich_1954]\] \[[Doggett and Soistmann 1989][research_doggett_soistmann_1989]\] \[[Doggett and Soistmann 1992][research_doggett_soistmann_1992]\] \[[Dowell 1996][research_dowell_1996]\] \[[Dowell 1999][research_dowell_1999]\] \[[Dracopoulos and Oz 1992][research_dracopoulos_oz_1992]\] \[[Dugundji and Ghareeb 1965][research_dugundji_ghareeb_1965]\] \[[Dynamics of Flexible Aircraft 2023][research_dynamics_of_2023_b]\] \[[Dynamics of Very Flexible 2023][research_dynamics_of_2023]\] \[[Edwards 1992][research_edwards_1992]\] \[[Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]\] \[[Eugeni et al 2020][research_eugeni_mastroddi_2020]\] \[[Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]\] \[[Farhat 1998][research_farhat_1998]\] \[[Farhat 2000][research_farhat_2000]\] \[[Farhat 2001][research_farhat_2001]\] \[[Foughner and Bensinger 1977][research_foughner_bensinger_1977]\] \[[Fuzzy logic for control 1991][research_fuzzy_logic_1991]\] \[[Garrick and Reed 1981][research_garrick_reed_1981]\] \[[Gilbert et al 1982][research_gilbert_schmidt_1982]\] \[[Gimmestad 1980][research_gimmestad_1980]\] \[[Giordano de Oliveira Silva and Moennich 2012][research_giordanodeoliveirasilva_moennich_2012]\] \[[Houbolt and Williamson 1975][research_houbolt_williamson_1975]\] \[[Jenkins and Kuhl 1977][research_jenkins_kuhl_1977]\] \[[Jones and Nisbet 1976][research_jones_nisbet_1976]\] \[[Jung and Reimerdes 2003][research_jung_reimerdes_2003]\] \[[Klotz et al 2023][research_klotz_thabet_2023]\] \[[Lottati 1986][research_lottati_1986]\] \[[Malik et al 2020][research_malik_ricci_2020]\] \[[NACA Conference on Aircraft 1957][research_naca_conference_1957]\] \[[Nguyen et al 2017][research_nguyen_ting_2017]\] \[[Noll et al 1983][research_noll_calico_1983]\] \[[Patil 2004][research_patil_2004]\] \[[Patil and Hodges 2000][research_patil_hodges_2000]\] \[[Patil et al 1998][research_patil_hodges_1998]\] \[[Pengelley and Wilson 1954][research_pengelley_wilson_1954]\] \[[Petre and Ashley 1976][research_petre_ashley_1976]\] \[[Pfifer and Danowsky 2016][research_pfifer_danowsky_2016]\] \[[Reed 1982][research_reed_1982]\] \[[Rehman 2022][research_rehman_2022]\] \[[Rimer et al 1984][research_rimer_chipman_1984]\] \[[Rimer et al 1984][research_rimer_chipman_1984_b]\] \[[Roeser and Mönnich 2024][research_roeser_monnich_2024]\] \[[Rynaski et al 1978][research_rynaski_andrisani_1978]\] \[[Santos et al 2024][research_santos_adeodato_2024]\] \[[Silva][research_silva]\] \[[Silva 2011][research_silva_2011]\] \[[Spain et al 1990][research_spain_soistmann_1990]\] \[[Static Aeroelasticity Effect 2014][research_static_aeroelasticity_2014_b]\] \[[Stojakovic][research_stojakovic]\] \[[Sudha et al 2018][research_sudha_deodhare_2018]\] \[[Suleman 2007][research_suleman_2007]\] \[[Suresh et al 2010][research_suresh_radhakrishnan_2010]\] \[[Tantaroudas et al 2015][research_tantaroudas_daronch_2015]\] \[[Theodorsen 1935][research_theodorsen_1935]\] \[[Triplett 1980][research_triplett_1980]\] \[[Weisshaar 1978][research_weisshaar_1978]\] \[[Weisshaar 1979][research_weisshaar_1979]\] \[[Weisshaar 1983][research_weisshaar_1983]\] \[[Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]\] \[[Yang and Li 2022][research_yang_li_aeroelastic_2022]\] \[[Yang and Wan 1978][research_yang_wan_1978]\] \[[Zahm and Bear 1929][research_zahm_bear_1929]\] \[[Zhu and Li 2023][research_zhu_li_2023]\]

### Approach, landing, ground effect and the low lift-to-drag glide

**The X-4's second research role.** Ground effect on wings and low aspect ratio configurations, unpowered and low lift-to-drag approaches, and landing guidance for gliding vehicles.

**61 records.** \[[Aircraft In Ground Effect 1997][research_aircraft_in_1997]\] \[[Al-Bakri et al 2020][research_albakri_albakri_2020]\] \[[Anderson 1975][research_anderson_1975]\] \[[Aoyagi and Hickey 1963][research_aoyagi_hickey_1963]\] \[[Application of quasi-object control 2008][research_application_of_quasi_object_2008]\] \[[Approach and Landing 2017][research_approach_and_2017]\] \[[Becht 1950][research_becht_1950]\] \[[Bryson 1969][research_bryson_1969]\] \[[Chang and Muirhead 1987][research_chang_muirhead_1987]\] \[[Chang and Muirhead 1987][research_chang_muirhead_1987_b]\] \[[Connelly 1982][research_connelly_1982]\] \[[Curry and Curry 1997][research_curry_curry_1997]\] \[[Davis and Harris 1973][research_davis_harris_1973]\] \[[de Divitiis 2005][research_dedivitiis_2005]\] \[[Douglas Aircraft Co Long Beach Ca 1963][research_douglasaircraftcolongbeachca_1963]\] \[[Drake 1965][research_drake_1965]\] \[[Eichhorn et al 2022][research_eichhorn_fritzsche_2022]\] \[[Graves 1999][research_graves_1999]\] \[[Gross 2002][research_gross_2002]\] \[[Han and Cho 2005][research_han_cho_2005]\] \[[Hoag and Schofield 1970][research_hoag_schofield_1970]\] \[[Hoffman et al 1970][research_hoffman_zvara_1970]\] \[[Hubbell][research_hubbell]\] \[[Izadi et al 2007][research_izadi_pakmehr_2007]\] \[[Jacob 1987][research_jacob_1987]\] \[[Jump and Padfield 2006][research_jump_padfield_2006]\] \[[Katz and Levin 1984][research_katz_levin_1984]\] \[[Kemp et al 1966][research_kemp_lockwood_1966]\] \[[King and Gopalarathnam 2005][research_king_gopalarathnam_2005]\] \[[Kluever 2004][research_kluever_2004]\] \[[Kluever 2007][research_kluever_2007]\] \[[Kock et al 1972][research_kock_1972]\] \[[Koenig and Rolls 1966][research_koenig_rolls_1966]\] \[[Lee and Ko 2018][research_lee_ko_2018]\] \[[Lee et al 1986][research_lee_lan_1986]\] \[[Lee et al 1987][research_lee_lan_1987]\] \[[Lee et al 1989][research_lee_lan_1989]\] \[[Li et al 2022][research_li_shi_2022]\] \[[Lorenzetti et al 1969][research_lorenzetti_nelsen_1969]\] \[[Mamada and Ando 1973][research_mamada_ando_1973]\] \[[Mamada and Ando 1974][research_mamada_ando_1974]\] \[[Matranga 1961][research_matranga_1961]\] \[[Matranga and Armstrong 1959][research_matranga_armstrong_1959]\] \[[Matranga and Menard 1959][research_matranga_menard_1959]\] \[[Memon and Altman 2016][research_memon_altman_2016]\] \[[Oguz Tasci et al 2022][research_oguztasci_tumse_2022]\] \[[Paulson and Kjelgaard 1982][research_paulson_kjelgaard_1982]\] \[[Plotkin and Dodbele 1988][research_plotkin_dodbele_1988]\] \[[Prilliman and Slingerland 1966][research_prilliman_slingerland_1966]\] \[[Recant 1939][research_recant_1939]\] \[[Schmidt 1985][research_schmidt_1985]\] \[[Srivastava et al 2017][research_srivastava_kumar_2017]\] \[[Staufenbiel and Schlichting 1988][research_staufenbiel_schlichting_1988]\] \[[Steinbach 1997][research_steinbach_1997]\] \[[Sugimoto 1992][research_sugimoto_1992]\] \[[Sullivan 1978][research_sullivan_1978]\] \[[Wetmore and Turner 1940][research_wetmore_turner_1940]\] \[[Zerihan and Zhang 2000][research_zerihan_zhang_2000]\] \[[Zhang and Zerihan 2003][research_zhang_zerihan_2003]\] \[[Zhang and Zerihan 2004][research_zhang_zerihan_2004]\] \[[Zhao et al 2014][research_zhao_sheng_2014]\]

### Flight mechanics texts and chapters

**The textbook layer the derivations stand on.** Textbooks and their chapters on flight mechanics, stability, control, simulation and the equations of motion, reports on aircraft motion in the large, one conference proceedings, the tables of stability characteristics of selected aircraft and one collected works. The relations in Sizing From First Principles are of the kind these texts present.

**45 records.** \[[Abzug and DaRos 1955][research_abzug_daros_1955]\] \[[Advanced Aircraft Control 2026][research_advanced_aircraft_2026]\] \[[Aerodynamics and the 2016][research_aerodynamics_and_2016]\] \[[Aircraft Control 2011][research_aircraft_control_2011]\] \[[Aircraft Control 2016][research_aircraft_control_2016]\] \[[Aircraft Dynamic Stability 2003][research_aircraft_dynamic_2003]\] \[[Aircraft Dynamic Stability 2014][research_aircraft_dynamic_2014]\] \[[Aircraft Dynamic Stability 2024][research_aircraft_dynamic_2024]\] \[[Aircraft Equations of Motion 2003][research_aircraft_equations_2003]\] \[[Aircraft Equations of Motion 2014][research_aircraft_equations_2014]\] \[[Aircraft Equations of Motion 2024][research_aircraft_equations_2024]\] \[[Aircraft Non-Linear Dynamics Equations 2014][research_aircraft_non_linear_2014]\] \[[Aircraft Stability and Control 2022][research_aircraft_stability_2022]\] \[[Aircraft Stability and Control 2026][research_aircraft_stability_2026]\] \[[Ananthasayanam 2002][research_ananthasayanam_2002]\] \[[Appendix H Stability Characteristics 2003][research_appendix_h_2003]\] \[[Basilio Chaves][research_basiliochaves]\] \[[Biber 2016][research_biber_2016]\] \[[Bossert et al 2003][research_bossert_morris_2003]\] \[[Complete model of aircraft][research_complete_model]\] \[[Conference on Aircraft Aerodynamics 1966][research_conference_on_1966]\] \[[Davey et al 2016][research_davey_gordon_2016]\] \[[Donlan 1976][research_donlan_collected_1976]\] \[[Flight Dynamics of Elastic 2014][research_flight_dynamics_2014]\] \[[Flight Simulation 2016][research_flight_simulation_2016]\] \[[Fundamentals of Airplane Flight 2007][research_fundamentals_of_2007]\] \[[Introduction to Aircraft Flight 2024][research_introduction_to_2024]\] \[[Introduction to Airplane Flight][research_introduction_to]\] \[[Langton 2006][research_langton_2006]\] \[[Maneuvering Stability Methods and 2003][research_maneuvering_stability_2003]\] \[[Marzouk 2025][research_marzouk_2025]\] \[[Nominal aircraft dynamics][research_nominal_aircraft]\] \[[Rigid-Body Flight Dynamics 2026][research_rigid_body_flight_2026]\] \[[Shayak et al 2024][research_shayak_girdhar_2024]\] \[[Stability Characteristics of Selected 2014][research_stability_characteristics_2014]\] \[[Stability Characteristics of Selected 2024][research_stability_characteristics_2024]\] \[[Static Flight Stability and 2026][research_static_flight_2026]\] \[[Takeda 1970][research_takeda_1970]\] \[[Thelander 1965][research_thelander_1965]\] \[[Use of Aerodynamic Forces 2022][research_use_of_2022]\] \[[Vepa 2023][research_vepa_2023_b]\] \[[Vepa 2023][research_vepa_2023_c]\] \[[Vepa 2023][research_vepa_2023_d]\] \[[Yechout 2024][research_yechout_2024]\] \[[Yechout et al 2014][research_yechout_morris_2014]\]

### Information, similarity, the atmosphere and cost

**The relations the article borrows from outside flight mechanics.** Sampling, channel capacity and the information an experiment provides, Bayesian experimental design and data-driven modelling, similarity, viscosity and the boundary layer, the standard atmosphere, and the cost of airplanes.

**13 records.** \[[Appendix B Properties of 2003][research_appendix_b_2003]\] \[[Brunton et al 2020][research_brunton_noack_2020]\] \[[Buckingham 1914][research_buckingham_1914]\] \[[Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]\] \[[International Standard Atmosphere ISA 2017][research_international_standard_2017]\] \[[Lindley 1956][research_lindley_1956]\] \[[Nyquist 1928][research_nyquist_1928]\] \[[Prandtl 1928][research_prandtl_1928]\] \[[Properties of the U.S 2014][research_properties_of_2014]\] \[[Properties of the U.S 2024][research_properties_of_2024]\] \[[Shannon 1948][research_shannon_1948]\] \[[Sutherland 1893][research_sutherland_1893]\] \[[Wright 1936][research_wright_1936]\]

## Where the Framing Breaks Down

The keystone framework fits the X-4 better than any aircraft in this series so far, and it fails in three specific ways.

The answer was available before the aircraft flew. The tail contribution to pitch damping derived above requires a lift-curve slope and a moment arm, and both were known. The NACA had published on tailless stability and control four years earlier. An instrument model that treats a research aircraft as reducing uncertainty struggles with a programme whose central number could have been computed, and the honest reading is that the X-4 was built to make a prediction believed rather than to make it.

That is not a criticism, and it is the second breakdown. Institutional belief is a real output and the framework does not price it. Northrop had a long-standing commitment to tailless configurations and a large industrial interest in them, and no paper analysis was going to settle the matter against that. A flying aircraft did. The value of the programme lies substantially in whose minds it changed, which is not an information-theoretic quantity.

The third is that the answer had an expiry date nobody could see. The X-4 established a limit of unaugmented aerodynamics, and unaugmented aerodynamics stopped being the relevant category within a generation. A framework that scores a programme on what it settled must contend with the fact that this one settled a question whose premises later dissolved. The result was not overturned. It was made irrelevant by a technology outside its scope, which is a different and more interesting fate.

## The Source Base

**The survey rests on 3,854 research records from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 863 are report primaries, being 22.4 percent, by the identifier rule set out under The Definition of Primary. **The programme's own reports carry the argument** \[[Sadoff and Crossfield 1954][research_x4_flight_evaluation_1954]\] \[[Sadoff and Sisk 1950][research_x4_longitudinal_1950]\], and every one of them is a primary by that rule.

The primary record is small, focused, and adequate, which suits a programme that asked one question. [Sadoff and Crossfield 1954][research_x4_flight_evaluation_1954] is the consolidated result, with [Sadoff and Sisk 1950][research_x4_longitudinal_1950], [Sadoff and Sisk 1950][research_x4_stall_1950], [Baker 1953][research_x4_buffet_1953], and [Saltzman 1955][research_x4_blunt_elevons_1955] covering the components. The tailless configuration literature that surrounds it, from [Laitone 1943][research_tailless_highspeed_1943] and [Donlan 1944][research_tailless_interim_1944] through the all-wing studies to the later delta work, is where the question is posed and framed. [Donlan 1976][research_donlan_collected_1976] collects the work of an engineer close to several of these decisions.

The secondary literature treats the aircraft briefly and the Northrop tailless programme at length. [Miller 2001][book_miller_2001_x_planes], [Jenkins Landis and Miller 2003][book_jenkins_landis_miller_2003], [Winchester 2005][book_winchester_2005_x_planes], and [Peebles 2014][book_peebles_2014_probing_the_sky] give the roster treatment, while [Pape and Campbell][book_pape_northrop] and [Coleman 1988][book_coleman_1988_jack_northrop] cover the flying wing lineage and the institutional commitment behind it. [Hallion 1972][book_hallion_1972_supersonic_flight], [Hallion 1981][book_hallion_1981_on_the_frontier], [Hallion 1981][book_hallion_1981_test_pilots], [Gorn 2001][book_gorn_2001_expanding_envelope], and [Bilstein 1989][book_bilstein_1989_orders] supply the programme and institutional context, with [Gunston 1992][book_gunston_1992_faster_than_sound] and [Wolfe 1979][book_wolfe_1979_right_stuff] the wider and the popular framing.

The engineering texts behind the relations are [Etkin and Reid 1996][book_etkin_reid_1996], [Nelson 1998][book_nelson_1998], [Stengel 2004][book_stengel_2004], [Stevens and Lewis 2015][book_stevens_lewis_2015], [McRuer Ashkenas and Graham 1973][book_mcruer_ashkenas_graham_1973], and [Hurt 1965][book_hurt_1965] for flight dynamics, which is where this article spends most of its mathematics, with [Anderson 2001][book_anderson_2001_fundamentals], [Anderson 2002][book_anderson_2002_modern_compressible], [Anderson 2012][book_anderson_2012_aircraft_performance], [Anderson 1997][book_anderson_1997_history_aerodynamics], [Bertin and Cummings 2013][book_bertin_cummings_2013], [Shapiro 1953][book_shapiro_1953], [Liepmann and Roshko 1957][book_liepmann_roshko_1957], [Ashley and Landahl 1965][book_ashley_landahl_1965], [Kuchemann 1978][book_kuchemann_1978], [Schlichting and Gersten 2017][book_schlichting_gersten_2017], and [White 2006][book_white_2006_viscous] for the aerodynamics. Design method is [Raymer 2018][book_raymer_2018], [Nicolai and Carichner 2010][book_nicolai_carichner_2010], [Torenbeek 1982][book_torenbeek_1982], [Roskam 1985][book_roskam_1985], [Stinton 2001][book_stinton_2001], and [Whitford 1987][book_whitford_1987]. Structures are [Bruhn 1973][book_bruhn_1973], [Niu 1988][book_niu_1988_airframe], and [Megson 2016][book_megson_2016], aeroelasticity [Bisplinghoff Ashley and Halfman 1955][book_bisplinghoff_ashley_halfman_1955], [Fung 1955][book_fung_1955], and [Dowell 2014][book_dowell_2014], and propulsion [Sutton and Biblarz 2016][book_sutton_biblarz_2016], [Hill and Peterson 1991][book_hill_peterson_1991], and [Huzel and Huang 1992][book_huzel_huang_1992]. Flight test practice is [Kimberlin 2003][book_kimberlin_2003] and [Ward Strganac and Niewoehner 2006][book_ward_strganac_niewoehner_2006], with error analysis in [Taylor 1997][book_taylor_1997_error_analysis] and [Bevington and Robinson 2002][book_bevington_robinson_2002]. The epistemology is [Vincenti 1990][book_vincenti_1990], [Petroski 1985][book_petroski_1985], and [Ferguson 1992][book_ferguson_1992], the organizational reading is [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Sagan 1993][book_sagan_1993], and [Reason 1990][book_reason_1990_human_error], and the information accounting is [Cover and Thomas 2006][book_cover_thomas_2006] with design of experiments in [Box Hunter and Hunter 2005][book_box_hunter_hunter_2005], [Gelman et al 2013][book_gelman_et_al_2013], [Lindley 1956][research_lindley_1956], and [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]. Sampling and channel capacity are [Nyquist 1928][research_nyquist_1928] and [Shannon 1948][research_shannon_1948]. The tunnel and institutional histories are [Baals and Corliss 1981][book_baals_corliss_1981], [Hansen 1987][book_hansen_1987_engineer_in_charge], and [Chambers and Chambers 2008][book_chambers_2008_radical_wings], the theoretical lineage [von Karman and Edson 1967][book_von_karman_edson_1967] and [Gorn 1992][book_gorn_1992_universal_man], the thermal thread [Heppenheimer 2007][book_heppenheimer_2007_heat_barrier], [Truitt 1960][book_truitt_1960], [Bertin 1994][book_bertin_1994_hypersonic], [Anderson 2006][book_anderson_2006_hypersonic], [Incropera and DeWitt][book_incropera_heat_transfer], [Carslaw and Jaeger 1959][book_carslaw_jaeger_1959], and [Boley and Weiner 1960][book_boley_weiner_1960], and the X-15 and successor works [Jenkins 2007][book_jenkins_2007_x15], [Jenkins 2000][book_jenkins_2000_hypersonics], [Thompson 1992][book_thompson_1992_edge_of_space], [Launius and Jenkins 2012][book_launius_jenkins_2012], and [Merlin 2009][book_merlin_2009_blackbird].

Foundational primaries bearing on the arguments include [Williams and Drake][research_williams_drake_1948] on the research airplane rationale, [Buckingham 1914][research_buckingham_1914] on similarity, [Sutherland 1893][research_sutherland_1893] on viscosity, [Glauert 1928][research_glauert_1928] and [Prandtl 1928][research_prandtl_1928] on compressibility and the boundary layer, [Jones 1947][research_jones_1947] on planform, [Ackeret 1925][research_ackeret_1925] on supersonic lift, [NACA Report 1135][research_naca_1135] for the compressible relations, [Theodorsen 1935][research_theodorsen_1935], [Collar 1946][research_collar_1946], and [Garrick and Reed 1981][research_garrick_reed_1981] on aeroelasticity, [Phillips 1948][research_phillips_1948] on rolling coupling, [Beeler et al 1956][research_beeler_1956] on drag measurement, [Wright 1936][research_wright_1936] on unit cost at these quantities, and [Grauer and Morelli 2023][research_grauer_morelli_2023] and [Brunton et al 2020][research_brunton_noack_2020] on the modern descendants of the measurement and modelling disciplines. The wider fleet and configuration context appears in [Sawyer and Trant 1947][research_xf7u_semispan_1947], [Fourth High Alpha Conference 1994][research_high_alpha_conf_1994], [Chambers and Hall 2003][research_uncommanded_lateral_2003], and [Patton et al 1979][research_spin_research_summary_1979]. Contemporary work on departure and upset, envelope protection, system identification and transonic flutter that bears on this configuration is gathered in the clusters on stall and departure, on stability augmentation, on flight test and parameter identification, and on aeroelasticity above. [Tu et al 2024][research_tu_yan_2024] predict departure and spin characteristics, [Cen et al 2020][research_cen_li_2020] treat the post-stall dynamics of a transport configuration as a bifurcation problem, [Moreira et al 2022][research_moreira_gripp_2022] integrate envelope protection into a longitudinal control law, [Jurado and McGehee 2019][research_jurado_mcgehee_2019] calibrate an air data system online, and [Yuan et al 2024][research_yuan_kou_2024] predict the transonic flutter boundary by resolvent analysis. The equivalent problems at model scale are worked on this blog in [Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_a118_propulsion_sizing], [Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_a120_staged_boosted_propulsion], [Stability, Control, and Configuration for Fixed-Wing UAVs][related_post_a122_stability_configuration], [Dynamic Stability and Control for Fixed-Wing UAVs][related_post_a123_dynamic_stability], and [Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_a127_structures_flight_envelope], the rocketplane lineage in [History of Rocketplanes][related_post_a96_history_rocketplanes], large high-speed configurations in [Two-Stage Flying Delta Wing Vehicles for Civil and National Security Applications][related_post_a106_two_stage_delta_wing], propellant chemistry in [Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217_rocket_propellant_chemistry], the computing and simulation infrastructure in [Aerospace, Programming Languages, and Information Technology Co-Development: Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing] and [Aerospace, Programming Languages, and Information Technology Co-Development: Aerospace Simulation and Real-Time Systems][related_post_a241_aerospace_simulation], and space policy in [Introduction to Space Studies][related_post_a90_intro_space_studies]. The [NASA Technical Reports Server][ref_ntrs] and the [NASA History Office][ref_nasa_x3_factsheet] hold the record, with the [Armstrong Flight Research Center][ref_nasa_armstrong] the institutional successor.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when it is a NASA Technical Reports Server url or carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. The NACA research memoranda, technical notes and reports on which this article's flight record rests are all reached through the reports server, so the rule counts them.

**The rule does not reach the journal and conference literature of the American Institute of Aeronautics and Astronautics, abbreviated AIAA.** 1,774 of the records carry its 10.2514 prefix, and among them are the handling qualities evaluations conducted at the Air Force Test Pilot School. **22.4 percent is therefore a lower bound on how much of this survey is first-hand.**

### Thin Subjects

**Eight subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| the horizontal tail's contribution to pitch damping | tail damping, tail contribution, contribution of the horizontal tail, horizontal tail contribution | 3 |
| the control anticipation parameter | control anticipation | 2 |
| a period and damping acceptability boundary | period damping, satisfactory period, period and damping | 1 |
| the crossover model of the human pilot | crossover | 1 |
| the manoeuvre margin and the manoeuvre point | maneuver point, maneuver margin, manoeuvre point, manoeuvre margin | 6 |
| aerodynamic centre migration through the transonic band | aerodynamic center shift, aerodynamic centre shift, aerodynamic center movement, aerodynamic centre movement, aerodynamic center travel, aerodynamic centre travel, aerodynamic center migration, neutral point shift | 0 |
| the logarithmic decrement | logarithmic decrement | 1 |
| the unpowered low lift-to-drag approach | low lift drag ratio, low lift to drag ratio, unpowered approach, unpowered landing | 6 |

**The keystone construct is among the thin subjects.** Three titles name the tail's share of pitch damping, against 154 records in the pitch damping cluster. The division between wing and tail was settled early and lives in the textbooks, so the papers measure the total and the article's partition stands on the relations shown in Sizing From First Principles.

**Aerodynamic centre migration is settled in the same way**, a textbook result that no title here names. **The crossover model is thin for a different reason, which is that its vocabulary does not discriminate**, since the model is presented under titles about human pilot dynamics in the pilot-induced oscillation cluster above, and the one title that names it extends it to fractional-order plants. **The logarithmic decrement has been absorbed into parameter identification**, and its one record here is a modal identification method.

### What the Survey Admits

**Every research title has been read for relevance, and a record is admitted only when a person reading its title finds it on this article's subject**, which is the flight dynamics of tailless and tailed aircraft in and around the transonic band, their configuration and control, and the measurement and judgement of their handling. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Pitch damping is also the literature of projectiles, missiles and re-entry bodies, and roll damping that of ships and barges. A yaw damper is also a railway component, and yaw stability, directional control and handling quality also belong to road vehicles. The word tailless also names genes, cats and whipscorpions, a pilot crossover study is a clinical trial design, buffeting also loads bridges and buildings, and longitudinal dynamics also describes particle beams. Hover, rotorcraft, tiltrotor and vertical take-off aircraft share the vocabulary of handling qualities and augmentation and fly a different regime, so they are excluded too, as are fluidic thrust vectoring treated as nozzle physics, icing, and lift-to-drag optimisation of aerofoils unrelated to the low lift-to-drag approach. Correction, erratum, corrigendum and withdrawal notices are excluded as well, because a survey counts research works and those are editorial events. A review of a book, a reference or definition entry, a notice such as front matter, an editorial or a news item, and a second deposit of a document already counted are not admitted either, since none of them is a research work in its own right.

**A record whose only link to this subject is aeronautics in general is excluded too**, and so is one whose subject belongs to a class of vehicle or a problem the argument never uses. Short take-off and powered-lift aircraft, wing-in-ground-effect craft, paragliders, wingsuits, tethered and spherical vehicles, and the low Reynolds number aerodynamics of micro air vehicles are such classes. So are the drag reduction and shape design of wings and aerofoils for cruise efficiency, the nacelle, pylon and truss-braced wing installations of transports, propeller and propfan installation and performance though not a propeller's effect on stability, the wake vortex hazard to a following aircraft, wind tunnel facility descriptions, the management of flight test programmes, and hardware and software without flight dynamics content. A method or phenomenon the argument relies on is admitted whatever the vehicle, so a study of buffet, flutter, handling or identification on a transport or a small unmanned aircraft is kept. So are drag rise, the area rule, induced drag and boundary-layer transition, which the sections above use, and transonic wall interference, which bears on how far a tunnel could represent the band in which the X-4 flew. Trade news, a bibliography, a program manual and mathematics primer chapters are excluded as items that are not research, and a book chapter is otherwise judged by its subject.

**Some records of doubtful relevance are kept.** Two studies of tiltrotor aircraft are kept because the article cites them for maximum likelihood identification and for augmentation scheduled against flying qualities requirements, both of which they support, and a free-flight study of a tailless missile model is kept as an independent route to the tailless configuration. Structural, acoustic and design optimisation work on flying wings and blended wing bodies is kept in the configuration cluster, because it is about the configuration this article's conclusion says has returned, and design optimisation whose object is the transonic buffet boundary is kept with the buffet literature. A reader may weigh each accordingly.

**A second reading of every title, under the exclusions above, removed 338 records that the first reading had admitted**, most of them transonic drag and shape design for cruise, powered-lift and short take-off aircraft, and aeronautics with no link to the argument. **A sample of 200 titles drawn at random from what remains found two off topic**, which places the remaining share below 3.6 percent at 95 percent confidence. One is a user's guide to a flying qualities software toolbox, which is a program manual, and the other a stability and control study of a powered-lift short-haul research aircraft. **The off-topic share that remains is otherwise a matter of reading judgement.**

## Epistemic State

Established historical fact includes the 1946 contract for two aircraft, the serials, the semitailless configuration with elevons and no horizontal surface, the two Westinghouse J30 engines, the first flight on 15 December 1948, the early retirement of the first airframe, the maximum speed near Mach 0.92, the persistent lightly damped longitudinal oscillation above roughly Mach 0.88, the programme's end in 1953, and the preservation of the surviving aircraft. These are documented in the sources cited.

Established engineering analysis includes every relation in the sizing sections. The tail contribution to pitch damping, the short period frequency and damping expressions, the elevon deflection constraint, the static margin and neutral point relations, the directional stability and yaw damping expressions, the logarithmic decrement, and the damper augmentation relation are standard results. The worked numbers are the author's own arithmetic applied to representative inputs and are labelled as derived.

Inference includes the suggestion that the reported tendency to hunt about all three axes is consistent with proximity to wing rock, which is offered in the contemporary literature section as a possibility and is not an identification any source consulted makes. It also includes the central claim that the programme's finding is about damping margin rather than about stability. The tailless damping ratio computed here is 0.244, which is stable, and the argument that the aircraft's difficulty arises from having no margin to lose in the transonic band is an interpretation supported by the reported behaviour rather than a statement the primary reports make in those terms.

The wing-alone pitch damping derivative deserves separate mention, since the article distinguishes a parallel-axis term it evaluates at minus 0.02 from an unsteady chordwise term of order unity, and only the first is computed here. The value of minus 0.8 used throughout is adopted as representative of a low aspect ratio swept planform rather than derived from this airframe, and the conclusion is insensitive to it, since any value small against the tail's minus 13 produces the same finding.

Weakly supported are the representative values throughout. The moment of inertia and the radius of gyration behind it, the static margin, the lift-curve slopes, the tail volume coefficient and arm used for the conventional comparison, and both pitch damping derivatives are plausible values for aircraft of these classes rather than measured properties of this airframe. The ratio between the tailless and tailed damping ratios is more trustworthy than either value, since the same assumptions enter both sides, and the qualitative conclusion that the tail supplies the overwhelming majority of pitch damping is robust to any reasonable choice of inputs.

Contested or unresolved in the sources consulted is the total flight count, given variously as about 82 and about 102 with no stated counting rule, and the precise Mach number at which the oscillation became objectionable, which is reported as a band rather than a value and plainly depended on the pilot. A partial reconciliation of the flight count is available. The secondary account states that the NACA phase ended with an eighty-first flight in September 1953, that the first airframe made ten flights, and that the second made twenty contractor flights, which would make the lower figure the NACA phase alone and the higher figure that phase together with the contractor and Air Force flying. That is a plausible counting rule rather than a documented one, and no primary source consulted states it.

The low lift-to-drag approach role described above rests on the secondary account rather than on a primary report. No NACA document on the X-4's own landing series is retrievable from the NASA Technical Reports Server, although the technique and its successors are primary-documented in the approach and landing literature cited. The claim that the speed brakes could spoil the ratio below three to one should therefore be treated as reported rather than as verified here.

A note on temporal position. This article carries an editorial date of 2025-10-10 and is written from current knowledge, including contemporary literature published well after that date.

## Out of Scope

This article does not treat the [X-1][related_post_a298_bell_x1], [X-2][related_post_a299_bell_x2], or [X-3][related_post_a300_douglas_x3] beyond the comparisons drawn, all of which have their own articles, nor the [X-5][ref_bell_x5] or [X-15][ref_na_x15], which appear later. It does not derive the standard relations reused here, since the [series opener][related_post_a297_xplanes_framing] does that once for all seventy-two articles, including the [flight envelope][ref_flight_envelope], [load factor][ref_load_factor], [wing loading][ref_wing_loading], [lift][ref_lift_coefficient] and [drag][ref_drag_coefficient] coefficients, [lift-to-drag][ref_lift_to_drag], [Reynolds][ref_reynolds_number] and [Prandtl][ref_prandtl_number] numbers, [measurement uncertainty][ref_measurement_uncertainty] and its [propagation][ref_propagation_of_uncertainty], and the [standard atmosphere][ref_isa] in its [tabulated form][ref_us_standard_atmosphere].

It does not attempt a history of the Northrop flying wing programme, which is a large subject with its own literature and only touches this aircraft at the point of motivation. It does not treat the [YB-49][ref_yb49], the [B-2][ref_b2_spirit], or the [X-36][ref_mcdonnell_x36] as aircraft, only as inheritors, nor the [Me 163][ref_me163] except as precedent. It does not cover [shock waves][ref_shock_wave] and [oblique shocks][ref_oblique_shock], [wave drag][ref_wave_drag], [supersonic][ref_supersonic_speed] flow, [boundary layer][ref_boundary_layer] and [separation][ref_flow_separation] behaviour, [buffeting][ref_buffeting], [aerodynamic centre][ref_aerodynamic_center] theory, [longitudinal][ref_longitudinal_static_stability] and [directional][ref_directional_stability] stability as general subjects, the [phugoid][ref_phugoid], [flight dynamics][ref_flight_dynamics] generally, [inertia coupling][ref_inertia_coupling] and [Euler's equations][ref_euler_equations_rigid], [moments of inertia][ref_moment_of_inertia] as a subject, [reaction control][ref_rcs], [stabilators][ref_stabilator], [yaw dampers][ref_yaw_damper] beyond the augmentation relation given, [duralumin][ref_duralumin], [yield][ref_yield_strength], [wind tunnels][ref_wind_tunnel], [flight testing][ref_flight_test], [telemetry][ref_telemetry], [strain gauges][ref_strain_gauge], [accelerometers][ref_accelerometer], the [sound barrier][ref_sound_barrier], [transonic][ref_transonic] flow, [swept wings][ref_swept_wing], the [aspect ratio][ref_aspect_ratio], [Mach][ref_mach_number] and [dynamic pressure][ref_dynamic_pressure] as quantities, the [speed of sound][ref_speed_of_sound], [takeoff][ref_takeoff] and [landing gear][ref_landing_gear], [Edwards][ref_edwards_afb] and the [Armstrong Flight Research Center][ref_armstrong_frc], [Bell Aircraft][ref_bell_aircraft], the [NACA][ref_naca] and [NASA][ref_nasa] as organizations, the [National Museum of the United States Air Force][ref_nmusaf], the [list of X-planes][ref_list_of_x_planes], or [experimental aircraft][ref_experimental_aircraft] as a category, all of which are treated where they belong.

## Conclusion

The Northrop X-4 was built to test whether a horizontal tail could be dispensed with at transonic speed, and it produced a clean answer that has been widely misremembered.

The tail is not primarily a control surface. A conventional configuration draws roughly 94 percent of its pitch damping from the tail, because the damping contribution scales as the square of tail length and the wing alone supplies almost none. Removing the tail therefore removes almost all the damping, and the X-4's short period damping ratio works out near 0.24 against 0.75 for an otherwise identical tailed aircraft. Neither number is unstable. The difference is margin, and the transonic band is where margin is consumed. The tailless aircraft becomes effectively undamped once its derivatives fall to 21 percent of nominal, where the tailed aircraft tolerates a fall to 7 percent. The X-4 hunted above Mach 0.88 because it had nothing left to give.

The elevons compound this, since pitch and roll authority come from the same deflection and a roll input consumes the pitch authority the aircraft may need in the following second, and the short moment arm means a large force buys a small moment.

The finding held for thirty years and then expired, not because it was wrong but because damping became something that could be manufactured. A pitch damper restores by feedback precisely what the missing tail removed, and once that was routine the tailless configuration returned in the [X-36][ref_mcdonnell_x36], the [B-2][ref_b2_spirit], and a large modern literature. The X-4 did not prove the configuration impossible. It measured what the configuration costs, which is what made the eventual remedy specifiable.

The next article takes the [Bell X-5][ref_bell_x5], the first aircraft to change its wing sweep in flight, which turned a configuration choice into a control input and found out what that costs.

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
- [Coleman 1988 Jack Northrop and the Flying Wing][book_coleman_1988_jack_northrop]
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
- [Pape and Campbell, Northrop Flying Wings][book_pape_northrop]
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
- [Wikipedia Article on Northrop][ref_northrop_corp]
- [Wikipedia Article on Propagation of Uncertainty][ref_propagation_of_uncertainty]
- [Wikipedia Article on Supersonic Speed][ref_supersonic_speed]
- [Wikipedia Article on Takeoff][ref_takeoff]
- [Wikipedia Article on Telemetry][ref_telemetry]
- [Wikipedia Article on the Accelerometer][ref_accelerometer]
- [Wikipedia Article on the Aerodynamic Center][ref_aerodynamic_center]
- [Wikipedia Article on the Armstrong Flight Research Center][ref_armstrong_frc]
- [Wikipedia Article on the Aspect Ratio][ref_aspect_ratio]
- [Wikipedia Article on the Bell X-5][ref_bell_x5]
- [Wikipedia Article on the Boundary Layer][ref_boundary_layer]
- [Wikipedia Article on the Drag Coefficient][ref_drag_coefficient]
- [Wikipedia Article on the Elevon][ref_elevon]
- [Wikipedia Article on the Flight Envelope][ref_flight_envelope]
- [Wikipedia Article on the Flying Wing][ref_flying_wing]
- [Wikipedia Article on the International Standard Atmosphere][ref_isa]
- [Wikipedia Article on the Lift Coefficient][ref_lift_coefficient]
- [Wikipedia Article on the Lift-to-Drag Ratio][ref_lift_to_drag]
- [Wikipedia Article on the Load Factor][ref_load_factor]
- [Wikipedia Article on the Mach Number][ref_mach_number]
- [Wikipedia Article on the McDonnell Douglas X-36][ref_mcdonnell_x36]
- [Wikipedia Article on the Messerschmitt Me 163][ref_me163]
- [Wikipedia Article on the Moment of Inertia][ref_moment_of_inertia]
- [Wikipedia Article on the National Advisory Committee for Aeronautics][ref_naca]
- [Wikipedia Article on the National Museum of the United States Air Force][ref_nmusaf]
- [Wikipedia Article on the North American X-15][ref_na_x15]
- [Wikipedia Article on the Northrop Grumman B-2 Spirit][ref_b2_spirit]
- [Wikipedia Article on the Northrop X-4 Bantam][ref_northrop_x4]
- [Wikipedia Article on the Northrop YB-49][ref_yb49]
- [Wikipedia Article on the Oblique Shock][ref_oblique_shock]
- [Wikipedia Article on the Phugoid][ref_phugoid]
- [Wikipedia Article on the Prandtl Number][ref_prandtl_number]
- [Wikipedia Article on the Reaction Control System][ref_rcs]
- [Wikipedia Article on the Reynolds Number][ref_reynolds_number]
- [Wikipedia Article on the Shock Wave][ref_shock_wave]
- [Wikipedia Article on the Sound Barrier][ref_sound_barrier]
- [Wikipedia Article on the Speed of Sound][ref_speed_of_sound]
- [Wikipedia Article on the Stabilator][ref_stabilator]
- [Wikipedia Article on the Stability Augmentation System][ref_stability_augmentation]
- [Wikipedia Article on the Strain Gauge][ref_strain_gauge]
- [Wikipedia Article on the Swept Wing][ref_swept_wing]
- [Wikipedia Article on the Tailless Aircraft][ref_tailless]
- [Wikipedia Article on the U.S. Standard Atmosphere][ref_us_standard_atmosphere]
- [Wikipedia Article on the Westinghouse J30][ref_j30]
- [Wikipedia Article on the Wind Tunnel][ref_wind_tunnel]
- [Wikipedia Article on the Yaw Damper][ref_yaw_damper]
- [Wikipedia Article on Transonic Flow][ref_transonic]
- [Wikipedia Article on Wave Drag][ref_wave_drag]
- [Wikipedia Article on Wing Loading][ref_wing_loading]
- [Wikipedia Article on Yield in Engineering][ref_yield_strength]
- [Wikipedia List of X-Planes][ref_list_of_x_planes]
- [Wikipedia Section on Buffeting][ref_buffeting]

### Research

- [11. Multiloop Flight Control Systems 1990][research_multiloop_flight_1990]
- [2017][research_rea_pecora_2017]
- [5. Longitudinal Dynamics 1990][research_longitudinal_dynamics_1990]
- [6. Aircraft Steady Gliding Longitudinal Flight 2011][research_aircraft_steady_2011_d]
- [7. Aircraft Cruise in Steady Level Longitudinal Flight 2011][research_aircraft_cruise_2011_b]
- [8. Aircraft Steady Longitudinal Flight 2011][research_aircraft_steady_2011_b]
- [A comparative study of nonlinear filters in Pilot-Induced Oscillation caused by actuator rate limiting 2015][research_a_comparative_2015]
- [A Comparison of Different Approaches for Predicting Transonic Buffet Onset on Infinite Swept Wings 2022][research_a_comparison_2022]
- [A General Theory of Aircraft Wing Rock 2010][research_a_general_2010]
- [A New Steady Approach to Predict the Transonic Buffet Onset 2006][research_a_new_2006]
- [A'Harrah and Lockenour 1971][research_aharrah_lockenour_1971]
- [Abbott et al 1977][research_abbott_boirun_1977]
- [Abdelhamid and Kandil 1998][research_abdelhamid_kandil_1998]
- [Abdulrahim 2004][research_abdulrahim_2004]
- [Abdulwahab 2009][research_nabdulwahab_2009]
- [Abramov et al 2005][research_abramov_goman_2005]
- [Abramova et al 2016][research_abramova_petrov_2016]
- [Abramova et al 2020][research_abramova_petrov_2020]
- [Abu-Elola et al 2024][research_abuelola_alqaisia_2024]
- [Abualigah et al 2024][research_abualigah_ekinci_2024]
- [Abzug and DaRos 1955][research_abzug_daros_1955]
- [Abzug and Larrabee][research_abzug_larrabee]
- [Abzug and Larrabee][research_abzug_larrabee_b]
- [Accelerated development and flight evaluation of active controls concepts for subsonic transport aircraft 1979][research_accelerated_development_1979]
- [Ackeret 1925][research_ackeret_1925]
- [Ackerman et al 2016][research_ackerman_xargay_2016]
- [Adamo 2023][research_adamo_2023]
- [Adams][research_adams]
- [Adams 1972][research_adams_1972]
- [Adams 1978][research_adams_1978]
- [Adams 1980][research_adams_1980]
- [Adams and Hatch 1970][research_adams_hatch_1970]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adams and Silsby 1947][research_adams_silsby_1947]
- [Adams et al 1970][research_adams_schy_1970]
- [Addendum 2 Longitudinal Control and Stability Surfaces 2000][research_addendum_2_2000]
- [Addendum 3 Lateral Control and Stability Surfaces 2000][research_addendum_3_2000]
- [Addington and Myatt 2000][research_addington_myatt_2000]
- [Adegbindin et al 2016][research_adegbindin_love_2016]
- [Adler and Martins 2023][research_adler_martins_2023]
- [Advanced Aircraft Control 2026][research_advanced_aircraft_2026]
- [Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]
- [Aerodynamic and Landing Measurements Obtained During the First Powered Flight of the North American X-15 Research Airplane 1960][research_aerodynamic_and_1960]
- [Aerodynamics and the Stability of Aircraft 2016][research_aerodynamics_and_2016]
- [Aerodynamics of arbitrary wing body combinations with vortex latticeand slender body theory 1976][research_aerodynamics_of_1976]
- [Aeroelasticity Problems in Compressible Subsonic and Transonic Flow 2010][research_aeroelasticity_problems_2010]
- [Agarwal and Deese 1983][research_agarwal_deese_1983]
- [Agarwal and Deese 1984][research_agarwal_deese_1984]
- [Agenbag et al 2009][research_agenbag_theron_2009]
- [Agrawal et al 1991][research_agrawal_kinard_1991]
- [Agrell and Elmeland 1984][research_agrell_elmeland_1984]
- [Agrell and Elmeland 1985][research_agrell_elmeland_1985]
- [Aharrah 1995][research_ralphaaharrah_1995]
- [Aharrah and Lockenour 1969][research_aharrah_lockenour_1969]
- [Ahmed and Kandagal 2016][research_ahmed_kandagal_2016]
- [Ahmed and Worley 2008][research_ahmed_worley_2008]
- [Ahmed et al 2024][research_ahmed_zakaria_2024]
- [Ahn et al 2017][research_ahn_kim_2017]
- [Aiken and See 1951][research_aiken_see_1951]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_b]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_e]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Aircraft Control 2011][research_aircraft_control_2011]
- [Aircraft Control 2016][research_aircraft_control_2016]
- [Aircraft Cruise in Steady Level Longitudinal Flight 2011][research_aircraft_cruise_2011]
- [Aircraft Dynamic Stability 2003][research_aircraft_dynamic_2003]
- [Aircraft Dynamic Stability 2014][research_aircraft_dynamic_2014]
- [Aircraft Dynamic Stability 2024][research_aircraft_dynamic_2024]
- [Aircraft Equations of Motion 2003][research_aircraft_equations_2003]
- [Aircraft Equations of Motion 2014][research_aircraft_equations_2014]
- [Aircraft Equations of Motion 2024][research_aircraft_equations_2024]
- [Aircraft Flight Control 2014][research_aircraft_flight_2014]
- [Aircraft In Ground Effect 1997][research_aircraft_in_1997]
- [Aircraft instrument for indicating rate of change of pitch 1998][research_aircraft_instrument_1998]
- [Aircraft lateral-directional handling qualities design 2011][research_aircraft_lateral_directional_2011]
- [Aircraft longitudinal handling qualities design 2011][research_aircraft_longitudinal_2011]
- [Aircraft Non-Linear Dynamics Equations of Motion 2014][research_aircraft_non_linear_2014]
- [Aircraft Stability and Control 2022][research_aircraft_stability_2022]
- [Aircraft Stability and Control 2026][research_aircraft_stability_2026]
- [Aircraft Stability and Control Augmentation 2003][research_aircraft_stability_2003]
- [Aircraft Stability and Control Augmentation 2014][research_aircraft_stability_2014]
- [Aircraft Stability and Control Augmentation 2024][research_aircraft_stability_2024]
- [Aircraft Stability Characteristics in a Single Horizontal Tail Failure and Evaluation of Countermeasures for Safe Landing 2021][research_aircraft_stability_2021]
- [Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]
- [Aircraft Static Stability 2003][research_aircraft_static_2003]
- [Aircraft Static Stability 2014][research_aircraft_static_2014]
- [Aircraft Static Stability 2024][research_aircraft_static_2024]
- [Aircraft Steady Gliding Longitudinal Flight 2011][research_aircraft_steady_2011_c]
- [Aircraft Steady Longitudinal Flight 2011][research_aircraft_steady_2011]
- [Airplane Trim 2012][research_airplane_trim_2012]
- [Airplane Trim 2022][research_airplane_trim_2022]
- [Airspeed Calibration 2011][research_airspeed_calibration_2011]
- [Airspeed Calibration 2021][research_airspeed_calibration_2021]
- [Airspeed Calibration of a Light Airplane via Flight Test 2008][research_airspeed_calibration_2008]
- [Airspeed Definitions and Airspeed Measurement 2022][research_airspeed_definitions_2022]
- [Airspeed Systems Theory and Calibration 2003][research_airspeed_systems_2003]
- [Ajaj and Djidjeli 2022][research_ajaj_djidjeli_2022]
- [Al Aian et al 2014][research_alaian_basuno_2014]
- [Al-Bakri et al 2020][research_albakri_albakri_2020]
- [Al-Gilani et al 2009][research_algilani_abdunabi_2009]
- [Al-Hiddabi and McClamroch 2002][research_alhiddabi_mcclamroch_2002]
- [Alatorre et al 2021][research_alatorre_castillo_2021]
- [Alberghini and Lee 2018][research_alberghini_lee_2018]
- [Albisser et al 2014][research_albisser_dobre_2014]
- [Alex 2014][research_alex_2014]
- [Ali 1997][research_ali_1997]
- [Ali et al 2025][research_ali_okasha_2025]
- [Ali et al 2026][research_ali_rasani_2026]
- [Alighanbari 2002][research_alighanbari_2002]
- [Allen 1951][research_allen_1951]
- [Allen 1976][research_allen_1976]
- [Allen and Tuttle 1973][research_allen_tuttle_1973]
- [Allen et al 2005][research_allen_lizotte_2005]
- [Alsahlani et al 2017][research_alsahlani_johnston_2017]
- [Altman 1952][research_altman_1952]
- [Altunkaya and Catak 2025][research_altunkaya_2025]
- [Altunkaya and Ozkol 2022][research_altunkaya_ozkol_2022]
- [Altunkaya and Ozkol 2022][research_altunkaya_ozkol_2022_b]
- [Altunkaya and Ozkol 2023][research_altunkaya_ozkol_2023]
- [Alwi and Edwards 2007][research_alwi_edwards_2007]
- [Alwi and Edwards 2009][research_alwi_edwards_2009]
- [Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]
- [Ameho and Prempain 2011][research_ameho_prempain_2011]
- [Amendola et al 2018][research_amendola_dimino_2018]
- [Ammar and Trépanier 2014][research_ammar_trepanier_2014]
- [Ammar et al 2017][research_ammar_legros_2017]
- [Amprikidis and Cooper 2004][research_amprikidis_cooper_2004]
- [An analysis of gap effects on wing-elevon aerodynamic characteristics 1981][research_an_analysis_1981]
- [An experimental and computational investigation of a swept-wing flowat subsonic speeds 1978][research_an_experimental_1978]
- [An Introduction to the Longitudinal Static Stability of Low-Speed Aircraft 1966][research_an_introduction_1966]
- [An investigation of separate surface stability augmentation systems for general aviation aircraft 1974][research_an_investigation_1974]
- [Analytical synthesis of the control laws at short-period longitudinal motion of the unmanned aerial vehicle 2024][research_analytical_synthesis_2024]
- [Anandakumar et al 2022][research_anandakumar_bernstein_2022]
- [Ananthasayanam 2002][research_ananthasayanam_2002]
- [Ananthkrishnan 2004][research_ananthkrishnan_2004]
- [Ananthkrishnan and Ramadevi 2002][research_ananthkrishnan_ramadevi_2002]
- [Andersen et al 1997][research_andersen_kolonay_1997]
- [Andersen et al 1998][research_andersen_kolonay_1998]
- [Andersen et al 1998][research_andersen_kolonay_1998_b]
- [Anderson 1949][research_anderson_1949]
- [Anderson 1970][research_anderson_1970]
- [Anderson 1975][research_anderson_1975]
- [Anderson 1986][research_anderson_1986]
- [Anderson 1992][research_sethbanderson_1992]
- [Anderson and Bray 1955][research_anderson_bray_1955]
- [Anderson and Christofferson 1947][research_anderson_christofferson_1947]
- [Anderson and Cooper 1947][research_anderson_cooper_1947]
- [Anderson and Vincent 1985][research_anderson_vincent_1985]
- [Anderson et al 1972][research_anderson_berger_1972]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Ando and Kajita 1992][research_ando_kajita_1992]
- [Andreea-Irina and Achim 2014][research_andreeairina_achim_2014]
- [Andrew and Stenton 1967][research_andrew_stenton_1967]
- [Andrianantara et al 2025][research_andrianantara_ghazi_2025]
- [Anglin and Byrdsong 1982][research_anglin_byrdsong_1982]
- [Ankenbruck 1945][research_allwing_modifications_1945]
- [Ankenbruck 1946][research_ankenbruck_1946]
- [Ankenbruck and McKinney 1947][research_ankenbruck_mckinney_1947]
- [Ankenbruck et al 1951][research_ankenbruck_sadoff_1951]
- [Ansell et al 2010][research_ansell_bragg_2010]
- [Ansell et al 2011][research_ansell_bragg_2011]
- [Ansell et al 2014][research_ansell_kerho_2014]
- [Anton et al 2009][research_anton_botez_2009]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Antoniou et al 2025][research_antoniou_antoniou_2025]
- [Aoyagi and Hickey 1963][research_aoyagi_hickey_1963]
- [APPENDICES A. Stability Derivatives and Transfer Function Factors for Representative Aircraft 1990][research_appendices_a_1990]
- [Appendix B Properties of the U.S. Standard Atmosphere 2003][research_appendix_b_2003]
- [Appendix C Stability and Control Derivatives for a Notional GA Aircraft 2021][research_appendix_c_2021]
- [Appendix G Development of Longitudinal and Lateral-Directional Transfer Functions 2003][research_appendix_g_2003]
- [Appendix H Stability Characteristics of Selected Aircraft 2003][research_appendix_h_2003]
- [Application of dynamic flight control to realization of aircraft spatial flight manoeuvre][research_application_of]
- [Application of quasi-object control systems by angular position of airplane for the translation of airplane from horizontal flight in a glide slope approach 2008][research_application_of_quasi_object_2008]
- [Approach and Landing 2017][research_approach_and_2017]
- [Approximate Expressions for the Dimensionless Aerodynamic Stability and Control Derivatives 1997][research_approximate_expressions_1997]
- [Approximate Expressions for the Dimensionless Aerodynamic Stability and Control Derivatives 2013][research_approximate_expressions_2013]
- [Approximate Expressions for the Dimensionless Aerodynamics Stability and Control Derivatives 2007][research_approximate_expressions_2007]
- [Arabian and Schmeer 1955][research_arabian_schmeer_1955]
- [Arai et al 2000][research_arai_noto_2000]
- [Araujo and Singh 1998][research_araujo_singh_1998]
- [Araujo-Estrada et al 2022][research_araujoestrada_lowenberg_2022]
- [Arbic 1956][research_tailless_freeflight_1956]
- [Archambaud et al 2004][research_archambaud_louis_2004]
- [Arena and Nelson 1989][research_arena_nelson_1989]
- [Arena and Nelson 1991][research_arena_nelson_1991]
- [Arena and Nelson 1992][research_arena_nelson_1992]
- [Arena and Nelson 1994][research_arena_nelson_1994]
- [Arena et al 1990][research_arena_nelson_1990]
- [Argyle and Beard 2016][research_argyle_beard_2016]
- [Arif et al 2023][research_arif_singh_2023]
- [Arik et al 2018][research_arik_turkmen_2018]
- [Armenta and Takahashi 2021][research_armenta_takahashi_2021]
- [Arnold 1942][research_arnold_1942]
- [Arnold 1968][research_arnold_1968]
- [Asada and Kawai 2024][research_asada_kawai_2024]
- [Asadi et al 2013][research_asadi_sabzehparvar_2013]
- [Asai 2022][research_asai_2022]
- [Asher et al 1957][research_asher_martuccelli_1957]
- [Ashkenas 1946][research_ashkenas_1946]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashkenas 1965][research_ashkenas_1965_b]
- [Ashkenas 1965][research_ashkenas_1965_c]
- [Ashkenas 1969][research_ashkenas_1969]
- [Ashkenas 1971][research_ashkenas_1971]
- [Ashkenas 1982][research_ashkenas_1982]
- [Ashkenas and Klyde 1989][research_ashkenas_klyde_1989]
- [Ashley 1980][research_ashley_1980]
- [Ashworth et al 1988][research_ashworth_mouch_1988]
- [Aslam et al 2025][research_aslam_islam_2025]
- [Aso and Tanaka 2017][research_aso_tanaka_2017]
- [Aso et al 2018][research_aso_tanaka_2018]
- [Assadourian and Reeder 1948][research_assadourian_reeder_1948]
- [Atesoglu and Ozgoren 2011][research_atesoglu_ozgoren_2011]
- [Atesoglu and Özgören 2006][research_atesoglu_ozgoren_2006]
- [Atkinson 2016][research_atkinson_2016]
- [Atmaca and Van Kampen 2025][research_atmaca_vankampen_2025]
- [Atmaca et al 2026][research_atmaca_stroosma_2026]
- [Atmospheric disturbance models and requirements for the flying qualities Military Standard and Handbook 1981][research_atmospheric_disturbance_1981]
- [Atzhorn and Stengel 1981][research_atzhorn_stengel_1981]
- [Atzhorn and Stengel 1984][research_atzhorn_stengel_1984]
- [Aubeelack][research_aubeelack]
- [Aul'chenko and Zamuraev 2012][research_aulchenko_zamuraev_2012]
- [Avanzini et al 2017][research_avanzini_nicassio_2017]
- [Averett and Wright 1966][research_averett_wright_1966]
- [Axelson 1947][research_axelson_1947]
- [Axelson 1975][research_axelson_1975]
- [Axelson 1977][research_axelson_1977]
- [Ayele et al 2023][research_ayele_maldonado_2023]
- [Ayers and Hallissy 1981][research_ayers_hallissy_1981]
- [Ayoub and McLachlan 1987][research_ayoub_mclachlan_1987]
- [Ayoub and McLachlan 1988][research_ayoub_mclachlan_1988]
- [Azor 1995][research_azor_1995]
- [Ba Zuhair 2019][research_bazuhair_2019]
- [Babcock and Arena 2004][research_babcock_arena_2004]
- [Babinsky and Ogawa 2006][research_babinsky_ogawa_2006]
- [Babister 1980][research_babister_1980]
- [Babister 1980][research_babister_1980_b]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]
- [Bachelder and Aponso 2022][research_bachelder_aponso_2022]
- [Bachelder and Aponso 2023][research_bachelder_aponso_2023_c]
- [Bachelder et al 2023][research_bachelder_aponso_2023]
- [Bachelder et al 2023][research_bachelder_aponso_2023_b]
- [Baggi et al 2020][research_baggi_franco_2020]
- [Baggi et al 2022][research_baggi_serrani_2022]
- [Bahri 2018][research_bahri_2018]
- [Bailey and Smith 1981][research_bailey_smith_1981]
- [Bailey and Smith 1982][research_bailey_smith_1982]
- [Bailey et al 1987][research_bailey_knotts_1987]
- [Bailey et al 1988][research_bailey_powers_1988]
- [Bainsla et al 2021][research_bainsla_singari_2021]
- [Bajpai and Chang][research_bajpai_chang]
- [Bakaul et al 2012][research_bakaul_wang_2012]
- [Bakaul et al 2014][research_bakaul_yankui_2014]
- [Bakaul et al 2015][research_bakaul_wang_2015]
- [Bakaul et al 2015][research_bakaul_wang_2015_b]
- [Baker 1953][research_x4_buffet_1953]
- [Baker and Farrell 1991][research_baker_farrell_1991]
- [Baker and Johnson 1955][research_baker_johnson_1955]
- [Balakrishna and Niranjana 1987][research_balakrishna_niranjana_1987]
- [Balas and Hodgkinson 2009][research_balas_hodgkinson_2009]
- [Balasubramanian et al 2024][research_balasubramanian_ahuja_2024]
- [Balasubramanian et al 2026][research_balasubramanian_n_2026]
- [Ball 1978][research_ball_1978]
- [Ball 1979][research_ball_1979]
- [Balleur et al 2002][research_balleur_girodrouxlavigne_2002]
- [Ballouz and Chang][research_ballouz_chang]
- [Balogun et al 2026][research_balogun_khan_2026]
- [Bandettini 1952][research_bandettini_1952]
- [Banerjee 1984][research_banerjee_1984]
- [Banerjee 1988][research_banerjee_1988]
- [Banerjee 1988][research_banerjee_1988_b]
- [Banerjee et al 2014][research_banerjee_liu_2014]
- [Banner et al 1958][research_banner_1958]
- [Bar-Gill and Stengel 1983][research_bargill_stengel_1983]
- [Barakos and Drikakis 1999][research_barakos_drikakis_1999]
- [Barber et al 1966][research_barber_haise_1966]
- [Barbosa et al 2019][research_barbosa_bertolin_2019]
- [Barbut et al 2010][research_barbut_braza_2010]
- [Bare et al 1981][research_bare_berrier_1981]
- [Barinov et al 2016][research_barinov_pavlenko_2016]
- [Barker and Balas 1999][research_barker_balas_1999]
- [Barnard 1969][research_barnard_1969]
- [Barnes and Visbal 2020][research_barnes_visbal_2020]
- [Barnwell 1974][research_barnwell_1974]
- [Barnwell et al 2003][research_barnwell_heinzen_2003]
- [Barren et al][research_barren_larson]
- [Barsby 1973][research_barsby_1973]
- [Bartlett 1975][research_bartlett_1975]
- [Bartlett and Sangiorgio 1975][research_bartlett_sangiorgio_1975]
- [Basilio Chaves][research_basiliochaves]
- [Bass et al 1966][research_bass_stoner_1966]
- [Bateman et al 2004][research_bateman_argrow_2004]
- [Bateman et al 2008][research_bateman_noura_2008]
- [Batina 1986][research_batina_1986]
- [Batina 1986][research_batina_1986_b]
- [Batina 1986][research_batina_1986_c]
- [Batina 1988][research_batina_1988]
- [Batina 1989][research_batina_1989]
- [Batina et al 1989][research_batina_seidel_1989]
- [Batterson and Klein 1984][research_batterson_klein_1984]
- [Baughman and Longeauay 2015][research_baughman_longeauay_2015]
- [Bazile and Calderara 2012][research_bazile_calderara_2012]
- [Bazuhair 2018][research_bazuhair_2018]
- [Bean and Lee 1994][research_bean_lee_1994]
- [Beaufrere 1988][research_beaufrere_1988]
- [Bechelder et al 2025][research_bechelder_bjorkman_2025]
- [Becht 1950][research_becht_1950]
- [Becht and Few 1950][research_becht_few_1950]
- [Beeler et al 1956][research_beeler_1956]
- [Begnini et al 2018][research_begnini_bones_2018]
- [Beh et al 2018][research_beh_hofinger_2018]
- [Beldica and Hilton 1999][research_beldica_hilton_1999]
- [Belesiotis-Kataras and Timme 2020][research_belesiotiskataras_timme_2020]
- [Belesiotis-Kataras and Timme 2021][research_belesiotiskataras_timme_2021]
- [Belisle et al 2010][research_belisle_neale_2010]
- [Bellman 1959][research_bellman_1959]
- [Benchaita and Ladaci 2021][research_benchaita_ladaci_2021]
- [Bendiksen 2008][research_bendiksen_2008]
- [Bendiksen 2009][research_bendiksen_2009]
- [Benepe et al 1974][research_benepe_cunningham_1974]
- [Benepe et al 1978][research_benepe_cunningham_1978]
- [Bengtson et al 1975][research_bengtson_dickovich_1975]
- [Benjamin et al 2021][research_benjamin_hesse_2021]
- [Bennett 1947][research_bennett_1947]
- [Bennett and Johnson 1947][research_bennett_johnson_1947]
- [Benoit et al 2014][research_benoit_verbeke_2014]
- [Benyamen et al 2020][research_benyamen_mckinnis_2020]
- [Bera 1974][research_bera_1974]
- [Bera 1974][research_bera_1974_b]
- [Berg 1991][research_berg_1991]
- [Berger et al 2012][research_berger_tischler_2012]
- [Berger et al 2013][research_berger_tischler_2013]
- [Berger et al 2025][research_berger_christensen_2025]
- [Bernal 2016][research_bernal_2016]
- [Berry 1981][research_berry_1981]
- [Berry 1982][research_berry_1982]
- [Berry 1985][research_berry_1985]
- [Berry 1986][research_berry_1986]
- [Berry 1986][research_berry_1986_b]
- [Berry and Powers 1970][research_berry_powers_1970]
- [Berry et al 1976][research_berry_mallick_1976]
- [Bertelrud 1981][research_bertelrud_1981]
- [Bertelrud and Graves 1994][research_bertelrud_graves_1994]
- [Bertelsen 2006][research_bertelsen_2006]
- [Berthold 1977][research_berthold_1977]
- [Bertolin et al 2021][research_bertolin_2021]
- [Bertoni et al 2010][research_bertoni_bertozzi_2010]
- [Beyers and Brown 2006][research_beyers_brown_2006]
- [Bharadvaj 1990][research_bharadvaj_1990]
- [Bharadvaj 1991][research_bharadvaj_1991]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2019][research_bian_nener_2019]
- [Biber 2016][research_biber_2016]
- [Biber 2017][research_biber_2017]
- [Bidinotto et al 2021][research_bidinotto_2021]
- [Bielat 1959][research_bielat_1959]
- [Bielat and Pierpont 1960][research_bielat_pierpont_1960]
- [Bielat and Wiley 1959][research_bielat_wiley_1959]
- [Biezad and Bole 2001][research_biezad_bole_2001]
- [Bihrle 1969][research_bihrle_1969]
- [Bihrle and Mulcay 1979][research_bihrle_mulcay_1979]
- [Bingaman 2012][research_bingaman_2012]
- [Binwen Lu et al 2016][research_binwenlu_jianjunma_2016]
- [Bippes 1990][research_bippes_1990]
- [Birch and Lee 2005][research_birch_lee_2005]
- [Bird and Jaquet 1951][research_bird_jaquet_1951]
- [Bird et al 1951][research_fuselage_tail_yawing_1951]
- [Bird et al 1953][research_bird_fisher_1953]
- [Biriukov 1959][research_biriukov_1959]
- [Bischoff 1983][research_bischoff_1983]
- [Bischoff and Palmer 1983][research_bischoff_palmer_1983]
- [Bise and Black][research_bise_black]
- [Bishop 1961][research_bishop_1961]
- [Black][research_black]
- [Black 1956][research_black_1956]
- [Black 2009][research_black_2009]
- [Black and Moorhouse 1979][research_black_moorhouse_1979]
- [Black and Thomas 1988][research_black_thomas]
- [Blaesser and Frederick 2020][research_blaesser_frederick_2020]
- [Blake 1993][research_blake_1993]
- [Blake et al 2009][research_blake_gotwald_2009]
- [Bland and Young 1961][research_bland_young_1961]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Blight et al 1986][research_blight_gangsaas_1986]
- [Blight et al 2018][research_blight_lanedailey_2018]
- [Blodgett and Lagor 2022][research_blodgett_lagor_2022]
- [Bloy 1996][research_bloy_1996]
- [Bloy 1998][research_bloy_1998]
- [Bobbitt 1980][research_bobbitt_1980]
- [Bobbitt and Foughner 1985][research_bobbitt_foughner_1985]
- [Bodonyl 1994][research_bodonyl_1994]
- [Bodson 2000][research_bodson_2000]
- [Bodur and Ucun 2023][research_bodur_ucun_2023]
- [Boelens 2017][research_boelens_2017]
- [Bogatyrev 2017][research_bogatyrev_2017]
- [Bogdan et al 2010][research_bogdan_radu_2010]
- [Bohlmann et al 1988][research_bohlmann_weisshaar_1988]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Boisseau 1955][research_boisseau_1955]
- [Bollech and Furlong 1948][research_bollech_furlong_1948]
- [Bolton and Collins 1974][research_bolton_collins_1974]
- [Bon 2021][research_bon_2021]
- [Bonnifet et al 2017][research_bonnifet_gerolymos_2017]
- [Boothe 1971][research_boothe_1971]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Booz 1988][research_booz_1988]
- [Boppe 1977][research_boppe_1977]
- [Boppe 1978][research_boppe_1978]
- [Bordei and Halanay 2018][research_bordei_halanay_2018]
- [Borri and Trainelli 2003][research_borri_trainelli_2003]
- [Bosch and Kuehl 1976][research_bosch_kuehl_1976]
- [Boschetti and Cardenas 2012][research_boschetti_cardenas_2012]
- [Boschetti et al 2010][research_boschetti_cardenas_2010]
- [Boskovic and Mehra][research_boskovic_mehra]
- [Boskovic and Mehra 1999][research_boskovic_mehra_1999]
- [Boskovic and Mehra 2000][research_boskovic_mehra_2000]
- [Boskovic et al][research_boskovic_ling]
- [Boskovic et al][research_boskovic_saimingli]
- [Bossert et al 2003][research_bossert_morris_2003]
- [Boswinkle and Smith 1958][research_boswinkle_smith_1958]
- [Bosworth and Stoliker 1996][research_bosworth_stoliker_1996]
- [Bosworth and Williams-Hayes 2007][research_bosworth_williamshayes_2007]
- [Bosworth and Williams-Hayes 2010][research_bosworth_williamshayes_2010]
- [Botez and Rotaru 2007][research_botez_rotaru_2007]
- [Bouadi][research_bouadi]
- [Bouadi et al 2012][research_bouadi_choukroun_2012]
- [Bourdin 2002][research_bourdin_2002]
- [Bourdin et al 2007][research_bourdin_gatto_2007]
- [Bowes and Miller 1976][research_bowes_miller_1976]
- [Bowling and Key 1976][research_bowling_key_1976]
- [Bowlus et al 1997][research_bowlus_multhopp_1997]
- [Bowman et al 1978][research_bowman_stough_1978]
- [Boyden 1974][research_boyden_1974]
- [Bradshaw et al 1985][research_bradshaw_davis_1985]
- [Bragg and Soltani 1990][research_bragg_soltani_1990]
- [Bragin 2018][research_bragin_2018]
- [Bramantya and Nugroho 2025][research_bramantya_nugroho_2025]
- [Brand 1981][research_brand_1981]
- [Brandon 1986][research_brandon_1986]
- [Brandon et al 1995][research_brandon_brown_1995]
- [Brandon et al 1996][research_brandon_simon_1996]
- [Brandon et al 2001][research_brandon_lan_2001]
- [Brandt and Bons 2024][research_brandt_bons_2024]
- [Brandt et al 2011][research_brandt_fossum_2011]
- [Brandt et al 2022][research_brandt_mcfadden_2022]
- [Brauser 1982][research_brauser_1982]
- [Brauser 1983][research_brauser_1983]
- [Bray 1963][research_bray_1963]
- [Breneman and Lower 1992][research_breneman_lower_1992]
- [Breul et al 1985][research_breul_keller_1985]
- [Breul et al 1987][research_breul_keller_1987]
- [Brewer 1946][research_brewer_1946]
- [Brewer and May 1948][research_brewer_may_1948]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Brigido-Gonzalez and Rodriguez-Cortes 2014][research_brigidogonzalez_rodriguezcortes_2014]
- [Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]
- [Brincklow et al 2021][research_brincklow_montgomery_2021]
- [Brincklow et al 2024][research_brincklow_montgomery_2024]
- [Brinker and Wise 1996][research_brinker_wise_1996]
- [Brinker and Wise 1998][research_brinker_wise_1998]
- [Brinker and Wise 1999][research_brinker_wise_1999]
- [Brinker and Wise 2000][research_brinker_wise_2000]
- [Brinker and Wise 2001][research_brinker_wise_2001]
- [Brody et al 2025][research_brody_fagley_2025]
- [Bronz et al 2019][research_bronz_aydin_2019]
- [Brooks 1986][research_brooks_1986]
- [Broussard and Stengel 1977][research_broussard_stengel_1977]
- [Brower and Wright 1966][research_brower_wright_1966]
- [Brown 1959][research_brown_1959]
- [Brown and Adams 1948][research_brown_adams_1948]
- [Brown and Bradley 1981][research_brown_bradley_1981]
- [Brown and Vos 2018][research_brown_vos_2018]
- [Browne et al 2024][research_browne_maldonado_2024]
- [Browne et al 2025][research_browne_maldonado_2025]
- [Bruner 1983][research_bruner_1983]
- [Brunet and Deck 2008][research_brunet_deck_2008]
- [Bruno Santos et al 2020][research_brunosantos_oliveira_2020]
- [Brunton et al 2020][research_brunton_noack_2020]
- [Brutch and Moncayo 2024][research_brutch_moncayo_2024]
- [Bryant 1950][research_bryant_1950]
- [Bryson 1954][research_bryson_1954]
- [Bryson 1969][research_bryson_1969]
- [Bryson and Rumpfkeil 2016][research_bryson_rumpfkeil_2016]
- [Buch and George M. 2010][research_buch_georgem_2010]
- [Buckingham 1914][research_buckingham_1914]
- [Buddhamatya et al 2026][research_buddhamatya_miranda_2026]
- [Buell and Johnson 1959][research_buell_johnson_1959]
- [Buell and Tinling 1957][research_buell_tinling_1957]
- [Buenz et al 1975][research_buenz_brooks_1975]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Buffington and Sparks 1998][research_buffington_sparks_1998_b]
- [Buffington et al 1993][research_buffington_sparks_1993]
- [Buffington et al 1994][research_buffington_sparks_1994]
- [Buffington et al 1998][research_buffington_sparks_1998]
- [Bugała et al 2023][research_bugala_sznajder_2023]
- [Bui 2013][research_bui_2013]
- [Bui 2015][research_bui_2015]
- [Bui 2016][research_bui_2016]
- [Bui 2018][research_bui_2018]
- [Bull and Kidd 1955][research_bull_kidd_1955]
- [Bunescu et al 2024][research_bunescu_stoican_2024]
- [Burcham and Burken 1994][research_burcham_burken_1994]
- [Burcham et al 1992][research_burcham_maine_1992]
- [Burdges 1973][research_burdges_1973]
- [Burken et al 2006][research_burken_williamshayes_2006]
- [Burkhalter 1993][research_burkhalter_1993]
- [Burkhalter et al 1992][research_burkhalter_spring_1992]
- [Burlion et al 2014][research_burlion_poussotvassal_2014]
- [Burner and Martinson 1996][research_burner_martinson_1996]
- [Burnham 1995][research_burnham_1995]
- [Burton and Bischoff 1976][research_burton_bischoff_1976]
- [Burton and Lamour 1971][research_burton_lamour_1971]
- [Buter and Rao 1984][research_buter_rao_1984]
- [Butler 1976][research_butler_1976]
- [Butler 1982][research_butler_1982]
- [Butler and Bons 2025][research_butler_bons_2025]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Cabaleiro de la Hoz and Fioriti 2021][research_cabaleirodelahoz_fioriti_2021]
- [Cadwell][research_cadwell]
- [Cai et al 2021][research_cai_xie_2021]
- [Calculation of Low Aspect Ratio Wing Aerodynamics by Using Nonlinear Vortex Lattice Method 2008][research_calculation_of_2008]
- [Calderon et al 2012][research_calderon_aupoix_2012]
- [Calise][research_calise]
- [Calise 2000][research_calise_2000]
- [Calise et al 1998][research_calise_lee_1998]
- [Calise et al 2001][research_calise_lee_2001]
- [Callaghan and Kunz 2019][research_callaghan_kunz_2019]
- [Callaghan and Kunz 2021][research_callaghan_kunz_2021]
- [Cameron and Cameron 1997][research_cameron_cameron_1997]
- [Cameron and Princen 2000][research_cameron_princen_2000]
- [Cameron et al 2003][research_cameron_thomson_2003]
- [Campbell 1957 Turbulence in the Wake of a Thin Airfoil at Low Speeds][research_campbell_1957]
- [Campbell 1958][research_campbell_1958]
- [Campbell 1959][research_campbell_1959]
- [Campbell et al 2005][research_campbell_carter_2005]
- [Campos 1989][research_campos_1989]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Campos et al 1995][research_campos_fonseca_1995]
- [Candon et al 2019][research_candon_levinski_2019]
- [Cao and Lyu 2024][research_cao_lyu_2024]
- [Cao et al 2025][research_cao_lin_2025]
- [Capello et al 2011][research_capello_guglieri_2011]
- [Capello et al 2019][research_capello_ferrero_2019]
- [Capone and Mason 1986][research_capone_mason_1986]
- [Capone et al 1983][research_capone_mason_1983]
- [Carlsen 1995][research_carlsen_1995]
- [Carlsson 2003][research_carlsson_2003]
- [Carlsson 2005][research_carlsson_2005]
- [Carnduff et al 2009][research_carnduff_erbsloeh_2009]
- [Carpenter et al 2008][research_carpenter_saric_2008]
- [Carpenter et al 2018][research_carpenter_solomon_2018]
- [Carrese et al 2016][research_carrese_marzocca_2016]
- [Carter et al 2006][research_bwb_bli_2006]
- [Carter et al 2008][research_carter_campbell_2008]
- [Cassaro et al 2018][research_cassaro_roos_2018]
- [Castaldi et al 2020][research_castaldi_mimmo_2020]
- [Castellani et al 2016][research_castellani_cooper_2016]
- [Cathey 1979][research_cathey_1979]
- [Caughey 1976][research_caughey_1976]
- [Caughey 1982][research_caughey_1982]
- [Caughey and Jameson 1977][research_caughey_jameson_1977]
- [Cavalcanti et al 2026][research_cavalcanti_2026]
- [Cavallaro and Bombardieri 2019][research_cavallaro_bombardieri_2019]
- [Cavanaugh 2003][research_cavanaugh_2003]
- [Celik and Roberts 1992][research_celik_roberts_1992]
- [Cen et al 2020][research_cen_li_2020]
- [Cenko and Madson 1993][research_cenko_madson_1993]
- [Chaderjian 1992][research_chaderjian_1992]
- [Chaderjian and Schiff 1993][research_chaderjian_schiff_1993]
- [Chai Xue et al 2010][research_chaixue_wangganglin_2010]
- [Chakravarty 1987][research_chakravarty_1987]
- [Chalk 1963][research_chalk_1963]
- [Chalk 1964][research_chalk_1964]
- [Chalk 1983][research_chalk_1983]
- [Chalk 1986][research_chalk_1986]
- [Chalk and Wilson 1968][research_chalk_wilson_1968]
- [Chalk and Wilson 1969][research_chalk_wilson_1969]
- [Chalk et al 1969][research_chalk_neal_1969]
- [Chaloner and Verdinelli 1995][research_chaloner_verdinelli_1995]
- [Chambers and Hall 2003][research_uncommanded_lateral_2003]
- [Champine et al 1958][research_champine_kraft_1958]
- [Chan et al 1976][research_chan_chen_1976]
- [Chan et al 2017][research_chan_hooker_2017]
- [Chandrasekharan et al 2015][research_chandrasekharan_iarocci_2015]
- [Chang and Muirhead 1987][research_chang_muirhead_1987]
- [Chang and Muirhead 1987][research_chang_muirhead_1987_b]
- [Chang et al 2004][research_chang_cho_2004]
- [Chang et al 2009][research_chang_ye_2009]
- [Chao et al 2017][research_chao_flanagan_2017]
- [Chaparro et al 2016][research_chaparro_fujiwara_2016]
- [Chapter 12. Control of Longitudinal Motions of Aircraft 1994][research_chapter_12_1994]
- [Chapter 13. Control of Lateral Motions of Aircraft 1994][research_chapter_13_1994]
- [Chapter 6. Lateral-Directional Motions 2005][research_chapter_6_2005]
- [Chapter 7. Coupled Longitudinal and Lateral-Directional Motions 2005][research_chapter_7_2005]
- [Chapter 8 The Aircraft Wing Rock Instability 2025][research_chapter_8_2025]
- [Chaudhuri and Nagaraja 1958][research_chaudhuri_nagaraja_1958]
- [Chaudhuri et al 2018][research_chaudhuri_jasa_2018]
- [Chavatzopoulos et al 2012][research_chavatzopoulos_giotis_2012]
- [Chavez and Vogel 2003][research_chavez_vogel_2003]
- [Chen 1982][research_chen_1982]
- [Chen 2018][research_chen_2018]
- [Chen and Boothe 1974][research_chen_boothe_1974]
- [Chen and Bui 1990][research_chen_bui_1990]
- [Chen and Lee 2008][research_chen_lee_2008]
- [Chen and Lin 2021][research_chen_lin_2021]
- [Chen and Valasek 1999][research_chen_valasek_1999]
- [Chen and Xie 2024][research_chen_xie_2024]
- [Chen et al 2001][research_chen_khalid_2001]
- [Chen et al 2019][research_chen_sun_2019]
- [Chen et al 2021][research_chen_shi_2021]
- [Chen et al 2024][research_chen_li_2024]
- [Chen et al 2025][research_chen_zhang_2025]
- [Chen et al 2025][research_chen_zhang_2025_b]
- [Chen et al 2026][research_chen_gray_2026]
- [Chen et al 2026][research_chen_zhang_2026]
- [Cheney 1988][research_cheney_1988]
- [Cheng 1982][research_cheng_1982]
- [Cheng 2009][research_cheng_2009]
- [Cheng et al 1980][research_cheng_meng_1980]
- [Cheng et al 2025][research_cheng_cea_2025]
- [Chevalier 1982][research_chevalier_1982]
- [Chevalier and Burke 1972][research_chevalier_burke_1972]
- [Chin 1992][research_chin_1992]
- [Chin and Lentink 2019][research_chin_lentink_2019]
- [Chipman et al 1984][research_chipman_rauch_1984]
- [Chiu][research_chiu]
- [Chng and Tsai 2008][research_chng_tsai_2008]
- [Choe et al 2010][research_choe_xargay_2010]
- [Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]
- [Chowdhury et al 2021][research_chowdhury_keshmiri_2021]
- [Chowhan et al 2019][research_chowhan_arya_2019]
- [Christison Gray and Martins 2026][research_christisongray_martins_2026]
- [Christophersen and Spahr 1944][research_christophersen_spahr_1944]
- [Chuan et al 2016][research_chuan_feng_2016]
- [Chung 2007][research_chung_2007]
- [Chung 2017][research_chung_2017]
- [Chung et al 2002][research_chung_lee_2002]
- [Chung et al 2003][research_chung_lee_2003]
- [Chung et al 2010][research_chung_hallberg_2010]
- [Chung et al 2019][research_chung_ma_2019]
- [ChunSheng Liu et al 2012][research_chunshengliu_xinzhongzhu_2012]
- [Church 1954][research_church_1954]
- [Chyczewski 2017][research_chyczewski_2017]
- [Ciliberti and Nicolosi 2026][research_ciliberti_nicolosi_2026]
- [Ciliberti et al 2017][research_ciliberti_dellavecchia_2017]
- [Citurs 1984][research_citurs_1984]
- [Clark and Gerhold 1999][research_clark_gerhold_1999]
- [Clark and Hodapp 1972][research_clark_hodapp_1972]
- [Clarke et al 2005][research_clarke_allen_2005]
- [Clarke et al 2018][research_clarke_burken_2018]
- [Claudia Alice 2010][research_claudiaalice_2010]
- [Cleary and Gray 1947][research_cleary_gray_1947]
- [Clevenson and Thompson 1957][research_clevenson_thompson_1957]
- [Coe et al 1975][research_coe_graham_1975]
- [Cole 1986][research_cole_1986]
- [Cole 1988][research_cole_1988]
- [Cole 1990][research_cole_1990]
- [Cole et al 2003][research_cole_noll_2003]
- [Coletti and Faruque 2022][research_coletti_faruque_2022]
- [Colgren and Loschke 2008][research_colgren_loschke_2008]
- [Colgren and Martin 2000][research_colgren_martin_2000]
- [Collar 1946][research_collar_1946]
- [Comments, with reply, on 'Fuzzy logic for control of roll and moment for a flexible wing aircraft' by S. Chiu et al 1992][research_comments_with_1992]
- [Complete model of aircraft perturbed motion][research_complete_model]
- [Conceptual and Preliminary Design of Flight Control Systems 2017][research_conceptual_and_2017]
- [Conference on Aircraft Aerodynamics 1966][research_conference_on_1966]
- [Configuration Development and Flying Qualities 2021][research_configuration_development_2021]
- [Cong et al 2023][research_cong_hu_2023]
- [Cong et al 2023][research_cong_hu_2023_b]
- [Connelly 1982][research_connelly_1982]
- [Conrad et al 2025][research_conrad_michalka_2025]
- [Consigny et al 1983][research_consigny_gravelle_1983]
- [Contreras-Torres et al 2022][research_contrerastorres_garciarodriguez_2022]
- [Control Allocation and Flight Control System Design 2016][research_control_allocation_2016]
- [Control Characteristics of the Human Pilot 2023][research_control_characteristics_2023]
- [Cook 1997][research_cook_1997]
- [Cook 1997][research_cook_1997_b]
- [Cook 1997][research_cook_1997_c]
- [Cook 1997][research_cook_1997_d]
- [Cook 2007][research_cook_2007]
- [Cook 2007][research_cook_2007_b]
- [Cook 2007][research_cook_2007_c]
- [Cook 2007][research_cook_2007_d]
- [Cook 2013][research_cook_2013]
- [Cook 2013][research_cook_2013_b]
- [Cook 2013][research_cook_2013_c]
- [Cook 2013][research_cook_2013_d]
- [Cook and de Castro 2004][research_cook_decastro_2004]
- [Cooke 1980][research_cooke_1980]
- [Cooney and Schott 1956][research_cooney_schott_1956]
- [Cooper et al 2021][research_cooper_klyde_2021]
- [Coppolino 1952][research_coppolino_1952]
- [Cord 1981][research_cord_1981]
- [Cord 1994][research_cord_1994]
- [Corda et al 1994][research_corda_stephenson_1994]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Corraro et al 2011][research_corraro_morani_2011]
- [Correia et al 2009][research_correia_silva_2009]
- [Cosenza and Kummeth 1974][research_cosenza_kummeth_1974]
- [Costa et al 1994][research_costa_koopman_1994]
- [Costes 1988][research_costes_1988]
- [Cotter 1946][research_cotter_1946]
- [Cotting 2010][research_cotting_2010]
- [Cotting et al 2008][research_cotting_cao_2008]
- [Cotting et al 2019][research_cotting_alt_2019]
- [Coupled Longitudinal and Lateral-Directional Motions 2015][research_coupled_longitudinal_2015]
- [Cousteix and Pailhas 1983][research_cousteix_pailhas_1983]
- [Covell 1985][research_covell_1985]
- [Cox and Jackson 1997][research_cox_jackson_1997]
- [Cox and Jackson 1997][research_cox_jackson_1997_b]
- [Cox and Marshall 2000][research_cox_marshall_2000]
- [Cox et al 1949][research_cox_siddall_1949]
- [Crabill 1956][research_crabill_1956]
- [Craig 1991][research_craig_1991]
- [Crandall and Swanson 1944][research_crandall_swanson_1944]
- [Crane 1948][research_crane_1948]
- [Crane and Beckhardt 1948][research_crane_beckhardt_1948]
- [Crane and Reeder 1945][research_crane_reeder_1945]
- [Crane and Sommer 1961][research_crane_sommer_1961]
- [Crassidis 2005][research_crassidis_2005]
- [Craun et al 2013][research_craun_acosta_2013]
- [Craun et al 2013][research_craun_acosta_2013_b]
- [Creer et al 1959][research_creer_1959]
- [Crider 2004][research_crider_2004]
- [Crisalli et al 1979][research_crisalli_stahara_1979]
- [Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]
- [Cromwell and Koven 1965][research_cromwell_koven_1965]
- [Croom and Huffman 1957][research_croom_huffman_1957]
- [Croom et al 1988][research_croom_whipple_1988]
- [Crother et al 1973][research_crother_gabelman_1973]
- [Crouch et al 2008][research_crouch_garbaruk_2008]
- [Crouch et al 2018][research_crouch_garbaruk_2018]
- [Crouch et al 2019][research_crouch_2019]
- [Crowe 1937][research_crowe_1937]
- [Cruz and Ware 1995][research_cruz_ware_1995]
- [Cui et al 2016][research_cui_yang_2016]
- [Cui et al 2026][research_cui_zhang_2026]
- [Culler and Farnsworth 2019][research_culler_farnsworth_2019]
- [Cunningham 1972][research_cunningham_1972]
- [Cunningham et al 2019][research_cunningham_shah_2019]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Currao and Yeh 2026][research_currao_yeh_2026]
- [Curry and Curry 1997][research_curry_curry_1997]
- [Curry and Sim 1982][research_curry_sim_1982]
- [Curry et al 1989][research_curry_moulton_1989]
- [Curry et al 1990][research_curry_moulton_1990]
- [Cusher and Gopalarathnam 2006][research_cusher_gopalarathnam_2006]
- [Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]
- [Cárdenas et al 2009][research_cardenas_boschetti_2009]
- [D'Aguanno et al 2021][research_daguanno_schrijer_2021]
- [D'Aguanno et al 2022][research_daguanno_campspons_2022]
- [D'Aguanno et al 2022][research_daguanno_schrijer_2022]
- [D'Aiutolo 1954][research_daiutolo_1954]
- [D'Aiutolo and Parker 1952][research_daiutolo_parker_1952]
- [D'Ewart et al 1958][research_dewart_jr_1958]
- [Dabney 2012][research_dabney_2012]
- [Dahiya 2017][research_dahiya_2017]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Dallery 1987][research_dallery_1987]
- [Damstrom and Mayes 1970][research_damstrom_mayes_1970]
- [Damstrom and Mayes 1971][research_damstrom_mayes_1971]
- [Damveld 2004][research_damveld_2004]
- [Dander 1962][research_dander_1962]
- [Dandois 2016][research_dandois_2016]
- [Dandwani et al 2025][research_dandwani_bragadoaldana_2025]
- [Danek 2002][research_danek_2002]
- [Danforth and O'Bryan 1951][research_danforth_obryan_1951]
- [Dang and Yang 2010][research_dang_yang_2010]
- [Dang et al 2019][research_dang_zhao_2019]
- [Danowsky et al 2008][research_danowsky_thompson_2008]
- [Danowsky et al 2017][research_danowsky_schmidt_2017]
- [Danowsky et al 2018][research_danowsky_kotikalpudi_2018]
- [Dantzig 1975][research_dantzig_1975]
- [Davenport and Leggett 1993][research_davenport_leggett_1993]
- [Davey et al 2016][research_davey_gordon_2016]
- [Davies 2020][research_davies_2020]
- [Davies 2025][research_davies_2025]
- [Davis 1952][research_davis_1952]
- [Davis 1969][research_davis_1969]
- [Davis and Harris 1973][research_davis_harris_1973]
- [Dawson and Maxwell 2003][research_dawson_maxwell_2003]
- [Dawson and Maxwell 2005][research_dawson_maxwell_2005]
- [Day 1953][research_richardeday_1953]
- [de Araujo et al 1997][research_dearaujo_singh_1997]
- [de Becdelievre and Kroo 2021][research_debecdelievre_kroo_2021]
- [de Carvalho Pereira and Júnior 2003][research_decarvalhopereira_junior_2003]
- [de Divitiis 2005][research_dedivitiis_2005]
- [de Melo et al 2024][research_demelo_bussamra_2024]
- [de Padua et al 2026][research_depadua_preisigheviana_2026]
- [de Vries and Van Kampen 2019][research_devries_vankampen_2019]
- [Dean et al 2008][research_dean_morton_2008]
- [Deb et al 2006][research_deb_gangtao_2006]
- [DeBusk et al 2009][research_debusk_johnson_2009]
- [Deck 2004][research_deck_2004]
- [Deck 2005][research_deck_2005]
- [Decker 1951][research_decker_1951]
- [Decker 1952][research_decker_1952]
- [Deepa and Gupta 2023][research_deepa_gupta_2023]
- [Deepa and Sudha 2016][research_deepa_sudha_2016]
- [Deere 2003][research_deere_2003]
- [Definitions of Aerodynamic Stability and Control Derivatives 1997][research_definitions_of_1997]
- [Definitions of Aerodynamic Stability and Control Derivatives 2007][research_definitions_of_2007]
- [Definitions of Aerodynamic Stability and Control Derivatives 2013][research_definitions_of_2013]
- [Dehaan 1990][research_dehaan_1990]
- [Delany 1942][research_delany_1942]
- [DeLaurier 2022][research_delaurier_2022]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Demourant and Ferreres 2013][research_demourant_ferreres_2013]
- [Dempster and Arnold 1969][research_dempster_arnold_1969]
- [Denegri 2000][research_denegri_2000]
- [Deneke et al 2026][research_deneke_carter_2026]
- [Deng et al 2023][research_deng_zhang_2023]
- [Denieul][research_denieul]
- [Denieul et al 2015][research_denieul_alazard_2015]
- [Deodhare and Vidyasagar][research_deodhare_vidyasagar]
- [Deppe et al 1996][research_deppe_chalk_1996]
- [Desai et al 1977][research_desai_viswanathan_1977]
- [Deshpande and Zhang 2021][research_deshpande_zhang_2021]
- [Design of Control Surfaces 2012][research_design_of_2012]
- [Deslich et al 2021][research_deslich_flick_2021]
- [Deters and Russell 1947][research_deters_russell_1947]
- [Development and flight evaluation of an augmented stability active controls concept with a small tail 1980][research_development_and_1980]
- [Development of a Continuous Full Flight-Envelope Simulation from System Identification Models 2012][research_development_of_2012]
- [Development of Longitudinal and Lateral-Directional Transfer Functions 2014][research_development_of_2014]
- [Development of Longitudinal and Lateral-Directional Transfer Functions 2024][research_development_of_2024]
- [Development of Neo-Ptero Tailless Micro Aircraft 2018][research_development_of_2018]
- [Devesa et al 2004][research_devesa_jourdan_2004]
- [Devi 2019][research_devi_2019]
- [Deyoung 1979][research_deyoung_1979]
- [Di Fabbio et al 2022][research_difabbio_tangermann_2022]
- [Di Pasquale 2024][research_dipasquale_2024]
- [Di Pasquale and Prince 2023][research_dipasquale_prince_2023]
- [Dias 2022][research_dias_2022]
- [Dias 2023][research_dias_2023]
- [Dias et al 2023][research_dias_budisic_2023]
- [Dicarlo et al 1992][research_dicarlo_brown_1992]
- [Didomenico and Biezad 1985][research_didomenico_biezad_1985]
- [Diederich 1954][research_diederich_1954]
- [DiFranco 1967][research_difranco_1967]
- [Difranco 1969][research_difranco_1969]
- [Difranco 1970][research_difranco_1970]
- [DiMaggio et al 2023][research_dimaggio_hartfield_2023]
- [Dimopoulos et al 2019][research_dimopoulos_panagiotou_2019]
- [Dingeldein 1944][research_dingeldein_1944]
- [Directional Control 2003][research_directional_control_2003]
- [Dixon 1972][research_dixon_1972]
- [Dodbele and Plotkin 1985][research_dodbele_plotkin_1985]
- [Dodd and Pratt 1970][research_dodd_pratt_1970]
- [Dodd and Pratt 1971][research_dodd_pratt_1971]
- [Dogan and Kaewchay 2007][research_dogan_kaewchay_2007]
- [Doggett and Soistmann 1989][research_doggett_soistmann_1989]
- [Doggett and Soistmann 1992][research_doggett_soistmann_1992]
- [Doko and Sasongko 2026][research_doko_sasongko_2026]
- [Dollyhigh 1970][research_dollyhigh_1970]
- [Doman 1995][research_doman_1995]
- [Doman and Oppenheimer 2002][research_doman_oppenheimer_2002]
- [Donaldson 1986][research_donaldson_1986]
- [Donegan 1984][research_donegan_1984]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2020][research_dong_shi_2020]
- [Dong et al 2022][research_dong_liu_2022]
- [Dong et al 2022][research_dong_low_ar_2022]
- [Dong et al 2025][research_dong_zhou_2025]
- [Dongmo 2011][research_dongmo_2011]
- [Donlan 1944][research_tailless_interim_1944]
- [Donlan 1976][research_donlan_1976]
- [Donlan 1976][research_donlan_collected_1976]
- [Donlan and Kuhn 1976][research_tailless_transonic_est_1976]
- [Donlan et al 1976][research_donlan_kemp_1976]
- [Dou et al 2025][research_dou_li_2025]
- [Doubrava et al 2008][research_doubrava_waszniowski_2008]
- [Douglas Aircraft Co Long Beach Ca 1963][research_douglasaircraftcolongbeachca_1963]
- [Dowell 1996][research_dowell_1996]
- [Dowell 1999][research_dowell_1999]
- [Dowell and Assael 2025][research_dowell_assael_2025]
- [Dracopoulos and Oz 1992][research_dracopoulos_oz_1992]
- [Drake 1965][research_drake_1965]
- [Drake and McKay 1953][research_drake_mckay_1953]
- [Drake and Williams 1958][research_williams_drake_1948]
- [Drake et al 1948][research_drake_mclaughlin_1948]
- [Drake et al 1955][research_drake_finch_1955]
- [Draper 1943][research_draper_1943]
- [Drewiacki et al 2016][research_drewiacki_silvestre_2016]
- [Drewiacki et al 2020][research_drewiacki_josesilvestre_2020]
- [Drinkwater et al 1970][research_drinkwater_1970]
- [Driscoll 1966][research_driscoll_1966]
- [Driver 1958][research_driver_1958]
- [Driver and Spearman 1959][research_driver_spearman_1959]
- [Dufaure De Lajarte 1936 Chief Characteristics and Advantages of Tailless Airplanes][research_delajarte_1936]
- [Duffy 1989][research_duffy_1989]
- [Dugan 1959][research_dugan_1959]
- [Dugundji and Ghareeb 1965][research_dugundji_ghareeb_1965]
- [Duncan 1934][research_duncan_1934]
- [Duncan 1950][research_duncan_1950]
- [Duncan et al 2013][research_duncan_crawford_2013]
- [Dunning 1957][research_dunning_1957]
- [Duraffourg et al 2013][research_duraffourg_burlion_2013]
- [Duran 2026][research_duran_2026]
- [Durham et al 2016][research_durham_bordignon_2016]
- [Dvorak and Choi 1982][research_dvorak_choi_1982]
- [Dvorak and Choi 1983][research_dvorak_choi_1983]
- [Dynamic Lateral-Directional Stability Theory and Flight Test Methods 2003][research_dynamic_lateral_directional_2003]
- [Dynamic Longitudinal Stability Flight Test Methods and Data Reduction 2003][research_dynamic_longitudinal_2003]
- [Dynamic Longitudinal Stability Theory 2003][research_dynamic_longitudinal_2003_b]
- [Dynamics of Flexible Aircraft with Quasi-Steady Deformations 2023][research_dynamics_of_2023_b]
- [Dynamics of Very Flexible Aircraft 2023][research_dynamics_of_2023]
- [Eastep et al 1998][research_eastep_andersen_1998]
- [Eastep et al 2001][research_eastep_andersen_2001]
- [Eberhardt and Ward 1999][research_eberhardt_ward_1999]
- [Edwards 1992][research_edwards_1992]
- [Edwards 2008][research_edwards_2008]
- [Edwards et al 1997][research_edwards_fittante_1997]
- [Edwards et al 2009][research_edwards_spain_2009]
- [Effect of sting plunging on measured nonlinear pitch damping 1978][research_effect_of_1978]
- [Effect of wind shear on the airspeed during the airplane landing approach 1990][research_effect_of_1990]
- [Efremov et al 2020][research_efremov_2020]
- [Efremov et al 2022][research_efremov_shcherbakov_2022]
- [Eggleston 1956][research_eggleston_1956]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Ehlers et al 2011][research_ehlers_niedermeier_2011]
- [Eichhorn et al 2022][research_eichhorn_fritzsche_2022]
- [Eichler 1970][research_eichler_1970]
- [Ekaterinaris 1995][research_ekaterinaris_1995]
- [El Mobaraky et al 2025][research_elmobaraky_kouiss_2025]
- [Eldredge et al 2009][research_eldredge_wang_2009]
- [Eldridge-Allegra et al 2024][research_eldridgeallegra_roseman_2024]
- [Elenin 2021][research_elenin_2021]
- [Elkhoury 2008][research_elkhoury_2008]
- [Elkhoury 2016][research_elkhoury_2016]
- [ElRamly][research_elramly]
- [Elsayed et al 2007][research_elsayed_scarano_2007]
- [Elzebda et al 1987][research_elzebda_mook_1987]
- [Elzebda et al 1989][research_elzebda_mook_1989]
- [Elzebda et al 1989][research_elzebda_nayfeh_1989]
- [Ema et al 1997][research_ema_mizukura_1997]
- [Emerson and Robinson 1958][research_emerson_robinson_1958]
- [Eney 1967][research_eney_1967]
- [Eney 1968][research_eney_1968]
- [Eney 1969][research_eney_1969]
- [Engelbrecht][research_engelbrecht]
- [Englar 1970][research_englar_1970]
- [Englar 1996][research_englar_1996]
- [English 1953][research_english_1953]
- [English 1954][research_english_1954]
- [English 1955][research_english_1955]
- [English 1955][research_english_1955_b]
- [English 1957][research_english_1957]
- [Enns 1990][research_enns_1990]
- [Enns 2003][research_enns_2003]
- [Enns 2015][research_enns_2015]
- [Eppink 2023][research_eppink_2023]
- [Epstein et al 1989][research_epstein_luntz_1989]
- [Equations, tables, and charts 1953][research_naca_1135]
- [Er-El et al 1989][research_erel_seter_1989]
- [Erickson 1987][research_erickson_1987]
- [Erickson et al 1989][research_erickson_schreiner_1989]
- [Ericsson 1980][research_ericsson_1980]
- [Ericsson 1983][research_ericsson_1983]
- [Ericsson 1984][research_ericsson_1984]
- [Ericsson 1986][research_ericsson_1986]
- [Ericsson 1987][research_ericsson_1987]
- [Ericsson 1987][research_ericsson_1987_b]
- [Ericsson 1988][research_ericsson_1988]
- [Ericsson 1988][research_ericsson_1988_b]
- [Ericsson 1989][research_ericsson_1989]
- [Ericsson 1991][research_ericsson_1991]
- [Ericsson 1993][research_ericsson_1993]
- [Ericsson 1995][research_ericsson_1995]
- [Ericsson 1996][research_ericsson_1996]
- [Ericsson 1996][research_ericsson_1996_b]
- [Ericsson 1996][research_ericsson_1996_c]
- [Ericsson 1997][research_ericsson_1997]
- [Ericsson 1997][research_ericsson_1997_b]
- [Ericsson 1997][research_ericsson_1997_c]
- [Ericsson 1998][research_ericsson_1998]
- [Ericsson 1998][research_ericsson_1998_b]
- [Ericsson 1999][research_ericsson_1999]
- [Ericsson 2000][research_ericsson_2000]
- [Ericsson 2000][research_ericsson_2000_b]
- [Ericsson 2002][research_ericsson_2002]
- [Ericsson and Beyers 2002][research_ericsson_beyers_2002]
- [Ericsson and Ericsson 1997][research_ericsson_ericsson_1997]
- [Ericsson and Hanff 1993][research_ericsson_hanff_1993]
- [Ericsson and King 1990][research_ericsson_king_1990]
- [Ericsson and King 1990][research_ericsson_king_1990_b]
- [Ericsson and Mendenhall 1994][research_ericsson_mendenhall_1994]
- [Ericsson and Reding 1977][research_ericsson_reding_1977]
- [Ericsson and Reding 1985][research_ericsson_reding_1985]
- [Erturk and Dogan 2015][research_erturk_dogan_2015]
- [Erturk et al 2022][research_erturk_ozkan_2022]
- [Esfandabadi and Djavareshkian 2026][research_esfandabadi_djavareshkian_2026]
- [Eshelby 1982][research_eshelby_1982]
- [Esposito and Orlando 2020][research_esposito_orlando_2020]
- [Esteban 2001][research_esteban_2001]
- [Esteban et al 2015][research_esteban_gavilan_2015]
- [Estevadeordal et al 2022][research_estevadeordal_ullah_2022]
- [Estimation and Sensitivity in Flight Control 2026][research_estimation_and_2026]
- [Etkin 1952][research_etkin_1952]
- [Eugeni et al 2020][research_eugeni_mastroddi_2020]
- [Eulrich and Mesiah 1974][research_eulrich_mesiah_1974]
- [Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]
- [Eulrich et al 1978][research_eulrich_govindaraj_1978]
- [Evangelou 1998][research_evangelou_1998]
- [Experience Gained During Development and Testing of the First Swept-Wing Jet Aircraft 2010][research_experience_gained_2010]
- [Experimental investigation of synthetic jet control of wing rock for a flying wing aircraft 2023][research_experimental_investigation_2023]
- [Extension of FLO Codes to Transonic Flow Prediction for Fighter Configurations 1982][research_extension_of_1982]
- [Faber 1958][research_faber_1958]
- [Faber and Crane 1961][research_feel_system_1961]
- [Fairbanks 1927][research_fairbanks_1927]
- [Fairuz Izzuddin Romli et al 2023][research_fairuzizzuddinromli_muhammadaimanmohammadsabri_2023]
- [Falkner 1951][research_falkner_1951]
- [Fan et al 2006][research_fan_zhu_2006]
- [Faraj and Mohammed 2008][research_afaraj_mmohammed_2008]
- [Farhangnia et al 1996][research_farhangnia_guruswamy_1996]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Fasiello et al 2019][research_fasiello_lu_2019]
- [Favaregh and Landman 2006][research_favaregh_landman_2006]
- [Favier et al 1988][research_favier_agnes_1988]
- [Favre 2018][research_favre_2018]
- [Fears et al 1995][research_fears_ross_1995]
- [Fechter and Mills 1988][research_fechter_mills_1988]
- [Feedback Flight Control 2026][research_feedback_flight_2026]
- [Feedback Stability Augmentation 2023][research_feedback_stability_2023]
- [Ferman and Turner 1999][research_ferman_turner_1999]
- [Ferman and Turner 1999][research_ferman_turner_1999_b]
- [Fernand and Downing 1994][research_fernand_downing_1994]
- [Fernandes and Maldonado 2024][research_fernandes_maldonado_2024]
- [Field et al 2002][research_field_armor_2002]
- [Field et al 2004][research_field_rossitto_2004]
- [Fields 1952][research_fields_1952]
- [Figat and Kwiek 2021][research_figat_kwiek_2021]
- [Filzek 1949][research_filzek_1949]
- [Finch and Matranga 1959][research_finch_matranga_1959]
- [Findlay and Findlay 1997][research_findlay_findlay_1997]
- [Fink and Lastinger 1961][research_fink_lastinger_1961]
- [Finn 1944][research_finn_1944]
- [Firsov et al 2017][research_firsov_isaenkov_2017]
- [Fischel and Nugent 1953][research_fischel_nugent_1953]
- [Fischel et al 1957][research_fischel_holleman_1957]
- [Fisher 1954][research_fisher_1954]
- [Fisher and Williams 1958][research_fisher_williams_1958]
- [Fisher et al 1976][research_fisher_stough_1976]
- [Flanagan et al 2019][research_flanagan_chao_2019]
- [Fletcher 1994][research_fletcher_1994]
- [Flight Control 2015][research_flight_control_2015]
- [Flight Control Design 2015][research_flight_control_2015_b]
- [Flight control of an airplane damaged in flight 2000][research_flight_control_of_2000]
- [Flight control system for an airplane 1999][research_flight_control_1999]
- [Flight Dynamics of Elastic Aircraft 2014][research_flight_dynamics_2014]
- [Flight Simulation 2016][research_flight_simulation_2016]
- [Flight TEST Manual 1959][research_flight_test_1959]
- [Flight test results for an advanced technology light airplane 1977][research_flight_test_1977]
- [Flight Test Results Pertaining to the Space Shuttlecraft Symposium Papers 1970][research_flight_test_1970]
- [Florio et al 2019][research_florio_mckibbin_2019]
- [Flow Control and High-Lift Performance for Flying-Wing Unmanned Combat Air Vehicle Configurations by inserting slots 2016][research_flow_control_2016]
- [Flow Field Investigation of a Blended Wing Body in Low Speeds 2023][research_flow_field_2023]
- [Fluid Dynamics Research on Supersonic Aircraft 1998][research_fluid_dynamics_1998]
- [Flying Qualities 2003][research_flying_qualities_2003]
- [Flying Qualities and Flight Testing of the Aeroplane 1998][research_flying_qualities_1998]
- [Flying Qualities Through Variable Conditions 2010][research_flying_qualities_2010]
- [Foa 1942][research_foa_1942]
- [Foch 1992][research_foch_1992]
- [Fonterose and Hall 1996][research_fonterose_hall_1996]
- [Forster and Steijl 2015][research_forster_steijl_2015]
- [Forster et al 2016][research_forster_biava_2016]
- [Fosdick 1970][research_fosdick_1970]
- [Foster 1959][research_foster_1959]
- [Foster et al 1993][research_foster_ross_1993]
- [Foughner and Bensinger 1977][research_foughner_bensinger_1977]
- [Fournis 2022][research_fournis_2022]
- [Fourth High Alpha Conference 1994][research_high_alpha_conf_1994]
- [Fox et al 1991][research_fox_donegan_1991]
- [Franklin 1970][research_franklin_1970]
- [Franklin 1971][research_franklin_1971]
- [Franklin 1971][research_franklin_1971_b]
- [Franklin 1972][research_franklin_1972]
- [Franklin and Miller 1967][research_franklin_miller_1967]
- [Franze et al 2013][research_franze_mattei_2013]
- [Franzmann et al 2021][research_franzmann_leopold_2021]
- [Franzmann et al 2022][research_franzmann_leopold_2022]
- [Franzmann et al 2022][research_franzmann_leopold_2022_b]
- [Fraser 1986][research_fraser_1986]
- [Frazier 1991][research_frazier_1991]
- [Fremaux et al 1993][research_tumbling_characteristics_1993]
- [Fremaux et al 1995][research_fremaux_vairo_1995]
- [Freuler and Hoffmann 1977][research_freuler_hoffmann_1977]
- [Friehmelt 1996][research_friehmelt_1996]
- [Friend and Sakamoto 1978][research_friend_sakamoto_1978]
- [Friend and Sefic 1972][research_friend_sefic_1972]
- [From Tube and Wing to Flying Wing 2013][research_from_tube_2013]
- [Fu et al 2009][research_fu_kirtikar_2009]
- [Fu et al 2021][research_fu_yu_2021]
- [Fujii and Obayashi 1986][research_fujii_obayashi_1986]
- [Fujino and Suzuki 2024][research_fujino_suzuki_2024]
- [Fukuda and Takimoto 2014][research_fukuda_takimoto_2014]
- [Fukumoto et al 2023][research_fukumoto_kouchi_2023]
- [Fukushima and Kawai 2019][research_fukushima_kawai_2019]
- [Fuller and Moorhouse 1982][research_fuller_moorhouse_1982]
- [Fundamentals of Airplane Flight Mechanics 2007][research_fundamentals_of_2007]
- [Fung 1982][research_fung_1982]
- [Funk and Rhyne 1956][research_funk_rhyne_1956]
- [Funk et al 1993][research_johndfunk_corinpbeck_1993]
- [Furey 1980][research_furey_1980]
- [Furlong 1948][research_furlong_1948]
- [Furlong and Bollech 1951][research_furlong_bollech_1951]
- [Furlong and Bollech 1955][research_furlong_bollech_1955]
- [Fuzzy logic for control of roll and moment for a flexible wing aircraft 1991][research_fuzzy_logic_1991]
- [G. The Experimental Aerodynamics of Wings at Transonic and Supersonic Speeds 1957][research_g_the_1957]
- [Gainer 2002][research_gainer_2002]
- [Gal-Or 1992][research_galor_1992]
- [Gal-Or 1994][research_galor_1994]
- [Gal-Or 2001][research_galor_2001]
- [Gal-Or 2003][research_galor_2003]
- [Gallman et al 1988][research_gallman_batina_1988]
- [Gamble and Inman 2016][research_gamble_inman_2016]
- [Gamble and Inman 2018][research_gamble_inman_2018]
- [Gandhi et al 2009][research_gandhi_cooper_2009]
- [Ganesh et al 2021][research_ganesh_keerthi_2021]
- [Gao and Cai 2016][research_gao_cai_2016]
- [Gao and Liu 2021][research_gao_liu_2021]
- [Gao and Smith 2020][research_gao_smith_2020]
- [Gao et al 2018][research_gao_zhang_2018]
- [Gao et al 2019][research_gao_zhang_2019]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2021][research_gao_an_2021_b]
- [Gao et al 2021][research_gao_an_2021_c]
- [Gao et al 2021][research_gao_an_2021_d]
- [Gao et al 2021][research_gao_an_2021_e]
- [Gao et al 2025][research_gao_tyrrell_2025]
- [Garbaruk et al 2021][research_garbaruk_strelets_2021]
- [Garbell 1946][research_garbell_1946]
- [Garcia et al 2001][research_garcia_slingerland_2001]
- [Garcia-Baquero et al 2018][research_garciabaquero_esteban_2018]
- [Gardner 1951][research_gardner_1951]
- [Gardner and Curfman 1947][research_gardner_curfman_1947]
- [Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]
- [Garman and Andrisani 2003][research_garman_andrisani_2003]
- [Garmann and Visbal 2020][research_garmann_visbal_2020]
- [Garmann and Visbal 2021][research_garmann_visbal_2021]
- [Garmann and Visbal 2022][research_garmann_visbal_2022]
- [Garmann and Visbal 2022][research_garmann_visbal_2022_b]
- [Garmann and Visbal 2023][research_garmann_visbal_2023]
- [Garmendia and Mavris 2014][research_garmendia_mavris_2014]
- [Garmendia and Mavris 2015][research_garmendia_mavris_2015]
- [Garmendia and Mavris 2016][research_garmendia_mavris_2016]
- [Garrec and Kubica 2005][research_garrec_kubica_2005]
- [Garren and Kelley 1970][research_garren_kelley_1970]
- [Garrick and Reed 1981][research_garrick_reed_1981]
- [Garris 1943][research_garris_1943]
- [Gatley et al 2006][research_gatley_turner_2006]
- [Gatto 2009][research_gatto_2009]
- [Gatto and Lowenberg 2006][research_gatto_lowenberg_2006]
- [Gautrey and Cook 1998][research_gautrey_cook_1998]
- [Gavilan et al 2015][research_gavilan_vazquez_2015]
- [Gaylor 1984][research_gaylor_1984]
- [Gebhardt 2017][research_gebhardt_2017]
- [Gee 1978][research_gee_1978]
- [General Electric Co Schenectady Ny 1952][research_generalelectriccoschenectadyny_1952]
- [Generally on automatic flight control][research_generally_on]
- [Geoghegan et al 2020][research_geoghegan_giannelis_2020]
- [Gera 1986][research_gera_1986]
- [Gera et al 1981][research_gera_wilson_1981]
- [German Development of the Swept Wing 1935-1945 2010][research_german_development_2010]
- [Gerontakos and Lee 2005][research_gerontakos_lee_2005]
- [Gerren 1995][research_gerren_1995]
- [Gertsen and Shomber 1965][research_gertsen_shomber_1965]
- [Getsov 2018][research_getsov_2018]
- [Ghaffari et al 2002][research_ghaffari_biedron_2002]
- [Ghaffari et al 2002][research_ghaffari_biedron_2002_b]
- [Ghalandari et al 2022][research_ghalandari_2022]
- [Ghasemi et al 2014][research_ghasemi_mosahebi_2014]
- [Ghee et al 1999][research_ghee_gonzalez_1999]
- [Giannelis et al 2019][research_giannelis_murray_2019]
- [Gibbings 1966][research_gibbings_1966]
- [Gibson 1990][research_gibson_1990]
- [Gibson et al 1957][research_gibson_igoe_1957]
- [Gibson et al 1958][research_gibson_herr_1958]
- [Gilbert et al 1982][research_gilbert_schmidt_1982]
- [Gilbreath and Markofski 2001][research_gilbreath_markofski_2001]
- [Giles 1970][research_giles_1970]
- [Giles 1972][research_giles_1972]
- [Gillan 1993][research_gillan_1993]
- [Gillard 1998][research_gillard_1998]
- [Gillard et al 1997][research_gillard_dorsett_1997]
- [Gillette et al 1993][research_gillette_page_1993]
- [Gillis 1957][research_gillis_1957]
- [Gillis and Chapman 1956][research_gillis_chapman_1956]
- [Gillis and Mitchell 1957][research_freeflight_longitudinal_1957]
- [Gilmore et al 2002][research_gilmore_wakayama_2002]
- [Gilyard 1972][research_gilyard_1972]
- [Gilyard 1973][research_gilyard_1973]
- [Gilyard et al 1972][research_gilyard_berry_1972]
- [Gimmestad 1980][research_gimmestad_1980]
- [Giordano de Oliveira Silva and Moennich 2012][research_giordanodeoliveirasilva_moennich_2012]
- [Glauert 1928][research_glauert_1928]
- [Gloss and Washburn 1977][research_gloss_washburn_1977]
- [Goc et al 2023][research_goc_agrawal_2023]
- [Godavarthi et al 2026][research_godavarthi_seo_2026]
- [Goetzendorf-Grabowski and Antoniewski 2016][research_goetzendorfgrabowski_antoniewski_2016]
- [Goland 1952][research_goland_1952]
- [Goman et al 1992][research_goman_khrabrov_1992]
- [Gomec et al 2020][research_gomec_unver_2020]
- [Gong et al 2024][research_gong_gao_2024]
- [Gonzalez and Bazile 2011][research_gonzalez_bazile_2011]
- [Gonzalez and Winkelmann 1993][research_gonzalez_winkelmann_1993]
- [González et al 2010][research_gonzalez_boschetti_2010]
- [Goodman 1949 The Static-Pressure Error of a Wing Airspeed Installation of the McDonnell XF-88 Airplane in Dives to Transonic Speeds][research_goodman_1949]
- [Goodson and King 1949][research_goodson_king_1949]
- [Goorjian et al 1985][research_goorjian_guruswamy_1985]
- [Gopalarathnam et al 1997][research_gopalarathnam_selig_1997]
- [Gopinath 1982][research_gopinath_1982]
- [Gordnier 1991][research_gordnier_1991]
- [Gordnier and Melville 2000][research_gordnier_melville_2000]
- [Goslin and Ho 1989][research_goslin_ho_1989]
- [Gosmann et al 2020][research_gosmann_gabrys_2020]
- [Goud and Dwivedi 2022][research_goud_dwivedi_2022]
- [Goushcha and Sekula 2025][research_goushcha_sekula_2025]
- [Govindarajan and Narasimha 2000][research_govindarajan_narasimha_2000]
- [Graffstein and Maslowski 2019][research_graffstein_maslowski_2019]
- [Graham and McCaskill 1950][research_graham_mccaskill_1950]
- [Granasy 1995][research_granasy_1995]
- [Grantham and Williams 1987][research_grantham_williams_1987]
- [Grantham et al 1976][research_grantham_nguyen_1976]
- [Grantz 1984][research_grantz_1984]
- [Gratton 2007][research_gratton_2007]
- [Gratton 2014][research_gratton_2014]
- [Gratton 2018][research_gratton_2018]
- [Gratton 2018][research_gratton_2018_b]
- [Grauer 2018][research_jaredagrauer_2018]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Graves 1999][research_graves_1999]
- [Gray 2009][research_gray_2009]
- [Gray and Kemper 2009][research_gray_kemper_2009]
- [Green 1988][research_green_1988]
- [Green 2008][research_green_2008]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Green and Mineck 1991][research_green_mineck_1991]
- [Green and Ott 2003][research_green_ott_2003]
- [Greenberg and Sternfield 1944][research_greenberg_sternfield_1944]
- [Greene et al 2014][research_greene_kunz_2014]
- [Greer et al 2021][research_greer_sardahi_2021]
- [Gregory et al 2007][research_gregory_cao_2007]
- [Gregory et al 2011][research_gregory_gadient_2011]
- [Gresham et al 2009][research_gresham_wang_2009_b]
- [Griffin and Jonas 1983][research_griffin_jonas_1983]
- [Grismer and Jenkins 1996][research_grismer_jenkins_1996]
- [Grismer et al 1997][research_grismer_myatt_1997]
- [Grismer et al 2000][research_grismer_kinsey_2000]
- [Gross 2002][research_gross_2002]
- [Gross et al 1986][research_gross_chandler_1986]
- [Grosser 1965][research_grosser_1965]
- [Grossman and Volpe 1977][research_grossman_volpe_1977]
- [Ground testing of X-48B blended wing body concept 2007][research_ground_testing_2007]
- [Gu et al 2008][research_gu_natesan_2008]
- [Guglieri 2012][research_guglieri_2012]
- [Guglieri and Quagliotti 1993][research_guglieri_quagliotti_1993]
- [Guiler][research_guiler]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]
- [Guillaume et al 2011][research_guillaume_gehri_2011]
- [Gumusboga and Iftar 2019][research_gumusboga_iftar_2019]
- [Gunes et al 2025][research_gunes_sel_2025]
- [Gunes et al 2025][research_gunes_sel_2025_b]
- [Gunnarsson 1997][research_gunnarsson_1997]
- [Guo and Ren 2015][research_guo_ren_2015]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2014][research_guo_burley_2014]
- [Guo et al 2026][research_guo_split_rudder_2026]
- [Gupta et al 2016][research_gupta_seiler_2016]
- [Guruswamy 1991][research_guruswamy_1991]
- [Guruswamy and Goorjian 1983][research_guruswamy_goorjian_1983]
- [Guruswamy and Goorjian 1985][research_guruswamy_goorjian_1985]
- [Guruswamy and Tu 1989][research_guruswamy_tu_1989]
- [Guruswamy and Tu 1994][research_guruswamy_tu_1994]
- [Guruswamy et al 1986][research_guruswamy_goorjian_1986]
- [Guy and Hadaway 1955][research_guy_hadaway_1955]
- [Gülsaçan et al 2018][research_gulsacan_sencan_2018]
- [Gümüşboğa and İftar 2020][research_gumusboga_iftar_2020]
- [Ha 1990][research_ha_1990]
- [Haas and Chopra 1988][research_haas_chopra_1988]
- [Haas and Chopra 1990][research_haas_chopra_1990]
- [Habboush and Yildiz 2022][research_habboush_yildiz_2022]
- [Habel and Steinberg 1953][research_habel_steinberg_1953]
- [Hagerman and Hofstetter 1969][research_hagerman_hofstetter_1969]
- [Hahne 1985][research_hahne_1985]
- [Haiping et al 2021][research_haiping_yanjun_2021]
- [Hall 1971][research_hall_1971]
- [Hall 1992][research_hall_1992]
- [Hall et al 1972][research_hall_sholar_1972]
- [Hall et al 1973][research_hall_weingarten_1973]
- [Hall et al 2003][research_hall_woodson_2003]
- [Hall et al 2006][research_hall_lawrence_2006]
- [Hallissy 1956][research_hallissy_1956]
- [Hamel and Jategaonkar 1996][research_hamel_jategaonkar_1996]
- [Hamidani and Kunz 2018][research_hamidani_kunz_2018]
- [Hammer and Garmann 2023][research_hammer_garmann_2023]
- [Hammer et al 2021][research_hammer_garmann_2021]
- [Hammer et al 2023][research_hammer_garmann_2023_b]
- [Hammett et al][research_hammett_reigelsperger]
- [Hammond et al 1984][research_hammond_downing_1984]
- [Hamza and Samir 2020][research_hamza_samir_2020]
- [Han and Cho 2005][research_han_cho_2005]
- [Han and Liu 2026][research_han_liu_2026]
- [Han et al 2023][research_han_liu_2023]
- [Han et al 2025][research_han_zhang_2025]
- [Hancock 1972][research_hancock_1972]
- [Handling qualities 2000][research_handling_qualities_2000]
- [Handling Qualities Analysis 2008][research_handling_qualities_2008]
- [Handling Qualities and Control Loading 2017][research_handling_qualities_2017]
- [Hanin and Barsony-Nagy 1983][research_hanin_barsonynagy_1983]
- [Hanke 2003][research_hanke_2003]
- [Hansen et al 2022][research_hansen_duan_2022]
- [Hansmann and Stumpf 2025][research_hansmann_stumpf_2025]
- [Hansmann and Stumpf 2026][research_hansmann_stumpf_2026]
- [Hanson et al 2011][research_hanson_schaefer_2011]
- [Hao et al 2023][research_hao_ma_2023]
- [Haoyun Fu et al 2009][research_haoyunfu_jinyan_2009]
- [Hardwick and Panella 2017][research_hardwick_panella_2017]
- [Hargrove 1976][research_hargrove_1976]
- [Harkegard][research_harkegard]
- [Harley et al 2009][research_harley_wilde_2009]
- [Harman 1944][research_harman_1944]
- [Harper and Cooper 1984][research_harper_cooper_1984]
- [Harper and Cooper 1986][research_harper_cooper_1986]
- [Harper and Jones 1947][research_harper_jones_1947]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harris 1935][research_thomasaharris_1935]
- [Harris 2000][research_harris_2000]
- [Harris and Black 1996][research_harris_black_1996]
- [Harris and Harris 1997][research_harris_harris_1997]
- [Harris et al 2000][research_harris_gautrey_2000]
- [Harris et al 2016][research_harris_arthurs_2016]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hart 1956][research_hart_1956]
- [Hart 1968][research_hart_1968]
- [Hart 1992][research_hart_1992]
- [Hart and Hartzell 1984][research_hart_hartzell_1984]
- [Hasan and Alam 2013][research_hasan_alam_2013]
- [Hatch and Montgomery 1968][research_hatch_montgomery_1968]
- [Hatch and Montgomery 1969][research_hatch_montgomery_1969]
- [Hauch et al 1995][research_hauch_jacobs_1995]
- [Hauser 1999][research_hauser_1999]
- [Hayabe and Kwak 2025][research_hayabe_kwak_2025]
- [Hayostek and Amitay 2018][research_hayostek_amitay_2018]
- [He et al 2016][research_he_yang_2016]
- [He et al 2018][research_he_aljiboory_2018]
- [He et al 2018][research_he_leprovost_2018]
- [He et al 2020][research_he_song_2020]
- [He et al 2021][research_he_wang_2021]
- [He et al 2022][research_he_hu_2022]
- [He et al 2022][research_he_hu_2022_b]
- [He et al 2023][research_he_hu_2023]
- [Hebbar et al 1992][research_hebbar_platzer_1992]
- [Hebbar et al 1993][research_hebbar_platzer_1993]
- [Heeg and Chwalowski 2017][research_heeg_chwalowski_2017]
- [Hefazi et al 2013][research_hefazi_vore_2013]
- [Heinze 1932][research_heinze_1932]
- [Heiss et al 1992][research_heiss_eberle_1992]
- [Helin and Walker 1985][research_helin_walker_1985]
- [Heltsley and Cline 1979][research_heltsley_cline_1979]
- [Heltsley et al 1981][research_heltsley_crosswy_1981]
- [Hemsch 1989][research_hemsch_1989]
- [Henderson and Huffman 1974][research_henderson_huffman_1974]
- [Henderson and Lavretsky 1999][research_henderson_lavretsky_1999]
- [Henne and Hicks 1978][research_henne_hicks_1978]
- [Hensley et al 1987][research_hensley_creighton_1987]
- [Herdiana et al 2024][research_herdiana_pinindriya_2024]
- [Heron and Myose 2003][research_heron_myose_2003]
- [Heron and Myose 2007][research_heron_myose_2007]
- [Herr et al 2023][research_herr_spinner_2023]
- [Hess][research_hess]
- [Hess 1977][research_hess_1977]
- [Hess 1979][research_hess_1979]
- [Hess 1980][research_hess_1980]
- [Hess 1981][research_hess_1981]
- [Hess 1982][research_hess_1982]
- [Hess 1984][research_hess_1984]
- [Hess 1987][research_hess_1987]
- [Hess 1994][research_hess_1994]
- [Hess 1995][research_hess_1995]
- [Hess 1997][research_hess_1997]
- [Hess 2009][research_hess_2009]
- [Hess 2011][research_hess_2011]
- [Hess 2016][research_hess_2016]
- [Hess 2016][research_hess_2016_b]
- [Hess and Hess 1997][research_hess_hess_1997]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hess and Stout 1997][research_hess_stout_1997]
- [Hgo and Ly 1995][research_hgo_ly_1995]
- [Hicks and Moulton 1988][research_hicks_moulton_1988]
- [Hieser et al 1956][research_hieser_kudlacik_1956]
- [Hill 1987][research_hill_1987]
- [Hillenherms et al 2003][research_hillenherms_schroder_2003]
- [Hirose et al 2007][research_hirose_nagai_2007]
- [Hirsch and McCormick 1965][research_hirsch_mccormick_1965]
- [Hirsch and McCORMICK 1966][research_hirsch_mccormick_1966]
- [Hitachi and Liu 2010][research_hitachi_liu_2010]
- [Hitzel 2017][research_hitzel_2017]
- [Hoadley and Vanderbok 1986][research_hoadley_vanderbok_1986]
- [Hoadley and VanderBok 1988][research_hoadley_vanderbok_1988]
- [Hoag and Schofield 1970][research_hoag_schofield_1970]
- [Hoang and Bui 2019][research_hoang_bui_2019]
- [Hoang and Bui 2019][research_hoang_bui_2019_b]
- [Hoang et al 1993][research_hoang_rediniotis_1993]
- [Hockman and Eisiminger 1948][research_hockman_eisiminger_1948]
- [Hodgkinson 2005][research_hodgkinson_2005]
- [Hodgkinson et al 1982][research_hodgkinson_wood_1982]
- [Hodgkinson et al 1988][research_hodgkinson_skow_1988]
- [Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]
- [Hoff and Gratton 2013][research_hoff_gratton_2013]
- [Hoffler et al 1988][research_hoffler_rao_1988]
- [Hoffman et al 1970][research_hoffman_zvara_1970]
- [Hoh 1988][research_hoh_1988]
- [Hoh and Mitchell 2018][research_hoh_mitchell_2018]
- [Holdaway 1954][research_holdaway_1954]
- [Holgate and Roskam 1968][research_holgate_roskam_1968]
- [Holleman and Gilyard 1972][research_holleman_gilyard_1972]
- [Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]
- [Hollister 1990][research_hollister_1990]
- [Holowicz and Holleman 1958][research_holowicz_holleman_1958]
- [Holst 1988][research_holst_1988]
- [Holst and Thomas 1982][research_holst_thomas_1982]
- [Holzapfel et al 2006][research_holzapfel_dacosta_2006]
- [Hong 1993][research_hong_1993]
- [Hong and Ma 2016][research_hong_ma_2016]
- [Hooker 2023][research_hooker_2023]
- [Hoot 1924][research_hoot_1924]
- [Hoover 1943][research_hoover_1943]
- [Hopkins and Lovette 1977][research_hopkins_lovette_1977]
- [Hopkins et al 1998][research_hopkins_henderson_1998]
- [Horizontal Tail Loads 1996][research_horizontal_tail_1996]
- [Hosangadi et al 2015][research_hosangadi_paul_2015]
- [Hoshi et al 2020][research_hoshi_kuya_2020]
- [Hosseini et al 2025][research_hosseini_hofmann_2025]
- [Hou et al 2022][research_hou_lv_2022]
- [Houbolt and Williamson 1975][research_houbolt_williamson_1975]
- [Hougui et al 1995][research_hougui_balas_1995]
- [House and Wallace 1941][research_house_wallace_1941]
- [Houtman et al 2023][research_houtman_timme_2023]
- [Houtman et al 2023][research_houtman_vevek_2023]
- [Howard et al 1996][research_howard_bray_1996]
- [Howard et al 2002][research_howard_demoss_2002]
- [Howell][research_howell]
- [Howell and Korst 1971][research_howell_korst_1971]
- [Hsu and Lan 1984][research_hsu_lan_1984]
- [Hsu and Lan 1985][research_hsu_lan_1985]
- [Hu][research_hu]
- [Hu 1992][research_hu_1992]
- [Hu 1995][research_hu_1995]
- [Hu et al 2024][research_hu_tailless_review_2024]
- [Hu et al 2025][research_hu_zhao_2025]
- [Huang and Chow 1996][research_huang_chow_1996]
- [Huang and Cummings 2021][research_huang_cummings_2021]
- [Huang and Hanff 1999][research_huang_hanff_1999]
- [Huang and Zhang 2020][research_huang_zhang_2020]
- [Huang et al 2000][research_huang_lou_2000]
- [Hubbell][research_hubbell]
- [Huber 1995][research_huber_1995]
- [Huber 2022][research_huber_2022]
- [Huber and Holdridge 1979][research_huber_holdridge_1979]
- [Huehne et al 2013][research_huehne_mahmood_2013]
- [Huff 1949][research_huff_ww_1949]
- [Huffman 1975][research_huffman_1975]
- [Hughes and Mennell 1974][research_hughes_mennell_1974]
- [Hui and Tobak 1985][research_hui_tobak_1985]
- [Huijts and Voskuijl 2015][research_huijts_voskuijl_2015]
- [Hull and Roger 1975][research_hull_roger_1975]
- [Hulshoff et al 1996][research_hulshoff_mulder_1996]
- [Humayun et al 2013][research_humayun_wang_2013]
- [Humphreys-Jennings et al 2019][research_humphreysjennings_lappas_2019]
- [Humphreys-Jennings et al 2020][research_humphreys_2020]
- [Hunn 1953][research_hunn_1953]
- [Hunsaker et al 2019][research_hunsaker_montgomery_2019]
- [Hunsaker et al 2020][research_hunsaker_montgomery_2020]
- [Hunter 1948][research_hunter_1948]
- [Hunter 1959][research_hunter_1959]
- [Hunter and Reeder 1946][research_hunter_reeder_1946]
- [Huo et al 2006][research_huo_ioannou_2006]
- [Hurt and Whitten 1960][research_pitchup_control_1960]
- [Hussain and Bons 2019][research_hussain_bons_2019]
- [Huston 1948][research_huston_1948]
- [Hwang and Pi 1975][research_hwang_pi_1975]
- [Hwang and Pi 1975][research_hwang_pi_1975_b]
- [Hwang and Pi 1978][research_hwang_pi_1978]
- [Hwang and Pi 1978][research_hwang_pi_1978_b]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang and Pi 1979][research_hwang_pi_1979_b]
- [Hwang et al 1991][research_hwang_chen_1991]
- [Hwang et al 2002][research_hwang_park_2002]
- [Ibrahim et al 2023][research_ibrahim_kamal_2023]
- [Ide et al 2019][research_ide_ishida_2019]
- [Ijaz et al 2019][research_ijaz_hamayun_2019]
- [Ijaz et al 2019][research_ijaz_hamayun_2019_b]
- [Ikard 1956 An Air-Flow-Direction Pickup Suitable for Telemetering Use on Pilotless Aircraft][research_ikard_1956]
- [Iliff and Maine 1982][research_iliff_maine_1982]
- [Iliff and Powers 1969][research_iliff_powers_1969]
- [Iliff and Wang 1996][research_iliff_wang_1996]
- [Iliff and Wang 1997][research_iliff_wang_1997]
- [Iliff and Wang 1999][research_iliff_wang_1999]
- [Illi et al 2013][research_illi_fingskes_2013]
- [Iloputaife and Iloputaife 1997][research_iloputaife_iloputaife_1997]
- [Imai 1964][research_imai_1964]
- [Immordino et al 2025][research_immordino_vaiuso_2025]
- [Inertia Coupling and Spin 2004][research_inertia_coupling_2004]
- [Inertia Coupling and Spin 2015][research_inertia_coupling_2015]
- [Iniguez de Heredia and Friehmelt 2005][research_iniguezdeheredia_friehmelt_2005]
- [Initial Tail Sizing 2013][research_initial_tail_2013]
- [Integrated Application of Active Controls IAAC technology to an advanced subsonic transport project-longitudinal handling qualities study of a relaxed-stability airplane 1983][research_integrated_application_1983]
- [International Standard Atmosphere ISA Table 2017][research_international_standard_2017]
- [Introduction The Flight Control Problem and Our Approach 2017][research_introduction_the_2017]
- [Introduction to Aircraft Flight Mechanics 2024][research_introduction_to_2024]
- [Introduction to Airplane Flight Mechanics][research_introduction_to]
- [Introduction to Stability and Control Flight Testing 2003][research_introduction_to_2003]
- [Invernizzi and Lovera 2018][research_invernizzi_lovera_2018]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Ionita 1996][research_ionita_1996]
- [Iosilevskii 2025][research_iosilevskii_2025]
- [Iovnovich et al 2017][research_iovnovich_raveh_2017]
- [Irfan et al 2026][research_irfan_nanangburhan_2026]
- [Irving 1966][research_irving_1966]
- [Irving 1966][research_irving_1966_b]
- [Irving 1966][research_irving_1966_c]
- [Ishida and Ueshima 2026][research_ishida_ueshima_2026]
- [Ishida et al 2017][research_ishida_hashimoto_2017]
- [Ishihara et al 2010][research_ishihara_benmenahem_2010]
- [Ishola et al 2024][research_ishola_whidborne_2024]
- [Iskrenovic-Momcilovic 2018][research_iskrenovicmomcilovic_2018]
- [Isogai 2013][research_isogai_2013]
- [Isogai 2016][research_isogai_2016]
- [Ito et al 2016][research_ito_endo_2016]
- [Itty and Leith 1992][research_itty_leith_1992]
- [Iwakawa et al 2015][research_iwakawa_furukawa_2015]
- [Iwatani et al 2022][research_iwatani_asada_2022]
- [Iyer et al 1992][research_iyer_spall_1992]
- [Izadi et al 2007][research_izadi_pakmehr_2007]
- [Izquierdo][research_izquierdo]
- [Izumi et al 2015][research_izumi_ogino_2015]
- [Jabbar et al 2026][research_jabbar_setiawan_2026]
- [Jackson 2023][research_jackson_2023]
- [Jackson and Snyder 1966][research_jackson_snyder_1966]
- [Jackson et al 1993][research_jackson_rivers_1993]
- [Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]
- [Jacob 1987][research_jacob_1987]
- [Jacobs 1983][research_jacobs_1983]
- [Jacobs Abbott and Davidson 1942 Investigation of Extreme Leading-Edge Roughness on Thick Low-Drag Airfoils to Indicate Those Critical to Separation][research_jacobs_1942]
- [Jacobs and Bartlett 1981][research_jacobs_bartlett_1981]
- [Jacobsen 2006][research_jacobsen_2006]
- [Jacobson and Lapins 1975][research_jacobson_lapins_1975]
- [Jado-Puente et al 2025][research_jadopuente_brutch_2025]
- [Jagtap et al 2025][research_jagtap_childs_2025]
- [Jahnke and Culick 1990][research_jahnke_culick_1990]
- [Jaiswal and Prakash 2022][research_jaiswal_prakash_2022]
- [Jalovecký and Janů 2010][research_jalovecky_janu_2010]
- [James and Meyn 1994][research_james_meyn_1994]
- [Jameson][research_jameson]
- [Jameson 1973][research_jameson_1973]
- [Jameson 1977][research_jameson_1977]
- [Jameson and Caughey 1977][research_jameson_caughey_1977]
- [Jamwal et al 2018][research_jamwal_hosangadi_2018]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Janardhan et al 2003][research_janardhan_grandhi_2003_b]
- [Janardhan et al 2005][research_janardhan_grandhi_2005]
- [Jang et al 1994][research_jang_kim_1994]
- [Jansen 1980][research_jansen_1980]
- [Jansen and Van Kampen 2025][research_jansen_vankampen_2025]
- [Jansen and Vos 2016][research_jansen_vos_2016]
- [Jarmark and Speyer 1988][research_jarmark_speyer_1988]
- [Jarrah 1989][research_jarrah_1989]
- [Jategaonkar 2005][research_jategaonkar_2005]
- [Jategaonkar et al 1997][research_jategaonkar_monnich_1997]
- [Jategaonkar et al 2004][research_jategaonkar_fischenberg_2004]
- [Javed and Shafi Khan 2019][research_javed_shafikhan_2019]
- [Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]
- [Jenkins 1989][research_jenkins_1989]
- [Jenkins and Kuhl 1977][research_jenkins_kuhl_1977]
- [Jenkins et al 1993][research_jenkins_myatt_1993]
- [Jenks et al 1977][research_jenks_henry_1977]
- [Jenney 1935][research_jenney_1935]
- [Jentzsch et al 2017][research_jentzsch_taubert_2017]
- [Jentzsch et al 2019][research_jentzsch_2019]
- [Jeram and Prasad 2003][research_jeram_prasad_2003]
- [Jeram and Prasad 2003][research_jeram_prasad_2003_b]
- [Jernell 1978][research_jernell_1978]
- [Ji et al 2021][research_ji_kim_2021]
- [Jiang 1999][research_jiang_1999]
- [Jiang et al 2000][research_jiang_an_2000]
- [Jiang et al 2018][research_jiang_tian_2018]
- [Jiang et al 2019][research_jiang_tian_2019]
- [Jiang et al 2019][research_jiang_zhang_2019]
- [Jiang et al 2025][research_jiang_guo_2025]
- [Jiang et al 2026][research_jiang_li_2026]
- [Jianjun Ma et al 2008][research_jianjunma_pengli_2008]
- [Jiayu et al 2024][research_jiayu_yuchao_2024]
- [Jiguang Li et al 2016][research_jiguangli_xinchen_2016]
- [Jingping et al 2011][research_jingping_weiguo_2011]
- [jingwei and jiaming 2020][research_jingwei_jiaming_2020]
- [Jinli and Zhichun 2013][research_jinli_zhichun_2013]
- [Jo et al 2015][research_jo_park_2015]
- [Jo et al 2016][research_jo_park_2016]
- [Johnson 1935][research_johnson_1935]
- [Johnson 1937][research_johnson_1937]
- [Johnson 1946][research_johnson_1946]
- [Johnson 1946 Flight Investigation to Improve the Dynamic Longitudinal Stability and Control-Feel Characteristics of the P-63A-1 Airplane with Closely Balanced Experimental Elevators][research_johnson_p63_1946]
- [Johnson 1948][research_johnson_1948]
- [Johnson 1949][research_johnson_glider_1949]
- [Johnson 1950][research_johnson_1950]
- [Johnson 1951][research_johnson_1951]
- [Johnson 1959][research_johnson_1959]
- [Johnson 1982][research_johnson_1982]
- [Johnson and Boisseau 1953][research_johnson_boisseau_1953]
- [Johnson and Hayes 1953][research_johnson_hayes_1953]
- [Johnson and Lind 2009][research_johnson_lind_2009]
- [Johnson and Weir 1968][research_johnson_weir_1968]
- [Johnson and Weir 1969][research_johnson_weir_1969]
- [Johnson and Yang 1985][research_johnson_yang_1985]
- [Johnston 1992][research_johnston_1992]
- [Johnston 1998][research_johnston_1998]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
- [Jones 1947][research_jones_1947]
- [Jones and Cohen 1976][research_jones_cohen_1976]
- [Jones and Farmer 1959][research_jones_farmer_1959]
- [Jones and Fehlner 1940 Transient Effects of the Wing Wake on the Horizontal Tail][research_jones_fehlner_1940]
- [Jones and Nisbet 1976][research_jones_nisbet_1976]
- [Jones et al 2006][research_jones_franke_2006]
- [Jones et al 2023][research_jones_klyde_2023]
- [Jordan et al 1987][research_jordan_hahne_1987]
- [Joshi and Rickard 1981][research_joshi_rickard_1981]
- [Joshi et al 1998][research_joshi_sreenatha_1998]
- [Jou and Mueller 1985][research_jou_mueller_1985]
- [Juhasz et al 2015][research_juhasz_tischler_2015]
- [Jump and Padfield 2006][research_jump_padfield_2006]
- [Jumper 1983][research_jumper_1983]
- [Jun 2023][research_jun_2023]
- [Jun and Nelson 1987][research_jun_nelson_1987]
- [Junfeng et al 2020][research_junfeng_wuzhou_2020]
- [Jung and Lowenberg 2005][research_jung_lowenberg_2005]
- [Jung and Reimerdes 2003][research_jung_reimerdes_2003]
- [Jurado and McGehee 2019][research_jurado_mcgehee_2019]
- [Justin James Matt et al 2025][research_justinjamesmatt_haiyangchao_2025]
- [Jyothi et al 2006][research_jyothi_bindu_2006]
- [Kaattari 1959][research_kaattari_1959]
- [Kahveci and Ioannou 2010][research_kahveci_ioannou_2010]
- [Kale and Pendharkar 2021][research_kale_pendharkar_2021]
- [Kaletka and Fu 1993][research_kaletka_fu_1993]
- [Kalyankar et al 2024][research_kalyankar_pompe_2024]
- [Kalyankar et al 2025][research_kalyankar_urreiztieta_2025]
- [Kamal et al 2015][research_kamal_aly_2015]
- [Kaminer et al 1996][research_kaminer_howard_1996]
- [Kanazaki and Setoguchi 2023][research_kanazaki_2023]
- [Kanchi et al 2026][research_kanchi_he_2026]
- [Kandil 1992][research_kandil_1992]
- [Kandil 1993][research_kandil_1993]
- [Kandil and Flanagan 1994][research_kandil_flanagan_1994]
- [Kandil and Menzies 1997][research_kandil_menzies_1997]
- [Kandil and Salman 1991][research_kandil_salman_1991]
- [Kandil and Salman 1992][research_kandil_salman_1992]
- [Kandil and Salman 1992][research_kandil_salman_1992_b]
- [Kandil et al 1993][research_kandil_kandil_1993]
- [Kandil et al 1993][research_kandil_kandil_1993_b]
- [Kandil et al 1994][research_kandil_kalisch_1994]
- [Kandil et al 1995][research_kandil_sheta_1995]
- [Kang and Choi 2022][research_kang_choi_2022]
- [Kania et al 2025][research_kania_2025]
- [Kannan and Bhat 2005][research_kannan_bhat_2005]
- [Karagiannis and Astolfi 2007][research_karagiannis_astolfi_2007]
- [Karahan 2026][research_karahan_2026]
- [Karasinski and Robinson 2022][research_karasinski_robinson_2022]
- [Karasu 2015][research_karasu_2015]
- [Karimi Kelayeh and Djavareshkian 2021][research_karimikelayeh_djavareshkian_2021]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karpouzian and Librescu 1992][research_karpouzian_librescu_1992]
- [Karr et al 2005][research_karr_nishita_2005]
- [Karthik et al 1999][research_karthik_tulapurkara_1999]
- [Karunanidhi et al 2022][research_karunanidhi_scholz_2022]
- [Kashiwagura and Shimoyama 2018][research_kashiwagura_shimoyama_2018]
- [Kass 1970][research_kass_1970]
- [Katayanagi 2001][research_katayanagi_2001]
- [Katayanagi 2004][research_katayanagi_2004]
- [Katz 1989][research_katz_1989]
- [Katz 1999][research_katz_1999]
- [Katz and Levin 1984][research_katz_levin_1984]
- [Katz and Levin 1991][research_katz_levin_1991]
- [Katzenmeier et al 2021][research_katzenmeier_vidy_2021]
- [Katzoff 1940][research_katzoff_1940]
- [Katzoff and Sweberg 1942][research_katzoff_sweberg_1942]
- [Kaups et al 1989][research_kaups_mehta_1989]
- [Kawazoe and Morita 2003][research_kawazoe_morita_2003]
- [Kawazoe and Morita 2004][research_kawazoe_morita_2004]
- [Kawazoe et al 2001][research_kawazoe_yorikane_2001]
- [Kaye][research_kaye]
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kazarin et al 2017][research_kazarin_mackunis_2017]
- [Keenan and Kuhlman 1991][research_keenan_kuhlman_1991]
- [Keener 1984][research_keener_1984]
- [Keener 1985][research_keener_1985]
- [Keener et al 1958][research_keener_mcleod_1958]
- [Kefayat and Kamali 2024][research_kefayat_kamali_2024]
- [Kehlet 1954][research_kehlet_1954]
- [Kehlet 1957][research_kehlet_1957]
- [Keidel et al 2017][research_keidel_fasel_2017]
- [Keidel et al 2019][research_keidel_fasel_2019]
- [Keidel et al 2020][research_keidel_fasel_2020]
- [Kelly 1988][research_kelly_1988]
- [Kemp and Becht 1953][research_kemp_becht_1953]
- [Kemp et al 1950][research_kemp_becht_1950]
- [Kemp et al 1966][research_kemp_lockwood_1966]
- [Kempel 1971][research_kempel_1971]
- [Kempel et al 1970][research_robertwkempel_larrywstrutz_1970]
- [Kempel et al 1975][research_kempel_dana_1975]
- [Kempel et al 1988][research_kempel_mcneill_1988]
- [Kendall 2005][research_kendall_2005]
- [Kendall 2018][research_kendall_2018]
- [Kendall and Morgan 2010][research_kendall_morgan_2010]
- [Kennelly et al 1990][research_kennelly_kroo_1990]
- [Kentfield 2006][research_kentfield_2006]
- [Kentfield 2009][research_kentfield_2009]
- [Kentfield and Spragins 2004][research_kentfield_spragins_2004]
- [Khalid 2023][research_khalid_2023]
- [Khan 2019][research_khan_2019]
- [Khan and Bandyopadhyay][research_khan_bandyopadhyay]
- [Khan and Deng 2012][research_khan_deng_2012]
- [Khan et al 2012][research_khan_weiguo_2012]
- [Khan et al 2025][research_khan_shaikh_2025]
- [Khan et al 2026][research_khan_masud_2026]
- [Kharisov and Hovakimyan 2010][research_kharisov_hovakimyan_2010]
- [Kholodar et al 2004][research_kholodar_dowell_2004]
- [Khot et al 1997][research_khot_eastep_1997]
- [Kidd 1988][research_kidd_1988]
- [Kidd and Bull 1963][research_kidd_bull_1963]
- [Kier et al 2020][research_kier_muller_2020]
- [Kikuchi et al 2024][research_kikuchi_kouchi_2024]
- [Kilgore and Adcock 1972][research_kilgore_adcock_1972]
- [Kim and Kunz 2016][research_kim_kunz_2016]
- [Kim and Marciniak 1998][research_kim_marciniak_1998]
- [Kim and Marciniak 1999][research_kim_marciniak_1999]
- [Kim and Marciniak 2000][research_kim_marciniak_2000]
- [Kim and Marciniak 2002][research_kim_marciniak_2002]
- [Kim and Song 2013][research_kim_song_2013]
- [Kim et al 2005][research_kim_rockwell_2005]
- [Kim et al 2013][research_kim_ahn_2013]
- [Kim et al 2025][research_kim_koh_2025]
- [Kimberlin and Sims 1992][research_kimberlin_sims_1992]
- [Kimler and Canfield 2006][research_kimler_canfield_2006]
- [King and Gopalarathnam 2005][research_king_gopalarathnam_2005]
- [Kirkham et al 1974][research_kirkham_jackson_1974]
- [Kirschstein and Alles 2004][research_kirschstein_alles_2004]
- [Kish et al 1996][research_kish_leggett_1996]
- [Kish et al 1997][research_kish_mosle_1997]
- [Kish et al 1997][research_kish_mosle_1997_b]
- [Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]
- [Kitsios et al 2020][research_kitsios_dimopoulos_2020]
- [Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]
- [Kjelgaard and Paulson 1981][research_kjelgaard_paulson_1981]
- [Klausmeyer 2004][research_klausmeyer_2004]
- [Klausmeyer 2018][research_klausmeyer_2018]
- [Klausmeyer 2026][research_klausmeyer_2026]
- [Klausmeyer and Laflin 2023][research_klausmeyer_laflin_2023]
- [Klawans and White 1957 A Method Utilizing Data on the Spiral, Roll-Subsidence, and Dutch Roll Modes for Determining Lateral Stability Derivatives from Flight Measurements][research_klawans_white_1957]
- [Kleckner 1943][research_kleckner_1943]
- [Kleckner 1943][research_kleckner_1943_b]
- [Klein 1979][research_klein_1979]
- [Klein 1999][research_klein_1999]
- [Klein and Batterson 1983][research_klein_batterson_1983]
- [Klein et al 1981][research_klein_batterson_1981]
- [Klein et al 1982][research_klein_lapins_1982]
- [Kleinert et al 2023][research_kleinert_ehrle_2023]
- [Klinar and Jones 1948][research_klinar_jones_1948]
- [Kloker 2008][research_kloker_2008]
- [Klotz et al 2023][research_klotz_thabet_2023]
- [Kluever 2004][research_kluever_2004]
- [Kluever 2007][research_kluever_2007]
- [Klunk and Freeman 2018][research_klunk_freeman_2018]
- [Klyde and Mitchell 1999][research_klyde_mitchell_1999]
- [Klyde and Mitchell 2003][research_klyde_mitchell_2003]
- [Klyde and Mitchell 2004][research_klyde_mitchell_2004]
- [Klyde et al 1996][research_klyde_mcruer_1996]
- [Klyde et al 1997][research_klyde_mcruer_1997]
- [Klyde et al 2002][research_klyde_smith_2002]
- [Klyde et al 2007][research_klyde_bachelder_2007]
- [Klyde et al 2020][research_klyde_schulze_2020]
- [Klyde et al 2020][research_klyde_schulze_2020_b]
- [Knapp et al 1953][research_knapp_jordan_1953]
- [Knight and Wykes 1966][research_knight_wykes_1966]
- [Kobayashi 2002][research_kobayashi_2002]
- [Kock et al 1972][research_kock_1972]
- [Koenig and Rolls 1966][research_koenig_rolls_1966]
- [Koike et al 2016][research_koike_ueno_2016]
- [Kojima and Hashimoto 2023][research_kojima_hashimoto_2023]
- [Kojima et al 2019][research_kojima_kameda_2019]
- [Kolesnikov 2005][research_kolesnikov_2005]
- [Kolonay and Yang 1998][research_kolonay_yang_1998]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Kong et al 2023][research_kong_pan_2023]
- [Konstadinopoulos et al 1985][research_konstadinopoulos_mook_1985]
- [Koreanschi et al 2014][research_koreanschi_oliviu_2014]
- [Koreanschi et al 2016][research_koreanschi_oliviu_2016]
- [Kornev and Pimenov 2022][research_kornev_pimenov_2022]
- [Korthäuer et al 2023][research_korthauer_accorinti_2023]
- [Kotfila and Painter 1969][research_kotfila_painter_1969]
- [Kotikalpudi et al 2018][research_kotikalpudi_danowsky_2018]
- [Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]
- [Koven and Kayten 1946][research_koven_kayten_1946]
- [Kowal and Vakili 1998][research_kowal_vakili_1998]
- [Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]
- [Kownacki 2013][research_kownacki_2013]
- [Kraft and Reeder 1948][research_kraft_reeder_1948]
- [Kraft et al 1948][research_kraft_goranson_1948]
- [Kraft et al 1953][research_kraft_1953]
- [Krekeler et al 1990][research_krekeler_wilson_1990]
- [Krishnaswamy et al][research_krishnaswamy_papageorgiou]
- [Krone 1980][research_krone_1980]
- [Krone 1980][research_krone_1980_b]
- [Kroo 1982][research_kroo_1982]
- [Kroo 1983][research_kroo_1983]
- [Kroo 1994][research_kroo_1994]
- [Kubica and Livet 1994][research_kubica_livet_1994]
- [Kucera and Hromčík 2013][research_kucera_hromcik_2013]
- [Kuehme et al 2014][research_kuehme_alley_2014]
- [Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]
- [Kumada and Sawada 2016][research_kumada_sawada_2016]
- [Kumar and Ghosh 2014][research_kumar_ghosh_2014]
- [Kumar and Ghosh 2023][research_kumar_ghosh_2023]
- [Kumar and Rao 2004][research_kumar_rao_2004]
- [Kumar et al 2020][research_kumar_mandal_2020]
- [Kumar et al 2021][research_kumar_sunil_2021]
- [Kumar et al 2023][research_kumar_okasha_2023]
- [Kumar et al 2025][research_kumar_palanivel_2025]
- [Kun et al 2011][research_kun_lixin_2011]
- [Kurtz et al 2016][research_kurtz_wittig_2016]
- [Kurz and Kloker 2015][research_kurz_kloker_2015]
- [Kusunose et al 1987][research_kusunose_marcum_1987]
- [Kutney and Piszkin 1963][research_kutney_piszkin_1963]
- [Kutney and Piszkin 1964][research_kutney_piszkin_1964]
- [Kuz'min 2007][research_kuzmin_2007]
- [Kuz'min 2009][research_kuzmin_2009]
- [Kuz'min 2010][research_kuzmin_2010]
- [Kuz'min and Shilkin 2009][research_kuzmin_shilkin_2009]
- [Kuzina][research_kuzina]
- [Kuzmina et al 2004][research_kuzmina_ishmuratov_2004]
- [Kwatny et al 1991][research_kwatny_bennett_1991]
- [Kwiek 2019][research_kwiek_2019]
- [Kwiek and Figat 2016][research_kwiek_figat_2016]
- [Köprücü and Öztürk 2024][research_koprucu_ozturk_2024]
- [Laar et al 2024][research_laar_atherstone_2024]
- [Lacey 1979][research_lacey_1979]
- [Lagemann 2024][research_lagemann_2024]
- [Lai et al 2014][research_lai_zhang_2014]
- [Laiq-Ur Rehman 2013][research_laiqurrehman_2013]
- [Laitone 1943][research_tailless_highspeed_1943]
- [Laitone 1978][research_laitone_1978]
- [Laitone 1978][research_laitone_1978_b]
- [Laitone and Vinh 1970][research_laitone_vinh_1970]
- [Lamar 2001][research_lamar_2001]
- [Lamar 2003][research_lamar_2003]
- [Lamar et al 2001][research_johnelamar_cliffordjobara_2001]
- [Lamb et al 1981][research_lamb_sawyer_1981]
- [Lamb et al 1981][research_lamb_sawyer_1981_b]
- [Lampropoulos and Sarris 2025][research_lampropoulos_sarris_2025]
- [Lan and Hsu 1982][research_lan_hsu_1982]
- [Lan et al 1978][research_lan_mehrotra_1978]
- [Lan et al 1995][research_lan_hsu_1995]
- [Lan et al 2002][research_lan_li_2002]
- [Landahl 1959][research_landahl_1959]
- [Lange 1945][research_lange_1945]
- [Lange 1947][research_lange_1947]
- [Langham 1979][research_langham_1979]
- [Langston et al 2016][research_langston_nelson_2016]
- [Langton 2006][research_langton_2006]
- [Lapin et al 1952][research_lapin_crookshanks_1952]
- [Lapins et al 1982][research_lapins_klein_1982]
- [Larrabee and Tymczyszyn 1968][research_larrabee_tymczyszyn_1968]
- [Larson 1986][research_larson_1986]
- [Larson 1987][research_larson_1987]
- [Lateral Control Power Rolling Performance 2003][research_lateral_control_2003]
- [Lateral-Directional Dynamic Modes 2016][research_lateral_directional_dynamic_2016]
- [Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]
- [Lateral-Directional Motion 2016][research_lateral_directional_motion_2016]
- [Lateral-Directional Motions 2015][research_lateral_directional_motions_2015]
- [Lateral-Directional Stability Theory and Flight Test Methods 2003][research_lateral_directional_stability_2003]
- [Lauchle 1974][research_lauchle_1974]
- [Laurence Le Page 1925][research_laurencelepage_1925]
- [Lauten et al 1954][research_lauten_1954]
- [Lawrence and Draper-Donley 2005][research_lawrence_draperdonley_2005]
- [Le Provost et al 2018][research_leprovost_williams_2018]
- [Lee 1946][research_lee_1946]
- [Lee 1947][research_lee_1947]
- [Lee 1985][research_lee_1985]
- [Lee 1990][research_lee_1990]
- [Lee 2000][research_lee_2000]
- [Lee and Batina 1990][research_lee_batina_1990]
- [Lee and Batina 1990][research_lee_batina_1990_b]
- [Lee and Batina 1991][research_lee_batina_1991]
- [Lee and Gross 2024][research_lee_gross_2024]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Pereira 2013][research_lee_pereira_2013]
- [Lee and Pereira 2013][research_lee_pereira_2013_b]
- [Lee and Singh 2013][research_lee_singh_2013]
- [Lee and Vining 2018][research_lee_vining_2018]
- [Lee and Yoon 2008][research_lee_yoon_2008]
- [Lee et al 1986][research_lee_lan_1986]
- [Lee et al 1987][research_lee_lan_1987]
- [Lee et al 1989][research_lee_lan_1989]
- [Lee et al 2001][research_lee_tischler_2001]
- [Lee et al 2008][research_lee_byoungmunmin_2008]
- [Lee et al 2023][research_lee_nam_2023]
- [Leggett and Cord 1994][research_leggett_cord_1994]
- [Legouis et al 1986][research_legouis_laneville_1986]
- [Legriffon et al 2023][research_legriffon_bertsch_2023]
- [Lei and Zha 2023][research_lei_zha_2023]
- [Lei et al 2025][research_lei_zhang_2025]
- [Leishman 2026][research_leishman_2026]
- [LeMay and Lovato 1994][research_lemay_lovato_1994]
- [Lemko and Molodchyk 2015][research_lemko_molodchyk_2015]
- [Lemley and Mullans 1974][research_lemley_mullans_1974]
- [Lemon et al 2011][research_lemon_litt_2011]
- [Lensi 2000][research_lensi_2000]
- [Leonard 2013][research_leonard_2013]
- [Lesiário and Hagström 2010][research_lesiario_hagstrom_2010]
- [Lesoinne 2007][research_lesoinne_2007]
- [Letko 1951][research_letko_1951]
- [Letko and Riley 1950][research_letko_riley_1950]
- [Levi and Nelson 1963][research_levi_nelson_1963]
- [Levi and Nelson 1964][research_levi_nelson_1964]
- [Levin 1981][research_levin_1981]
- [Levinski and Hill 2006][research_levinski_hill_2006]
- [Levison and Rickard 1981][research_levison_rickard_1981]
- [Levy 1992][research_levy_1992]
- [Leylek and Costello 2013][research_leylek_costello_2013]
- [Li 2024][research_li_2024]
- [Li and Ma 2014][research_li_ma_2014]
- [Li et al 1999][research_li_zhu_1999]
- [Li et al 2011][research_li_yu_2011]
- [Li et al 2012][research_li_yu_2012]
- [Li et al 2013][research_li_xu_2013]
- [Li et al 2013][research_li_yang_2013]
- [Li et al 2014][research_li_qu_2014]
- [Li et al 2017][research_li_chen_2017]
- [Li et al 2017][research_li_yong_2017]
- [Li et al 2018][research_li_dong_2018]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2019][research_li_qian_2019]
- [Li et al 2019][research_li_sun_2019]
- [Li et al 2021][research_li_chen_2021]
- [Li et al 2022][research_li_shi_2022]
- [Li et al 2022][research_li_split_rudder_2022]
- [Li et al 2022][research_li_sun_2022]
- [Li et al 2023][research_li_han_2023]
- [Li et al 2023][research_li_liu_2023]
- [Li et al 2023][research_li_sun_2023]
- [Li et al 2023][research_li_wing_rock_2023]
- [Li et al 2024][research_li_han_2024]
- [Li et al 2025][research_li_dai_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_zhang_2025]
- [Li et al 2026][research_li_shu_2026]
- [Li et al 2026][research_li_wei_2026]
- [Li Peng et al 2009][research_lipeng_qinweiwei_2009]
- [Liang et al 2025][research_liang_feng_2025]
- [Liang Qu et al 2016][research_liangqu_yinghui_2016]
- [Liao et al 2002][research_liao_wang_2002]
- [Lichota 2016][research_lichota_2016]
- [Lichota 2023][research_lichota_2023]
- [Lichota et al 2016][research_lichota_ohme_2016]
- [Lichoń 2016][research_lichon_2016]
- [Lichtenstein 1952][research_tail_size_effect_1952]
- [Lichter et al 2009][research_lichter_bateman_2009]
- [Licini et al 2024][research_licini_white_2024]
- [Liddell et al 1947][research_liddell_1947]
- [Liebeck 2002][research_liebeck_2002]
- [Liebeck 2003][research_liebeck_2003]
- [Liebeck 2008][research_liebeck_2008]
- [Liebeck et al 1998][research_liebeck_page_1998]
- [Liebst and Nolan 1993][research_liebst_nolan_1993]
- [Liebst et al 2002][research_liebst_chapa_2002]
- [Liersch and Bishop 2018][research_liersch_bishop_2018]
- [Lijewski 1987][research_lijewski_1987]
- [Lim et al 2025][research_lim_hur_2025]
- [Limache and Cliff 1999][research_limache_cliff_1999]
- [Lin and Hsu 2004][research_lin_hsu_2004]
- [Lin and Lee 2023][research_lin_lee_2023]
- [Lin et al 2017][research_lin_wang_2017]
- [Lin et al 2019][research_lin_zhang_2019]
- [Lin et al 2026][research_lin_zong_2026]
- [Lina and Ricker 1952][research_lina_ricker_1952]
- [Lindley 1956][research_lindley_1956]
- [Lindsay 2021][research_lindsay_2021]
- [Lindsey 1946][research_lindsey_1946]
- [Linear Quadratic Flight Control 2026][research_linear_quadratic_2026]
- [Lingyu et al 2006][research_lingyu_youwu_2006]
- [Lisoski and Kendall 2007][research_lisoski_kendall_2007]
- [Liu 2022][research_liu_2022]
- [Liu 2024][research_liu_2024]
- [Liu and Elham 2019][research_liu_elham_2019]
- [Liu and Gao 2010][research_liu_gao_2010]
- [Liu and Hu 2014][research_liu_hu_2014]
- [Liu and Lone 2013][research_liu_lone_2013]
- [Liu and Wang 2012][research_liu_wang_2012]
- [Liu and Wang 2025][research_liu_wang_2025]
- [Liu and Weng 2007][research_liu_weng_2007]
- [Liu and Whidborne 2021][research_liu_whidborne_2021]
- [Liu and Zhang 2022][research_liu_zhang_rudder_2022]
- [Liu et al 2005][research_liu_zhang_2005]
- [Liu et al 2006][research_liu_zhang_2006]
- [Liu et al 2016][research_liu_wang_2016]
- [Liu et al 2018][research_liu_zhang_2018]
- [Liu et al 2021][research_liu_luo_2021]
- [Liu et al 2022][research_liu_wang_2022]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2026][research_liu_flying_wing_aero_2026]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_lyu_2026]
- [Lock and Rogers 1962][research_lock_rogers_1962]
- [Lockwood 1966][research_lockwood_1966]
- [Lockwood 1974][research_lockwood_1974]
- [Loechert et al 2018][research_loechert_huber_2018]
- [Loeser and Rohlf 2016][research_loeser_rohlf_2016]
- [Lokos et al 2005][research_lokos_lizotte_2005]
- [Lomax et al 1973][research_lomax_bailey_1973]
- [Lombardi et al 1997][research_lombardi_salvetti_1997]
- [Long 1968][research_long_1968]
- [Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]
- [Longitudinal Aircraft Dynamics and the Instantaneous Acceleration Center of Rotation 2011][research_longitudinal_aircraft_2011]
- [Longitudinal Control and Trim Theory and Flight Test Methods 2003][research_longitudinal_control_2003]
- [Longitudinal Dynamics 1998][research_longitudinal_dynamics_1998]
- [Longitudinal Maneuvering Stability Theory 2003][research_longitudinal_maneuvering_2003]
- [Longitudinal Stability 2021][research_longitudinal_stability_2021]
- [Longitudinal Stability Fore and AFT Balance 2014][research_longitudinal_stability_2014]
- [Longitudinal Trim and Stability 2016][research_longitudinal_trim_2016]
- [Lopez et al 1959][research_lopez_buell_1959]
- [Loranchet et al 2025][research_loranchet_tiako_2025]
- [Lorber and Carta 1988][research_lorber_carta_1988]
- [Lorber et al 1991][research_lorber_covino_1991]
- [Lorenzetti et al 1969][research_lorenzetti_nelsen_1969]
- [Lottati 1986][research_lottati_1986]
- [Lotze et al 1975][research_lotze_sensburg_1975]
- [Lowenberg 2010][research_lowenberg_2010]
- [Lowry and Schneiter 1948][research_lowry_schneiter_1948]
- [Lu][research_lu]
- [Lu and Jump 2014][research_lu_jump_2014]
- [Lu and Turkoglu 2016][research_lu_turkoglu_2016]
- [Lu and Turkoglu 2018][research_lu_turkoglu_2018]
- [Lu and Van Kampen 2015][research_lu_vankampen_2015]
- [Lu et al 2019][research_lu_ma_2019]
- [Lu et al 2026][research_lu_lan_2026]
- [Luckring 2003][research_luckring_2003]
- [Luckring and Hiller 2025][research_luckring_hiller_2025]
- [Lucky Bose et al 2024][research_luckybose_isfaqahmedrafsun_2024]
- [Lundstrom 1949][research_lundstrom_1949]
- [Lungu et al 2022][research_lungu_flores_2022]
- [Luo and Lan 1993][research_luo_lan_1993]
- [Luo and Wang 1998][research_luo_wang_1998]
- [Luoma 1953][research_luoma_1953]
- [Lusardi et al 2012][research_lusardi_blanken_2012]
- [Lutze 1980][research_lutze_1980]
- [Lutze and Fan 1998][research_lutze_fan_1998]
- [Lutze et al 1993][research_lutze_durham_1993]
- [Luu 2025][research_luu_2025]
- [Luu and Ochi 2023][research_luu_ochi_2023]
- [Ly 1984][research_ly_1984]
- [Lykins and Keshmiri 2010][research_lykins_keshmiri_2010]
- [Lyu et al 2023][research_lyu_zhang_2023]
- [Ma and Wang 2009][research_ma_wang_2009]
- [Ma et al 2008][research_ma_li_2008]
- [Ma et al 2016][research_ma_deng_2016]
- [Ma et al 2019][research_ma_huang_2019]
- [Ma et al 2019][research_ma_zhu_2019]
- [Ma et al 2025][research_ma_alwi_2025]
- [Macdonald 1984][research_macdonald_1984]
- [Mace and Cosner 1983][research_mace_cosner_1983]
- [Mack 1979][research_mack_1979]
- [Maggin 1944][research_maggin_1944]
- [Magill et al 1994][research_magill_darden_1994]
- [Magness et al 1992][research_magness_robinson_1992]
- [Mahmood 2025][research_mahmood_2025]
- [Mahmood et al 2025][research_mahmood_aasim_2025]
- [Maimako et al 2026][research_maimako_mintah_2026]
- [Maine 1977][research_maine_1977]
- [Maine 1978][research_maine_1978]
- [Maine and Iliff 1979][research_maine_iliff_1979]
- [Maine and Iliff 1982][research_maine_iliff_1982]
- [Malaek and Karimi 2008][research_malaek_karimi_2008]
- [Malaek and Sajjadi Kia 2004][research_malaek_sajjadikia_2004]
- [Malcom 1969][research_malcom_1969]
- [Malcom and Husband 1976][research_malcom_husband_1976]
- [Malik and Li 1993][research_malik_li_1993]
- [Malik et al 2020][research_malik_ricci_2020]
- [Malmuth et al 1983][research_malmuth_wu_1983]
- [Malpica and Lusardi 2013][research_malpica_lusardi_2013]
- [Mamada and Ando 1973][research_mamada_ando_1973]
- [Mamada and Ando 1974][research_mamada_ando_1974]
- [Mamla and Galinski 2009][research_mamla_galinski_2009]
- [Mandal][research_mandal]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Maneuvering Stability Methods and Data Reduction 2003][research_maneuvering_stability_2003]
- [Mann and Mercer 1985][research_mann_mercer_1985]
- [Mann et al 1987][research_mann_huffman_1987]
- [Manning and Gleason 1992][research_manning_gleason_1992]
- [Mansor et al 2015][research_mansor_nogoud_2015]
- [Mansour 1984][research_mansour_1984]
- [Mansour 1985][research_mansour_1985]
- [Maqsood and Go 2011][research_maqsood_go_2011]
- [Marchetti 1968][research_marchetti_1968]
- [Maria-Agneta and Stef 2011][research_mariaagneta_stef_2011]
- [Maricic 2006][research_maricic_2006]
- [Marino and Mastrocola 1948][research_marino_mastrocola_1948]
- [Marino and Mastrocola 1952][research_marino_mastrocola_1952]
- [Marion and Sharma 2025][research_marion_sharma_2025]
- [Markofski and Bailey 1999][research_markofski_bailey_1999]
- [Marques 2013][research_marques_2013]
- [Marschalk et al 2021][research_marschalk_luteijn_2021]
- [Martin 2007][research_martin_2007]
- [Martin 2008][research_martin_2008]
- [Martinez 1961][research_martinez_1961]
- [Martinez-Garcia et al 2017][research_martinezgarcia_gordon_2017]
- [Martos et al 2011][research_martos_kiszely_2011]
- [Martz et al 1987][research_martz_biezad_1987]
- [Martz et al 1988][research_martz_biezad_1988]
- [Marwaha et al 2008][research_marwaha_valasek_2008]
- [Marx 1977][research_marx_1977]
- [Marzouk 2025][research_marzouk_2025]
- [Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]
- [Masini et al 2019][research_masini_timme_2019]
- [Masini et al 2020][research_masini_timme_2020]
- [Mason 1953][research_mason_1953]
- [Mason 1982][research_mason_1982]
- [Massey and Kandil 1998][research_massey_kandil_1998]
- [Mastin et al 1996][research_mastin_smith_1996]
- [Matamoros and de Visser 2018][research_matamoros_devisser_2018]
- [Matheny and Gatlin 1978][research_matheny_gatlin_1978]
- [Matranga 1961][research_matranga_1961]
- [Matranga 1961][research_matranga_1961_b]
- [Matranga and Armstrong 1959][research_matranga_armstrong_1959]
- [Matranga and Menard 1959][research_matranga_menard_1959]
- [Matsuno and Nakamura 2000][research_matsuno_nakamura_2000]
- [Matsuno et al 2003][research_matsuno_yokouchi_2003]
- [Matějů 2019][research_mateju_2019]
- [Maughmer et al 1990][research_maughmer_ozoroski_1990]
- [Mavriplis and Levy 2002][research_mavriplis_levy_2002]
- [Mayer et al 2019][research_mayer_lutz_2019]
- [Mayes et al 1970][research_mayes_lores_1970]
- [Mayya et al 2022][research_mayya_karnick_2022]
- [Mazumder 2024][research_mazumder_2024]
- [McCarley and Lindak 2016][research_mccarley_lindak_2016]
- [McCarty 1982][research_mccarty_1982]
- [McClelland and Woolsey 2020][research_mcclelland_woolsey_2020]
- [McCracken and Jorris 2011][research_mccracken_jorris_2011]
- [McCuish and Caldwell 2018][research_mccuish_caldwell_2018]
- [McFall 1954][research_mcfall_1954]
- [McFall and Hollinger 1953][research_mcfall_hollinger_1953]
- [McFarlane et al 2008][research_mcfarlane_richardson_2008]
- [McKay 1994][research_mckay_1994]
- [McKeehen 1998][research_mckeehen_1998]
- [McKeehen et al 1997][research_mckeehen_myatt_1997]
- [McKelvey 1993][research_mckelvey_1993]
- [McKenzie 1973][research_mckenzie_1973]
- [McKinney 1946][research_mckinney_1946]
- [McKinney 1946][research_mckinney_1946_b]
- [McKinney and Shanks 1948][research_mckinney_shanks_1948]
- [McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]
- [McLean 1994][research_mclean_1994]
- [McLemore and Peterson 1960][research_mclemore_peterson_1960]
- [McMaster and Schenk 1973][research_mcmaster_schenk_1973]
- [McNeill et al 1961][research_mcneill_mclean_1961]
- [McRuer 1965][research_mcruer_1965]
- [McRuer 1995][research_mcruer_1995]
- [Measuring Airspeed 2021][research_measuring_airspeed_2021]
- [Meckstroth and Blake 2015][research_meckstroth_blake_2015]
- [Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]
- [Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020_b]
- [Medina et al 2019][research_medina_rockwood_2019]
- [Medved 1990][research_medved_1990]
- [Meheut et al 2012][research_meheut_arntz_2012]
- [Mehra et al 1972][research_mehra_stepner_1972]
- [Mehra et al 1974][research_mehra_stepner_1974]
- [Meijer and Cunningham 1992][research_meijer_cunningham_1992]
- [Memon and Altman 2016][research_memon_altman_2016]
- [Meng et al 2007][research_meng_jia_2007]
- [Mengali 2003][research_mengali_2003]
- [Mennell 1976][research_mennell_1976]
- [Menshchikov and Somov 2019][research_menshchikov_somov_2019]
- [Menzies 1996][research_menzies_1996]
- [Menzies and Kandil 1996][research_menzies_kandil_1996]
- [Menzies et al 1995][research_menzies_kandil_1995]
- [Mercer and Maiden 1972][research_mercer_maiden_1972]
- [Merceruio][research_merceruio]
- [Mertens et al 1986][research_mertens_klevenhusen_1986]
- [Mertins et al 2005][research_mertins_elsholz_2005]
- [Metcalf 1936][research_metcalf_1936]
- [Methods for Improving Longitudinal Stability and Control 2003][research_methods_for_2003]
- [Metodiev 2024][research_metodiev_2024]
- [Meyer 1983][research_meyer_1983]
- [Meyer and Husband 1990][research_meyer_husband_1990]
- [Meyer et al 1989][research_meyer_yip_1989]
- [Mialon et al 2010][research_mialon_khrabov_2010]
- [Michal 1998][research_michal_1998]
- [Midhat 2017][research_midhat_2017]
- [Midmer and Bruecker 2024][research_midmer_bruecker_2024]
- [Miklosovic and Perry 2014][research_miklosovic_perry_2014]
- [Miklosovic et al 2012][research_miklosovic_imber_2012]
- [Milenković-Babić 2018][research_milenkovicbabic_2018]
- [Milenković-Babić et al 2017][research_milenkovicbabic_samardzic_2017]
- [Milenković-Babić et al 2024][research_milenkovicbabic_ivkovic_2024]
- [Miles 1952][research_miles_1952]
- [Milholen and Chokani 1994][research_milholen_chokani_1994]
- [Miller 1969][research_miller_1969]
- [Miller 1970][research_miller_1970]
- [Miller 1983][research_miller_1983]
- [Miller and Forster 2025][research_miller_forster_2025]
- [Miller and Franklin 1968][research_miller_franklin_1968]
- [Milne and Martos 2012][research_milne_martos_2012]
- [Ming-Zhou et al 2016][research_mingzhou_guoping_2016]
- [Minghang and Hu 2014][research_minghang_hu_2014]
- [Mirels 1953][research_mirels_1953]
- [Mistry et al 2013][research_mistry_page_2013]
- [Mitcham 1949][research_mitcham_1949]
- [Mitcham and Blanchard 1950][research_mitcham_blanchard_1950]
- [Mitcham et al 1951][research_mitcham_blanchard_1951]
- [Mitcham et al 1952][research_mitcham_blanchard_1952]
- [Mitcham et al 1956][research_tailless_triangular_1956]
- [Mitchell 2000][research_mitchell_2000]
- [Mitchell and Hoh 1982][research_mitchell_hoh_1982]
- [Mitchell and Hoh 1984][research_mitchell_hoh_1984]
- [Mitchell and Klyde 2008][research_mitchell_klyde_2008]
- [Mitchell and Peck 1950][research_mitchell_peck_1950]
- [Mitchell et al][research_mitchell_kish]
- [Mitchell et al 1992][research_mitchell_aponso_1992]
- [Mitchell et al 1995][research_mitchell_aponso_1995]
- [Mitchell et al 2003][research_mitchell_doman_2003]
- [Mitikiri and Mohseni 2018][research_mitikiri_mohseni_2018]
- [Mitiku et al 2024][research_mitiku_salau_2024]
- [Miyaji and Takegawa 2022][research_miyaji_2022]
- [Mizoguchi et al 2014][research_mizoguchi_kajikawa_2014]
- [Modeling and Control for a Blended Wing Body Aircraft 2015][research_modeling_and_2015]
- [Modern Aircraft Flight Control 1988][research_modern_aircraft_1988]
- [Moennich and Dalldorff 1993][research_moennich_dalldorff_1993]
- [Moes et al 2000][research_moes_noffz_2000]
- [Moes et al 2003][research_moes_smith_2003]
- [Moes et al 2006][research_moes_smith_2006]
- [Mohamed and Dongare 2021][research_mohamed_dongare_2021]
- [Mohamed and Dongare 2021][research_mohamed_dongare_2021_b]
- [Mohamed and Dongare 2021][research_mohamed_dongare_2021_c]
- [Mohamed et al 2009][research_mohamed_nadarajah_2009]
- [Mohamed et al 2009][research_mohamed_nadarajah_2009_b]
- [Mohamed et al 2021][research_mohamed_abdelhady_2021]
- [Mohamed et al 2026][research_mohamed_abdullah_2026]
- [Mohammed 2007][research_mohammed_2007]
- [Mohammed 2015][research_mohammed_2015]
- [Mohammed et al 2013][research_mohammed_wu_2013]
- [Mohan and Kumar 2023][research_mohan_kumar_2023]
- [Mohanty and swain 2025][research_mohanty_swain_2025]
- [Mohd. Nasir 2026][research_mohdnasir_2026]
- [Moitra 1985][research_moitra_1985]
- [Molinari et al 2015][research_molinari_arrieta_2015]
- [Molinari et al 2018][research_molinari_arrieta_2018]
- [Molland and Turnock 2007][research_molland_turnock_2007]
- [Molland and Turnock 2022][research_molland_turnock_2022]
- [Molton et al 2013][research_molton_dandois_2013]
- [Monaghan 1978][research_monaghan_1978]
- [Monaghan and Friend 1973][research_monaghan_friend_1973]
- [Monahemi et al 1995][research_monahemi_barlow_1995]
- [Montano et al 2024][research_montano_dimino_2024]
- [Montgomery 1971][research_montgomery_1971]
- [Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]
- [Montgomery and Price 1974][research_montgomery_price_1974]
- [Mooij 1985][research_mooij_1985]
- [Mooij 1985][research_mooij_1985_b]
- [Mooij 1985][research_mooij_1985_c]
- [Mooij 1985][research_mooij_1985_d]
- [Mooij 1985][research_mooij_1985_e]
- [Mooij 1985][research_mooij_1985_f]
- [Moore 1957][research_moore_1957]
- [Moore and Frei 1983][research_moore_frei_1983]
- [Moore and Moore 2008][research_moore_moore_2008]
- [Moore and Pullin 1995][research_moore_pullin_1995]
- [Moore et al 2024][research_moore_rahimi_2024]
- [Moorhouse 1979][research_moorhouse_1979]
- [Moorhouse 1990][research_moorhouse_1990]
- [Moorhouse 1995][research_moorhouse_1995]
- [Moorhouse and Fielding 1998][research_moorhouse_fielding_1998]
- [Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]
- [Moorthamers et al 2021][research_moorthamers_wiberg_2021]
- [Moosavi 2025][research_moosavi_2025]
- [Moreines et al 1965][research_moreines_sellite_1965]
- [Moreira et al 2022][research_moreira_gripp_2022]
- [Morelli 2000][research_morelli_2000]
- [Morelli 2002][research_morelli_2002]
- [Morelli 2021][research_morelli_2021]
- [Morelli 2021][research_morelli_2021_b]
- [Morelli and Grauer 2018][research_morelli_grauer_2018]
- [Mori et al 2024][research_mori_yakeno_2024]
- [Morra and Nicolosi 2025][research_morra_nicolosi_2025]
- [Morris 1966][research_morris_1966]
- [Morris 1992][research_morris_1992]
- [Morris and Tigner 1995][research_morris_tigner_1995]
- [Morris and Ward 1989][research_morris_ward_1989]
- [Morris et al 2012][research_morris_allison_2012]
- [Morris et al 2013][research_morris_sultan_2013]
- [Morris et al 2014][research_morris_allison_2014]
- [Morton 1956][research_morton_1956]
- [Morton et al 2002][research_morton_mitchell_2002]
- [Moseley and Taylor 1953][research_moseley_taylor_1953]
- [Moseley and Taylor 1954][research_moseley_taylor_1954]
- [Moseley and Thompson 1957][research_moseley_thompson_1957]
- [Moses 1997][research_moses_1997]
- [Moses and Ashley 1998][research_moses_ashley_1998]
- [Moses and Huttsell 2000][research_moses_huttsell_2000]
- [Moss et al 1991][research_moss_cole_1991]
- [Moszczynski and Grant 2017][research_moszczynski_grant_2017]
- [Moul and Brown 1959][research_artificial_pitch_damping_1959]
- [Moulin and Karpel 2007][research_moulin_karpel_2007]
- [Moulton et al 2024][research_moulton_abraham_2024]
- [Muchamad Bayu Sakti Pratama et al 2022][research_muchamadbayusaktipratama_erwinsulaeman_2022]
- [Mudd 1969][research_mudd_1969]
- [Mulder 1985][research_mulder_1985]
- [Mulder 1988][research_mulder_1988]
- [Mulder et al 2009][research_mulder_lubbers_2009]
- [Muller 1967][research_muller_1967]
- [Mullins et al 1996][research_mullins_tipton_1996]
- [Mungall 1946][research_mungall_1946]
- [Munger et al 1983][research_munger_carlin_1983]
- [Muralidharan et al 1979][research_muralidharan_baron_1979]
- [Murphy and Klein 2008][research_murphy_klein_2008]
- [Murphy and Klein 2010][research_murphy_klein_2010]
- [Murray 1949][research_murray_1949]
- [Murray et al 2020][research_murray_giannellis_2020]
- [Murri et al 1983][research_murri_croom_1983]
- [Murri et al 1984][research_murri_nguyen_1984]
- [Musa et al 2015][research_musa_mansor_2015]
- [Musa et al 2026][research_musa_mansor_2026]
- [Muzzey and Kidd 1959][research_muzzey_kidd_1959]
- [Muñoz][research_munoz]
- [Myala et al 2019][research_myala_borra_2019]
- [Myatt and Jenkins 1996][research_myatt_jenkins_1996]
- [Myatt and Myatt 1997][research_myatt_myatt_1997]
- [Myatt et al 1998][research_myatt_schumacher_1998]
- [Myers and Walsh 1988][research_myers_walsh_1988]
- [Myers et al 1982][research_myers_mcruer_1982]
- [Myers et al 1983][research_myers_johnston_1983]
- [NACA 1951 An Investigation of the Effect of Vertical-Fin Location and Area on Low-Speed Lateral Stability][research_vertical_fin_location_1951]
- [NACA Conference on Aircraft Loads, Structures, and Flutter 1957][research_naca_conference_1957]
- [Nagabhushan and Lutze 1983][research_nagabhushan_lutze_1983]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Nahom Jidovetski et al 2025][research_nahomjidovetski_raveh_2025]
- [Naigle et al 2022][research_naigle_hiltner_2022]
- [Nallapula et al 2012][research_nallapula_schade_2012]
- [Nangia and Palmer 2002][research_nangia_palmer_2002]
- [Nangia et al 2003][research_nangia_palmer_2003]
- [Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]
- [Napolitano and Spagnuolo 1993][research_napolitano_spagnuolo_1993]
- [Napolitano and Swaim 1989][research_napolitano_swaim_1989]
- [Napolitano et al 1996][research_napolitano_paris_1996]
- [Narayanan et al 2026][research_narayanan_kumar_2026]
- [Nardi 1970][research_nardi_1970]
- [Nardi et al 1976][research_nardi_kawana_1976]
- [NASA advanced design program. Design and analysis of a radio-controlled flying wing aircraft 1993][research_nasa_advanced_1993]
- [Nash et al 2025][research_nash_timme_2025]
- [Nasir and Kuntjoro 2013][research_nasir_kuntjoro_2013]
- [Nasir et al 2012][research_nasir_kuntjoro_2012]
- [Nasir et al 2014][research_nasir_kuntjoro_2014]
- [Natesan and Bhat 2005][research_natesan_bhat_2005]
- [Nayfeh et al 1989][research_nayfeh_elzebda_1989]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Neal and Smith 1971][research_neal_smith_1971]
- [Neely and Griner 1959][research_neely_griner_1959]
- [Neighbor and Wiler 1978][research_neighbor_wiler_1978]
- [Nelson][research_nelson]
- [Nelson and Arena 1993][research_nelson_arena_1993]
- [Nelson and Durham 2002][research_nelson_durham_2002]
- [Nelson et al 1991][research_nelson_arena_1991]
- [Ness 1971][research_ness_1971]
- [Neumark 1950][research_neumark_1950]
- [Neves and Mariani 2024][research_neves_mariani_2024]
- [Newell and Campbell 1954][research_newell_campbell_1954]
- [Newell et al 1963][research_newell_dolbin_1963]
- [Newey][research_newey]
- [Newman and Buttrill 1995][research_newman_buttrill_1995]
- [Newton 2025][research_newton_2025]
- [Newton and Kroo 2023][research_newton_kroo_2023]
- [Newton and Kroo 2024][research_newton_kroo_2024]
- [Newton and Kroo 2025][research_newton_kroo_2025]
- [Ng and Malcolm 1990][research_ng_malcolm_1990]
- [Ng et al 1989][research_ng_malcolm_1989]
- [Ng et al 1991][research_ng_ong_1991]
- [Ng et al 1992][research_ng_malcolm_1992]
- [Ng et al 1993][research_ng_skaff_1993]
- [Ng et al 1994][research_ng_skaff_1994]
- [Ngo et al][research_ngo_reigelsperger]
- [Ngo et al 1996][research_ngo_reigelsperger_1996]
- [Nguyen 1974][research_nguyen_1974]
- [Nguyen and Cord 1999][research_nguyen_cord_1999]
- [Nguyen and Stepanyan 2010][research_nguyen_stepanyan_2010]
- [Nguyen and Xiong][research_nhannguyen_juntaoxiong_b]
- [Nguyen and Xiong 2021][research_nguyen_xiong_2021]
- [Nguyen and Xiong 2022][research_nguyen_xiong_2022]
- [Nguyen and Xiong 2023][research_nguyen_xiong_2023]
- [Nguyen and Xiong 2026][research_nguyen_xiong_2026]
- [Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]
- [Nguyen et al 1981][research_nguyen_yip_1981]
- [Nguyen et al 1985][research_nguyen_whipple_1985]
- [Nguyen et al 1997][research_nguyen_cord_1997]
- [Nguyen et al 2006][research_nguyen_krishnakumar_2006]
- [Nguyen et al 2017][research_nguyen_ting_2017]
- [Nguyen et al 2019][research_nguyen_fugate_2019]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Nguyen et al 2021][research_nguyen_saturation_pio_2021]
- [Nguyen et al 2025][research_nguyen_xiong_2025]
- [Nicholas et al 1984][research_nicholas_naville_1984]
- [Nicolosi et al 2010][research_nicolosi_demarco_2010]
- [Nicolosi et al 2013][research_nicolosi_demarco_2013]
- [Nie et al 2020][research_nie_liu_2020]
- [Nie et al 2021][research_nie_liu_2021]
- [Nie et al 2026][research_nie_zhang_2026]
- [Nie et al 2026][research_nie_zhang_2026_b]
- [Nielsen et al 1953][research_nielsen_1953]
- [Niestroy 2025][research_niestroy_2025]
- [Niestroy et al 2017][research_niestroy_dorsett_2017]
- [Niestroy et al 2019][research_niestroy_williams_2019]
- [Nieto-Wire and Sobel 2007][research_nietowire_sobel_2007]
- [Nieto-Wire and Sobel 2009][research_nietowire_sobel_2009]
- [Nieto-Wire and Sobel 2011][research_nietowire_sobel_2011]
- [Nieto-Wire and Sobel 2013][research_nietowire_sobel_2013]
- [Nieto-Wire and Sobel 2014][research_nietowire_sobel_2014]
- [Nikbay et al 2025][research_nikbay_yildiz_2025]
- [Niranjana et al 1993][research_niranjana_rao_1993]
- [Nishanth et al 2019][research_p_arokkiaswamy_2019]
- [Nissen 1943][research_nissen_1943]
- [Niu et al 2023][research_niu_yan_2023]
- [Nixon 1974][research_nixon_1974]
- [Nixon 2020][research_nixon_2020]
- [Noll et al 1983][research_noll_calico_1983]
- [Nominal aircraft dynamics][research_nominal_aircraft]
- [Nomura 2003][research_nomura_2003]
- [Nonweiler 1960][research_nonweiler_1960]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Norton 1924][research_norton_1924]
- [Norton and Carroll 1922][research_norton_carroll_1922]
- [Nugent 1959][research_nugent_1959]
- [Nurohman et al 2018][research_nurohman_arifianto_2018]
- [Nusrath et al 2014][research_nusrath_sarmah_2014]
- [Nuthi and Subbarao 2014][research_nuthi_subbarao_2014]
- [Nyquist 1928][research_nyquist_1928]
- [Nävert and Sedin 1992][research_navert_sedin_1992]
- [O'Donnell and Mohseni 2017][research_odonnell_mohseni_2017]
- [O'Donnell and Mohseni 2019][research_odonnell_mohseni_2019]
- [O'Kelly 1954][research_okelly_1954]
- [O'Kelly 1955][research_okelly_1955]
- [Obayashi and Guruswamy 1994][research_obayashi_guruswamy_1994]
- [OBrien and Takahashi 2024][research_obrien_takahashi_2024]
- [Obryan et al 1979][research_obryan_glover_1979]
- [Oehman and Suddath 1964][research_oehman_suddath_1964]
- [Oertel and Stank 1999][research_oertel_stank_1999]
- [Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]
- [Oggioni et al 2026][research_oggioni_riboldi_2026]
- [Ogren et al 1974][research_ogren_sotanski_1974]
- [Oguz Tasci et al 2022][research_oguztasci_tumse_2022]
- [Ohara 1964][research_ohara_1964]
- [Ohira et al 2013][research_ohira_kwak_2013]
- [Ohmichi et al 2017][research_ohmichi_ishida_2017]
- [Ohmichi et al 2018][research_ohmichi_ishida_2018]
- [Okada et al 1987][research_okada_bando_1987]
- [Oki 1960][research_oki_1960]
- [Okolo et al 2014][research_okolo_dogan_2014]
- [Okonkwo and Jemitola 2022][research_okonkwo_jemitola_2022]
- [Olcott et al 1981][research_olcott_sackel_1981]
- [Oliva 2000][research_oliva_2000]
- [Olsen 1966][research_olsen_1966]
- [Olsen and Seegmiller 1992][research_olsen_seegmiller_1992]
- [Olsen and Seegmiller 1993][research_olsen_seegmiller_1993]
- [Olson and Mead 1950][research_olson_mead_1950]
- [Olson and Mead 1951][research_olson_mead_1951]
- [Onstott and Faulkner 1978][research_onstott_faulkner_1978]
- [Orhan and Subbarao 2021][research_orhan_subbarao_2021]
- [Ossmann 2015][research_ossmann_2015]
- [Osterhuber et al 2004][research_osterhuber_hanel_2004]
- [Ostroff 1998][research_ostroff_1998]
- [Oswald 1932][research_oswald_1932]
- [Owashi et al 2017][research_owashi_tanaka_2017]
- [Owens et al 2003][research_owens_capone_2003]
- [Owens et al 2019][research_owens_beeler_2019]
- [Oyama 2021][research_oyama_2021]
- [Ozcan et al 2025][research_ozcan_tekyurt_2025]
- [Ozer 2025][research_ozer_2025]
- [Pabla 2021][research_pabla_2021]
- [Padua and Preisighe Viana 2025][research_padua_preisigheviana_2025]
- [Page and Gillette 1994][research_page_gillette_1994]
- [Pahle et al 1996][research_pahle_wichman_1996]
- [Painter and Caw 1978][research_painter_caw_1978]
- [Painter and Sitterle 1972][research_painter_sitterle_1972]
- [Pakmehr et al][research_pakmehr_gordon]
- [Pakmehr et al 2005][research_pakmehr_gordon_2005]
- [Palazzo and Spearman 1954][research_palazzo_spearman_1954]
- [Pambagjo et al 2001][research_pambagjo_nakahashi_2001]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Panagiotou et al 2022][research_panagiotou_antoniou_2022]
- [Papa and Stoliker 1988][research_papa_stoliker_1988]
- [Papamoschou and Mayoral 2014][research_papamoschou_mayoral_2014]
- [Paranjape and Ananthkrishan 2005][research_paranjape_ananthkrishan_2005]
- [Paranjape and Chung 2010][research_paranjape_chung_2010]
- [Paranjape et al 2011][research_paranjape_chung_2011]
- [Parello][research_parello]
- [Paris][research_paris]
- [Paris and Alaverdi 1998][research_paris_alaverdi_1998]
- [Park 2017][research_park_2017]
- [Park and Abla 1982][research_park_abla_1982]
- [Park and Abla 1983][research_park_abla_1983]
- [Park and Chung 2012][research_park_chung_2012]
- [Park and Ohtsu 1998][research_park_ohtsu_1998]
- [Park and Rokhsaz 2003][research_park_rokhsaz_2003]
- [Park et al 2001][research_park_lee_2001]
- [Park et al 2015][research_park_ocheltree_2015]
- [Park et al 2016][research_park_choi_2016]
- [Park et al 2016][research_park_jo_2016]
- [Park et al 2017][research_park_choi_2017]
- [Park et al 2017][research_park_jo_2017]
- [Parker et al 1991][research_parker_spain_1991]
- [Parks and Wingrove 1980][research_parks_wingrove_1980]
- [Parrish and Steinmetz 1972][research_parrish_steinmetz_1972]
- [Pasley et al 1973][research_pasley_rohling_1973]
- [Patel and Lefas 2026][research_patel_lefas_2026]
- [Patel et al 2007][research_patel_cao_2007]
- [Patel et al 2007][research_patel_cao_2007_b]
- [Patil 2004][research_patil_2004]
- [Patil and Hodges 2000][research_patil_hodges_2000]
- [Patil et al 1998][research_patil_hodges_1998]
- [Patterson 1984][research_patterson_1984]
- [Pattinson et al 2013][research_pattinson_lowenberg_2013]
- [Patton et al 1979][research_spin_research_summary_1979]
- [Paudel 2016][research_paudel_2016]
- [Paul and Rein 2016][research_paul_rein_2016]
- [Paul and Rein 2017][research_paul_rein_2017]
- [Paul et al 1997][research_paul_garrard_1997]
- [Paul O and Paul P 2019][research_paulo_paulp_2019]
- [Paulson 1944][research_paulson_1944]
- [Paulson 1948][research_paulson_1948]
- [Paulson and Kjelgaard 1982][research_paulson_kjelgaard_1982]
- [Paulus et al 2013][research_paulus_wirth_2013]
- [Pavelka and Tatum 1980][research_pavelka_tatum_1980]
- [Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]
- [Pawlak 1994][research_pawlak_1994]
- [Paziresh et al 2017][research_paziresh_nikseresht_2017]
- [Peahl et al 1986][research_peahl_kolkailah_1986]
- [Pearson and Aiken 1944][research_pearson_aiken_1944]
- [Pedreiro et al 1996][research_pedreiro_rock_1996]
- [Pedreiro et al 1998][research_pedreiro_takahara_1998]
- [Pedreiro et al 1999][research_pedreiro_takahara_1999]
- [Pedro and Tshabalala 2017][research_pedro_tshabalala_2017]
- [Pedro and Tshabalala 2017][research_pedro_tshabalala_2017_b]
- [Pei et al 2025][research_pei_huang_2025]
- [Peigin and Epstein 2006][research_peigin_epstein_2006]
- [Pelletier and Nelson 1994][research_pelletier_nelson_1994]
- [Pena and Voulgaris 2001][research_pena_voulgaris_2001]
- [Peng et al 2013][research_peng_xuefeng_2013]
- [Peng et al 2014][research_peng_wang_2014]
- [Pengelley and Wilson 1954][research_pengelley_wilson_1954]
- [Pepper and Foster 1947][research_pepper_foster_1947]
- [Perez et al 2006][research_perez_liu_2006]
- [Peristy et al 2019][research_peristy_perez_2019]
- [Perkins 1959][research_perkins_1959]
- [Perkins et al 1977][research_perkins_jr_1977]
- [Perraud et al 2003][research_perraud_moens_2003]
- [Perry 1976][research_perry_1976]
- [Perry 1978][research_perry_1978]
- [Perry and Miklosovic 2012][research_perry_miklosovic_2012]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Peters et al 1997][research_peters_andrisani_1997]
- [Petersen 1979][research_petersen_1979]
- [Petersen 1981][research_petersen_1981]
- [Peterson 1961][research_peterson_1961]
- [Peterson 2024][research_peterson_2024]
- [Peterson and Grant 2011][research_peterson_grant_2011]
- [Peterson and Menees 1961][research_peterson_menees_1961]
- [Peterson and Menees 1961][research_peterson_menees_1961_b]
- [Petre and Ashley 1976][research_petre_ashley_1976]
- [Petrenko and Gašparovič 2025][research_petrenko_gasparovic_2025]
- [Petrocchi and Barakos 2023][research_petrocchi_barakos_2023]
- [Petrocchi and Barakos 2023][research_petrocchi_barakos_2023_b]
- [Pettit and Grandhi 2003][research_pettit_grandhi_2003]
- [Pfaff 1965][research_pfaff_1965]
- [Pfifer and Danowsky 2016][research_pfifer_danowsky_2016]
- [Pfnür et al 2018][research_pfnur_oppelt_2018]
- [Phillips][research_phillips]
- [Phillips 1942][research_phillips_1942]
- [Phillips 1942][research_phillips_1942_b]
- [Phillips 1942][research_phillips_shortperiod_1942]
- [Phillips 1948][research_phillips_1948]
- [Phillips 1988][research_phillips_1988]
- [Phillips 1989][research_phillips_1989]
- [Phillips and Crane 1943][research_phillips_crane_1943]
- [Phillips et al 1944][research_phillips_williams_1944]
- [Phillips et al 2002][research_phillips_anderson_2002]
- [Phillips et al 2010][research_phillips_gururajan_2010]
- [Phillips et al 2019][research_phillips_jentzsch_2019]
- [Phunpeng et al 2023][research_phunpeng_khaengkarn_2023]
- [Physics-assisted reduced-order modeling for identifying dominant features of transonic buffet 2023][research_physics_assisted_reduced_order_2023]
- [PI control of a tailless fighter aircraft with dynamic inversion and neural networks 1999][research_pi_control_1999]
- [Pitch-down dynamic stall characteristics 1994][research_pitch_down_dynamic_1994]
- [Place et al 1974][research_place_altmann_1974]
- [Placement in Flight Control 2026][research_placement_in_2026]
- [Plaetschke and Weiss 1988][research_plaetschke_weiss_1988]
- [Plante][research_plante]
- [Plante and Laurendeau 2019][research_plante_laurendeau_2019]
- [Plante et al 2017][research_plante_dandois_2017]
- [Plotkin and Dodbele 1988][research_plotkin_dodbele_1988]
- [Polamus and Spreemann 1961][research_polamus_spreemann_1961]
- [Polivanov and Sidorenko 2026][research_polivanov_sidorenko_2026]
- [Polonsky 2026][research_polonsky_2026]
- [Poojari 2022][research_poojari_2022]
- [Popescu 1999][research_popescu_1999]
- [Poplingher and Raveh 2018][research_poplingher_raveh_2018]
- [Poplingher and Raveh 2022][research_poplingher_raveh_2022]
- [Poplingher et al 2022][research_poplingher_mallik_2022]
- [Portapas and Cooke 2020][research_portapas_2020]
- [Posingies 1968][research_posingies_1968]
- [Pototzky 2014][research_pototzky_2014]
- [Pototzky 2018][research_pototzky_2018]
- [Pototzky and Moses 2005][research_pototzky_moses_2005]
- [Potsdam et al 1997][research_potsdam_page_1997]
- [Potvin and Grant 2026][research_potvin_grant_2026]
- [Pounds and Walker 1980][research_pounds_walker_1980]
- [Powell and Katz 1974][research_powell_katz_1974]
- [Powers 1968][research_powers_1968]
- [Powers 1972][research_powers_1972]
- [Powers 1980][research_powers_1980]
- [Powers 1982][research_powers_1982]
- [Powers 1984][research_powers_1984]
- [Powers 1986][research_powers_1986]
- [Powers 1986][research_powers_1986_b]
- [Prakash et al 2009][research_prakash_uthup_2009]
- [Prandtl 1928][research_prandtl_1928]
- [Pratheepan and Bruce Ralphin Rose 2015][research_j_j_2015]
- [Predachenko and Lemko 2017][research_predachenko_lemko_2017]
- [Predachenko and Lemko 2019][research_predachenko_lemko_2019]
- [Prediction and Verification of Aerodynamic Drag, Part II Wind-Tunnel/Flight Correlation of Lift, Drag, and Pitching Moment 1985][research_prediction_and_1985]
- [Prediction of transonic flutter for a supercritical wing by modified strip analysis and comparison with experiment 1981][research_prediction_of_1981]
- [Prediction of vortex breakdown effects on a rolling delta wing 1994][research_prediction_of_1994]
- [Preliminary Sizing of the Vertical and Horizontal Tails 2010][research_preliminary_sizing_2010]
- [Prilliman and Slingerland 1966][research_prilliman_slingerland_1966]
- [Prior et al 2023][research_prior_rozinka_2023]
- [Prochazka et al 2018][research_prochazka_eduardo_2018]
- [Properties of the U.S. Standard Atmosphere 2014][research_properties_of_2014]
- [Properties of the U.S. Standard Atmosphere 2024][research_properties_of_2024]
- [Protz and Sparks 1998][research_protz_sparks_1998]
- [Prudente and Cavalieri 2007][research_prudente_cavalieri_2007]
- [Prudnikov et al 1993][research_prudnikov_karavayev_1993]
- [Puentes and Takahashi 2024][research_puentes_takahashi_2024]
- [Pujara 1988][research_pujara_1988]
- [Purser and Spear 1946][research_purser_spear_1946]
- [Purser and Spear 1947][research_purser_spear_1947]
- [Purser and Turner 1941 Wind-Tunnel Investigation of Perforated Split Flaps for Use as Dive Brakes on a Tapered NACA 23012 Airfoil][research_purser_turner_1941]
- [Purwadi et al 2023][research_purwadi_hidayat_2023]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putnam and Ayers 1989][research_putnam_ayers_1989]
- [Qi et al 2017][research_qi_wang_2017]
- [Qi et al 2018][research_qi_zhao_2018]
- [Qi et al 2018][research_qi_zhao_2018_b]
- [Qi et al 2021][research_qi_bwb_2021]
- [Qi et al 2026][research_qi_gao_2026]
- [Qian and Alonso 2018][research_qian_alonso_2018]
- [Qian and Alonso 2021][research_qian_alonso_2021]
- [Qin 2002][research_qin_2002]
- [Qin et al 2007][research_qin_wong_2007]
- [Qin et al 2023][research_qin_wei_2023]
- [Qiu and Ang 2019][research_qiu_ang_2019]
- [Qiu and Sun 2009][research_qiu_sun_2009]
- [Qu et al 2011][research_qu_li_2011]
- [Qu et al 2013][research_qu_li_2013]
- [Quan 2013][research_quan_2013]
- [Quantitative Design Requirements for Flight Control 2017][research_quantitative_design_2017]
- [Quast et al 1991][research_quast_nelson_1991]
- [Queijo and Wells 1956][research_queijo_wells_1956]
- [Queijo and Wolhart 1951][research_queijo_wolhart_1951]
- [Queijo et al 1954][research_queijo_fences_1954]
- [Querry][research_querry]
- [Quigley et al 1960][research_quigley_anderson_1960]
- [Quinn and Cutchins 1984][research_quinn_cutchins_1984]
- [Quitter et al 2023][research_quitter_marino_2023]
- [Qureshi et al 2014][research_qureshi_wang_2014]
- [R.Yass et al 2009][research_aryass_hfarhood_2009]
- [Radzetsky et al 1994][research_radzetsky_reibert_1994]
- [Raffel et al 2021][research_raffel_wienke_2021]
- [Raghavan and Ananthkrishnan 2005][research_raghavan_ananthkrishnan_2005]
- [Raghavan and Patil 2009][research_raghavan_patil_2009]
- [Rahman et al 2025][research_rahman_vowotor_2025]
- [Rainey 1957][research_rainey_1957]
- [Rainey and Igoe 1958][research_rainey_igoe_1958]
- [Raj 1983][research_raj_1983]
- [Raj 1984][research_raj_1984]
- [Raj and Mohan 2015][research_raj_mohan_2015]
- [Rajanna et al 2024][research_rajanna_jaiswal_2024]
- [Rajanna et al 2026][research_rajanna_lua_2026]
- [Rajput et al 2014][research_rajput_zhang_2014]
- [Rajput et al 2015][research_rajput_zhangweiguo_2015]
- [Ramachandran and Wells 1974][research_ramachandran_wells_1974]
- [Rambacher et al 2024][research_rambacher_butler_2024]
- [Ramirez Zeigler and Avery 2026][research_ramirezzeigler_avery_2026]
- [Ramm 1990][research_ramm_1990_b]
- [Raney 1987][research_raney_1987]
- [Raney and Batterson 1989][research_raney_batterson_1989]
- [Rao 1984][research_rao_1984]
- [Rao and Huffman 1978][research_rao_huffman_1978]
- [Rao and Johnson 1982][research_rao_johnson_1982]
- [Rao and Johnson 1983][research_rao_johnson_1983]
- [Raol and Singh 2023][research_raol_singh_2023]
- [Rashad et al 2025][research_rashad_elbadawy_2025]
- [Rastgoftar et al 2017][research_rastgoftar_ni_2017]
- [Rathert et al 1951][research_rathert_1951]
- [Ratliff and Pagilla 2008][research_ratliff_pagilla_2008]
- [Raveh 2011][research_raveh_2011]
- [Ray 1965][research_ray_1965]
- [Ray et al 1972][research_ray_mckinney_1972]
- [Ray et al 1973][research_ray_mckinney_1973]
- [Razon et al 2023][research_razon_maher_2023]
- [Re 1974][research_re_1974]
- [Rea et al 2018][research_rea_pecora_2018]
- [Recant 1939][research_recant_1939]
- [Redeker and Voersmann 1988][research_redeker_voersmann_1988]
- [Rediess and Melton 1994][research_rediess_melton_1994]
- [Rediniotis et al 1994][research_rediniotis_klute_1994]
- [Reed 1955][research_reed_1955]
- [Reed 1982][research_reed_1982]
- [Reed 1984][research_reed_1984]
- [Reed 1985][research_reed_1985]
- [Reed 1987][research_reed_1987]
- [Reed and Clay 1937][research_reed_clay_1937]
- [Reeder 1944][research_reeder_1944]
- [Reeder 1945][research_reeder_1945]
- [Reeder 1945][research_reeder_1945_b]
- [Reeder 1945][research_reeder_1945_c]
- [Regan 2008][research_regan_2008]
- [Rehman 2022][research_rehman_2022]
- [Reibert et al 1997][research_reibert_saric_1997]
- [Reigelsperger et al 1995][research_reigelsperger_hammett_1995]
- [Reimann et al 2005][research_reimann_tinetti_2005]
- [Reist and Zingg 2014][research_reist_zingg_2014]
- [Reist and Zingg 2015][research_reist_zingg_2015]
- [Reist and Zingg 2016][research_reist_zingg_2016]
- [Ren et al 2022][research_ren_gao_2022]
- [Report No. 379. Rolling moments due to rolling and yaw for four wing models in rotation 1931][research_report_no_1931]
- [Repperger et al 1997][research_repperger_koivo_1997]
- [Reu and Ying 1991][research_reu_ying_1991]
- [Reynolds and Smith 1948][research_reynolds_smith_1948]
- [Rezaei and Khosravi 2023][research_rezaei_khosravi_2023]
- [Rezazadeh Movahhed and Hamed 2025][research_rezazadehmovahhed_hamed_2025]
- [Rezazadeh Movahhed and Hamed 2026][research_rezazadehmovahhed_hamed_2026]
- [Rhoads 1952][research_rhoads_1952]
- [Rhoads 1967][research_rhoads_1967]
- [Rhoads 1970][research_rhoads_1970]
- [Rhudy 2016][research_rhudy_2016]
- [Ribner 1950][research_ribner_1950]
- [Richards et al 2014][research_richards_adams_2014]
- [Rickard 1978][research_rickard_1978]
- [Rickard and Levison 1981][research_rickard_levison_1981]
- [Rickey 1946][research_rickey_1946]
- [Riebe and MacLeod 1950][research_riebe_macleod_1950]
- [Riethausen 2026][research_riethausen_2026]
- [Rigid-Body Flight Dynamics 2026][research_rigid_body_flight_2026]
- [Riley and Drajeske 1991][research_riley_drajeske_1991]
- [Rimer et al 1983][research_rimer_chipman_1983]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1984][research_rimer_chipman_1984_b]
- [Rising 1982][research_rising_1982]
- [Rising et al 1984][research_rising_davis_1984]
- [Risse et al 2010][research_risse_anton_2010]
- [Rivera and Florance 2000][research_rivera_florance_2000]
- [Rivers et al 2012][research_rivers_hunter_2012]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1977][research_rizzetta_1977_b]
- [Rizzetta 1996][research_rizzetta_1996]
- [Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]
- [Rizzi 1984][research_rizzi_1984]
- [Rizzi 1985][research_rizzi_1985]
- [Rizzi 1995][research_rizzi_1995]
- [Ro et al 1992][research_ro_barlow_1992]
- [Roache 1965][research_roache_1965]
- [Robb et al 2023][research_robb_vuppala_2023]
- [Robbins et al 2023][research_robbins_stansbury_2023]
- [Roberts 1963][research_roberts_1963]
- [Roberts 1988][research_roberts_1988_b]
- [Roberts and Lind 2009][research_roberts_lind_2009]
- [Roberts et al 2006][research_roberts_yang_2006]
- [Robinson and Robinson 1980][research_robinson_robinson_1980]
- [Robinson et al 2020][research_robinson_yuan_2020]
- [Rockwell 1994][research_rockwell_1994]
- [Rockwood et al 2019][research_rockwood_medina_2019]
- [Rodchenko et al 2003][research_rodchenko_zaichik_2003]
- [Rodden 1989][research_rodden_1989]
- [Rodemich and Andrew 1965][research_rodemich_andrew_1965]
- [Rodgers 1964][research_rodgers_1964]
- [Rodgers 1965][research_rodgers_1965]
- [Rodgers 1966][research_rodgers_1966]
- [Roeser and Mönnich 2024][research_roeser_monnich_2024]
- [Rogalski 2018][research_rogalski_2018]
- [Rogalski and Dołęga 2006][research_rogalski_dolega_2006]
- [Rogalski et al 2021][research_rogalski_rzucidlo_2021]
- [Rogers 2007][research_rogers_2007]
- [Rogers and Walter K. 1953][research_rogers_walterk_1953]
- [Rogers and Walter K. 1958][research_rogers_walterk_1958]
- [Rohling 1968][research_rohling_1968]
- [Rohling 1969][research_rohling_1969]
- [Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]
- [Rojas Carvajal and Amitay 2025][research_rojascarvajal_amitay_2025]
- [Rojas Carvajal et al 2022][research_rojascarvajal_guha_2022]
- [Rojas Carvajal et al 2024][research_rojascarvajal_kumarguha_2024]
- [Rokoni and Hasan 2013][research_rokoni_hasan_2013]
- [Rolek 1974][research_rolek_1974]
- [Rolls and Wingrove 1958][research_rolls_wingrove_1958]
- [Roman et al 2000][research_roman_allen_2000]
- [Roman et al 2003][research_roman_gilmore_2003]
- [Romberg 2003][research_romberg_2003]
- [Romere and Chambliss 1972][research_romere_chambliss_1972]
- [Rong et al 2016][research_rong_deng_2016]
- [Roohani and Skews 2009][research_roohani_skews_2009]
- [Rooney et al 1982][research_rooney_chung_1982]
- [Roos 1980][research_roos_1980]
- [Roos 1985][research_roos_1985]
- [Rosario-Gabriel and Cortes 2018][research_rosariogabriel_cortes_2018]
- [Rose and Seginer 1978][research_rose_seginer_1978]
- [Rosemann and Birkemeyer 2002][research_rosemann_birkemeyer_2002]
- [Rosenberg 1944][research_rosenberg_1944]
- [Rosenow et al 2022][research_rosenow_sachwitz_2022]
- [Roskam 1977][research_roskam_1977]
- [Ross 1972][research_ross_1972]
- [Ross 1972][research_ross_1972_b]
- [Rossetti and Beblo 2022][research_rossetti_beblo_2022]
- [Rossitto and Hodgkinson 1993][research_rossitto_hodgkinson_1993]
- [Rostami et al 2021][research_rostami_chung_2021]
- [Rotaru et al 2016][research_rotaru_circiu_2016]
- [Row and Fischel 1963][research_row_fischel_1963]
- [Rowan and Dogan 2023][research_rowan_dogan_2023]
- [Roy 2009][research_roy_2009]
- [Roy and Ghosh 2010][research_roy_ghosh_2010]
- [Roysdon and Khalid 2010][research_roysdon_khalid_2010]
- [Roysdon and Khalid 2011][research_roysdon_khalid_2011]
- [Rubio-Sierra et al 2022][research_rubiosierra_delgado_2022]
- [Rudesh et al 2025][research_rudesh_singh_2025]
- [Ruhlin and Murphy 1981][research_ruhlin_murphy_1981]
- [Rui et al 2007][research_rui_zhou_2007]
- [Runckel and Henderson 1952][research_runckel_henderson_1952]
- [Runyan and George-Falvy 1979][research_runyan_georgefalvy_1979]
- [Ruseno 2021][research_ruseno_2021]
- [Russell 1996][research_russell_1996]
- [Rustagi et al 2018][research_rustagi_kothari_2018]
- [Rymarz and Ramaprian 1995][research_rymarz_ramaprian_1995]
- [Rynaski 1985][research_rynaski_1985]
- [Rynaski 1994][research_rynaski_1994]
- [Rynaski et al 1978][research_rynaski_andrisani_1978]
- [Rynaski et al 1986][research_rynaski_weingarten_1986]
- [Ryu and Andrisani 2000][research_ryu_andrisani_2000]
- [Ryu and Andrisani 2000][research_ryu_andrisani_2000_b]
- [Ryu and Andrisani 2003][research_ryu_andrisani_2003]
- [Rzucidlo and Tomczyk 2007][research_rzucidlo_tomczyk_2007]
- [Sachs 1969][research_sachs_1969]
- [Sachs 1977][research_sachs_1977]
- [Sachs 1990][research_sachs_1990]
- [Sachs 1999][research_sachs_1999]
- [Sachs et al 1994][research_sachs_knoll_1994]
- [Sadoff 1958][research_sadoff_1958]
- [Sadoff 1962][research_sadoff_1962]
- [Sadoff and Crossfield 1954][research_x4_flight_evaluation_1954]
- [Sadoff and Sisk 1950][research_x4_longitudinal_1950]
- [Sadoff and Sisk 1950][research_x4_stall_1950]
- [Sadoff and Sisk 1950 Summary Report of Results Obtained During Demonstration Tests of the Northrop X-4 Airplanes][research_sadoff_sisk_1950]
- [Sadoff et al 1954][research_sadoff_blunt_te_1954]
- [Sadoff et al 1961][research_sadoff_mcfadden_1961]
- [Sadraey 2022][research_sadraey_2022]
- [Sadraey 2022][research_sadraey_2022_b]
- [Sadraey 2022][research_sadraey_2022_c]
- [Sadraey 2022][research_sadraey_2022_d]
- [Saephan and van Dam 2006][research_saephan_vandam_2006]
- [Saephan and van Dam 2006][research_saephan_vandam_2006_b]
- [Saephan and Van Dam 2008][research_saephan_vandam_2008]
- [Saetti and Rogers 2020][research_saetti_rogers_2020]
- [Saghafi and Banazadeh 2006][research_saghafi_banazadeh_2006]
- [Saheby et al 2026][research_saheby_2026]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Salahudden et al 2020][research_salahudden_giri_2020]
- [Saltzman 1955][research_x4_blunt_elevons_1955]
- [Samardžić 2023][research_samardzic_2023]
- [Samardžić et al 2013][research_samardzic_isakovic_2013]
- [Sammonds and Bunnell 1980][research_sammonds_bunnell_1980]
- [Sammonds and Bunnell 1981][research_sammonds_bunnell_1981]
- [Sandahl 1948][research_sandahl_1948]
- [Sandahl 1948][research_sandahl_delta_1948]
- [Sandahl 1948][research_sandahl_swept_1948]
- [Sandahl and Strass 1950][research_sandahl_strass_1950_b]
- [Sandahl et al 1949][research_sandahl_bland_1949]
- [Sandahl et al 1950][research_sandahl_strass_1950]
- [Sanders 1965][research_sanders_1965]
- [Sanders et al 2003][research_sanders_eastep_2003]
- [Sanders et al 2018][research_sanders_tischler_2018]
- [Sanderson 1965][research_sanderson_1965]
- [Sandlin and Swanson 1990][research_sandlin_swanson_1990]
- [Sanfilippo 1970][research_sanfilippo_1970]
- [Sang][research_sang]
- [Sanghi et al 2020][research_sanghi_riso_2020]
- [Sanghi et al 2024][research_sanghi_cesnik_2024]
- [Sanghi et al 2025][research_sanghi_riso_2025]
- [Santos et al 2024][research_santos_adeodato_2024]
- [Saporito et al 2021][research_saporito_daronch_2021]
- [Saraswathi 2000][research_saraswathi_2000]
- [Saric 1997][research_saric_1997]
- [Saric 2010][research_saric_2010]
- [Saric and Yeates 1985][research_saric_yeates_1985]
- [Sarigul-Klijn et al 2008][research_sarigulklijn_nespeca_2008]
- [Sarkar and Panneerselvam 1998][research_sarkar_panneerselvam_1998]
- [Sarkar et al 2009][research_sarkar_ananthasayanam_2009]
- [Sarrafian and Powers 1985][research_sarrafian_powers_1985]
- [Sarrafian and Powers 1988][research_sarrafian_powers_1988]
- [Saucez][research_saucez]
- [Saucez and Boiffier 2012][research_saucez_boiffier_2012]
- [Saussie et al 2011][research_saussie_akhrif_2011]
- [Sawyer and Trant 1947][research_xf7u_semispan_1947]
- [Sawyer and Trant 1950][research_sawyer_trant_1950]
- [Sboev D 2024][research_sboevd_2024]
- [Scalera and Durham 1999][research_scalera_durham_1999]
- [Schade and Hassell 1953][research_schade_hassell_1953]
- [Schaeffler and Telionis 1998][research_schaeffler_telionis_1998]
- [Schairer 1941][research_schairer_1941]
- [Schauerhamer and Robinson 2017][research_schauerhamer_robinson_2017]
- [Schauerte and Schreyer 2023][research_schauerte_schreyer_2023]
- [Schauerte and Schreyer 2024][research_schauerte_schreyer_2024]
- [Schauerte and Schreyer 2025][research_schauerte_schreyer_2025]
- [Schiavetta et al 2006][research_schiavetta_boelens_2006]
- [Schierbrock and Takahashi 2021][research_schierbrock_takahashi_2021]
- [Schiess 1986][research_schiess_1986]
- [Schiess 1988][research_schiess_1988]
- [Schiff and Tobak 1981][research_schiff_tobak_1981]
- [Schirrer et al 2013][research_schirrer_kozek_2013]
- [Schmidt 1983][research_schmidt_1983]
- [Schmidt 1985][research_schmidt_1985]
- [Schmidt 1986][research_schmidt_1986]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt and Wright 1991][research_schmidt_wright_1991]
- [Schmidt et al 2016][research_schmidt_zhao_2016]
- [Schmidt et al 2019][research_schmidt_danowsky_2019]
- [Schmidt et al 2025][research_schmidt_static_margin_2025]
- [Schmitt et al 1983][research_schmitt_destarac_1983]
- [Schmitt et al 1990][research_schmitt_reneaux_1990]
- [Schnoebelen and Yechout 2003][research_schnoebelen_yechout_2003]
- [Schnurbusch 1944][research_schnurbusch_1944]
- [Schnurbusch 1945][research_schnurbusch_1945]
- [Scholz 2021][research_scholz_2021]
- [Schroeder 2001][research_schroeder_2001]
- [Schroeder and Chung 2000][research_schroeder_chung_2000]
- [Schroeder et al 1998][research_schroeder_chung_1998]
- [Schroeder et al 2001][research_schroeder_chung_2001]
- [Schuck et al 2013][research_schuck_heller_2013]
- [Schuelein 2008][research_schuelein_2008]
- [Schuldenfrei et al 1947][research_schuldenfrei_1947]
- [Schuler 1983][research_schuler_1983]
- [Schult 1954][research_schult_1954]
- [Schult and Fields 1952][research_schult_fields_1952]
- [Schult and Fields 1954][research_schult_fields_1954]
- [Schumacher 1952][research_schumacher_1952]
- [Schwanz 1972][research_schwanz_1972]
- [Schweiger et al 2000][research_schweiger_weiss_2000]
- [Schweikhard 1966][research_schweikhard_1966]
- [Schweikhard 1967][research_schweikhard_1967]
- [Schwithal et al 2025][research_schwithal_wallace_2025]
- [Schy 1972][research_schy_1972]
- [Schütte et al 2018][research_schutte_huber_2018]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
- [Seacord and Campbell 1945][research_allwing_stability_1945]
- [Sears 1980][research_sears_1980]
- [Seaver et al 2023][research_seaver_bennett_2023]
- [Sebastia and Hornung 2023][research_sebastia_hornung_2023]
- [Sebastia et al 2024][research_sebastia_wurz_2024]
- [Seckel 1964][research_seckel_1964]
- [Seckel 1964][research_seckel_1964_b]
- [Seckel 1964][research_seckel_1964_c]
- [Seckel 1964][research_seckel_1964_d]
- [Seckel 1964][research_seckel_1964_e]
- [Seckel 1964][research_seckel_1964_f]
- [Seebass 1997][research_seebass_1997]
- [Seidel et al 1985][research_seidel_sandford_1985]
- [Seider and Haenel 1991][research_seider_haenel_1991]
- [Semaan et al 2013][research_semaan_scholz_2013]
- [Seraj and Martins 2025][research_seraj_martins_2025]
- [Serpieri and Kotsonis 2015][research_serpieri_kotsonis_2015]
- [Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016]
- [Serpieri and Kotsonis 2016][research_serpieri_kotsonis_2016_b]
- [Sevart 1971][research_sevart_1971]
- [Sevart and Patel 1973][research_sevart_patel_1973]
- [Sevart et al 1972][research_sevart_patel_1972]
- [Sgueglia][research_sgueglia]
- [Shafer 1975][research_shafer_1975]
- [Shafer 1991][research_shafer_1991]
- [Shafer 1992][research_shafer_1992]
- [Shafer 1994][research_shafer_1994]
- [Shafer and Steinmetz 2001][research_shafer_steinmetz_2001]
- [Shafer and Steinmetz 2001][research_shafer_steinmetz_2001_b]
- [Shafer et al 1983][research_shafer_smith_1983]
- [Shafer et al 1984][research_shafer_smith_1984]
- [Shafer et al 1989][research_shafer_koehler_1989]
- [Shah and Granda 1998][research_shah_granda_1998]
- [Shamikh 2013][research_shamikh_2013]
- [Shams][research_shams]
- [Shams et al 2023][research_shams_khouli_2023]
- [Shams et al 2026][research_shams_khouli_2026]
- [Shams Taleghani et al 2020][research_shamstaleghani_ghajar_2020]
- [Shankar and Goebel 1983][research_shankar_goebel_1983]
- [Shankar and Goebel 1985][research_shankar_goebel_1985]
- [Shankar and Malmuth 1980][research_shankar_malmuth_1980]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shankar and Malmuth 1983][research_shankar_malmuth_1983]
- [Shankar et al 1979][research_shankar_malmuth_1979]
- [Shannon 1948][research_shannon_1948]
- [Shao et al 2022][research_shao_liu_2022]
- [Shao et al 2024][research_shao_guo_2024]
- [Shao et al 2026][research_shao_he_2026]
- [Shao et al 2026][research_shao_meng_2026]
- [Sharif et al 2022][research_sharif_abbas_2022]
- [Sharma and Hosder 2024][research_sharma_hosder_2024]
- [Shayak et al 2024][research_shayak_girdhar_2024]
- [Shayan and Van Kampen 2021][research_shayan_vankampen_2021]
- [Shearwood et al 2020][research_shearwood_2020]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Shearwood et al 2021][research_shearwood_nabawy_2021]
- [Shearwood et al 2021][research_shearwood_nabawy_2021_b]
- [Shearwood et al 2023][research_shearwood_nabawy_2023]
- [Shekar et al 2026][research_shekar_molloy_2026]
- [Shen and Chen 2025][research_shen_chen_2025]
- [Shen et al 2019][research_shen_huang_2019]
- [Shen et al 2021][research_shen_huang_2021]
- [Sheneshen and kamal 2025][research_sheneshen_kamal_2025]
- [Sherman et al 2021][research_sherman_tirona_2021]
- [Sheta 2003][research_sheta_2003]
- [Sheta 2004][research_sheta_2004]
- [Sheta and Huttsell 2001][research_sheta_huttsell_2001]
- [Sheta and Huttsell 2002][research_sheta_huttsell_2002]
- [Sheta and Huttsell 2003][research_sheta_huttsell_2003]
- [Sheta et al 2001][research_sheta_rock_2001]
- [Sheta et al 2003][research_sheta_moses_2003]
- [Shevchuk 2014][research_shevchuk_2014]
- [Shevell 1978][research_shevell_1978]
- [Shi and Ma 2023][research_shi_ma_2023]
- [Shi and Wu 2022][research_shi_wu_2022]
- [Shibata et al 1987][research_shibata_nakao_1987]
- [Shin 2010][research_shin_2010]
- [Shin 2011][research_shin_2011]
- [Shiqi et al 2018][research_shiqi_tian_2018]
- [Shmilovich and Caughey][research_shmilovich_caughey]
- [Shmilovich and Caughey 1985][research_shmilovich_caughey_1985]
- [Shmilovich et al 2023][research_shmilovich_yadlin_2023]
- [Shmilovich et al 2026][research_shmilovich_yadlin_2026]
- [Shmul et al 2018][research_shmul_erenthal_2018]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Shrivastava 1987][research_shrivastava_1987]
- [Shtessel et al 1999][research_shtessel_buffington_1999]
- [Shtessel et al 2002][research_shtessel_buffington_2002]
- [Shuang et al 2016][research_shuang_zhang_2016]
- [Shuang et al 2017][research_shuang_zhang_2017]
- [Shumsky 2006][research_shumsky_2006]
- [Siddiqui et al 2023][research_siddiqui_sultan_2023]
- [Siddiqui et al 2025][research_siddiqui_maqsood_2025]
- [Sieradzki 2016][research_sieradzki_2016]
- [Silva][research_silva]
- [Silva][research_silva_b]
- [Silva 2011][research_silva_2011]
- [Silva et al 2019][research_silva_grinet_2019]
- [Silva et al 2022][research_silva_nunes_2022]
- [Silvers and Spreemann 1950][research_silvers_spreemann_1950]
- [Silvers et al 1958][research_silvers_fournier_1958]
- [Sim 1973][research_sim_1973]
- [Sim 1997][research_sim_1997]
- [Sim and Curry 1978][research_sim_curry_1978]
- [Simbuerger et al 2022][research_simbuerger_raveh_2022]
- [Simmons et al 2023][research_simmons_sysid_2023]
- [Simon 2014][research_simon_2014]
- [Simon et al 1993][research_simon_blake_1993]
- [Simon et al 2023][research_simon_williams_2023]
- [Simon et al 2024][research_simon_williams_2024]
- [Simulation in support of flight test - In retrospect 1988][research_simulation_in_1988]
- [Simulation Requirements for Flight Control Design 2017][research_simulation_requirements_2017]
- [Sinacori 1986][research_sinacori_1986]
- [Sinclair 1988][research_sinclair_1988]
- [Singh 2016][research_singh_2016]
- [Singh and Chowdhury 2021][research_singh_chowdhury_2021]
- [Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]
- [Singh and Raol 2000][research_singh_raol_2000]
- [Singh and Scholz 2018][research_singh_scholz_2018]
- [Singh and Venkatraman 2023][research_singh_venkatraman_2023]
- [Singh and Venkatraman 2026][research_singh_venkatraman_2026]
- [Singh et al 1994][research_singh_yim_1994]
- [Singh et al 1995][research_singh_yirn_1995]
- [Singh et al 2014][research_singh_mcdonough_2014]
- [Singh et al 2016][research_singh_brown_2016]
- [Singh et al 2016][research_singh_toropov_2016]
- [Singh et al 2022][research_singh_karnick_2022]
- [Singhasenee et al 2026][research_singhasenee_lamon_2026]
- [Sinha and Ananthkrishnan 2017][research_sinha_ananthkrishnan_2017]
- [Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021]
- [Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021_b]
- [Sinha and Ananthkrishnan 2021][research_sinha_ananthkrishnan_2021_c]
- [Siqueira et al 2007][research_siqueira_moreira_2007]
- [Sisk and Mataeny 1980][research_sisk_mataeny_1980]
- [Sisk and Matheny 1979][research_sisk_matheny_1979]
- [Sisk and Mooney 1953][research_sisk_mooney_1953]
- [Sisk et al 1965][research_xb70_review_1965]
- [Sissingh 2015][research_sissingh_2015]
- [Siu et al 2013][research_siu_martos_2013]
- [Sivan 1971][research_sivan_1971]
- [Siwakosit et al 2000][research_siwakosit_hess_2000]
- [Sizlo et al 1979][research_sizlo_berg_1979]
- [Sjoberg 1945][research_sjoberg_1945]
- [Sjoberg and Reeder 1948][research_sjoberg_reeder_1948]
- [Sjoberg and Reeder 1948][research_sjoberg_reeder_1948_b]
- [Sklenář and Matějů 2022][research_sklenar_mateju_2022]
- [Skoog 1951][research_skoog_1951]
- [Skujins and Cesnik 2011][research_skujins_cesnik_2011]
- [Sleeman 1957][research_sleeman_1957]
- [Sleeman and Byrnes 1953][research_sleeman_byrnes_1953]
- [Sleeman and Morrison 1953][research_sleeman_morrison_1953]
- [Slingerland 2002][research_slingerland_2002]
- [Slingerland 2005][research_slingerland_2005]
- [Sliwa 1980][research_sliwa_1980]
- [Smetana and Knepper 1973][research_smetana_knepper_1973]
- [Smetana et al 1972][research_smetana_summery_1972]
- [Smith 1953][research_smith_tailless_1953]
- [Smith 1959][research_smith_1959]
- [Smith 1975][research_smith_1975]
- [Smith 1977][research_smith_1977]
- [Smith 1979][research_smith_1979]
- [Smith 1981][research_smith_1981]
- [Smith 1982][research_smith_1982]
- [Smith 1986][research_smith_1986]
- [Smith and Berry 1975][research_smith_berry_1975]
- [Smith and Edwards 1980][research_smith_edwards_1980]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Taylor 1967][research_smith_taylor_1967]
- [Snell 1998][research_snell_1998]
- [Snyder et al 1972][research_snyder_fry_1972]
- [Sobel 1982][research_sobel_1982]
- [Sobel et al 1986][research_sobel_lee_1986]
- [Soehne 1956][research_soehne_1956]
- [Soemarwoto et al 2000][research_soemarwoto_labrujere_2000]
- [Soinne 1999][research_soinne_1999]
- [Solarte-Pineda et al 2026][research_solartepineda_bravomosquera_2026]
- [Solies 1994][research_solies_1994]
- [Solies 1994][research_solies_1994_b]
- [Solies 1994][research_solies_1994_c]
- [Song et al 1995][research_song_jeon_1995]
- [Song et al 2014][research_song_yang_2014]
- [Song et al 2025][research_song_wong_2025]
- [Sonneveldt et al 2011][research_sonneveldt_chu_2011]
- [Sorensen et al 1972][research_sorensen_tyler_1972]
- [Soudakov et al 2017][research_soudakov_petrov_2017]
- [Soule 1937][research_soule_1937]
- [Soule 1940][research_soule_1940]
- [Soule and McAvoy 1934][research_hasoule_whmcavoy_1934]
- [Soule and Wetmore 1933][research_soule_wetmore_1933]
- [Soule and Wheatley 1934][research_soule_wheatley_1934]
- [Spacht 1980][research_spacht_1980]
- [Spaid 1984][research_spaid_1984]
- [Spain et al 1990][research_spain_soistmann_1990]
- [Sparks][research_sparks]
- [Sparks and Sparks 1997][research_sparks_sparks_1997]
- [Spearman 1983][research_spearman_1983]
- [Spearman and Driver 1959][research_spearman_driver_1959]
- [Spearman et al 1955][research_spearman_driver_1955]
- [Spearman et al 1956][research_spearman_robinson_1956]
- [Speyer and Crues 1985][research_speyer_crues_1985]
- [Speyer and Crues 1987][research_speyer_crues_1987]
- [Spooner and Martina 1948][research_spooner_martina_1948]
- [Spreemann 1959][research_spreemann_1959]
- [Spreemann and Few 1954][research_spreemann_few_1954]
- [Spreiter and Stahara 1971][research_spreiter_stahara_1971]
- [Srinathkumar et al 1993][research_srinathkumar_madhuranath_1993]
- [Srinathkumar et al 1995][research_srinathkumar_parameswaran_1995]
- [Srinivasan et al 1986][research_srinivasan_mccroskey_1986]
- [Srivastava et al 2017][research_srivastava_kumar_2017]
- [Srour et al 2021][research_srour_noura_2021]
- [Stability and control of aircraft with manual all-moving tailplanes 1986][research_stability_and_1986]
- [Stability Characteristics of Selected Aircraft 2014][research_stability_characteristics_2014]
- [Stability Characteristics of Selected Aircraft 2024][research_stability_characteristics_2024]
- [Staelens et al 2007][research_staelens_blackwelder_2007]
- [Stalford 1979][research_stalford_1979]
- [Stalford 1980][research_stalford_1980]
- [Stall Characteristics 2003][research_stall_characteristics_2003]
- [Stall Speed Measurement 2003][research_stall_speed_2003]
- [Stam and de Visser 2025][research_stam_devisser_2025]
- [Stancil 1979][research_stancil_1979]
- [Stanewsky and Little 1971][research_stanewsky_little_1971]
- [Stanford 2016][research_stanford_2016]
- [Stanford and Jacobson 2023][research_stanford_jacobson_2023]
- [Stanford and Jacobson 2024][research_stanford_jacobson_2024]
- [Stanford et al 2020][research_stanford_jacobson_2020]
- [Stargill 1983][research_stargill_1983]
- [Static Aeroelasticity Effect of Wing Flexibility on Control Effectiveness 2014][research_static_aeroelasticity_2014]
- [Static Aeroelasticity Effect of Wing Flexibility on Lift Distribution and Divergence 2014][research_static_aeroelasticity_2014_b]
- [Static Flight Stability and Control 2026][research_static_flight_2026]
- [Static Longitudinal Stability Flight Test Methods 2003][research_static_longitudinal_2003]
- [Static Longitudinal Stability Theory 2003][research_static_longitudinal_2003_b]
- [Staufenbiel and Schlichting 1988][research_staufenbiel_schlichting_1988]
- [Stebbins and Loth 2022][research_stebbins_loth_2022]
- [Steer 2000][research_steer_2000]
- [Steer 2003][research_steer_2003]
- [Steers and Iliff 1975][research_steers_iliff_1975]
- [Steger and Bailey 1979][research_steger_bailey_1979]
- [Stegmüller et al 2022][research_stegmuller_katzenmeier_2022]
- [Stegmüller et al 2026][research_stegmuller_haybock_2026]
- [Steimle et al 2008][research_steimle_schroder_2008]
- [Steimle et al 2010][research_steimle_schroder_2010]
- [Steinbach 1997][research_steinbach_1997]
- [Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]
- [Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]
- [Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]
- [Stengel 1973][research_stengel_1973]
- [Stengel 1976][research_stengel_1976]
- [Stengel 1981][research_stengel_1981]
- [Stengel 1983][research_stengel_1983]
- [Stengel 1985][research_stengel_1985]
- [Stengel and Berry 1976][research_stengel_berry_1976]
- [Stengel and Berry 1977][research_stengel_berry_1977]
- [Stengel and Miller 1978][research_stengel_miller_1978]
- [Stepanyan et al 2010][research_stepanyan_kalmanje_2010]
- [Stephenson and Hardy 1989][research_stephenson_hardy_1989]
- [Stephenson et al 1955][research_stephenson_selan_1955]
- [Stephenson et al 1990][research_stephenson_jeske_1990]
- [Sternfield and Gates 1949 A Method of Calculating a Stability Boundary That Defines a Region of Satisfactory Period-Damping Relationship of the Oscillatory Mode of Motion][research_sternfield_gates_1949]
- [Stevens and McCormack 1944][research_stevens_mccormack_1944]
- [Stickan et al 2014][research_stickan_dillinger_2014]
- [Stojakovic][research_stojakovic]
- [Stone 1950 Wing-Dropping Characteristics of Some Straight and Swept Wings at Transonic Speeds as Determined with Rocket-Powered Models][research_stone_1950]
- [Stone and Daughtridge 1948][research_stone_daughtridge_1948]
- [Stone and Naylor 1972][research_stone_naylor_1972]
- [Stough and Kauffman 1950][research_stough_kauffman_1950]
- [Stough et al 1987][research_stough_dicarlo_1987]
- [Strass 1948][research_strass_1948]
- [Strass 1954][research_strass_1954]
- [Strass and Marley 1952][research_strass_marley_1952]
- [Strass and Tucker 1954][research_strass_tucker_1954]
- [Strass et al 1951][research_strass_fields_1951]
- [Strass et al 1952][research_strass_fields_1952]
- [Streett 1981][research_streett_1981]
- [Streett 1982][research_streett_1982]
- [Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]
- [Strutz 1972][research_strutz_1972]
- [Studwell and Wu 1973][research_studwell_wu_1973]
- [Su and Chow 1993][research_su_chow_1993]
- [Su and Chow 1995][research_su_chow_1995]
- [Su et al 2014][research_su_zhou_2014]
- [Su et al 2022][research_su_hu_2022]
- [Su et al 2023][research_su_hu_2023]
- [Suarez et al 1992][research_suarez_kramer_1992]
- [Suarez et al 1993][research_suarez_smith_1993]
- [Suarez et al 1993][research_suarez_smith_1993_b]
- [Suchomel 1987][research_suchomel_1987]
- [Sudderth and McNeill 1976][research_sudderth_mcneill_1976]
- [Sudderth et al 1975][research_sudderth_bohn_1975]
- [Sudha et al 2018][research_sudha_deodhare_2018]
- [Sudhakar et al 2025][research_s_c_2025]
- [Sudhakar et al 2026][research_sudhakar_prem_2026]
- [Sugimoto 1992][research_sugimoto_1992]
- [Sugioka et al 2015][research_sugioka_numata_2015]
- [Sugioka et al 2018][research_sugioka_koike_2018]
- [Sugioka et al 2021][research_sugioka_nakakita_2021]
- [Suikat et al 1987][research_suikat_donaldson_1987]
- [Suikat et al 1989][research_suikat_donaldson_1989]
- [Suleman 2007][research_suleman_2007]
- [Suleman et al 2000][research_suleman_crawford_2000]
- [Suleman et al 2002][research_suleman_crawford_2002]
- [Sullivan 1978][research_sullivan_1978]
- [Summey and Smetana 1977][research_summey_smetana_1977]
- [Sun and Hu 2005][research_sun_hu_2005]
- [Sun and Xu 2021][research_sun_xu_2021]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2021][research_sun_zhou_2021]
- [Sun et al 2024][research_sun_zhou_2024]
- [Sun et al 2026][research_sun_wang_2026]
- [Sundar 1978][research_sundar_1978]
- [Sundaram and Wu 1983][research_sundaram_wu_1983]
- [Suplisson et al 2011][research_suplisson_brandt_2011]
- [Suresh et al 2010][research_suresh_radhakrishnan_2010]
- [Suresh et al 2012][research_suresh_siddesh_2012]
- [Suresh et al 2013][research_suresh_radhakrishnan_2013]
- [Susanto 2022][research_susanto_2022]
- [Sutherland 1893][research_sutherland_1893]
- [Swaim 1978][research_swaim_1978]
- [Swaim 1980][research_swaim_1980]
- [Swaim and Fullman 1977][research_swaim_fullman_1977]
- [Sweberg 1942][research_sweberg_1942]
- [Sweberg 1945][research_sweberg_1945]
- [Syed Haseeb 2026][research_m_2026]
- [Szema and Shankar 1984][research_szema_shankar_1984]
- [Szwabowski and Baker 2023][research_szwabowski_baker_2023]
- [Taboada et al 2018][research_taboada_boschetti_2018]
- [Tahir et al 2026][research_tahir_wing_rock_2026]
- [Tai et al 2023][research_tai_wang_2023]
- [Takeda 1970][research_takeda_1970]
- [Talmage and Reeder 1947][research_talmage_reeder_1947]
- [Tamaki and Kawai 2023][research_tamaki_kawai_2023]
- [Tamayama et al 2003][research_tamayama_kheirandish_2003]
- [Tan et al 2014][research_tan_wu_2014]
- [Tan et al 2014][research_tan_zhou_2014]
- [Tan et al 2017][research_tan_wang_2017]
- [Tan et al 2018][research_tan_wang_2018]
- [Tan et al 2025][research_tan_yang_2025]
- [Tang 1971][research_tang_1971]
- [Tang 2019][research_tang_2019]
- [Tang and Dowell 1995][research_tang_dowell_1995]
- [Tang and Dowell 2013][research_tang_dowell_2013]
- [Tang and Pearson 1971][research_tang_pearson_1971]
- [Tanner and Montgomery 1979][research_tanner_montgomery_1979]
- [Tantaroudas et al 2015][research_tantaroudas_daronch_2015]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023_b]
- [Taraborrelli 2023][research_taraborrelli_2023]
- [Tarn and Hsu][research_tarn_hsu]
- [Tarn and Hsu 1993][research_tarn_hsu_1993]
- [Tatar and Masdari 2019][research_tatar_masdari_2019]
- [Taufik et al 2024][research_taufik_zaidaan_2024]
- [Taylor 1952][research_taylor_1952]
- [Taylor 2012][research_taylor_2012]
- [Taylor and Pamadi 1983][research_taylor_pamadi_1983]
- [Taylor and Ratnayake 2011][research_taylor_ratnayake_2011]
- [Taylor and Yoo 2011][research_taylor_yoo_2011]
- [Taylor et al 1965][research_taylor_robinson_1965]
- [Taylor et al 1997][research_taylor_peake_1997]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Telionis 1990][research_telionis_1990]
- [Telionis 1995][research_telionis_1995]
- [Telionis 2001][research_telionis_2001]
- [Teofilatto 2001][research_teofilatto_2001]
- [Teperin et al 2018][research_teperin_teperina_2018]
- [Teplitz et al 1946][research_teplitz_kayten_1946]
- [Terrell and Zein-Sabatto 2017][research_terrell_zeinsabatto_2017]
- [Test Techniques for Flight Control Systems of Large Transport Aircraft 2021][research_test_techniques_2021]
- [Tewari 2000][research_tewari_2000]
- [Tewes and Taubert 2015][research_tewes_taubert_2015]
- [Thacker and Lan 1993][research_thacker_lan_1993]
- [The effects of aft-loaded airfoils on aircraft trim drag 1989][research_the_effects_1989]
- [The effects of canard-wing flow-field interactions on longitudinal stability, effective dihedral and potential deep-stall trim 1988][research_the_effects_1988]
- [The effects of sustained acceleration, airframe buffet, and aircraft flying qualities on tracking performance 1977][research_the_effects_1977]
- [The stability of the boundary layer on a swept wing with wall cooling 1979][research_the_stability_1979]
- [The Transformation of Aerodynamic Stability Derivatives from a Body Axes Reference to a Wind Axes Reference 1997][research_the_transformation_1997]
- [The Transformation of Aerodynamic Stability Derivatives from a Body Axes Reference to a Wind Axes Reference 2007][research_the_transformation_2007]
- [Thelander 1965][research_thelander_1965]
- [Theodore et al 2014][research_theodore_malpica_2014]
- [Theodorsen 1979][research_theodorsen_1935]
- [Thomas and Dowell 2015][research_thomas_dowell_2015]
- [Thomas and Dowell 2020][research_thomas_dowell_2020]
- [Thomas and Holst 1983][research_thomas_holst_1983]
- [Thomas and Wolhart 1957][research_thomas_wolhart_1957]
- [Thomas et al 2001][research_thomas_dowell_2001]
- [Thomas et al 2010][research_thomas_burley_2010]
- [Thompson and Gilruth 1940][research_thompson_gilruth_1940]
- [Thompson and Moseley 1956][research_thompson_moseley_1956]
- [Thompson et al 1950][research_thompson_bray_1950]
- [Thomson 1946][research_thomson_1946]
- [Three-dimensional boundary-layer transition on a swept wing at Mach 3.5 1994][research_three_dimensional_boundary_layer_1994]
- [Tian et al 2017][research_tian_feng_2017]
- [Tigner et al 1998][research_tigner_holden_1998]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Timme 2020][research_timme_2020]
- [Timme and Thormann 2016][research_timme_thormann_2016]
- [Ting and Ayoubi 2012][research_ting_ayoubi_2012]
- [Ting and Ayoubi 2013][research_ting_ayoubi_2013]
- [Tingting and Aijun 2014][research_tingting_aijun_2014]
- [Tipton and Smith 1995][research_tipton_smith_1995]
- [Tipton et al 1996][research_tipton_smith_1996]
- [Tischler 2018][research_tischler_2018]
- [Tischler 2018][research_tischler_2018_b]
- [Tleulinov and Jafarzade 2019][research_tleulinov_jafarzade_2019]
- [Tobak 1953][research_tobak_1953]
- [Tobak et al 1950][research_tobak_reese_1950]
- [Toffol et al 2025][research_toffol_paolini_2025]
- [Tohidi and Yildiz 2019][research_tohidi_yildiz_2019]
- [Tohidi et al 2018][research_tohidi_yildiz_2018]
- [Tokutake and Itoh][research_tokutake_itoh]
- [Tokutake et al 2003][research_tokutake_sato_2003]
- [Tokutake et al 2006][research_tokutake_fujinaga_2006]
- [Tokutake et al 2008][research_tokutake_fujinaga_2008]
- [Tomac and Stenfelt 2014][research_tomac_stenfelt_2014]
- [Tomczyk 2008][research_tomczyk_2008]
- [Tomek and Boyden 2000][research_tomek_boyden_2000]
- [Tomek et al 2020][research_tomek_ullah_2020]
- [Tonon and Belluati 2018][research_tonon_belluati_2018]
- [Torenbeek 2016][research_torenbeek_2016]
- [Torvik 1990][research_torvik_1990]
- [Tournes and Johnson 1999][research_tournes_johnson_1999]
- [Tournes et al 1997][research_tournes_shtessel_1997]
- [Tourrette 1996][research_tourrette_1996]
- [Tousi et al 1988][research_tousi_bajaj_1988]
- [Traas et al 2026][research_traas_atmaca_2026]
- [Trailing Edge Circulation Control of an Airfoil at Transonic Mach Numbers 2006][research_trailing_edge_2006]
- [Tran and Lind 2010][research_tran_lind_2010]
- [Tran et al 2017][research_tran_sakamoto_2017]
- [Trankle and Rabin 1983][research_trankle_rabin_1983]
- [Transformation of Aerodynamic Stability Derivatives from a Body Axes Reference to a Wind Axes Reference 2013][research_transformation_of_2013]
- [Transonic Aircraft Configurations 2012][research_transonic_aircraft_2012]
- [Transonic Airfoil Theory 1986][research_transonic_airfoil_1986]
- [Transonic and supersonic flight 1992][research_transonic_and_1992]
- [Transonic Computational Experience for Advanced Tactical Aircraft 1982][research_transonic_computational_1982]
- [Transonic control effectiveness for 1977][research_elevon_transonic_1977]
- [Transonic flight test of a laminar flow leading edge with surface excrescences 1994][research_transonic_flight_1994]
- [Transonic Navier-Stokes flow computations over wing-fuselage geometries 1972][research_transonic_navier_stokes_1972]
- [Trim and Longitudinal Static Stability 2017][research_trim_and_2017]
- [Triplett 1980][research_triplett_1980]
- [Tseng et al 2006][research_tseng_gupta_2006]
- [Tsuchiya et al 2022][research_tsuchiya_takahashi_2022]
- [Tu et al 2019][research_tu_marzanek_2019]
- [Tu et al 2024][research_tu_yan_2024]
- [Tucker and Quinn 1944][research_tucker_quinn_1944]
- [Tufts et al 2013][research_tufts_reed_2013]
- [Turn Performance and Maneuver Margin 2021][research_turn_performance_2021]
- [Turner and Cooper 1947][research_turner_cooper_1947]
- [Twisdale and Kirsten 1984][research_twisdale_kirsten_1984]
- [Ueno et al 1998][research_ueno_matsuno_1998]
- [Ueno et al 2004][research_ueno_sarae_2004]
- [Ul Haq et al 2026][research_ulhaq_atmaca_2026]
- [Ulbrich 2006][research_ulbrich_2006]
- [Ullah et al 2021][research_ullah_tomek_2021]
- [Ullah et al 2022][research_ullah_fabijanic_2022]
- [Ulrich et al 2001][research_ulrich_roche_2001]
- [Umm-e-Aymon et al 2016][research_ummeaymon_shah_2016]
- [Underwood 1942][research_underwood_1942]
- [Urbano][research_urbano]
- [Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]
- [Urie and Reaser 1979][research_urie_reaser_1979]
- [Urnes 2012][research_urnes_2012]
- [Urnes and Yeager 1991][research_urnes_yeager_1991]
- [Use of Aerodynamic Forces to Control the Trajectory of an Aircraft 2022][research_use_of_2022]
- [Uselton 1978][research_uselton_1978]
- [Uybarreta et al 2024][research_uybarreta_kabaliuk_2024]
- [Uybarreta et al 2025][research_uybarreta_grant_2025]
- [Vale J 2013][research_valej_2013]
- [Valentin 2011][research_valentin_2011]
- [Vallone][research_vallone]
- [van Arnhem et al 2019][research_vanarnhem_devries_2019]
- [van Dam 1985][research_vandam_1985]
- [Van Dam 1986][research_vandam_1986]
- [van der Maas 1959][research_vandermaas_1959]
- [Van der Velden 1987][research_vandervelden_1987]
- [Van Dommelen 1995][research_vandommelen_1995]
- [Van Pelt 1981][research_vanpelt_1981]
- [Van Thullenar 1957][research_vanthullenar_1957]
- [Vandervelden 1989][research_oblique_flying_wing_1989]
- [Vandierendonck 1973][research_vandierendonck_1973]
- [Vardaki and Gursul 2004][research_vardaki_gursul_2004]
- [Vatsa 1987][research_vatsa_1987]
- [Vatsa and Wedan 1988][research_vatsa_wedan_1988]
- [Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]
- [Veismann et al 2023][research_veismann_2023]
- [Velden 1997][research_velden_1997]
- [Velger and Shinar 1983][research_velger_shinar_1983]
- [Velicki and Thrash 2010][research_velicki_thrash_2010]
- [Velkova 2017][research_velkova_2017]
- [Vensel 1942][research_vensel_1942]
- [Vepa 2023][research_vepa_2023]
- [Vepa 2023][research_vepa_2023_b]
- [Vepa 2023][research_vepa_2023_c]
- [Vepa 2023][research_vepa_2023_d]
- [Verma and Kulkarni 2024][research_verma_kulkarni_2024]
- [Vertical Tail Loads 1996][research_vertical_tail_1996]
- [Vetter 2002][research_vetter_2002]
- [Vey et al 2010][research_vey_greenblatt_2010]
- [Vianto et al 2021][research_vianto_tobing_2021]
- [Vile et al 2019][research_vile_alwi_2019]
- [Vile et al 2019][research_vile_alwi_2019_b]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vile et al 2021][research_vile_alwi_2021]
- [Vincent and Botez 2015][research_vincent_botez_2015]
- [Vincent and Franklin 1981][research_vincent_franklin_1981]
- [Vindigni 2024][research_vindigni_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024]
- [Vindigni et al 2024][research_vindigni_mantegna_2024_b]
- [Visbal 2017][research_visbal_2017]
- [Visbal and Garmann 2012][research_visbal_garmann_2012]
- [Vishwanathan][research_vishwanathan]
- [Visonneau et al 2022][research_visonneau_guilmineau_2022]
- [Vitale Press and Shufflebarger 1954 An Investigation of the Use of Rocket-Powered Models for Gust-Load Studies with an Application to a Tailless Swept-Wing Model at Transonic Speeds][research_vitale_1954]
- [Volpe and Grossman 1978][research_volpe_grossman_1978]
- [Volpe and Jameson 1990][research_volpe_jameson_1990]
- [Vos et al 2002][research_vos_brown_2002]
- [Voss et al 2026][research_voss_frohler_2026]
- [Völkl and Breitsamter 2026][research_volkl_breitsamter_2026]
- [Völkl et al 2026][research_volkl_weiner_2026]
- [Waggoner 1980][research_waggoner_1980]
- [Waggoner 1982][research_waggoner_1982]
- [Wahler et al 2023][research_wahler_varriale_2023]
- [Wakayama 1998][research_wakayama_1998]
- [Wakayama 2000][research_wakayama_2000]
- [Wakayama 2008][research_wakayama_2008]
- [Wakayama and Kroo 1998][research_wakayama_kroo_1998]
- [Wakefield 1959 Effects of Wing-Crank, Leading-Edge Chord Extensions and Horizontal-Tail Height on the Longitudinal Stability of Sweptwing Models at Mach Numbers from 0.6 to 1.4][research_wakefield_1959]
- [Walchli and Langan 1999][research_walchli_langan_1999]
- [Waldmann et al 2019][research_waldmann_lutz_2019]
- [Waldmann et al 2023][research_waldmann_ehrle_2023]
- [Walker 1940][research_walker_1940]
- [Walker 1987][research_walker_1987]
- [Walker 1997][research_x36_test_pilot_1997]
- [Walker and Ballantyne 1950][research_walker_ballantyne_1950]
- [Walkley 1986][research_walkley_1986]
- [Walkley and Smith 1987][research_walkley_smith_1987]
- [Wallace 1942][research_wallace_1942]
- [Wallace 1944][research_wallace_1944]
- [Wallace 1952][research_wallace_1952]
- [Wallace and Recant 1943][research_wallace_recant_1943]
- [Walsh 1992][research_walsh_1992]
- [Walsh 1993][research_walsh_1993]
- [Walton and Katz 1992][research_walton_katz_1992]
- [Walton and Katz 1993][research_walton_katz_1993]
- [Wang 1979][research_wang_1979]
- [Wang 2019][research_wang_aeroelastic_2019]
- [Wang and Caughey 1992][research_wang_caughey_1992]
- [Wang and Feng 2025][research_wang_feng_2025]
- [Wang and Feng 2026][research_wang_feng_2026]
- [Wang and Guo 2012][research_wang_guo_2012]
- [Wang and Qi 2021][research_wang_qi_2021]
- [Wang and Wang 2012][research_wang_wang_2012]
- [Wang and Wang 2012][research_wang_wang_2012_b]
- [Wang and Zhao 2025][research_wang_zhao_2025]
- [Wang et al 1994][research_wang_herbert_1994]
- [Wang et al 1994][research_wang_herbert_1994_b]
- [Wang et al 1999][research_wang_lan_1999]
- [Wang et al 2002][research_wang_lan_2002]
- [Wang et al 2012][research_wang_santone_2012]
- [Wang et al 2012][research_wang_zhang_2012]
- [Wang et al 2017][research_wang_guo_2017]
- [Wang et al 2018][research_wang_zhang_2018]
- [Wang et al 2019][research_wang_wan_2019]
- [Wang et al 2020][research_wang_tang_2020]
- [Wang et al 2020][research_wang_yin_2020]
- [Wang et al 2020][research_wang_zhang_2020]
- [Wang et al 2021][research_wang_criteria_2021]
- [Wang et al 2021][research_wang_hou_2021]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2022][research_wang_bwb_airworthiness_2022]
- [Wang et al 2022][research_wang_tai_2022]
- [Wang et al 2022][research_wang_zhao_latdir_2022]
- [Wang et al 2023][research_wang_hu_2023]
- [Wang et al 2023][research_wang_zhou_2023]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_sun_2024]
- [Wang et al 2024][research_wang_tvsas_2024]
- [Wang et al 2024][research_wang_zhang_2024]
- [Wang et al 2024][research_wang_zhang_2024_b]
- [Wang et al 2024][research_wang_zhao_2024]
- [Wang et al 2025][research_wang_liu_2025]
- [Wang et al 2025][research_wang_rotating_wingtip_2025]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2026][research_wang_li_2026]
- [Wang et al 2026][research_wang_liu_2026]
- [Wanner 1973][research_wanner_1973]
- [Ward 1949][research_ward_1949]
- [Ward 1968][research_ward_1968]
- [Warner and Onstott 1986][research_warner_onstott_1986]
- [Warren et al 1997][research_warren_hassan_1997]
- [Warsop et al 2019][research_warsop_crowther_2019]
- [Washizu and Osuga 1960][research_washizu_osuga_1960]
- [Wasicko 1972][research_wasicko_1972]
- [Waters et al 2013][research_waters_voskuijl_2013]
- [Wawrzyniak 1970][research_wawrzyniak_1970]
- [Wei 1985][research_wei_1985]
- [Wei et al 2024][research_wei_zheng_2024]
- [Weick and Harris 1934][research_weick_harris_1934]
- [Weick and Noyes 1933][research_weick_noyes_1933]
- [Weick and Wenzinger 1932][research_weick_wenzinger_1932]
- [Weil 1981][research_weil_1981]
- [Weil and Spear 1947][research_weil_spear_1947]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weingarten and Chalk 1984][research_weingarten_chalk_1984]
- [Weinstein et al 2018][research_weinstein_hubbard_2018]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1983][research_weisshaar_1983]
- [Weisshaar and Zeiler 1982][research_weisshaar_zeiler_1982]
- [Wells 2002][research_wells_2002]
- [Wells and Hess 2002][research_wells_hess_2002]
- [Wells and Hess 2003][research_wells_hess_2003]
- [Weltz et al 2007][research_weltz_shweyk_2007]
- [Wen et al 2013][research_wen_deng_2013]
- [Wen-qiang et al 2008][research_wenqiang_jianjun_2008]
- [Wendel 1987][research_wendel_1987]
- [Wenqian et al 2010][research_wenqian_efremov_2010]
- [Wentz and Nyenhuis 1984][research_wentz_nyenhuis_1984]
- [Werner et al 2024][research_werner_henne_2024]
- [Westbrook 1965][research_westbrook_1965]
- [Westermayer et al 2010][research_westermayer_schirrer_2010]
- [Westin and de Freitas Pinto 2008][research_westin_defreitaspinto_2008]
- [Wetmore 1939][research_wetmore_1939]
- [Wetmore and Turner 1940][research_wetmore_turner_1940]
- [Wetzel 1954][research_wetzel_1954]
- [Weyl 1944][research_weyl_1944]
- [Weyl 1945][research_weyl_1945]
- [Weyl 1945][research_weyl_1945_b]
- [Weyl 1945][research_weyl_1945_c]
- [Weyl 1945][research_weyl_1945_d]
- [Weyl 1945][research_weyl_1945_e]
- [Wheldon and Whites 1966][research_wheldon_whites_1966]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [White and Innis 1959][research_tailless_delta_lowspeed_1959]
- [White et al 2001][research_white_saric_2001]
- [Whoric 1973][research_whoric_1973]
- [Wichman et al 1996][research_keithdwichman_josephwpahle_1996]
- [Wienke et al 2023][research_wienke_bertsch_2023]
- [Wildschek 2014][research_wildschek_2014]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Williams and Hoover 1945][research_waltercwilliams_herberthhoover_1945]
- [Williams et al 1995][research_williams_inelson_1995]
- [Williams et al 2025][research_williams_niestroy_2025]
- [Willig 1968][research_willig_1968]
- [Wilmott 1986][research_wilmott_1986]
- [Wilson et al 1990][research_wilson_buckley_1990]
- [Wilson et al 1991][research_wilson_hall_1991]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 1994][research_wilson_citurs_1994]
- [Wilson et al 2014][research_wilson_peters_2014]
- [Wing Buffet Control by using an EJector-Type Device 2021][research_wing_buffet_2021]
- [Wing tunnel model for simulating an infinite swept wing 1998][research_wing_tunnel_1998]
- [Wing twist control and adjustment system 1998][research_wing_twist_1998]
- [Winkelmann 1989][research_winkelmann_1989]
- [Winn and Kishi 1972][research_winn_kishi_1972]
- [Winograd Cooper Rathert and Rolls 1950 Preliminary Flight Investigation of the Wing-Dropping Tendency and Lateral-Control Characteristics of a 35 Degree Swept-Wing Airplane at Transonic Mach Numbers][research_winograd_1950]
- [Wise 1992][research_wise_1992]
- [Wise et al 1999][research_wise_brinker_1999]
- [Witte et al 2003][research_witte_monson_2003]
- [Wittenmark 1990][research_wittenmark_1990]
- [Wolkovitch 1984][research_wolkovitch_1984]
- [Wollner and Cooney 1948][research_wollner_cooney_1948]
- [Wolowicz 1945][research_wolowicz_1945]
- [Wolowicz and Yancey 1973][research_wolowicz_yancey_1973]
- [Wong et al 1993][research_wong_rock_1993]
- [Wong et al 2007][research_wong_moigne_2007]
- [Wood 1984][research_wood_1984]
- [Woodcock and Browne 1986][research_woodcock_browne_1986]
- [Woodcock and George 1976][research_woodcock_george_1976]
- [Woodruff et al 2011][research_woodruff_saric_2011]
- [Woods and Wood 1998][research_woods_wood_1998]
- [Woolard 1980][research_woolard_1980]
- [Wright 1936][research_wright_1936]
- [Wright and Loving 1953][research_wright_loving_1953]
- [Wu and Liu 2021][research_wu_liu_2021]
- [Wu and Perng 2004][research_wu_perng_2004]
- [Wu and Zheng 2022][research_wu_zheng_2022]
- [Wu et al 2012][research_wu_chen_2012]
- [Wykes 1968][research_wykes_1968]
- [Xi and Zhao 2017][research_xi_zhao_2017]
- [Xiang and Wang 2026][research_xiang_wang_2026]
- [Xiao et al 2004][research_xiao_tsai_2004]
- [Xiaoxiao and Zhu 2025][research_xiaoxiao_zhu_2025]
- [Xie et al 2010][research_xie_yang_2010]
- [Xie et al 2011][research_xie_yang_2011]
- [Xie et al 2019][research_xie_zhao_2019]
- [Xie et al 2022][research_xie_cai_2022]
- [Xie et al 2023][research_xie_cai_2023]
- [Xie et al 2026][research_xie_cai_2026]
- [Xin et al 2019][research_xin_blown_elevon_2019]
- [Xiong and Liu 2013][research_xiong_liu_2013]
- [Xiong and Nguyen 2024][research_xiong_nguyen_2024]
- [Xu 2012][research_xu_2012]
- [Xu and Deng 2014][research_xu_deng_2014]
- [Xu and Dowell 2026][research_xu_dowell_2026]
- [Xu and Feng 2025][research_xu_feng_2025]
- [Xu and Qiu 2011][research_xu_qiu_2011]
- [Xu and Yu 2025][research_xu_yu_2025]
- [Xu and Zha 2019][research_xu_zha_2019]
- [Xu and Zha 2021][research_xu_zha_2021]
- [Xu and Zhou 2015][research_xu_zhou_2015]
- [Xu et al 2013][research_xu_deng_2013]
- [Xu et al 2013][research_xu_zhu_2013]
- [Xu et al 2019][research_xu_pio_2019]
- [Xu et al 2019][research_xu_xu_2019]
- [Xu et al 2022][research_xu_yang_2022]
- [Xu et al 2026][research_xu_gao_2026]
- [Xue et al 2021][research_xue_yunsong_2021]
- [Xun et al 2026][research_xun_ground_effect_2026]
- [Yamasaki and Lele 2024][research_yamasaki_lele_2024]
- [Yan and Shi 2024][research_yan_shi_2024]
- [Yan et al 2025][research_yan_sun_2025]
- [Yan et al 2026][research_yan_dai_2026]
- [Yanagihara et al 1991][research_yanagihara_suzuki_1991]
- [Yancey 1964][research_yancey_1964]
- [Yang][research_yang]
- [Yang and Chao 1996][research_yang_chao_1996]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Li 2022][research_yang_li_aeroelastic_2022]
- [Yang and Przekwas 1993][research_yang_przekwas_1993]
- [Yang and Przekwas 1993][research_yang_przekwas_1993_b]
- [Yang and Shen 2007][research_yang_shen_2007]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang et al 1980][research_yang_guruswamy_1980]
- [Yang et al 2009][research_yang_zhong_2009]
- [Yang et al 2010][research_yang_fan_2010]
- [Yang et al 2022][research_yang_zhong_2022]
- [Yang et al 2024][research_yang_wen_2024]
- [YanKui Wang and Qian Li 2015][research_yankuiwang_qianli_2015]
- [Yasuaki and Egami 1999][research_yasuaki_egami_1999]
- [Yates 1960][research_yates_1960]
- [Yates and Schneiter 1946][research_yates_schneiter_1946]
- [Yavuz 2012][research_yavuz_2012]
- [Yavuztürk et al 2017][research_yavuzturk_topbas_2017]
- [Yazawa 1977][research_yazawa_1977]
- [Ye et al 2009][research_ye_zhang_2009]
- [Yechout 2024][research_yechout_2024]
- [Yechout and Oelschlaeger 1976][research_yechout_oelschlaeger_1976]
- [Yechout et al 2014][research_yechout_morris_2014]
- [Yeo et al 2015][research_yeo_atkins_2015]
- [Yerly et al 2016][research_yerly_deluca_2016]
- [Yi et al 2017][research_yi_dong_2017]
- [Yi Zhu et al 2016][research_yizhu_xinchen_2016]
- [Yildiz and Kolmanovsky 2010][research_yildiz_kolmanovsky_2010]
- [Yildiz et al 2011][research_yildiz_kolmanovsky_2011]
- [Yildiz et al 2019][research_yildiz_akcal_2019]
- [Yiming et al 2019][research_yiming_mei_2019]
- [Yin and Wang 2017][research_yin_wang_2017]
- [Yin et al 2019][research_yin_wang_2019]
- [Yingsong et al 2015][research_yingsong_zhichun_2015]
- [Yingyang et al 2025][research_yingyang_peng_2025]
- [Yong et al 2020][research_yong_wu_2020]
- [Yoo and Bowers 2018][research_yoo_bowers_2018]
- [Yoshinaga et al 2004][research_yoshinaga_nakaji_2004]
- [You 2026][research_you_2026]
- [Young 1961][research_young_1961]
- [Young 2026][research_young_2026]
- [Young and Martin 1992][research_young_martin_1992]
- [Young et al 1992][research_young_hergert_1992]
- [Yu 1981][research_yu_1981]
- [Yu and Bernal 2016][research_yu_bernal_2016]
- [Yu and Liu 2013][research_yu_liu_2013]
- [Yu et al 2013][research_yu_bernal_2013]
- [yu et al 2022][research_yu_li_2022]
- [Yu et al 2023][research_yu_li_2023]
- [Yu et al 2023][research_yu_li_2023_b]
- [Yu et al 2023][research_yu_tailless_2023]
- [Yu et al 2024][research_yu_li_2024]
- [Yu et al 2024][research_yu_li_2024_b]
- [Yu et al 2024][research_yu_tao_2024]
- [Yu et al 2026][research_yu_bose_2026]
- [Yuan et al 2023][research_yuan_ma_2023]
- [Yuan et al 2024][research_yuan_kou_2024]
- [Yuan et al 2024][research_yuan_ma_2024]
- [Yue et al 2009][research_yue_wang_2009]
- [Yue et al 2013][research_yue_wang_2013]
- [Yue et al 2013][research_yue_wang_2013_b]
- [Yurkovich 1996][research_yurkovich_1996]
- [Yuwei et al 2021][research_yuwei_aijun_2021]
- [Yüksel et al 2023][research_yuksel_kandemir_2023]
- [Zaal 2016][research_zaal_2016]
- [Zaheer and Ajmal 2019][research_zaheer_ajmal_2019]
- [Zahm and Bear 1929][research_zahm_bear_1929]
- [Zahn and Breitsamter 2022][research_zahn_breitsamter_2022]
- [Zahn et al 2025][research_zahn_zieher_2025]
- [Zanette and Almeida 2015][research_zanette_almeida_2015]
- [Zauner and Sandham 2020][research_zauner_sandham_2020]
- [Zauner et al 2023][research_zauner_moise_2023]
- [Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]
- [Zeiler 1998][research_zeiler_1998]
- [Zerihan and Zhang 2000][research_zerihan_zhang_2000]
- [Zeyada et al 1998][research_zeyada_hess_1998]
- [Zeyada et al 1999][research_zeyada_hess_1999]
- [Zhang 1988][research_zhang_1988]
- [Zhang 2021][research_zhang_2021]
- [Zhang and He 2026][research_zhang_he_2026]
- [Zhang and He 2026][research_zhang_he_fluidic_2026]
- [Zhang and Jia 2013][research_zhang_jia_2013]
- [Zhang and Ma 2021][research_zhang_ma_2021]
- [Zhang and Meng 2019][research_zhang_meng_2019]
- [Zhang and Qu 2015][research_zhang_qu_2015]
- [Zhang and Yang 2024][research_zhang_yang_2024]
- [Zhang and Ye 2010][research_zhang_ye_2010]
- [Zhang and Ye 2015][research_zhang_ye_2015]
- [Zhang and Zerihan 2003][research_zhang_zerihan_2003]
- [Zhang and Zerihan 2004][research_zhang_zerihan_2004]
- [Zhang and Zhang 2013][research_zhang_zhang_2013]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang et al 2007][research_zhang_suresh_2007]
- [Zhang et al 2008][research_zhang_rabbath_2008]
- [Zhang et al 2012][research_zhang_li_2012]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2013][research_zhang_zhu_2013]
- [Zhang et al 2015][research_zhang_wang_2015]
- [Zhang et al 2018][research_zhang_liu_2018]
- [Zhang et al 2018][research_zhang_shuang_2018]
- [Zhang et al 2018][research_zhang_xu_2018]
- [Zhang et al 2018][research_zhang_zhou_2018]
- [Zhang et al 2018][research_zhang_zhou_2018_b]
- [Zhang et al 2021][research_zhang_su_2021]
- [Zhang et al 2023][research_zhang_huang_2023]
- [Zhang et al 2024][research_zhang_liu_2024]
- [Zhang et al 2024][research_zhang_zhao_2024]
- [Zhang et al 2025][research_zhang_xiang_2025]
- [Zhang et al 2025][research_zhang_zhao_2025]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhao 1988][research_zhao_1988]
- [Zhao and Hu 2009][research_zhao_hu_2009]
- [Zhao et al 2014][research_zhao_sheng_2014]
- [Zhao et al 2020][research_zhao_dai_2020]
- [Zhao et al 2023][research_zhao_deng_2023]
- [Zhao et al 2024][research_zhao_zhang_2024]
- [Zhao et al 2025][research_zhao_wang_2025]
- [Zheng and Xu 2013][research_zheng_xu_2013]
- [Zheng et al 2012][research_zheng_feng_2012]
- [Zheng-hong 1992][research_zhenghong_1992]
- [Zhijie et al 2025][research_zhijie_taiyu_2025]
- [Zhishuai and Lingling 2022][research_zhishuai_lingling_2022]
- [Zhong et al 2009][research_zhong_yang_2009]
- [Zhong et al 2025][research_zhong_xia_2025]
- [Zhou 1994][research_zhou_1994]
- [Zhou et al 2017][research_zhou_chen_2017]
- [Zhou et al 2022][research_zhou_dong_2022]
- [Zhou et al 2025][research_zhou_liu_2025]
- [Zhu and Li 2023][research_zhu_li_2023]
- [Zhu et al 2016][research_zhu_gao_2016]
- [Zhu et al 2025][research_zhu_yang_2025]
- [Zhu et al 2026][research_zhu_yang_2026]
- [Zhubin and Ruikun 2023][research_zhubin_ruikun_2023]
- [Zierep 1988][research_zierep_1988]
- [Zierep 1993][research_zierep_1993]
- [Ziff et al 1953][research_ziff_rathert_1953]
- [Zilong et al 2024][research_zilong_jie_2024]
- [Zimmerman et al 1989][research_zimmerman_ferman_1989]
- [Zink et al 2000][research_zink_mavris_2000]
- [Zink et al 2001][research_zink_raveh_2001]
- [Zięba et al 2026][research_zieba_rzucidlo_2026]
- [Zogopoulos-Papaliakos et al 2020][research_zogopoulospapaliakos_karras_2020]
- [Zohar and Er-El 1988][research_zohar_erel_1988]
- [Zolghadri et al 2016][research_zolghadri_leberre_2016]
- [Zoppini et al 2022][research_zoppini_ragni_2022]
- [Zou][research_zou]
- [Zou and Li 2005][research_zou_li_2005]
- [Zou et al 2012][research_zou_yang_2012]
- [Zou et al 2016][research_zou_li_2016]
- [Zou et al 2017][research_zou_yin_2017]
- [Zou et al 2022][research_zou_huang_2022]
- [Zou et al 2026][research_zou_zhen_2026]
- [Zverkov et al 2012][research_zverkov_kozlov_2012]
- [Zweig and Ben-Asher 1995][research_zweig_benasher_1995]
- [Ünen and Yıldız 2025][research_unen_yildiz_2025]

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
[book_coleman_1988_jack_northrop]: https://openlibrary.org/works/OL4986268W
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
[book_hallion_1981_on_the_frontier]: https://openlibrary.org/works/OL2688458W
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
[book_pape_northrop]: https://openlibrary.org/works/OL27791413W
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
[ref_armstrong_frc]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_b2_spirit]: https://en.wikipedia.org/wiki/Northrop_Grumman_B-2_Spirit
[ref_bell_aircraft]: https://en.wikipedia.org/wiki/Bell_Aircraft
[ref_bell_x5]: https://en.wikipedia.org/wiki/Bell_X-5
[ref_boundary_layer]: https://en.wikipedia.org/wiki/Boundary_layer
[ref_buffeting]: https://en.wikipedia.org/wiki/Aeroelasticity#Buffeting
[ref_directional_stability]: https://en.wikipedia.org/wiki/Directional_stability
[ref_drag_coefficient]: https://en.wikipedia.org/wiki/Drag_coefficient
[ref_duralumin]: https://en.wikipedia.org/wiki/Duralumin
[ref_dutch_roll]: https://en.wikipedia.org/wiki/Dutch_roll
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_edwards_afb]: https://en.wikipedia.org/wiki/Edwards_Air_Force_Base
[ref_elevon]: https://en.wikipedia.org/wiki/Elevon
[ref_euler_equations_rigid]: https://en.wikipedia.org/wiki/Euler%27s_equations_(rigid_body_dynamics)
[ref_experimental_aircraft]: https://en.wikipedia.org/wiki/Experimental_aircraft
[ref_flight_dynamics]: https://en.wikipedia.org/wiki/Flight_dynamics_(fixed-wing_aircraft)
[ref_flight_envelope]: https://en.wikipedia.org/wiki/Flight_envelope
[ref_flight_test]: https://en.wikipedia.org/wiki/Flight_test
[ref_flow_separation]: https://en.wikipedia.org/wiki/Flow_separation
[ref_flying_wing]: https://en.wikipedia.org/wiki/Flying_wing
[ref_inertia_coupling]: https://en.wikipedia.org/wiki/Inertia_coupling
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_j30]: https://en.wikipedia.org/wiki/Westinghouse_J30
[ref_landing_gear]: https://en.wikipedia.org/wiki/Landing_gear
[ref_lift_coefficient]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_lift_to_drag]: https://en.wikipedia.org/wiki/Lift-to-drag_ratio
[ref_list_of_x_planes]: https://en.wikipedia.org/wiki/List_of_X-planes
[ref_load_factor]: https://en.wikipedia.org/wiki/Load_factor_(aeronautics)
[ref_longitudinal_static_stability]: https://en.wikipedia.org/wiki/Longitudinal_static_stability
[ref_mach_number]: https://en.wikipedia.org/wiki/Mach_number
[ref_mcdonnell_x36]: https://en.wikipedia.org/wiki/McDonnell_Douglas_X-36
[ref_me163]: https://en.wikipedia.org/wiki/Messerschmitt_Me_163_Komet
[ref_measurement_uncertainty]: https://en.wikipedia.org/wiki/Measurement_uncertainty
[ref_moment_of_inertia]: https://en.wikipedia.org/wiki/Moment_of_inertia
[ref_na_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_naca]: https://en.wikipedia.org/wiki/National_Advisory_Committee_for_Aeronautics
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasa_x3_factsheet]: https://www.nasa.gov/history/
[ref_nmusaf]: https://en.wikipedia.org/wiki/National_Museum_of_the_United_States_Air_Force
[ref_northrop_corp]: https://en.wikipedia.org/wiki/Northrop_Corporation
[ref_northrop_x4]: https://en.wikipedia.org/wiki/Northrop_X-4_Bantam
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_phugoid]: https://en.wikipedia.org/wiki/Phugoid
[ref_prandtl_number]: https://en.wikipedia.org/wiki/Prandtl_number
[ref_propagation_of_uncertainty]: https://en.wikipedia.org/wiki/Propagation_of_uncertainty
[ref_rcs]: https://en.wikipedia.org/wiki/Reaction_control_system
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_shock_wave]: https://en.wikipedia.org/wiki/Shock_wave
[ref_sound_barrier]: https://en.wikipedia.org/wiki/Sound_barrier
[ref_speed_of_sound]: https://en.wikipedia.org/wiki/Speed_of_sound
[ref_stabilator]: https://en.wikipedia.org/wiki/Stabilator
[ref_stability_augmentation]: https://en.wikipedia.org/wiki/Stability_augmentation_system
[ref_strain_gauge]: https://en.wikipedia.org/wiki/Strain_gauge
[ref_supersonic_speed]: https://en.wikipedia.org/wiki/Supersonic_speed
[ref_swept_wing]: https://en.wikipedia.org/wiki/Swept_wing
[ref_tailless]: https://en.wikipedia.org/wiki/Tailless_aircraft
[ref_takeoff]: https://en.wikipedia.org/wiki/Takeoff
[ref_telemetry]: https://en.wikipedia.org/wiki/Telemetry
[ref_transonic]: https://en.wikipedia.org/wiki/Transonic
[ref_us_standard_atmosphere]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_wave_drag]: https://en.wikipedia.org/wiki/Wave_drag
[ref_wind_tunnel]: https://en.wikipedia.org/wiki/Wind_tunnel
[ref_wing_loading]: https://en.wikipedia.org/wiki/Wing_loading
[ref_yaw_damper]: https://en.wikipedia.org/wiki/Yaw_damper
[ref_yb49]: https://en.wikipedia.org/wiki/Northrop_YB-49
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
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_a_comparative_2015]: https://doi.org/10.1201/b19371-12
[research_a_comparison_2022]: https://doi.org/10.14529/jsfi220401
[research_a_general_2010]: https://doi.org/10.2514/5.9781600867644.0353.0377
[research_a_new_2006]: https://doi.org/10.5139/jksas.2006.34.5.012
[research_abbott_boirun_1977]: https://doi.org/10.21236/ada045222
[research_abdelhamid_kandil_1998]: https://ntrs.nasa.gov/citations/19990041098
[research_abdulrahim_2004]: https://doi.org/10.2514/6.2004-128
[research_abramov_goman_2005]: https://doi.org/10.2514/6.2005-6331
[research_abramova_petrov_2016]: https://doi.org/10.1063/1.4963940
[research_abramova_petrov_2020]: https://doi.org/10.1134/s0015462820040023
[research_abualigah_ekinci_2024]: https://doi.org/10.31763/ijrcs.v4i2.1433
[research_abuelola_alqaisia_2024]: https://doi.org/10.1109/rem63063.2024.10735705
[research_abzug_daros_1955]: https://doi.org/10.21236/ada003615
[research_abzug_larrabee]: https://doi.org/10.1017/cbo9780511607141.005
[research_abzug_larrabee_b]: https://doi.org/10.1017/cbo9780511607141.023
[research_accelerated_development_1979]: https://ntrs.nasa.gov/citations/19790025046
[research_ackeret_1925]: https://ntrs.nasa.gov/citations/19930087085
[research_ackerman_xargay_2016]: https://doi.org/10.2514/6.2016-0631
[research_adamo_2023]: https://doi.org/10.21741/9781644902813-1
[research_adams]: https://doi.org/10.22215/etd/2017-11821
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_adams_1978]: https://ntrs.nasa.gov/citations/19780012199
[research_adams_1980]: https://ntrs.nasa.gov/citations/19810006482
[research_adams_hatch_1970]: https://doi.org/10.2514/6.1970-568
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adams_schy_1970]: https://ntrs.nasa.gov/citations/19700057227
[research_adams_silsby_1947]: https://ntrs.nasa.gov/citations/20030063953
[research_addendum_2_2000]: https://doi.org/10.1002/9781118903094.oth2
[research_addendum_3_2000]: https://doi.org/10.1002/9781118903094.oth3
[research_addington_myatt_2000]: https://doi.org/10.21236/ada383536
[research_adegbindin_love_2016]: https://doi.org/10.2514/6.2016-3361
[research_adler_martins_2023]: https://doi.org/10.2514/6.2023-4020
[research_advanced_aircraft_2026]: https://doi.org/10.1017/9781009399913.014
[research_advisorygroupforaerospaceresearchanddevelopment_1984]: https://ntrs.nasa.gov/citations/19840026325
[research_aerodynamic_and_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_aerodynamics_and_2016]: https://doi.org/10.1201/b13767-12
[research_aerodynamics_of_1976]: https://doi.org/10.2514/6.1976-198
[research_aeroelasticity_problems_2010]: https://doi.org/10.2514/5.9781600867552.0335.0373
[research_afaraj_mmohammed_2008]: https://doi.org/10.37649/aengs.2008.14201
[research_agarwal_deese_1983]: https://doi.org/10.2514/6.1983-501
[research_agarwal_deese_1984]: https://doi.org/10.2514/6.1984-1551
[research_agenbag_theron_2009]: https://doi.org/10.2514/1.39755
[research_agrawal_kinard_1991]: https://doi.org/10.2514/6.1991-3205
[research_agrell_elmeland_1984]: https://doi.org/10.2514/6.1984-2158
[research_agrell_elmeland_1985]: https://doi.org/10.2514/3.45185
[research_aharrah_lockenour_1969]: https://doi.org/10.2514/6.1969-895
[research_aharrah_lockenour_1971]: https://doi.org/10.2514/3.59105
[research_ahmed_kandagal_2016]: https://doi.org/10.1016/j.proeng.2016.05.153
[research_ahmed_worley_2008]: https://doi.org/10.2514/6.2008-366
[research_ahmed_zakaria_2024]: https://doi.org/10.1142/s230138502550027x
[research_ahn_kim_2017]: https://doi.org/10.5139/ijass.2017.18.2.290
[research_aiken_see_1951]: https://ntrs.nasa.gov/citations/20050031169
[research_aircraft_control_2011]: https://doi.org/10.1201/9781315252988-14
[research_aircraft_control_2016]: https://doi.org/10.1002/9781118827789.ch2
[research_aircraft_cruise_2011]: https://doi.org/10.2307/j.ctvcm4h26.12
[research_aircraft_cruise_2011_b]: https://doi.org/10.1515/9781400839063-010
[research_aircraft_dynamic_2003]: https://doi.org/10.2514/5.9781600862069.0303.0388
[research_aircraft_dynamic_2014]: https://doi.org/10.2514/5.9781624102547.0331.0420
[research_aircraft_dynamic_2024]: https://doi.org/10.2514/5.9781624107252.0333.0422
[research_aircraft_equations_2003]: https://doi.org/10.2514/5.9781600862069.0145.0172
[research_aircraft_equations_2014]: https://doi.org/10.2514/5.9781624102547.0163.0194
[research_aircraft_equations_2024]: https://doi.org/10.2514/5.9781624107252.0165.0196
[research_aircraft_flight_2014]: https://doi.org/10.1201/b17346-12
[research_aircraft_in_1997]: https://doi.org/10.2514/5.9781600861529.0141.0150
[research_aircraft_instrument_1998]: https://doi.org/10.1108/aeat.1998.12770cad.015
[research_aircraft_lateral_directional_2011]: https://doi.org/10.1049/pbce074e_ch9
[research_aircraft_longitudinal_2011]: https://doi.org/10.1049/pbce074e_ch10
[research_aircraft_non_linear_2014]: https://doi.org/10.1201/b17346-8
[research_aircraft_stability_1998]: https://doi.org/10.2514/5.9781600862052.0333.0354
[research_aircraft_stability_2003]: https://doi.org/10.2514/5.9781600862069.0433.0472
[research_aircraft_stability_2014]: https://doi.org/10.2514/5.9781624102547.0465.0508
[research_aircraft_stability_2021]: https://doi.org/10.47176/jafm.14.03.31974
[research_aircraft_stability_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n42
[research_aircraft_stability_2024]: https://doi.org/10.2514/5.9781624107252.0467.0510
[research_aircraft_stability_2026]: https://doi.org/10.1017/9781009399913.010
[research_aircraft_static_2003]: https://doi.org/10.2514/5.9781600862069.0173.0238
[research_aircraft_static_2014]: https://doi.org/10.2514/5.9781624102547.0195.0264
[research_aircraft_static_2024]: https://doi.org/10.2514/5.9781624107252.0197.0266
[research_aircraft_steady_2011]: https://doi.org/10.2307/j.ctvcm4h26.13
[research_aircraft_steady_2011_b]: https://doi.org/10.1515/9781400839063-011
[research_aircraft_steady_2011_c]: https://doi.org/10.2307/j.ctvcm4h26.11
[research_aircraft_steady_2011_d]: https://doi.org/10.1515/9781400839063-009
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320203
[research_airforcetestpilotschooledwardsafbca_1967]: https://doi.org/10.21236/ada320209
[research_airforcetestpilotschooledwardsafbca_1969]: https://doi.org/10.21236/ada319985
[research_airforcetestpilotschooledwardsafbca_1981]: https://doi.org/10.21236/ada320347
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1988_b]: https://doi.org/10.21236/ada319979
[research_airforcetestpilotschooledwardsafbca_1988_e]: https://doi.org/10.21236/ada319975
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_c]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1990_d]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada319972
[research_airforcetestpilotschooledwardsafbca_1991_b]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada319982
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_airplane_trim_2012]: https://doi.org/10.1017/cbo9781139161893.010
[research_airplane_trim_2022]: https://doi.org/10.2514/5.9781624106408.0223.0240
[research_airspeed_calibration_2008]: https://doi.org/10.5302/j.icros.2008.14.7.629
[research_airspeed_calibration_2011]: https://doi.org/10.2514/5.9781600868283.0013.0017
[research_airspeed_calibration_2021]: https://doi.org/10.1002/9781118949818.ch8
[research_airspeed_definitions_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n29
[research_airspeed_systems_2003]: https://doi.org/10.2514/5.9781600861840.0029.0038
[research_ajaj_djidjeli_2022]: https://doi.org/10.3390/designs6050092
[research_alaian_basuno_2014]: https://doi.org/10.4028/www.scientific.net/amm.660.481
[research_alatorre_castillo_2021]: https://doi.org/10.1109/icuas51884.2021.9476680
[research_albakri_albakri_2020]: https://doi.org/10.2514/1.g004934
[research_alberghini_lee_2018]: https://doi.org/10.2514/6.2018-4170
[research_albisser_dobre_2014]: https://doi.org/10.1109/ecc.2014.6862536
[research_alex_2014]: https://doi.org/10.14323/ijuseng.2014.4
[research_algilani_abdunabi_2009]: https://doi.org/10.21608/asat.2009.23738
[research_alhiddabi_mcclamroch_2002]: https://doi.org/10.2514/2.4871
[research_ali_1997]: https://ntrs.nasa.gov/citations/19970026582
[research_ali_okasha_2025]: https://doi.org/10.1016/j.treng.2025.100397
[research_ali_rasani_2026]: https://doi.org/10.1098/rsos.251990
[research_alighanbari_2002]: https://doi.org/10.2514/2.2986
[research_allen_1951]: https://ntrs.nasa.gov/citations/19930086898
[research_allen_1976]: https://ntrs.nasa.gov/citations/19760009048
[research_allen_lizotte_2005]: https://ntrs.nasa.gov/citations/20050204113
[research_allen_tuttle_1973]: https://ntrs.nasa.gov/citations/19740004405
[research_allwing_modifications_1945]: https://ntrs.nasa.gov/citations/19930092557
[research_allwing_stability_1945]: https://ntrs.nasa.gov/citations/19930092552
[research_alsahlani_johnston_2017]: https://doi.org/10.1051/eucass/201609003
[research_altman_1952]: https://doi.org/10.21236/ada075871
[research_altunkaya_2025]: https://doi.org/10.2514/1.g008188
[research_altunkaya_ozkol_2022]: https://doi.org/10.1016/j.ast.2021.107310
[research_altunkaya_ozkol_2022_b]: https://doi.org/10.20944/preprints202212.0180.v1
[research_altunkaya_ozkol_2023]: https://doi.org/10.3390/aerospace10030234
[research_alwi_edwards_2007]: https://doi.org/10.1109/cca.2007.4389401
[research_alwi_edwards_2009]: https://doi.org/10.1109/acc.2009.5160331
[research_alyanak_pendleton_2014]: https://doi.org/10.2514/6.2014-3158
[research_ameho_prempain_2011]: https://doi.org/10.1109/acc.2011.5991349
[research_amendola_dimino_2018]: https://doi.org/10.1016/b978-0-08-100964-2.00018-6
[research_ammar_legros_2017]: https://doi.org/10.1016/j.ast.2017.09.037
[research_ammar_trepanier_2014]: https://doi.org/10.1115/imece2014-36676
[research_amprikidis_cooper_2004]: https://doi.org/10.2514/6.2004-1884
[research_an_analysis_1981]: https://doi.org/10.2514/6.1981-364
[research_an_experimental_1978]: https://doi.org/10.2514/6.1978-1200
[research_an_introduction_1966]: https://doi.org/10.1016/c2013-0-08104-2
[research_an_investigation_1974]: https://ntrs.nasa.gov/citations/19740013534
[research_analytical_synthesis_2024]: https://doi.org/10.36652/0869-4931-2024-78-9-404-410
[research_anandakumar_bernstein_2022]: https://doi.org/10.2514/6.2022-0965
[research_ananthasayanam_2002]: https://doi.org/10.2514/6.2002-4877
[research_ananthkrishnan_2004]: https://doi.org/10.2514/6.2004-4950
[research_ananthkrishnan_ramadevi_2002]: https://doi.org/10.2514/2.4952
[research_andersen_kolonay_1997]: https://doi.org/10.2514/6.1997-1385
[research_andersen_kolonay_1998]: https://doi.org/10.2514/2.2378
[research_andersen_kolonay_1998_b]: https://doi.org/10.2514/6.1998-529
[research_anderson_1949]: https://ntrs.nasa.gov/citations/19930082543
[research_anderson_1970]: https://doi.org/10.21236/ad0710590
[research_anderson_1975]: https://ntrs.nasa.gov/citations/19750013155
[research_anderson_1986]: https://ntrs.nasa.gov/citations/19870013196
[research_anderson_berger_1972]: https://doi.org/10.2514/6.1972-870
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_bray_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_anderson_christofferson_1947]: https://ntrs.nasa.gov/citations/20030064139
[research_anderson_cooper_1947]: https://ntrs.nasa.gov/citations/20030063229
[research_anderson_vincent_1985]: https://doi.org/10.1109/cdc.1985.268918
[research_ando_kajita_1992]: https://doi.org/10.2322/jjsass1969.40.14
[research_andreeairina_achim_2014]: https://doi.org/10.13111/2066-8201.2014.6.s1.1
[research_andrew_stenton_1967]: https://doi.org/10.2514/6.1967-16
[research_andrianantara_ghazi_2025]: https://doi.org/10.2514/6.2025-1826
[research_anglin_byrdsong_1982]: https://doi.org/10.2514/6.1982-960
[research_ankenbruck_1946]: https://ntrs.nasa.gov/citations/19930092559
[research_ankenbruck_mckinney_1947]: https://ntrs.nasa.gov/citations/19930082130
[research_ankenbruck_sadoff_1951]: https://ntrs.nasa.gov/citations/19930086811
[research_ansell_bragg_2010]: https://doi.org/10.2514/6.2010-4225
[research_ansell_bragg_2011]: https://doi.org/10.2514/1.c031435
[research_ansell_kerho_2014]: https://doi.org/10.2514/1.c032703
[research_anton_botez_2009]: https://doi.org/10.2514/6.2009-6046
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_antoniou_antoniou_2025]: https://doi.org/10.3390/engproc2025090018
[research_aoyagi_hickey_1963]: https://ntrs.nasa.gov/citations/19630006046
[research_appendices_a_1990]: https://doi.org/10.1515/9781400855988.687
[research_appendix_b_2003]: https://doi.org/10.2514/5.9781600862069.0573.0576
[research_appendix_c_2021]: https://doi.org/10.1002/9781118949818.app3
[research_appendix_g_2003]: https://doi.org/10.2514/5.9781600862069.0609.0612
[research_appendix_h_2003]: https://doi.org/10.2514/5.9781600862069.0613.0622
[research_application_of]: https://doi.org/10.1007/bfb0043104
[research_application_of_quasi_object_2008]: https://doi.org/10.18372/1990-5548.18.642
[research_approach_and_2017]: https://doi.org/10.1002/9781118534786.ch11
[research_approximate_expressions_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50024-1
[research_approximate_expressions_2007]: https://doi.org/10.1016/b978-075066927-6/50025-8
[research_approximate_expressions_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00031-6
[research_arabian_schmeer_1955]: https://ntrs.nasa.gov/citations/20090026307
[research_arai_noto_2000]: https://doi.org/10.2514/6.2000-4327
[research_araujo_singh_1998]: https://doi.org/10.2514/2.4250
[research_araujoestrada_lowenberg_2022]: https://doi.org/10.1016/j.ast.2021.107325
[research_archambaud_louis_2004]: https://doi.org/10.2514/6.2004-2245
[research_arena_nelson_1989]: https://doi.org/10.2514/6.1989-3348
[research_arena_nelson_1990]: https://ntrs.nasa.gov/citations/19900058097
[research_arena_nelson_1991]: https://doi.org/10.2514/6.1991-434
[research_arena_nelson_1992]: https://doi.org/10.2514/6.1992-4497
[research_arena_nelson_1994]: https://doi.org/10.2514/3.46625
[research_argyle_beard_2016]: https://doi.org/10.1109/acc.2016.7526733
[research_arif_singh_2023]: https://doi.org/10.2514/6.2023-1567
[research_arik_turkmen_2018]: https://doi.org/10.4316/aece.2018.04007
[research_armenta_takahashi_2021]: https://doi.org/10.2514/6.2021-2441
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnold_1968]: https://doi.org/10.2514/6.1968-1068
[research_artificial_pitch_damping_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_aryass_hfarhood_2009]: https://doi.org/10.30684/etj.27.9.16
[research_asada_kawai_2024]: https://doi.org/10.2514/6.2024-0494
[research_asadi_sabzehparvar_2013]: https://doi.org/10.1108/00022661311313623
[research_asai_2022]: https://doi.org/10.52843/cassyni.pd9g9h
[research_asher_martuccelli_1957]: https://doi.org/10.21236/ad0142088
[research_ashkenas_1946]: https://ntrs.nasa.gov/citations/19930084594
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_ashkenas_1965_b]: https://doi.org/10.21236/ad0627989
[research_ashkenas_1965_c]: https://doi.org/10.2514/6.1965-314
[research_ashkenas_1969]: https://doi.org/10.2514/6.1969-898
[research_ashkenas_1971]: https://doi.org/10.2514/3.59104
[research_ashkenas_1982]: https://doi.org/10.2514/6.1982-1353
[research_ashkenas_klyde_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashley_1980]: https://doi.org/10.2514/3.57891
[research_ashworth_mouch_1988]: https://doi.org/10.2514/6.1988-563
[research_aslam_islam_2025]: https://doi.org/10.2514/6.2025-2429
[research_aso_tanaka_2017]: https://doi.org/10.1299/jsmemecj.2017.g1800304
[research_aso_tanaka_2018]: https://doi.org/10.1299/jsmetld.2018.27.1003
[research_assadourian_reeder_1948]: https://ntrs.nasa.gov/citations/20050029413
[research_atesoglu_ozgoren_2006]: https://doi.org/10.2514/6.2006-6056
[research_atesoglu_ozgoren_2011]: https://doi.org/10.2514/6.2011-6636
[research_atkinson_2016]: https://doi.org/10.2514/6.2016-1185
[research_atmaca_stroosma_2026]: https://doi.org/10.2514/6.2026-0550
[research_atmaca_vankampen_2025]: https://doi.org/10.2514/6.2025-0081
[research_atmospheric_disturbance_1981]: https://doi.org/10.2514/6.1981-302
[research_atzhorn_stengel_1981]: https://doi.org/10.2514/6.1981-2331
[research_atzhorn_stengel_1984]: https://doi.org/10.2514/3.19866
[research_aubeelack]: https://doi.org/10.70675/fa207839z078cz4de3za09fz53641267d140
[research_aulchenko_zamuraev_2012]: https://doi.org/10.1134/s1063785012090027
[research_avanzini_nicassio_2017]: https://doi.org/10.2514/1.g002387
[research_averett_wright_1966]: https://ntrs.nasa.gov/citations/19660010231
[research_axelson_1947]: https://ntrs.nasa.gov/citations/19790079934
[research_axelson_1975]: https://doi.org/10.2514/6.1975-996
[research_axelson_1977]: https://doi.org/10.2514/3.58819
[research_ayele_maldonado_2023]: https://doi.org/10.20944/preprints202311.1589.v1
[research_ayers_hallissy_1981]: https://ntrs.nasa.gov/citations/19810023573
[research_ayoub_mclachlan_1987]: https://doi.org/10.2514/6.1987-1230
[research_ayoub_mclachlan_1988]: https://doi.org/10.1063/1.4738826
[research_azor_1995]: https://doi.org/10.2514/6.1995-3312
[research_babcock_arena_2004]: https://doi.org/10.2514/6.2004-5174
[research_babinsky_ogawa_2006]: https://doi.org/10.2514/6.2006-3698
[research_babister_1980]: https://doi.org/10.1016/b978-0-08-024768-7.50013-2
[research_babister_1980_b]: https://doi.org/10.1016/b978-0-08-024768-7.50011-9
[research_bachelder_aponso_2020]: https://doi.org/10.4050/sm_2020_hq-915
[research_bachelder_aponso_2020_b]: https://doi.org/10.4050/sm_2020_hq-914
[research_bachelder_aponso_2022]: https://doi.org/10.2514/6.2022-0890
[research_bachelder_aponso_2023]: https://doi.org/10.4050/sm_2023_hq-1194
[research_bachelder_aponso_2023_b]: https://doi.org/10.2514/6.2023-1369
[research_bachelder_aponso_2023_c]: https://doi.org/10.4050/sm_2023_hq-1185
[research_baggi_franco_2020]: https://doi.org/10.2514/6.2020-0841
[research_baggi_serrani_2022]: https://doi.org/10.1109/ccta49430.2022.9966141
[research_bahri_2018]: https://doi.org/10.1088/1742-6596/1130/1/012026
[research_bailey_knotts_1987]: https://doi.org/10.2514/6.1987-2370
[research_bailey_powers_1988]: https://doi.org/10.2514/6.1988-4327
[research_bailey_smith_1981]: https://doi.org/10.2514/6.1981-1776
[research_bailey_smith_1982]: https://ntrs.nasa.gov/citations/19830004840
[research_bainsla_singari_2021]: https://doi.org/10.4271/2021-01-0040
[research_bajpai_chang]: https://doi.org/10.1109/dasc.2001.964246
[research_bakaul_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.178
[research_bakaul_wang_2015]: https://doi.org/10.2514/6.2015-0746
[research_bakaul_wang_2015_b]: https://doi.org/10.2514/6.2015-1039
[research_bakaul_yankui_2014]: https://doi.org/10.2514/1.j052957
[research_baker_farrell_1991]: https://doi.org/10.2514/6.1991-2836
[research_baker_johnson_1955]: https://ntrs.nasa.gov/citations/19930088625
[research_balakrishna_niranjana_1987]: https://doi.org/10.2514/6.1987-2626
[research_balas_hodgkinson_2009]: https://doi.org/10.2514/6.2009-6319
[research_balasubramanian_ahuja_2024]: https://doi.org/10.2514/6.2024-4144
[research_balasubramanian_n_2026]: https://doi.org/10.2139/ssrn.6295219
[research_ball_1978]: https://doi.org/10.2514/6.1978-1500
[research_ball_1979]: https://doi.org/10.2514/3.58559
[research_balleur_girodrouxlavigne_2002]: https://doi.org/10.1007/978-3-540-45856-2_9
[research_ballouz_chang]: https://doi.org/10.17918/etd-7772
[research_balogun_khan_2026]: https://doi.org/10.2514/6.2026-2330
[research_bandettini_1952]: https://ntrs.nasa.gov/citations/19930087234
[research_banerjee_1984]: https://doi.org/10.2514/3.45022
[research_banerjee_1988]: https://doi.org/10.2514/6.1988-2212
[research_banerjee_1988_b]: https://doi.org/10.2514/3.45607
[research_banerjee_liu_2014]: https://doi.org/10.5890/jand.2014.12.012
[research_banner_1958]: https://ntrs.nasa.gov/citations/19630008170
[research_barakos_drikakis_1999]: https://doi.org/10.1615/tsfp1.1590
[research_barber_haise_1966]: https://doi.org/10.4271/660219
[research_barbosa_bertolin_2019]: https://doi.org/10.2514/6.2019-0365
[research_barbut_braza_2010]: https://doi.org/10.1007/978-3-642-14168-3_16
[research_bare_berrier_1981]: https://ntrs.nasa.gov/citations/19810021548
[research_bargill_stengel_1983]: https://doi.org/10.4271/830761
[research_barinov_pavlenko_2016]: https://doi.org/10.1615/tsagiscij.2016018284
[research_barker_balas_1999]: https://doi.org/10.2514/6.1999-4133
[research_barnard_1969]: https://doi.org/10.2514/6.1969-793
[research_barnes_visbal_2020]: https://doi.org/10.2514/6.2020-3043
[research_barnwell_1974]: https://doi.org/10.2514/6.1974-185
[research_barnwell_heinzen_2003]: https://ntrs.nasa.gov/citations/20040001365
[research_barren_larson]: https://doi.org/10.1109/naecon.1995.521987
[research_barsby_1973]: https://doi.org/10.1017/s0001925900006508
[research_bartlett_1975]: https://ntrs.nasa.gov/citations/19830002803
[research_bartlett_sangiorgio_1975]: https://ntrs.nasa.gov/citations/19830002815
[research_basiliochaves]: https://doi.org/10.17771/pucrio.acad.23190
[research_bass_stoner_1966]: https://ntrs.nasa.gov/citations/19670061426
[research_bateman_argrow_2004]: https://doi.org/10.2514/6.2004-6587
[research_bateman_noura_2008]: https://doi.org/10.1109/med.2008.4602147
[research_batina_1986]: https://doi.org/10.2514/6.1986-862
[research_batina_1986_b]: https://doi.org/10.2514/3.45324
[research_batina_1986_c]: https://doi.org/10.2514/3.45302
[research_batina_1988]: https://doi.org/10.2514/6.1988-105
[research_batina_1989]: https://doi.org/10.2514/3.45734
[research_batina_seidel_1989]: https://doi.org/10.2514/3.45718
[research_batterson_klein_1984]: https://doi.org/10.2514/6.1984-2085
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_bazile_calderara_2012]: https://doi.org/10.1051/eucass/201203053
[research_bazuhair_2018]: https://doi.org/10.3103/s106879981802006x
[research_bazuhair_2019]: https://doi.org/10.3846/aviation.2019.10301
[research_bean_lee_1994]: https://doi.org/10.2514/6.1994-1800
[research_beaufrere_1988]: https://doi.org/10.2514/6.1988-4503
[research_bechelder_bjorkman_2025]: https://doi.org/10.4050/sm_handling_2025-5299
[research_becht_1950]: https://ntrs.nasa.gov/citations/19930086394
[research_becht_few_1950]: https://ntrs.nasa.gov/citations/19930086242
[research_beeler_1956]: https://ntrs.nasa.gov/citations/19930084521
[research_begnini_bones_2018]: https://doi.org/10.2514/6.2018-3004
[research_beh_hofinger_2018]: https://doi.org/10.1201/9781315136820-15
[research_beldica_hilton_1999]: https://doi.org/10.2514/6.1999-1423
[research_belesiotiskataras_timme_2020]: https://doi.org/10.2514/6.2020-1985
[research_belesiotiskataras_timme_2021]: https://doi.org/10.2514/6.2021-0611
[research_belisle_neale_2010]: https://doi.org/10.2514/6.2010-4381
[research_bellman_1959]: https://ntrs.nasa.gov/citations/19980228028
[research_benchaita_ladaci_2021]: https://doi.org/10.1016/j.ast.2021.106745
[research_bendiksen_2008]: https://doi.org/10.2514/1.29547
[research_bendiksen_2009]: https://doi.org/10.2514/1.36413
[research_benepe_cunningham_1974]: https://ntrs.nasa.gov/citations/19740043918
[research_benepe_cunningham_1978]: https://ntrs.nasa.gov/citations/19780025170
[research_bengtson_dickovich_1975]: https://doi.org/10.21236/ada016932
[research_benjamin_hesse_2021]: https://doi.org/10.2514/6.2021-2517
[research_bennett_1947]: https://ntrs.nasa.gov/citations/20050019246
[research_bennett_johnson_1947]: https://ntrs.nasa.gov/citations/19930081894
[research_benoit_verbeke_2014]: https://doi.org/10.2514/6.2014-2056
[research_benyamen_mckinnis_2020]: https://doi.org/10.1109/aero47225.2020.9172481
[research_bera_1974]: https://doi.org/10.2514/3.44413
[research_bera_1974_b]: https://doi.org/10.2514/3.59229
[research_berg_1991]: https://doi.org/10.2514/6.1991-2630
[research_berger_christensen_2025]: https://doi.org/10.4050/sm_handling_2025-5294
[research_berger_tischler_2012]: https://doi.org/10.2514/6.2012-4503
[research_berger_tischler_2013]: https://doi.org/10.2514/6.2013-4506
[research_bernal_2016]: https://doi.org/10.2514/6.2016-0287
[research_berry_1981]: https://doi.org/10.2514/6.1981-1823
[research_berry_1982]: https://ntrs.nasa.gov/citations/19820044745
[research_berry_1985]: https://doi.org/10.2514/6.1985-1852
[research_berry_1986]: https://doi.org/10.2514/3.20153
[research_berry_1986_b]: https://doi.org/10.2514/3.22902
[research_berry_mallick_1976]: https://ntrs.nasa.gov/citations/19770011063
[research_berry_powers_1970]: https://doi.org/10.2514/6.1970-566
[research_bertelrud_1981]: https://doi.org/10.2514/6.1981-2418
[research_bertelrud_graves_1994]: https://doi.org/10.2514/6.1994-2152
[research_bertelsen_2006]: https://doi.org/10.2514/1.20509
[research_berthold_1977]: https://ntrs.nasa.gov/citations/19770014233
[research_bertolin_2021]: https://doi.org/10.2514/1.g005783
[research_bertoni_bertozzi_2010]: https://doi.org/10.1109/acc.2010.5530953
[research_beyers_brown_2006]: https://doi.org/10.2514/6.2006-6001
[research_bharadvaj_1990]: https://doi.org/10.2514/6.1990-935
[research_bharadvaj_1991]: https://doi.org/10.2514/3.10817
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_nener_2019]: https://doi.org/10.1109/access.2019.2894961
[research_biber_2016]: https://doi.org/10.2514/6.2016-0806
[research_biber_2017]: https://doi.org/10.1504/ijsa.2017.10007965
[research_bidinotto_2021]: https://doi.org/10.1017/aer.2021.82
[research_bielat_1959]: https://ntrs.nasa.gov/citations/19980232001
[research_bielat_pierpont_1960]: https://ntrs.nasa.gov/citations/19650017034
[research_bielat_wiley_1959]: https://ntrs.nasa.gov/citations/19980227088
[research_biezad_bole_2001]: https://doi.org/10.2514/6.2001-4198
[research_bihrle_1969]: https://doi.org/10.2514/6.1969-894
[research_bihrle_mulcay_1979]: https://ntrs.nasa.gov/citations/19800003810
[research_bingaman_2012]: https://doi.org/10.2514/6.2012-4415
[research_binwenlu_jianjunma_2016]: https://doi.org/10.1109/cgncc.2016.7828906
[research_bippes_1990]: https://doi.org/10.1007/978-3-642-84103-3_38
[research_birch_lee_2005]: https://doi.org/10.2514/1.13139
[research_bird_fisher_1953]: https://ntrs.nasa.gov/citations/19930091098
[research_bird_jaquet_1951]: https://ntrs.nasa.gov/citations/19930092084
[research_biriukov_1959]: https://doi.org/10.1016/0021-8928(59)90174-1
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_bischoff_palmer_1983]: https://doi.org/10.21236/ada327418
[research_bise_black]: https://doi.org/10.1109/naecon.1990.112814
[research_bishop_1961]: https://doi.org/10.1017/s0368393100075957
[research_black]: https://doi.org/10.22215/etd/1993-02521
[research_black_1956]: https://doi.org/10.1017/s0368393100132390
[research_black_2009]: https://doi.org/10.2514/6.2009-6324
[research_black_moorhouse_1979]: https://doi.org/10.21236/ada085085
[research_black_thomas]: https://doi.org/10.1109/naecon.1989.40228
[research_blaesser_frederick_2020]: https://doi.org/10.2514/6.2020-2633
[research_blake_1993]: https://doi.org/10.2514/6.1993-3619
[research_blake_gotwald_2009]: https://doi.org/10.2514/6.2009-6044
[research_bland_young_1961]: https://ntrs.nasa.gov/citations/19660024039
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_blight_gangsaas_1986]: https://doi.org/10.2514/3.20145
[research_blight_lanedailey_2018]: https://doi.org/10.1201/9781315136820-9
[research_blodgett_lagor_2022]: https://doi.org/10.2514/6.2022-2036
[research_bloy_1996]: https://doi.org/10.1177/030641909602400305
[research_bloy_1998]: https://doi.org/10.2514/2.7580
[research_bobbitt_1980]: https://doi.org/10.2514/6.1980-861
[research_bobbitt_foughner_1985]: https://ntrs.nasa.gov/citations/19860053591
[research_bodonyl_1994]: https://doi.org/10.21236/ada281526
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_bodur_ucun_2023]: https://doi.org/10.1109/rast57548.2023.10197950
[research_boelens_2017]: https://doi.org/10.2514/1.c033211
[research_bogatyrev_2017]: https://doi.org/10.1615/tsagiscij.2017020745
[research_bogdan_radu_2010]: https://doi.org/10.13111/2066-8201.2010.2.1.2
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmann_weisshaar_1988]: https://doi.org/10.2514/6.1988-2263
[research_boisseau_1955]: https://ntrs.nasa.gov/citations/20050029385
[research_bollech_furlong_1948]: https://ntrs.nasa.gov/citations/19930085413
[research_bolton_collins_1974]: https://doi.org/10.2514/6.1974-860
[research_bon_2021]: https://doi.org/10.31031/aes.2021.02.000523
[research_bonnifet_gerolymos_2017]: https://doi.org/10.2514/6.2017-3955
[research_boothe_1971]: https://doi.org/10.2514/6.1971-771
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_booz_1988]: https://doi.org/10.2514/6.1988-4363
[research_boppe_1977]: https://doi.org/10.2514/6.1977-207
[research_boppe_1978]: https://doi.org/10.2514/6.1978-104
[research_bordei_halanay_2018]: https://doi.org/10.1063/1.5081531
[research_borri_trainelli_2003]: https://doi.org/10.2514/6.2003-5620
[research_bosch_kuehl_1976]: https://doi.org/10.2514/6.1976-1932
[research_boschetti_cardenas_2010]: https://doi.org/10.2514/6.2010-8121
[research_boschetti_cardenas_2012]: https://doi.org/10.2514/6.2012-1051
[research_boskovic_ling]: https://doi.org/10.1109/cdc.2002.1184767
[research_boskovic_mehra]: https://doi.org/10.1109/acc.2002.1024911
[research_boskovic_mehra_1999]: https://doi.org/10.2514/6.1999-4041
[research_boskovic_mehra_2000]: https://doi.org/10.2514/2.4617
[research_boskovic_saimingli]: https://doi.org/10.1109/plans.2000.838323
[research_bossert_morris_2003]: https://doi.org/10.2514/4.862069
[research_boswinkle_smith_1958]: https://ntrs.nasa.gov/citations/19660027826
[research_bosworth_stoliker_1996]: https://ntrs.nasa.gov/citations/19960029101
[research_bosworth_williamshayes_2007]: https://ntrs.nasa.gov/citations/20070022348
[research_bosworth_williamshayes_2010]: https://ntrs.nasa.gov/citations/20100025868
[research_botez_rotaru_2007]: https://doi.org/10.1017/s0001924000004528
[research_bouadi]: https://doi.org/10.70675/aa62b2a6zce9ez41fcz95cdz6ebfead4b829
[research_bouadi_choukroun_2012]: https://doi.org/10.1109/dasc.2012.6382988
[research_bourdin_2002]: https://doi.org/10.2514/6.2002-3151
[research_bourdin_gatto_2007]: https://doi.org/10.2514/6.2007-4443
[research_bowes_miller_1976]: https://doi.org/10.21236/ada026963
[research_bowling_key_1976]: https://ntrs.nasa.gov/citations/19760024079
[research_bowlus_multhopp_1997]: https://doi.org/10.2514/6.1997-3830
[research_bowman_stough_1978]: https://doi.org/10.2514/6.1978-1477
[research_boyden_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_bradshaw_davis_1985]: https://doi.org/10.2514/6.1985-3088
[research_bragg_soltani_1990]: https://doi.org/10.2514/3.45928
[research_bragin_2018]: https://doi.org/10.1615/tsagiscij.2018029594
[research_bramantya_nugroho_2025]: https://doi.org/10.14710/teknik.v46i3.54148
[research_brand_1981]: https://ntrs.nasa.gov/citations/19830035754
[research_brandon_1986]: https://ntrs.nasa.gov/citations/19860009816
[research_brandon_brown_1995]: https://doi.org/10.2514/6.1995-3457
[research_brandon_lan_2001]: https://doi.org/10.2514/6.2001-4017
[research_brandon_simon_1996]: https://doi.org/10.2514/6.1996-3444
[research_brandt_bons_2024]: https://doi.org/10.2514/6.2024-0693
[research_brandt_fossum_2011]: https://doi.org/10.2514/6.2011-7039
[research_brandt_mcfadden_2022]: https://doi.org/10.2514/6.2022-3888
[research_brauser_1982]: https://doi.org/10.1016/s1474-6670(17)62884-2
[research_brauser_1983]: https://doi.org/10.1016/b978-0-08-029348-6.50013-0
[research_bray_1963]: https://doi.org/10.2514/6.1963-1003
[research_breneman_lower_1992]: https://doi.org/10.2514/6.1992-4083
[research_breul_keller_1985]: https://doi.org/10.2514/6.1985-3062
[research_breul_keller_1987]: https://doi.org/10.2514/3.20202
[research_brewer_1946]: https://ntrs.nasa.gov/citations/20050031173
[research_brewer_may_1948]: https://ntrs.nasa.gov/citations/19930082266
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brigidogonzalez_rodriguezcortes_2014]: https://doi.org/10.1109/acc.2014.6859390
[research_brincklow_hunsaker_2021]: https://doi.org/10.1017/aer.2020.139
[research_brincklow_montgomery_2021]: https://doi.org/10.2514/6.2021-0327
[research_brincklow_montgomery_2024]: https://doi.org/10.1017/aer.2024.21
[research_brinker_wise_1996]: https://doi.org/10.2514/3.21782
[research_brinker_wise_1998]: https://doi.org/10.2514/6.1998-4107
[research_brinker_wise_1999]: https://doi.org/10.2514/6.1999-4040
[research_brinker_wise_2000]: https://doi.org/10.2514/6.2000-3941
[research_brinker_wise_2001]: https://doi.org/10.2514/2.4826
[research_brody_fagley_2025]: https://doi.org/10.2514/1.c038208
[research_bronz_aydin_2019]: https://doi.org/10.2514/6.2019-0580
[research_brooks_1986]: https://doi.org/10.2514/6.1986-9796
[research_broussard_stengel_1977]: https://doi.org/10.2514/3.44630
[research_brower_wright_1966]: https://ntrs.nasa.gov/citations/19660005466
[research_brown_1959]: https://ntrs.nasa.gov/citations/19980228294
[research_brown_adams_1948]: https://ntrs.nasa.gov/citations/19930082378
[research_brown_bradley_1981]: https://doi.org/10.2514/6.1981-2390
[research_brown_vos_2018]: https://doi.org/10.2514/6.2018-0522
[research_browne_maldonado_2024]: https://doi.org/10.2514/6.2024-0065
[research_browne_maldonado_2025]: https://doi.org/10.2514/1.c037981
[research_bruner_1983]: https://doi.org/10.4271/830711
[research_brunet_deck_2008]: https://doi.org/10.2514/6.2008-4152
[research_brunosantos_oliveira_2020]: https://doi.org/10.5151/siintec2020-analysisofelevator
[research_brunton_noack_2020]: https://doi.org/10.1146/annurev-fluid-010719-060214
[research_brutch_moncayo_2024]: https://doi.org/10.2514/6.2024-1200
[research_bryant_1950]: https://ntrs.nasa.gov/citations/19930090408
[research_bryson_1954]: https://doi.org/10.2514/8.2916
[research_bryson_1969]: https://doi.org/10.2514/6.1969-865
[research_bryson_rumpfkeil_2016]: https://doi.org/10.2514/6.2016-0294
[research_buch_georgem_2010]: https://doi.org/10.21236/ada526601
[research_buckingham_1914]: https://doi.org/10.1103/physrev.4.345
[research_buddhamatya_miranda_2026]: https://doi.org/10.2514/6.2026-2116
[research_buell_johnson_1959]: https://ntrs.nasa.gov/citations/19980228141
[research_buell_tinling_1957]: https://ntrs.nasa.gov/citations/19930084743
[research_buenz_brooks_1975]: https://doi.org/10.21236/ada021996
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_buffington_sparks_1993]: https://doi.org/10.23919/acc.1993.4792886
[research_buffington_sparks_1994]: https://doi.org/10.1016/0005-1098(94)90093-0
[research_buffington_sparks_1998]: https://doi.org/10.2514/6.1998-4248
[research_buffington_sparks_1998_b]: https://doi.org/10.1109/acc.1998.703591
[research_bugala_sznajder_2023]: https://doi.org/10.2478/tar-2023-0023
[research_bui_2013]: https://doi.org/10.2514/6.2013-3032
[research_bui_2015]: https://doi.org/10.2514/1.c032883
[research_bui_2016]: https://doi.org/10.2514/6.2016-3720
[research_bui_2018]: https://doi.org/10.2514/6.2018-3808
[research_bull_kidd_1955]: https://doi.org/10.21236/ad0106019
[research_bunescu_stoican_2024]: https://doi.org/10.3390/aerospace11070579
[research_burcham_burken_1994]: https://doi.org/10.2514/6.1994-2123
[research_burcham_maine_1992]: https://doi.org/10.2514/6.1992-4109
[research_burdges_1973]: https://doi.org/10.2514/6.1973-792
[research_burken_williamshayes_2006]: https://ntrs.nasa.gov/citations/20060023991
[research_burkhalter_1993]: https://doi.org/10.2514/3.46447
[research_burkhalter_spring_1992]: https://doi.org/10.2514/3.46183
[research_burlion_poussotvassal_2014]: https://doi.org/10.3182/20140824-6-za-1003.01588
[research_burner_martinson_1996]: https://doi.org/10.2514/6.1996-2253
[research_burnham_1995]: https://doi.org/10.2514/6.1995-1338
[research_burton_bischoff_1976]: https://doi.org/10.2514/6.1976-894
[research_burton_lamour_1971]: https://doi.org/10.2514/6.1971-49
[research_buter_rao_1984]: https://ntrs.nasa.gov/citations/19850002610
[research_butler_1976]: https://doi.org/10.21236/ada032654
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_bons_2025]: https://doi.org/10.2514/6.2025-0260
[research_bwb_bli_2006]: https://ntrs.nasa.gov/citations/20080015860
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_cabaleirodelahoz_fioriti_2021]: https://doi.org/10.1177/09544100211063110
[research_cadwell]: https://doi.org/10.15368/theses.2010.189
[research_cai_xie_2021]: https://doi.org/10.2514/6.2021-2448
[research_calculation_of_2008]: https://doi.org/10.5139/jksas.2008.36.11.1039
[research_calderon_aupoix_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.543
[research_calise]: https://doi.org/10.1109/wescon.1995.485489
[research_calise_2000]: https://doi.org/10.2514/6.2000-3940
[research_calise_lee_1998]: https://doi.org/10.2514/6.1998-4108
[research_calise_lee_2001]: https://doi.org/10.2514/2.4825
[research_callaghan_kunz_2019]: https://doi.org/10.2514/6.2019-3548
[research_callaghan_kunz_2021]: https://doi.org/10.2514/1.g004748
[research_cameron_cameron_1997]: https://doi.org/10.2514/6.1997-3788
[research_cameron_princen_2000]: https://doi.org/10.2514/6.2000-4539
[research_cameron_thomson_2003]: https://doi.org/10.1017/s0001924000134013
[research_campbell_1957]: https://ntrs.nasa.gov/citations/20040034247
[research_campbell_1958]: https://doi.org/10.2514/8.7491
[research_campbell_1959]: https://doi.org/10.1108/eb033068
[research_campbell_carter_2005]: https://ntrs.nasa.gov/citations/20050041753
[research_campos_1989]: https://doi.org/10.2514/6.1989-2041
[research_campos_fonseca_1995]: https://doi.org/10.1016/0376-0421(94)00005-6
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_candon_levinski_2019]: https://doi.org/10.2514/6.2019-0763
[research_cao_lin_2025]: https://doi.org/10.2139/ssrn.5375639
[research_cao_lyu_2024]: https://doi.org/10.3390/act13090369
[research_capello_ferrero_2019]: https://doi.org/10.2514/6.2019-4311
[research_capello_guglieri_2011]: https://doi.org/10.1007/978-94-007-3033-5_4
[research_capone_mason_1983]: https://doi.org/10.2514/6.1983-86
[research_capone_mason_1986]: https://doi.org/10.2514/6.1986-1779
[research_cardenas_boschetti_2009]: https://doi.org/10.2514/1.44306
[research_carlsen_1995]: https://doi.org/10.2514/3.46836
[research_carlsson_2003]: https://doi.org/10.2514/6.2003-450
[research_carlsson_2005]: https://doi.org/10.2514/1.5440
[research_carnduff_erbsloeh_2009]: https://doi.org/10.2514/1.36730
[research_carpenter_saric_2008]: https://doi.org/10.2514/6.2008-7335
[research_carpenter_solomon_2018]: https://doi.org/10.2514/6.2018-3809
[research_carrese_marzocca_2016]: https://doi.org/10.2514/6.2016-1552
[research_carter_campbell_2008]: https://doi.org/10.2514/6.2008-839
[research_cassaro_roos_2018]: https://doi.org/10.23919/ecc.2018.8550390
[research_castaldi_mimmo_2020]: https://doi.org/10.1049/pbce126e_ch9
[research_castellani_cooper_2016]: https://doi.org/10.2514/6.2016-1573
[research_cathey_1979]: https://doi.org/10.2514/6.1979-232
[research_caughey_1976]: https://doi.org/10.2514/3.58626
[research_caughey_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50009-7
[research_caughey_jameson_1977]: https://doi.org/10.2514/6.1977-677
[research_cavalcanti_2026]: https://doi.org/10.2514/1.c038528
[research_cavallaro_bombardieri_2019]: https://doi.org/10.2514/6.2019-1118
[research_cavanaugh_2003]: https://doi.org/10.2514/6.2003-5613
[research_celik_roberts_1992]: https://ntrs.nasa.gov/citations/19920039519
[research_cen_li_2020]: https://doi.org/10.1177/0954410020944085
[research_cenko_madson_1993]: https://doi.org/10.2514/6.1993-855
[research_chaderjian_1992]: https://doi.org/10.2514/6.1992-4428
[research_chaderjian_schiff_1993]: https://ntrs.nasa.gov/citations/19930063270
[research_chaixue_wangganglin_2010]: https://doi.org/10.1109/car.2010.5456588
[research_chakravarty_1987]: https://doi.org/10.2514/6.1987-2257
[research_chalk_1963]: https://doi.org/10.2514/6.1963-1001
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chalk_1983]: https://doi.org/10.2514/3.19820
[research_chalk_1986]: https://doi.org/10.2514/3.20144
[research_chalk_neal_1969]: https://doi.org/10.21236/ad0860856
[research_chalk_wilson_1968]: https://doi.org/10.2514/6.1968-245
[research_chalk_wilson_1969]: https://doi.org/10.2514/3.44041
[research_chaloner_verdinelli_1995]: https://doi.org/10.1214/ss/1177009939
[research_champine_kraft_1958]: https://ntrs.nasa.gov/citations/19660024788
[research_chan_chen_1976]: https://doi.org/10.21236/adb013236
[research_chan_hooker_2017]: https://doi.org/10.2514/6.2017-0098
[research_chandrasekharan_iarocci_2015]: https://doi.org/10.4271/2015-01-2566
[research_chang_cho_2004]: https://doi.org/10.2514/6.2004-1142
[research_chang_muirhead_1987]: https://doi.org/10.2514/3.45413
[research_chang_muirhead_1987_b]: https://ntrs.nasa.gov/citations/19870014987
[research_chang_ye_2009]: https://doi.org/10.2514/1.42408
[research_chao_flanagan_2017]: https://doi.org/10.2514/6.2017-1631
[research_chaparro_fujiwara_2016]: https://doi.org/10.2514/6.2016-3418
[research_chapter_12_1994]: https://doi.org/10.1515/9781400880034-015
[research_chapter_13_1994]: https://doi.org/10.1515/9781400880034-016
[research_chapter_6_2005]: https://doi.org/10.1515/9781400866816-007
[research_chapter_7_2005]: https://doi.org/10.1515/9781400866816-008
[research_chapter_8_2025]: https://doi.org/10.1137/1.9781611978438.ch8
[research_chaudhuri_jasa_2018]: https://doi.org/10.2514/6.2018-1658
[research_chaudhuri_nagaraja_1958]: https://doi.org/10.2514/8.7791
[research_chavatzopoulos_giotis_2012]: https://doi.org/10.1007/978-3-642-32909-8_27
[research_chavez_vogel_2003]: https://doi.org/10.1115/imece2003-42864
[research_chen_1982]: https://doi.org/10.2514/6.1982-162
[research_chen_2018]: https://doi.org/10.1063/1.5033619
[research_chen_boothe_1974]: https://doi.org/10.2514/6.1974-833
[research_chen_bui_1990]: https://doi.org/10.2514/6.1990-1586
[research_chen_gray_2026]: https://doi.org/10.2514/6.2026-1489
[research_chen_khalid_2001]: https://doi.org/10.2514/6.2001-2485
[research_chen_lee_2008]: https://doi.org/10.2514/1.29611
[research_chen_li_2024]: https://doi.org/10.3390/s24051597
[research_chen_lin_2021]: https://doi.org/10.1088/1742-6596/1846/1/012024
[research_chen_shi_2021]: https://doi.org/10.1063/5.0057280
[research_chen_sun_2019]: https://doi.org/10.1109/cac48633.2019.8996867
[research_chen_valasek_1999]: https://doi.org/10.2514/6.1999-4173
[research_chen_xie_2024]: https://doi.org/10.1088/1742-6596/2882/1/012003
[research_chen_zhang_2025]: https://doi.org/10.2139/ssrn.5626389
[research_chen_zhang_2025_b]: https://doi.org/10.1088/1742-6596/2955/1/012011
[research_chen_zhang_2026]: https://doi.org/10.2139/ssrn.7380660
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_cheng_1982]: https://doi.org/10.1016/b978-0-12-493280-7.50010-3
[research_cheng_2009]: https://doi.org/10.1017/s1727719100002938
[research_cheng_cea_2025]: https://doi.org/10.2514/6.2025-0714
[research_cheng_meng_1980]: https://doi.org/10.2514/6.1980-342
[research_chevalier_1982]: https://ntrs.nasa.gov/citations/19820008173
[research_chevalier_burke_1972]: https://doi.org/10.2514/6.1972-125
[research_chin_1992]: https://doi.org/10.2514/6.1992-2617
[research_chin_lentink_2019]: https://doi.org/10.1007/s00348-019-2838-7
[research_chipman_rauch_1984]: https://ntrs.nasa.gov/citations/19840013485
[research_chiu]: https://doi.org/10.15368/theses.2012.54
[research_chng_tsai_2008]: https://doi.org/10.2514/6.2008-6722
[research_choe_xargay_2010]: https://doi.org/10.2514/6.2010-7775
[research_choosakngaongam_rapeeujjin_2024]: https://doi.org/10.37934/cfdl.16.5.18
[research_chowdhury_keshmiri_2021]: https://doi.org/10.1109/icuas51884.2021.9476811
[research_chowhan_arya_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christisongray_martins_2026]: https://doi.org/10.2514/6.2026-1010
[research_christophersen_spahr_1944]: https://ntrs.nasa.gov/citations/19930092586
[research_chuan_feng_2016]: https://doi.org/10.2514/6.2016-0513
[research_chung_2007]: https://doi.org/10.2514/1.32203
[research_chung_2017]: https://doi.org/10.5139/ijass.2017.18.1.1
[research_chung_hallberg_2010]: https://doi.org/10.2514/6.2010-1035
[research_chung_lee_2002]: https://doi.org/10.2514/6.2002-2934
[research_chung_lee_2003]: https://doi.org/10.2514/2.3160
[research_chung_ma_2019]: https://doi.org/10.3390/app9153043
[research_chunshengliu_xinzhongzhu_2012]: https://doi.org/10.1109/acc.2012.6314694
[research_church_1954]: https://ntrs.nasa.gov/citations/19930087964
[research_chyczewski_2017]: https://doi.org/10.2514/1.j055463
[research_ciliberti_dellavecchia_2017]: https://doi.org/10.1016/j.paerosci.2017.11.001
[research_ciliberti_nicolosi_2026]: https://doi.org/10.2139/ssrn.6838882
[research_citurs_1984]: https://doi.org/10.21236/ada153173
[research_clark_gerhold_1999]: https://doi.org/10.2514/6.1999-1937
[research_clark_hodapp_1972]: https://doi.org/10.2514/6.1972-1032
[research_clarke_allen_2005]: https://ntrs.nasa.gov/citations/20050204120
[research_clarke_burken_2018]: https://doi.org/10.1201/9781315136820-13
[research_claudiaalice_2010]: https://doi.org/10.13111/2066-8201.2010.2.1.10
[research_cleary_gray_1947]: https://ntrs.nasa.gov/citations/20050019287
[research_clevenson_thompson_1957]: https://ntrs.nasa.gov/citations/19630006361
[research_coe_graham_1975]: https://ntrs.nasa.gov/citations/19750022117
[research_cole_1986]: https://doi.org/10.2514/6.1986-9
[research_cole_1988]: https://doi.org/10.2514/3.45609
[research_cole_1990]: https://doi.org/10.2514/6.1990-981
[research_cole_noll_2003]: https://doi.org/10.2514/2.6873
[research_coletti_faruque_2022]: https://doi.org/10.2514/6.2022-0556
[research_colgren_loschke_2008]: https://doi.org/10.2514/1.32083
[research_colgren_martin_2000]: https://doi.org/10.2514/6.2000-4448
[research_collar_1946]: https://doi.org/10.1017/s0368393100120358
[research_comments_with_1992]: https://doi.org/10.1109/37.120456
[research_complete_model]: https://doi.org/10.1007/bfb0043101
[research_conceptual_and_2017]: https://doi.org/10.2514/5.9781624104435.0231.0266
[research_conference_on_1966]: https://ntrs.nasa.gov/citations/19750065506
[research_configuration_development_2021]: https://doi.org/10.1017/9781139094672.012
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_cong_hu_2023_b]: https://doi.org/10.2139/ssrn.4677641
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_conrad_michalka_2025]: https://doi.org/10.1109/aero63441.2025.11068476
[research_consigny_gravelle_1983]: https://doi.org/10.2514/6.1983-1809
[research_contrerastorres_garciarodriguez_2022]: https://doi.org/10.1109/cce56709.2022.9975869
[research_control_allocation_2016]: https://doi.org/10.1002/9781118827789.ch8
[research_control_characteristics_2023]: https://doi.org/10.2514/5.9781624106170.0837.0858
[research_cook_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50015-0
[research_cook_1997_b]: https://doi.org/10.1016/b978-0-340-63200-0.50012-5
[research_cook_1997_c]: https://doi.org/10.1016/b978-0-340-63200-0.50018-6
[research_cook_1997_d]: https://doi.org/10.1016/b978-0-340-63200-0.50016-2
[research_cook_2007]: https://doi.org/10.1016/b978-075066927-6/50013-1
[research_cook_2007_b]: https://doi.org/10.1016/b978-075066927-6/50010-6
[research_cook_2007_c]: https://doi.org/10.1016/b978-075066927-6/50016-7
[research_cook_2007_d]: https://doi.org/10.1016/b978-075066927-6/50014-3
[research_cook_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00010-9
[research_cook_2013_b]: https://doi.org/10.1016/b978-0-08-098242-7.00007-9
[research_cook_2013_c]: https://doi.org/10.1016/b978-0-08-098242-7.00013-4
[research_cook_2013_d]: https://doi.org/10.1016/b978-0-08-098242-7.00011-0
[research_cook_decastro_2004]: https://doi.org/10.1017/s0001924000005029
[research_cooke_1980]: https://doi.org/10.2514/6.1980-1608
[research_cooney_schott_1956]: https://ntrs.nasa.gov/citations/19930084592
[research_cooper_klyde_2021]: https://doi.org/10.4050/f-0077-2021-16798
[research_coppolino_1952]: https://ntrs.nasa.gov/citations/19930087469
[research_cord_1981]: https://doi.org/10.2514/6.1981-1821
[research_cord_1994]: https://doi.org/10.2514/6.1994-3490
[research_corda_stephenson_1994]: https://ntrs.nasa.gov/citations/19950005778
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_corraro_morani_2011]: https://doi.org/10.5772/13961
[research_correia_silva_2009]: https://doi.org/10.2514/6.2009-746
[research_cosenza_kummeth_1974]: https://doi.org/10.2514/6.1974-620
[research_costa_koopman_1994]: https://ntrs.nasa.gov/citations/19950006282
[research_costes_1988]: https://doi.org/10.2514/6.1988-4160
[research_cotter_1946]: https://ntrs.nasa.gov/citations/19930081690
[research_cotting_2010]: https://doi.org/10.2514/6.2010-7944
[research_cotting_alt_2019]: https://doi.org/10.2514/6.2019-1082
[research_cotting_cao_2008]: https://doi.org/10.2514/6.2008-6551
[research_coupled_longitudinal_2015]: https://doi.org/10.2307/j.ctt1287kgx.10
[research_cousteix_pailhas_1983]: https://doi.org/10.1007/978-3-642-81991-9_21
[research_covell_1985]: https://ntrs.nasa.gov/citations/19850019510
[research_cox_jackson_1997]: https://ntrs.nasa.gov/citations/19970014738
[research_cox_jackson_1997_b]: https://ntrs.nasa.gov/citations/19970026105
[research_cox_marshall_2000]: https://ntrs.nasa.gov/citations/20000052206
[research_cox_siddall_1949]: https://doi.org/10.1108/eb031772
[research_crabill_1956]: https://ntrs.nasa.gov/citations/20050030066
[research_craig_1991]: https://ntrs.nasa.gov/citations/19920001772
[research_crandall_swanson_1944]: https://ntrs.nasa.gov/citations/19930092936
[research_crane_1948]: https://ntrs.nasa.gov/citations/20050028619
[research_crane_beckhardt_1948]: https://ntrs.nasa.gov/citations/20050031072
[research_crane_reeder_1945]: https://ntrs.nasa.gov/citations/20050028615
[research_crane_sommer_1961]: https://ntrs.nasa.gov/citations/19980227996
[research_crassidis_2005]: https://doi.org/10.2514/6.2005-5919
[research_craun_acosta_2013]: https://ntrs.nasa.gov/citations/20140008293
[research_craun_acosta_2013_b]: https://ntrs.nasa.gov/citations/20140008294
[research_creer_1959]: https://ntrs.nasa.gov/citations/19980228135
[research_crider_2004]: https://doi.org/10.2514/6.2004-6293
[research_crisalli_stahara_1979]: https://doi.org/10.21236/ada082005
[research_crombie_moorhouse_1980]: https://doi.org/10.21236/ada088629
[research_cromwell_koven_1965]: https://doi.org/10.2514/6.1965-794
[research_croom_huffman_1957]: https://ntrs.nasa.gov/citations/19930084891
[research_croom_whipple_1988]: https://ntrs.nasa.gov/citations/19890063988
[research_crother_gabelman_1973]: https://doi.org/10.21236/ada004416
[research_crouch_2019]: https://doi.org/10.1017/jfm.2019.748
[research_crouch_garbaruk_2008]: https://doi.org/10.2514/6.2008-4233
[research_crouch_garbaruk_2018]: https://doi.org/10.2514/6.2018-3229
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_cruz_ware_1995]: https://ntrs.nasa.gov/citations/19960013916
[research_cui_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000528
[research_cui_zhang_2026]: https://doi.org/10.1051/jnwpu/20264410151
[research_culler_farnsworth_2019]: https://doi.org/10.2514/6.2019-1394
[research_cunningham_1972]: https://doi.org/10.2514/3.59005
[research_cunningham_shah_2019]: https://doi.org/10.2514/6.2019-0717
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_currao_yeh_2026]: https://doi.org/10.2139/ssrn.6450319
[research_curry_curry_1997]: https://doi.org/10.2514/6.1997-3649
[research_curry_moulton_1989]: https://ntrs.nasa.gov/citations/19900004886
[research_curry_moulton_1990]: https://ntrs.nasa.gov/citations/19900019217
[research_curry_sim_1982]: https://doi.org/10.2514/6.1982-1329
[research_cusher_gopalarathnam_2006]: https://doi.org/10.2514/6.2006-3320
[research_cusher_gopalarathnam_2012]: https://doi.org/10.2514/1.c031454
[research_dabney_2012]: https://doi.org/10.1061/9780784412190.150
[research_daguanno_campspons_2022]: https://doi.org/10.2514/6.2022-1807
[research_daguanno_schrijer_2021]: https://doi.org/10.2514/6.2021-2558
[research_daguanno_schrijer_2022]: https://doi.org/10.2514/1.j061974
[research_dahiya_2017]: https://doi.org/10.26438/ijcse/v5i9.2126
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_daiutolo_1954]: https://ntrs.nasa.gov/citations/19930088291
[research_daiutolo_parker_1952]: https://ntrs.nasa.gov/citations/19930087340
[research_dallery_1987]: https://ntrs.nasa.gov/citations/19870009096
[research_damstrom_mayes_1970]: https://doi.org/10.2514/6.1970-341
[research_damstrom_mayes_1971]: https://doi.org/10.2514/3.44266
[research_damveld_2004]: https://doi.org/10.2514/6.2004-5365
[research_dander_1962]: https://doi.org/10.21236/ad0294920
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandwani_bragadoaldana_2025]: https://doi.org/10.2514/6.2025-3426
[research_danek_2002]: https://doi.org/10.1108/00022660210442263
[research_danforth_obryan_1951]: https://ntrs.nasa.gov/citations/20090012111
[research_dang_yang_2010]: https://doi.org/10.2514/6.2010-3051
[research_dang_zhao_2019]: https://doi.org/10.3390/app9194132
[research_danowsky_kotikalpudi_2018]: https://doi.org/10.2514/6.2018-3427
[research_danowsky_schmidt_2017]: https://doi.org/10.2514/6.2017-1394
[research_danowsky_thompson_2008]: https://doi.org/10.2514/6.2008-6370
[research_dantzig_1975]: https://doi.org/10.21236/ada016217
[research_davenport_leggett_1993]: https://ntrs.nasa.gov/citations/19940020624
[research_davey_gordon_2016]: https://doi.org/10.1007/978-981-10-0379-0_7
[research_davies_2020]: https://doi.org/10.1201/9780429261152-9
[research_davies_2025]: https://doi.org/10.1201/9781032692883-10
[research_davis_1952]: https://doi.org/10.2514/8.2275
[research_davis_1969]: https://doi.org/10.2514/6.1969-57
[research_davis_harris_1973]: https://doi.org/10.2514/3.44368
[research_dawson_maxwell_2003]: https://doi.org/10.2514/6.2003-1427
[research_dawson_maxwell_2005]: https://doi.org/10.2514/1.10693
[research_dean_morton_2008]: https://doi.org/10.2514/6.2008-6378
[research_dearaujo_singh_1997]: https://doi.org/10.2514/6.1997-3488
[research_deb_gangtao_2006]: https://doi.org/10.1109/acc.2006.1655376
[research_debecdelievre_kroo_2021]: https://doi.org/10.2514/6.2021-3063
[research_debusk_johnson_2009]: https://doi.org/10.2514/6.2009-5935
[research_decarvalhopereira_junior_2003]: https://doi.org/10.4271/2003-01-3587
[research_deck_2004]: https://doi.org/10.2514/6.2004-5378
[research_deck_2005]: https://doi.org/10.2514/1.9885
[research_decker_1951]: https://doi.org/10.2514/8.2130
[research_decker_1952]: https://doi.org/10.2514/8.2407
[research_dedivitiis_2005]: https://doi.org/10.2514/1.4830
[research_deepa_gupta_2023]: https://doi.org/10.61653/joast.v65i2.2013.727
[research_deepa_sudha_2016]: https://doi.org/10.1134/s0869864316020049
[research_deere_2003]: https://doi.org/10.2514/6.2003-3800
[research_definitions_of_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50019-8
[research_definitions_of_2007]: https://doi.org/10.1016/b978-075066927-6/50019-2
[research_definitions_of_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00025-0
[research_dehaan_1990]: https://doi.org/10.2514/6.1990-3062
[research_delajarte_1936]: https://ntrs.nasa.gov/citations/19930094623
[research_delany_1942]: https://ntrs.nasa.gov/citations/20090016408
[research_delaurier_2022]: https://doi.org/10.1201/9781315228167-4
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_demelo_bussamra_2024]: https://doi.org/10.21203/rs.3.rs-3761279/v1
[research_demourant_ferreres_2013]: https://doi.org/10.1051/eucass/201306729
[research_dempster_arnold_1969]: https://doi.org/10.2514/3.44062
[research_denegri_2000]: https://doi.org/10.2514/6.2000-1394
[research_deneke_carter_2026]: https://doi.org/10.2514/6.2026-0884
[research_deng_zhang_2023]: https://doi.org/10.3390/aerospace10060537
[research_denieul]: https://doi.org/10.70675/a7535743z7dc2z46afz82a7zf34af4291668
[research_denieul_alazard_2015]: https://doi.org/10.2514/6.2015-2553
[research_deodhare_vidyasagar]: https://doi.org/10.1109/cdc.1992.371670
[research_depadua_preisigheviana_2026]: https://doi.org/10.2514/6.2026-4237
[research_deppe_chalk_1996]: https://ntrs.nasa.gov/citations/19970004404
[research_desai_viswanathan_1977]: https://doi.org/10.2514/3.44585
[research_deshpande_zhang_2021]: https://doi.org/10.1142/s2737480721400069
[research_design_of_2012]: https://doi.org/10.1002/9781118352700.ch12
[research_deslich_flick_2021]: https://doi.org/10.2514/6.2021-0607
[research_deters_russell_1947]: https://ntrs.nasa.gov/citations/19930082045
[research_development_and_1980]: https://ntrs.nasa.gov/citations/19840024325
[research_development_of_2012]: https://doi.org/10.2514/5.9781600868207.0645.0718
[research_development_of_2014]: https://doi.org/10.2514/5.9781624102547.0661.0664
[research_development_of_2018]: https://doi.org/10.26666/rmp.jesr.2018.6.1
[research_development_of_2024]: https://doi.org/10.2514/5.9781624107252.0731.0734
[research_devesa_jourdan_2004]: https://doi.org/10.2514/1.3612
[research_devi_2019]: https://doi.org/10.21275/sr231208204149
[research_devries_vankampen_2019]: https://doi.org/10.2514/6.2019-0144
[research_dewart_jr_1958]: https://doi.org/10.21236/ad0155543
[research_deyoung_1979]: https://ntrs.nasa.gov/citations/19790015752
[research_dias_2022]: https://doi.org/10.2514/6.2022-3637
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dias_budisic_2023]: https://doi.org/10.31224/3001
[research_dicarlo_brown_1992]: https://doi.org/10.2514/6.1992-4094
[research_didomenico_biezad_1985]: https://doi.org/10.2514/6.1985-1788
[research_diederich_1954]: https://doi.org/10.2514/8.3153
[research_difabbio_tangermann_2022]: https://doi.org/10.2514/6.2022-1204
[research_difranco_1967]: https://doi.org/10.21236/ad0656784
[research_difranco_1969]: https://doi.org/10.2514/6.1969-768
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_dimaggio_hartfield_2023]: https://doi.org/10.2514/6.2023-0623
[research_dimopoulos_panagiotou_2019]: https://doi.org/10.1051/matecconf/201930402013
[research_dingeldein_1944]: https://ntrs.nasa.gov/citations/19930092859
[research_dipasquale_2024]: https://doi.org/10.2514/6.2024-2723
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_directional_control_2003]: https://doi.org/10.2514/5.9781600861840.0341.0358
[research_dixon_1972]: https://doi.org/10.2514/6.1972-781
[research_dodbele_plotkin_1985]: https://doi.org/10.2514/6.1985-1588
[research_dodd_pratt_1970]: https://doi.org/10.2514/6.1970-1512
[research_dodd_pratt_1971]: https://doi.org/10.2514/3.59147
[research_dogan_kaewchay_2007]: https://doi.org/10.2514/1.25440
[research_doggett_soistmann_1989]: https://doi.org/10.2514/6.1989-1325
[research_doggett_soistmann_1992]: https://doi.org/10.2514/3.46155
[research_doko_sasongko_2026]: https://doi.org/10.11648/j.ajae.20261201.11
[research_dollyhigh_1970]: https://doi.org/10.2514/6.1970-932
[research_doman_1995]: https://doi.org/10.21236/ada305053
[research_doman_oppenheimer_2002]: https://doi.org/10.2514/6.2002-4667
[research_donaldson_1986]: https://ntrs.nasa.gov/citations/19860016870
[research_donegan_1984]: https://doi.org/10.21236/ada143764
[research_dong_liu_2022]: https://doi.org/10.3390/drones6100295
[research_dong_low_ar_2022]: https://doi.org/10.1017/jfm.2022.451
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_shi_2020]: https://doi.org/10.1016/j.ast.2020.105766
[research_dong_zhou_2025]: https://doi.org/10.1016/j.ast.2025.110199
[research_dongmo_2011]: https://doi.org/10.2514/6.2011-6305
[research_donlan_1976]: https://ntrs.nasa.gov/citations/19770022138
[research_donlan_collected_1976]: https://ntrs.nasa.gov/citations/19770022115
[research_donlan_kemp_1976]: https://ntrs.nasa.gov/citations/19770022127
[research_dou_li_2025]: https://doi.org/10.1007/978-981-97-9774-5_3
[research_doubrava_waszniowski_2008]: https://doi.org/10.2514/6.2008-6527
[research_douglasaircraftcolongbeachca_1963]: https://doi.org/10.21236/ad0406168
[research_dowell_1996]: https://doi.org/10.21236/ada325524
[research_dowell_1999]: https://doi.org/10.21236/ada362982
[research_dowell_assael_2025]: https://doi.org/10.2514/1.j065403
[research_dracopoulos_oz_1992]: https://doi.org/10.2514/3.46156
[research_drake_1965]: https://doi.org/10.2514/6.1965-316
[research_drake_finch_1955]: https://ntrs.nasa.gov/citations/19930088854
[research_drake_mckay_1953]: https://ntrs.nasa.gov/citations/19930087560
[research_drake_mclaughlin_1948]: https://ntrs.nasa.gov/citations/19930085320
[research_draper_1943]: https://ntrs.nasa.gov/citations/19930092574
[research_drewiacki_josesilvestre_2020]: https://doi.org/10.2514/6.2020-0282
[research_drewiacki_silvestre_2016]: https://doi.org/10.2514/6.2016-3539
[research_drinkwater_1970]: https://ntrs.nasa.gov/citations/19700033494
[research_driscoll_1966]: https://doi.org/10.4271/660220
[research_driver_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_driver_spearman_1959]: https://ntrs.nasa.gov/citations/19630002676
[research_duffy_1989]: https://doi.org/10.2514/6.1989-3383
[research_dugan_1959]: https://ntrs.nasa.gov/citations/19980228238
[research_dugundji_ghareeb_1965]: https://doi.org/10.2514/6.1965-113
[research_duncan_1934]: https://doi.org/10.1017/s0368393100110156
[research_duncan_1950]: https://doi.org/10.1017/s0001925900000378
[research_duncan_crawford_2013]: https://doi.org/10.2514/6.2013-2412
[research_dunning_1957]: https://ntrs.nasa.gov/citations/19930089807
[research_duraffourg_burlion_2013]: https://doi.org/10.23919/ecc.2013.6669369
[research_duran_2026]: https://doi.org/10.2514/6.2026-2637
[research_durham_bordignon_2016]: https://doi.org/10.1002/9781118827789
[research_dvorak_choi_1982]: https://doi.org/10.21236/ada112146
[research_dvorak_choi_1983]: https://doi.org/10.2514/3.44872
[research_dynamic_lateral_directional_2003]: https://doi.org/10.2514/5.9781600861840.0311.0322
[research_dynamic_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0247.0254
[research_dynamic_longitudinal_2003_b]: https://doi.org/10.2514/5.9781600861840.0235.0246
[research_dynamics_of_2023]: https://doi.org/10.1017/9781108354868.010
[research_dynamics_of_2023_b]: https://doi.org/10.1017/9781108354868.006
[research_eastep_andersen_1998]: https://doi.org/10.2514/6.1998-4932
[research_eastep_andersen_2001]: https://doi.org/10.2514/2.2842
[research_eberhardt_ward_1999]: https://doi.org/10.2514/6.1999-4042
[research_edwards_1992]: https://doi.org/10.2514/6.1992-4002
[research_edwards_2008]: https://doi.org/10.2514/1.30082
[research_edwards_fittante_1997]: https://doi.org/10.21236/ada325252
[research_edwards_spain_2009]: https://doi.org/10.2514/1.30079
[research_effect_of_1978]: https://doi.org/10.2514/6.1978-832
[research_effect_of_1990]: https://doi.org/10.2514/6.1990-2838
[research_efremov_2020]: https://doi.org/10.2514/1.g004409
[research_efremov_shcherbakov_2022]: https://doi.org/10.34759/vst-2022-1-201-210
[research_eggleston_1956]: https://ntrs.nasa.gov/citations/19930084573
[research_ehlers_niedermeier_2011]: https://doi.org/10.2514/6.2011-6540
[research_ehlers_weisshaar_1993]: https://doi.org/10.2514/3.46376
[research_eichhorn_fritzsche_2022]: https://doi.org/10.2514/6.2022-1933
[research_eichler_1970]: https://doi.org/10.2514/3.44170
[research_ekaterinaris_1995]: https://doi.org/10.2514/6.1995-781
[research_eldredge_wang_2009]: https://doi.org/10.2514/6.2009-3687
[research_eldridgeallegra_roseman_2024]: https://doi.org/10.2514/6.2024-1945
[research_elenin_2021]: https://doi.org/10.31799/2077-5687-2021-2-26-32
[research_elevon_transonic_1977]: https://ntrs.nasa.gov/citations/19770013202
[research_elkhoury_2008]: https://doi.org/10.2514/1.32609
[research_elkhoury_2016]: https://doi.org/10.2514/1.c033576
[research_elmobaraky_kouiss_2025]: https://doi.org/10.1007/978-3-031-78922-9_16
[research_elramly]: https://doi.org/10.22215/etd/1975-00290
[research_elsayed_scarano_2007]: https://doi.org/10.2514/6.2007-4451
[research_elzebda_mook_1987]: https://doi.org/10.2514/6.1987-496
[research_elzebda_mook_1989]: https://doi.org/10.2514/3.45795
[research_elzebda_nayfeh_1989]: https://doi.org/10.2514/3.45833
[research_ema_mizukura_1997]: https://doi.org/10.5100/jje.33.supplement_136
[research_emerson_robinson_1958]: https://ntrs.nasa.gov/citations/19980228314
[research_eney_1967]: https://doi.org/10.2514/6.1967-576
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_eney_1969]: https://doi.org/10.2514/6.1969-896
[research_engelbrecht]: https://doi.org/10.31274/rtd-180813-14663
[research_englar_1970]: https://doi.org/10.21236/ad0882075
[research_englar_1996]: https://ntrs.nasa.gov/citations/19960023623
[research_english_1953]: https://ntrs.nasa.gov/citations/19930081603
[research_english_1954]: https://ntrs.nasa.gov/citations/19930088372
[research_english_1955]: https://ntrs.nasa.gov/citations/19930088587
[research_english_1955_b]: https://ntrs.nasa.gov/citations/19930088612
[research_english_1957]: https://ntrs.nasa.gov/citations/19930089655
[research_enns_1990]: https://doi.org/10.2514/6.1990-3338
[research_enns_2003]: https://doi.org/10.21236/ada411755
[research_enns_2015]: https://doi.org/10.1007/978-1-4471-5058-9_20
[research_eppink_2023]: https://doi.org/10.2514/6.2023-3999
[research_epstein_luntz_1989]: https://doi.org/10.2514/3.45835
[research_erel_seter_1989]: https://doi.org/10.2514/3.45754
[research_erickson_1987]: https://doi.org/10.2514/3.56784
[research_erickson_schreiner_1989]: https://doi.org/10.2514/6.1989-3345
[research_ericsson_1980]: https://doi.org/10.2514/6.1980-1801
[research_ericsson_1983]: https://doi.org/10.2514/6.1983-1810
[research_ericsson_1984]: https://doi.org/10.2514/3.44967
[research_ericsson_1986]: https://doi.org/10.2514/6.1986-1773
[research_ericsson_1987]: https://doi.org/10.2514/6.1987-2496
[research_ericsson_1987_b]: https://doi.org/10.2514/6.1987-268
[research_ericsson_1988]: https://doi.org/10.2514/6.1988-4370
[research_ericsson_1988_b]: https://doi.org/10.2514/6.1988-2597
[research_ericsson_1989]: https://doi.org/10.2514/3.45720
[research_ericsson_1991]: https://doi.org/10.2514/6.1991-417
[research_ericsson_1993]: https://doi.org/10.2514/3.46341
[research_ericsson_1995]: https://doi.org/10.2514/6.1995-317
[research_ericsson_1996]: https://doi.org/10.2514/3.46998
[research_ericsson_1996_b]: https://doi.org/10.2514/6.1996-788
[research_ericsson_1996_c]: https://doi.org/10.2514/6.1996-3404
[research_ericsson_1997]: https://doi.org/10.2514/2.2165
[research_ericsson_1997_b]: https://doi.org/10.2514/2.2233
[research_ericsson_1997_c]: https://doi.org/10.2514/2.2192
[research_ericsson_1998]: https://doi.org/10.2514/2.2399
[research_ericsson_1998_b]: https://doi.org/10.2514/6.1998-498
[research_ericsson_1999]: https://doi.org/10.2514/6.1999-141
[research_ericsson_2000]: https://doi.org/10.2514/6.2000-137
[research_ericsson_2000_b]: https://doi.org/10.2514/2.2692
[research_ericsson_2002]: https://doi.org/10.2514/6.2002-712
[research_ericsson_beyers_2002]: https://doi.org/10.2514/6.2002-94
[research_ericsson_ericsson_1997]: https://doi.org/10.2514/6.1997-3645
[research_ericsson_hanff_1993]: https://doi.org/10.2514/6.1993-620
[research_ericsson_king_1990]: https://doi.org/10.2514/6.1990-301
[research_ericsson_king_1990_b]: https://doi.org/10.2514/6.1990-3037
[research_ericsson_mendenhall_1994]: https://doi.org/10.2514/6.1994-167
[research_ericsson_reding_1977]: https://doi.org/10.2514/6.1977-667
[research_ericsson_reding_1985]: https://doi.org/10.2514/3.45093
[research_erturk_dogan_2015]: https://doi.org/10.2514/6.2015-0020
[research_erturk_ozkan_2022]: https://doi.org/10.2514/6.2022-3647
[research_esfandabadi_djavareshkian_2026]: https://doi.org/10.1155/ijae/8522389
[research_eshelby_1982]: https://doi.org/10.2514/3.44765
[research_esposito_orlando_2020]: https://doi.org/10.1063/5.0026477
[research_esteban_2001]: https://doi.org/10.2514/6.2001-4010
[research_esteban_gavilan_2015]: https://doi.org/10.1016/j.ifacol.2015.08.070
[research_estevadeordal_ullah_2022]: https://doi.org/10.2514/6.2022-1959
[research_estimation_and_2026]: https://doi.org/10.1017/9781009399913.017
[research_etkin_1952]: https://doi.org/10.2514/8.2267
[research_eugeni_mastroddi_2020]: https://doi.org/10.1007/978-3-030-34713-0_42
[research_eulrich_govindaraj_1978]: https://doi.org/10.2514/6.1978-1326
[research_eulrich_mesiah_1974]: https://doi.org/10.21236/ada021994
[research_eulrich_rynaski_1980]: https://doi.org/10.2514/6.1980-1633
[research_evangelou_1998]: https://doi.org/10.1049/cp:19980616
[research_experience_gained_2010]: https://doi.org/10.2514/5.9781600867552.0443.0543
[research_experimental_investigation_2023]: https://doi.org/10.1063/5.0147213
[research_extension_of_1982]: https://doi.org/10.2514/5.9781600865558.0467.0487
[research_faber_1958]: https://ntrs.nasa.gov/citations/19930085061
[research_fairbanks_1927]: https://ntrs.nasa.gov/citations/19930091321
[research_fairuzizzuddinromli_muhammadaimanmohammadsabri_2023]: https://doi.org/10.37934/cfdl.15.3.1221
[research_falkner_1951]: https://doi.org/10.1108/eb031999
[research_fan_zhu_2006]: https://doi.org/10.1109/isda.2006.162
[research_farhangnia_guruswamy_1996]: https://doi.org/10.2514/6.1996-286
[research_farhat_1998]: https://doi.org/10.21236/ada361695
[research_farhat_2000]: https://doi.org/10.21236/ada389378
[research_farhat_2001]: https://doi.org/10.21236/ada387498
[research_fasiello_lu_2019]: https://doi.org/10.2514/6.2019-1230
[research_favaregh_landman_2006]: https://doi.org/10.2514/6.2006-6145
[research_favier_agnes_1988]: https://doi.org/10.2514/3.45663
[research_favre_2018]: https://doi.org/10.1201/9781315136820-8
[research_fears_ross_1995]: https://ntrs.nasa.gov/citations/19950023805
[research_fechter_mills_1988]: https://doi.org/10.2514/6.1988-2174
[research_feedback_flight_2026]: https://doi.org/10.1017/9781009399913.013
[research_feedback_stability_2023]: https://doi.org/10.2514/5.9781624106170.0671.0728
[research_feel_system_1961]: https://ntrs.nasa.gov/citations/20040027953
[research_ferman_turner_1999]: https://doi.org/10.21236/ada416808
[research_ferman_turner_1999_b]: https://doi.org/10.21236/ada377712
[research_fernand_downing_1994]: https://doi.org/10.2514/6.1994-3543
[research_fernandes_maldonado_2024]: https://doi.org/10.20944/preprints202405.0053.v1
[research_field_armor_2002]: https://doi.org/10.2514/6.2002-4800
[research_field_rossitto_2004]: https://doi.org/10.2514/1.3315
[research_fields_1952]: https://ntrs.nasa.gov/citations/19930087247
[research_figat_kwiek_2021]: https://doi.org/10.1108/aeat-05-2020-0085
[research_filzek_1949]: https://ntrs.nasa.gov/citations/20050029422
[research_finch_matranga_1959]: https://ntrs.nasa.gov/citations/19980236840
[research_findlay_findlay_1997]: https://doi.org/10.2514/6.1997-621
[research_fink_lastinger_1961]: https://ntrs.nasa.gov/citations/19980231058
[research_finn_1944]: https://ntrs.nasa.gov/citations/19930092461
[research_firsov_isaenkov_2017]: https://doi.org/10.2514/6.2017-0714
[research_fischel_holleman_1957]: https://ntrs.nasa.gov/citations/19930090141
[research_fischel_nugent_1953]: https://ntrs.nasa.gov/citations/19930087532
[research_fisher_1954]: https://ntrs.nasa.gov/citations/19930083900
[research_fisher_stough_1976]: https://doi.org/10.4271/760461
[research_fisher_williams_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_flanagan_chao_2019]: https://doi.org/10.1109/icuas.2019.8798212
[research_fletcher_1994]: https://doi.org/10.2514/6.1994-2146
[research_flight_control_1999]: https://doi.org/10.1108/aeat.1999.12771aad.001
[research_flight_control_2015]: https://doi.org/10.1201/b19350-7
[research_flight_control_2015_b]: https://doi.org/10.1002/9781119141174.ch9
[research_flight_control_of_2000]: https://doi.org/10.18372/2306-1472.7.11270
[research_flight_dynamics_2014]: https://doi.org/10.1201/b17346-14
[research_flight_simulation_2016]: https://doi.org/10.1002/9781118827789.app2
[research_flight_test_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50001-6
[research_flight_test_1970]: https://ntrs.nasa.gov/citations/19710000627
[research_flight_test_1977]: https://doi.org/10.2514/6.1977-1217
[research_florio_mckibbin_2019]: https://doi.org/10.21914/anziamj.v59i0.13408
[research_flow_control_2016]: https://doi.org/10.21152/1750-9548.10.2.117
[research_flow_field_2023]: https://doi.org/10.47176/jafm.16.04.1475
[research_fluid_dynamics_1998]: https://ntrs.nasa.gov/citations/19990018232
[research_flying_qualities_1998]: https://doi.org/10.1108/aeat.1998.12770eae.001
[research_flying_qualities_2003]: https://doi.org/10.2514/5.9781600861840.0359.0363
[research_flying_qualities_2010]: https://doi.org/10.2514/5.9781600867644.0251.0268
[research_foa_1942]: https://doi.org/10.2514/8.10959
[research_foch_1992]: https://doi.org/10.2514/6.1992-4078
[research_fonterose_hall_1996]: https://doi.org/10.2514/3.21752
[research_forster_biava_2016]: https://doi.org/10.2514/6.2016-3773
[research_forster_steijl_2015]: https://doi.org/10.2514/6.2015-1709
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_foster_1959]: https://ntrs.nasa.gov/citations/19630002675
[research_foster_ross_1993]: https://doi.org/10.2514/6.1993-3647
[research_foughner_bensinger_1977]: https://ntrs.nasa.gov/citations/19780034892
[research_fournis_2022]: https://doi.org/10.2514/6.2022-3886
[research_fox_donegan_1991]: https://doi.org/10.2514/3.46039
[research_franklin_1970]: https://doi.org/10.2514/6.1970-998
[research_franklin_1971]: https://doi.org/10.2514/6.1971-905
[research_franklin_1971_b]: https://doi.org/10.2514/3.44303
[research_franklin_1972]: https://doi.org/10.2514/3.58970
[research_franklin_miller_1967]: https://doi.org/10.2514/6.1967-577
[research_franze_mattei_2013]: https://doi.org/10.1109/cdc.2013.6760903
[research_franzmann_leopold_2021]: https://doi.org/10.2514/6.2021-0836
[research_franzmann_leopold_2022]: https://doi.org/10.12783/ballistics22/36122
[research_franzmann_leopold_2022_b]: https://doi.org/10.3390/aerospace9020051
[research_fraser_1986]: https://doi.org/10.2514/3.56420
[research_frazier_1991]: https://doi.org/10.2514/6.1991-3173
[research_freeflight_longitudinal_1957]: https://ntrs.nasa.gov/citations/19930092326
[research_fremaux_vairo_1995]: https://doi.org/10.2514/3.46730
[research_freuler_hoffmann_1977]: https://doi.org/10.2514/6.1977-1216
[research_friehmelt_1996]: https://doi.org/10.2514/6.1996-3412
[research_friend_sakamoto_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_friend_sefic_1972]: https://ntrs.nasa.gov/citations/19720022354
[research_from_tube_2013]: https://doi.org/10.1002/9781118568101.ch5
[research_fu_kirtikar_2009]: https://doi.org/10.2514/6.2009-5758
[research_fu_yu_2021]: https://doi.org/10.1109/icuas51884.2021.9476716
[research_fujii_obayashi_1986]: https://doi.org/10.2514/6.1986-1831
[research_fujino_suzuki_2024]: https://doi.org/10.2514/6.2024-4390
[research_fukuda_takimoto_2014]: https://doi.org/10.1109/iccas.2014.6987817
[research_fukumoto_kouchi_2023]: https://doi.org/10.2514/6.2023-1180
[research_fukushima_kawai_2019]: https://doi.org/10.2514/6.2019-1846
[research_fuller_moorhouse_1982]: https://doi.org/10.2514/6.1982-1354
[research_fundamentals_of_2007]: https://doi.org/10.1007/978-3-540-46573-7
[research_fung_1982]: https://doi.org/10.21236/ada215096
[research_funk_rhyne_1956]: https://ntrs.nasa.gov/citations/19930084537
[research_furey_1980]: https://doi.org/10.21236/ada112312
[research_furlong_1948]: https://ntrs.nasa.gov/citations/19930085460
[research_furlong_bollech_1951]: https://ntrs.nasa.gov/citations/19930083050
[research_furlong_bollech_1955]: https://ntrs.nasa.gov/citations/19930092228
[research_fuselage_tail_yawing_1951]: https://ntrs.nasa.gov/citations/19930083055
[research_fuzzy_logic_1991]: https://doi.org/10.1109/37.88591
[research_g_the_1957]: https://doi.org/10.1515/9781400879908-016
[research_gainer_2002]: https://ntrs.nasa.gov/citations/20030009800
[research_gallman_batina_1988]: https://doi.org/10.2514/3.45587
[research_galor_1992]: https://doi.org/10.2514/3.46214
[research_galor_1994]: https://doi.org/10.1515/tjj.1994.11.2-3.119
[research_galor_2001]: https://doi.org/10.1515/tjj.2001.18.1.41
[research_galor_2003]: https://doi.org/10.1515/tjj.2003.20.4.297
[research_gamble_inman_2016]: https://doi.org/10.4028/www.scientific.net/ast.101.127
[research_gamble_inman_2018]: https://doi.org/10.1117/12.2287471
[research_gandhi_cooper_2009]: https://doi.org/10.2514/6.2009-5890
[research_ganesh_keerthi_2021]: https://doi.org/10.1007/978-981-15-9601-8_40
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00008-5
[research_gao_an_2021_b]: https://doi.org/10.1016/b978-0-12-822990-3.00002-4
[research_gao_an_2021_c]: https://doi.org/10.1016/b978-0-12-822990-3.00005-x
[research_gao_an_2021_d]: https://doi.org/10.1016/b978-0-12-822990-3.00004-8
[research_gao_an_2021_e]: https://doi.org/10.1016/b978-0-12-822990-3.00007-3
[research_gao_cai_2016]: https://doi.org/10.1016/j.cja.2016.06.014
[research_gao_liu_2021]: https://doi.org/10.1177/1077546320986715
[research_gao_smith_2020]: https://doi.org/10.2514/6.2020-1955
[research_gao_tyrrell_2025]: https://doi.org/10.2514/6.2025-2022
[research_gao_zhang_2018]: https://doi.org/10.1016/j.ast.2018.03.047
[research_gao_zhang_2019]: https://doi.org/10.1063/1.5087014
[research_garbaruk_strelets_2021]: https://doi.org/10.2514/1.j060707
[research_garbell_1946]: https://doi.org/10.2514/8.11442
[research_garcia_slingerland_2001]: https://doi.org/10.2514/6.2001-5237
[research_garciabaquero_esteban_2018]: https://doi.org/10.1016/j.ifacol.2018.07.099
[research_gardner_1951]: https://ntrs.nasa.gov/citations/20050029468
[research_gardner_curfman_1947]: https://ntrs.nasa.gov/citations/19930085706
[research_garkushenko_vinogradov_2016]: https://doi.org/10.3103/s1068799816040085
[research_garman_andrisani_2003]: https://doi.org/10.2514/6.2003-5618
[research_garmann_visbal_2020]: https://doi.org/10.2514/6.2020-1759
[research_garmann_visbal_2021]: https://doi.org/10.2514/6.2021-1450
[research_garmann_visbal_2022]: https://doi.org/10.2514/1.j061332
[research_garmann_visbal_2022_b]: https://doi.org/10.2514/1.j062010
[research_garmann_visbal_2023]: https://doi.org/10.2514/6.2023-0861
[research_garmendia_mavris_2014]: https://doi.org/10.2514/6.2014-2058
[research_garmendia_mavris_2015]: https://doi.org/10.2514/6.2015-0754
[research_garmendia_mavris_2016]: https://doi.org/10.2514/1.c033184
[research_garrec_kubica_2005]: https://doi.org/10.2514/1.3733
[research_garren_kelley_1970]: https://ntrs.nasa.gov/citations/19710003947
[research_garrick_reed_1981]: https://doi.org/10.2514/3.57579
[research_garris_1943]: https://ntrs.nasa.gov/citations/19930092575
[research_gatley_turner_2006]: https://doi.org/10.1016/j.ast.2005.07.004
[research_gatto_2009]: https://doi.org/10.2514/1.38916
[research_gatto_lowenberg_2006]: https://doi.org/10.2514/1.19821
[research_gautrey_cook_1998]: https://doi.org/10.1017/s000192400006543x
[research_gavilan_vazquez_2015]: https://doi.org/10.2514/1.g000028
[research_gaylor_1984]: https://doi.org/10.2514/6.1984-2489
[research_gebhardt_2017]: https://doi.org/10.2514/6.2017-3244
[research_gee_1978]: https://ntrs.nasa.gov/citations/19780010099
[research_generalelectriccoschenectadyny_1952]: https://doi.org/10.21236/ad0000287
[research_generally_on]: https://doi.org/10.1007/bfb0043100
[research_geoghegan_giannelis_2020]: https://doi.org/10.2514/6.2020-1989
[research_gera_1986]: https://doi.org/10.2514/6.1986-167
[research_gera_wilson_1981]: https://doi.org/10.2514/6.1981-2505
[research_german_development_2010]: https://doi.org/10.2514/4.867552
[research_gerontakos_lee_2005]: https://doi.org/10.1007/s00348-005-0056-y
[research_gerren_1995]: https://ntrs.nasa.gov/citations/19960003535
[research_gertsen_shomber_1965]: https://doi.org/10.2514/6.1965-780
[research_getsov_2018]: https://doi.org/10.46687/jsar.v13i1.232
[research_ghaffari_biedron_2002]: https://ntrs.nasa.gov/citations/20020022843
[research_ghaffari_biedron_2002_b]: https://ntrs.nasa.gov/citations/20020078006
[research_ghalandari_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghasemi_mosahebi_2014]: https://doi.org/10.2514/6.2014-0557
[research_ghee_gonzalez_1999]: https://doi.org/10.21236/ada368657
[research_giannelis_murray_2019]: https://doi.org/10.2514/6.2019-1339
[research_gibbings_1966]: https://doi.org/10.2514/3.43754
[research_gibson_1990]: https://doi.org/10.2514/6.1990-2844
[research_gibson_herr_1958]: https://ntrs.nasa.gov/citations/19660030332
[research_gibson_igoe_1957]: https://ntrs.nasa.gov/citations/19930089755
[research_gilbert_schmidt_1982]: https://doi.org/10.2514/6.1982-1544
[research_gilbreath_markofski_2001]: https://doi.org/10.2514/6.2001-4007
[research_giles_1970]: https://doi.org/10.2514/6.1970-569
[research_giles_1972]: https://doi.org/10.2514/3.58942
[research_gillan_1993]: https://doi.org/10.2514/6.1993-3419
[research_gillard_1998]: https://doi.org/10.21236/ada362903
[research_gillard_dorsett_1997]: https://doi.org/10.2514/6.1997-3487
[research_gillette_page_1993]: https://doi.org/10.2514/6.1993-1191
[research_gillis_1957]: https://ntrs.nasa.gov/citations/19930089776
[research_gillis_chapman_1956]: https://ntrs.nasa.gov/citations/20050019449
[research_gilmore_wakayama_2002]: https://doi.org/10.2514/6.2002-5666
[research_gilyard_1972]: https://ntrs.nasa.gov/citations/19720015377
[research_gilyard_1973]: https://ntrs.nasa.gov/citations/19730007283
[research_gilyard_berry_1972]: https://doi.org/10.2514/6.1972-961
[research_gimmestad_1980]: https://doi.org/10.2514/3.44673
[research_giordanodeoliveirasilva_moennich_2012]: https://doi.org/10.2514/6.2012-4412
[research_glauert_1928]: https://doi.org/10.1098/rspa.1928.0039
[research_gloss_washburn_1977]: https://doi.org/10.2514/6.1977-1132
[research_goc_agrawal_2023]: https://doi.org/10.2514/6.2023-4338
[research_godavarthi_seo_2026]: https://doi.org/10.2514/6.2026-2313
[research_goetzendorfgrabowski_antoniewski_2016]: https://doi.org/10.1108/aeat-02-2015-0055
[research_goland_1952]: https://doi.org/10.21236/ad0004240
[research_goman_khrabrov_1992]: https://doi.org/10.2514/6.1992-4498
[research_gomec_unver_2020]: https://doi.org/10.2514/6.2020-0278
[research_gong_gao_2024]: https://doi.org/10.3390/aerospace11020121
[research_gonzalez_bazile_2011]: https://doi.org/10.4271/2011-01-2762
[research_gonzalez_boschetti_2010]: https://doi.org/10.2514/6.2010-8230
[research_gonzalez_winkelmann_1993]: https://doi.org/10.2514/6.1993-3496
[research_goodman_1949]: https://ntrs.nasa.gov/citations/20050030041
[research_goodson_king_1949]: https://ntrs.nasa.gov/citations/19930085843
[research_goorjian_guruswamy_1985]: https://ntrs.nasa.gov/citations/19850016892
[research_gopalarathnam_selig_1997]: https://doi.org/10.2514/6.1997-2232
[research_gopinath_1982]: https://doi.org/10.2514/3.44818
[research_gordnier_1991]: https://doi.org/10.21236/ada244320
[research_gordnier_melville_2000]: https://doi.org/10.2514/2.2683
[research_goslin_ho_1989]: https://ntrs.nasa.gov/citations/19900000800
[research_gosmann_gabrys_2020]: https://doi.org/10.23919/acc45564.2020.9147800
[research_goud_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1057
[research_goushcha_sekula_2025]: https://doi.org/10.2514/6.2025-1124
[research_govindarajan_narasimha_2000]: https://doi.org/10.1007/978-3-662-03997-7_27
[research_graffstein_maslowski_2019]: https://doi.org/10.1108/aeat-01-2018-0017
[research_graham_mccaskill_1950]: https://doi.org/10.2514/8.1786
[research_granasy_1995]: https://doi.org/10.2514/6.1995-3923
[research_grantham_nguyen_1976]: https://ntrs.nasa.gov/citations/19770011064
[research_grantham_williams_1987]: https://ntrs.nasa.gov/citations/19870062309
[research_grantz_1984]: https://ntrs.nasa.gov/citations/19850003701
[research_gratton_2007]: https://doi.org/10.1017/s0001924000004632
[research_gratton_2014]: https://doi.org/10.1007/978-3-319-11409-5_13
[research_gratton_2018]: https://doi.org/10.1007/978-3-319-75617-2_11
[research_gratton_2018_b]: https://doi.org/10.1007/978-3-319-75617-2_13
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_graves_1999]: https://ntrs.nasa.gov/citations/19990081122
[research_gray_2009]: https://doi.org/10.2514/6.2009-6317
[research_gray_kemper_2009]: https://doi.org/10.2514/6.2009-1746
[research_green_1988]: https://doi.org/10.2514/6.1988-4142
[research_green_2008]: https://doi.org/10.2514/1.34571
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_green_mineck_1991]: https://doi.org/10.2514/3.46095
[research_green_ott_2003]: https://doi.org/10.2514/6.2003-925
[research_greenberg_sternfield_1944]: https://ntrs.nasa.gov/citations/19960024284
[research_greene_kunz_2014]: https://doi.org/10.2514/6.2014-2194
[research_greer_sardahi_2021]: https://doi.org/10.23919/acc50511.2021.9483198
[research_gregory_cao_2007]: https://doi.org/10.2514/6.2007-6525
[research_gregory_gadient_2011]: https://ntrs.nasa.gov/citations/20110014624
[research_gresham_wang_2009_b]: https://doi.org/10.2514/6.2009-543
[research_griffin_jonas_1983]: https://doi.org/10.2514/6.1983-1835
[research_grismer_jenkins_1996]: https://doi.org/10.2514/6.1996-2432
[research_grismer_kinsey_2000]: https://doi.org/10.2514/6.2000-4325
[research_grismer_myatt_1997]: https://doi.org/10.2514/6.1997-3644
[research_gross_2002]: https://doi.org/10.2514/6.2002-310
[research_gross_chandler_1986]: https://doi.org/10.23919/acc.1986.4789163
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_grossman_volpe_1977]: https://doi.org/10.21236/ada043460
[research_ground_testing_2007]: https://doi.org/10.1108/aeat.2007.12779bab.029
[research_gu_natesan_2008]: https://doi.org/10.1243/09596518jsce485
[research_guglieri_2012]: https://doi.org/10.1007/s11071-012-0369-3
[research_guglieri_quagliotti_1993]: https://doi.org/10.2514/3.46357
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_guiler_huebsch_2005]: https://doi.org/10.4271/2005-01-3391
[research_guiler_huebsch_2005_b]: https://doi.org/10.2514/6.2005-4981
[research_guillaume_gehri_2011]: https://doi.org/10.1017/s0001924000005777
[research_gulsacan_sencan_2018]: https://doi.org/10.2514/1.j057083
[research_gumusboga_iftar_2019]: https://doi.org/10.1109/codit.2019.8820480
[research_gumusboga_iftar_2020]: https://doi.org/10.14736/kyb-2020-4-0767
[research_gunes_sel_2025]: https://doi.org/10.3390/electronics14173555
[research_gunes_sel_2025_b]: https://doi.org/10.1109/intcec65580.2025.11255759
[research_gunnarsson_1997]: https://doi.org/10.1007/bfb0113874
[research_guo_burley_2014]: https://doi.org/10.2514/6.2014-0365
[research_guo_ren_2015]: https://doi.org/10.2514/6.2015-2559
[research_guo_split_rudder_2026]: https://doi.org/10.1016/j.ast.2026.112086
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_gupta_seiler_2016]: https://doi.org/10.2514/6.2016-1753
[research_guruswamy_1991]: https://doi.org/10.2514/6.1991-1013
[research_guruswamy_goorjian_1983]: https://doi.org/10.2514/6.1983-888
[research_guruswamy_goorjian_1985]: https://doi.org/10.2514/3.45107
[research_guruswamy_goorjian_1986]: https://ntrs.nasa.gov/citations/19860060148
[research_guruswamy_tu_1989]: https://doi.org/10.2514/3.45820
[research_guruswamy_tu_1994]: https://doi.org/10.2514/6.1994-1725
[research_guy_hadaway_1955]: https://ntrs.nasa.gov/citations/19930093831
[research_ha_1990]: https://doi.org/10.2514/6.1990-3226
[research_haas_chopra_1988]: https://doi.org/10.2514/3.45684
[research_haas_chopra_1990]: https://doi.org/10.2514/3.45937
[research_habboush_yildiz_2022]: https://doi.org/10.1109/lcsys.2021.3136460
[research_habel_steinberg_1953]: https://ntrs.nasa.gov/citations/19930087362
[research_hagerman_hofstetter_1969]: https://doi.org/10.2514/6.1969-794
[research_hahne_1985]: https://ntrs.nasa.gov/citations/19860010873
[research_haiping_yanjun_2021]: https://doi.org/10.23919/ccc52363.2021.9550109
[research_hall_1971]: https://doi.org/10.2514/3.59106
[research_hall_1992]: https://doi.org/10.2514/6.1992-4261
[research_hall_lawrence_2006]: https://doi.org/10.2514/6.2006-6689
[research_hall_sholar_1972]: https://doi.org/10.2514/6.1972-379
[research_hall_weingarten_1973]: https://doi.org/10.2514/6.1973-783
[research_hall_woodson_2003]: https://ntrs.nasa.gov/citations/20030015485
[research_hallissy_1956]: https://ntrs.nasa.gov/citations/19930089116
[research_hamel_jategaonkar_1996]: https://doi.org/10.2514/3.46898
[research_hamidani_kunz_2018]: https://doi.org/10.2514/6.2018-1019
[research_hammer_garmann_2021]: https://doi.org/10.2514/6.2021-2948
[research_hammer_garmann_2023]: https://doi.org/10.2514/6.2023-1979
[research_hammer_garmann_2023_b]: https://doi.org/10.2514/1.j063039
[research_hammett_reigelsperger]: https://doi.org/10.1109/acc.1995.529230
[research_hammond_downing_1984]: https://ntrs.nasa.gov/citations/19840060699
[research_hamza_samir_2020]: https://doi.org/10.35840/2631-5106/4123
[research_han_cho_2005]: https://doi.org/10.2514/1.6477
[research_han_liu_2023]: https://doi.org/10.1088/1742-6596/2472/1/012051
[research_han_liu_2026]: https://doi.org/10.4271/2026-99-1613
[research_han_zhang_2025]: https://doi.org/10.3390/drones9080585
[research_hancock_1972]: https://doi.org/10.1017/s0001924000044055
[research_handling_qualities_2000]: https://doi.org/10.2514/5.9781600866555.0119.0169
[research_handling_qualities_2008]: https://doi.org/10.1201/b15919-14
[research_handling_qualities_2017]: https://doi.org/10.4324/9781315255217-11
[research_hanin_barsonynagy_1983]: https://doi.org/10.2514/3.8147
[research_hanke_2003]: https://doi.org/10.2514/6.2003-5317
[research_hansen_duan_2022]: https://doi.org/10.2514/1.g006577
[research_hansmann_stumpf_2025]: https://doi.org/10.21203/rs.3.rs-7011252/v1
[research_hansmann_stumpf_2026]: https://doi.org/10.1007/s13272-026-00979-7
[research_hanson_schaefer_2011]: https://ntrs.nasa.gov/citations/20110023802
[research_hao_ma_2023]: https://doi.org/10.3390/aerospace10060511
[research_haoyunfu_jinyan_2009]: https://doi.org/10.1109/acc.2009.5160161
[research_hardwick_panella_2017]: https://doi.org/10.5220/0006418800001626
[research_hargrove_1976]: https://ntrs.nasa.gov/citations/19760024060
[research_harkegard]: https://doi.org/10.1109/cdc.2002.1184694
[research_harley_wilde_2009]: https://doi.org/10.2514/6.2009-146
[research_harman_1944]: https://ntrs.nasa.gov/citations/19930092577
[research_harper_cooper_1984]: https://doi.org/10.2514/6.1984-2442
[research_harper_cooper_1986]: https://doi.org/10.2514/3.20142
[research_harper_jones_1947]: https://ntrs.nasa.gov/citations/19930081822
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harris_2000]: https://doi.org/10.1177/002029400003300805
[research_harris_arthurs_2016]: https://doi.org/10.1109/icuas.2016.7502624
[research_harris_black_1996]: https://doi.org/10.2514/6.1996-3379
[research_harris_gautrey_2000]: https://doi.org/10.1017/s0001924000028098
[research_harris_harris_1997]: https://doi.org/10.2514/6.1997-5505
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_1968]: https://doi.org/10.2514/6.1968-817
[research_hart_1992]: https://doi.org/10.2514/6.1992-4118
[research_hart_hartzell_1984]: https://ntrs.nasa.gov/citations/19850006178
[research_hasan_alam_2013]: https://doi.org/10.1016/j.proeng.2013.03.123
[research_hasoule_whmcavoy_1934]: https://ntrs.nasa.gov/citations/19930091590
[research_hatch_montgomery_1968]: https://ntrs.nasa.gov/citations/19680056564
[research_hatch_montgomery_1969]: https://ntrs.nasa.gov/citations/19690059167
[research_hauch_jacobs_1995]: https://doi.org/10.2514/6.1995-1080
[research_hauser_1999]: https://doi.org/10.21236/ada387263
[research_hayabe_kwak_2025]: https://doi.org/10.2514/6.2025-0257
[research_hayostek_amitay_2018]: https://doi.org/10.2514/6.2018-3729
[research_he_aljiboory_2018]: https://doi.org/10.2514/6.2018-2211
[research_he_hu_2022]: https://doi.org/10.3390/aerospace9070352
[research_he_hu_2022_b]: https://doi.org/10.1016/j.isatra.2022.04.041
[research_he_hu_2023]: https://doi.org/10.3390/drones7050294
[research_he_leprovost_2018]: https://doi.org/10.2514/6.2018-0327
[research_he_song_2020]: https://doi.org/10.2514/6.2020-1908
[research_he_wang_2021]: https://doi.org/10.2514/6.2021-2534
[research_he_yang_2016]: https://doi.org/10.1016/j.jfluidstructs.2015.11.014
[research_hebbar_platzer_1992]: https://doi.org/10.2514/3.46230
[research_hebbar_platzer_1993]: https://doi.org/10.2514/6.1993-868
[research_heeg_chwalowski_2017]: https://doi.org/10.2514/6.2017-0191
[research_hefazi_vore_2013]: https://doi.org/10.2514/6.2013-965
[research_heinze_1932]: https://ntrs.nasa.gov/citations/19930090268
[research_heiss_eberle_1992]: https://doi.org/10.2514/6.1992-2620
[research_helin_walker_1985]: https://doi.org/10.2514/6.1985-130
[research_heltsley_cline_1979]: https://doi.org/10.21236/ada068328
[research_heltsley_crosswy_1981]: https://doi.org/10.21236/ada103929
[research_hemsch_1989]: https://doi.org/10.2514/3.45723
[research_henderson_huffman_1974]: https://ntrs.nasa.gov/citations/19740023308
[research_henderson_lavretsky_1999]: https://doi.org/10.2514/6.1999-4080
[research_henne_hicks_1978]: https://doi.org/10.2514/6.1978-105
[research_hensley_creighton_1987]: https://ntrs.nasa.gov/citations/19880010087
[research_herdiana_pinindriya_2024]: https://doi.org/10.4186/ej.2024.28.12.29
[research_heron_myose_2003]: https://doi.org/10.2514/6.2003-3527
[research_heron_myose_2007]: https://doi.org/10.2514/6.2007-6725
[research_herr_spinner_2023]: https://doi.org/10.2514/6.2023-0246
[research_hess]: https://doi.org/10.1109/icsmc.1995.538185
[research_hess_1977]: https://doi.org/10.1177/001872087701900503
[research_hess_1979]: https://doi.org/10.2514/6.1979-1784
[research_hess_1980]: https://doi.org/10.2514/6.1980-1624
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hess_1982]: https://ntrs.nasa.gov/citations/19830001809
[research_hess_1984]: https://doi.org/10.2514/6.1984-236
[research_hess_1987]: https://doi.org/10.2514/6.1987-2537
[research_hess_1994]: https://ntrs.nasa.gov/citations/19950016877
[research_hess_1995]: https://doi.org/10.1109/21.364831
[research_hess_1997]: https://doi.org/10.2514/2.4169
[research_hess_2009]: https://doi.org/10.2514/6.2009-6320
[research_hess_2011]: https://doi.org/10.2514/6.2011-6554
[research_hess_2016]: https://doi.org/10.1016/j.ifacol.2016.12.206
[research_hess_2016_b]: https://doi.org/10.2514/1.g001303
[research_hess_hess_1997]: https://doi.org/10.2514/6.1997-454
[research_hess_peng_2018]: https://doi.org/10.2514/1.c034497
[research_hess_stout_1997]: https://ntrs.nasa.gov/citations/19980022679
[research_hgo_ly_1995]: https://doi.org/10.2514/6.1995-3251
[research_hicks_moulton_1988]: https://doi.org/10.2514/6.1988-2144
[research_hieser_kudlacik_1956]: https://ntrs.nasa.gov/citations/20050029376
[research_high_alpha_conf_1994]: https://ntrs.nasa.gov/citations/19950007815
[research_hill_1987]: https://doi.org/10.21236/ada186949
[research_hillenherms_schroder_2003]: https://doi.org/10.1007/978-3-540-44866-2_14
[research_hirose_nagai_2007]: https://doi.org/10.2514/6.2007-124
[research_hirsch_mccormick_1965]: https://doi.org/10.2514/6.1965-793
[research_hirsch_mccormick_1966]: https://doi.org/10.2514/3.43778
[research_hitachi_liu_2010]: https://doi.org/10.2514/6.2010-7856
[research_hitzel_2017]: https://doi.org/10.2514/1.c033246
[research_hoadley_vanderbok_1986]: https://doi.org/10.2514/6.1986-2694
[research_hoadley_vanderbok_1988]: https://doi.org/10.2514/3.45574
[research_hoag_schofield_1970]: https://ntrs.nasa.gov/citations/19710000636
[research_hoang_bui_2019]: https://doi.org/10.1007/s12206-019-0120-9
[research_hoang_bui_2019_b]: https://doi.org/10.1007/s12206-019-0520-x
[research_hoang_rediniotis_1993]: https://doi.org/10.2514/6.1993-185
[research_hockman_eisiminger_1948]: https://doi.org/10.2514/8.11490
[research_hodgkinson_2005]: https://doi.org/10.2514/1.3787
[research_hodgkinson_potsdam_1990]: https://ntrs.nasa.gov/citations/19910031662
[research_hodgkinson_skow_1988]: https://doi.org/10.2514/6.1988-4329
[research_hodgkinson_wood_1982]: https://doi.org/10.2514/6.1982-1609
[research_hoff_gratton_2013]: https://doi.org/10.1017/s0001924000008824
[research_hoffler_rao_1988]: https://doi.org/10.2514/3.45563
[research_hoffman_zvara_1970]: https://doi.org/10.2514/3.29898
[research_hoh_1988]: https://doi.org/10.2514/6.1988-4328
[research_hoh_mitchell_2018]: https://doi.org/10.1201/9781315136820-1
[research_holdaway_1954]: https://ntrs.nasa.gov/citations/19930093744
[research_holgate_roskam_1968]: https://doi.org/10.2514/6.1968-56
[research_holleman_gilyard_1972]: https://ntrs.nasa.gov/citations/19720014376
[research_hollingsworth_cohen_1971]: https://doi.org/10.2514/3.59167
[research_hollister_1990]: https://doi.org/10.2514/6.1990-3331
[research_holowicz_holleman_1958]: https://ntrs.nasa.gov/citations/20150018940
[research_holst_1988]: https://doi.org/10.2514/3.45706
[research_holst_thomas_1982]: https://doi.org/10.2514/6.1982-105
[research_holzapfel_dacosta_2006]: https://doi.org/10.2514/6.2006-6222
[research_hong_1993]: https://ntrs.nasa.gov/citations/19930017961
[research_hong_ma_2016]: https://doi.org/10.4028/www.scientific.net/amm.829.110
[research_hooker_2023]: https://doi.org/10.2514/6.2023-0052
[research_hoot_1924]: https://ntrs.nasa.gov/citations/19930091235
[research_hoover_1943]: https://ntrs.nasa.gov/citations/19930092604
[research_hopkins_henderson_1998]: https://doi.org/10.1117/12.310663
[research_hopkins_lovette_1977]: https://ntrs.nasa.gov/citations/19770013088
[research_horizontal_tail_1996]: https://doi.org/10.2514/5.9781600862465.0115.0142
[research_hosangadi_paul_2015]: https://doi.org/10.2514/6.2015-3159
[research_hoshi_kuya_2020]: https://doi.org/10.2514/6.2020-0091
[research_hosseini_hofmann_2025]: https://doi.org/10.2514/6.2025-2173
[research_hou_lv_2022]: https://doi.org/10.1016/j.ast.2022.107950
[research_houbolt_williamson_1975]: https://doi.org/10.21236/ada021713
[research_hougui_balas_1995]: https://doi.org/10.2514/6.1995-3253
[research_house_wallace_1941]: https://ntrs.nasa.gov/citations/19930091783
[research_houtman_timme_2023]: https://doi.org/10.1017/flo.2023.8
[research_houtman_vevek_2023]: https://doi.org/10.2514/6.2023-3242
[research_howard_bray_1996]: https://doi.org/10.2514/3.46942
[research_howard_demoss_2002]: https://doi.org/10.2514/6.2002-4615
[research_howell]: https://doi.org/10.1109/cca.1992.269735
[research_howell_korst_1971]: https://doi.org/10.2514/6.1971-568
[research_hsu_lan_1984]: https://ntrs.nasa.gov/citations/19860012049
[research_hsu_lan_1985]: https://doi.org/10.2514/6.1985-199
[research_hu]: https://doi.org/10.17760/d20449615
[research_hu_1992]: https://doi.org/10.1016/0955-7997(92)90038-9
[research_hu_1995]: https://doi.org/10.1016/0955-7997(95)00083-6
[research_hu_tailless_review_2024]: https://doi.org/10.1142/s2737480724300026
[research_hu_zhao_2025]: https://doi.org/10.1007/s11768-025-00268-4
[research_huang_chow_1996]: https://doi.org/10.2514/3.13210
[research_huang_cummings_2021]: https://doi.org/10.15394/ijaaa.2021.1642
[research_huang_hanff_1999]: https://doi.org/10.2514/6.1999-4102
[research_huang_lou_2000]: https://doi.org/10.2514/6.2000-3911
[research_huang_zhang_2020]: https://doi.org/10.1109/icuas48674.2020.9213966
[research_hubbell]: https://doi.org/10.33915/etd.4382
[research_huber_1995]: https://doi.org/10.2514/6.1995-3199
[research_huber_2022]: https://doi.org/10.2514/6.2022-3438
[research_huber_holdridge_1979]: https://doi.org/10.2514/6.1979-1773
[research_huehne_mahmood_2013]: https://doi.org/10.2514/6.2013-2798
[research_huff_ww_1949]: https://doi.org/10.21236/ad0035641
[research_huffman_1975]: https://ntrs.nasa.gov/citations/19750019955
[research_hughes_mennell_1974]: https://ntrs.nasa.gov/citations/19750005750
[research_hui_tobak_1985]: https://ntrs.nasa.gov/citations/19850015394
[research_huijts_voskuijl_2015]: https://doi.org/10.1016/j.ast.2015.07.001
[research_hull_roger_1975]: https://doi.org/10.21236/adb011143
[research_hulshoff_mulder_1996]: https://doi.org/10.2514/6.1996-3416
[research_humayun_wang_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.48
[research_humphreys_2020]: https://doi.org/10.3390/aerospace7050051
[research_humphreysjennings_lappas_2019]: https://doi.org/10.20944/preprints201911.0284.v1
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_hunsaker_montgomery_2019]: https://doi.org/10.2514/6.2019-2040
[research_hunsaker_montgomery_2020]: https://doi.org/10.2514/6.2020-1264
[research_hunter_1948]: https://ntrs.nasa.gov/citations/19930082385
[research_hunter_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50015-6
[research_hunter_reeder_1946]: https://ntrs.nasa.gov/citations/19930092531
[research_huo_ioannou_2006]: https://doi.org/10.2514/6.2006-1477
[research_hussain_bons_2019]: https://doi.org/10.2514/6.2019-3684
[research_huston_1948]: https://ntrs.nasa.gov/citations/19930090948
[research_hwang_chen_1991]: https://doi.org/10.2514/6.1991-2423
[research_hwang_park_2002]: https://doi.org/10.2514/6.2002-4625
[research_hwang_pi_1975]: https://doi.org/10.2514/3.44487
[research_hwang_pi_1975_b]: https://doi.org/10.2514/6.1975-70
[research_hwang_pi_1978]: https://doi.org/10.2514/6.1978-1456
[research_hwang_pi_1978_b]: https://ntrs.nasa.gov/citations/19790004833
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58518
[research_hwang_pi_1979_b]: https://ntrs.nasa.gov/citations/19790054122
[research_ibrahim_kamal_2023]: https://doi.org/10.2514/6.2023-0102
[research_ide_ishida_2019]: https://doi.org/10.2514/6.2019-1847
[research_ijaz_hamayun_2019]: https://doi.org/10.1007/s12555-017-0399-1
[research_ijaz_hamayun_2019_b]: https://doi.org/10.1177/0142331219835589
[research_ikard_1956]: https://ntrs.nasa.gov/citations/19930084540
[research_iliff_maine_1982]: https://doi.org/10.2514/6.1982-1373
[research_iliff_powers_1969]: https://doi.org/10.2514/6.1969-315
[research_iliff_wang_1996]: https://ntrs.nasa.gov/citations/19970004545
[research_iliff_wang_1997]: https://ntrs.nasa.gov/citations/19970010502
[research_iliff_wang_1999]: https://ntrs.nasa.gov/citations/19990019364
[research_illi_fingskes_2013]: https://doi.org/10.2514/6.2013-2510
[research_iloputaife_iloputaife_1997]: https://doi.org/10.2514/6.1997-3497
[research_imai_1964]: https://doi.org/10.1007/978-3-642-88337-8_24
[research_immordino_vaiuso_2025]: https://doi.org/10.2139/ssrn.5154352
[research_inertia_coupling_2004]: https://doi.org/10.2514/5.9781600862274.0631.0676
[research_inertia_coupling_2015]: https://doi.org/10.2514/5.9781624102745.0681.0730
[research_iniguezdeheredia_friehmelt_2005]: https://doi.org/10.2514/6.2005-6351
[research_initial_tail_2013]: https://doi.org/10.2514/5.9781600868986.0211.0218
[research_integrated_application_1983]: https://ntrs.nasa.gov/citations/19850002697
[research_international_standard_2017]: https://doi.org/10.1002/9781118534786.app1
[research_introduction_the_2017]: https://doi.org/10.2514/5.9781624104435.0001.0038
[research_introduction_to]: https://doi.org/10.1007/978-3-540-46573-7_1
[research_introduction_to_2003]: https://doi.org/10.2514/5.9781600861840.0199.0208
[research_introduction_to_2024]: https://doi.org/10.2514/5.9781624107252.0000.0000
[research_invernizzi_lovera_2018]: https://doi.org/10.1016/j.automatica.2018.05.024
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_ionita_1996]: https://doi.org/10.2514/6.1996-3424
[research_iosilevskii_2025]: https://doi.org/10.1007/978-3-031-73625-4_11
[research_iovnovich_raveh_2017]: https://doi.org/10.2514/1.c033918
[research_irfan_nanangburhan_2026]: https://doi.org/10.35261/barometer.v11i2.13201
[research_irving_1966]: https://doi.org/10.1016/b978-1-4832-0019-4.50011-9
[research_irving_1966_b]: https://doi.org/10.1016/b978-1-4832-0019-4.50009-0
[research_irving_1966_c]: https://doi.org/10.1016/b978-1-4832-0019-4.50014-4
[research_ishida_hashimoto_2017]: https://doi.org/10.2514/6.2017-0494
[research_ishida_ueshima_2026]: https://doi.org/10.2514/1.c038925
[research_ishihara_benmenahem_2010]: https://doi.org/10.2514/6.2010-3455
[research_ishola_whidborne_2024]: https://doi.org/10.3390/robotics13120179
[research_iskrenovicmomcilovic_2018]: https://doi.org/10.14313/jamris_3-2018/18
[research_isogai_2013]: https://doi.org/10.2322/tjsass.56.303
[research_isogai_2016]: https://doi.org/10.2322/tjsass.59.25
[research_ito_endo_2016]: https://doi.org/10.1299/jsmermd.2016.1a2-18a4
[research_itty_leith_1992]: https://doi.org/10.2514/6.1992-4496
[research_iwakawa_furukawa_2015]: https://doi.org/10.2514/6.2015-2584
[research_iwatani_asada_2022]: https://doi.org/10.2514/6.2022-0461
[research_iyer_spall_1992]: https://doi.org/10.2514/6.1992-2630
[research_izadi_pakmehr_2007]: https://doi.org/10.1109/aero.2007.352761
[research_izquierdo]: https://doi.org/10.11606/d.18.2016.tde-26072016-104731
[research_izumi_ogino_2015]: https://doi.org/10.2514/6.2015-0259
[research_j_j_2015]: https://doi.org/10.14445/23488360/ijme-v2i6p103
[research_jabbar_setiawan_2026]: https://doi.org/10.35261/barometer.v11i2.13206
[research_jackson_2023]: https://doi.org/10.32920/ryerson.14660895.v1
[research_jackson_rivers_1993]: https://doi.org/10.2514/3.25564
[research_jackson_snyder_1966]: https://ntrs.nasa.gov/citations/19660029457
[research_jackuliak_bugaj_2026]: https://doi.org/10.23919/ntca68808.2026.11524172
[research_jacob_1987]: https://doi.org/10.2514/3.45429
[research_jacobs_1942]: https://ntrs.nasa.gov/citations/19930092756
[research_jacobs_1983]: https://ntrs.nasa.gov/citations/19850007386
[research_jacobs_bartlett_1981]: https://ntrs.nasa.gov/citations/19810010483
[research_jacobsen_2006]: https://doi.org/10.1016/j.ast.2006.05.002
[research_jacobson_lapins_1975]: https://ntrs.nasa.gov/citations/19750055452
[research_jadopuente_brutch_2025]: https://doi.org/10.2514/6.2025-2279
[research_jagtap_childs_2025]: https://doi.org/10.2139/ssrn.5087765
[research_jahnke_culick_1990]: https://ntrs.nasa.gov/citations/19900035129
[research_jaiswal_prakash_2022]: https://doi.org/10.13111/2066-8201.2022.14.1.4
[research_jalovecky_janu_2010]: https://doi.org/10.1007/978-3-642-05022-0_27
[research_james_meyn_1994]: https://doi.org/10.4271/941140
[research_jameson]: https://doi.org/10.1007/bfb0074531
[research_jameson_1973]: https://doi.org/10.2514/6.1973-3002
[research_jameson_1977]: https://doi.org/10.2172/7093932
[research_jameson_caughey_1977]: https://doi.org/10.2172/7308750
[research_jamwal_hosangadi_2018]: https://doi.org/10.2514/6.2018-3956
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_janardhan_grandhi_2003_b]: https://doi.org/10.2514/6.2003-1944
[research_janardhan_grandhi_2005]: https://doi.org/10.2514/1.627
[research_jang_kim_1994]: https://doi.org/10.2514/6.1994-3518
[research_jansen_1980]: https://doi.org/10.2514/6.1980-1568
[research_jansen_vankampen_2025]: https://doi.org/10.2514/6.2025-2794
[research_jansen_vos_2016]: https://doi.org/10.2514/6.2016-1281
[research_jaredagrauer_2018]: https://ntrs.nasa.gov/citations/20190000878
[research_jarmark_speyer_1988]: https://doi.org/10.2514/6.1988-4156
[research_jarrah_1989]: https://doi.org/10.2514/6.1989-295
[research_jategaonkar_2005]: https://doi.org/10.2514/1.15766
[research_jategaonkar_fischenberg_2004]: https://doi.org/10.2514/1.3165
[research_jategaonkar_monnich_1997]: https://doi.org/10.2514/2.2169
[research_javed_shafikhan_2019]: https://doi.org/10.1109/ibcast.2019.8667178
[research_jeffrie_rolston_1972]: https://doi.org/10.2514/6.1972-761
[research_jenkins_1989]: https://doi.org/10.2514/6.1989-3351
[research_jenkins_kuhl_1977]: https://ntrs.nasa.gov/citations/20020086520
[research_jenkins_myatt_1993]: https://doi.org/10.2514/6.1993-621
[research_jenks_henry_1977]: https://ntrs.nasa.gov/citations/19770014139
[research_jenney_1935]: https://doi.org/10.2514/8.126
[research_jentzsch_2019]: https://doi.org/10.2514/1.j056962
[research_jentzsch_taubert_2017]: https://doi.org/10.2514/6.2017-3042
[research_jeram_prasad_2003]: https://doi.org/10.2514/6.2003-5311
[research_jeram_prasad_2003_b]: https://doi.org/10.4050/vfs-f59-000144
[research_jernell_1978]: https://ntrs.nasa.gov/citations/19780017136
[research_ji_kim_2021]: https://doi.org/10.3390/aerospace8050126
[research_jiang_1999]: https://doi.org/10.4271/1999-01-5618
[research_jiang_an_2000]: https://doi.org/10.2514/6.2000-4324
[research_jiang_guo_2025]: https://doi.org/10.1108/aeat-06-2024-0164
[research_jiang_li_2026]: https://doi.org/10.3390/drones10060433
[research_jiang_tian_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000875
[research_jiang_tian_2019]: https://doi.org/10.1016/j.ast.2019.03.043
[research_jiang_zhang_2019]: https://doi.org/10.23919/chicc.2019.8866455
[research_jianjunma_pengli_2008]: https://doi.org/10.1109/asc-icsc.2008.4675349
[research_jiayu_yuchao_2024]: https://doi.org/10.1007/978-981-99-8045-1_32
[research_jiguangli_xinchen_2016]: https://doi.org/10.1109/cgncc.2016.7828811
[research_jingping_weiguo_2011]: https://doi.org/10.1016/j.proeng.2011.08.232
[research_jingwei_jiaming_2020]: https://doi.org/10.1109/icmeas51739.2020.00036
[research_jinli_zhichun_2013]: https://doi.org/10.1016/j.proeng.2013.08.028
[research_jo_park_2015]: https://doi.org/10.2514/6.2015-3235
[research_jo_park_2016]: https://doi.org/10.2514/6.2016-0163
[research_johndfunk_corinpbeck_1993]: https://ntrs.nasa.gov/citations/19940008845
[research_johnelamar_cliffordjobara_2001]: https://ntrs.nasa.gov/citations/20010047400
[research_johnson_1935]: https://doi.org/10.2514/8.111
[research_johnson_1937]: https://doi.org/10.2514/8.473
[research_johnson_1946]: https://ntrs.nasa.gov/citations/20090026463
[research_johnson_1948]: https://ntrs.nasa.gov/citations/19930082439
[research_johnson_1950]: https://ntrs.nasa.gov/citations/19930092035
[research_johnson_1951]: https://ntrs.nasa.gov/citations/20050030031
[research_johnson_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50013-2
[research_johnson_1982]: https://doi.org/10.1007/978-3-662-12610-3_31
[research_johnson_boisseau_1953]: https://ntrs.nasa.gov/citations/20050029408
[research_johnson_glider_1949]: https://ntrs.nasa.gov/citations/20090026465
[research_johnson_hayes_1953]: https://ntrs.nasa.gov/citations/19930087757
[research_johnson_lind_2009]: https://doi.org/10.2514/6.2009-6151
[research_johnson_p63_1946]: https://ntrs.nasa.gov/citations/19930092636
[research_johnson_weir_1968]: https://doi.org/10.2514/6.1968-819
[research_johnson_weir_1969]: https://doi.org/10.2514/3.44096
[research_johnson_yang_1985]: https://doi.org/10.4271/850912
[research_johnston_1992]: https://doi.org/10.2514/6.1992-2653
[research_johnston_1998]: https://doi.org/10.2514/6.1998-2736
[research_johnston_ashkenas_1974]: https://doi.org/10.21236/ada014366
[research_jones_1947]: https://ntrs.nasa.gov/citations/19930091936
[research_jones_cohen_1976]: https://ntrs.nasa.gov/citations/19760011989
[research_jones_farmer_1959]: https://ntrs.nasa.gov/citations/19980223588
[research_jones_fehlner_1940]: https://ntrs.nasa.gov/citations/19930081625
[research_jones_franke_2006]: https://doi.org/10.2514/6.2006-2832
[research_jones_klyde_2023]: https://doi.org/10.4050/sm_2023_hq-1189
[research_jones_nisbet_1976]: https://ntrs.nasa.gov/citations/19760064883
[research_jordan_hahne_1987]: https://ntrs.nasa.gov/citations/19870061804
[research_joshi_rickard_1981]: https://doi.org/10.2514/6.1981-1887
[research_joshi_sreenatha_1998]: https://doi.org/10.1109/87.709502
[research_jou_mueller_1985]: https://doi.org/10.21236/ada172853
[research_juhasz_tischler_2015]: https://doi.org/10.2514/6.2015-0906
[research_jump_padfield_2006]: https://doi.org/10.1108/17488840610639618
[research_jumper_1983]: https://doi.org/10.2514/3.44961
[research_jun_2023]: https://doi.org/10.1109/csat61646.2023.00170
[research_jun_nelson_1987]: https://doi.org/10.2514/6.1987-332
[research_junfeng_wuzhou_2020]: https://doi.org/10.1109/icus50048.2020.9274833
[research_jung_lowenberg_2005]: https://doi.org/10.2514/6.2005-6123
[research_jung_reimerdes_2003]: https://doi.org/10.1007/978-3-540-44866-2_10
[research_jurado_mcgehee_2019]: https://doi.org/10.2514/1.c034964
[research_justinjamesmatt_haiyangchao_2025]: https://doi.org/10.31224/4308
[research_jyothi_bindu_2006]: https://doi.org/10.2514/6.2006-7792
[research_kaattari_1959]: https://ntrs.nasa.gov/citations/19980228137
[research_kahveci_ioannou_2010]: https://doi.org/10.2514/6.2010-3397
[research_kale_pendharkar_2021]: https://doi.org/10.1088/1742-6596/2089/1/012024
[research_kaletka_fu_1993]: https://doi.org/10.2514/6.1993-3635
[research_kalyankar_pompe_2024]: https://doi.org/10.2514/6.2024-3758
[research_kalyankar_urreiztieta_2025]: https://doi.org/10.2514/6.2025-3090
[research_kamal_aly_2015]: https://doi.org/10.2514/6.2015-1595
[research_kaminer_howard_1996]: https://doi.org/10.2514/6.1996-3861
[research_kanazaki_2023]: https://doi.org/10.3390/aerospace10090790
[research_kanchi_he_2026]: https://doi.org/10.2514/6.2026-4639
[research_kandil_1992]: https://ntrs.nasa.gov/citations/19930000910
[research_kandil_1993]: https://ntrs.nasa.gov/citations/19940015148
[research_kandil_flanagan_1994]: https://doi.org/10.2514/6.1994-3486
[research_kandil_kalisch_1994]: https://doi.org/10.2514/6.1994-1887
[research_kandil_kandil_1993]: https://doi.org/10.2514/6.1993-3688
[research_kandil_kandil_1993_b]: https://doi.org/10.2514/6.1993-3472
[research_kandil_menzies_1997]: https://ntrs.nasa.gov/citations/19970017810
[research_kandil_salman_1991]: https://ntrs.nasa.gov/citations/19910059024
[research_kandil_salman_1992]: https://doi.org/10.2514/6.1992-280
[research_kandil_salman_1992_b]: https://ntrs.nasa.gov/citations/19930030334
[research_kandil_sheta_1995]: https://doi.org/10.2514/6.1995-3464
[research_kang_choi_2022]: https://doi.org/10.1007/s42405-021-00425-4
[research_kania_2025]: https://doi.org/10.3390/app152212097
[research_kannan_bhat_2005]: https://doi.org/10.2514/1.12821
[research_karagiannis_astolfi_2007]: https://doi.org/10.23919/ecc.2007.7069048
[research_karahan_2026]: https://doi.org/10.70286/eoss-26.01.2026.001.15-23
[research_karasinski_robinson_2022]: https://doi.org/10.2514/6.2022-0509
[research_karasu_2015]: https://doi.org/10.18186/jte.97467
[research_karimikelayeh_djavareshkian_2021]: https://doi.org/10.1016/j.cja.2020.06.022
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karpouzian_librescu_1992]: https://doi.org/10.2514/6.1992-2469
[research_karr_nishita_2005]: https://doi.org/10.1007/s10489-005-4614-z
[research_karthik_tulapurkara_1999]: https://doi.org/10.2514/2.2529
[research_karunanidhi_scholz_2022]: https://doi.org/10.1063/5.0082095
[research_kashiwagura_shimoyama_2018]: https://doi.org/10.2514/6.2018-1914
[research_kass_1970]: https://doi.org/10.2514/6.1970-875
[research_katayanagi_2001]: https://doi.org/10.2322/tjsass.44.48
[research_katayanagi_2004]: https://doi.org/10.2514/6.2004-4998
[research_katz_1989]: https://doi.org/10.2514/3.10231
[research_katz_1999]: https://doi.org/10.1016/s0376-0421(99)00004-4
[research_katz_levin_1984]: https://doi.org/10.2514/3.44988
[research_katz_levin_1991]: https://doi.org/10.2514/3.46024
[research_katzenmeier_vidy_2021]: https://doi.org/10.1007/s13272-021-00523-9
[research_katzoff_1940]: https://ntrs.nasa.gov/citations/19930091767
[research_katzoff_sweberg_1942]: https://ntrs.nasa.gov/citations/19930091817
[research_kaups_mehta_1989]: https://doi.org/10.2514/3.45774
[research_kawazoe_morita_2003]: https://doi.org/10.2514/6.2003-3471
[research_kawazoe_morita_2004]: https://doi.org/10.2514/6.2004-2352
[research_kawazoe_yorikane_2001]: https://doi.org/10.2514/6.2001-299
[research_kaye]: https://doi.org/10.22215/etd/1995-02921
[research_kaygan_ulusoy_2018]: https://doi.org/10.30518/jav.482507
[research_kazarin_mackunis_2017]: https://doi.org/10.2514/6.2017-3730
[research_keenan_kuhlman_1991]: https://doi.org/10.2514/6.1991-3305
[research_keener_1984]: https://doi.org/10.2514/6.1984-2092
[research_keener_1985]: https://doi.org/10.2514/3.45163
[research_keener_mcleod_1958]: https://ntrs.nasa.gov/citations/19930090188
[research_kefayat_kamali_2024]: https://doi.org/10.1109/iccia65044.2024.10768167
[research_kehlet_1954]: https://ntrs.nasa.gov/citations/20090023148
[research_kehlet_1957]: https://ntrs.nasa.gov/citations/19930089726
[research_keidel_fasel_2017]: https://doi.org/10.1115/smasis2017-3826
[research_keidel_fasel_2019]: https://doi.org/10.2514/6.2019-0854
[research_keidel_fasel_2020]: https://doi.org/10.2514/1.c035606
[research_keithdwichman_josephwpahle_1996]: https://ntrs.nasa.gov/citations/19970001693
[research_kelly_1988]: https://doi.org/10.2514/6.1988-2129
[research_kemp_becht_1950]: https://ntrs.nasa.gov/citations/19930086033
[research_kemp_becht_1953]: https://ntrs.nasa.gov/citations/19930087785
[research_kemp_lockwood_1966]: https://ntrs.nasa.gov/citations/19660028848
[research_kempel_1971]: https://ntrs.nasa.gov/citations/19710023831
[research_kempel_dana_1975]: https://ntrs.nasa.gov/citations/19750018943
[research_kempel_mcneill_1988]: https://doi.org/10.2514/6.1988-402
[research_kendall_2005]: https://doi.org/10.4271/2005-01-3418
[research_kendall_2018]: https://doi.org/10.1201/9781315136820-7
[research_kendall_morgan_2010]: https://ntrs.nasa.gov/citations/20100042338
[research_kennelly_kroo_1990]: https://ntrs.nasa.gov/citations/19920022969
[research_kentfield_2006]: https://doi.org/10.2514/1.16890
[research_kentfield_2009]: https://doi.org/10.2514/6.2009-3961
[research_kentfield_spragins_2004]: https://doi.org/10.2514/1.558
[research_khalid_2023]: https://doi.org/10.4197/eng.33-1.5
[research_khan_2019]: https://doi.org/10.18178/ijmmm.2019.7.5.464
[research_khan_bandyopadhyay]: https://doi.org/10.1109/icit.2000.854106
[research_khan_deng_2012]: https://doi.org/10.1109/ibcast.2012.6177558
[research_khan_masud_2026]: https://doi.org/10.2514/6.2026-2104
[research_khan_shaikh_2025]: https://doi.org/10.37934/arfmts.18.1.106117
[research_khan_weiguo_2012]: https://doi.org/10.1016/j.proeng.2011.12.678
[research_kharisov_hovakimyan_2010]: https://doi.org/10.2514/6.2010-3395
[research_kholodar_dowell_2004]: https://doi.org/10.2514/1.618
[research_khot_eastep_1997]: https://doi.org/10.2514/6.1997-1268
[research_kidd_1988]: https://doi.org/10.2514/6.1988-4335
[research_kidd_bull_1963]: https://doi.org/10.21236/ad0400265
[research_kier_muller_2020]: https://doi.org/10.2514/6.2020-1621
[research_kikuchi_kouchi_2024]: https://doi.org/10.2514/6.2024-0905
[research_kilgore_adcock_1972]: https://ntrs.nasa.gov/citations/19720014377
[research_kim_ahn_2013]: https://doi.org/10.2514/6.2013-5169
[research_kim_koh_2025]: https://doi.org/10.1007/s42405-025-01059-6
[research_kim_kunz_2016]: https://doi.org/10.2514/6.2016-3542
[research_kim_marciniak_1998]: https://doi.org/10.2514/6.1998-4259
[research_kim_marciniak_1999]: https://doi.org/10.2514/6.1999-1468
[research_kim_marciniak_2000]: https://doi.org/10.2514/2.2630
[research_kim_marciniak_2002]: https://doi.org/10.2514/2.2936
[research_kim_rockwell_2005]: https://doi.org/10.2514/1.9989
[research_kim_song_2013]: https://doi.org/10.2514/1.c031212
[research_kimberlin_sims_1992]: https://doi.org/10.2514/6.1992-4090
[research_kimler_canfield_2006]: https://doi.org/10.2514/6.2006-7134
[research_king_gopalarathnam_2005]: https://doi.org/10.2514/1.10942
[research_kirkham_jackson_1974]: https://doi.org/10.2514/6.1974-988
[research_kirschstein_alles_2004]: https://doi.org/10.1016/j.ast.2004.06.002
[research_kish_leggett_1996]: https://doi.org/10.2514/6.1996-3431
[research_kish_mosle_1997]: https://doi.org/10.21236/ada286959
[research_kish_mosle_1997_b]: https://doi.org/10.2514/6.1997-3703
[research_kisslinger_wendl_1971]: https://doi.org/10.21236/ad0727762
[research_kitsios_dimopoulos_2020]: https://doi.org/10.1109/icuas48674.2020.9213877
[research_kizildeniz_kiyak_2025]: https://doi.org/10.1108/aeat-03-2025-0127
[research_kjelgaard_paulson_1981]: https://ntrs.nasa.gov/citations/19810023576
[research_klausmeyer_2004]: https://doi.org/10.2514/6.2004-553
[research_klausmeyer_2018]: https://doi.org/10.2514/6.2018-2992
[research_klausmeyer_2026]: https://doi.org/10.2514/6.2026-1329
[research_klausmeyer_laflin_2023]: https://doi.org/10.2514/6.2023-4399
[research_klawans_white_1957]: https://ntrs.nasa.gov/citations/19930084970
[research_kleckner_1943]: https://ntrs.nasa.gov/citations/19930092864
[research_kleckner_1943_b]: https://ntrs.nasa.gov/citations/19930092865
[research_klein_1979]: https://ntrs.nasa.gov/citations/19790011900
[research_klein_1999]: https://ntrs.nasa.gov/citations/19990100653
[research_klein_batterson_1981]: https://doi.org/10.2514/6.1981-1866
[research_klein_batterson_1983]: https://doi.org/10.2514/6.1983-2066
[research_klein_lapins_1982]: https://doi.org/10.2514/6.1982-180
[research_kleinert_ehrle_2023]: https://doi.org/10.1007/s13272-023-00670-1
[research_klinar_jones_1948]: https://ntrs.nasa.gov/citations/20050030058
[research_kloker_2008]: https://doi.org/10.2514/6.2008-3835
[research_klotz_thabet_2023]: https://doi.org/10.1016/j.rineng.2023.101088
[research_kluever_2004]: https://doi.org/10.2514/6.2004-4770
[research_kluever_2007]: https://doi.org/10.2514/1.28081
[research_klunk_freeman_2018]: https://doi.org/10.2514/6.2018-5022
[research_klyde_bachelder_2007]: https://doi.org/10.2514/6.2007-6385
[research_klyde_mcruer_1996]: https://doi.org/10.2514/6.1996-3432
[research_klyde_mcruer_1997]: https://doi.org/10.2514/2.3998
[research_klyde_mitchell_1999]: https://doi.org/10.2514/6.1999-1069
[research_klyde_mitchell_2003]: https://doi.org/10.2514/6.2003-5463
[research_klyde_mitchell_2004]: https://doi.org/10.2514/1.3215
[research_klyde_schulze_2020]: https://doi.org/10.2514/1.g004981
[research_klyde_schulze_2020_b]: https://ntrs.nasa.gov/citations/20200002019
[research_klyde_smith_2002]: https://doi.org/10.2514/6.2002-4697
[research_knapp_jordan_1953]: https://ntrs.nasa.gov/citations/19930089110
[research_knight_wykes_1966]: https://doi.org/10.2514/6.1966-999
[research_kobayashi_2002]: https://doi.org/10.2322/tjsass.45.124
[research_kock_1972]: https://ntrs.nasa.gov/citations/19720011372
[research_koenig_rolls_1966]: https://ntrs.nasa.gov/citations/19660018215
[research_koike_ueno_2016]: https://doi.org/10.2514/6.2016-4044
[research_kojima_hashimoto_2023]: https://doi.org/10.2514/6.2023-1425
[research_kojima_kameda_2019]: https://doi.org/10.1007/978-3-319-91017-8_134
[research_kolesnikov_2005]: https://doi.org/10.2514/6.2005-5977
[research_kolonay_yang_1998]: https://doi.org/10.2514/2.2260
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_kong_pan_2023]: https://doi.org/10.1088/1742-6596/2658/1/012047
[research_konstadinopoulos_mook_1985]: https://doi.org/10.2514/6.1985-198
[research_koprucu_ozturk_2024]: https://doi.org/10.56753/asrel.2024.3.5
[research_koreanschi_oliviu_2014]: https://doi.org/10.2514/6.2014-3170
[research_koreanschi_oliviu_2016]: https://doi.org/10.2514/6.2016-1083
[research_kornev_pimenov_2022]: https://doi.org/10.34759/trd-2022-123-07
[research_korthauer_accorinti_2023]: https://doi.org/10.2514/1.j061915
[research_kotfila_painter_1969]: https://ntrs.nasa.gov/citations/19690061424
[research_kotikalpudi_danowsky_2018]: https://doi.org/10.2514/6.2018-3426
[research_kousen_bendiksen_1994]: https://doi.org/10.2514/3.46644
[research_koven_kayten_1946]: https://ntrs.nasa.gov/citations/19930092590
[research_kowal_vakili_1998]: https://doi.org/10.2514/6.1998-416
[research_kowalska_goetzendorfgrabowski_2022]: https://doi.org/10.1108/aeat-01-2022-0001
[research_kownacki_2013]: https://doi.org/10.2478/ama-2013-0025
[research_kraft_1953]: https://ntrs.nasa.gov/citations/19930083857
[research_kraft_goranson_1948]: https://ntrs.nasa.gov/citations/20090022749
[research_kraft_reeder_1948]: https://ntrs.nasa.gov/citations/20050028482
[research_krekeler_wilson_1990]: https://doi.org/10.2514/6.1990-219
[research_krishnaswamy_papageorgiou]: https://doi.org/10.1109/acc.2005.1470177
[research_krone_1980]: https://doi.org/10.2514/6.1980-3047
[research_krone_1980_b]: https://doi.org/10.2514/6.1980-1882
[research_kroo_1982]: https://doi.org/10.2514/3.61557
[research_kroo_1983]: https://doi.org/10.2514/6.1983-2476
[research_kroo_1994]: https://ntrs.nasa.gov/citations/19960049782
[research_kubica_livet_1994]: https://doi.org/10.2514/6.1994-3630
[research_kucera_hromcik_2013]: https://doi.org/10.1051/eucass/201306767
[research_kuehme_alley_2014]: https://doi.org/10.2514/6.2014-2577
[research_kuhlman_liaw_1987]: https://doi.org/10.2514/6.1987-2482
[research_kumada_sawada_2016]: https://doi.org/10.2514/6.2016-1346
[research_kumar_ghosh_2014]: https://doi.org/10.1017/s0001924000010149
[research_kumar_ghosh_2023]: https://doi.org/10.61653/joast.v66i4.2014.481
[research_kumar_mandal_2020]: https://doi.org/10.2514/6.2020-3064
[research_kumar_okasha_2023]: https://doi.org/10.1109/aset56582.2023.10180448
[research_kumar_palanivel_2025]: https://doi.org/10.2514/6.2025-1076
[research_kumar_rao_2004]: https://doi.org/10.14429/dsj.54.2041
[research_kumar_sunil_2021]: https://doi.org/10.1007/978-981-15-9601-8_13
[research_kun_lixin_2011]: https://doi.org/10.1016/j.proeng.2011.10.021
[research_kurtz_wittig_2016]: https://doi.org/10.2514/1.c033357
[research_kurz_kloker_2015]: https://doi.org/10.2514/6.2015-3079
[research_kusunose_marcum_1987]: https://doi.org/10.2514/6.1987-1196
[research_kutney_piszkin_1963]: https://doi.org/10.2514/6.1963-276
[research_kutney_piszkin_1964]: https://doi.org/10.2514/3.43551
[research_kuzina]: https://doi.org/10.22215/etd/1986-01124
[research_kuzmin_2007]: https://doi.org/10.1007/978-3-540-75995-9_64
[research_kuzmin_2009]: https://doi.org/10.1016/j.compfluid.2008.01.017
[research_kuzmin_2010]: https://doi.org/10.1142/9789814313377_0022
[research_kuzmin_shilkin_2009]: https://doi.org/10.1007/978-3-540-92779-2_134
[research_kuzmina_ishmuratov_2004]: https://doi.org/10.2514/6.2004-4611
[research_kwatny_bennett_1991]: https://doi.org/10.1109/9.100946
[research_kwiek_2019]: https://doi.org/10.1108/aeat-01-2018-0032
[research_kwiek_figat_2016]: https://doi.org/10.1017/aer.2015.16
[research_laar_atherstone_2024]: https://doi.org/10.2514/6.2024-2669
[research_lacey_1979]: https://doi.org/10.21236/ada085065
[research_lagemann_2024]: https://doi.org/10.52843/cassyni.p1bbsw
[research_lai_zhang_2014]: https://doi.org/10.2514/6.2014-1200
[research_laiqurrehman_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.12
[research_laitone_1978]: https://doi.org/10.2514/3.58457
[research_laitone_1978_b]: https://doi.org/10.2514/3.58339
[research_laitone_vinh_1970]: https://doi.org/10.2514/6.1970-977
[research_lamar_2001]: https://ntrs.nasa.gov/citations/20010047593
[research_lamar_2003]: https://ntrs.nasa.gov/citations/20040040242
[research_lamb_sawyer_1981]: https://ntrs.nasa.gov/citations/19810020557
[research_lamb_sawyer_1981_b]: https://ntrs.nasa.gov/citations/19810052971
[research_lampropoulos_sarris_2025]: https://doi.org/10.3844/jastsp.2025.1.11
[research_lan_hsu_1982]: https://doi.org/10.2514/6.1982-1385
[research_lan_hsu_1995]: https://doi.org/10.2514/6.1995-3442
[research_lan_li_2002]: https://doi.org/10.2514/6.2002-4804
[research_lan_mehrotra_1978]: https://ntrs.nasa.gov/citations/19780015111
[research_landahl_1959]: https://doi.org/10.1016/b978-1-4831-9832-3.50015-2
[research_lange_1945]: https://ntrs.nasa.gov/citations/19930092687
[research_lange_1947]: https://ntrs.nasa.gov/citations/19930093787
[research_langham_1979]: https://doi.org/10.2514/6.1979-1621
[research_langston_nelson_2016]: https://doi.org/10.2514/6.2016-1036
[research_langton_2006]: https://doi.org/10.1002/9780470058480
[research_lapin_crookshanks_1952]: https://doi.org/10.2514/8.2336
[research_lapins_klein_1982]: https://doi.org/10.2514/6.1982-1295
[research_larrabee_tymczyszyn_1968]: https://doi.org/10.2514/6.1968-189
[research_larson_1986]: https://doi.org/10.2514/6.1986-2237
[research_larson_1987]: https://ntrs.nasa.gov/citations/19870007386
[research_lateral_control_2003]: https://doi.org/10.2514/5.9781600861840.0323.0340
[research_lateral_directional_dynamic_2016]: https://doi.org/10.1201/b15956-11
[research_lateral_directional_dynamics_1998]: https://doi.org/10.2514/5.9781600862052.0207.0256
[research_lateral_directional_motion_2016]: https://doi.org/10.1201/b15956-10
[research_lateral_directional_motions_2015]: https://doi.org/10.2307/j.ctt1287kgx.9
[research_lateral_directional_stability_2003]: https://doi.org/10.2514/5.9781600861840.0297.0310
[research_lauchle_1974]: https://doi.org/10.2514/3.62987
[research_laurencelepage_1925]: https://doi.org/10.1017/s0368393100134601
[research_lauten_1954]: https://ntrs.nasa.gov/citations/19630003991
[research_lawrence_draperdonley_2005]: https://doi.org/10.2514/6.2005-5906
[research_lee_1946]: https://doi.org/10.1017/s0368393100120863
[research_lee_1947]: https://doi.org/10.1017/s036839310011185x
[research_lee_1985]: https://doi.org/10.2514/3.45210
[research_lee_1990]: https://doi.org/10.1017/s0001924000022752
[research_lee_2000]: https://doi.org/10.1016/s0376-0421(00)00003-8
[research_lee_batina_1990]: https://ntrs.nasa.gov/citations/19900009895
[research_lee_batina_1990_b]: https://ntrs.nasa.gov/citations/19910001591
[research_lee_batina_1991]: https://doi.org/10.2514/3.45996
[research_lee_byoungmunmin_2008]: https://doi.org/10.1109/iccas.2008.4694548
[research_lee_gross_2024]: https://doi.org/10.2514/6.2024-1352
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lan_1986]: https://ntrs.nasa.gov/citations/19870017425
[research_lee_lan_1987]: https://ntrs.nasa.gov/citations/19870016603
[research_lee_lan_1989]: https://ntrs.nasa.gov/citations/19890051814
[research_lee_nam_2023]: https://doi.org/10.5139/jksas.2023.51.6.363
[research_lee_pereira_2013]: https://doi.org/10.1016/j.jfluidstructs.2013.08.004
[research_lee_pereira_2013_b]: https://doi.org/10.1007/s00348-013-1564-9
[research_lee_singh_2013]: https://doi.org/10.2514/6.2013-4511
[research_lee_tischler_2001]: https://doi.org/10.2514/6.2001-4266
[research_lee_vining_2018]: https://doi.org/10.2514/6.2018-4171
[research_lee_yoon_2008]: https://doi.org/10.1016/j.simpat.2007.08.009
[research_leggett_cord_1994]: https://doi.org/10.2514/6.1994-2113
[research_legouis_laneville_1986]: https://doi.org/10.1080/00423118608968837
[research_legriffon_bertsch_2023]: https://doi.org/10.25144/14610
[research_lei_zha_2023]: https://doi.org/10.2514/6.2023-3606
[research_lei_zhang_2025]: https://doi.org/10.1134/s0869864324060222
[research_leishman_2026]: https://doi.org/10.2514/1.c039163
[research_lemay_lovato_1994]: https://doi.org/10.2514/6.1994-70
[research_lemko_molodchyk_2015]: https://doi.org/10.1109/apuavd.2015.7346552
[research_lemley_mullans_1974]: https://doi.org/10.2514/3.60344
[research_lemon_litt_2011]: https://doi.org/10.2514/6.2011-6308
[research_lensi_2000]: https://doi.org/10.2514/6.2000-3901
[research_leonard_2013]: https://ntrs.nasa.gov/citations/20140008292
[research_leprovost_williams_2018]: https://doi.org/10.2514/6.2018-3068
[research_lesiario_hagstrom_2010]: https://doi.org/10.2514/6.2010-7821
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_letko_1951]: https://ntrs.nasa.gov/citations/19930083094
[research_letko_riley_1950]: https://ntrs.nasa.gov/citations/19930082786
[research_levi_nelson_1963]: https://doi.org/10.2514/6.1963-1801
[research_levi_nelson_1964]: https://doi.org/10.2514/3.43579
[research_levin_1981]: https://doi.org/10.2514/6.1981-1876
[research_levinski_hill_2006]: https://doi.org/10.2514/6.2006-3484
[research_levison_rickard_1981]: https://doi.org/10.2514/6.1981-1773
[research_levy_1992]: https://doi.org/10.2514/6.1992-4193
[research_leylek_costello_2013]: https://doi.org/10.2514/6.2013-4982
[research_li_2024]: https://doi.org/10.1007/978-981-97-3998-1_62
[research_li_chen_2017]: https://doi.org/10.1016/j.dt.2017.06.003
[research_li_chen_2021]: https://doi.org/10.1177/01423312211027037
[research_li_dai_2025]: https://doi.org/10.1016/j.taml.2024.100554
[research_li_dong_2018]: https://doi.org/10.1002/asjc.1841
[research_li_han_2023]: https://doi.org/10.2139/ssrn.4654500
[research_li_han_2024]: https://doi.org/10.1016/j.ast.2024.108968
[research_li_liu_2023]: https://doi.org/10.1016/j.isatra.2022.10.021
[research_li_ma_2014]: https://doi.org/10.4028/www.scientific.net/amm.472.185
[research_li_qian_2019]: https://doi.org/10.1007/978-981-13-3305-7_108
[research_li_qu_2014]: https://doi.org/10.1109/icsai.2014.7009259
[research_li_shi_2022]: https://doi.org/10.3934/jimo.2020180
[research_li_shu_2026]: https://doi.org/10.2139/ssrn.6999271
[research_li_split_rudder_2022]: https://doi.org/10.1016/j.jfluidstructs.2022.103718
[research_li_sun_2019]: https://doi.org/10.1016/j.ejcon.2019.04.008
[research_li_sun_2022]: https://doi.org/10.1109/access.2022.3157878
[research_li_sun_2023]: https://doi.org/10.1088/1742-6596/2472/1/012019
[research_li_wang_2025]: https://doi.org/10.23919/ccc64809.2025.11179130
[research_li_wei_2026]: https://doi.org/10.1016/j.measurement.2025.120038
[research_li_wing_rock_2023]: https://doi.org/10.1017/flo.2023.30
[research_li_xu_2013]: https://doi.org/10.4028/www.scientific.net/amr.706-708.1038
[research_li_yang_2013]: https://doi.org/10.4028/www.scientific.net/amr.655-657.757
[research_li_yong_2017]: https://doi.org/10.23919/chicc.2017.8027800
[research_li_yu_2011]: https://doi.org/10.4028/www.scientific.net/amm.138-139.404
[research_li_yu_2012]: https://doi.org/10.1166/asl.2012.2975
[research_li_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9019083
[research_li_zhang_2025]: https://doi.org/10.1051/jnwpu/20254350888
[research_li_zhu_1999]: https://doi.org/10.1007/bf01179541
[research_liang_feng_2025]: https://doi.org/10.3390/aerospace13010011
[research_liangqu_yinghui_2016]: https://doi.org/10.21629/jsee.2016.04.18
[research_liao_wang_2002]: https://doi.org/10.2514/6.2002-4449
[research_lichon_2016]: https://doi.org/10.5604/12314005.1217238
[research_lichota_2016]: https://doi.org/10.15632/jtam-pl.54.1.87
[research_lichota_2023]: https://doi.org/10.1108/aeat-01-2023-0013
[research_lichota_ohme_2016]: https://doi.org/10.2514/6.2016-3704
[research_lichter_bateman_2009]: https://doi.org/10.2514/6.2009-6257
[research_licini_white_2024]: https://doi.org/10.1119/5.0142119
[research_liddell_1947]: https://ntrs.nasa.gov/citations/20050081862
[research_liebeck_2002]: https://doi.org/10.2514/6.2002-2
[research_liebeck_2003]: https://doi.org/10.2514/6.2003-2659
[research_liebeck_2008]: https://doi.org/10.2514/6.2008-6414
[research_liebeck_page_1998]: https://doi.org/10.2514/6.1998-438
[research_liebst_chapa_2002]: https://doi.org/10.2514/2.4941
[research_liebst_nolan_1993]: https://doi.org/10.2514/6.1993-3662
[research_liersch_bishop_2018]: https://doi.org/10.2514/6.2018-2839
[research_lijewski_1987]: https://doi.org/10.2514/6.1987-2273
[research_lim_hur_2025]: https://doi.org/10.9766/kimst.2025.28.1.092
[research_limache_cliff_1999]: https://doi.org/10.2514/6.1999-4313
[research_lin_hsu_2004]: https://doi.org/10.1109/tfuzz.2004.834803
[research_lin_lee_2023]: https://doi.org/10.1061/jaeeez.aseng-5054
[research_lin_wang_2017]: https://doi.org/10.23919/chicc.2017.8028365
[research_lin_zhang_2019]: https://doi.org/10.23919/chicc.2019.8865352
[research_lin_zong_2026]: https://doi.org/10.1063/5.0334699
[research_lina_ricker_1952]: https://ntrs.nasa.gov/citations/19930083537
[research_lindley_1956]: https://doi.org/10.1214/aoms/1177728069
[research_lindsay_2021]: https://doi.org/10.32920/ryerson.14643990
[research_lindsey_1946]: https://ntrs.nasa.gov/citations/19930092792
[research_linear_quadratic_2026]: https://doi.org/10.1017/9781009399913.016
[research_lingyu_youwu_2006]: https://doi.org/10.1109/chicc.2006.4347425
[research_lipeng_qinweiwei_2009]: https://doi.org/10.1109/icma.2009.5244811
[research_lisoski_kendall_2007]: https://ntrs.nasa.gov/citations/20080009492
[research_liu_2022]: https://doi.org/10.1007/978-981-19-4586-1_13
[research_liu_2024]: https://doi.org/10.1088/1742-6596/2691/1/012030
[research_liu_elham_2019]: https://doi.org/10.2514/6.2019-0258
[research_liu_flying_wing_aero_2026]: https://doi.org/10.1016/j.ast.2026.112709
[research_liu_gao_2010]: https://doi.org/10.1109/icsps.2010.5555726
[research_liu_hu_2014]: https://doi.org/10.2514/6.2014-3015
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_lone_2013]: https://doi.org/10.2514/6.2013-4605
[research_liu_luo_2021]: https://doi.org/10.3390/app11041555
[research_liu_lyu_2026]: https://doi.org/10.1109/tiv.2023.3337863
[research_liu_wang_2012]: https://doi.org/10.2991/iccasm.2012.300
[research_liu_wang_2016]: https://doi.org/10.2514/6.2016-4386
[research_liu_wang_2022]: https://doi.org/10.23919/ccc55666.2022.9902299
[research_liu_wang_2025]: https://doi.org/10.1088/1742-6596/2977/1/012038
[research_liu_weng_2007]: https://doi.org/10.1007/978-3-540-75995-9_87
[research_liu_whidborne_2021]: https://doi.org/10.1016/j.neucom.2021.08.069
[research_liu_zhang_2005]: https://doi.org/10.2514/6.2005-4724
[research_liu_zhang_2006]: https://doi.org/10.2514/1.18554
[research_liu_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9019008
[research_liu_zhang_2023]: https://doi.org/10.1002/aisy.202300420
[research_liu_zhang_rudder_2022]: https://doi.org/10.3390/aerospace9020079
[research_lock_rogers_1962]: https://doi.org/10.1016/b978-0-08-006550-2.50020-x
[research_lockwood_1966]: https://ntrs.nasa.gov/citations/19660023730
[research_lockwood_1974]: https://ntrs.nasa.gov/citations/19740012539
[research_loechert_huber_2018]: https://doi.org/10.2514/6.2018-3329
[research_loeser_rohlf_2016]: https://doi.org/10.1007/978-3-319-27279-5_57
[research_lokos_lizotte_2005]: https://doi.org/10.2514/6.2005-6315
[research_lomax_bailey_1973]: https://ntrs.nasa.gov/citations/19730019157
[research_lombardi_salvetti_1997]: https://doi.org/10.2514/6.1997-1838
[research_long_1968]: https://doi.org/10.2514/6.1968-264
[research_longitudinal_aircraft_2011]: https://doi.org/10.1109/mcs.2011.941250
[research_longitudinal_control_2003]: https://doi.org/10.2514/5.9781600861840.0275.0284
[research_longitudinal_dynamics_1990]: https://doi.org/10.1515/9781400855988.296
[research_longitudinal_dynamics_1998]: https://doi.org/10.2514/5.9781600862052.0165.0206
[research_longitudinal_maneuvering_2003]: https://doi.org/10.2514/5.9781600861840.0255.0264
[research_longitudinal_stability_2014]: https://doi.org/10.5040/9781472987563.ch-004
[research_longitudinal_stability_2021]: https://doi.org/10.1002/9781118949818.ch14
[research_longitudinal_trim_2016]: https://doi.org/10.1201/b15956-7
[research_longlu_turkoglu_2015]: https://doi.org/10.1109/aero.2015.7118952
[research_lopez_buell_1959]: https://ntrs.nasa.gov/citations/19980228044
[research_loranchet_tiako_2025]: https://doi.org/10.2514/6.2025-98091
[research_lorber_carta_1988]: https://doi.org/10.2514/3.45621
[research_lorber_covino_1991]: https://doi.org/10.2514/6.1991-1795
[research_lorenzetti_nelsen_1969]: https://doi.org/10.2514/3.44042
[research_lottati_1986]: https://doi.org/10.2514/3.45350
[research_lotze_sensburg_1975]: https://doi.org/10.2514/6.1975-1025
[research_lowenberg_2010]: https://doi.org/10.1002/9780470686652.eae255
[research_lowry_schneiter_1948]: https://ntrs.nasa.gov/citations/19930082306
[research_lu]: https://doi.org/10.31979/etd.4ys8-zqt7
[research_lu_jump_2014]: https://doi.org/10.2514/1.g000079
[research_lu_lan_2026]: https://doi.org/10.1109/ccdc69976.2026.11560122
[research_lu_ma_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_turkoglu_2016]: https://doi.org/10.2514/6.2016-1624
[research_lu_turkoglu_2018]: https://doi.org/10.1155/2018/8654031
[research_lu_vankampen_2015]: https://doi.org/10.2514/6.2015-0859
[research_luattnguyen_williampgilbert_1980]: https://ntrs.nasa.gov/citations/19800020743
[research_luckring_2003]: https://doi.org/10.2514/6.2003-753
[research_luckring_hiller_2025]: https://doi.org/10.2514/6.2025-2018
[research_luckybose_isfaqahmedrafsun_2024]: https://doi.org/10.30574/wjarr.2024.23.3.2961
[research_lundstrom_1949]: https://ntrs.nasa.gov/citations/19650074057
[research_lungu_flores_2022]: https://doi.org/10.1109/codit55151.2022.9803999
[research_luo_lan_1993]: https://doi.org/10.2514/3.20993
[research_luo_wang_1998]: https://doi.org/10.2514/2.2257
[research_luoma_1953]: https://ntrs.nasa.gov/citations/20050029467
[research_lusardi_blanken_2012]: https://ntrs.nasa.gov/citations/20120011852
[research_lutze_1980]: https://doi.org/10.2514/6.1980-309
[research_lutze_durham_1993]: https://doi.org/10.2514/6.1993-3650
[research_lutze_fan_1998]: https://doi.org/10.2514/6.1998-4457
[research_luu_2025]: https://doi.org/10.32920/29170238
[research_luu_ochi_2023]: https://doi.org/10.2322/tastj.21.1
[research_ly_1984]: https://doi.org/10.2514/6.1984-1911
[research_lykins_keshmiri_2010]: https://doi.org/10.2514/6.2010-7648
[research_lyu_zhang_2023]: https://doi.org/10.1016/j.ast.2023.108384
[research_m_2026]: https://doi.org/10.36227/techrxiv.176827253.34525913/v1
[research_ma_alwi_2025]: https://doi.org/10.1109/systol66549.2025.11267295
[research_ma_deng_2016]: https://doi.org/10.1016/j.cja.2016.08.004
[research_ma_huang_2019]: https://doi.org/10.1007/978-981-13-3305-7_124
[research_ma_li_2008]: https://doi.org/10.1109/isscaa.2008.4776304
[research_ma_wang_2009]: https://doi.org/10.2514/6.2009-55
[research_ma_zhu_2019]: https://doi.org/10.3390/app9204236
[research_macdonald_1984]: https://doi.org/10.2514/6.1984-561
[research_mace_cosner_1983]: https://doi.org/10.2514/6.1983-1366
[research_mack_1979]: https://doi.org/10.2514/6.1979-264
[research_maggin_1944]: https://ntrs.nasa.gov/citations/19930092727
[research_magill_darden_1994]: https://doi.org/10.2514/6.1994-3457
[research_magness_robinson_1992]: https://ntrs.nasa.gov/citations/19940030465
[research_mahmood_2025]: https://doi.org/10.1080/00207721.2025.2568091
[research_mahmood_aasim_2025]: https://doi.org/10.1109/aset66891.2025.11428017
[research_maimako_mintah_2026]: https://doi.org/10.2139/ssrn.7115964
[research_maine_1977]: https://doi.org/10.2514/6.1977-1135
[research_maine_1978]: https://ntrs.nasa.gov/citations/19780025111
[research_maine_iliff_1979]: https://doi.org/10.2514/3.58588
[research_maine_iliff_1982]: https://doi.org/10.2514/6.1982-1318
[research_malaek_karimi_2008]: https://doi.org/10.2514/1.29372
[research_malaek_sajjadikia_2004]: https://doi.org/10.2514/6.2004-5363
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malcom_husband_1976]: https://doi.org/10.2514/6.1976-1912
[research_malik_li_1993]: https://doi.org/10.2514/6.1993-77
[research_malik_ricci_2020]: https://doi.org/10.1007/s13272-020-00459-6
[research_malmuth_wu_1983]: https://doi.org/10.2514/6.1983-184
[research_malpica_lusardi_2013]: https://doi.org/10.21236/ada589936
[research_mamada_ando_1973]: https://doi.org/10.2514/3.60279
[research_mamada_ando_1974]: https://doi.org/10.2514/3.59236
[research_mamla_galinski_2009]: https://doi.org/10.2514/1.42084
[research_mandal]: https://doi.org/10.33915/etd.6152
[research_mandal_gu_2016]: https://doi.org/10.3390/aerospace3040042
[research_maneuvering_stability_2003]: https://doi.org/10.2514/5.9781600861840.0265.0274
[research_mann_huffman_1987]: https://ntrs.nasa.gov/citations/19870017441
[research_mann_mercer_1985]: https://doi.org/10.2514/6.1985-4069
[research_manning_gleason_1992]: https://doi.org/10.2514/6.1992-4425
[research_mansor_nogoud_2015]: https://doi.org/10.1109/iccneee.2015.7381444
[research_mansour_1984]: https://doi.org/10.2514/6.1984-522
[research_mansour_1985]: https://doi.org/10.2514/3.9056
[research_maqsood_go_2011]: https://doi.org/10.1007/s11071-011-0300-3
[research_marchetti_1968]: https://doi.org/10.2514/3.43902
[research_mariaagneta_stef_2011]: https://doi.org/10.5772/14936
[research_maricic_2006]: https://doi.org/10.2298/tam0604311m
[research_marilyneogburn_johnvfoster_1991]: https://ntrs.nasa.gov/citations/19910063214
[research_marino_mastrocola_1948]: https://ntrs.nasa.gov/citations/19930085769
[research_marino_mastrocola_1952]: https://ntrs.nasa.gov/citations/19930083049
[research_marion_sharma_2025]: https://doi.org/10.2514/6.2025-97857
[research_markofski_bailey_1999]: https://doi.org/10.2514/6.1999-4005
[research_marques_2013]: https://doi.org/10.14323/ijuseng.2013.5
[research_marschalk_luteijn_2021]: https://doi.org/10.2514/6.2021-0286
[research_martin_2007]: https://doi.org/10.21236/ada473149
[research_martin_2008]: https://doi.org/10.2514/6.2008-7337
[research_martinez_1961]: https://doi.org/10.21236/ad0265941
[research_martinezgarcia_gordon_2017]: https://doi.org/10.1109/access.2017.2778013
[research_martos_kiszely_2011]: https://doi.org/10.2514/6.2011-6669
[research_martz_biezad_1987]: https://doi.org/10.2514/6.1987-2536
[research_martz_biezad_1988]: https://doi.org/10.2514/3.20350
[research_marwaha_valasek_2008]: https://doi.org/10.2514/6.2008-6895
[research_marx_1977]: https://doi.org/10.2514/6.1977-1440
[research_marzouk_2025]: https://doi.org/10.20944/preprints202506.1467.v1
[research_masaoka_hashimoto_2024]: https://doi.org/10.1109/icrca60878.2024.10649279
[research_masini_timme_2019]: https://doi.org/10.1017/jfm.2019.906
[research_masini_timme_2020]: https://doi.org/10.2514/1.j059219
[research_mason_1953]: https://ntrs.nasa.gov/citations/20050041783
[research_mason_1982]: https://doi.org/10.2514/6.1982-97
[research_massey_kandil_1998]: https://doi.org/10.2514/6.1998-762
[research_mastin_smith_1996]: https://doi.org/10.2514/6.1996-2416
[research_matamoros_devisser_2018]: https://doi.org/10.2514/6.2018-1116
[research_mateju_2019]: https://doi.org/10.13164/conf.read.2018.13
[research_matheny_gatlin_1978]: https://ntrs.nasa.gov/citations/19780012197
[research_matranga_1961]: https://ntrs.nasa.gov/citations/19980227282
[research_matranga_1961_b]: https://ntrs.nasa.gov/citations/20040047146
[research_matranga_armstrong_1959]: https://ntrs.nasa.gov/citations/19980235626
[research_matranga_menard_1959]: https://ntrs.nasa.gov/citations/19630004018
[research_matsuno_nakamura_2000]: https://doi.org/10.2514/6.2000-655
[research_matsuno_yokouchi_2003]: https://doi.org/10.2514/6.2003-738
[research_maughmer_ozoroski_1990]: https://ntrs.nasa.gov/citations/19900012419
[research_mavriplis_levy_2002]: https://doi.org/10.2514/6.2002-838
[research_mayer_lutz_2019]: https://doi.org/10.2514/1.c034969
[research_mayes_lores_1970]: https://doi.org/10.2514/3.44207
[research_mayya_karnick_2022]: https://doi.org/10.2514/6.2022-4173
[research_mazumder_2024]: https://doi.org/10.21203/rs.3.rs-4706004/v1
[research_mccarley_lindak_2016]: https://doi.org/10.2514/6.2016-3359
[research_mccarty_1982]: https://ntrs.nasa.gov/citations/19820058689
[research_mcclelland_woolsey_2020]: https://doi.org/10.2514/1.g004224
[research_mccracken_jorris_2011]: https://doi.org/10.2514/6.2011-6444
[research_mccuish_caldwell_2018]: https://doi.org/10.1201/9781315136820-12
[research_mcfall_1954]: https://ntrs.nasa.gov/citations/19930087765
[research_mcfall_hollinger_1953]: https://ntrs.nasa.gov/citations/19930087467
[research_mcfarlane_richardson_2008]: https://doi.org/10.2514/6.2008-7156
[research_mckay_1994]: https://doi.org/10.2514/6.1994-3668
[research_mckeehen_1998]: https://doi.org/10.2514/6.1998-4159
[research_mckeehen_myatt_1997]: https://doi.org/10.2514/6.1997-3790
[research_mckelvey_1993]: https://doi.org/10.1016/b978-0-08-041898-8.50009-8
[research_mckenzie_1973]: https://doi.org/10.2514/6.1973-782
[research_mckinney_1946]: https://ntrs.nasa.gov/citations/19930081718
[research_mckinney_1946_b]: https://ntrs.nasa.gov/citations/19930092558
[research_mckinney_shanks_1948]: https://ntrs.nasa.gov/citations/19930082275
[research_mcklnney_dollyhlgh_1971]: https://doi.org/10.2514/3.59148
[research_mclean_1994]: https://doi.org/10.1049/cp:19940361
[research_mclemore_peterson_1960]: https://ntrs.nasa.gov/citations/19980228270
[research_mcmaster_schenk_1973]: https://doi.org/10.2514/6.1973-822
[research_mcneill_mclean_1961]: https://ntrs.nasa.gov/citations/20040008111
[research_mcruer_1965]: https://doi.org/10.21236/ad0470337
[research_mcruer_1995]: https://ntrs.nasa.gov/citations/19960020960
[research_measuring_airspeed_2021]: https://doi.org/10.2514/5.9781624105920.0039.0066
[research_meckstroth_blake_2015]: https://doi.org/10.2514/6.2015-2324
[research_meckstroth_ordonez_2020]: https://doi.org/10.2514/6.2020-3178
[research_meckstroth_ordonez_2020_b]: https://doi.org/10.2514/6.2020-3177
[research_medina_rockwood_2019]: https://doi.org/10.2514/6.2019-2324
[research_medved_1990]: https://doi.org/10.2514/6.1990-1417
[research_meheut_arntz_2012]: https://doi.org/10.2514/6.2012-3122
[research_mehra_stepner_1972]: https://ntrs.nasa.gov/citations/19720054594
[research_mehra_stepner_1974]: https://doi.org/10.2514/3.60327
[research_meijer_cunningham_1992]: https://doi.org/10.2514/6.1992-4501
[research_memon_altman_2016]: https://doi.org/10.2514/6.2016-1847
[research_meng_jia_2007]: https://doi.org/10.2514/6.2007-1272
[research_mengali_2003]: https://doi.org/10.2514/2.g6330tc
[research_mennell_1976]: https://ntrs.nasa.gov/citations/19760023185
[research_menshchikov_somov_2019]: https://doi.org/10.1063/1.5086976
[research_menzies_1996]: https://ntrs.nasa.gov/citations/19970017825
[research_menzies_kandil_1995]: https://doi.org/10.2514/6.1995-1771
[research_menzies_kandil_1996]: https://doi.org/10.2514/6.1996-3391
[research_mercer_maiden_1972]: https://ntrs.nasa.gov/citations/19720022360
[research_merceruio]: https://doi.org/10.33915/etd.291
[research_mertens_klevenhusen_1986]: https://doi.org/10.2514/6.1986-512
[research_mertins_elsholz_2005]: https://doi.org/10.1016/j.ast.2005.06.003
[research_metcalf_1936]: https://doi.org/10.2514/8.322
[research_methods_for_2003]: https://doi.org/10.2514/5.9781600861840.0285.0296
[research_metodiev_2024]: https://doi.org/10.3897/arb.v36.e10
[research_meyer_1983]: https://doi.org/10.2514/6.1983-2071
[research_meyer_husband_1990]: https://doi.org/10.2514/6.1990-2847
[research_meyer_yip_1989]: https://ntrs.nasa.gov/citations/19890060320
[research_mialon_khrabov_2010]: https://doi.org/10.2514/6.2010-8244
[research_michal_1998]: https://ntrs.nasa.gov/citations/19980137606
[research_midhat_2017]: https://doi.org/10.30684/etj.35.5a.6
[research_midmer_bruecker_2024]: https://doi.org/10.2514/6.2024-4474
[research_miklosovic_imber_2012]: https://doi.org/10.2514/6.2012-2893
[research_miklosovic_perry_2014]: https://doi.org/10.2514/6.2014-2796
[research_milenkovicbabic_2018]: https://doi.org/10.1108/aeat-04-2017-0104
[research_milenkovicbabic_ivkovic_2024]: https://doi.org/10.5937/fme2404556m
[research_milenkovicbabic_samardzic_2017]: https://doi.org/10.1108/aeat-02-2016-0026
[research_miles_1952]: https://doi.org/10.2514/8.2188
[research_milholen_chokani_1994]: https://doi.org/10.2514/3.46593
[research_miller_1969]: https://doi.org/10.2514/6.1969-897
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1983]: https://doi.org/10.2514/6.1983-2482
[research_miller_forster_2025]: https://doi.org/10.2514/6.2025-1271
[research_miller_franklin_1968]: https://doi.org/10.2514/3.43919
[research_milne_martos_2012]: https://doi.org/10.2514/6.2012-2855
[research_minghang_hu_2014]: https://doi.org/10.2514/6.2014-0555
[research_mingzhou_guoping_2016]: https://doi.org/10.1016/j.conengprac.2016.03.007
[research_mirels_1953]: https://doi.org/10.2514/8.2735
[research_mistry_page_2013]: https://doi.org/10.2514/6.2013-2842
[research_mitcham_1949]: https://ntrs.nasa.gov/citations/20010062502
[research_mitcham_blanchard_1950]: https://ntrs.nasa.gov/citations/20050019416
[research_mitcham_blanchard_1951]: https://ntrs.nasa.gov/citations/20050030030
[research_mitcham_blanchard_1952]: https://ntrs.nasa.gov/citations/20050029440
[research_mitchell_2000]: https://doi.org/10.2514/6.2000-3985
[research_mitchell_aponso_1992]: https://ntrs.nasa.gov/citations/19920019341
[research_mitchell_aponso_1995]: https://doi.org/10.2514/6.1995-3425
[research_mitchell_doman_2003]: https://doi.org/10.21236/ada417898
[research_mitchell_hoh_1982]: https://doi.org/10.2514/6.1982-1356
[research_mitchell_hoh_1984]: https://doi.org/10.2514/3.8551
[research_mitchell_kish]: https://doi.org/10.1109/aero.1998.685777
[research_mitchell_klyde_2008]: https://doi.org/10.2514/1.31470
[research_mitchell_peck_1950]: https://ntrs.nasa.gov/citations/20090023623
[research_mitikiri_mohseni_2018]: https://doi.org/10.2514/6.2018-0876
[research_mitiku_salau_2024]: https://doi.org/10.1002/adc2.224
[research_miyaji_2022]: https://doi.org/10.1299/jfst.2022jfst0004
[research_mizoguchi_kajikawa_2014]: https://doi.org/10.2514/6.2014-2014
[research_modeling_and_2015]: https://doi.org/10.1007/978-3-319-10792-9
[research_modern_aircraft_1988]: https://doi.org/10.1007/bfb0043099
[research_moennich_dalldorff_1993]: https://doi.org/10.2514/6.1993-3668
[research_moes_noffz_2000]: https://ntrs.nasa.gov/citations/20010002099
[research_moes_smith_2003]: https://ntrs.nasa.gov/citations/20030107571
[research_moes_smith_2006]: https://ntrs.nasa.gov/citations/20110012932
[research_mohamed_abdelhady_2021]: https://doi.org/10.1007/s00348-021-03282-9
[research_mohamed_abdullah_2026]: https://doi.org/10.21203/rs.3.rs-8464285/v1
[research_mohamed_dongare_2021]: https://doi.org/10.1007/978-981-16-0104-0_4
[research_mohamed_dongare_2021_b]: https://doi.org/10.1007/978-981-16-0104-0_3
[research_mohamed_dongare_2021_c]: https://doi.org/10.1007/978-981-16-0104-0_1
[research_mohamed_nadarajah_2009]: https://doi.org/10.2514/1.40685
[research_mohamed_nadarajah_2009_b]: https://doi.org/10.2514/6.2009-50
[research_mohammed_2007]: https://doi.org/10.30684/etj.25.6.5
[research_mohammed_2015]: https://doi.org/10.13111/2066-8201.2015.7.2.10
[research_mohammed_wu_2013]: https://doi.org/10.4028/www.scientific.net/amm.0.753
[research_mohan_kumar_2023]: https://doi.org/10.61653/joast.v75i1.2023.14
[research_mohanty_swain_2025]: https://doi.org/10.21203/rs.3.rs-8327022/v1
[research_mohdnasir_2026]: https://doi.org/10.24191/jmeche.v23i3.11599
[research_moitra_1985]: https://doi.org/10.2514/6.1985-123
[research_molinari_arrieta_2015]: https://doi.org/10.1117/12.2179176
[research_molinari_arrieta_2018]: https://doi.org/10.1177/1045389x18798952
[research_molland_turnock_2007]: https://doi.org/10.1016/b978-075066944-3/50010-x
[research_molland_turnock_2022]: https://doi.org/10.1016/b978-0-12-824378-7.00003-2
[research_molton_dandois_2013]: https://doi.org/10.2514/1.j051000
[research_monaghan_1978]: https://ntrs.nasa.gov/citations/19780015113
[research_monaghan_friend_1973]: https://ntrs.nasa.gov/citations/19730019173
[research_monahemi_barlow_1995]: https://doi.org/10.2514/6.1995-3344
[research_montano_dimino_2024]: https://doi.org/10.3390/aerospace11040266
[research_montgomery_1971]: https://doi.org/10.2514/6.1971-955
[research_montgomery_hunsaker_2022]: https://doi.org/10.2514/6.2022-2531
[research_montgomery_price_1974]: https://doi.org/10.2514/6.1974-887
[research_mooij_1985]: https://doi.org/10.1007/978-94-017-1193-7_5
[research_mooij_1985_b]: https://doi.org/10.1007/978-94-017-1193-7_6
[research_mooij_1985_c]: https://doi.org/10.1007/978-94-017-1193-7_2
[research_mooij_1985_d]: https://doi.org/10.1007/978-94-017-1193-7
[research_mooij_1985_e]: https://doi.org/10.1007/978-94-017-1193-7_3
[research_mooij_1985_f]: https://doi.org/10.1007/978-94-017-1193-7_4
[research_moore_1957]: https://ntrs.nasa.gov/citations/19930089773
[research_moore_frei_1983]: https://doi.org/10.2514/6.1983-1834
[research_moore_moore_2008]: https://doi.org/10.2514/6.2008-215
[research_moore_pullin_1995]: https://doi.org/10.1017/s0022112095004642
[research_moore_rahimi_2024]: https://doi.org/10.1504/ijvd.2024.137837
[research_moorhouse_1979]: https://doi.org/10.2514/6.1979-402
[research_moorhouse_1990]: https://doi.org/10.2514/6.1990-2849
[research_moorhouse_1995]: https://doi.org/10.2514/6.1995-3426
[research_moorhouse_fielding_1998]: https://doi.org/10.2514/6.1998-4568
[research_moorhouse_jenkins_1975]: https://doi.org/10.2514/3.44474
[research_moorthamers_wiberg_2021]: https://doi.org/10.2514/6.2021-1825
[research_moosavi_2025]: https://doi.org/10.2514/1.j065155
[research_moreines_sellite_1965]: https://doi.org/10.4271/650570
[research_moreira_gripp_2022]: https://doi.org/10.2514/1.g006443
[research_morelli_2000]: https://doi.org/10.2514/6.2000-3902
[research_morelli_2002]: https://doi.org/10.2514/6.2002-4704
[research_morelli_2021]: https://doi.org/10.1007/s10957-021-01912-0
[research_morelli_2021_b]: https://doi.org/10.2514/6.2021-2795
[research_morelli_grauer_2018]: https://doi.org/10.2514/6.2018-3477
[research_mori_yakeno_2024]: https://doi.org/10.2514/6.2024-4486
[research_morra_nicolosi_2025]: https://doi.org/10.2514/6.2025-3424
[research_morris_1966]: https://doi.org/10.2514/6.1966-770
[research_morris_1992]: https://doi.org/10.2514/6.1992-4604
[research_morris_allison_2012]: https://doi.org/10.2514/6.2012-4850
[research_morris_allison_2014]: https://doi.org/10.2514/1.c032340
[research_morris_sultan_2013]: https://doi.org/10.2514/6.2013-4927
[research_morris_tigner_1995]: https://doi.org/10.2514/6.1995-3327
[research_morris_ward_1989]: https://doi.org/10.2514/6.1989-3349
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_morton_mitchell_2002]: https://doi.org/10.2514/6.2002-2968
[research_moseley_taylor_1953]: https://ntrs.nasa.gov/citations/19930087921
[research_moseley_taylor_1954]: https://ntrs.nasa.gov/citations/19930088001
[research_moseley_thompson_1957]: https://ntrs.nasa.gov/citations/19630004887
[research_moses_1997]: https://doi.org/10.1117/12.274700
[research_moses_ashley_1998]: https://ntrs.nasa.gov/citations/19980073173
[research_moses_huttsell_2000]: https://ntrs.nasa.gov/citations/20000052124
[research_moss_cole_1991]: https://doi.org/10.2514/6.1991-1049
[research_moszczynski_grant_2017]: https://doi.org/10.2514/6.2017-3893
[research_moulin_karpel_2007]: https://doi.org/10.2514/1.19876
[research_moulton_abraham_2024]: https://doi.org/10.2514/6.2024-2480
[research_muchamadbayusaktipratama_erwinsulaeman_2022]: https://doi.org/10.37934/cfdl.14.1.2037
[research_mudd_1969]: https://doi.org/10.1177/001872086901100403
[research_mulder_1985]: https://doi.org/10.1016/s1474-6670(17)60606-2
[research_mulder_1988]: https://doi.org/10.1016/s1474-6670(17)54913-7
[research_mulder_lubbers_2009]: https://doi.org/10.2514/6.2009-5692
[research_muller_1967]: https://doi.org/10.2514/3.59369
[research_mullins_tipton_1996]: https://doi.org/10.2514/6.1996-894
[research_multiloop_flight_1990]: https://doi.org/10.1515/9781400855988.600
[research_mungall_1946]: https://ntrs.nasa.gov/citations/20050019329
[research_munger_carlin_1983]: https://doi.org/10.2514/6.1983-2560
[research_munoz]: https://doi.org/10.11606/t.18.2009.tde-15052024-152026
[research_muralidharan_baron_1979]: https://doi.org/10.21236/ada069880
[research_murphy_klein_2008]: https://doi.org/10.2514/6.2008-6202
[research_murphy_klein_2010]: https://doi.org/10.2514/6.2010-8122
[research_murray_1949]: https://doi.org/10.1108/eb031761
[research_murray_giannellis_2020]: https://doi.org/10.2514/6.2020-1987
[research_murri_croom_1983]: https://doi.org/10.2514/6.1983-1837
[research_murri_nguyen_1984]: https://ntrs.nasa.gov/citations/19840009116
[research_musa_mansor_2015]: https://doi.org/10.2514/6.2015-1498
[research_musa_mansor_2026]: https://doi.org/10.2139/ssrn.7319830
[research_muzzey_kidd_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50020-x
[research_myala_borra_2019]: https://doi.org/10.1109/i-pact44901.2019.8960152
[research_myatt_jenkins_1996]: https://doi.org/10.2514/6.1996-3406
[research_myatt_myatt_1997]: https://doi.org/10.2514/6.1997-3646
[research_myatt_schumacher_1998]: https://doi.org/10.2514/6.1998-4455
[research_myers_johnston_1983]: https://ntrs.nasa.gov/citations/19840006090
[research_myers_mcruer_1982]: https://doi.org/10.2514/6.1982-1608
[research_myers_walsh_1988]: https://doi.org/10.2514/6.1988-2175
[research_nabdulwahab_2009]: https://doi.org/10.30684/etj.27.7.11
[research_naca_1135]: https://ntrs.nasa.gov/citations/19930091059
[research_naca_conference_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_nagabhushan_lutze_1983]: https://doi.org/10.2514/6.1983-279
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_nahomjidovetski_raveh_2025]: https://doi.org/10.2514/6.2025-0624
[research_naigle_hiltner_2022]: https://doi.org/10.2514/6.2022-2326
[research_nallapula_schade_2012]: https://doi.org/10.2514/6.2012-3142
[research_nangia_palmer_2002]: https://doi.org/10.2514/6.2002-4616
[research_nangia_palmer_2003]: https://doi.org/10.2514/6.2003-605
[research_napolitano_kincheloe_1996]: https://doi.org/10.2514/6.1996-3851
[research_napolitano_paris_1996]: https://doi.org/10.2514/6.1996-3420
[research_napolitano_spagnuolo_1993]: https://ntrs.nasa.gov/citations/19940020331
[research_napolitano_swaim_1989]: https://doi.org/10.2514/6.1989-3425
[research_narayanan_kumar_2026]: https://doi.org/10.1051/e3sconf/202669202008
[research_nardi_1970]: https://doi.org/10.2514/6.1970-515
[research_nardi_kawana_1976]: https://ntrs.nasa.gov/citations/19760013737
[research_nasa_advanced_1993]: https://ntrs.nasa.gov/citations/19940020116
[research_nash_timme_2025]: https://doi.org/10.2514/6.2025-3767
[research_nasir_kuntjoro_2012]: https://doi.org/10.4028/www.scientific.net/amm.225.375
[research_nasir_kuntjoro_2013]: https://doi.org/10.4028/www.scientific.net/amm.393.329
[research_nasir_kuntjoro_2014]: https://doi.org/10.1016/j.protcy.2014.09.051
[research_natesan_bhat_2005]: https://doi.org/10.2514/6.2005-6406
[research_navert_sedin_1992]: https://doi.org/10.1007/978-3-663-09834-8_43
[research_nayfeh_elzebda_1989]: https://doi.org/10.2514/3.45844
[research_neal_smith_1970]: https://doi.org/10.2514/6.1970-927
[research_neal_smith_1971]: https://doi.org/10.2514/3.59174
[research_neely_griner_1959]: https://ntrs.nasa.gov/citations/19980223625
[research_neighbor_wiler_1978]: https://doi.org/10.2514/6.1978-1271
[research_nelson]: https://doi.org/10.1109/plans.1992.185868
[research_nelson_arena_1991]: https://ntrs.nasa.gov/citations/19920009538
[research_nelson_arena_1993]: https://doi.org/10.1007/978-3-642-52460-8_29
[research_nelson_durham_2002]: https://doi.org/10.2514/6.2002-4498
[research_ness_1971]: https://doi.org/10.2514/3.44301
[research_neumark_1950]: https://doi.org/10.1108/eb031964
[research_neves_mariani_2024]: https://doi.org/10.2514/6.2024-0140
[research_newell_campbell_1954]: https://doi.org/10.21236/ad0092495
[research_newell_dolbin_1963]: https://doi.org/10.21236/ad0425705
[research_newey]: https://doi.org/10.15368/theses.2020.107
[research_newman_buttrill_1995]: https://doi.org/10.2514/6.1995-3250
[research_newton_2025]: https://doi.org/10.2514/6.2025-2350
[research_newton_kroo_2023]: https://doi.org/10.2514/6.2023-3319
[research_newton_kroo_2024]: https://doi.org/10.2514/6.2024-4581
[research_newton_kroo_2025]: https://doi.org/10.2514/1.g008400
[research_ng_malcolm_1989]: https://ntrs.nasa.gov/citations/19890060277
[research_ng_malcolm_1990]: https://doi.org/10.2514/6.1990-3080
[research_ng_malcolm_1992]: https://ntrs.nasa.gov/citations/19920064163
[research_ng_ong_1991]: https://ntrs.nasa.gov/citations/19910069122
[research_ng_skaff_1993]: https://doi.org/10.2514/6.1993-3492
[research_ng_skaff_1994]: https://doi.org/10.2514/3.46674
[research_ngo_reigelsperger]: https://doi.org/10.1109/cca.1996.558615
[research_ngo_reigelsperger_1996]: https://doi.org/10.2514/6.1996-3866
[research_nguyen_1974]: https://ntrs.nasa.gov/citations/19740025338
[research_nguyen_cord_1997]: https://doi.org/10.2514/6.1997-3730
[research_nguyen_cord_1999]: https://doi.org/10.2514/6.1999-4004
[research_nguyen_fugate_2019]: https://doi.org/10.2514/6.2019-0217
[research_nguyen_krishnakumar_2006]: https://ntrs.nasa.gov/citations/20060053343
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005197
[research_nguyen_saturation_pio_2021]: https://doi.org/10.2514/1.g005840
[research_nguyen_stepanyan_2010]: https://doi.org/10.2514/6.2010-3471
[research_nguyen_ting_2017]: https://doi.org/10.2514/6.2017-4219
[research_nguyen_whipple_1985]: https://ntrs.nasa.gov/citations/19860017780
[research_nguyen_xiong_2021]: https://doi.org/10.2514/6.2021-2574
[research_nguyen_xiong_2022]: https://doi.org/10.2514/6.2022-1325
[research_nguyen_xiong_2023]: https://doi.org/10.2514/6.2023-0998
[research_nguyen_xiong_2025]: https://doi.org/10.2514/6.2025-2184
[research_nguyen_xiong_2026]: https://doi.org/10.2514/6.2026-2315
[research_nguyen_yip_1981]: https://doi.org/10.2514/6.1981-1883
[research_nhannguyen_juntaoxiong_b]: https://ntrs.nasa.gov/citations/20230000002
[research_nicholas_naville_1984]: https://ntrs.nasa.gov/citations/19840062226
[research_nicolosi_demarco_2010]: https://doi.org/10.2514/6.2010-7947
[research_nicolosi_demarco_2013]: https://doi.org/10.1016/j.ast.2011.11.011
[research_nie_liu_2020]: https://doi.org/10.1109/access.2020.3001913
[research_nie_liu_2021]: https://doi.org/10.3390/app11041407
[research_nie_zhang_2026]: https://doi.org/10.1063/5.0343289
[research_nie_zhang_2026_b]: https://doi.org/10.2514/1.j066341
[research_nielsen_1953]: https://ntrs.nasa.gov/citations/19930093732
[research_niestroy_2025]: https://doi.org/10.2514/6.2025-1636
[research_niestroy_dorsett_2017]: https://doi.org/10.2514/6.2017-1757
[research_niestroy_williams_2019]: https://doi.org/10.2514/6.2019-0279
[research_nietowire_sobel_2007]: https://doi.org/10.2514/6.2007-6417
[research_nietowire_sobel_2009]: https://doi.org/10.2514/6.2009-6306
[research_nietowire_sobel_2011]: https://doi.org/10.1155/2011/549131
[research_nietowire_sobel_2013]: https://doi.org/10.2514/6.2013-4778
[research_nietowire_sobel_2014]: https://doi.org/10.2514/1.g000036
[research_nikbay_yildiz_2025]: https://doi.org/10.2139/ssrn.5985995
[research_niranjana_rao_1993]: https://ntrs.nasa.gov/citations/19940020629
[research_nissen_1943]: https://ntrs.nasa.gov/citations/19930092866
[research_niu_yan_2023]: https://doi.org/10.1016/j.cja.2022.08.018
[research_nixon_1974]: https://doi.org/10.2514/3.60334
[research_nixon_2020]: https://doi.org/10.2514/6.2020-2729
[research_noll_calico_1983]: https://doi.org/10.2514/6.1983-2220
[research_nominal_aircraft]: https://doi.org/10.1007/bfb0043102
[research_nomura_2003]: https://doi.org/10.2514/6.2003-4145
[research_nonweiler_1960]: https://doi.org/10.1017/s0368393100072485
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_norton_1924]: https://ntrs.nasa.gov/citations/19930091236
[research_norton_carroll_1922]: https://ntrs.nasa.gov/citations/19930080802
[research_nugent_1959]: https://ntrs.nasa.gov/citations/19630004009
[research_nurohman_arifianto_2018]: https://doi.org/10.1088/1742-6596/1005/1/012020
[research_nusrath_sarmah_2014]: https://doi.org/10.4271/2014-01-2168
[research_nuthi_subbarao_2014]: https://doi.org/10.2514/6.2014-0544
[research_nyquist_1928]: https://doi.org/10.1109/T-AIEE.1928.5055024
[research_obayashi_guruswamy_1994]: https://doi.org/10.2514/3.46541
[research_oblique_flying_wing_1989]: https://ntrs.nasa.gov/citations/19890015862
[research_obrien_takahashi_2024]: https://doi.org/10.2514/6.2024-2320
[research_obryan_glover_1979]: https://ntrs.nasa.gov/citations/19790063866
[research_odonnell_mohseni_2017]: https://doi.org/10.2514/6.2017-1270
[research_odonnell_mohseni_2019]: https://doi.org/10.2514/1.c034704
[research_oehman_suddath_1964]: https://ntrs.nasa.gov/citations/19650018213
[research_oertel_stank_1999]: https://doi.org/10.2514/6.1999-551
[research_oggioni_riboldi_2026]: https://doi.org/10.3390/engproc2026142017
[research_ogren_sotanski_1974]: https://doi.org/10.21236/ad0784134
[research_oguztasci_tumse_2022]: https://doi.org/10.1016/j.oceaneng.2022.112120
[research_ohara_1964]: https://doi.org/10.2514/6.1964-555
[research_ohira_kwak_2013]: https://doi.org/10.2514/6.2013-342
[research_ohmichi_ishida_2017]: https://doi.org/10.2514/6.2017-1436
[research_ohmichi_ishida_2018]: https://doi.org/10.2514/1.j056855
[research_okada_bando_1987]: https://doi.org/10.4271/872334
[research_okelly_1954]: https://ntrs.nasa.gov/citations/20090023309
[research_okelly_1955]: https://ntrs.nasa.gov/citations/20090023313
[research_oki_1960]: https://doi.org/10.1016/s1474-6670(17)70239-x
[research_okolo_dogan_2014]: https://doi.org/10.2514/6.2014-0543
[research_okonkwo_jemitola_2022]: https://doi.org/10.2139/ssrn.4297908
[research_olcott_sackel_1981]: https://ntrs.nasa.gov/citations/19820014369
[research_oliva_2000]: https://doi.org/10.2514/6.2000-4038
[research_olsen_1966]: https://doi.org/10.21236/ad0647369
[research_olsen_seegmiller_1992]: https://doi.org/10.2514/6.1992-402
[research_olsen_seegmiller_1993]: https://doi.org/10.2514/3.49105
[research_olson_mead_1950]: https://ntrs.nasa.gov/citations/19930086313
[research_olson_mead_1951]: https://ntrs.nasa.gov/citations/19930086476
[research_onstott_faulkner_1978]: https://doi.org/10.2514/3.55750
[research_orhan_subbarao_2021]: https://doi.org/10.2514/6.2021-0108
[research_ossmann_2015]: https://doi.org/10.2514/6.2015-1310
[research_osterhuber_hanel_2004]: https://doi.org/10.2514/6.2004-4751
[research_ostroff_1998]: https://ntrs.nasa.gov/citations/19980039322
[research_oswald_1932]: https://ntrs.nasa.gov/citations/19930091482
[research_owashi_tanaka_2017]: https://doi.org/10.1299/jsmermd.2017.1p2-e04
[research_owens_beeler_2019]: https://ntrs.nasa.gov/citations/20200002391
[research_owens_capone_2003]: https://ntrs.nasa.gov/citations/20030007921
[research_oyama_2021]: https://doi.org/10.32920/ryerson.14635701
[research_ozcan_tekyurt_2025]: https://doi.org/10.23919/iccas66577.2025.11301141
[research_ozer_2025]: https://doi.org/10.1109/access.2025.3648550
[research_p_arokkiaswamy_2019]: https://doi.org/10.2139/ssrn.3507300
[research_pabla_2021]: https://doi.org/10.32920/ryerson.14657811
[research_padua_preisigheviana_2025]: https://doi.org/10.2514/6.2025-3459
[research_page_gillette_1994]: https://doi.org/10.2514/6.1994-3491
[research_pahle_wichman_1996]: https://ntrs.nasa.gov/citations/19990064010
[research_painter_caw_1978]: https://ntrs.nasa.gov/citations/19790005843
[research_painter_sitterle_1972]: https://ntrs.nasa.gov/citations/19720018367
[research_pakmehr_gordon]: https://doi.org/10.1109/acc.2005.1470181
[research_pakmehr_gordon_2005]: https://doi.org/10.1115/imece2005-82196
[research_palazzo_spearman_1954]: https://ntrs.nasa.gov/citations/20090023310
[research_pambagjo_nakahashi_2001]: https://doi.org/10.2514/6.2001-129
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_panagiotou_antoniou_2022]: https://doi.org/10.1016/j.ast.2022.107467
[research_papa_stoliker_1988]: https://doi.org/10.2514/6.1988-2105
[research_papamoschou_mayoral_2014]: https://doi.org/10.1121/1.4899467
[research_paranjape_ananthkrishan_2005]: https://doi.org/10.2514/6.2005-5800
[research_paranjape_chung_2010]: https://doi.org/10.2514/6.2010-7633
[research_paranjape_chung_2011]: https://doi.org/10.1088/1748-3182/6/2/026005
[research_parello]: https://doi.org/10.70675/552ef228z4a56z4305z8fa7z20a49691720d
[research_paris]: https://doi.org/10.33915/etd.9553
[research_paris_alaverdi_1998]: https://doi.org/10.2514/6.1998-4450
[research_park_2017]: https://doi.org/10.5139/ijass.2017.18.2.344
[research_park_abla_1982]: https://doi.org/10.2514/6.1982-183
[research_park_abla_1983]: https://doi.org/10.2514/3.19811
[research_park_choi_2016]: https://doi.org/10.2514/6.2016-2024
[research_park_choi_2017]: https://doi.org/10.2514/1.c034052
[research_park_chung_2012]: https://doi.org/10.5139/jksas.2012.40.2.165
[research_park_jo_2016]: https://doi.org/10.2514/6.2016-4038
[research_park_jo_2017]: https://doi.org/10.2514/6.2017-1754
[research_park_lee_2001]: https://doi.org/10.2514/6.2001-4014
[research_park_ocheltree_2015]: https://doi.org/10.2514/6.2015-3387
[research_park_ohtsu_1998]: https://doi.org/10.1016/s1474-6670(17)38409-4
[research_park_rokhsaz_2003]: https://doi.org/10.2514/6.2003-4069
[research_parker_spain_1991]: https://doi.org/10.2514/6.1991-936
[research_parks_wingrove_1980]: https://ntrs.nasa.gov/citations/19820037228
[research_parrish_steinmetz_1972]: https://ntrs.nasa.gov/citations/19720023363
[research_pasley_rohling_1973]: https://doi.org/10.2514/6.1973-791
[research_patel_cao_2007]: https://doi.org/10.1109/acc.2007.4283114
[research_patel_cao_2007_b]: https://doi.org/10.2514/6.2007-6314
[research_patel_lefas_2026]: https://doi.org/10.2514/1.c038444
[research_patil_2004]: https://doi.org/10.2514/1.11482
[research_patil_hodges_1998]: https://doi.org/10.2514/6.1998-1955
[research_patil_hodges_2000]: https://doi.org/10.2514/6.2000-1627
[research_patterson_1984]: https://doi.org/10.2514/6.1984-2491
[research_pattinson_lowenberg_2013]: https://doi.org/10.2514/1.c032184
[research_paudel_2016]: https://doi.org/10.11648/j.ijmea.20160404.12
[research_paul_garrard_1997]: https://doi.org/10.2514/6.1997-3776
[research_paul_rein_2016]: https://doi.org/10.2514/6.2016-0799
[research_paul_rein_2017]: https://doi.org/10.2514/1.c034080
[research_paulo_paulp_2019]: https://doi.org/10.35840/2631-5009/7530
[research_paulson_1944]: https://ntrs.nasa.gov/citations/19930092549
[research_paulson_1948]: https://ntrs.nasa.gov/citations/20050030051
[research_paulson_kjelgaard_1982]: https://ntrs.nasa.gov/citations/19830001746
[research_paulus_wirth_2013]: https://doi.org/10.2514/6.2013-2908
[research_pavelka_tatum_1980]: https://doi.org/10.2514/6.1980-1620
[research_pavlenko_reslan_2022]: https://doi.org/10.34759/vst-2022-3-17-28
[research_pawlak_1994]: https://doi.org/10.2514/6.1994-2116
[research_paziresh_nikseresht_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000704
[research_peahl_kolkailah_1986]: https://ntrs.nasa.gov/citations/19860021266
[research_pearson_aiken_1944]: https://ntrs.nasa.gov/citations/19930091876
[research_pedreiro_rock_1996]: https://doi.org/10.2514/6.1996-773
[research_pedreiro_takahara_1998]: https://doi.org/10.2514/6.1998-4518
[research_pedreiro_takahara_1999]: https://doi.org/10.2514/2.2539
[research_pedro_tshabalala_2017]: https://doi.org/10.1109/ascc.2017.8287198
[research_pedro_tshabalala_2017_b]: https://doi.org/10.1016/j.ifacol.2017.12.033
[research_pei_huang_2025]: https://doi.org/10.1109/raiic65850.2025.11170302
[research_peigin_epstein_2006]: https://doi.org/10.2514/6.2006-3457
[research_pelletier_nelson_1994]: https://doi.org/10.2514/6.1994-1879
[research_pena_voulgaris_2001]: https://doi.org/10.1177/107754630100700805
[research_peng_wang_2014]: https://doi.org/10.4028/www.scientific.net/amr.1049-1050.953
[research_peng_xuefeng_2013]: https://doi.org/10.1109/cac.2013.6775713
[research_pengelley_wilson_1954]: https://doi.org/10.21236/ad0061591
[research_pepper_foster_1947]: https://ntrs.nasa.gov/citations/20050019467
[research_perez_liu_2006]: https://doi.org/10.5589/q06-004
[research_peristy_perez_2019]: https://doi.org/10.2514/6.2019-0583
[research_perkins_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50012-0
[research_perkins_jr_1977]: https://doi.org/10.21236/ada062275
[research_perraud_moens_2003]: https://doi.org/10.2514/6.2003-3796
[research_perry_1976]: https://ntrs.nasa.gov/citations/19760011057
[research_perry_1978]: https://ntrs.nasa.gov/citations/19780023100
[research_perry_miklosovic_2012]: https://doi.org/10.1115/imece2012-85266
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_peters_andrisani_1997]: https://doi.org/10.2514/6.1997-3701
[research_petersen_1979]: https://doi.org/10.2514/6.1979-1789
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_peterson_1961]: https://ntrs.nasa.gov/citations/19980227076
[research_peterson_2024]: https://doi.org/10.2514/6.2024-2873
[research_peterson_grant_2011]: https://doi.org/10.2514/6.2011-6542
[research_peterson_menees_1961]: https://ntrs.nasa.gov/citations/20040008079
[research_peterson_menees_1961_b]: https://ntrs.nasa.gov/citations/20040008213
[research_petre_ashley_1976]: https://doi.org/10.2514/3.58707
[research_petrenko_gasparovic_2025]: https://doi.org/10.35116/aa.2025.0002
[research_petrocchi_barakos_2023]: https://doi.org/10.2514/6.2023-2276
[research_petrocchi_barakos_2023_b]: https://doi.org/10.2514/6.2023-3527
[research_pettit_grandhi_2003]: https://doi.org/10.2514/2.7208
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfifer_danowsky_2016]: https://doi.org/10.2514/6.2016-1750
[research_pfnur_oppelt_2018]: https://doi.org/10.1007/s13272-018-0340-1
[research_phillips]: https://doi.org/10.33915/etd.3049
[research_phillips_1942]: https://ntrs.nasa.gov/citations/19930092603
[research_phillips_1942_b]: https://ntrs.nasa.gov/citations/20150015694
[research_phillips_1948]: https://ntrs.nasa.gov/citations/19930082293
[research_phillips_1988]: https://doi.org/10.2514/6.1988-751
[research_phillips_1989]: https://doi.org/10.2514/3.20432
[research_phillips_anderson_2002]: https://doi.org/10.2514/6.2002-830
[research_phillips_crane_1943]: https://ntrs.nasa.gov/citations/19930092867
[research_phillips_gururajan_2010]: https://doi.org/10.2514/6.2010-7948
[research_phillips_jentzsch_2019]: https://doi.org/10.2514/6.2019-0045
[research_phillips_shortperiod_1942]: https://ntrs.nasa.gov/citations/19930092630
[research_phillips_williams_1944]: https://ntrs.nasa.gov/citations/19930092587
[research_phunpeng_khaengkarn_2023]: https://doi.org/10.1109/ieecon56657.2023.10126642
[research_physics_assisted_reduced_order_2023]: https://doi.org/10.1063/5.0152127
[research_pi_control_1999]: https://doi.org/10.1109/acc.1999.786342
[research_pitch_down_dynamic_1994]: https://doi.org/10.2514/6.1994-535
[research_pitchup_control_1960]: https://ntrs.nasa.gov/citations/19980227095
[research_place_altmann_1974]: https://doi.org/10.21236/ad0785104
[research_placement_in_2026]: https://doi.org/10.1017/9781009399913.015
[research_plaetschke_weiss_1988]: https://doi.org/10.1007/978-3-7091-2628-8_11
[research_plante]: https://doi.org/10.70675/4579ebe8z5299z46f6z8e4fz76e3d841710d
[research_plante_dandois_2017]: https://doi.org/10.2514/6.2017-3903
[research_plante_laurendeau_2019]: https://doi.org/10.2514/1.j057224
[research_plotkin_dodbele_1988]: https://doi.org/10.2514/3.9920
[research_polamus_spreemann_1961]: https://ntrs.nasa.gov/citations/19980227774
[research_polivanov_sidorenko_2026]: https://doi.org/10.3390/aerospace13020120
[research_polonsky_2026]: https://doi.org/10.2514/1.c038869
[research_poojari_2022]: https://doi.org/10.47893/gret.2022.1089
[research_popescu_1999]: https://doi.org/10.2514/6.1999-1441
[research_poplingher_mallik_2022]: https://doi.org/10.2514/6.2022-2314
[research_poplingher_raveh_2018]: https://doi.org/10.2514/6.2018-2910
[research_poplingher_raveh_2022]: https://doi.org/10.2514/6.2022-2483
[research_portapas_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_posingies_1968]: https://doi.org/10.21236/ad0680275
[research_pototzky_2014]: https://doi.org/10.2514/6.2014-0731
[research_pototzky_2018]: https://doi.org/10.2514/6.2018-3474
[research_pototzky_moses_2005]: https://doi.org/10.2514/6.2005-2291
[research_potsdam_page_1997]: https://doi.org/10.2514/6.1997-2317
[research_potvin_grant_2026]: https://doi.org/10.2514/6.2026-1883
[research_pounds_walker_1980]: https://doi.org/10.2514/6.1980-461
[research_powell_katz_1974]: https://doi.org/10.2514/6.1974-885
[research_powers_1968]: https://ntrs.nasa.gov/citations/19680014432
[research_powers_1972]: https://ntrs.nasa.gov/citations/19720019363
[research_powers_1980]: https://doi.org/10.2514/6.1980-1571
[research_powers_1982]: https://doi.org/10.2514/3.56150
[research_powers_1984]: https://ntrs.nasa.gov/citations/19840012498
[research_powers_1986]: https://doi.org/10.2514/3.20147
[research_powers_1986_b]: https://ntrs.nasa.gov/citations/19860000382
[research_prakash_uthup_2009]: https://doi.org/10.2514/6.2009-3631
[research_prandtl_1928]: https://ntrs.nasa.gov/citations/19930090813
[research_predachenko_lemko_2017]: https://doi.org/10.1109/apuavd.2017.8308773
[research_predachenko_lemko_2019]: https://doi.org/10.18372/1990-5548.61.14222
[research_prediction_and_1985]: https://doi.org/10.2514/5.9781600865732.0173.0206
[research_prediction_of_1981]: https://doi.org/10.2514/6.1981-609
[research_prediction_of_1994]: https://doi.org/10.2514/6.1994-1883
[research_preliminary_sizing_2010]: https://doi.org/10.2514/5.9781600867538.0283.0292
[research_prilliman_slingerland_1966]: https://doi.org/10.2514/6.1966-14
[research_prior_rozinka_2023]: https://doi.org/10.2514/6.2023-4398
[research_prochazka_eduardo_2018]: https://doi.org/10.1109/ccta.2018.8511538
[research_properties_of_2014]: https://doi.org/10.2514/5.9781624102547.0625.0632
[research_properties_of_2024]: https://doi.org/10.2514/5.9781624107252.0695.0702
[research_protz_sparks_1998]: https://doi.org/10.2514/6.1998-4298
[research_prudente_cavalieri_2007]: https://doi.org/10.2514/6.2007-4557
[research_prudnikov_karavayev_1993]: https://doi.org/10.1007/978-3-642-52460-8_27
[research_puentes_takahashi_2024]: https://doi.org/10.2514/6.2024-0001
[research_pujara_1988]: https://doi.org/10.2514/3.20301
[research_purser_spear_1946]: https://ntrs.nasa.gov/citations/19930081810
[research_purser_spear_1947]: https://ntrs.nasa.gov/citations/19930082127
[research_purser_turner_1941]: https://ntrs.nasa.gov/citations/19930092828
[research_purwadi_hidayat_2023]: https://doi.org/10.1063/5.0181422
[research_pushtaev_1989]: https://doi.org/10.1016/0041-5553(89)90024-4
[research_puthisikamani_sreenivasaraja_2023]: https://doi.org/10.61653/joast.v74i4.2022.47
[research_putnam_ayers_1989]: https://ntrs.nasa.gov/citations/19890011556
[research_qi_bwb_2021]: https://doi.org/10.1007/s13272-021-00538-2
[research_qi_gao_2026]: https://doi.org/10.3390/aerospace13060496
[research_qi_wang_2017]: https://doi.org/10.23919/acc.2017.7963645
[research_qi_zhao_2018]: https://doi.org/10.23919/acc.2018.8431539
[research_qi_zhao_2018_b]: https://doi.org/10.1109/cdc.2018.8618742
[research_qian_alonso_2018]: https://doi.org/10.2514/6.2018-3739
[research_qian_alonso_2021]: https://doi.org/10.2514/6.2021-3022
[research_qin_2002]: https://doi.org/10.2514/6.2002-5448
[research_qin_wei_2023]: https://doi.org/10.23919/ccc58697.2023.10240514
[research_qin_wong_2007]: https://doi.org/10.2514/6.2007-57
[research_qiu_ang_2019]: https://doi.org/10.1155/2019/5046395
[research_qiu_sun_2009]: https://doi.org/10.1109/iciea.2009.5138445
[research_qu_li_2011]: https://doi.org/10.1109/icciautom.2011.6183979
[research_qu_li_2013]: https://doi.org/10.12696/gsam.2013.0935
[research_quan_2013]: https://doi.org/10.4028/www.scientific.net/amr.748.555
[research_quantitative_design_2017]: https://doi.org/10.2514/5.9781624104435.0105.0170
[research_quast_nelson_1991]: https://ntrs.nasa.gov/citations/19910069152
[research_queijo_fences_1954]: https://ntrs.nasa.gov/citations/19930092215
[research_queijo_wells_1956]: https://ntrs.nasa.gov/citations/19930084622
[research_queijo_wolhart_1951]: https://ntrs.nasa.gov/citations/19930092095
[research_querry]: https://doi.org/10.70675/be362339z0dfez4119zaaedz4df05825ab93
[research_quigley_anderson_1960]: https://ntrs.nasa.gov/citations/19980223993
[research_quinn_cutchins_1984]: https://doi.org/10.2514/6.1984-2094
[research_quitter_marino_2023]: https://doi.org/10.2514/6.2023-3370
[research_qureshi_wang_2014]: https://doi.org/10.2514/6.2014-2104
[research_radzetsky_reibert_1994]: https://doi.org/10.2514/6.1994-2373
[research_raffel_wienke_2021]: https://doi.org/10.2514/1.c036022
[research_raghavan_ananthkrishnan_2005]: https://doi.org/10.2514/6.2005-6029
[research_raghavan_patil_2009]: https://doi.org/10.2514/1.36847
[research_rahman_vowotor_2025]: https://doi.org/10.2139/ssrn.5220226
[research_rainey_1957]: https://ntrs.nasa.gov/citations/19930091024
[research_rainey_igoe_1958]: https://ntrs.nasa.gov/citations/19930093826
[research_raj_1983]: https://doi.org/10.2514/6.1983-262
[research_raj_1984]: https://doi.org/10.2514/3.48237
[research_raj_mohan_2015]: https://doi.org/10.1109/iccsp.2015.7322579
[research_rajanna_jaiswal_2024]: https://doi.org/10.1007/s00466-023-02436-2
[research_rajanna_lua_2026]: https://doi.org/10.2514/6.2026-0805
[research_rajput_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.643.54
[research_rajput_zhangweiguo_2015]: https://doi.org/10.1109/ascc.2015.7244649
[research_ralphaaharrah_1995]: https://ntrs.nasa.gov/citations/19950024642
[research_ramachandran_wells_1974]: https://doi.org/10.2514/6.1974-790
[research_rambacher_butler_2024]: https://doi.org/10.2514/6.2024-1936
[research_ramirezzeigler_avery_2026]: https://doi.org/10.2514/6.2026-4580
[research_ramm_1990_b]: https://doi.org/10.1093/oso/9780195060973.003.0005
[research_raney_1987]: https://doi.org/10.2514/6.1987-2625
[research_raney_batterson_1989]: https://ntrs.nasa.gov/citations/19890012431
[research_rao_1984]: https://ntrs.nasa.gov/citations/19850011675
[research_rao_huffman_1978]: https://ntrs.nasa.gov/citations/19780024105
[research_rao_johnson_1982]: https://ntrs.nasa.gov/citations/19820038517
[research_rao_johnson_1983]: https://doi.org/10.2514/3.44904
[research_raol_singh_2023]: https://doi.org/10.1201/9781003293514-10
[research_rashad_elbadawy_2025]: https://doi.org/10.2514/6.2025-2080
[research_rastgoftar_ni_2017]: https://doi.org/10.2514/6.2017-1515
[research_rathert_1951]: https://ntrs.nasa.gov/citations/19930086490
[research_ratliff_pagilla_2008]: https://doi.org/10.1109/acc.2008.4586722
[research_raveh_2011]: https://doi.org/10.2514/1.c031224
[research_ray_1965]: https://doi.org/10.2514/6.1965-737
[research_ray_mckinney_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_ray_mckinney_1973]: https://ntrs.nasa.gov/citations/19730017272
[research_razon_maher_2023]: https://doi.org/10.2514/6.2023-1551
[research_re_1974]: https://ntrs.nasa.gov/citations/19830002754
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_recant_1939]: https://ntrs.nasa.gov/citations/19930081443
[research_redeker_voersmann_1988]: https://doi.org/10.2514/6.1988-2165
[research_rediess_melton_1994]: https://doi.org/10.2514/6.1994-2172
[research_rediniotis_klute_1994]: https://doi.org/10.2514/3.12044
[research_reed_1955]: https://ntrs.nasa.gov/citations/19930088802
[research_reed_1982]: https://ntrs.nasa.gov/citations/19820024497
[research_reed_1984]: https://doi.org/10.2514/6.1984-1678
[research_reed_1985]: https://doi.org/10.1007/978-3-642-82462-3_57
[research_reed_1987]: https://doi.org/10.1063/1.866473
[research_reed_clay_1937]: https://ntrs.nasa.gov/citations/19930081377
[research_reeder_1944]: https://ntrs.nasa.gov/citations/19930092869
[research_reeder_1945]: https://ntrs.nasa.gov/citations/19930092600
[research_reeder_1945_b]: https://ntrs.nasa.gov/citations/19930092601
[research_reeder_1945_c]: https://ntrs.nasa.gov/citations/19930092602
[research_regan_2008]: https://doi.org/10.2514/6.2008-6571
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
[research_reibert_saric_1997]: https://doi.org/10.2514/6.1997-1816
[research_reigelsperger_hammett_1995]: https://doi.org/10.2514/6.1995-3249
[research_reimann_tinetti_2005]: https://doi.org/10.2514/6.2005-2980
[research_reist_zingg_2014]: https://doi.org/10.2514/6.2014-0905
[research_reist_zingg_2015]: https://doi.org/10.2514/6.2015-3292
[research_reist_zingg_2016]: https://doi.org/10.2514/6.2016-3874
[research_ren_gao_2022]: https://doi.org/10.3390/act11060155
[research_report_no_1931]: https://doi.org/10.1016/s0016-0032(31)90566-8
[research_repperger_koivo_1997]: https://doi.org/10.1109/acc.1997.611837
[research_reu_ying_1991]: https://doi.org/10.2514/6.1991-599
[research_reynolds_smith_1948]: https://ntrs.nasa.gov/citations/19930085437
[research_rezaei_khosravi_2023]: https://doi.org/10.36909/jer.16725
[research_rezazadehmovahhed_hamed_2025]: https://doi.org/10.1007/s13369-025-10504-3
[research_rezazadehmovahhed_hamed_2026]: https://doi.org/10.2139/ssrn.6740761
[research_rhoads_1952]: https://doi.org/10.21236/ad0014479
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_rhoads_1970]: https://doi.org/10.21236/ad0876589
[research_rhudy_2016]: https://doi.org/10.2514/6.2016-4301
[research_ribner_1950]: https://ntrs.nasa.gov/citations/19930082764
[research_richardeday_1953]: https://ntrs.nasa.gov/citations/19930087801
[research_richards_adams_2014]: https://doi.org/10.2514/6.2014-0037
[research_rickard_1978]: https://doi.org/10.2514/6.1978-1371
[research_rickard_levison_1981]: https://ntrs.nasa.gov/citations/19820005814
[research_rickey_1946]: https://ntrs.nasa.gov/citations/19930092688
[research_riebe_macleod_1950]: https://ntrs.nasa.gov/citations/20050030032
[research_riethausen_2026]: https://doi.org/10.21741/9781644904251-86
[research_rigid_body_flight_2026]: https://doi.org/10.1017/9781009399913.005
[research_riley_drajeske_1991]: https://doi.org/10.2514/6.1991-2884
[research_rimer_chipman_1983]: https://doi.org/10.2514/6.1983-2125
[research_rimer_chipman_1984]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1984_b]: https://ntrs.nasa.gov/citations/19840060637
[research_rising_1982]: https://doi.org/10.2514/6.1982-1297
[research_rising_davis_1984]: https://ntrs.nasa.gov/citations/19850030442
[research_risse_anton_2010]: https://doi.org/10.2514/6.2010-9261
[research_rivera_florance_2000]: https://doi.org/10.2514/6.2000-1768
[research_rivers_hunter_2012]: https://doi.org/10.2514/6.2012-3209
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1977_b]: https://doi.org/10.21236/ada056946
[research_rizzetta_1996]: https://doi.org/10.2514/6.1996-2012
[research_rizzetta_visbal_2016]: https://doi.org/10.2514/6.2016-3930
[research_rizzi_1984]: https://doi.org/10.2514/6.1984-2142
[research_rizzi_1985]: https://doi.org/10.2514/3.45127
[research_rizzi_1995]: https://doi.org/10.1007/978-3-642-79440-7_9
[research_ro_barlow_1992]: https://doi.org/10.2514/6.1992-46
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_robb_vuppala_2023]: https://doi.org/10.2514/6.2023-2610
[research_robbins_stansbury_2023]: https://doi.org/10.1504/ijvd.2023.10060015
[research_roberts_1963]: https://doi.org/10.21236/ad0420853
[research_roberts_1988_b]: https://doi.org/10.2514/6.1988-2077
[research_roberts_lind_2009]: https://doi.org/10.2514/6.2009-5846
[research_roberts_yang_2006]: https://doi.org/10.2514/6.2006-6345
[research_robertwkempel_larrywstrutz_1970]: https://ntrs.nasa.gov/citations/19710000629
[research_robinson_robinson_1980]: https://doi.org/10.2514/6.1980-1884
[research_robinson_yuan_2020]: https://doi.org/10.2514/6.2020-2726
[research_rockwell_1994]: https://doi.org/10.21236/ada278988
[research_rockwood_medina_2019]: https://doi.org/10.2514/6.2019-3335
[research_rodchenko_zaichik_2003]: https://doi.org/10.2514/2.6920
[research_rodden_1989]: https://doi.org/10.2514/3.45842
[research_rodemich_andrew_1965]: https://doi.org/10.21236/ad0618097
[research_rodgers_1964]: https://doi.org/10.2514/6.1964-167
[research_rodgers_1965]: https://doi.org/10.2514/3.43615
[research_rodgers_1966]: https://doi.org/10.2514/3.43765
[research_roeser_monnich_2024]: https://doi.org/10.1007/978-3-031-69425-7_5
[research_rogalski_2018]: https://doi.org/10.1108/aeat-02-2018-0088
[research_rogalski_dolega_2006]: https://doi.org/10.3846/16487788.2006.9635930
[research_rogalski_rzucidlo_2021]: https://doi.org/10.1108/aeat-11-2020-0269
[research_rogers_2007]: https://doi.org/10.2514/6.2007-6307
[research_rogers_walterk_1953]: https://doi.org/10.21236/ad0013358
[research_rogers_walterk_1958]: https://doi.org/10.21236/ad0200177
[research_rohling_1968]: https://doi.org/10.2514/6.1968-1066
[research_rohling_1969]: https://doi.org/10.2514/3.44097
[research_rojascarvajal_amitay_2023]: https://doi.org/10.2514/6.2023-0456
[research_rojascarvajal_amitay_2025]: https://doi.org/10.2514/1.j064152
[research_rojascarvajal_guha_2022]: https://doi.org/10.2514/6.2022-0470
[research_rojascarvajal_kumarguha_2024]: https://doi.org/10.2514/1.j063505
[research_rokoni_hasan_2013]: https://doi.org/10.3329/jme.v43i1.15782
[research_rolek_1974]: https://doi.org/10.1177/154193127401800304
[research_rolls_wingrove_1958]: https://ntrs.nasa.gov/citations/19980228476
[research_roman_allen_2000]: https://doi.org/10.2514/6.2000-4335
[research_roman_gilmore_2003]: https://doi.org/10.2514/6.2003-554
[research_romberg_2003]: https://doi.org/10.2514/6.iac-03-i.2.09
[research_romere_chambliss_1972]: https://ntrs.nasa.gov/citations/19730003168
[research_rong_deng_2016]: https://doi.org/10.5028/jatm.v8i3.627
[research_roohani_skews_2009]: https://doi.org/10.1007/978-3-540-85181-3_98
[research_rooney_chung_1982]: https://doi.org/10.2514/6.1982-1524
[research_roos_1980]: https://doi.org/10.2514/3.57965
[research_roos_1985]: https://doi.org/10.2514/6.1985-1609
[research_rosariogabriel_cortes_2018]: https://doi.org/10.1109/icuas.2018.8453350
[research_rose_seginer_1978]: https://doi.org/10.2514/3.58399
[research_rosemann_birkemeyer_2002]: https://doi.org/10.1007/978-3-540-45856-2_12
[research_rosenberg_1944]: https://doi.org/10.2514/8.11091
[research_rosenow_sachwitz_2022]: https://doi.org/10.3390/aerospace9050263
[research_roskam_1977]: https://ntrs.nasa.gov/citations/19770054237
[research_ross_1972]: https://doi.org/10.2514/6.1972-62
[research_ross_1972_b]: https://doi.org/10.2514/3.59050
[research_rossetti_beblo_2022]: https://doi.org/10.2514/6.2022-1156
[research_rossitto_hodgkinson_1993]: https://doi.org/10.2514/6.1993-3815
[research_rostami_chung_2021]: https://doi.org/10.1177/09544100211029450
[research_rotaru_circiu_2016]: https://doi.org/10.1063/1.4951802
[research_row_fischel_1963]: https://doi.org/10.2514/6.1963-75
[research_rowan_dogan_2023]: https://doi.org/10.2514/6.2023-1453
[research_roy_2009]: https://doi.org/10.21236/ada511003
[research_roy_ghosh_2010]: https://doi.org/10.21236/ada532004
[research_roysdon_khalid_2010]: https://doi.org/10.2514/6.2010-9167
[research_roysdon_khalid_2011]: https://doi.org/10.2514/6.2011-1563
[research_rubiosierra_delgado_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001399
[research_rudesh_singh_2025]: https://doi.org/10.1007/s44245-025-00117-3
[research_ruhlin_murphy_1981]: https://doi.org/10.2514/6.1981-650
[research_rui_zhou_2007]: https://doi.org/10.1109/chicc.2006.4346934
[research_runckel_henderson_1952]: https://ntrs.nasa.gov/citations/19930087259
[research_runyan_georgefalvy_1979]: https://doi.org/10.2514/6.1979-267
[research_ruseno_2021]: https://doi.org/10.35894/jtk.v6i2.39
[research_russell_1996]: https://doi.org/10.1016/b978-034063170-6/50011-6
[research_rustagi_kothari_2018]: https://doi.org/10.2514/6.2018-0530
[research_rymarz_ramaprian_1995]: https://doi.org/10.2514/6.1995-2161
[research_rynaski_1985]: https://doi.org/10.2514/6.1985-1849
[research_rynaski_1994]: https://doi.org/10.2514/6.1994-3672
[research_rynaski_andrisani_1978]: https://doi.org/10.2514/6.1978-1328
[research_rynaski_weingarten_1986]: https://doi.org/10.2514/6.1986-2249
[research_ryu_andrisani_2000]: https://doi.org/10.2514/6.2000-3989
[research_ryu_andrisani_2000_b]: https://doi.org/10.2514/6.2000-3988
[research_ryu_andrisani_2003]: https://doi.org/10.2514/2.5070
[research_rzucidlo_tomczyk_2007]: https://doi.org/10.4271/2007-01-3804
[research_s_c_2025]: https://doi.org/10.1108/aeat-08-2024-0241
[research_sachs_1969]: https://doi.org/10.2514/3.44111
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_1990]: https://doi.org/10.2514/6.1990-2804
[research_sachs_1999]: https://doi.org/10.2514/2.2550
[research_sachs_knoll_1994]: https://doi.org/10.2514/6.1994-3508
[research_sadoff_1958]: https://ntrs.nasa.gov/citations/19980232012
[research_sadoff_1962]: https://ntrs.nasa.gov/citations/19630000307
[research_sadoff_blunt_te_1954]: https://ntrs.nasa.gov/citations/19650075959
[research_sadoff_mcfadden_1961]: https://ntrs.nasa.gov/citations/19980227090
[research_sadoff_sisk_1950]: https://ntrs.nasa.gov/citations/19930086420
[research_sadraey_2022]: https://doi.org/10.1007/978-3-031-18765-0_3
[research_sadraey_2022_b]: https://doi.org/10.1007/978-3-031-18765-0_5
[research_sadraey_2022_c]: https://doi.org/10.1007/978-3-031-18765-0_4
[research_sadraey_2022_d]: https://doi.org/10.1007/978-3-031-18765-0_6
[research_saephan_vandam_2006]: https://doi.org/10.2514/6.2006-6131
[research_saephan_vandam_2006_b]: https://doi.org/10.2514/6.2006-3321
[research_saephan_vandam_2008]: https://doi.org/10.2514/1.33730
[research_saetti_rogers_2020]: https://doi.org/10.4050/sm_2020_hq-916
[research_saghafi_banazadeh_2006]: https://doi.org/10.2514/6.2006-4980
[research_saheby_2026]: https://doi.org/10.1016/j.ast.2025.111026
[research_sahyoun_boose_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_salahudden_giri_2020]: https://doi.org/10.1109/icuas48674.2020.9213975
[research_samardzic_2023]: https://doi.org/10.1007/978-3-031-42041-2_5
[research_samardzic_isakovic_2013]: https://doi.org/10.1016/j.measurement.2013.04.074
[research_sammonds_bunnell_1980]: https://ntrs.nasa.gov/citations/19800061746
[research_sammonds_bunnell_1981]: https://ntrs.nasa.gov/citations/19810012554
[research_sandahl_1948]: https://ntrs.nasa.gov/citations/19930085323
[research_sandahl_bland_1949]: https://ntrs.nasa.gov/citations/19930085881
[research_sandahl_delta_1948]: https://ntrs.nasa.gov/citations/19930085426
[research_sandahl_strass_1950]: https://ntrs.nasa.gov/citations/19930086227
[research_sandahl_strass_1950_b]: https://ntrs.nasa.gov/citations/19930086271
[research_sandahl_swept_1948]: https://ntrs.nasa.gov/citations/19930085384
[research_sanders_1965]: https://doi.org/10.2514/3.43662
[research_sanders_eastep_2003]: https://doi.org/10.2514/2.3062
[research_sanders_tischler_2018]: https://doi.org/10.2514/6.2018-0296
[research_sanderson_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50017-8
[research_sandlin_swanson_1990]: https://ntrs.nasa.gov/citations/19900017199
[research_sanfilippo_1970]: https://doi.org/10.2514/6.1970-962
[research_sang]: https://doi.org/10.18130/v3q79n
[research_sanghi_cesnik_2024]: https://doi.org/10.2514/1.c037470
[research_sanghi_riso_2020]: https://doi.org/10.2514/6.2020-2645
[research_sanghi_riso_2025]: https://doi.org/10.2514/1.c038166
[research_santos_adeodato_2024]: https://doi.org/10.21203/rs.3.rs-4176374/v1
[research_saporito_daronch_2021]: https://doi.org/10.2514/6.2021-3101
[research_saraswathi_2000]: https://doi.org/10.14429/dsj.50.3366
[research_saric_1997]: https://doi.org/10.21236/ada388392
[research_saric_2010]: https://doi.org/10.21236/ada564004
[research_saric_yeates_1985]: https://doi.org/10.2514/6.1985-493
[research_sarigulklijn_nespeca_2008]: https://doi.org/10.2514/6.2008-6877
[research_sarkar_ananthasayanam_2009]: https://doi.org/10.2514/6.2009-5940
[research_sarkar_panneerselvam_1998]: https://doi.org/10.2514/6.1998-4260
[research_sarrafian_powers_1985]: https://ntrs.nasa.gov/citations/19850024811
[research_sarrafian_powers_1988]: https://doi.org/10.2514/3.20309
[research_saucez]: https://doi.org/10.70675/f03a0681z9efcz414ez8944zcc71830d8acb
[research_saucez_boiffier_2012]: https://doi.org/10.2514/6.2012-4501
[research_saussie_akhrif_2011]: https://doi.org/10.1109/med.2011.5983189
[research_sawyer_trant_1950]: https://ntrs.nasa.gov/citations/20050028471
[research_sboevd_2024]: https://doi.org/10.53954/9785605099659_25
[research_scalera_durham_1999]: https://doi.org/10.2514/6.1999-4281
[research_schade_hassell_1953]: https://ntrs.nasa.gov/citations/19930092179
[research_schaeffler_telionis_1998]: https://doi.org/10.2514/6.1998-673
[research_schairer_1941]: https://doi.org/10.2514/8.10709
[research_schauerhamer_robinson_2017]: https://doi.org/10.2514/1.c034187
[research_schauerte_schreyer_2023]: https://doi.org/10.2514/6.2023-0431
[research_schauerte_schreyer_2024]: https://doi.org/10.2514/6.2024-1946
[research_schauerte_schreyer_2025]: https://doi.org/10.2514/6.2025-3837
[research_schiavetta_boelens_2006]: https://doi.org/10.2514/6.2006-3171
[research_schierbrock_takahashi_2021]: https://doi.org/10.2514/6.2021-0325
[research_schiess_1986]: https://ntrs.nasa.gov/citations/19860021284
[research_schiess_1988]: https://ntrs.nasa.gov/citations/19880007404
[research_schiff_tobak_1981]: https://ntrs.nasa.gov/citations/19810022579
[research_schirrer_kozek_2013]: https://doi.org/10.1007/978-3-7091-1571-8_28
[research_schmidt_1983]: https://doi.org/10.2514/6.1983-2231
[research_schmidt_1985]: https://doi.org/10.2514/6.1985-1851
[research_schmidt_1986]: https://doi.org/10.2514/6.1986-2711
[research_schmidt_2016]: https://doi.org/10.2514/6.2016-2099
[research_schmidt_danowsky_2019]: https://doi.org/10.2514/6.2019-1816
[research_schmidt_static_margin_2025]: https://doi.org/10.2514/1.c038107
[research_schmidt_wright_1991]: https://doi.org/10.2514/6.1991-2885
[research_schmidt_zhao_2016]: https://doi.org/10.2514/6.2016-1748
[research_schmitt_destarac_1983]: https://doi.org/10.2514/6.1983-1804
[research_schmitt_reneaux_1990]: https://doi.org/10.2514/6.1990-3042
[research_schnoebelen_yechout_2003]: https://doi.org/10.2514/6.2003-204
[research_schnurbusch_1944]: https://ntrs.nasa.gov/citations/19930092595
[research_schnurbusch_1945]: https://ntrs.nasa.gov/citations/19930092682
[research_scholz_2021]: https://doi.org/10.13111/2066-8201.2021.13.3.13
[research_schroeder_2001]: https://ntrs.nasa.gov/citations/20010038275
[research_schroeder_chung_1998]: https://doi.org/10.2514/6.1998-4333
[research_schroeder_chung_2000]: https://doi.org/10.2514/2.4578
[research_schroeder_chung_2001]: https://ntrs.nasa.gov/citations/20010037958
[research_schuck_heller_2013]: https://doi.org/10.2514/6.2013-5180
[research_schuelein_2008]: https://doi.org/10.2514/6.2008-4208
[research_schuldenfrei_1947]: https://ntrs.nasa.gov/citations/19930093791
[research_schuler_1983]: https://doi.org/10.2514/6.1983-2104
[research_schult_1954]: https://ntrs.nasa.gov/citations/19930088315
[research_schult_fields_1952]: https://ntrs.nasa.gov/citations/19930087271
[research_schult_fields_1954]: https://ntrs.nasa.gov/citations/19930088082
[research_schumacher_1952]: https://doi.org/10.21236/ada075866
[research_schutte_huber_2018]: https://doi.org/10.2514/1.c033700
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schweiger_weiss_2000]: https://doi.org/10.2514/6.2000-4828
[research_schweikhard_1966]: https://ntrs.nasa.gov/citations/19670032784
[research_schweikhard_1967]: https://doi.org/10.2514/3.43804
[research_schwithal_wallace_2025]: https://doi.org/10.2514/6.2025-1825
[research_schy_1972]: https://ntrs.nasa.gov/citations/19730035786
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_sears_1980]: https://doi.org/10.2514/6.1980-3036
[research_seaver_bennett_2023]: https://doi.org/10.2514/6.2023-3293
[research_sebastia_hornung_2023]: https://doi.org/10.2514/6.2023-3528
[research_sebastia_wurz_2024]: https://doi.org/10.2514/6.2024-3997
[research_seckel_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50026-9
[research_seckel_1964_b]: https://doi.org/10.1016/b978-0-12-634450-9.50007-5
[research_seckel_1964_c]: https://doi.org/10.1016/b978-0-12-634450-9.50028-2
[research_seckel_1964_d]: https://doi.org/10.1016/b978-0-12-634450-9.50019-1
[research_seckel_1964_e]: https://doi.org/10.1016/b978-0-12-634450-9.50021-x
[research_seckel_1964_f]: https://doi.org/10.1016/b978-0-12-634450-9.50020-8
[research_seebass_1997]: https://doi.org/10.1007/978-3-7091-2658-5_20
[research_seidel_sandford_1985]: https://doi.org/10.2514/6.1985-598
[research_seider_haenel_1991]: https://doi.org/10.2514/6.1991-184
[research_semaan_scholz_2013]: https://doi.org/10.2514/6.2013-2813
[research_seraj_martins_2025]: https://doi.org/10.2514/1.c037899
[research_serpieri_kotsonis_2015]: https://doi.org/10.2514/6.2015-2576
[research_serpieri_kotsonis_2016]: https://doi.org/10.2514/6.2016-3791
[research_serpieri_kotsonis_2016_b]: https://doi.org/10.2514/6.2016-3792
[research_sethbanderson_1992]: https://ntrs.nasa.gov/citations/19930010715
[research_sevart_1971]: https://ntrs.nasa.gov/citations/19740003716
[research_sevart_patel_1972]: https://ntrs.nasa.gov/citations/19740003696
[research_sevart_patel_1973]: https://ntrs.nasa.gov/citations/19740003694
[research_sgueglia]: https://doi.org/10.70675/2046c996z7c68z4b65za4ffz08317a09ee02
[research_shafer_1975]: https://ntrs.nasa.gov/citations/19760007049
[research_shafer_1991]: https://ntrs.nasa.gov/citations/19910063180
[research_shafer_1992]: https://ntrs.nasa.gov/citations/19920019867
[research_shafer_1994]: https://ntrs.nasa.gov/citations/19940031462
[research_shafer_koehler_1989]: https://ntrs.nasa.gov/citations/19910005869
[research_shafer_smith_1983]: https://doi.org/10.2514/6.1983-2107
[research_shafer_smith_1984]: https://ntrs.nasa.gov/citations/19840008145
[research_shafer_steinmetz_2001]: https://ntrs.nasa.gov/citations/20010037948
[research_shafer_steinmetz_2001_b]: https://ntrs.nasa.gov/citations/20010038270
[research_shah_granda_1998]: https://doi.org/10.2514/6.1998-4448
[research_shamikh_2013]: https://doi.org/10.31185/ejuow.vol1.iss2.10
[research_shams]: https://doi.org/10.22215/etd/2023-15773
[research_shams_khouli_2023]: https://doi.org/10.2514/6.2023-0337
[research_shams_khouli_2026]: https://doi.org/10.1115/1.4071374
[research_shamstaleghani_ghajar_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001140
[research_shankar_goebel_1983]: https://doi.org/10.2514/6.1983-502
[research_shankar_goebel_1985]: https://doi.org/10.2514/6.1985-428
[research_shankar_malmuth_1979]: https://doi.org/10.2514/6.1979-1565
[research_shankar_malmuth_1980]: https://doi.org/10.2514/6.1980-127
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shankar_malmuth_1983]: https://doi.org/10.2514/3.44893
[research_shannon_1948]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
[research_shao_guo_2024]: https://doi.org/10.2139/ssrn.5041226
[research_shao_he_2026]: https://doi.org/10.2139/ssrn.6351262
[research_shao_liu_2022]: https://doi.org/10.1109/isas55863.2022.9757298
[research_shao_meng_2026]: https://doi.org/10.1016/j.cja.2026.104393
[research_sharif_abbas_2022]: https://doi.org/10.47893/gret.2022.1084
[research_sharma_hosder_2024]: https://doi.org/10.3390/aerospace11020137
[research_shayak_girdhar_2024]: https://doi.org/10.3389/fpace.2024.1308872
[research_shayan_vankampen_2021]: https://doi.org/10.2514/6.2021-0884
[research_shearwood_2020]: https://doi.org/10.3390/aerospace7100150
[research_shearwood_nabawy_2020]: https://doi.org/10.2514/6.2020-2677
[research_shearwood_nabawy_2021]: https://doi.org/10.2514/6.2021-2530
[research_shearwood_nabawy_2021_b]: https://doi.org/10.2514/6.2021-1826
[research_shearwood_nabawy_2023]: https://doi.org/10.1109/access.2023.3286848
[research_shekar_molloy_2026]: https://doi.org/10.2514/6.2026-1491
[research_shen_chen_2025]: https://doi.org/10.3390/drones9090624
[research_shen_huang_2019]: https://doi.org/10.1016/j.cja.2019.04.007
[research_shen_huang_2021]: https://doi.org/10.1016/j.cja.2020.07.022
[research_sheneshen_kamal_2025]: https://doi.org/10.1088/1742-6596/3070/1/012004
[research_sherman_tirona_2021]: https://doi.org/10.2514/6.2021-0819
[research_sheta_2003]: https://doi.org/10.1177/1077546303009005005
[research_sheta_2004]: https://doi.org/10.2514/1.9327
[research_sheta_huttsell_2001]: https://doi.org/10.2514/6.2001-1664
[research_sheta_huttsell_2002]: https://doi.org/10.2514/6.2002-948
[research_sheta_huttsell_2003]: https://doi.org/10.1016/s0889-9746(02)00138-x
[research_sheta_moses_2003]: https://doi.org/10.2514/6.2003-1887
[research_sheta_rock_2001]: https://doi.org/10.2514/6.2001-710
[research_shevchuk_2014]: https://doi.org/10.18372/1990-5548.39.7327
[research_shevell_1978]: https://doi.org/10.2514/3.58419
[research_shi_ma_2023]: https://doi.org/10.1109/isaes58852.2023.10281222
[research_shi_wu_2022]: https://doi.org/10.1016/j.procs.2022.10.049
[research_shibata_nakao_1987]: https://doi.org/10.2514/6.1987-2587
[research_shin_2010]: https://doi.org/10.2514/6.2010-8338
[research_shin_2011]: https://doi.org/10.5139/jksas.2011.39.8.725
[research_shiqi_tian_2018]: https://doi.org/10.2514/6.2018-0790
[research_shmilovich_caughey]: https://doi.org/10.1007/3-540-13917-6_190
[research_shmilovich_caughey_1985]: https://doi.org/10.2514/3.45169
[research_shmilovich_yadlin_2023]: https://doi.org/10.2514/6.2023-0655
[research_shmilovich_yadlin_2026]: https://doi.org/10.2514/1.c037586
[research_shmul_erenthal_2018]: https://doi.org/10.1201/9781315136820-10
[research_shomber_gertsen_1967]: https://doi.org/10.2514/3.43851
[research_shrivastava_1987]: https://ntrs.nasa.gov/citations/19870013189
[research_shtessel_buffington_1999]: https://doi.org/10.2514/6.1999-4136
[research_shtessel_buffington_2002]: https://doi.org/10.1109/87.987075
[research_shuang_zhang_2016]: https://doi.org/10.1109/cgncc.2016.7828825
[research_shuang_zhang_2017]: https://doi.org/10.2514/6.2017-1253
[research_shumsky_2006]: https://doi.org/10.1109/ifost.2006.312262
[research_siddiqui_maqsood_2025]: https://doi.org/10.1016/j.ijnonlinmec.2024.104934
[research_siddiqui_sultan_2023]: https://doi.org/10.1007/s11012-023-01649-2
[research_sieradzki_2016]: https://doi.org/10.5604/05096669.1226890
[research_silva]: https://doi.org/10.11606/003273318
[research_silva_2011]: https://doi.org/10.2514/6.2011-6355
[research_silva_b]: https://doi.org/10.11606/003239828
[research_silva_grinet_2019]: https://doi.org/10.14209/jcis.2019.3
[research_silva_nunes_2022]: https://doi.org/10.2514/6.2022-0689
[research_silvers_fournier_1958]: https://ntrs.nasa.gov/citations/20050028468
[research_silvers_spreemann_1950]: https://ntrs.nasa.gov/citations/19930086053
[research_sim_1973]: https://ntrs.nasa.gov/citations/19740003701
[research_sim_1997]: https://ntrs.nasa.gov/citations/19970027378
[research_sim_curry_1978]: https://ntrs.nasa.gov/citations/19790001897
[research_simbuerger_raveh_2022]: https://doi.org/10.2514/1.c036626
[research_simmons_sysid_2023]: https://doi.org/10.2514/1.c037260
[research_simon_2014]: https://doi.org/10.3384/lic.diva-103742
[research_simon_blake_1993]: https://doi.org/10.2514/6.1993-4000
[research_simon_williams_2023]: https://doi.org/10.2514/6.2023-3565
[research_simon_williams_2024]: https://doi.org/10.2514/6.2024-0491
[research_simulation_in_1988]: https://doi.org/10.2514/6.1988-2130
[research_simulation_requirements_2017]: https://doi.org/10.2514/5.9781624104435.0171.0230
[research_sinacori_1986]: https://doi.org/10.21236/ada359459
[research_sinclair_1988]: https://doi.org/10.2514/6.1988-2027
[research_singh_2016]: https://doi.org/10.18535/ijecs/v5i11.88
[research_singh_brown_2016]: https://doi.org/10.2514/1.c033658
[research_singh_chowdhury_2021]: https://doi.org/10.47531/mantech/ecc.2021.42
[research_singh_jategaonkar_1996]: https://doi.org/10.2514/3.46993
[research_singh_karnick_2022]: https://doi.org/10.2514/6.2022-4172
[research_singh_mcdonough_2014]: https://doi.org/10.2514/1.c032183
[research_singh_raol_2000]: https://doi.org/10.1017/s0001924000091442
[research_singh_scholz_2018]: https://doi.org/10.2514/6.2018-4023
[research_singh_toropov_2016]: https://doi.org/10.2514/6.2016-3364
[research_singh_venkatraman_2023]: https://doi.org/10.2514/6.2023-1566
[research_singh_venkatraman_2026]: https://doi.org/10.2514/1.j065133
[research_singh_yim_1994]: https://doi.org/10.2514/6.1994-3680
[research_singh_yirn_1995]: https://doi.org/10.2514/3.56652
[research_singhasenee_lamon_2026]: https://doi.org/10.2514/6.2026-0319
[research_sinha_ananthkrishnan_2017]: https://doi.org/10.1201/9781315151977-6
[research_sinha_ananthkrishnan_2021]: https://doi.org/10.1201/9781003096801-3
[research_sinha_ananthkrishnan_2021_b]: https://doi.org/10.1201/9781003096801-6
[research_sinha_ananthkrishnan_2021_c]: https://doi.org/10.1201/9781003096801-7
[research_siqueira_moreira_2007]: https://doi.org/10.2514/6.2007-6767
[research_sisk_mataeny_1980]: https://ntrs.nasa.gov/citations/19800014838
[research_sisk_matheny_1979]: https://ntrs.nasa.gov/citations/19790015808
[research_sisk_mooney_1953]: https://ntrs.nasa.gov/citations/19930087506
[research_sissingh_2015]: https://doi.org/10.2514/5.9781624102738.0135.0174
[research_siu_martos_2013]: https://doi.org/10.2514/6.2013-5086
[research_sivan_1971]: https://doi.org/10.2514/6.1971-792
[research_siwakosit_hess_2000]: https://ntrs.nasa.gov/citations/20000109867
[research_sizlo_berg_1979]: https://ntrs.nasa.gov/citations/19820024501
[research_sjoberg_1945]: https://ntrs.nasa.gov/citations/19930092646
[research_sjoberg_reeder_1948]: https://ntrs.nasa.gov/citations/19930082317
[research_sjoberg_reeder_1948_b]: https://ntrs.nasa.gov/citations/19930082366
[research_sklenar_mateju_2022]: https://doi.org/10.3846/aviation.2022.15963
[research_skoog_1951]: https://ntrs.nasa.gov/citations/19930086551
[research_skujins_cesnik_2011]: https://doi.org/10.2514/6.2011-6525
[research_sleeman_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_sleeman_byrnes_1953]: https://ntrs.nasa.gov/citations/20090023635
[research_sleeman_morrison_1953]: https://ntrs.nasa.gov/citations/20050029410
[research_slingerland_2002]: https://doi.org/10.2514/6.2002-5842
[research_slingerland_2005]: https://doi.org/10.2514/6.2005-815
[research_sliwa_1980]: https://ntrs.nasa.gov/citations/19810005457
[research_smetana_knepper_1973]: https://doi.org/10.2514/3.44355
[research_smetana_summery_1972]: https://ntrs.nasa.gov/citations/19720018355
[research_smith_1959]: https://ntrs.nasa.gov/citations/19630003098
[research_smith_1975]: https://ntrs.nasa.gov/citations/19760004017
[research_smith_1977]: https://doi.org/10.21236/ada069198
[research_smith_1979]: https://ntrs.nasa.gov/citations/19790023049
[research_smith_1981]: https://ntrs.nasa.gov/citations/19820005276
[research_smith_1982]: https://doi.org/10.21236/ada113996
[research_smith_1986]: https://doi.org/10.2514/6.1986-2202
[research_smith_berry_1975]: https://ntrs.nasa.gov/citations/19750008488
[research_smith_edwards_1980]: https://ntrs.nasa.gov/citations/19800012870
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_tailless_1953]: https://ntrs.nasa.gov/citations/19930087359
[research_smith_taylor_1967]: https://ntrs.nasa.gov/citations/19680002077
[research_snell_1998]: https://doi.org/10.2514/6.1998-500
[research_snyder_fry_1972]: https://ntrs.nasa.gov/citations/19730006307
[research_sobel_1982]: https://doi.org/10.1109/cdc.1982.268384
[research_sobel_lee_1986]: https://doi.org/10.1109/cdc.1986.267487
[research_soehne_1956]: https://ntrs.nasa.gov/citations/20050019614
[research_soemarwoto_labrujere_2000]: https://doi.org/10.1016/b978-008043693-7/50116-1
[research_soinne_1999]: https://doi.org/10.2514/6.1999-3147
[research_solartepineda_bravomosquera_2026]: https://doi.org/10.2514/1.c038573
[research_solies_1994]: https://doi.org/10.2514/3.46602
[research_solies_1994_b]: https://doi.org/10.2514/3.46495
[research_solies_1994_c]: https://ntrs.nasa.gov/citations/19950016905
[research_song_jeon_1995]: https://doi.org/10.2514/6.1995-3497
[research_song_wong_2025]: https://doi.org/10.2514/6.2025-2185
[research_song_yang_2014]: https://doi.org/10.1016/j.cja.2014.08.003
[research_sonneveldt_chu_2011]: https://doi.org/10.5772/13839
[research_sorensen_tyler_1972]: https://doi.org/10.2514/6.1972-963
[research_soudakov_petrov_2017]: https://doi.org/10.2514/6.2017-0489
[research_soule_1937]: https://ntrs.nasa.gov/citations/19930091661
[research_soule_1940]: https://ntrs.nasa.gov/citations/19930091777
[research_soule_wetmore_1933]: https://ntrs.nasa.gov/citations/19930081319
[research_soule_wheatley_1934]: https://ntrs.nasa.gov/citations/19930091516
[research_spacht_1980]: https://doi.org/10.2514/6.1980-1885
[research_spaid_1984]: https://doi.org/10.2514/6.1984-100
[research_spain_soistmann_1990]: https://ntrs.nasa.gov/citations/19910029821
[research_sparks]: https://doi.org/10.1109/cca.1998.728594
[research_sparks_sparks_1997]: https://doi.org/10.2514/6.1997-3636
[research_spearman_1983]: https://ntrs.nasa.gov/citations/19830009237
[research_spearman_driver_1955]: https://ntrs.nasa.gov/citations/19930090584
[research_spearman_driver_1959]: https://ntrs.nasa.gov/citations/19980228222
[research_spearman_robinson_1956]: https://ntrs.nasa.gov/citations/20050028458
[research_speyer_crues_1985]: https://doi.org/10.2514/6.1985-1762
[research_speyer_crues_1987]: https://doi.org/10.2514/3.20212
[research_spin_research_summary_1979]: https://ntrs.nasa.gov/citations/19790052693
[research_spooner_martina_1948]: https://ntrs.nasa.gov/citations/19930085375
[research_spreemann_1959]: https://ntrs.nasa.gov/citations/19630003100
[research_spreemann_few_1954]: https://ntrs.nasa.gov/citations/20090026295
[research_spreiter_stahara_1971]: https://doi.org/10.2514/3.49980
[research_srinathkumar_madhuranath_1993]: https://doi.org/10.2514/6.1993-3620
[research_srinathkumar_parameswaran_1995]: https://doi.org/10.2514/6.1995-3501
[research_srinivasan_mccroskey_1986]: https://doi.org/10.21236/ada169116
[research_srivastava_kumar_2017]: https://doi.org/10.1109/icraae.2017.8297218
[research_srour_noura_2021]: https://doi.org/10.1109/systol52990.2021.9594939
[research_stability_and_1986]: https://doi.org/10.2514/6.1986-2231
[research_stability_characteristics_2014]: https://doi.org/10.2514/5.9781624102547.0665.0680
[research_stability_characteristics_2024]: https://doi.org/10.2514/5.9781624107252.0735.0750
[research_staelens_blackwelder_2007]: https://doi.org/10.2514/6.2007-68
[research_stalford_1979]: https://doi.org/10.21236/ada080025
[research_stalford_1980]: https://doi.org/10.2514/6.1980-1631
[research_stall_characteristics_2003]: https://doi.org/10.2514/5.9781600861840.0365.0382
[research_stall_speed_2003]: https://doi.org/10.2514/5.9781600861840.0039.0052
[research_stam_devisser_2025]: https://doi.org/10.2514/6.2025-0082
[research_stancil_1979]: https://doi.org/10.2514/3.58481
[research_stanewsky_little_1971]: https://doi.org/10.2514/3.59192
[research_stanford_2016]: https://doi.org/10.2514/1.c033613
[research_stanford_jacobson_2020]: https://doi.org/10.2514/6.2020-2716
[research_stanford_jacobson_2023]: https://doi.org/10.2514/6.2023-0589
[research_stanford_jacobson_2024]: https://doi.org/10.2514/1.c037679
[research_stargill_1983]: https://doi.org/10.2514/6.1983-2132
[research_static_aeroelasticity_2014]: https://doi.org/10.1002/9781118700440.ch8
[research_static_aeroelasticity_2014_b]: https://doi.org/10.1002/9781118700440.ch7
[research_static_flight_2026]: https://doi.org/10.1017/9781009399913.011
[research_static_longitudinal_2003]: https://doi.org/10.2514/5.9781600861840.0223.0233
[research_static_longitudinal_2003_b]: https://doi.org/10.2514/5.9781600861840.0209.0222
[research_staufenbiel_schlichting_1988]: https://doi.org/10.2514/3.45562
[research_stebbins_loth_2022]: https://doi.org/10.2514/6.2022-1170
[research_steer_2000]: https://doi.org/10.2514/6.2000-4109
[research_steer_2003]: https://doi.org/10.2514/6.2003-5308
[research_steers_iliff_1975]: https://ntrs.nasa.gov/citations/19750010172
[research_steger_bailey_1979]: https://doi.org/10.2514/6.1979-134
[research_stegmuller_haybock_2026]: https://doi.org/10.2514/1.c038577
[research_stegmuller_katzenmeier_2022]: https://doi.org/10.1007/s13272-022-00593-3
[research_steimle_schroder_2008]: https://doi.org/10.2514/6.2008-6908
[research_steimle_schroder_2010]: https://doi.org/10.1007/978-3-642-04088-7_13
[research_steinbach_1997]: https://doi.org/10.2514/2.2195
[research_stenfelt_ringertz_2009]: https://doi.org/10.2514/1.41092
[research_stenfelt_ringertz_2010]: https://doi.org/10.2514/1.c031017
[research_stenfelt_ringertz_2013]: https://doi.org/10.2514/1.c031868
[research_stengel_1973]: https://doi.org/10.2514/3.44358
[research_stengel_1976]: https://ntrs.nasa.gov/citations/19770003440
[research_stengel_1981]: https://doi.org/10.2514/6.1981-1889
[research_stengel_1983]: https://doi.org/10.2514/3.56341
[research_stengel_1985]: https://doi.org/10.2514/6.1985-1789
[research_stengel_berry_1976]: https://doi.org/10.2514/6.1976-1973
[research_stengel_berry_1977]: https://ntrs.nasa.gov/citations/19770014156
[research_stengel_miller_1978]: https://doi.org/10.2514/6.1978-1361
[research_stepanyan_kalmanje_2010]: https://doi.org/10.2514/6.2010-3490
[research_stephenson_hardy_1989]: https://ntrs.nasa.gov/citations/19900008323
[research_stephenson_jeske_1990]: https://ntrs.nasa.gov/citations/19900014097
[research_stephenson_selan_1955]: https://ntrs.nasa.gov/citations/19930088699
[research_sternfield_gates_1949]: https://ntrs.nasa.gov/citations/19930082531
[research_stevens_mccormack_1944]: https://ntrs.nasa.gov/citations/19890067903
[research_stickan_dillinger_2014]: https://doi.org/10.1016/j.jfluidstructs.2014.04.014
[research_stojakovic]: https://doi.org/10.2298/bg20120711stojakovic
[research_stone_1950]: https://ntrs.nasa.gov/citations/19930086136
[research_stone_daughtridge_1948]: https://ntrs.nasa.gov/citations/20050019380
[research_stone_naylor_1972]: https://doi.org/10.1109/cdc.1972.268998
[research_stough_dicarlo_1987]: https://ntrs.nasa.gov/citations/19870014181
[research_stough_kauffman_1950]: https://ntrs.nasa.gov/citations/19930082844
[research_strass_1948]: https://ntrs.nasa.gov/citations/19930085597
[research_strass_1954]: https://ntrs.nasa.gov/citations/19930088106
[research_strass_fields_1951]: https://ntrs.nasa.gov/citations/19930086810
[research_strass_fields_1952]: https://ntrs.nasa.gov/citations/19930087886
[research_strass_marley_1952]: https://ntrs.nasa.gov/citations/19930086907
[research_strass_tucker_1954]: https://ntrs.nasa.gov/citations/19930088308
[research_streett_1981]: https://doi.org/10.2514/6.1981-1266
[research_streett_1982]: https://doi.org/10.2514/3.51149
[research_strelkov_kharlamov_1967]: https://doi.org/10.1007/bf01040744
[research_strutz_1972]: https://ntrs.nasa.gov/citations/19720023253
[research_studwell_wu_1973]: https://doi.org/10.2514/3.60273
[research_su_chow_1993]: https://doi.org/10.2514/6.1993-3024
[research_su_chow_1995]: https://doi.org/10.2514/3.46815
[research_su_hu_2022]: https://doi.org/10.1155/2022/6515234
[research_su_hu_2023]: https://doi.org/10.1088/1742-6596/2477/1/012094
[research_su_zhou_2014]: https://doi.org/10.4028/www.scientific.net/amm.543-547.348
[research_suarez_kramer_1992]: https://doi.org/10.2514/6.1992-2716
[research_suarez_smith_1993]: https://doi.org/10.2514/6.1993-187
[research_suarez_smith_1993_b]: https://ntrs.nasa.gov/citations/19940011307
[research_suchomel_1987]: https://doi.org/10.2514/6.1987-347
[research_sudderth_bohn_1975]: https://ntrs.nasa.gov/citations/19750012273
[research_sudderth_mcneill_1976]: https://ntrs.nasa.gov/citations/19770011062
[research_sudha_deodhare_2018]: https://doi.org/10.2514/1.c034585
[research_sudhakar_prem_2026]: https://doi.org/10.1017/aer.2026.10189
[research_sugimoto_1992]: https://doi.org/10.2514/3.46234
[research_sugioka_koike_2018]: https://doi.org/10.1007/s00348-018-2565-5
[research_sugioka_nakakita_2021]: https://doi.org/10.1007/s00348-020-03118-y
[research_sugioka_numata_2015]: https://doi.org/10.2514/6.2015-0025
[research_suikat_donaldson_1987]: https://ntrs.nasa.gov/citations/19880027050
[research_suikat_donaldson_1989]: https://ntrs.nasa.gov/citations/19890014099
[research_suleman_2007]: https://doi.org/10.21236/ada525877
[research_suleman_crawford_2000]: https://doi.org/10.1115/imece2000-1711
[research_suleman_crawford_2002]: https://doi.org/10.1177/104538902761402477
[research_sullivan_1978]: https://doi.org/10.2514/3.58461
[research_summey_smetana_1977]: https://ntrs.nasa.gov/citations/19770013083
[research_sun_hu_2005]: https://doi.org/10.1515/ijnsns.2005.6.1.25
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_wang_2026]: https://doi.org/10.1016/j.ast.2026.112004
[research_sun_xu_2021]: https://doi.org/10.1109/ccdc52312.2021.9601687
[research_sun_zhou_2021]: https://doi.org/10.1016/j.ast.2021.106638
[research_sun_zhou_2024]: https://doi.org/10.1016/j.isatra.2023.10.024
[research_sundar_1978]: https://doi.org/10.2514/6.1978-833
[research_sundaram_wu_1983]: https://doi.org/10.2514/6.1983-1852
[research_suplisson_brandt_2011]: https://doi.org/10.2514/6.2011-7038
[research_suresh_radhakrishnan_2010]: https://doi.org/10.1260/1757-2258.2.3.189
[research_suresh_radhakrishnan_2013]: https://doi.org/10.1016/j.ast.2011.10.012
[research_suresh_siddesh_2012]: https://doi.org/10.1260/1757-2258.4.3-4.103
[research_susanto_2022]: https://doi.org/10.24843/mite.2022.v21i02.p19
[research_sutherland_1893]: https://doi.org/10.1080/14786449308620508
[research_swaim_1978]: https://doi.org/10.2514/6.1978-1365
[research_swaim_1980]: https://doi.org/10.2514/6.1980-1835
[research_swaim_fullman_1977]: https://doi.org/10.2514/3.58867
[research_sweberg_1942]: https://ntrs.nasa.gov/citations/19930092659
[research_sweberg_1945]: https://ntrs.nasa.gov/citations/19930092476
[research_szema_shankar_1984]: https://doi.org/10.2514/6.1984-427
[research_szwabowski_baker_2023]: https://doi.org/10.2514/6.2023-3949
[research_taboada_boschetti_2018]: https://doi.org/10.2514/6.2018-0776
[research_tahir_wing_rock_2026]: https://doi.org/10.2514/1.c038034
[research_tai_wang_2023]: https://doi.org/10.3390/aerospace10040350
[research_tail_size_effect_1952]: https://ntrs.nasa.gov/citations/19930092137
[research_tailless_delta_lowspeed_1959]: https://ntrs.nasa.gov/citations/19980232080
[research_tailless_freeflight_1956]: https://ntrs.nasa.gov/citations/19630004110
[research_tailless_highspeed_1943]: https://ntrs.nasa.gov/citations/19930092578
[research_tailless_interim_1944]: https://ntrs.nasa.gov/citations/19770022126
[research_tailless_transonic_est_1976]: https://ntrs.nasa.gov/citations/19770022131
[research_tailless_triangular_1956]: https://ntrs.nasa.gov/citations/19930084649
[research_takeda_1970]: https://doi.org/10.5100/jje.6.137
[research_talmage_reeder_1947]: https://ntrs.nasa.gov/citations/20050019271
[research_tamaki_kawai_2023]: https://doi.org/10.2514/6.2023-0429
[research_tamayama_kheirandish_2003]: https://doi.org/10.2322/tjsass.46.186
[research_tan_wang_2017]: https://doi.org/10.2514/6.2017-3960
[research_tan_wang_2018]: https://doi.org/10.2514/6.2018-3898
[research_tan_wu_2014]: https://doi.org/10.1109/icsai.2014.7009296
[research_tan_yang_2025]: https://doi.org/10.1109/icccr65461.2025.11072631
[research_tan_zhou_2014]: https://doi.org/10.4028/www.scientific.net/amr.940.419
[research_tang_1971]: https://ntrs.nasa.gov/citations/19710015105
[research_tang_2019]: https://doi.org/10.2514/6.2019-3274
[research_tang_dowell_1995]: https://doi.org/10.2514/3.46837
[research_tang_dowell_2013]: https://doi.org/10.2514/1.j051781
[research_tang_pearson_1971]: https://ntrs.nasa.gov/citations/19710029224
[research_tanner_montgomery_1979]: https://ntrs.nasa.gov/citations/19790011963
[research_tantaroudas_daronch_2015]: https://doi.org/10.2514/6.2015-0240
[research_tanveer_ahmad_2023]: https://doi.org/10.3390/asec2023-15315
[research_tanveer_ahmad_2023_b]: https://doi.org/10.3390/aerospace10060563
[research_taraborrelli_2023]: https://doi.org/10.21741/9781644902813-92
[research_tarn_hsu]: https://doi.org/10.1109/tencon.1992.271877
[research_tarn_hsu_1993]: https://doi.org/10.23919/acc.1993.4793048
[research_tatar_masdari_2019]: https://doi.org/10.1016/j.ast.2019.06.046
[research_taufik_zaidaan_2024]: https://doi.org/10.1109/icspc63060.2024.10862738
[research_taylor_1952]: https://doi.org/10.1108/eb032201
[research_taylor_2012]: https://doi.org/10.2514/6.2012-4410
[research_taylor_pamadi_1983]: https://doi.org/10.2514/6.1983-2086
[research_taylor_peake_1997]: https://doi.org/10.2514/6.1997-1777
[research_taylor_ratnayake_2011]: https://doi.org/10.2514/6.2011-6276
[research_taylor_robinson_1965]: https://ntrs.nasa.gov/citations/19730062066
[research_taylor_yoo_2011]: https://doi.org/10.2514/6.2011-6253
[research_teel_1999]: https://doi.org/10.21236/ada367415
[research_teel_1999_b]: https://doi.org/10.21236/ada367012
[research_telionis_1990]: https://doi.org/10.21236/ada231946
[research_telionis_1995]: https://doi.org/10.21236/ada299820
[research_telionis_2001]: https://doi.org/10.21236/ada398139
[research_teofilatto_2001]: https://doi.org/10.1016/s1369-8869(00)00025-2
[research_teperin_teperina_2018]: https://doi.org/10.1615/tsagiscij.2018029236
[research_teplitz_kayten_1946]: https://ntrs.nasa.gov/citations/20040085365
[research_terrell_zeinsabatto_2017]: https://doi.org/10.1109/secon.2017.7925309
[research_test_techniques_2021]: https://doi.org/10.1016/c2018-0-00829-4
[research_tewari_2000]: https://doi.org/10.2514/6.2000-4251
[research_tewes_taubert_2015]: https://doi.org/10.2514/6.2015-0783
[research_thacker_lan_1993]: https://doi.org/10.2514/6.1993-3617
[research_the_effects_1977]: https://doi.org/10.1016/0022-460x(77)90512-0
[research_the_effects_1988]: https://doi.org/10.2514/6.1988-2514
[research_the_effects_1989]: https://doi.org/10.2514/6.1989-836
[research_the_stability_1979]: https://doi.org/10.2514/6.1979-1495
[research_the_transformation_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50025-3
[research_the_transformation_2007]: https://doi.org/10.1016/b978-075066927-6/50026-x
[research_thelander_1965]: https://doi.org/10.21236/ad0617354
[research_theodore_malpica_2014]: https://ntrs.nasa.gov/citations/20180008501
[research_theodorsen_1935]: https://ntrs.nasa.gov/citations/19800006788
[research_thomas_burley_2010]: https://ntrs.nasa.gov/citations/20100023399
[research_thomas_dowell_2001]: https://doi.org/10.2514/6.2001-1209
[research_thomas_dowell_2015]: https://doi.org/10.2514/6.2015-3435
[research_thomas_dowell_2020]: https://doi.org/10.2514/6.2020-3137
[research_thomas_holst_1983]: https://doi.org/10.2514/6.1983-499
[research_thomas_wolhart_1957]: https://ntrs.nasa.gov/citations/19930085077
[research_thomasaharris_1935]: https://ntrs.nasa.gov/citations/19930091601
[research_thompson_bray_1950]: https://ntrs.nasa.gov/citations/19930090286
[research_thompson_gilruth_1940]: https://ntrs.nasa.gov/citations/19930081526
[research_thompson_moseley_1956]: https://ntrs.nasa.gov/citations/19930089197
[research_thomson_1946]: https://doi.org/10.2514/8.11345
[research_three_dimensional_boundary_layer_1994]: https://doi.org/10.2514/6.1994-2375
[research_tian_feng_2017]: https://doi.org/10.2514/1.c033574
[research_tigner_holden_1998]: https://doi.org/10.2514/6.1998-4831
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_timme_2020]: https://doi.org/10.1017/jfm.2019.1001
[research_timme_thormann_2016]: https://doi.org/10.2514/6.2016-3848
[research_ting_ayoubi_2012]: https://doi.org/10.2514/6.2012-2580
[research_ting_ayoubi_2013]: https://doi.org/10.2514/1.i010053
[research_tingting_aijun_2014]: https://doi.org/10.1109/icarcv.2014.7064295
[research_tipton_smith_1995]: https://doi.org/10.4271/952053
[research_tipton_smith_1996]: https://doi.org/10.2514/6.1996-408
[research_tischler_2018]: https://doi.org/10.1201/9781315136820-2
[research_tischler_2018_b]: https://doi.org/10.1201/9781315136820
[research_tleulinov_jafarzade_2019]: https://doi.org/10.1088/1742-6596/1158/4/042027
[research_tobak_1953]: https://ntrs.nasa.gov/citations/19930087459
[research_tobak_reese_1950]: https://ntrs.nasa.gov/citations/19930086385
[research_toffol_paolini_2025]: https://doi.org/10.2514/6.2025-1853
[research_tohidi_yildiz_2018]: https://doi.org/10.1109/ccta.2018.8511389
[research_tohidi_yildiz_2019]: https://doi.org/10.23919/ecc.2019.8795847
[research_tokutake_fujinaga_2006]: https://doi.org/10.2514/6.2006-6225
[research_tokutake_fujinaga_2008]: https://doi.org/10.1017/s0001924000002153
[research_tokutake_itoh]: https://doi.org/10.1109/sice.2002.1196598
[research_tokutake_sato_2003]: https://doi.org/10.2514/6.2003-5549
[research_tomac_stenfelt_2014]: https://doi.org/10.1016/j.ast.2014.09.007
[research_tomczyk_2008]: https://doi.org/10.2514/6.2008-6352
[research_tomek_boyden_2000]: https://ntrs.nasa.gov/citations/20040086749
[research_tomek_ullah_2020]: https://doi.org/10.2514/6.2020-1980
[research_tonon_belluati_2018]: https://doi.org/10.1201/9781315136820-11
[research_torenbeek_2016]: https://doi.org/10.1002/9780470686652.eae1003
[research_torvik_1990]: https://doi.org/10.21236/ada229487
[research_tournes_johnson_1999]: https://doi.org/10.2514/6.1999-3982
[research_tournes_shtessel_1997]: https://doi.org/10.2514/6.1997-3633
[research_tourrette_1996]: https://doi.org/10.2514/6.1996-2034
[research_tousi_bajaj_1988]: https://doi.org/10.1080/00423118808968894
[research_traas_atmaca_2026]: https://doi.org/10.2514/6.2026-0549
[research_trailing_edge_2006]: https://doi.org/10.2514/5.9781600866838.0245.0276
[research_tran_lind_2010]: https://doi.org/10.2514/6.2010-8227
[research_tran_sakamoto_2017]: https://doi.org/10.1016/j.ast.2017.05.010
[research_trankle_rabin_1983]: https://doi.org/10.2514/6.1983-2098
[research_transformation_of_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00032-8
[research_transonic_aircraft_2012]: https://doi.org/10.2514/5.9781600869174.0171.0220
[research_transonic_airfoil_1986]: https://doi.org/10.1016/b978-0-444-87958-5.50008-x
[research_transonic_and_1992]: https://doi.org/10.1017/cbo9780511607134.012
[research_transonic_computational_1982]: https://doi.org/10.2514/5.9781600865558.0451.0465
[research_transonic_flight_1994]: https://doi.org/10.2514/6.1994-2142
[research_transonic_navier_stokes_1972]: https://doi.org/10.2514/3.46413
[research_trim_and_2017]: https://doi.org/10.1002/9781118534786.app5
[research_triplett_1980]: https://doi.org/10.2514/6.1980-794
[research_tseng_gupta_2006]: https://ntrs.nasa.gov/citations/20060019186
[research_tsuchiya_takahashi_2022]: https://doi.org/10.1299/jsmermd.2022.1a1-j06
[research_tu_marzanek_2019]: https://doi.org/10.2514/6.2019-2165
[research_tu_yan_2024]: https://doi.org/10.1007/s42405-024-00735-3
[research_tucker_quinn_1944]: https://ntrs.nasa.gov/citations/19930092795
[research_tufts_reed_2013]: https://doi.org/10.2514/6.2013-2411
[research_tumbling_characteristics_1993]: https://ntrs.nasa.gov/citations/19930064305
[research_turn_performance_2021]: https://doi.org/10.2514/5.9781624105920.0623.0676
[research_turner_cooper_1947]: https://ntrs.nasa.gov/citations/20030063925
[research_twisdale_kirsten_1984]: https://doi.org/10.2514/3.19871
[research_ueno_matsuno_1998]: https://doi.org/10.2514/6.1998-2520
[research_ueno_sarae_2004]: https://doi.org/10.2514/6.2004-4943
[research_ulbrich_2006]: https://doi.org/10.2514/6.2006-519
[research_ulhaq_atmaca_2026]: https://doi.org/10.2514/6.2026-1744
[research_ullah_fabijanic_2022]: https://doi.org/10.2514/6.2022-3392
[research_ullah_tomek_2021]: https://doi.org/10.3390/fluids6120457
[research_ulrich_roche_2001]: https://doi.org/10.1007/978-3-540-45359-8_32
[research_ummeaymon_shah_2016]: https://doi.org/10.1109/icet.2016.7813243
[research_uncommanded_lateral_2003]: https://ntrs.nasa.gov/citations/20030010279
[research_underwood_1942]: https://ntrs.nasa.gov/citations/19930092755
[research_unen_yildiz_2025]: https://doi.org/10.2139/ssrn.5745146
[research_urbano]: https://doi.org/10.70675/2b693b33z65d9z4febz924azb275085bbb6b
[research_uribequintero_takahashi_2024]: https://doi.org/10.2514/6.2024-4048
[research_urie_reaser_1979]: https://doi.org/10.2514/6.1979-1653
[research_urnes_2012]: https://doi.org/10.2514/6.2012-2570
[research_urnes_yeager_1991]: https://doi.org/10.2514/6.1991-3106
[research_use_of_2022]: https://doi.org/10.1002/9781119988281.ch1
[research_uselton_1978]: https://doi.org/10.2514/6.1978-830
[research_uybarreta_grant_2025]: https://doi.org/10.2514/6.2025-3613
[research_uybarreta_kabaliuk_2024]: https://doi.org/10.2514/6.2024-4491
[research_valej_2013]: https://doi.org/10.4172/2168-9792.1000119
[research_valentin_2011]: https://doi.org/10.13111/2066-8201.2011.3.1.9
[research_vallone]: https://doi.org/10.15368/theses.2010.146
[research_vanarnhem_devries_2019]: https://doi.org/10.2514/6.2019-3036
[research_vandam_1985]: https://doi.org/10.4271/851770
[research_vandam_1986]: https://doi.org/10.2514/6.1986-1824
[research_vandermaas_1959]: https://doi.org/10.1016/b978-1-4831-9730-2.50014-4
[research_vandervelden_1987]: https://ntrs.nasa.gov/citations/19880013507
[research_vandierendonck_1973]: https://doi.org/10.2514/6.1973-159
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vanpelt_1981]: https://doi.org/10.2514/6.1981-2375
[research_vanthullenar_1957]: https://doi.org/10.1080/00431672.1957.9924976
[research_vardaki_gursul_2004]: https://doi.org/10.2514/6.2004-4729
[research_vatsa_1987]: https://doi.org/10.2514/3.45456
[research_vatsa_wedan_1988]: https://doi.org/10.2514/6.1988-102
[research_vaughn_lindsay_1988]: https://doi.org/10.2514/6.1988-2102
[research_veismann_2023]: https://doi.org/10.2514/1.j062561
[research_velden_1997]: https://doi.org/10.1007/978-3-7091-2658-5_19
[research_velger_shinar_1983]: https://doi.org/10.2514/3.44823
[research_velicki_thrash_2010]: https://doi.org/10.1017/s0001924000004000
[research_velkova_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.1
[research_vensel_1942]: https://ntrs.nasa.gov/citations/19930092582
[research_vepa_2023]: https://doi.org/10.1201/9781003266310-8
[research_vepa_2023_b]: https://doi.org/10.1201/9781003266310-10
[research_vepa_2023_c]: https://doi.org/10.1201/9781003266310-4
[research_vepa_2023_d]: https://doi.org/10.1201/9781003266310
[research_verma_kulkarni_2024]: https://doi.org/10.1088/2631-8695/ad937d
[research_vertical_fin_location_1951]: https://ntrs.nasa.gov/citations/19930086584
[research_vertical_tail_1996]: https://doi.org/10.2514/5.9781600862465.0143.0161
[research_vetter_2002]: https://ntrs.nasa.gov/citations/20020079425
[research_vey_greenblatt_2010]: https://doi.org/10.2514/6.2010-4865
[research_vianto_tobing_2021]: https://doi.org/10.47355/avia.v3i2.49
[research_vile_alwi_2019]: https://doi.org/10.23919/acc.2019.8814298
[research_vile_alwi_2019_b]: https://doi.org/10.1109/cdc40024.2019.9030030
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vile_alwi_2021]: https://doi.org/10.1109/systol52990.2021.9595385
[research_vincent_botez_2015]: https://doi.org/10.2514/6.2015-0904
[research_vincent_franklin_1981]: https://doi.org/10.2514/6.1981-2449
[research_vindigni_2024]: https://doi.org/10.21741/9781644903193-27
[research_vindigni_mantegna_2024]: https://doi.org/10.1016/j.jsv.2023.118151
[research_vindigni_mantegna_2024_b]: https://doi.org/10.1088/1742-6596/2746/1/012007
[research_visbal_2017]: https://doi.org/10.1103/physrevfluids.2.024703
[research_visbal_garmann_2012]: https://doi.org/10.1115/fedsm2012-72405
[research_vishwanathan]: https://doi.org/10.33915/etd.1816
[research_visonneau_guilmineau_2022]: https://doi.org/10.2514/6.2022-0027
[research_vitale_1954]: https://ntrs.nasa.gov/citations/19930083881
[research_volkl_breitsamter_2026]: https://doi.org/10.1007/978-3-032-11115-9_52
[research_volkl_weiner_2026]: https://doi.org/10.2139/ssrn.7193341
[research_volpe_grossman_1978]: https://doi.org/10.21236/ada058425
[research_volpe_jameson_1990]: https://doi.org/10.2514/3.45923
[research_vos_brown_2002]: https://doi.org/10.2514/6.2002-3428
[research_voss_frohler_2026]: https://doi.org/10.2514/6.2026-4001
[research_waggoner_1980]: https://doi.org/10.2514/6.1980-129
[research_waggoner_1982]: https://doi.org/10.2514/6.1982-163
[research_wahler_varriale_2023]: https://doi.org/10.2514/6.2023-3485
[research_wakayama_1998]: https://doi.org/10.2514/6.1998-4938
[research_wakayama_2000]: https://doi.org/10.2514/6.2000-4740
[research_wakayama_2008]: https://ntrs.nasa.gov/citations/20090002563
[research_wakayama_kroo_1998]: https://doi.org/10.2514/6.1998-4736
[research_wakefield_1959]: https://ntrs.nasa.gov/citations/19630003104
[research_walchli_langan_1999]: https://doi.org/10.2514/6.1999-3194
[research_waldmann_ehrle_2023]: https://doi.org/10.1007/s00348-023-03642-7
[research_waldmann_lutz_2019]: https://doi.org/10.2514/6.2019-2315
[research_walker_1940]: https://doi.org/10.1108/eb030696
[research_walker_1987]: https://doi.org/10.2514/6.1987-239
[research_walker_ballantyne_1950]: https://ntrs.nasa.gov/citations/19930082846
[research_walkley_1986]: https://doi.org/10.2514/6.1986-2627
[research_walkley_smith_1987]: https://doi.org/10.2514/3.45487
[research_wallace_1942]: https://ntrs.nasa.gov/citations/19930092566
[research_wallace_1944]: https://ntrs.nasa.gov/citations/19930092678
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_wallace_recant_1943]: https://ntrs.nasa.gov/citations/19930093673
[research_walsh_1992]: https://ntrs.nasa.gov/citations/19920066278
[research_walsh_1993]: https://ntrs.nasa.gov/citations/19930013934
[research_waltercwilliams_herberthhoover_1945]: https://ntrs.nasa.gov/citations/20150019958
[research_walton_katz_1992]: https://ntrs.nasa.gov/citations/19920043109
[research_walton_katz_1993]: https://ntrs.nasa.gov/citations/19930061155
[research_wang_1979]: https://doi.org/10.21236/ada074260
[research_wang_aeroelastic_2019]: https://doi.org/10.1063/1.5087963
[research_wang_bwb_airworthiness_2022]: https://doi.org/10.1016/j.cja.2021.09.002
[research_wang_caughey_1992]: https://doi.org/10.2514/3.46269
[research_wang_criteria_2021]: https://doi.org/10.3390/aerospace8120360
[research_wang_feng_2025]: https://doi.org/10.1063/5.0251122
[research_wang_feng_2026]: https://doi.org/10.2514/1.j066379
[research_wang_guo_2012]: https://doi.org/10.1504/ijmic.2012.046692
[research_wang_guo_2017]: https://doi.org/10.1016/j.cja.2017.03.004
[research_wang_herbert_1994]: https://doi.org/10.2514/6.1994-2374
[research_wang_herbert_1994_b]: https://doi.org/10.2514/6.1994-180
[research_wang_hou_2021]: https://doi.org/10.1109/cac53003.2021.9727458
[research_wang_hu_2023]: https://doi.org/10.3390/aerospace10020198
[research_wang_lan_1999]: https://doi.org/10.2514/6.1999-4012
[research_wang_lan_2002]: https://doi.org/10.2514/6.2002-4626
[research_wang_li_2026]: https://doi.org/10.3390/drones10080601
[research_wang_liu_2024]: https://doi.org/10.23919/iccas63016.2024.10773270
[research_wang_liu_2025]: https://doi.org/10.1007/s42401-025-00344-2
[research_wang_liu_2026]: https://doi.org/10.2139/ssrn.6635080
[research_wang_qi_2021]: https://doi.org/10.1088/1742-6596/1924/1/012005
[research_wang_rotating_wingtip_2025]: https://doi.org/10.3390/aerospace12080688
[research_wang_santone_2012]: https://doi.org/10.1155/2012/394791
[research_wang_sun_2024]: https://doi.org/10.3390/aerospace11050366
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_tang_2020]: https://doi.org/10.1088/1742-6596/1509/1/012022
[research_wang_tvsas_2024]: https://doi.org/10.1016/j.cja.2024.05.002
[research_wang_wan_2019]: https://doi.org/10.2514/6.2019-0004
[research_wang_wang_2012]: https://doi.org/10.1016/s1000-9361(11)60412-3
[research_wang_wang_2012_b]: https://doi.org/10.2991/iccasm.2012.209
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_yin_2020]: https://doi.org/10.1088/1757-899x/887/1/012035
[research_wang_zhang_2012]: https://doi.org/10.1007/s11431-012-4987-2
[research_wang_zhang_2018]: https://doi.org/10.1109/icarcv.2018.8581089
[research_wang_zhang_2020]: https://doi.org/10.1016/j.cja.2020.03.016
[research_wang_zhang_2024]: https://doi.org/10.1016/j.cja.2024.03.034
[research_wang_zhang_2024_b]: https://doi.org/10.1007/978-981-97-1654-8_2
[research_wang_zhang_2025]: https://doi.org/10.1109/icus66297.2025.11295617
[research_wang_zhao_2024]: https://doi.org/10.2139/ssrn.5001796
[research_wang_zhao_2025]: https://doi.org/10.3390/math13152375
[research_wang_zhao_latdir_2022]: https://doi.org/10.3390/aerospace9080433
[research_wang_zhou_2023]: https://doi.org/10.22541/au.170019911.18793089/v1
[research_wanner_1973]: https://doi.org/10.1017/s0001924000042032
[research_ward_1949]: https://doi.org/10.1017/s0001925900000056
[research_ward_1968]: https://doi.org/10.2514/3.43928
[research_warner_onstott_1986]: https://ntrs.nasa.gov/citations/19860023540
[research_warren_hassan_1997]: https://doi.org/10.2514/6.1997-2245
[research_warsop_crowther_2019]: https://doi.org/10.2514/6.2019-0044
[research_washizu_osuga_1960]: https://doi.org/10.2322/jjsass1953.8.249
[research_wasicko_1972]: https://ntrs.nasa.gov/citations/19720024388
[research_waters_voskuijl_2013]: https://doi.org/10.1016/j.ast.2013.01.004
[research_wawrzyniak_1970]: https://ntrs.nasa.gov/citations/19700028513
[research_wei_1985]: https://doi.org/10.2514/6.1985-1902
[research_wei_zheng_2024]: https://doi.org/10.3390/app14135463
[research_weick_harris_1934]: https://ntrs.nasa.gov/citations/19930091518
[research_weick_noyes_1933]: https://ntrs.nasa.gov/citations/19930081241
[research_weick_wenzinger_1932]: https://ntrs.nasa.gov/citations/19930081207
[research_weil_1981]: https://ntrs.nasa.gov/citations/19810017618
[research_weil_spear_1947]: https://ntrs.nasa.gov/citations/20050019466
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weingarten_chalk_1984]: https://doi.org/10.2514/3.8550
[research_weinstein_hubbard_2018]: https://doi.org/10.2514/6.2018-3313
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1983]: https://ntrs.nasa.gov/citations/19840055636
[research_weisshaar_zeiler_1982]: https://doi.org/10.2514/6.1982-1325
[research_wells_2002]: https://doi.org/10.21236/ada398917
[research_wells_hess_2002]: https://doi.org/10.2514/6.2002-4650
[research_wells_hess_2003]: https://doi.org/10.2514/2.5084
[research_weltz_shweyk_2007]: https://doi.org/10.2514/6.2007-6387
[research_wen_deng_2013]: https://doi.org/10.1016/j.proeng.2013.12.032
[research_wendel_1987]: https://doi.org/10.2514/6.1987-2880
[research_wenqian_efremov_2010]: https://doi.org/10.1016/s1000-9361(09)60248-x
[research_wenqiang_jianjun_2008]: https://doi.org/10.3182/20080706-5-kr-1001.01009
[research_wentz_nyenhuis_1984]: https://doi.org/10.2514/6.1984-2189
[research_werner_henne_2024]: https://doi.org/10.2514/6.2024-2333
[research_westbrook_1965]: https://doi.org/10.2514/6.1965-313
[research_westermayer_schirrer_2010]: https://doi.org/10.3182/20100906-5-jp-2022.00005
[research_westin_defreitaspinto_2008]: https://doi.org/10.4271/2008-36-0247
[research_wetmore_1939]: https://ntrs.nasa.gov/citations/19930081477
[research_wetmore_turner_1940]: https://ntrs.nasa.gov/citations/19930091772
[research_wetzel_1954]: https://ntrs.nasa.gov/citations/20090025891
[research_weyl_1944]: https://doi.org/10.1108/eb031199
[research_weyl_1945]: https://doi.org/10.1108/eb031237
[research_weyl_1945_b]: https://doi.org/10.1108/eb031247
[research_weyl_1945_c]: https://doi.org/10.1108/eb031217
[research_weyl_1945_d]: https://doi.org/10.1108/eb031288
[research_weyl_1945_e]: https://doi.org/10.1108/eb031306
[research_wheldon_whites_1966]: https://doi.org/10.2514/6.1966-734
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_white_saric_2001]: https://doi.org/10.2514/6.2001-271
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_wienke_bertsch_2023]: https://doi.org/10.2514/6.2023-4170
[research_wildschek_2014]: https://doi.org/10.2514/6.2014-0599
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_williams_drake_1948]: https://ntrs.nasa.gov/citations/19650070849
[research_williams_inelson_1995]: https://doi.org/10.2514/6.1995-3441
[research_williams_niestroy_2025]: https://doi.org/10.2514/6.2025-1451
[research_willig_1968]: https://doi.org/10.2514/3.43959
[research_wilmott_1986]: https://doi.org/10.1017/s0001924000015347
[research_wilson_buckley_1990]: https://doi.org/10.2514/6.1990-2806
[research_wilson_citurs_1994]: https://ntrs.nasa.gov/citations/19950007833
[research_wilson_hall_1991]: https://doi.org/10.4271/912149
[research_wilson_peters_2014]: https://doi.org/10.2514/6.2014-0602
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wing_buffet_2021]: https://doi.org/10.15372/pmtf20210215
[research_wing_tunnel_1998]: https://doi.org/10.1108/aeat.1998.12770ead.003
[research_wing_twist_1998]: https://doi.org/10.1108/aeat.1998.12770dad.005
[research_winkelmann_1989]: https://doi.org/10.2514/6.1989-570
[research_winn_kishi_1972]: https://doi.org/10.21236/ad0753343
[research_winograd_1950]: https://ntrs.nasa.gov/citations/19930086344
[research_wise_1992]: https://doi.org/10.23919/acc.1992.4792318
[research_wise_brinker_1999]: https://doi.org/10.1002/(sici)1099-1239(19991215)9:14<999::aid-rnc449>3.0.co;2-o
[research_witte_monson_2003]: https://doi.org/10.21236/ada421043
[research_wittenmark_1990]: https://doi.org/10.1016/0005-1098(90)90047-l
[research_wolkovitch_1984]: https://doi.org/10.2514/6.1984-2471
[research_wollner_cooney_1948]: https://ntrs.nasa.gov/citations/19930085417
[research_wolowicz_1945]: https://ntrs.nasa.gov/citations/19930092554
[research_wolowicz_yancey_1973]: https://ntrs.nasa.gov/citations/19730023226
[research_wong_moigne_2007]: https://doi.org/10.1017/s0001924000004425
[research_wong_rock_1993]: https://doi.org/10.2514/6.1993-56
[research_wood_1984]: https://doi.org/10.2514/6.1984-2104
[research_woodcock_browne_1986]: https://doi.org/10.2514/6.1986-2131
[research_woodcock_george_1976]: https://ntrs.nasa.gov/citations/19760024077
[research_woodruff_saric_2011]: https://doi.org/10.2514/6.2011-3882
[research_woods_wood_1998]: https://doi.org/10.2514/6.1998-2745
[research_woolard_1980]: https://doi.org/10.2514/3.57886
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_wright_loving_1953]: https://ntrs.nasa.gov/citations/20050019302
[research_wu_chen_2012]: https://doi.org/10.1142/s2010194512008999
[research_wu_liu_2021]: https://doi.org/10.1145/3459104.3459109
[research_wu_perng_2004]: https://doi.org/10.2514/1.9285
[research_wu_zheng_2022]: https://doi.org/10.1155/2022/6447812
[research_wykes_1968]: https://ntrs.nasa.gov/citations/19680064036
[research_x36_test_pilot_1997]: https://ntrs.nasa.gov/citations/19970031950
[research_x4_blunt_elevons_1955]: https://ntrs.nasa.gov/citations/19930088514
[research_x4_buffet_1953]: https://ntrs.nasa.gov/citations/19930087804
[research_x4_flight_evaluation_1954]: https://ntrs.nasa.gov/citations/19930088365
[research_x4_longitudinal_1950]: https://ntrs.nasa.gov/citations/19930086356
[research_x4_stall_1950]: https://ntrs.nasa.gov/citations/19930090543
[research_xb70_review_1965]: https://ntrs.nasa.gov/citations/20000011988
[research_xf7u_semispan_1947]: https://ntrs.nasa.gov/citations/20050019378
[research_xi_zhao_2017]: https://doi.org/10.1109/ascc.2017.8287228
[research_xiang_wang_2026]: https://doi.org/10.1063/5.0313854
[research_xiao_tsai_2004]: https://doi.org/10.2514/6.2004-1056
[research_xiaoxiao_zhu_2025]: https://doi.org/10.1109/cac67268.2025.11486871
[research_xie_cai_2022]: https://doi.org/10.2514/6.2022-3204
[research_xie_cai_2023]: https://doi.org/10.2514/1.c037239
[research_xie_cai_2026]: https://doi.org/10.2514/1.c038668
[research_xie_yang_2010]: https://doi.org/10.2514/6.2010-2713
[research_xie_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.213.334
[research_xie_zhao_2019]: https://doi.org/10.1109/icusai47366.2019.9124755
[research_xin_blown_elevon_2019]: https://doi.org/10.1016/j.ast.2019.105324
[research_xiong_liu_2013]: https://doi.org/10.2514/6.2013-3205
[research_xiong_nguyen_2024]: https://doi.org/10.2514/6.2024-4056
[research_xu_2012]: https://doi.org/10.4028/www.scientific.net/amr.538-541.2627
[research_xu_deng_2013]: https://doi.org/10.1016/j.proeng.2013.12.024
[research_xu_deng_2014]: https://doi.org/10.1007/s11433-014-5630-y
[research_xu_dowell_2026]: https://doi.org/10.2514/6.2026-2312
[research_xu_feng_2025]: https://doi.org/10.1016/j.cja.2025.103443
[research_xu_gao_2026]: https://doi.org/10.1007/978-981-95-1954-5_6
[research_xu_pio_2019]: https://doi.org/10.1016/j.cja.2019.06.003
[research_xu_qiu_2011]: https://doi.org/10.4028/www.scientific.net/amm.148-149.833
[research_xu_xu_2019]: https://doi.org/10.1007/978-981-13-3305-7_24
[research_xu_yang_2022]: https://doi.org/10.1109/iai55780.2022.9976698
[research_xu_yu_2025]: https://doi.org/10.3390/aerospace13010017
[research_xu_zha_2019]: https://doi.org/10.2514/6.2019-3168
[research_xu_zha_2021]: https://doi.org/10.2514/1.c035727
[research_xu_zhou_2015]: https://doi.org/10.1016/j.ast.2015.07.022
[research_xu_zhu_2013]: https://doi.org/10.1109/tencon.2013.6718805
[research_xue_yunsong_2021]: https://doi.org/10.1177/0036850421998137
[research_xun_ground_effect_2026]: https://doi.org/10.2514/1.c038881
[research_yamasaki_lele_2024]: https://doi.org/10.2514/6.2024-4524
[research_yan_dai_2026]: https://doi.org/10.1063/5.0326645
[research_yan_shi_2024]: https://doi.org/10.1109/isaes61964.2024.10751145
[research_yan_sun_2025]: https://doi.org/10.1080/23307706.2025.2546106
[research_yanagihara_suzuki_1991]: https://doi.org/10.4271/911979
[research_yancey_1964]: https://ntrs.nasa.gov/citations/19650001037
[research_yang]: https://doi.org/10.31274/td-20260812-346
[research_yang_chao_1996]: https://doi.org/10.1006/mssp.1996.0013
[research_yang_fan_2010]: https://doi.org/10.1007/s11431-009-0323-x
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_li_aeroelastic_2022]: https://doi.org/10.3390/aerospace9090515
[research_yang_przekwas_1993]: https://doi.org/10.2514/6.1993-2976
[research_yang_przekwas_1993_b]: https://doi.org/10.2514/6.1993-637
[research_yang_shen_2007]: https://doi.org/10.2514/6.2007-1052
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wen_2024]: https://doi.org/10.1016/j.ast.2024.109336
[research_yang_zhong_2009]: https://doi.org/10.1109/aero.2009.4839614
[research_yang_zhong_2022]: https://doi.org/10.1117/12.2645332
[research_yankuiwang_qianli_2015]: https://doi.org/10.1109/ibcast.2015.7058540
[research_yasuaki_egami_1999]: https://doi.org/10.2514/6.1999-921
[research_yates_1960]: https://ntrs.nasa.gov/citations/19630004021
[research_yates_schneiter_1946]: https://ntrs.nasa.gov/citations/20050019307
[research_yavuz_2012]: https://doi.org/10.1016/j.jfluidstructs.2012.05.006
[research_yavuzturk_topbas_2017]: https://doi.org/10.2514/6.2017-1865
[research_yazawa_1977]: https://doi.org/10.2514/6.1977-1134
[research_ye_zhang_2009]: https://doi.org/10.1109/acc.2009.5160615
[research_yechout_2024]: https://doi.org/10.2514/4.107252
[research_yechout_morris_2014]: https://doi.org/10.2514/4.102547
[research_yechout_oelschlaeger_1976]: https://doi.org/10.2514/6.1976-1913
[research_yeo_atkins_2015]: https://doi.org/10.2514/1.c032682
[research_yerly_deluca_2016]: https://doi.org/10.2514/6.2016-3570
[research_yi_dong_2017]: https://doi.org/10.1142/9789813220362_0073
[research_yildiz_akcal_2019]: https://doi.org/10.2514/1.g004180
[research_yildiz_kolmanovsky_2010]: https://doi.org/10.1109/acc.2010.5530869
[research_yildiz_kolmanovsky_2011]: https://doi.org/10.1109/acc.2011.5991270
[research_yiming_mei_2019]: https://doi.org/10.1109/iccais46528.2019.9074698
[research_yin_wang_2017]: https://doi.org/10.12783/dtetr/amsm2017/14821
[research_yin_wang_2019]: https://doi.org/10.1109/icmae.2019.8881023
[research_yingsong_zhichun_2015]: https://doi.org/10.1016/j.proeng.2014.12.506
[research_yingyang_peng_2025]: https://doi.org/10.1016/j.isatra.2025.02.001
[research_yizhu_xinchen_2016]: https://doi.org/10.1109/cgncc.2016.7828830
[research_yong_wu_2020]: https://doi.org/10.1109/icca51439.2020.9264484
[research_yoo_bowers_2018]: https://ntrs.nasa.gov/citations/20180006832
[research_yoshinaga_nakaji_2004]: https://doi.org/10.2514/6.2004-5367
[research_you_2026]: https://doi.org/10.2139/ssrn.6802803
[research_young_1961]: https://ntrs.nasa.gov/citations/19660024038
[research_young_2026]: https://doi.org/10.2139/ssrn.6790560
[research_young_hergert_1992]: https://doi.org/10.2514/6.1992-4032
[research_young_martin_1992]: https://ntrs.nasa.gov/citations/20000023168
[research_yu_1981]: https://doi.org/10.2514/6.1981-1258
[research_yu_bernal_2013]: https://doi.org/10.2514/6.2013-2992
[research_yu_bernal_2016]: https://doi.org/10.2514/6.2016-1066
[research_yu_bose_2026]: https://doi.org/10.2514/6.2026-1052
[research_yu_li_2022]: https://doi.org/10.21203/rs.3.rs-1518375/v1
[research_yu_li_2023]: https://doi.org/10.1007/s11071-023-08849-1
[research_yu_li_2023_b]: https://doi.org/10.1016/j.ast.2023.108472
[research_yu_li_2024]: https://doi.org/10.1109/tfuzz.2024.3356577
[research_yu_li_2024_b]: https://doi.org/10.1109/tvt.2023.3329470
[research_yu_liu_2013]: https://doi.org/10.4028/www.scientific.net/amm.278-280.1713
[research_yu_tailless_2023]: https://doi.org/10.1002/rnc.6570
[research_yu_tao_2024]: https://doi.org/10.3390/app14188546
[research_yuan_kou_2024]: https://doi.org/10.2514/1.j064214
[research_yuan_ma_2023]: https://doi.org/10.1016/j.ast.2023.108508
[research_yuan_ma_2024]: https://doi.org/10.2139/ssrn.4937605
[research_yue_wang_2009]: https://doi.org/10.2514/6.2009-6155
[research_yue_wang_2013]: https://doi.org/10.2514/6.2013-624
[research_yue_wang_2013_b]: https://doi.org/10.2514/6.2013-623
[research_yuksel_kandemir_2023]: https://doi.org/10.2514/6.2023-2119
[research_yurkovich_1996]: https://doi.org/10.2514/6.1996-1447
[research_yuwei_aijun_2021]: https://doi.org/10.23919/jsee.2021.000089
[research_zaal_2016]: https://doi.org/10.2514/1.g001592
[research_zaheer_ajmal_2019]: https://doi.org/10.1109/ibcast.2019.8667242
[research_zahm_bear_1929]: https://ntrs.nasa.gov/citations/19930091354
[research_zahn_breitsamter_2022]: https://doi.org/10.1007/s13272-022-00619-w
[research_zahn_zieher_2025]: https://doi.org/10.3390/aerospace12050415
[research_zanette_almeida_2015]: https://doi.org/10.2514/6.2015-3227
[research_zauner_moise_2023]: https://doi.org/10.1007/s10494-023-00415-4
[research_zauner_sandham_2020]: https://doi.org/10.1103/physrevfluids.5.083903
[research_zaytseva_kuznetsov_2021]: https://doi.org/10.18698/0536-1044-2021-12-3-10
[research_zeiler_1998]: https://doi.org/10.2514/2.2273
[research_zerihan_zhang_2000]: https://doi.org/10.2514/2.2711
[research_zeyada_hess_1998]: https://doi.org/10.2514/6.1998-4334
[research_zeyada_hess_1999]: https://doi.org/10.2514/2.4463
[research_zhang_1988]: https://doi.org/10.2514/6.1988-4362
[research_zhang_2021]: https://doi.org/10.1007/978-981-15-8155-7_267
[research_zhang_deng_2026]: https://doi.org/10.3390/aerospace13010098
[research_zhang_he_2026]: https://doi.org/10.1016/j.cja.2025.103582
[research_zhang_he_fluidic_2026]: https://doi.org/10.1016/j.cja.2025.103811
[research_zhang_huang_2023]: https://doi.org/10.1016/j.cja.2023.03.017
[research_zhang_jia_2013]: https://doi.org/10.1109/mic.2013.6758104
[research_zhang_li_2012]: https://doi.org/10.4028/www.scientific.net/amm.235.170
[research_zhang_liu_2018]: https://doi.org/10.1002/asjc.1821
[research_zhang_liu_2024]: https://doi.org/10.1108/aeat-05-2024-0128
[research_zhang_ma_2021]: https://doi.org/10.1007/978-981-15-8155-7_183
[research_zhang_meng_2019]: https://doi.org/10.1016/j.isatra.2019.02.037
[research_zhang_qu_2015]: https://doi.org/10.2514/6.2015-0068
[research_zhang_rabbath_2008]: https://doi.org/10.1109/acc.2008.4586631
[research_zhang_shuang_2018]: https://doi.org/10.1007/s12555-017-0454-y
[research_zhang_su_2021]: https://doi.org/10.1109/ccdc52312.2021.9601405
[research_zhang_suresh_2007]: https://doi.org/10.1109/cca.2007.4389398
[research_zhang_wang_2015]: https://doi.org/10.2991/amcce-15.2015.362
[research_zhang_xiang_2025]: https://doi.org/10.23919/ccc64809.2025.11178744
[research_zhang_xu_2018]: https://doi.org/10.2514/6.2018-3067
[research_zhang_yang_2024]: https://doi.org/10.1109/isaes61964.2024.10750958
[research_zhang_ye_2010]: https://doi.org/10.1016/j.actaastro.2009.09.016
[research_zhang_ye_2015]: https://doi.org/10.2514/1.c032552
[research_zhang_yu_2013]: https://doi.org/10.1155/2013/714168
[research_zhang_zerihan_2003]: https://doi.org/10.2514/2.3150
[research_zhang_zerihan_2004]: https://doi.org/10.2514/1.1380
[research_zhang_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amm.397-400.218
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhao_2024]: https://doi.org/10.1063/5.0214653
[research_zhang_zhao_2025]: https://doi.org/10.1109/tase.2024.3363838
[research_zhang_zhou_2018]: https://doi.org/10.2514/6.2018-3574
[research_zhang_zhou_2018_b]: https://doi.org/10.2514/1.j056804
[research_zhang_zhu_2013]: https://doi.org/10.1109/tencon.2013.6718806
[research_zhao_1988]: https://doi.org/10.2514/6.1988-3735
[research_zhao_dai_2020]: https://doi.org/10.1016/j.cja.2019.12.022
[research_zhao_deng_2023]: https://doi.org/10.1016/j.cja.2023.08.016
[research_zhao_hu_2009]: https://doi.org/10.2514/1.39464
[research_zhao_sheng_2014]: https://doi.org/10.1109/cgncc.2014.7007465
[research_zhao_wang_2025]: https://doi.org/10.23919/ccc64809.2025.11179337
[research_zhao_zhang_2024]: https://doi.org/10.1063/5.0189340
[research_zheng_feng_2012]: https://doi.org/10.4028/www.scientific.net/amr.566.676
[research_zheng_xu_2013]: https://doi.org/10.1109/cac.2013.6775832
[research_zhenghong_1992]: https://doi.org/10.1007/bf02481800
[research_zhijie_taiyu_2025]: https://doi.org/10.1007/s00348-025-04112-y
[research_zhishuai_lingling_2022]: https://doi.org/10.1109/ccdc55256.2022.10034339
[research_zhong_xia_2025]: https://doi.org/10.1007/978-981-95-2998-8_44
[research_zhong_yang_2009]: https://doi.org/10.2514/6.2009-58
[research_zhou_1994]: https://doi.org/10.2514/6.1994-3517
[research_zhou_chen_2017]: https://doi.org/10.1016/j.taml.2017.11.006
[research_zhou_dong_2022]: https://doi.org/10.1109/cac57257.2022.10055837
[research_zhou_liu_2025]: https://doi.org/10.3724/j.issn.1674-4969.20240059
[research_zhu_gao_2016]: https://doi.org/10.1142/9789814740616_0016
[research_zhu_li_2023]: https://doi.org/10.1007/978-981-99-5877-1_9
[research_zhu_yang_2025]: https://doi.org/10.2139/ssrn.5615374
[research_zhu_yang_2026]: https://doi.org/10.2139/ssrn.6994998
[research_zhubin_ruikun_2023]: https://doi.org/10.1088/1742-6596/2551/1/012001
[research_zieba_rzucidlo_2026]: https://doi.org/10.3390/aerospace13030240
[research_zierep_1988]: https://doi.org/10.1016/b978-0-08-036232-8.50010-4
[research_zierep_1993]: https://doi.org/10.1016/b978-0-444-88889-1.50033-9
[research_ziff_rathert_1953]: https://ntrs.nasa.gov/citations/19930087836
[research_zilong_jie_2024]: https://doi.org/10.1109/icetci61221.2024.10594102
[research_zimmerman_ferman_1989]: https://doi.org/10.2514/6.1989-1378
[research_zink_mavris_2000]: https://doi.org/10.2514/6.2000-4827
[research_zink_raveh_2001]: https://doi.org/10.2514/6.2001-1427
[research_zogopoulospapaliakos_karras_2020]: https://doi.org/10.1109/icuas48674.2020.9214012
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zolghadri_leberre_2016]: https://doi.org/10.2514/1.c032596
[research_zoppini_ragni_2022]: https://doi.org/10.2139/ssrn.4036119
[research_zou]: https://doi.org/10.31274/rtd-180813-10754
[research_zou_huang_2022]: https://doi.org/10.2514/1.g006114
[research_zou_li_2005]: https://doi.org/10.2514/1.15025
[research_zou_li_2016]: https://doi.org/10.1117/12.2225043
[research_zou_yang_2012]: https://doi.org/10.1109/wcica.2012.6358155
[research_zou_yin_2017]: https://doi.org/10.1109/ccsse.2017.8087893
[research_zou_zhen_2026]: https://doi.org/10.2139/ssrn.6802811
[research_zverkov_kozlov_2012]: https://doi.org/10.54362/1818-7919-2012-7-4-57-67
[research_zweig_benasher_1995]: https://doi.org/10.2514/6.1995-3482
