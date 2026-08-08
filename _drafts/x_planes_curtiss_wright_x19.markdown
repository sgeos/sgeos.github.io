---
layout: post
mathjax: true
comments: true
title: "X-Planes: Curtiss-Wright X-19"
date: 2025-10-25 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 20
---

<!-- A316 -->
<script>console.log("A316");</script>

The [Curtiss-Wright X-19][ref_x19] carried 13,660 pounds on 154.6 square feet of wing. That is a wing loading of 88 pounds per square foot in an aircraft required to land vertically, at a moment when transports flew at 60 and fighters at 80. **The wings were not merely small. They were too small to carry the aircraft at any speed below 137 knots**, which is a strange property for a machine whose entire purpose was to arrive at zero. This article is the twentieth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], and the [X-18][related_post_a315_hiller_x18].

The previous article covered the [X-18][related_post_a315_hiller_x18], which tilted its whole wing. It would be natural to expect the same analysis here, since both aircraft convert by rotating propellers from vertical to horizontal. **That expectation is wrong, and following it would produce the wrong article.** A tilt-wing must keep its wing flying at absurd angles of attack, so the fraction of that wing immersed in the propeller slipstream governs everything. A tilt-propeller never rotates its wing at all. The wing sits at zero incidence from hover to cruise and never sees an angle it could not see in ordinary flight.

The question the X-19 asked instead is whether a propeller can be counted on for lift. Not thrust turned upward, which is trivial, but the force a propeller develops **at right angles to its own axis** when the oncoming flow meets the disc obliquely. Curtiss-Wright called this the radial lift force, and the company's claim was that it is large enough to size a wing around.

The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003] and the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]. The keystone's own literature is older than the aircraft by eighteen years and belongs to aerodynamic stability rather than to vertical flight, which is [Ribner 1945, Propellers in yaw][research_ribner_1945_2] and [Ribner 1945][research_ribner_1945].

## The Research Question

### The Keystone Is the Propeller Normal Force

**The keystone is how much lift a propeller produces without pointing at the sky.**

A propeller meeting the air along its own axis produces thrust and nothing else. Incline the axis to the flow and the symmetry breaks. Each blade sees a velocity that varies around the azimuth, the loading varies with it, and the disc as a whole exerts a force perpendicular to its axis. It was understood by 1909 that a yawed propeller acts like a fin, and [RUMPH et al 1942][research_rumph_1942] treated the effect as a stability problem, which is what it had always been. A tractor propeller ahead of the centre of gravity is destabilising precisely because this force exists.

Curtiss-Wright proposed to stop treating it as a nuisance and start treating it as lift.

If the propellers carry part of the lift, the wing carries less, so the wing can be smaller. Writing the argument down makes its leverage visible. If the propellers supply a fraction $\phi$ of the lift at the slowest wing-borne speed, the wing need only supply the rest.

$$S = \frac{2 W \left( 1 - \phi \right)}{\rho V_{\text{conv}}^{2} C_{L,\max}}$$

A smaller wing is lighter, has less drag at high speed, and presents less area to the downwash in hover. The X-19's 88 pounds per square foot is the arithmetic consequence of taking that argument seriously.

The same force that supplies $\phi$ is a nuisance elsewhere, and the sign is what distinguishes the two readings. A propeller mounted a distance $x_p$ ahead of the centre of gravity contributes a pitching moment that grows with angle of attack.

$$\frac{\partial C_m}{\partial \alpha} = \frac{x_p}{q S \bar{c}} \frac{\partial N}{\partial \alpha}$$

That derivative is positive for a tractor propeller, which is destabilising, and it is the reason the effect was studied for thirty years before anyone proposed to exploit it.

### Why This Was the Binding Unknown in 1960

The competing configurations of the moment each had a defect that was already visible. The tail-sitter of the [X-13][related_post_a310_ryan_x13] required the pilot to land looking backward and upward. The tilt-wing of the [X-18][related_post_a315_hiller_x18] stalled the un-immersed part of its wing throughout conversion. The deflected slipstream arrangements studied by [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960] and [Grunwald 1961][research_grunwald_1961] paid a large download penalty.

The tilt-propeller avoided all three. Nothing about it requires the wing to stall, nothing requires the pilot to fly backward, and the wing is small enough that the download is modest. **The unknown was not whether the configuration could hover or cruise. It was whether the propeller force that made the small wing defensible was real at the size claimed.**

That question had an answer in the literature and the answer was not obviously encouraging. [Ribner 1943][research_ribner_1943] and its final form [Ribner 1945, Propellers in yaw][research_ribner_1945_2] give a theory calibrated against experiment, and [Crigler and Gilman 1949][research_crigler_gilman_1949] and [Crigler and Gilman 1952][research_crigler_gilman_1952] give methods for computing the forces on a propeller in pitch or yaw. The forces are real. Whether they are large enough to size an aircraft around is a question of magnitude, and magnitude is what this article computes.

## Programme Origin

The X-19 did not begin as a military aircraft and did not begin with that designation. [Curtiss-Wright][ref_curtiss_wright] developed it as a civil executive transport under the company designations X-200 and M-200, carrying four passengers, funded from company research money.

Before the transport there was a demonstrator. The [Curtiss-Wright X-100][ref_x100] was built to test two things at once, the radial lift force itself and the gimballed nacelles a tilt-propeller needs. Construction began in February 1958. Tethered hovering started on 20 April 1959, free hover followed in September 1959, and **the first and only transition from vertical to high-speed flight was made on 13 April 1960**. Curtiss-Wright declared the concept proven, handed the aircraft to NASA in October 1960 for tests at Langley, and it went afterward to the Smithsonian, where [Smithsonian National Air and Space Museum, Curtiss-Wright X-100][ref_si_x100] and [Vertipedia, Curtiss-Wright X-100][ref_vertipedia_x100] record it.

Then the company's management changed and the new management declined to keep spending research funds on it. The two aircraft were offered to the Tri-Service VTOL programme, a joint Army, Navy and Air Force office, and the Air Force contracted for conversion of two prototypes to military standard under the Tri-Service Assault Transport programme. The changes were substantial and none of them were aerodynamic. Ejection seats, a rescue hoist, a mock refuelling probe, and a fuselage stretch for passenger access.

**The sequence is worth stating plainly because it is unusual.** A company proved a concept on a small demonstrator with its own money, lost interest, and sold the follow-on to a government that wanted a transport. The aircraft that resulted was heavier than the one the concept had been proven on and carried equipment the proof never involved.

## Sizing From First Principles

### The Wing Cannot Carry the Aircraft

Start with the number that makes everything else necessary. The forward wing spans 19.5 feet over 56.1 square feet and the aft wing spans 23.5 feet over 98.5 square feet. Aspect ratio and mean chord follow from span and area alone.

$$\text{AR} = \frac{b^{2}}{S}, \qquad \bar{c} = \frac{S}{b}$$

which gives 6.78 and 2.88 feet forward, and 5.61 and 4.19 feet aft. Total area is 154.6 square feet against 13,660 pounds.

Each surface has its own lift-curve slope, reduced from the two-dimensional value by its finite span, where $a_0$ is $2\pi$ per radian and $e$ is the span efficiency.

$$a = \frac{a_0}{1 + a_0 / \left( \pi e \, \text{AR} \right)}$$

At $e = 0.90$ this is 4.732 per radian forward and 4.500 aft. The aircraft's single equivalent slope is the area-weighted mean of the two, and it is used throughout the article.

$$\bar{a} = \frac{S_f a_f + S_a a_a}{S_f + S_a} = 4.584 \ \text{rad}^{-1}$$

Wing loading follows immediately.

$$\frac{W}{S} = \frac{13{,}660}{154.6} = 88.4 \ \text{lb/ft}^2$$

The speed at which a wing alone supports that loading is the stall speed, where $\rho$ is density, $S$ is wing area and $C_{L,\max}$ the maximum lift coefficient.

$$V_{s} = \sqrt{\frac{2W}{\rho S C_{L,\max}}}$$

For an unflapped wing with $C_{L,\max} = 1.4$ at sea level this gives 230.4 feet per second, or **136.5 knots**. At 1.2 it is 147.5 knots and at 1.6 it is 127.7 knots. The record states the wings had no incidence, no dihedral and no sweepback, and mentions no high-lift devices, so the middle value is the generous reading rather than the conservative one.

**An aircraft that stalls at 136 knots and is required to land at zero has a gap of 136 knots to explain.** Tilting the propellers explains most of it, because a propeller pointed upward is a lifting device regardless of any subtlety. The radial lift force is what explains the rest, and the rest is where the wing area was won.

### What a Propeller Does in Oblique Flow

Write the force from momentum rather than from blade elements, because the momentum form has exactly one unknown and that unknown can be estimated from geometry.

Let the disc of area $A$ meet a freestream $V$ with its axis at angle $\alpha_d$ to the flow. Resolve the freestream into a component along the axis and a component in the plane of the disc.

$$V_{\text{axial}} = V \cos\alpha_d, \qquad V_{\text{in-plane}} = V \sin\alpha_d$$

The mass flow through the disc is set by the axial component plus whatever the propeller induces, where $v_i$ is the induced velocity.

$$\dot{m} = \rho A \left( V \cos\alpha_d + v_i \right)$$

The blades resist the in-plane component and turn part of it toward the axis. Let $k$ be the fraction of the in-plane momentum flux the disc removes. The reaction on the aircraft is the radial lift force.

$$N = k \, \rho A \left( V \cos\alpha_d + v_i \right) V \sin\alpha_d$$

**This is the keystone relation of the article and everything downstream depends on $k$.**

### The Fin Analogy Fixes the Unknown

Leaving $k$ free would make the calculation circular, since any wing area could then be justified by choosing $k$ to suit. [Ribner 1945, Propellers in yaw][research_ribner_1945_2] supplies the constraint. Ribner extends the fin analogy to the form of the side-force expression and identifies the effective fin area with **the projected side area of the propeller**, meaning the blade area seen from the side rather than the disc area.

Write the propeller as a fin of area $S_f$ and lift-curve slope $a_b$ and equate the two expressions at small angle and high speed, where $v_i$ vanishes against $V$.

$$\tfrac{1}{2} \rho V^2 S_f a_b \alpha_d = k \rho A V^2 \alpha_d$$

The dynamic pressure, the freestream and the disc angle all cancel, which is why the fin analogy is useful rather than merely suggestive. What remains is pure geometry.

$$k = \frac{S_f a_b}{2A}$$

The projected side area of a propeller with $B$ blades of chord $c$ and radius $R$ is not simply the blade area, because a rotating blade presents its full width to the side only twice per revolution. The azimuthal mean of that projection supplies the factor.

$$\frac{1}{2\pi} \int_{0}^{2\pi} \left| \cos\psi \right| \, d\psi = \frac{2}{\pi}$$

Multiplying the blade area by that mean gives the effective fin.

$$S_f = \frac{2}{\pi} B c R$$

So $k$ follows from blade chord. The blade chord is not in the public record. It has to be derived, and deriving it turns out to explain something else entirely.

### The Cruise Requirement Caps the Tip Speed

The X-19 was quoted at 400 knots at 20,000 feet. A propeller at 400 knots is close to its own limit, because the blade tip sees the vector sum of flight speed and rotational speed. Write the helical tip Mach number with $a$ the speed of sound, $\Omega$ the rotational rate and $R$ the radius.

$$M_{h} = \frac{\sqrt{V^2 + (\Omega R)^2}}{a}$$

Propeller efficiency collapses as $M_h$ approaches unity, so take 0.90 as the working ceiling and solve for the rotational tip speed the cruise permits.

$$\Omega R \le \sqrt{\left( M_{h,\lim} a \right)^2 - V^2}$$

At 20,000 feet the dynamic pressure at that speed is 288.6 pounds per square foot, the speed of sound is 1,036.8 feet per second and 400 knots is 675.1 feet per second, a flight Mach number of 0.651. The ceiling gives 933.2 feet per second for the helical tip, and the rotational component that leaves is **644.2 feet per second**. The rotational rate and the shaft speed follow.

$$\Omega = \frac{\Omega R}{R} = \frac{644.2}{6.5} = 99.11 \ \text{rad/s}, \qquad n = \frac{60 \, \Omega}{2\pi} = 946 \ \text{rpm}$$

**That is a slow propeller.** Take the tip speed back to sea level and compare it against the static case, where no flight speed adds to it.

$$M_{\text{tip,static}} = \frac{\Omega R}{a_0} = \frac{644.2}{1{,}116.5} = 0.577$$

where a conventional propeller would run near 0.8. The 400-knot requirement has taken most of the tip speed away.

The other measure of how hard this propeller is working is the advance ratio, the distance advanced per revolution against the diameter.

$$J = \frac{V}{n D} = \frac{675.1}{(15.77)(13)} = 3.29$$

which is high, and is the regime in which a propeller behaves least like a hovering rotor.

### Hover Then Demands an Extraordinary Blade

A propeller that turns slowly must be large in blade area to produce thrust, because thrust scales with the square of tip speed. Hovering thrust must also exceed weight, since the wings sit under the discs and are pushed down by the slipstream.

Compute the download first. With the nacelles at the tips, the disc reaches inboard by one radius from each tip, so the immersed fraction of a semi-span is the radius over the semi-span whenever the disc does not reach the root.

$$f_{\text{imm}} = \frac{R}{b/2} = \frac{2R}{b}$$

which is 0.667 forward and 0.553 aft, and the immersed area is the sum over the two surfaces.

$$S_{\text{imm}} = \sum_j f_{\text{imm},j} S_j = 91.9 \ \text{ft}^2 = 59.4\% \ \text{of the wing}$$

The slipstream velocity at the wing is a multiple $\lambda$ of the induced velocity, and the download is that dynamic pressure acting on the immersed area with a normal-flow drag coefficient.

$$D_{\text{down}} = \tfrac{1}{2} \rho \left( \lambda v_i \right)^2 S_{\text{imm}} C_{D,\perp}$$

Thrust and download depend on each other through $v_i$, so they solve together. Substituting the momentum-theory induced velocity into the download makes the pair LINEAR in thrust rather than requiring iteration, because $v_i^2$ is proportional to $T$.

$$T = W + \frac{\lambda^{2} S_{\text{imm}} C_{D,\perp}}{4 A} \, T \quad \Longrightarrow \quad T = \frac{W}{1 - \lambda^{2} S_{\text{imm}} C_{D,\perp} / 4A}$$

The coefficient is 0.1168, so the download is **1,807 pounds, or 13.2 percent of gross weight**, and the required thrust is 15,467 pounds. Momentum theory then gives the induced velocity, where $A$ is the total disc area of 530.9 square feet.

$$v_i = \sqrt{\frac{T}{2 \rho A}} = 78.28 \ \text{ft/s}$$

Ideal power in hover is the thrust acting through the induced velocity, and the figure of merit is what converts it into a shaft requirement.

$$P_{\text{ideal}} = T v_i = 2{,}201 \ \text{hp}, \qquad P_{\text{req}} = \frac{P_{\text{ideal}}}{\text{FM}} = 3{,}145 \ \text{hp}$$

Against 5,300 installed that is a comfortable margin.

$$\frac{P_{\text{inst}}}{P_{\text{req}}} = \frac{5{,}300}{3{,}145} = 1.69$$

Now the blade. Thrust scales with the square of tip speed, which is why a slow propeller must be wide.

$$T_1 = C_T \rho A_1 (\Omega R)^{2}$$

Inverting it for the thrust coefficient, with a thrust of 3,867 pounds being one quarter of the total including download,

$$C_T = \frac{T_1}{\rho A_1 (\Omega R)^2} = 0.02953$$

Blade loading $C_T/\sigma$ is what stalls a rotor, and taking 0.14 as the limit for a heavily twisted blade fixes the solidity, where solidity is blade area over disc area.

$$\sigma = \frac{B c}{\pi R}, \qquad \sigma = \frac{C_T}{(C_T/\sigma)_{\lim}} = 0.2109$$

Inverting the first for the chord,

$$c = \frac{\sigma \pi R}{B} = \frac{(0.2109)(\pi)(6.5)}{3} = 1.436 \ \text{ft}$$

**A chord of 17.2 inches on a 13-foot propeller.** The ratio of chord to radius is 0.221, where a conventional propeller runs near 0.09, and the blade aspect ratio is that ratio inverted.

$$\text{AR}_b = \frac{R}{c} = \frac{6.5}{1.436} = 4.53$$

which is a wing rather than a blade.

### The Wide Blade Is Demanded Twice

Photographs of the X-19 show propellers of remarkable width, and the usual explanation is that the wide chord was chosen to maximise radial lift. The calculation above reaches the same blade **without invoking radial lift at all**. Hovering at a tip speed the 400-knot cruise permits requires it on its own.

This matters for how the configuration should be judged. The wide blade is not a cost incurred to obtain the radial lift force. It is a consequence of two requirements that were going to be imposed anyway, and the radial lift force comes with it. [Dunham and Gentry 1989][research_dunham_gentry_1989] and [Dunham and Gentry 1989, The Effect of Solidity on Propelle][research_dunham_gentry_1989_2] address exactly this coupling, since solidity is the quantity blade chord expresses and normal force is what it produces.

Feeding the chord back gives the projected side area and the recovery fraction.

$$S_f = \frac{2}{\pi}(3)(1.436)(6.5) = 17.83 \ \text{ft}^2 \ \text{per propeller}$$

With a blade lift-curve slope of 4.214 per radian at aspect ratio 4.53, the recovery fraction is

$$k = \frac{(17.83)(4.214)}{2(132.73)} = 0.283$$

**The disc removes about 28 percent of the in-plane momentum that passes through it.** The value is physically admissible, being safely below unity, and it was obtained from geometry rather than chosen.

### How Much Lift the Propellers Actually Supply

At the quoted cruise of 347.6 knots at 15,000 feet, dynamic pressure and the lift coefficient the aircraft must reach follow directly.

$$q = \tfrac{1}{2} \rho V^{2} = 257.4 \ \text{lb/ft}^{2}, \qquad C_L = \frac{W}{q S} = 0.343$$

which is unremarkable, and corresponds to an attitude of 4.29 degrees before any interference is allowed for.

$$\alpha = \frac{C_L}{\bar{a}} = \frac{0.343}{4.584} = 0.0749 \ \text{rad}$$

Compare the lift slopes of the two contributors. For the wings, with $\bar{a} = 4.584$ per radian area-weighted across the two surfaces,

$$\frac{\partial L}{\partial \alpha} = q S \bar{a} = 182{,}410 \ \text{lb/rad}$$

and for the four propellers, from the keystone relation at small angle,

$$\frac{\partial N}{\partial \alpha} = 4 k \rho A_1 (V + v_i) V = 77{,}585 \ \text{lb/rad}$$

so the propellers supply

$$\frac{\partial N / \partial \alpha}{\partial N / \partial \alpha + \partial L / \partial \alpha} = 29.8\%$$

of the incidence-dependent lift. The figure barely moves across lift-to-drag ratios from 7 to 10, changing only in the third significant figure, because $v_i$ is under two feet per second at this speed and contributes almost nothing.

**Curtiss-Wright's claim survives the arithmetic.** Roughly three tenths of the lift slope in cruise comes from the propellers.

### What That Bought, Computed Two Ways

The honest counterfactual is not to switch the radial lift force off and leave the wing unchanged, which describes no aircraft anyone would build. It is to hold the conversion speed fixed and ask how much wing would be needed without the propellers' help.

The first route ignores drag and thrust entirely. The wing works at its stall angle, which is the maximum lift coefficient over the equivalent slope.

$$\alpha_{\text{stall}} = \frac{C_{L,\max}}{\bar{a}} = \frac{1.4}{4.584} = 0.3054 \ \text{rad} = 17.5^{\circ}$$

With the nacelles horizontal the propeller axis sits at that same angle to the flow, so the balance to solve is the wing at maximum lift plus the keystone relation evaluated at the stall angle.

$$W = \tfrac{1}{2} \rho V^{2} S C_{L,\max} + 4 k \rho A_1 \left( V \cos\alpha_{\text{stall}} + v_i \right) V \sin\alpha_{\text{stall}}$$

Both terms grow as $V^2$ apart from the small induced-velocity contribution, so the solution is close to a closed form and the speed falls to **115.1 knots**, against **136.5 knots** for the wing alone. Wing area scales with the square of that speed.

$$\frac{S_{\text{equiv}}}{S} = \left( \frac{V_{\text{without}}}{V_{\text{with}}} \right)^{2} = 1.408$$

which puts the equivalent plain wing at 217.7 square feet and 62.7 pounds per square foot.

The second route reads the same quantity off the fully trimmed corridor derived below, where drag, thrust and induced velocity are all present, and gets 114.3 knots against 138.0 knots, an equivalent wing of 225.3 square feet at 60.6 pounds per square foot. **The two routes differ by 3.5 percent**, which is the useful part, since they share no machinery beyond the keystone relation itself.

The conclusion is specific. Without the radial lift force the X-19 would have needed a wing of roughly 220 square feet at about 61 pounds per square foot, **which is an ordinary transport wing loading of the period**. The radial lift force is exactly what separates 88 from 61.

### The Conversion Corridor

Steady level flight at nacelle angle $i$ requires two equations rather than one. With the propeller axis at $i + \alpha$ to the flight path,

$$T \sin(i + \alpha) + N \cos(i + \alpha) + L \cos\alpha = W$$

The second is the horizontal balance along the flight path, where the radial lift force acts against the thrust rather than with it, because the force normal to a forward-tilted disc leans backward.

$$T \cos(i + \alpha) - N \sin(i + \alpha) - D = 0$$

Thrust appears in both and is not free. Eliminating it by multiplying the first by $\cos(i+\alpha)$, the second by $\sin(i+\alpha)$ and subtracting leaves a condition on angle of attack alone.

$$\cos(i + \alpha) \left[ W - L \cos\alpha \right] - N - D \sin(i + \alpha) = 0$$

The drag needed here is not available from the sources, so derive it from the quoted maximum speed rather than assume it. Drag is parasite plus induced, written with an equivalent flat-plate area $f$ so that the tiny reference wing does not distort the coefficient.

$$D = \tfrac{1}{2} \rho V^{2} \left( f + \frac{S C_L^{2}}{\pi e \, \text{AR}_{\text{eff}}} \right)$$

At maximum speed thrust equals drag, and thrust power is the shaft power the propellers convert.

$$D = \frac{\eta_p P_{\text{shaft}}}{V} = \frac{(0.80)(5{,}300)(550)}{675.1} = 3{,}454 \ \text{lb}$$

Of that, 277 pounds is induced, and the remainder inverts to the flat-plate area.

$$f = \frac{D - D_i}{q} = \frac{3{,}454 - 277}{288.6} = 11.01 \ \text{ft}^{2}$$

Thrust available at any other speed is not this quantity divided by speed, which diverges at the hover. Momentum theory with the same power gives a form that stays finite at zero.

$$2 \rho A_1 v_i \left( V + v_i \right)^{2} = \frac{\eta_p P_{\text{shaft}}}{4}, \qquad T = 4 \cdot 2 \rho A_1 v_i \left( V + v_i \right)$$

A solution exists only where the angle of attack it demands is below the stall and the thrust it demands is below what the engines can deliver. Those two ceilings are the corridor, and at sea level they give the following.

| Nacelle angle | Minimum | Maximum | Width |
|---|---|---|---|
| 90 degrees | 3.0 kt | 55.1 kt | 52.1 kt |
| 80 degrees | 3.0 kt | 71.7 kt | 68.7 kt |
| 70 degrees | 14.8 kt | 85.9 kt | 71.1 kt |
| 60 degrees | 52.7 kt | 100.1 kt | 47.4 kt |
| 50 degrees | 71.7 kt | 116.7 kt | 45.0 kt |
| 40 degrees | 81.2 kt | 135.7 kt | 54.5 kt |
| 30 degrees | 90.7 kt | 164.1 kt | 73.5 kt |
| 20 degrees | 97.8 kt | 206.8 kt | 109.0 kt |
| 10 degrees | 104.9 kt | 268.4 kt | 163.5 kt |
| 0 degrees | 114.3 kt | 325.3 kt | 210.9 kt |

Continuity is a condition on consecutive rows rather than an impression from the table. A conversion can be flown at constant speed through a nacelle step only where the bands share a speed.

$$V_{\min}(i_{n+1}) \le V_{\max}(i_{n}) \quad \text{for every consecutive pair}$$

**Every band satisfies it, so a continuous path from hover to cruise exists.** The narrowest point is at 50 degrees of nacelle, 45 knots wide. The top speed at zero nacelle at sea level is 325 knots, which is consistent with the 400-knot figure quoted at 20,000 feet rather than in conflict with it.

### A Result That Does Not Support the Sales Argument

Running the same corridor with the radial lift force removed produces something that has to be reported carefully, because it cuts against the argument the article has been building.

| Nacelle angle | Minimum with | Minimum without |
|---|---|---|
| 90 degrees | 3.0 kt | 3.0 kt |
| 70 degrees | 14.8 kt | 67.0 kt |
| 60 degrees | 52.7 kt | 109.6 kt |
| 40 degrees | 81.2 kt | 126.2 kt |
| 20 degrees | 97.8 kt | 133.3 kt |
| 0 degrees | 114.3 kt | 138.0 kt |

**That corridor is also continuous.** Without the radial lift force the aircraft still converts, at higher speeds and through narrower bands, but it converts. The radial lift force is therefore **not** what makes the X-19 possible, which is the stronger claim and the one a reader might have expected this article to reach.

What it does is lower every boundary. Writing the reduction as a difference makes its shape visible.

$$\Delta V(i) = V_{\min}^{\text{without}}(i) - V_{\min}^{\text{with}}(i)$$

That difference is 56.9 knots at 60 degrees of nacelle and 23.7 knots at zero, so the benefit is largest exactly where the disc meets the flow most obliquely, which is what the keystone relation predicts through its $\sin\alpha_d$ factor. That reduction is what the small wing was bought with. The distinction between making a configuration possible and making it cheaper is worth preserving, and the arithmetic supports only the second.

## Dependent Systems

### The Tandem Wing, Which Costs Attitude

Two wings in line is not merely a way to divide area. The aft wing flies in the downwash of the forward one, and at 2.05 forward semi-spans behind it the far-field value is nearly reached. Write the downwash gradient with respect to aircraft attitude.

$$\frac{d\varepsilon}{d\alpha} = \frac{2 a_{\text{fwd}}}{\pi \text{AR}_{\text{fwd}}} = 0.444$$

The aft wing therefore loses 44 percent of every degree of attitude the aircraft takes. Trim solves in closed form because the downwash is proportional to the same angle that produces it.

$$W = q \alpha \left[ S_f a_f + S_a a_a \left( 1 - \frac{d\varepsilon}{d\alpha} \right) \right]$$

Without the interference the cruise attitude would be 4.29 degrees. With it the attitude is **5.94 degrees**, a penalty of 1.65 degrees, or 38.5 percent more attitude for the same lift. The downwash at the aft wing is 2.64 degrees at that condition.

The consequence shows up in the lift split, where the forward surface works at the full attitude and the aft surface at the attitude less the downwash.

$$L_f = q S_f a_f \alpha = 7{,}086 \ \text{lb}, \qquad L_a = q S_a a_a \left( \alpha - \varepsilon \right) = 6{,}574 \ \text{lb}$$

Comparing the lift share against the area share is what makes the penalty concrete.

$$\frac{L_a}{L_f + L_a} = 48.1\% \quad \text{on} \quad \frac{S_a}{S} = 63.7\% \ \text{of the area}$$

**The larger wing is the less effective one**, which is the price of putting it second.

### Pitch Control, Which the Layout Supplies for Nothing

Here the tandem arrangement earns its keep, and the comparison with the previous article is direct.

The [X-18][related_post_a315_hiller_x18] carried a turbojet in its tail for no purpose except pitch control in hover, because a tilt-wing with two propellers on one lateral axis has no way to generate a pitching moment at zero airspeed. The X-19 has four propellers at two longitudinal stations. Differential thrust between the stations is a pitching moment with no additional hardware whatever.

Shifting a fraction $f$ of total thrust from one station to the other raises each station by $fT/2$ and lowers the other by the same, so both arms of length $\ell/2$ contribute.

$$M = 2 \left( \tfrac{1}{2} f T \right) \frac{\ell}{2} = \tfrac{1}{2} f T \ell$$

With a station separation of 20 feet, 10 percent differential gives 15,467 foot-pounds. The inertia it acts against is the mass times the square of the pitch radius of gyration.

$$I_{yy} = m k_y^{2} = \left( \frac{13{,}660}{32.174} \right) (13.2)^{2} = 73{,}976 \ \text{slug ft}^{2}$$

Angular acceleration is the quotient of the two.

$$\ddot{\theta} = \frac{M}{I_{yy}} = \frac{15{,}467}{73{,}976} = 0.209 \ \text{rad/s}^{2}$$

At 30 percent it is 0.627 radians per second squared, or 35.9 degrees per second squared. **That is ample authority obtained from geometry rather than from an engine.**

Roll uses the same relation with the lateral arm in place of the half-station-separation, so the moment is the differential acting at the mean semi-span of 10.75 feet.

$$M_\phi = f T \, y = (0.10)(15{,}467)(10.75) = 16{,}627 \ \text{ft\,lb}$$

The roll inertia is dominated by four heavy nacelles at the tips rather than by the fuselage, so the radius of gyration is a larger fraction of span than a conventional aircraft would show.

$$I_{xx} = m k_x^{2} = (424.6)(6.45)^{2} = 17{,}663 \ \text{slug ft}^{2}, \qquad \ddot{\phi} = 53.9 \ \text{deg/s}^{2}$$

Roll is better still, because the arm is comparable and the inertia is a quarter of the pitch value.

### Yaw Control, Which It Does Not

With all four nacelles vertical, the only yaw effector available is differential torque. Diagonally opposite propellers turned the same way, which cancels torque reaction in pairs, so raising one diagonal pair and lowering the other leaves a net reaction on the airframe. Torque per propeller follows from hovering power and rotational speed.

$$Q_1 = \frac{P_1}{\Omega} = \frac{786 \times 550}{99.11} = 4{,}363 \ \text{ft\,lb}$$

A differential of fraction $f$ between the diagonal pairs, two propellers each, leaves

$$Q_{\text{net}} = 4 f Q_1$$

At 20 percent this is 3,490 foot-pounds. The yaw inertia is the largest of the three, because the mass is distributed along the longest dimension.

$$I_{zz} = m k_z^{2} = (424.6)(15.4)^{2} = 100{,}690 \ \text{slug ft}^{2}$$

Dividing the one by the other is where the configuration runs out of authority.

$$\ddot{\psi} = \frac{Q_{\text{net}}}{I_{zz}} = \frac{3{,}490}{100{,}690} = 0.0347 \ \text{rad/s}^{2} = 1.99 \ \text{deg/s}^{2}$$

At 30 percent it is 2.98 degrees per second squared.

**That is roughly an order of magnitude short of the control power VTOL criteria of the period call for**, and the handling-qualities literature of exactly those years is where the criteria live, in [Reeder 1958][research_reeder_1958], [Carlson 1958][research_carlson_1958] and [Slaughter 1958][research_slaughter_1958], with the earlier hovering analyses in [MILLER 1948][research_miller_1948] and [ALBACHTEN 1956][research_albachten_1956]. The record states that the programme was troubled by control system problems without saying which axis, and this calculation offers a candidate rather than an answer.

The caveat is real. If the nacelles could be tilted differentially between the left and right sides, a yaw couple is available that this calculation does not include, and the aircraft would then have adequate yaw control by an effector the sources do not describe. The computation establishes that **differential torque alone is not enough**, not that the aircraft lacked yaw control.

### The Cross-Shaft, and What It Cost

The [X-18][related_post_a315_hiller_x18] had two engines that were not interconnected, and losing one meant losing the aircraft. That is the defect the X-19's designers had in front of them, and they fixed it. Two engines drive four propellers through an interconnected transmission, so an engine failure is a power reduction rather than an asymmetry.

The magnitude of what the fix prevents is easy to state. Losing both propellers on one side leaves a rolling moment of

$$M_{\text{upset}} = \frac{T}{2} \times 10.75 = 83{,}135 \ \text{ft\,lb}$$

Comparing it against the roll control available at the largest differential is what makes the case.

$$\frac{M_{\text{upset}}}{M_{\phi,\max}} = \frac{83{,}135}{49{,}881} = 1.67$$

**The upset exceeds full roll control by two thirds.** Without the interconnect it is unrecoverable, so the cross-shaft is not a refinement.

The cost is transmission. With one engine dead the survivor drives the far pair through the shaft, which is half the hovering power, or 1,572 horsepower. Torque depends on where in the drive train the shaft runs.

$$Q = \frac{P}{\Omega}$$

At 6,000 revolutions per minute that is 1,376 foot-pounds, at 3,000 it is 2,753, and at propeller speed of 946 it is **8,726 foot-pounds**. Shafts therefore run fast and every propeller needs its own reduction gearbox, which is why the drive system is the large item. The transmission literature of the following decade, [MEIER 1964][research_meier_1964], [Moellmann and O'Connor 1967][research_moellmann_o_connor_1967], [Bowen and Walker 1972][research_bowen_walker_1972] and [Chase 1973][research_chase_1973], is about weight and life in exactly these components.

**The cure for the X-18's disease became the X-19's cause of death.** That sentence is the article's central historical claim and the flight test record is what supports it.

### The Propellers Themselves

Disc loading is where the tilt-propeller beats the tilt-wing outright.

$$\frac{W}{A} = \frac{13{,}660}{530.93} = 25.7 \ \text{lb/ft}^2$$

against 82.1 for the X-18. Four thirteen-foot propellers present a great deal more disc than two sixteen-foot ones, and the penalty for disc loading is explicit once the induced velocity is substituted into the ideal power.

$$\frac{P_{\text{ideal}}}{W} = v_i = \sqrt{\frac{1}{2\rho} \cdot \frac{W}{A}}$$

**Induced power per pound scales with the square root of disc loading**, so the X-19 pays $\sqrt{25.7/82.1} = 0.56$ of what the X-18 pays for every pound it holds up. Power loading follows.

$$\frac{W}{P_{\text{req}}} = \frac{13{,}660}{3{,}145} = 4.34 \ \text{lb/hp}$$

Pitch control of the blades is the mechanism every axis depends on, and controllable-pitch propeller behaviour is treated in [BOSWELL 1961][research_boswell_1961] and [Valentine and Kader 1976][research_valentine_kader_1976], with static thrust estimation in [COWARD 1955][research_coward_1955] and [Brusse and Cronk 1965][research_brusse_cronk_1965].

## The Flight Test Record

The X-19 first flew on 20 November 1963 at Caldwell, New Jersey. It was lost on 25 August 1965. In between it accumulated **50 flights totalling four hours**.

Those two numbers deserve to be set against each other.

$$\frac{4 \times 60}{50} = 4.8 \ \text{minutes per flight}$$

Over the 645 days between first flight and loss the calendar rate is as thin as the airborne one.

$$\frac{645}{50} = 12.9 \ \text{days per flight}, \qquad \frac{4.0}{645/30.44} = 0.19 \ \text{flight hours per month}$$

A programme averaging eleven minutes of flight per calendar month is not a flight test programme in any ordinary sense.

**The X-19 never transitioned.** The crew was lost before the transition could be attempted, so the aircraft never once demonstrated the capability the whole configuration existed to provide. Every number in the sizing section above describes an aircraft that did not fly the regime it was sized for.

### The Final Flight

The aircraft was lost when a gearbox failed and propellers separated. Test pilot James V. Ryan and the co-pilot ejected in North American LW-2B seats as the airframe rolled inverted, reportedly at 390 feet, with 2.5 seconds elapsed between propeller separation and ejection, and canopies fully deployed two seconds later at about 230 feet. Both crew survived with minor injuries from ejection through the canopy.

A ballistic airframe has a fixed time budget.

$$t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2(390)}{32.174}} = 4.92 \ \text{s}$$

Against that budget, the interval the crew actually used is the quantity worth naming.

$$\frac{t_{\text{eject}}}{t} = \frac{2.5}{4.92} = 50.8\%$$

**The 2.5 seconds between failure and ejection consumed half the time that existed**, leaving 2.42 seconds. The descent and the speed reached in that interval are the two quantities the reported figures must be tested against.

$$\Delta h = \tfrac{1}{2} g t^{2} = \tfrac{1}{2}(32.174)(2.5)^{2} = 100.5 \ \text{ft}, \qquad v = g t = 80.4 \ \text{ft/s}$$

There is an inconsistency in the reported figures that should be stated rather than smoothed. Both readings reduce to the same mean-rate test.

$$\bar{v} = \frac{h_{\text{eject}} - h_{\text{canopy}}}{\Delta t}$$

If 390 feet is the altitude at propeller separation, ejection occurred near 289 feet and the test gives

$$\bar{v} = \frac{289.5 - 230}{2.0} = 29.7 \ \text{ft/s}$$

which is far below the 80.4 feet per second the airframe had already reached, and would require the seat to arrest most of the descent. If instead **390 feet is the altitude at ejection**, the same test gives

$$\bar{v} = \frac{390 - 230}{2.0} = 80.0 \ \text{ft/s}$$

which matches the free-fall state almost exactly. The second reading is self-consistent and the first is not, so the figure most likely refers to the ejection rather than the failure.

Sources also disagree on the location. The first flight is placed at Caldwell, New Jersey, while at least one account places the loss at the Federal Aviation Administration's National Aviation Facilities Experimental Center, which is at Atlantic City rather than Caldwell. The conflict is recorded here rather than resolved.

The programme was cancelled four months later. The second airframe was never completed and survives in storage, recorded by [National Museum of the United States Air Force, Curtiss-Wright X-19][ref_nmusaf_x19] and [Vertipedia, Curtiss-Wright X-19][ref_vertipedia_x19].

## Comparison With Ground Prediction

The comparison this section usually makes cannot be made, and the reason is itself the finding.

**There is no flight data from the regime the aircraft was built to explore**, because the aircraft never entered it. Four hours of hovering and low-speed work does not test a radial lift force that only becomes significant with forward speed. Every quantity this article computes about cruise, conversion and lift sharing is a prediction against which no X-19 measurement exists.

What does exist is the [X-100][ref_x100], which transitioned once on 13 April 1960 and which Curtiss-Wright regarded as proof. That is a real data point and it is the only one. It establishes that a tilt-propeller with radial lift propellers can convert. It does not establish anything quantitative about the X-19, which was heavier, differently proportioned, and carrying military equipment the X-100 never had.

The wind tunnel record for adjacent configurations is comparatively rich. Tilt-wing and four-propeller models appear in [Grunwald 1961][research_grunwald_1961], [Newsom and Tosti 1959][research_newsom_tosti_1959], [Tosti 1962][research_tosti_1962] and [Winston and Huston 1962][research_winston_huston_1962], slipstream effects on performance and stability in [GOLAND et al 1964][research_goland_1964] and [Butler et al 1966][research_butler_1966], and a tandem-wing configuration in ground effect in [Harry and Trobaugh 1966][research_harry_trobaugh_1966]. **None of it is the X-19**, and the gap between a configuration's literature and an airframe's data is the whole of what this section can report.

## What the Data Changed

Very little, and the reasons are worth separating.

The radial lift force did not enter subsequent practice as a sizing principle. No later production aircraft was given a wing sized on the assumption that its propellers would carry three tenths of the lift slope. The [tiltrotor][ref_tiltrotor] line that eventually reached service in the [V-22][ref_v22] took the opposite approach, using large rotors and a conventional wing.

The tandem-wing arrangement did not propagate either, though it was studied afterward and the canard interference literature of the 1970s, [Gloss and Mckinney 1973][research_gloss_mckinney_1973], [Gloss 1974][research_gloss_1974], [Gloss 1975][research_gloss_1975], [Gloss and Washburn 1977][research_gloss_washburn_1977] and [Gloss et al 1978][research_gloss_1978], covers the same physics in a different application.

**What did propagate is the negative result about drive systems.** Four propellers on two engines requires an interconnected transmission with many gearboxes, each of which is a single point of failure whose failure is not survivable. The X-19 demonstrated that at the cost of the airframe. The tri-service programme's other tilt aircraft, the [XC-142][ref_xc142] and the [X-22][ref_x22], carried the same architecture and the same lesson.

The most useful thing the X-19 changed may be the sharpest and the least flattering. **A programme that flies four hours in twenty-one months is not testing an aircraft**, and the tri-service VTOL effort produced several such programmes at once.

## Where the Framing Breaks Down

**Treating the X-19 through the radial lift force overstates what the radial lift force decided.** The corridor computed above is continuous with the effect switched off. The keystone framing is correct about what the aircraft was sold on and about what its wing area required, and it is wrong if it suggests the configuration depended on the effect for feasibility.

**The keystone is also not what killed the aircraft.** A gearbox did, and no amount of analysis of propeller normal force has anything to say about gear tooth life. An article built around an aerodynamic keystone will underweight the mechanical system that actually determined the outcome, and this one would too if the point were not made explicitly.

**The comparison with the X-18 can be pushed too far.** The two aircraft look adjacent and are adjacent in the designation sequence, but their governing quantities have nothing in common. Immersed fraction is meaningless for the X-19 and propeller normal force is nearly meaningless for the X-18, whose propellers stay roughly aligned with the flow because the whole wing rotates with them.

**This article's own model has a limit.** The in-plane momentum picture treats the disc as an actuator turning a stream tube, which is defensible while the disc is moderately inclined and indefensible once it is close to broadside, where a propeller is a bluff body shedding a wake and no linear proportionality to $\sin\alpha_d$ has any basis. The condition to test is the disc incidence, which is the nacelle angle plus the angle of attack.

$$\alpha_d = i + \alpha \le 60^{\circ}$$

**Five of the ten corridor rows above violate it**, reaching 89.5 degrees at the hover end, so the low-speed half of the corridor should be read as indicative rather than quantitative. This is the same discipline A312 applied when it found its own perfect-gas arithmetic valid to Mach 7.06 against an aircraft that flew at 6.70.

## The Source Base

The vehicle's own literature is thin and mostly encyclopaedic. The keystone's literature is the opposite, being deep, primary, and forty years older than the aircraft.

That inversion is the defining feature here. [Ribner 1943][research_ribner_1943], [Ribner 1943, Formulas for propellers in yaw and][research_ribner_1943_2], [Ribner 1943, Proposal for a propeller side-forc][research_ribner_1943_3], [Ribner 1945][research_ribner_1945] and [Ribner 1945, Propellers in yaw][research_ribner_1945_2] are wartime and immediately post-war work on a stability nuisance, and they are the strongest citations in this article. The X-19 exists because someone read that literature and asked whether the nuisance could be a feature.

The tilt-wing and convertiplane design literature of the late 1950s is well populated, in [McCormick and Mallen 1956][research_mccormick_mallen_1956], [McCormick and Mallen 1957][research_mccormick_mallen_1957], [Stepniewski 1957][research_stepniewski_1957], [Mallen and Dancik 1959][research_mallen_dancik_1959], [DALLAS and IRVIN 1956][research_dallas_irvin_1956] and [McCormick and W. 1956][research_mccormick_w_1956], with the aeroelastic problems in [Loewy and Yntema 1958][research_loewy_yntema_1958].

**What is missing is any primary flight test report for this airframe**, and given four hours of flying, it is possible that little was written.

## Epistemic State

**Historical fact.** The X-19 first flew on 20 November 1963 and was destroyed on 25 August 1965. It made 50 flights totalling four hours and never transitioned. Both crew ejected and survived. The programme was cancelled and the second airframe was never completed. The X-100 preceded it, first hovered free in September 1959, and made a single transition on 13 April 1960. The aircraft began as the company-funded X-200 or M-200 and was adopted by the Tri-Service VTOL programme.

**Published figures taken as given.** Gross weight 13,660 pounds, wing areas 56.1 and 98.5 square feet, spans 19.5 and 23.5 feet, four propellers of 13 feet, two Lycoming T55-L-7 engines of 2,650 shaft horsepower, length 44 feet, maximum speed 400 knots at 20,000 feet, cruise 347.6 knots at 15,000 feet.

**Engineering analysis.** Wing loading of 88.4 pounds per square foot, stall at 136.5 knots, download of 13.2 percent, hover induced velocity of 78.3 feet per second, permitted tip speed of 644.2 feet per second, derived blade chord of 17.2 inches, in-plane recovery fraction of 0.283, cruise lift share of 29.8 percent, equivalent plain wing of 218 to 225 square feet, the corridor table, tandem attitude penalty of 1.65 degrees, control accelerations, cross-shaft torques, and the free-fall budget are all computed here from published geometry and are not quoted from any source.

**Assumed quantities, each of which moves the answers.** Maximum lift coefficient of 1.4, helical tip Mach limit of 0.90, blade loading limit of 0.14, hover figure of merit of 0.70, download drag coefficient of 1.20 with slipstream factor 1.5, propeller efficiency of 0.80 at maximum speed, span efficiencies, an effective tandem aspect ratio of 6.0, a propeller station separation of 20 feet, and radii of gyration at 0.30, 0.30 and 0.35 of the relevant dimension. **The propeller rotational speed is not in the public record and was derived from the cruise requirement rather than taken from a source.**

**A model inconsistency found and fixed rather than carried.** An earlier version of the calculation used a figure of merit of 0.70 in one place and a propeller efficiency of 0.80 in another for what the momentum model treats as a single quantity. The corridor is now reported across both values, and the low-speed boundaries are identical while the high-speed boundaries move by about 5 percent.

**Two errors the equation review exposed, both in the drafted text.** The pitch-moment relation was displayed as $M = fT\ell$, which evaluates to twice the 15,467 foot-pounds quoted in the prose beside it. The quoted value was right and the displayed algebra carried a spurious factor of two, so the article contradicted itself in a way every automated check passed. The yaw inertia was transcribed as 100,565 slug feet squared against a computed 100,690, which left the acceleration built on it correct and the stated inertia wrong. **Writing the relation down has now caught a wrong claim in twelve consecutive articles in this series.** A third defect was introduced by the review itself, an unterminated display block that would have rendered as broken mathematics, and the style checker was extended to catch that class.

**A defect that no automated check would have caught.** The first corridor formulation solved the vertical equilibrium equation for thrust and then tested the same equation, which is satisfied identically at any speed down to zero. It returned 0.6 knots at every nacelle angle below 60 degrees. Nothing flagged it. It was caught by reading the output and finding it absurd, which is the same way A315's 454-knot crossover speed was caught.

**Inference, not established.** That the wide blade was forced by hover at a capped tip speed rather than chosen for radial lift is an inference from the arithmetic, not a statement from any Curtiss-Wright document. That weak yaw control contributed to the recorded control system problems is a candidate explanation only, and the alternative that differential nacelle tilt supplied yaw authority is not excluded by anything here.

**Unresolved conflict in the record.** The location of the final flight is given variously as Caldwell, New Jersey, and as the Federal Aviation Administration's experimental centre at Atlantic City. The reported altitudes and timings of the ejection are mutually inconsistent under one reading and consistent under another, and the article states both rather than choosing silently.

**Written from present knowledge.** The contemporary material postdates the editorial date of this article.

## Out of Scope

Blade element analysis of the propellers, including the twist distribution and the compressibility behaviour of a 17-inch chord at the tip. Structural design of the wings and the nacelle pivots. Aeroelastic behaviour of a heavy nacelle on a short wing, which [Loewy and Yntema 1958][research_loewy_yntema_1958] indicates is not trivial. Gear tooth stress and lubrication, which determined the outcome. Acoustic behaviour, which the X-100 was reported to do well on. The autorotation and engine-out descent case. Ground effect and recirculation during vertical landing, which [Huston and Winston 1960][research_huston_winston_1960], [O'Bryan 1961][research_o_bryan_1961], [Pruyn and Taylor 1970][research_pruyn_taylor_1970] and [Renselaer 1975][research_renselaer_1975] address for adjacent configurations. Cockpit workload and the pilot's task during a conversion that was never flown.

## Conclusion

The X-19 asked whether a propeller could be counted on for lift, and the answer this article computes is that it can, to the tune of about thirty percent of the lift slope in cruise, which is enough to build a wing loading of 88 pounds per square foot on where 61 would otherwise be needed.

**That answer was never confirmed in flight by the aircraft that asked the question.** Fifty flights and four hours produced no transition, and the airframe was destroyed by a gearbox before the regime it was designed for was ever entered. The confirmation that does exist belongs to the X-100, a smaller and lighter demonstrator that transitioned once in 1960.

Three conclusions survive the analysis and one does not. The wide propeller blade was demanded twice over, by hover at a tip speed the cruise capped and by the radial lift force, which makes the configuration more coherent than it appears. The tandem layout supplied for nothing the pitch control that the [X-18][related_post_a315_hiller_x18] required a turbojet to obtain, and supplied yaw control that this analysis finds an order of magnitude short. The interconnected drive that cured the X-18's fatal engine-out asymmetry introduced the gearbox that destroyed the X-19, which is as clean an illustration as this series has produced that **a fix and a failure mode can be the same component**.

The conclusion that does not survive is the one the marketing rested on. The radial lift force did not make this aircraft possible. The corridor closes without it. What it made possible was a smaller wing, and a smaller wing is an economy rather than an enabler.

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45

### Reference

[ref_curtiss_wright]: https://en.wikipedia.org/wiki/Curtiss-Wright
[ref_nmusaf_x19]: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/196863/curtiss-wright-x-19/
[ref_si_x100]: https://airandspace.si.edu/collection-objects/curtiss-wright-x-100/nasm_A19690014000
[ref_tiltrotor]: https://en.wikipedia.org/wiki/Tiltrotor
[ref_v22]: https://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey
[ref_vertipedia_x100]: https://vertipedia.vtol.org/aircraft/getAircraft/aircraftID/810
[ref_vertipedia_x19]: https://vertipedia.vtol.org/aircraft/getAircraft/aircraftID/811
[ref_x100]: https://en.wikipedia.org/wiki/Curtiss-Wright_X-100
[ref_x19]: https://en.wikipedia.org/wiki/Curtiss-Wright_X-19
[ref_x22]: https://en.wikipedia.org/wiki/Bell_X-22
[ref_xc142]: https://en.wikipedia.org/wiki/LTV_XC-142

### Research

[research_albachten_1956]: https://doi.org/10.21236/ad0116273
[research_boswell_1961]: https://doi.org/10.21236/ad0262952
[research_bowen_walker_1972]: https://doi.org/10.21236/ad0758465
[research_brusse_cronk_1965]: https://ntrs.nasa.gov/citations/19660010796
[research_butler_1966]: https://doi.org/10.21236/ad0629637
[research_carlson_1958]: https://doi.org/10.4050/jahs.3.11
[research_chase_1973]: https://doi.org/10.21236/ad0771978
[research_coward_1955]: https://doi.org/10.21236/ad0101718
[research_crigler_gilman_1949]: https://ntrs.nasa.gov/citations/19930085544
[research_crigler_gilman_1952]: https://ntrs.nasa.gov/citations/19930083122
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_dunham_gentry_1989]: https://ntrs.nasa.gov/citations/19900058369
[research_dunham_gentry_1989_2]: https://doi.org/10.4271/892205
[research_gloss_1974]: https://ntrs.nasa.gov/citations/19740020361
[research_gloss_1975]: https://ntrs.nasa.gov/citations/19750015442
[research_gloss_1978]: https://ntrs.nasa.gov/citations/19790005842
[research_gloss_mckinney_1973]: https://ntrs.nasa.gov/citations/19740003706
[research_gloss_washburn_1977]: https://ntrs.nasa.gov/citations/19770022153
[research_goland_1964]: https://doi.org/10.21236/ad0608186
[research_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227988
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_huston_winston_1960]: https://ntrs.nasa.gov/citations/19980227777
[research_kuhn_grunwald_1960]: https://ntrs.nasa.gov/citations/19980227804
[research_loewy_yntema_1958]: https://doi.org/10.4050/jahs.3.1.35
[research_mallen_dancik_1959]: https://doi.org/10.4050/jahs.4.15
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mccormick_mallen_1957]: https://doi.org/10.4050/jahs.2.49
[research_mccormick_w_1956]: https://doi.org/10.21236/ad0159429
[research_meier_1964]: https://doi.org/10.2514/6.1964-175
[research_miller_1948]: https://doi.org/10.2514/8.11623
[research_moellmann_o_connor_1967]: https://doi.org/10.21236/ad0649534
[research_newsom_tosti_1959]: https://ntrs.nasa.gov/citations/19980228402
[research_o_bryan_1961]: https://ntrs.nasa.gov/citations/20040008178
[research_pruyn_taylor_1970]: https://doi.org/10.4050/sm_env_1970-2300
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_renselaer_1975]: https://ntrs.nasa.gov/citations/19750034271
[research_ribner_1943]: https://ntrs.nasa.gov/citations/19930093307
[research_ribner_1943_2]: https://ntrs.nasa.gov/citations/19930093304
[research_ribner_1943_3]: https://ntrs.nasa.gov/citations/19930093306
[research_ribner_1945]: https://ntrs.nasa.gov/citations/19930091896
[research_ribner_1945_2]: https://ntrs.nasa.gov/citations/19930091897
[research_rumph_1942]: https://doi.org/10.2514/8.10936
[research_slaughter_1958]: https://doi.org/10.4050/jahs.3.9
[research_stepniewski_1957]: https://doi.org/10.1017/s2753447200003528
[research_tosti_1962]: https://ntrs.nasa.gov/citations/19620003850
[research_valentine_kader_1976]: https://doi.org/10.21236/ada035756
[research_winston_huston_1962]: https://ntrs.nasa.gov/citations/19630000659

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
[related_post_a315_hiller_x18]: {% post_url 2025-10-24-x_planes_hiller_x18 %}
