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

The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003] and the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]. The keystone's own literature is older than the aircraft by eighteen years and belongs to aerodynamic stability and not to vertical flight, which is [Ribner 1945, Propellers in yaw][research_ribner_1945_2] and [Ribner 1945][research_ribner_1945].

## The Research Question

### The Keystone Is the Propeller Normal Force

**The keystone is how much lift a propeller produces without pointing at the sky.**

A propeller meeting the air along its own axis produces thrust and nothing else. Incline the axis to the flow and the symmetry breaks. Each blade sees a velocity that varies around the azimuth, the loading varies with it, and the disc as a whole exerts a force perpendicular to its axis. It was understood by 1909 that a yawed propeller acts like a fin, and [Rumph et al 1942][research_rumph_1942] treated the effect as a stability problem, which is what it had always been. A tractor propeller ahead of the centre of gravity is destabilising precisely because this force exists.

Curtiss-Wright proposed to stop treating it as a nuisance and start treating it as lift.

If the propellers carry part of the lift, the wing carries less, so the wing can be smaller. Writing the argument down makes its leverage visible. If the propellers supply a fraction $\phi$ of the lift at the slowest wing-borne speed, the wing need only supply the rest.

$$S = \frac{2 W \left( 1 - \phi \right)}{\rho V_{\text{conv}}^{2} C_{L,\max}}$$

A smaller wing is lighter, has less drag at high speed, and presents less area to the downwash in hover. The X-19's 88 pounds per square foot is the arithmetic consequence of taking that argument seriously.

The same force that supplies $\phi$ is a nuisance elsewhere, and the sign is what distinguishes the two readings. A propeller mounted a distance $x_p$ ahead of the centre of gravity contributes a pitching moment that grows with angle of attack.

$$\frac{\partial C_m}{\partial \alpha} = \frac{x_p}{q S \bar{c}} \frac{\partial N}{\partial \alpha}$$

That derivative is positive for a tractor propeller, which is destabilising, and it is the reason the effect was studied for thirty years before anyone proposed to exploit it.

**The scale of that literature is the strongest evidence that the X-19's premise was not eccentric.** Wind tunnel investigation of how a running propeller moves an aeroplane's neutral point was a standing programme at the National Advisory Committee for Aeronautics, hereafter NACA, through the 1940s and 1950s, in [Delany 1942][research_delany_1942], [Pitkin 1943][research_pitkin_1943], [Schuldenfrei 1944][research_schuldenfrei_1944], [Purser and Spear 1947][research_purser_spear_1947], [Hagerman 1947][research_hagerman_1947], [Weil and Sleeman 1948][research_weil_sleeman_1948], [Brewer and May 1948][research_brewer_may_1948], [Lange and McLemore 1950][research_lange_mclemore_1950], [Queijo et al 1953][research_queijo_1953], [Sleeman 1953][research_sleeman_1953], [Vollo and Brassaw 1956][research_vollo_brassaw_1956], [Sleeman 1957][research_sleeman_1957], [Goodson 1961][research_goodson_1961], [Donlan 1976, Factors affecting static longitudi][research_donlan_1976_2], [Nagy and Kirsten 1976][research_nagy_kirsten_1976], [Ostowari and Naik 1986][research_ostowari_naik_1986].

Every one of those reports treats the propeller force as a correction to be predicted and designed around. **Curtiss-Wright's proposal was to change its sign in the accounting, not its magnitude in the physics.**

### Why This Was the Binding Unknown in 1960

The competing configurations of the moment each had a defect that was already visible. The tail-sitter of the [X-13][related_post_a310_ryan_x13] required the pilot to land looking backward and upward. The tilt-wing of the [X-18][related_post_a315_hiller_x18] stalled the un-immersed part of its wing throughout conversion. The deflected slipstream arrangements studied by [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960] and [Grunwald 1961][research_grunwald_1961] paid a large download penalty.

The tilt-propeller avoided all three. Nothing about it requires the wing to stall, nothing requires the pilot to fly backward, and the wing is small enough that the download is modest. The competing arrangements were compared against one another continuously in the design literature of the period, in [Hickey 1956][research_hickey_1956], [Koenig and Quigley 1960][research_koenig_quigley_1960], [Quigley and Koenig 1961][research_quigley_koenig_1961], [Putman 1961][research_putman_1961], [Hargraves 1961][research_hargraves_1961], [Newsom 1962][research_newsom_1962], [Newsom 1962, Force-test Investigation of the St][research_newsom_1962_2], [Breul 1963][research_breul_1963], [Goodson 1966][research_goodson_1966], [Goodson 1966, Comparison of wind-tunnel and flig][research_goodson_1966_2], [Beppu et al 1966][research_beppu_1966], [Curtiss et al 1967][research_curtiss_1967], [Strand and Levinsky 1969][research_strand_levinsky_1969], [Kvaternik 1973][research_kvaternik_1973], [Widdison et al 1974][research_widdison_1974], [Detore and Sambell 1975][research_detore_sambell_1975], [Sambell 1976][research_sambell_1976], [Morisset 1977][research_morisset_1977], [Bartie et al 1986][research_bartie_1986], [Huston et al 1989][research_huston_1989]. **The unknown was not whether the configuration could hover or cruise. It was whether the propeller force that made the small wing defensible was real at the size claimed.**

That question had an answer in the literature and the answer was not obviously encouraging. [Ribner 1943][research_ribner_1943] and its final form [Ribner 1945, Propellers in yaw][research_ribner_1945_2] give a theory calibrated against experiment, and [Crigler and Gilman 1949][research_crigler_gilman_1949] and [Crigler and Gilman 1952][research_crigler_gilman_1952] give methods for computing the forces on a propeller in pitch or yaw. The forces are real. Whether they are large enough to size an aircraft around is a question of magnitude, and magnitude is what this article computes.

## Programme Origin

The X-19 did not begin as a military aircraft and did not begin with that designation. **The programme's own final report is the primary source for what follows.** It is Air Force Flight Dynamics Laboratory technical report AFFDL-TR-66-195, written by Curtiss-Wright's Wright Aeronautical Division and issued in May 1967 in two volumes, [Fluk et al 1967, Volume I][research_fluk_1967] and [Fluk et al 1967, Volume II][research_fluk_1967_2], hereafter the final report. It records that [Curtiss-Wright][ref_curtiss_wright] designed the aircraft first as the Model 200, or M-200, a six-place corporate executive transport with four rotating-combustion engines of 580 horsepower each, a gross weight of 10,000 pounds and a maximum level speed of 400 miles an hour at 16,000 feet.

Before the transport there was a demonstrator. The [Curtiss-Wright X-100][ref_x100] was built to test two things at once, the radial lift force itself and the gimballed nacelles a tilt-propeller needs. The [Smithsonian National Air and Space Museum][ref_si_x100] records that construction began on 20 February 1958, that tethered hovering started on 20 April 1959, and that **the first and only transition from vertical to high-speed flight was made on 13 April 1960**, and [Vertipedia][ref_vertipedia_x100] places the first free hover in September 1959. The final report describes a two-place aircraft of 3,500 pounds with one Lycoming YT53 engine of 825 horsepower driving two three-blade propellers of 10 feet, a wing of 22.5 square feet, and a wing loading it puts in excess of 170 pounds per square foot, although its own weight and area give $3{,}500 / 22.5 = 156$ pounds per square foot. It gives 220 hours of ground running and 10 flight hours, while the museum gives fourteen hours of flight. The museum records that the aircraft went to the National Aeronautics and Space Administration, hereafter NASA, in October 1960 for ground erosion tests at Langley, and the final report adds a test in the 40 by 80 foot wind tunnel at Ames to obtain propeller loads at high tilt.

The X-100 also showed what the transport would have to fix. The final report lists insufficient hover control power, roll and yaw coupling in hover, and strong pitch-up with forward speed, and it gives these as the reasons for moving to four propellers on two tandem wings, since four propellers at two stations give pitch and roll control without an auxiliary device. Then the company's management changed. The final report states that after the change it was decided that a new aircraft with new and untried engines had little hope, so the design was redrawn around two Lycoming T55-L-5 turboshaft engines and pointed toward military use, and it states that no military specification existed, so the design objectives were Curtiss-Wright's own. The museum records that the company persuaded the services to fund the aircraft under a tri-service agreement between the Army, the Navy and the Air Force, with the Air Force managing the project, and that two airframes were built for what became a vertical take-off and landing programme, hereafter VTOL.

**The sequence is worth stating plainly because it is unusual.** A company proved a concept on a small demonstrator, redesigned the follow-on when its management changed, and sold it to a government that had written no requirement for it. The aircraft that resulted weighed 13,660 pounds, nearly four times the X-100's 3,500 and well above the 10,000 for which, the final report notes, its transmission had first been designed.

## Sizing From First Principles

### The Wing Cannot Carry the Aircraft

Start with the number that makes everything else necessary. The [final report's][research_fluk_1967] dimension table gives the forward wing a span of 19.5 feet over 56.1 square feet and the aft wing a span of 21.5 feet over 98.5 square feet, both measured to the nacelle centrelines, with constant chords of 34.5 and 55.0 inches. The overall rear-wing span of 23.5 feet in the [Jane's-derived specification][ref_x19] is a different measurement, and it is the wrong one here, because the propeller discs are centred on the nacelles. Aspect ratio and mean chord follow from span and area alone.

$$\text{AR} = \frac{b^{2}}{S}, \qquad \bar{c} = \frac{S}{b}$$

which gives 6.78 and 2.88 feet forward, and 4.69 and 4.58 feet aft. The report states aspect ratios of 6.8 and 4.7, and the chords are its 34.5 and 55.0 inches. Total area is 154.6 square feet against the report's normal gross weight of 13,660 pounds.

Each surface has its own lift-curve slope, reduced from the two-dimensional value by its finite span, where $a_0$ is $2\pi$ per radian and $e$ is the span efficiency.

$$a = \frac{a_0}{1 + a_0 / \left( \pi e \, \text{AR} \right)}$$

At $e = 0.90$ this is 4.732 per radian forward and 4.264 aft. The aircraft's single equivalent slope is the area-weighted mean of the two, and it is used throughout the article.

$$\bar{a} = \frac{S_f a_f + S_a a_a}{S_f + S_a} = 4.434 \ \text{rad}^{-1}$$

Wing loading follows immediately.

$$\frac{W}{S} = \frac{13{,}660}{154.6} = 88.4 \ \text{lb/ft}^2$$

The report itself calls the loading approximately 85 pounds per square foot on both wings.

The speed at which a wing alone supports that loading is the stall speed, where $\rho$ is density, $S$ is wing area and $C_{L,\max}$ the maximum lift coefficient.

$$V_{s} = \sqrt{\frac{2W}{\rho S C_{L,\max}}}$$

For an unflapped wing with $C_{L,\max} = 1.4$ at sea level this gives 230.4 feet per second, or **136.5 knots**. At 1.2 it is 147.5 knots and at 1.6 it is 127.7 knots. The final report gives both wings zero incidence, zero dihedral and zero sweepback, and its only high-lift device is a plain flap of 15.16 square feet on the forward wing, so the middle value is used and the two bounds show how far the answer moves with it.

**An aircraft that stalls at 136 knots and is required to land at zero has a gap of 136 knots to explain.** Tilting the propellers explains most of it, because a propeller pointed upward is a lifting device regardless of any subtlety. The radial lift force is what explains the rest, and the rest is where the wing area was won.

### What a Propeller Does in Oblique Flow

Write the force from momentum, not from blade elements, because the momentum form has exactly one unknown and that unknown can be estimated from geometry.

Let the disc of area $A$ meet a freestream $V$ with its axis at angle $\alpha_d$ to the flow. Resolve the freestream into a component along the axis and a component in the plane of the disc.

$$V_{\text{axial}} = V \cos\alpha_d, \qquad V_{\text{in-plane}} = V \sin\alpha_d$$

The mass flow through the disc is set by the axial component plus whatever the propeller induces, where $v_i$ is the induced velocity.

$$\dot{m} = \rho A \left( V \cos\alpha_d + v_i \right)$$

The blades resist the in-plane component and turn part of it toward the axis. Let $k$ be the fraction of the in-plane momentum flux the disc removes. The reaction on the aircraft is the radial lift force.

$$N = k \, \rho A \left( V \cos\alpha_d + v_i \right) V \sin\alpha_d$$

**This is the keystone relation of the article and everything downstream depends on $k$.**

### The Fin Analogy Fixes the Unknown

Leaving $k$ free would make the calculation circular, since any wing area could then be justified by choosing $k$ to suit. [Ribner 1945, Propellers in yaw][research_ribner_1945_2] supplies the constraint. Ribner extends the fin analogy to the form of the side-force expression and identifies the effective fin area with **the projected side area of the propeller**, meaning the blade area seen from the side and not the disc area.

Write the propeller as a fin of area $S_f$ and lift-curve slope $a_b$ and equate the two expressions at small angle and high speed, where $v_i$ vanishes against $V$.

$$\tfrac{1}{2} \rho V^2 S_f a_b \alpha_d = k \rho A V^2 \alpha_d$$

The dynamic pressure, the freestream and the disc angle all cancel, which is why the fin analogy is useful, not merely suggestive. What remains is pure geometry.

$$k = \frac{S_f a_b}{2A}$$

The projected side area of a propeller with $B$ blades of chord $c$ and radius $R$ is not simply the blade area, because a rotating blade presents its full width to the side only twice per revolution. The azimuthal mean of that projection supplies the factor.

$$\frac{1}{2\pi} \int_{0}^{2\pi} \left| \cos\psi \right| \, d\psi = \frac{2}{\pi}$$

Multiplying the blade area by that mean gives the effective fin.

$$S_f = \frac{2}{\pi} B c R$$

So $k$ follows from blade chord, and the final report records the blade. Before using it, the rotational speed has to be settled, because blade loading depends on it as strongly as on chord.

### The Cruise Requirement Caps the Tip Speed

The [Jane's-derived specification][ref_x19] quotes a maximum speed of 400 knots at 20,000 feet. The [final report][research_fluk_1967] states the design objective as a speed range up to 400 miles an hour, which it equates to Mach 0.65. Those two statements disagree. Four hundred miles an hour is 586.7 feet per second, which is Mach 0.566 at 20,000 feet and cannot reach Mach 0.65 at any altitude of the standard atmosphere, whose slowest speed of sound is 968.1 feet per second, while 400 knots at 20,000 feet is Mach 0.651. The 400-knot figure is used here. A propeller at 400 knots is close to its own limit, because the blade tip sees the vector sum of flight speed and rotational speed. Write the helical tip Mach number with $a$ the speed of sound, $\Omega$ the rotational rate and $R$ the radius.

$$M_{h} = \frac{\sqrt{V^2 + (\Omega R)^2}}{a}$$

Propeller efficiency collapses as $M_h$ approaches unity, so take 0.90 as the working ceiling and solve for the rotational tip speed the cruise permits.

$$\Omega R \le \sqrt{\left( M_{h,\lim} a \right)^2 - V^2}$$

At 20,000 feet the dynamic pressure at that speed is 288.6 pounds per square foot, the speed of sound is 1,036.8 feet per second and 400 knots is 675.1 feet per second, a flight Mach number of 0.651. The ceiling gives 933.2 feet per second for the helical tip, and the rotational component that leaves is **644.2 feet per second**. The rotational rate and the shaft speed follow.

$$\Omega = \frac{\Omega R}{R} = \frac{644.2}{6.5} = 99.11 \ \text{rad/s}, \qquad n = \frac{60 \, \Omega}{2\pi} = 946 \ \text{rpm}$$

**The record confirms the derivation.** The propeller qualification schedule in the final report runs the propellers at 957 revolutions per minute for maximum-speed cruise, and the [specification][ref_x19] gives 955. The derived 946 is 1.1 percent below the record, and the record's speed puts the helical tip at

$$M_h = \frac{\sqrt{675.1^2 + 651.4^2}}{1{,}036.8} = 0.905, \qquad \Omega R = \frac{2\pi (957)}{60} (6.5) = 651.4 \ \text{ft/s}$$

which is the assumed 0.90 ceiling almost exactly. **That is a slow propeller.** Take the tip speed back to sea level and compare it against the static case, where no flight speed adds to it.

$$M_{\text{tip,static}} = \frac{\Omega R}{a_0} = \frac{644.2}{1{,}116.5} = 0.577$$

where a conventional propeller would run near 0.8. That is what the propeller would see if it hovered at its cruise speed, and the next section shows that it did not.

The other measure of how hard this propeller is working is the advance ratio, the distance advanced per revolution against the diameter.

$$J = \frac{V}{n D} = \frac{675.1}{(15.77)(13)} = 3.29$$

which is high, and is the regime in which a propeller behaves least like a hovering rotor.

**This regime has its own literature, distinct from that of the hovering rotor.** The high-speed propeller was a continuous research subject from the wartime compressibility work to the advanced turboprop programmes, in [Wood and Woodward 1944][research_wood_woodward_1944], [Stack et al 1950][research_stack_1950], [Doetsch and Mark 1953][research_doetsch_mark_1953], [Perisho 1959][research_perisho_1959], [Watts and Biggers 1972][research_watts_biggers_1972], [Hohenemser and Prelewicz 1974][research_hohenemser_prelewicz_1974], [Reader 1980][research_reader_1980], [Bober and Mitchell 1980][research_bober_mitchell_1980], [Mitchell and Mikkelson 1982][research_mitchell_mikkelson_1982], [Gilchrist 1983][research_gilchrist_1983], [Takallu and Lessard 1991][research_takallu_lessard_1991], [Gazzaniga and Rose 1992][research_gazzaniga_rose_1992], [Harris 1996][research_harris_1996], [Gur and Rosen 2005][research_gur_rosen_2005], [Cavcar 2011][research_cavcar_2011].

Two of those bear directly on the X-19. Wind tunnel measurement of two-blade propellers to forward Mach numbers of 0.725 established where efficiency begins to fall, which is the constraint that sets the tip speed above. A later reanalysis of early high-speed propellers applied explicitly to civil tiltrotor configurations is the same question asked again for the configuration the X-19 anticipated.

### What Hover Asks of the Propeller

Hovering thrust must exceed weight, since the wings sit under the discs and are pushed down by the slipstream. Compute the download first. With the nacelles at the tips, the disc reaches inboard by one radius from each tip, so the immersed fraction of a semi-span is the radius over the semi-span whenever the disc does not reach the root.

$$f_{\text{imm}} = \frac{R}{b/2} = \frac{2R}{b}$$

which is 0.667 forward and 0.605 aft, and the immersed area is the sum over the two surfaces.

$$S_{\text{imm}} = \sum_j f_{\text{imm},j} S_j = 97.0 \ \text{ft}^2 = 62.7\% \ \text{of the wing}$$

measured for adjacent configurations and not calculated, in [White et al 1960][research_white_1960], [Curtiss et al 1985][research_curtiss_1985], [Chen and Schweikhard 1985][research_chen_schweikhard_1985], [Leonard, III 2001][research_leonard_iii_2001], [Qin et al 2017][research_qin_2017].

The slipstream velocity at the wing is a multiple $\lambda$ of the induced velocity, and the download is that dynamic pressure acting on the immersed area with a normal-flow drag coefficient.

$$D_{\text{down}} = \tfrac{1}{2} \rho \left( \lambda v_i \right)^2 S_{\text{imm}} C_{D,\perp}$$

Thrust and download depend on each other through $v_i$, so they solve together. Substituting the momentum-theory induced velocity into the download makes the pair **linear** in thrust, not requiring iteration, because $v_i^2$ is proportional to $T$.

$$T = W + \frac{\lambda^{2} S_{\text{imm}} C_{D,\perp}}{4 A} \, T \quad \Longrightarrow \quad T = \frac{W}{1 - \lambda^{2} S_{\text{imm}} C_{D,\perp} / 4A}$$

The coefficient is 0.1233, so the download is **1,921 pounds, or 14.1 percent of gross weight**, and the required thrust is 15,581 pounds. The [final report][research_fluk_1967] gives the measured download only in figures, but it states two things that bear on this estimate. The download measured on the full-scale X-100 and on its model was higher than predicted, and the blockage of the rear wing raised propeller thrust by 3 or 4 percent, which is a correction the momentum model does not contain. Momentum theory then gives the induced velocity, where $A$ is the total disc area of 530.9 square feet.

$$v_i = \sqrt{\frac{T}{2 \rho A}} = 78.57 \ \text{ft/s}$$

Ideal power in hover is the thrust acting through the induced velocity, and the figure of merit is what converts it into a shaft requirement.

$$P_{\text{ideal}} = T v_i = 2{,}226 \ \text{hp}, \qquad P_{\text{req}} = \frac{P_{\text{ideal}}}{\text{FM}} = 3{,}180 \ \text{hp}$$

Against 5,300 installed that is a comfortable margin. The momentum-theory result and its experimental corrections are long established, in [Castles and Gray 1951][research_castles_gray_1951], [Warsett 1953][research_warsett_1953], [Blaser 1969][research_blaser_1969], [Boatwright and Clingan 1969][research_boatwright_clingan_1969], [Parker et al 1972][research_parker_1972], [Velkoff 1981][research_velkoff_1981], [Naumowicz and Smith 1992][research_naumowicz_smith_1992], [Talbot et al 1994][research_talbot_1994], [Zhao et al 2014][research_zhao_2014], [Ramasamy 2015][research_ramasamy_2015], and one of those addresses a high disc loading propeller in cross flow by vortex-lattice methods, which is the keystone condition approached by a different route entirely.

$$\frac{P_{\text{inst}}}{P_{\text{req}}} = \frac{5{,}300}{3{,}180} = 1.67$$

The record allows one check on this. The propeller and transmission qualification schedule in the final report, written for the 13,660-pound aircraft, sets 860 horsepower at each propeller for take-off and hover, and dividing the ideal power by that total gives the figure of merit the schedule implies.

$$P_{\text{sched}} = 4 \times 860 = 3{,}440 \ \text{hp}, \qquad \text{FM}_{\text{sched}} = \frac{2{,}226}{3{,}440} = 0.647$$

That is below the 0.70 assumed here, and well below the 0.80 the report says the designers expected when they chose the disc loading. A qualification schedule is a design load case rather than a measurement, so this bounds the assumption rather than replacing it.

### The Blade the Record Gives

Thrust scales with the square of tip speed, which is why a slow propeller must be wide.

$$T_1 = C_T \rho A_1 (\Omega R)^{2}$$

**The X-19 did not hover at its cruise speed.** The qualification schedule runs the propellers at 1,204 revolutions per minute for take-off and hover, 1,066 in transition and 957 in cruise, and the flight test summary in [Volume II][research_fluk_1967_2] records the pilot changing propeller speed in flight at 50 to 60 knots from 98.5 to 88 percent of the power-turbine speed and back. The hover speed gives a tip speed of

$$\Omega R = \frac{2\pi (1{,}204)}{60} (6.5) = 819.5 \ \text{ft/s}, \qquad M_{\text{tip}} = \frac{819.5}{1{,}116.5} = 0.734$$

which is the "approximately 820 feet per second" the report states for peak static thrust.

The report also gives the blade. Each propeller has three blades of NACA 64 sections, a blade area of 8.4 square feet and an activity factor of 168. Activity factor weights chord by the cube of radius,

$$\text{AF} = \frac{10^{5}}{16} \int_{0.15}^{1} \frac{c}{D} \, x^{3} \, dx$$

where $x$ is the fraction of tip radius, so a blade of constant chord with the same activity factor has the chord

$$c_{\text{AF}} = \frac{\text{AF} \, D}{\tfrac{10^{5}}{16} \cdot \tfrac{1 - 0.15^{4}}{4}} = \frac{(168)(13)}{1{,}561.7} = 1.398 \ \text{ft}$$

The blade area must be per blade. If 8.4 square feet were the whole propeller, each blade would average a chord of 0.431 feet and an activity factor of 51.7, which is a third of the stated 168. That reading is an inference from the two figures, since the table does not say. Spread over the radius, the area gives a mean chord and a solidity, where solidity is blade area over disc area.

$$\bar{c} = \frac{A_b}{R} = \frac{8.4}{6.5} = 1.292 \ \text{ft}, \qquad \sigma = \frac{B A_b}{\pi R^{2}} = \frac{(3)(8.4)}{132.73} = 0.190$$

**A mean chord of 15.5 inches on a 13-foot propeller.** The ratio of chord to radius is 0.199, where a conventional propeller runs near 0.09, and the blade aspect ratio is that ratio inverted.

$$\text{AR}_b = \frac{R}{\bar{c}} = \frac{6.5}{1.292} = 5.03$$

which is a wing rather than a blade.

Blade loading $C_T/\sigma$ is what stalls a rotor, and 0.14 is a common limit for a heavily twisted blade. At the hover tip speed, with one quarter of the total thrust including download, the documented blade sits far below it.

$$C_T = \frac{T_1}{\rho A_1 (\Omega R)^2} = \frac{3{,}895}{(0.002377)(132.73)(819.5)^{2}} = 0.01838, \qquad \frac{C_T}{\sigma} = 0.097$$

Had the propellers hovered at the 644.2 feet per second the cruise permits, the same thrust would need a thrust coefficient of 0.02975 and a blade loading of 0.157, beyond the limit, and holding the limit would need a chord of

$$c = \frac{\pi R}{B} \cdot \frac{C_T}{0.14} = \frac{\pi (6.5)}{3} \cdot \frac{0.02975}{0.14} = 1.446 \ \text{ft}$$

or 17.4 inches. The variable propeller speed is what spared the blade that requirement.

Stall on a heavily loaded rotor blade was measured and modelled repeatedly, and the solidity that follows from it is the classical design variable, in [Saari and Sorin 1946][research_saari_sorin_1946], [Delano 1947][research_delano_1947], [Chawla 1952][research_chawla_1952], [Meyer and Falabella 1953][research_meyer_falabella_1953], [Hirsch 1954][research_hirsch_1954], [Castles and Durham 1956][research_castles_durham_1956], [Bradley 1956][research_bradley_1956], [Liiva 1968][research_liiva_1968], [Fisher and McCroskey 1971][research_fisher_mccroskey_1971], [Bobo 1972][research_bobo_1972], [Gabel and Tarzanin 1972][research_gabel_tarzanin_1972], [Bellinger 1972][research_bellinger_1972], [Crimi 1975][research_crimi_1975], [Borst 1978][research_borst_1978], [Gentry et al 1991][research_gentry_1991], [Yamauchi and Johnson 1994][research_yamauchi_johnson_1994].

**One of those is the precise experiment this article's argument needs.** A wind-tunnel investigation of the effect of high solidity on propeller characteristics at high forward speed asks exactly the question the X-19's blade answers, and it was published in 1947, sixteen years before the aircraft flew.

### The Wide Blade Was Chosen for Radial Force

Photographs of the X-19 show propellers of remarkable width, and the final report says why. Its propeller design section states that the blades were configured to generate high values of radial force while keeping efficiency high at take-off and cruise, that the diameter was fixed by the disc loading and every other feature by a compromise among cruise, take-off and radial lift, and that a narrower blade with a higher design lift coefficient was rejected because the radial force relation requires a large blade area. Three blades were chosen over four so that each could be wide and thick inboard while staying below 30 percent thickness, and two blades were rejected because they would generate very high vibratory loads at high shaft angles.

**The width was therefore bought for the radial lift force**, and the hover arithmetic above shows what it cost. At hover speed the blade is lightly loaded, with a blade loading of 0.097, which is consistent with the report's stated aim of lightly loaded propellers turning slowly for low noise. Only hovering at the cruise speed would have demanded such a blade on its own, and the aircraft did not do that. [Dunham and Gentry 1989][research_dunham_gentry_1989] and [Dunham and Gentry 1989, The Effect of Solidity on Propelle][research_dunham_gentry_1989_2] address exactly this coupling, since solidity is the quantity blade chord expresses and normal force is what it produces.

Feeding the documented blade back gives the projected side area and the recovery fraction.

$$S_f = \frac{2}{\pi} B A_b = \frac{2}{\pi}(3)(8.4) = 16.04 \ \text{ft}^2 \ \text{per propeller}$$

With a blade lift-curve slope of 4.358 per radian at aspect ratio 5.03, the recovery fraction is

$$k = \frac{(16.04)(4.358)}{2(132.73)} = 0.263$$

**The disc removes about 26 percent of the in-plane momentum that passes through it.** The value is physically admissible, being safely below unity, and it was obtained from the documented geometry rather than chosen.

The assumption the keystone relation makes, that the normal force grows in proportion to the sine of the disc angle, was measured at full scale before the X-19 flew. [Yaggy and Rogallo 1960][research_yaggy_rogallo_1960] tested three full-scale propellers in the Ames 40 by 80 foot wind tunnel at shaft angles from 0 to 85 degrees, one of them a ten-foot Curtiss-Wright propeller designed to produce large normal forces, and found normal force, yawing moment and pitching moment nearly linear in shaft angle over large ranges at constant blade angle and effective advance ratio. The final report cites that measurement among its own sources. Later work reports the effect of solidity and inclination on propeller-nacelle force coefficients, which is the same pairing this section derives by hand. **A quantity this article obtains from a fin analogy and a projected area is a quantity somebody else measured.**

### How Much Lift the Propellers Actually Supply

The [final report][research_fluk_1967_2] gives the cruise speed as 325 knots at 15,000 feet, where its estimated lift-to-drag ratio of 7.1 is best for that altitude. The [Jane's-derived specification][ref_x19] gives 347.6 knots, and the report's figure is used. Dynamic pressure and the lift coefficient the aircraft must reach follow directly.

$$q = \tfrac{1}{2} \rho V^{2} = 225.0 \ \text{lb/ft}^{2}, \qquad C_L = \frac{W}{q S} = 0.393$$

which is unremarkable, and corresponds to an attitude of 5.07 degrees before any interference is allowed for.

$$\alpha = \frac{C_L}{\bar{a}} = \frac{0.393}{4.434} = 0.0886 \ \text{rad}$$

Compare the lift slopes of the two contributors. For the wings, with $\bar{a} = 4.434$ per radian area-weighted across the two surfaces,

$$\frac{\partial L}{\partial \alpha} = q S \bar{a} = 154{,}238 \ \text{lb/rad}$$

and for the four propellers, from the keystone relation at small angle,

$$\frac{\partial N}{\partial \alpha} = 4 k \rho A_1 (V + v_i) V = 63{,}148 \ \text{lb/rad}$$

so the propellers supply

$$\frac{\partial N / \partial \alpha}{\partial N / \partial \alpha + \partial L / \partial \alpha} = 29.0\%$$

of the incidence-dependent lift, with the thrust set by a lift-to-drag ratio of 8. The figure moves by less than a tenth of a percentage point across lift-to-drag ratios from 7 to 10, because $v_i$ is about two feet per second at this speed and contributes almost nothing.

**Curtiss-Wright's claim survives the arithmetic.** Roughly three tenths of the lift slope in cruise comes from the propellers. The final report's own design statement is that at the design cruise condition the propellers would generate at least 20 percent of the lift required, with the front propellers at a shaft angle of 2.8 degrees at 271 knots equivalent airspeed. The two figures measure different things, a share of the lift slope here and a share of the total lift there, so they agree in size without testing each other.

The mutual interference between a propeller and the surface behind it is the older half of the same subject, and it was worked continuously from the 1940s onward, in [Katzoff 1940][research_katzoff_1940], [Thoren and Johnson 1940][research_thoren_johnson_1940], [Purser and Spear 1946][research_purser_spear_1946], [Spreemann and Kuhn 1956][research_spreemann_kuhn_1956], [Kuhn 1957][research_kuhn_1957], [Brenckmann 1958][research_brenckmann_1958], [Vidal et al 1960][research_vidal_1960], [Kuhn and Grunwald 1961][research_kuhn_grunwald_1961], [Welge and Crowder 1978][research_welge_crowder_1978], [Bencze et al 1978][research_bencze_1978], [Rizk 1980][research_rizk_1980], [Welge et al 1981][research_welge_1981], [Johnson and White 1983][research_johnson_white_1983], [Miley et al 1985][research_miley_1985], [Howard et al 1985][research_howard_1985], [Miley et al 1986][research_miley_1986], [Howard and Miley 1989][research_howard_miley_1989], [Johnson et al 1991][research_johnson_1991], [Applin et al 1994][research_applin_1994], [Gentry et al 1994][research_gentry_1994].

**The X-19 sits at an unusual point in that literature.** A tilt-wing or a deflected-slipstream aircraft wants the slipstream **on** the wing, and most of the work above is about arranging that. The X-19 wants lift from the disc itself and treats the slipstream over the wing as a secondary effect, which inverts the usual emphasis without leaving the field.

### What That Bought, Computed Two Ways

The honest counterfactual is not to switch the radial lift force off and leave the wing unchanged, which describes no aircraft anyone would build. It is to hold the conversion speed fixed and ask how much wing would be needed without the propellers' help.

The first route ignores drag and thrust entirely. The wing works at its stall angle, which is the maximum lift coefficient over the equivalent slope.

$$\alpha_{\text{stall}} = \frac{C_{L,\max}}{\bar{a}} = \frac{1.4}{4.434} = 0.3157 \ \text{rad} = 18.1^{\circ}$$

With the nacelles horizontal the propeller axis sits at that same angle to the flow, so the balance to solve is the wing at maximum lift plus the keystone relation evaluated at the stall angle.

$$W = \tfrac{1}{2} \rho V^{2} S C_{L,\max} + 4 k \rho A_1 \left( V \cos\alpha_{\text{stall}} + v_i \right) V \sin\alpha_{\text{stall}}$$

Both terms grow as $V^2$ apart from the small induced-velocity contribution, so the solution is close to a closed form and the speed falls to **115.8 knots**, against **136.5 knots** for the wing alone. Wing area scales with the square of that speed.

$$\frac{S_{\text{equiv}}}{S} = \left( \frac{V_{\text{without}}}{V_{\text{with}}} \right)^{2} = 1.391$$

which puts the equivalent plain wing at 215.1 square feet and 63.5 pounds per square foot.

The second route reads the same quantity off the fully trimmed corridor derived below, where drag, thrust and induced velocity are all present, and gets 116.7 knots against 138.0 knots, an equivalent wing of 216.3 square feet at 63.2 pounds per square foot. **The two routes differ by 0.6 percent**, which is the useful part, since they share no machinery beyond the keystone relation itself.

The conclusion is specific. Without the radial lift force the X-19 would have needed a wing of roughly 215 square feet at about 63 pounds per square foot, **which is an ordinary transport wing loading of the period**. The radial lift force is exactly what separates 88 from 63.

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

**The induced part of that split is not a detail for an aircraft with two wings.** Trim on a multi-surface aeroplane costs drag in a way a single wing does not, because the two surfaces can be loaded against each other, and that cost has a literature of its own in [Lockwood Taylor 1942][research_taylor_1942], [Nissen et al 1948][research_nissen_1948], [Payne 1958][research_payne_1958], [Churchill and Harrington 1959][research_churchill_harrington_1959], [Milla and Blick 1966][research_milla_blick_1966], [Lundry 1967][research_lundry_1967], [Katz et al 1980][research_katz_1980], [Lottati 1984][research_lottati_1984], [Bennett 1984][research_bennett_1984], [Goodrich et al 1989][research_goodrich_1989], [Chiocchia and Pignataro 1995][research_chiocchia_pignataro_1995]. One of those gives a closed-form trim solution minimising drag for aircraft with multiple longitudinal control surfaces, and another treats the induced drag reduction available from propeller and wing interaction directly.

Thrust available at any other speed is not this quantity divided by speed, which diverges at the hover. Momentum theory with the same power gives a form that stays finite at zero.

$$2 \rho A_1 v_i \left( V + v_i \right)^{2} = \frac{\eta_p P_{\text{shaft}}}{4}, \qquad T = 4 \cdot 2 \rho A_1 v_i \left( V + v_i \right)$$

A solution exists only where the angle of attack it demands is below the stall and the thrust it demands is below what the engines can deliver. Those two ceilings are the corridor, and at sea level they give the following.

| Nacelle angle | Minimum | Maximum | Width |
|---|---|---|---|
| 90 degrees | 3.0 kt | 57.5 kt | 54.5 kt |
| 80 degrees | 3.0 kt | 74.1 kt | 71.1 kt |
| 70 degrees | 12.4 kt | 85.9 kt | 73.5 kt |
| 60 degrees | 52.7 kt | 102.5 kt | 49.8 kt |
| 50 degrees | 71.7 kt | 119.1 kt | 47.4 kt |
| 40 degrees | 83.5 kt | 138.0 kt | 54.5 kt |
| 30 degrees | 90.7 kt | 166.5 kt | 75.8 kt |
| 20 degrees | 100.1 kt | 209.2 kt | 109.0 kt |
| 10 degrees | 107.2 kt | 270.8 kt | 163.5 kt |
| 0 degrees | 116.7 kt | 325.3 kt | 208.6 kt |

Continuity is a condition on consecutive rows rather than an impression from the table. A conversion can be flown at constant speed through a nacelle step only where the bands share a speed.

$$V_{\min}(i_{n+1}) \le V_{\max}(i_{n}) \quad \text{for every consecutive pair}$$

**Every band satisfies it, so a continuous path from hover to cruise exists.**

Corridors of this kind were computed and flown for most of the configurations of the period, and the body of work is large, in [Smith 1958][research_smith_1958], [Smith 1959][research_smith_1959], [NACA 1960][research_naca_1960], [NACA 1960, Conference on V/Stol Aircraft a Co][research_naca_1960_2], [Tapscott 1960][research_tapscott_1960], [Anderson 1960][research_anderson_1960], [Tapscott 1960, Criteria for Control and Response][research_tapscott_1960_2], [Kirby 1961][research_kirby_1961], [NACA 1961][research_naca_1961], [Garren 1961][research_garren_1961], [Kelley 1962][research_kelley_1962], [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962], [Drinkwater and Rolls 1963][research_drinkwater_rolls_1963], [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963], [Linnell 1963][research_linnell_1963], [Rolls 1965][research_rolls_1965], [Garren et al 1965][research_garren_1965], [Hegarty et al 1965][research_hegarty_1965], [Garren and Kelly 1965][research_garren_kelly_1965], [Hickey et al 1966][research_hickey_1966], [Margason 1966][research_margason_1966], [Division 1966][research_division_1966], [Fry et al 1966][research_fry_1966], [Trenka 1967][research_trenka_1967]. The narrowest point is at 50 degrees of nacelle, 47.4 knots wide. The top speed at zero nacelle at sea level is 325 knots, which is consistent with the 400-knot figure quoted at 20,000 feet rather than in conflict with it.

### A Result That Does Not Support the Sales Argument

Running the same corridor with the radial lift force removed produces something that has to be reported carefully, because it cuts against the argument the article has been building.

| Nacelle angle | Minimum with | Minimum without |
|---|---|---|
| 90 degrees | 3.0 kt | 3.0 kt |
| 70 degrees | 12.4 kt | 59.8 kt |
| 60 degrees | 52.7 kt | 107.2 kt |
| 40 degrees | 83.5 kt | 126.2 kt |
| 20 degrees | 100.1 kt | 133.3 kt |
| 0 degrees | 116.7 kt | 138.0 kt |

**That corridor is also continuous.** Without the radial lift force the aircraft still converts, at higher speeds and through narrower bands, but it converts. The radial lift force is therefore **not** what makes the X-19 possible, which is the stronger claim and the one a reader might have expected this article to reach.

What it does is lower every boundary. Writing the reduction as a difference makes its shape visible.

$$\Delta V(i) = V_{\min}^{\text{without}}(i) - V_{\min}^{\text{with}}(i)$$

That difference is 54.5 knots at 60 degrees of nacelle and 21.3 knots at zero, so the benefit is largest exactly where the disc meets the flow most obliquely, which is what the keystone relation predicts through its $\sin\alpha_d$ factor. That reduction is what the small wing was bought with. The distinction between making a configuration possible and making it cheaper is worth preserving, and the arithmetic supports only the second.

**The conditions the aircraft actually flew sit in the part of the corridor the radial lift force opens.** The flight test summary in the [final report][research_fluk_1967_2] records a stabilised 80 knots at a nacelle angle of 65 degrees on Flight 49, and on Flight 50 a level run at 90 knots with the nacelles at 55 degrees, after which the speed varied between 95 and 105 knots. In the model, trim at both conditions exists with the radial lift force and does not exist without it, because the minimum speeds without it are 59.8 knots at 70 degrees, 107.2 knots at 60 degrees and 121.5 knots at 50 degrees. The model's angles of attack at those two points are compared with the pilot's estimates in the comparison section below. **Within this model, the flight envelope the X-19 explored depended on the effect, even though a conversion flown faster at every nacelle angle could have done without it.**

## Dependent Systems

### The Tandem Wing, Which Costs Attitude

Two wings in line is not merely a way to divide area. The aft wing flies in the downwash of the forward one. The [final report][research_fluk_1967] puts the two quarter-chord points 23 feet 4.1 inches apart, which is 2.39 forward semi-spans, so the far-field value is nearly reached. Write the downwash gradient with respect to aircraft attitude.

$$\frac{d\varepsilon}{d\alpha} = \frac{2 a_{\text{fwd}}}{\pi \text{AR}_{\text{fwd}}} = 0.444$$

The aft wing therefore loses 44 percent of every degree of attitude the aircraft takes. Trim solves in closed form because the downwash is proportional to the same angle that produces it.

$$W = q \alpha \left[ S_f a_f + S_a a_a \left( 1 - \frac{d\varepsilon}{d\alpha} \right) \right]$$

Without the interference the cruise attitude would be 5.07 degrees. With it the attitude is **6.97 degrees**, a penalty of 1.90 degrees, or 37.4 percent more attitude for the same lift. The downwash at the aft wing is 3.10 degrees at that condition.

The consequence shows up in the lift split, where the forward surface works at the full attitude and the aft surface at the attitude less the downwash.

$$L_f = q S_f a_f \alpha = 7{,}270 \ \text{lb}, \qquad L_a = q S_a a_a \left( \alpha - \varepsilon \right) = 6{,}390 \ \text{lb}$$

Comparing the lift share against the area share is what makes the penalty concrete.

$$\frac{L_a}{L_f + L_a} = 46.8\% \quad \text{on} \quad \frac{S_a}{S} = 63.7\% \ \text{of the area}$$

**The larger wing is the less effective one**, which is the price of putting it second. The designers met the same downwash in their control layout. The final report records that the ailerons were first placed on the forward wing and moved to the aft wing once it was realised that a forward aileron's added lift increases the downwash at the aft wing behind it and cancels much of its own rolling moment. Its assessment adds that the tandem layout cost at least 6 percent of hover lift, from a centre of gravity forward of the midpoint between the propeller stations and from the larger download under the rear propellers.

Interference between two lifting surfaces in line is a well-populated subject, though most of it arrives under the word canard rather than tandem, in [Gebhard 1953][research_gebhard_1953], [Kirby 1956][research_kirby_1956], [Driver 1958][research_driver_1958], [Morse and Newhouse 1960][research_morse_newhouse_1960], [McKinney and Newsom 1962][research_mc_kinney_newsom_1962], [Clark et al 1963][research_clark_1963], [Curtiss 1965][research_curtiss_c_1965], [Winston et al 1975][research_winston_1975], [Gloss and Washburn 1979][research_gloss_washburn_1979], [Feistel et al 1981][research_feistel_1981], [Prabhu and Tiwari 1983][research_prabhu_tiwari_1983], [Keith and Selberg 1984][research_keith_selberg_1984], [Phillips 1985][research_phillips_1985], [Batina 1985][research_batina_1985], [Rangwalla and Wilson 1987][research_rangwalla_wilson_1987], [Er-El 1988][research_er_el_1988], [Brown and Timmerman 1991][research_brown_timmerman_1991], [Craig et al 1991][research_craig_1991].

**Three of those are about this exact machine or its close relatives.** Experimental research on four-duct tandem vertical take-off configurations, an investigation of control and stability augmentation for tandem tilting ducted-propeller aircraft, and downwash tests of dual tandem ducted-propeller research aircraft all address a four-propulsor tandem layout. The ducts are the difference, and the longitudinal arrangement is not.

### Pitch Control, Which the Layout Supplies for Nothing

Here the tandem arrangement earns its keep, and the comparison with the previous article is direct.

The [X-18][related_post_a315_hiller_x18] carried a turbojet in its tail for no purpose except pitch control in hover, because a tilt-wing with two propellers on one lateral axis has no way to generate a pitching moment at zero airspeed. The X-19 has four propellers at two longitudinal stations. Differential thrust between the stations is a pitching moment with no additional hardware whatever.

Shifting a fraction $f$ of total thrust from one station to the other raises each station by $fT/2$ and lowers the other by the same, so both arms of length $\ell/2$ contribute.

$$M = 2 \left( \tfrac{1}{2} f T \right) \frac{\ell}{2} = \tfrac{1}{2} f T \ell$$

The station separation is taken as the 23.34 feet between the wing quarter-chord points that the [final report][research_fluk_1967] gives, because its assessment places the tilt centre near the one-third chord of each wing, so the two separations differ by a fraction of a foot. Ten percent differential then gives 18,185 foot-pounds.

The inertia it acts against does not have to be assumed. The final report lists the design hover control moments and the maximum angular accelerations they produce for a 12,300-pound aircraft, which are 27,000 foot-pounds and 0.68 radians per second squared in pitch, 20,000 and 1.75 in roll, and 5,600 and 0.12 in yaw. The quotient of each pair is the inertia the designers used.

$$I = \frac{M_{\max}}{\ddot{\theta}_{\max}} \quad \Longrightarrow \quad I_{yy} = \frac{27{,}000}{0.68} = 39{,}706, \quad I_{xx} = \frac{20{,}000}{1.75} = 11{,}429, \quad I_{zz} = \frac{5{,}600}{0.12} = 46{,}667 \ \text{slug ft}^{2}$$

These refer to the lighter weight, so they slightly understate the inertia at 13,660 pounds. Angular acceleration in pitch is the quotient of moment and inertia.

$$\ddot{\theta} = \frac{M}{I_{yy}} = \frac{18{,}185}{39{,}706} = 0.458 \ \text{rad/s}^{2}$$

At 30 percent it is 1.374 radians per second squared. The design maximum of 27,000 foot-pounds corresponds to a differential fraction of hovering thrust, at the design weight, of

$$f = \frac{2 M_{\max}}{W \ell} = \frac{2 (27{,}000)}{(12{,}300)(23.34)} = 0.188$$

so the specified pitch authority asks for less than a fifth of the thrust to move between stations. **That is ample authority obtained from geometry rather than from an engine.**

Roll uses the same relation with the lateral arm in place of the half-station-separation, so the moment is the differential acting at the mean semi-span of 10.25 feet.

$$M_\phi = f T \, y = (0.10)(15{,}581)(10.25) = 15{,}970 \ \text{ft\,lb}, \qquad \ddot{\phi} = \frac{15{,}970}{11{,}429} = 1.397 \ \text{rad/s}^{2}$$

Roll is better still, because the arm is comparable and the inertia is less than a third of the pitch value. The final report records why the designers wanted it. Jet-lift VTOL experience, and NASA's recommendation from the X-14A, pointed to roll accelerations of 1.5 to 1.8 radians per second squared at low speed, against the 1.14 of the original X-19 specification, so the maximum roll moment was raised to 20,000 foot-pounds. Later flight data showed that full roll control was needed to reach 35 knots of lateral velocity with the roll stability augmentation switched off.

### Yaw Control, Which It Does Not

With all four nacelles vertical, yaw can come from torque reaction and from thrust acting through nacelles that are not quite vertical. The [final report][research_fluk_1967_2] records both. The nacelles were toed in, and the propeller rotation, right-handed for propellers 2 and 4 and left-handed for 1 and 3, was chosen so that torque reaction adds to the yawing moment from thrust, which it credits with a 50 percent increase in hover yaw control power. The torque part can be estimated. Torque per propeller follows from hovering power and the hover rotational speed of 126.08 radians per second.

$$Q_1 = \frac{P_1}{\Omega} = \frac{795 \times 550}{126.08} = 3{,}468 \ \text{ft\,lb}$$

A differential of fraction $f$ between the two pairs of like rotation, two propellers each, leaves

$$Q_{\text{net}} = 4 f Q_1$$

At 20 percent this is 2,774 foot-pounds, which is half of the documented 5,600, and it acts on the largest of the three inertias.

$$\ddot{\psi} = \frac{Q_{\text{net}}}{I_{zz}} = \frac{2{,}774}{46{,}667} = 0.0594 \ \text{rad/s}^{2}$$

**The documented total is itself small.** The design maximum of 0.12 radians per second squared is, by the final report's own account, low. It states that the hover control powers departed deliberately from the military helicopter handling specification MIL-H-8501A, that precise heading changes were difficult because the yaw time constant was about 14 seconds, giving acceleration control rather than rate control, and that the X-19's hover yaw control would be unacceptable in an operational aircraft. It also records that no problem in flight could be attributed to it, while noting that most testing was flown in calm air. The handling-qualities literature of exactly those years is where the criteria live, in [Reeder 1958][research_reeder_1958], [Carlson 1958][research_carlson_1958] and [Slaughter 1958][research_slaughter_1958], with the earlier hovering analyses in [Miller 1948][research_miller_1948] and [Albachten 1956][research_albachten_1956].

The criteria themselves were an active subject rather than a settled one while the X-19 was being built, and the body of work behind them is substantial, in [Carpenter and Paulnock 1949][research_carpenter_paulnock_1949], [Kidd and Bull 1963][research_kidd_bull_1963], [Ashkenas 1965][research_ashkenas_1965], [Ashkenas 1965, A Study of Conventional Airplane H][research_ashkenas_1965_2], [Hoffman 1969][research_hoffman_1969], [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_2], [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_3], [Air Force Test Pilot School Edwards Afb Ca 1969][research_ca_1969], [McCormick 1969][research_mccormick_1969], [Hoffman et al 1970][research_hoffman_1970], [Aiken et al 1977][research_aiken_1977], [Corliss et al 1977][research_corliss_1977], [Smith 1977][research_smith_1977], [Gerken 1979][research_gerken_1979], [Goldstein 1982][research_goldstein_1982], [NACA 1982][research_naca_1982], [Corless and Blanken 1983][research_corless_blanken_1983].

**Differential tilt was proposed and never fitted.** Among the remedies the final report lists, differential fore and aft tilting of the left and right propellers is the one it calls feasible and the only one that would meet the yaw requirement of the Advisory Group for Aeronautical Research and Development's report 408, and it records that none of the remedies had been made when the project ended. The report's assessment attributes most of the aircraft's lateral-directional stability and control deficiencies in forward flight to a different cause, the large dihedral effect of a tall vertical tail whose short moment arm forced its size.

### The Cross-Shaft, and What It Cost

The [X-18][related_post_a315_hiller_x18] had two engines that were not interconnected, and losing one meant losing the aircraft. That is the defect the X-19's designers had in front of them, and they fixed it. The [final report][research_fluk_1967] states that the shafting of the transmission interconnects all four propellers to the two engines and that either engine can supply flight power to all four, so an engine failure is a power reduction rather than an asymmetry.

The magnitude of what the fix prevents is easy to state. Losing both propellers on one side leaves a rolling moment of

$$M_{\text{upset}} = \frac{T}{2} \times 10.25 = 79{,}851 \ \text{ft\,lb}$$

Comparing it against the design maximum roll moment of 20,000 foot-pounds is what makes the case.

$$\frac{M_{\text{upset}}}{M_{\phi,\max}} = \frac{79{,}851}{20{,}000} = 3.99$$

**The upset is four times full roll control.** Without the interconnect it is unrecoverable, so the cross-shaft is not a refinement. Losing a single propeller, which no shaft can prevent, is half of that, $39{,}925$ foot-pounds or twice full roll control, and the final flight described below is that case.

The cost is transmission. With one engine dead the survivor drives the far pair through the shaft, which is half the hovering power, or 1,590 horsepower. Torque depends on where in the drive train the shaft runs.

$$Q = \frac{P}{\Omega}$$

At 6,000 revolutions per minute that is 1,392 foot-pounds, at 3,000 it is 2,783, and at the hover propeller speed of 1,204 it is **6,935 foot-pounds**. Shafts therefore run fast and every propeller needs its own reduction gearing, which is why the drive system is the large item. The transmission literature of the following decade is about weight and life in exactly these components, in [Leishman 1966][research_leishman_1966], [Laskin et al 1968][research_laskin_1968], [Badgley and Laskin 1970][research_badgley_laskin_1970], [Hayden and Keller 1974][research_hayden_keller_1974], [Battles 1975][research_battles_1975], [Townsend et al 1976][research_townsend_1976], [Korzun 1976][research_korzun_1976], [Vaicaitis 1980][research_vaicaitis_1980], [Mancini 1983][research_mancini_1983], [White 1985][research_white_1985], [Coy et al 1988][research_coy_1988], [Mitchell 1991][research_mitchell_1991], [Savage and Lewicki 1991][research_savage_lewicki_1991], [Krantz 1994][research_krantz_1994], [Henry 1995][research_henry_1995], [Dempsey et al 2013][research_dempsey_2013].

**The shape of that literature is itself an argument.** It is dominated by helicopter transmissions, by failure analysis, by split-torque arrangements and by overhaul economics, which is what a field looks like once it has accepted that the drive system is the hard part. The final report's assessment says the same of the X-19 at first hand. The transmission was first designed for a 10,000-pound aircraft, the torque requirement grew with the weight and the control inertias, and the designers had to uprate it inside the original envelope. That forced a finite-life design built on a hover time-torque histogram, with the governor limiting any throttle input to 20 percent, where helicopter practice designs for full throttle torque at infinite life. The report calls the philosophy the subject of many heated discussions, and records that experience demonstrated in a dramatic fashion that the minimum requirement is to design for the maximum torque the throttle can impose, because full throttle is an instinctive pilot reaction.

**The drive system was the programme's most argued-over component, but the record does not make it the cause of the loss.** The part that failed on the last flight was the housing that carried a propeller on its nacelle gearbox, and the loads that broke it were generated by the propeller.

### The Propellers Themselves

Disc loading is where the tilt-propeller beats the tilt-wing outright.

$$\frac{W}{A} = \frac{13{,}660}{530.93} = 25.7 \ \text{lb/ft}^2$$

against 82.1 for the X-18. The figure was chosen rather than inherited. The [final report][research_fluk_1967] explains that a thrust-to-power ratio near 6.0 pounds per horsepower with a figure of merit of 0.80 gives a disc loading of 25 pounds per square foot, that this set the X-100's ten-foot propellers, and that the X-19 kept the loading, which fixed its diameter at 13 feet. Four thirteen-foot propellers present a great deal more disc than two sixteen-foot ones, and the penalty for disc loading is explicit once the induced velocity is substituted into the ideal power.

$$\frac{P_{\text{ideal}}}{W} = v_i = \sqrt{\frac{1}{2\rho} \cdot \frac{W}{A}}$$

**Induced power per pound scales with the square root of disc loading**, so the X-19 pays $\sqrt{25.7/82.1} = 0.56$ of what the X-18 pays for every pound it holds up. Power loading follows.

$$\frac{W}{P_{\text{req}}} = \frac{13{,}660}{3{,}180} = 4.30 \ \text{lb/hp}$$

Pitch control of the blades is the mechanism every axis depends on, and the final report records redundant dual-piston pitch-change actuators for that reason. Static thrust estimation is treated in [Coward 1955][research_coward_1955] and [Brusse and Cronk 1965][research_brusse_cronk_1965].

## The Flight Test Record

The X-19 first hovered on 20 November 1963, a date [Vertipedia][ref_vertipedia_x19] and the [Smithsonian][ref_si_x100] both give, and it was lost on 25 August 1965. **The [final report][research_fluk_1967_2] gives 50 flights and a total flight time of 3 hours 45 minutes**, all on the first airframe, serial 62-12197, with 84 lift-offs, and it adds 134 hours of ground running and tie-down tests across both airframes. The figure of four hours in the secondary accounts appears to be that total rounded. Flights 1 to 7 were flown under an earlier contract, and the report gives 3 hours 44 minutes for Flights 8 to 50 in one place and 3 hours 38 minutes in another, so its own accounting of the contract time is not internally consistent. The total is used here.

Those two numbers deserve to be set against each other.

$$\frac{225}{50} = 4.5 \ \text{minutes per flight}$$

Over the 644 days between first hover on 20 November 1963 and loss on 25 August 1965 the calendar rate is as thin as the airborne one.

$$\frac{644}{50} = 12.9 \ \text{days per flight}, \qquad \frac{3.75}{644/30.44} = 0.177 \ \text{flight hours per month}$$

A programme averaging under eleven minutes of flight per calendar month is not a flight test programme in any ordinary sense.

**The programme moved in distinct phases, and the final report sets them out.** Flights 8 to 19, 70 minutes and 25 lift-offs, developed the pilot's hovering ability without stability augmentation, including spot turns, translation in every direction and hovering at 5 to 25 feet to find the ground effect. From Flight 20 the stability augmentation was switched on and evaluated. Every flight before Flight 38 was made at the Caldwell-Wright Airport in Caldwell, New Jersey, together with the first 262 ground runs. The programme then moved to the Federal Aviation Agency's National Aviation Facilities Experimental Center at Pomona, New Jersey, for its 10,000-foot runway and adjoining airspace, and a company co-pilot joined the crew. There, Flights 40 to 43 were conversion runs along the runway that advanced the speed from 20 knots at a nacelle angle of 90 degrees to 62 knots at 82 degrees. Flight 44 made short take-offs and landings at 20 to 60 knots. Flights 45 to 49 took off at 60 knots with the nacelles at 77 degrees and tilted further in flight to reach 70 and then 80 knots, with coordinated turns at 60 knots, and Flight 49 held a stabilised 80 knots at a nacelle angle of 65 degrees.

**The X-19 never completed a conversion.** The report's summary states that the conversion envelope had been extended to 100 knots with the nacelles tilted to 45 degrees, and that every flight lay within the Flight Capability Demonstration, whose purpose was sustained hover followed by gradually increasing tilt toward cruise. The aircraft never flew with its nacelles down and its wings carrying it, which the report puts at 160 knots, so it never demonstrated the regime the whole configuration existed to provide. Every number about cruise in the sizing section above describes a regime the aircraft did not reach.

### The Final Flight

The [final report][research_fluk_1967_2] chronicles Flight 50 at length, quoting the account it supplied to the Air Force accident board. The flight was planned to extend the conversion to 90 and 100 knots on an airfield circuit. After a 60-knot short take-off with the nacelles at 77 degrees, the pilot lowered them to 65 degrees to accelerate to 80 knots and climbed to 1,000 feet. At the top of the climb the nacelles were brought to 55 degrees and the aircraft reached 90 knots, with the pilot estimating an angle of attack of 10 degrees and the stick 85 to 90 percent forward. Uncomfortable with that, he returned the nacelles to 63 degrees, at about 7 degrees angle of attack, and on the downwind leg the aircraft held between 1,000 and 1,300 feet and 95 to 105 knots under good control.

Temperature warning lights ended the flight. Power was reduced at 105 knots and 1,100 feet, and the aircraft descended in a tightening right turn that missed the runway. At about 60 feet and 85 knots, descending at 1,100 to 1,200 feet per minute, the co-pilot applied nearly full power. The aircraft rotated 10 to 15 degrees, climbed at up to 1,400 feet per minute, accelerated to 120 knots, and the propeller speed rose to about 103 percent before the fuel governor held it. The aircraft levelled at 400 feet with the right turn continuing, and three to four seconds after the top of the turn **the No. 2 propeller left the aircraft**. It rolled left and pitched up, the No. 1 propeller followed after about 40 degrees of roll, and the remaining two were torn off by the rate of rotation. At a roll angle of 200 to 210 degrees, at about 400 feet and 120 knots, both pilots ejected almost together. Their parachutes opened at about 250 feet, and they landed with minor injuries, about 500 feet from where the airframe struck a dried reservoir bed inside the airport boundary and burned.

**The failure was structural, and the loads that caused it came from the propeller.** The report's propeller section names the failed part as the propeller housing, a ribbed casting of AZ92A magnesium that carried the propeller on the nacelle gearbox housing. It states that the housing could not carry the vibratory propeller loads at twice the rotational frequency that the flight testing imposed, and that the investigation found three causes acting together. Strain-gauge data from Flights 32 to 50 showed that during conversion flying the vibratory load at twice propeller frequency was as large as the steady once-per-revolution load, considerably higher than the original design criteria anticipated. The emergency manoeuvre just before the failure produced steady loads well above design values. And the actual stress gradient at the rib transition was twice the value in the analysis, with sand pits in the rib tips adding to the stress concentration. The housing was redesigned and static tested before the contract ended.

The secondary accounts call this a gearbox or transmission failure, the [Smithsonian][ref_si_x100] adding pilot error and [Vertipedia][ref_vertipedia_x19] a transmission part. The record is more specific. **The part that broke was the structure joining the propeller to the drive, not a gear, and the load that broke it was the propeller's own response to oblique flow.** The steady once-per-revolution load is the shaft moment that the report derives alongside the normal force, from the same asymmetric blade loading that produces the radial lift force, which is the keystone of this article. The report states that the higher harmonics cannot be calculated with any reliable accuracy by the methods of the day, that flight test was relied on to find them, and that they may become significant in transition and are then controlling loads for the propeller, the nacelle housings and the tilt mechanism. The aircraft was lost in the regime it existed to explore, to a load its designers could not compute.

The flight also tested the emergency logic the cross-shaft section set out. Losing one propeller leaves a rolling moment twice the design maximum roll control, and the record shows the aircraft rolling and pitching at once and shedding the other propellers as the rate built.

A ballistic airframe has a fixed time budget. From the 400 feet of the ejection,

$$t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2(400)}{32.174}} = 4.99 \ \text{s}$$

and a body starting with no vertical velocity takes

$$t_{150} = \sqrt{\frac{2(400 - 250)}{32.174}} = 3.05 \ \text{s}$$

to fall the 150 feet to the height at which the parachutes opened. The report gives no timings, so the interval cannot be checked against it. At a roll angle of 200 to 210 degrees the aircraft was 20 to 30 degrees past inverted, which implies that the seats fired the crew partly toward the ground, and the 150 feet between ejection and canopy is what the seats and the parachutes had to work with.

**The seat is the reason there is anything to reconstruct.** Escape at low altitude from an uncontrolled attitude was the hardest case the ejection-seat literature of the period addressed, and it was addressed at length, in [Watts et al 1947][research_watts_1947], [Hodell and Rosner 1957][research_hodell_rosner_1957], [Latham 1957][research_latham_1957], [Manzuk 1970][research_manzuk_1970], [Gross and Mawhinney 1970][research_gross_mawhinney_1970], [Stech 1977][research_stech_1977], [Budd Co Fort Washington Pa Technical Center 1978][research_center_1978], [Howland 1979][research_howland_1979], [Hawker and Payne 1979][research_hawker_payne_1979], [Lofland 1980][research_lofland_1980], [Chiang 1980][research_chiang_1980], [Pauer 2018][research_pauer_2018].

Two of those are contemporaneous with the design of the seat that saved this crew. Rocket-track ejection testing at Edwards and a study of seat ejection treated as body ballistics both date from 1957, six years before the X-19 first flew. **An inverted ejection at a few hundred feet sits outside the envelope any of that work would have certified**, which is the honest way to state what happened rather than calling it routine.

The programme was cancelled four months later. The report records that the second airframe, serial 62-12198, had been reassigned from structural testing to carry on the flight programme and had completed its transmission runs and preflight tests, but never flew. It survives in storage, recorded by [National Museum of the United States Air Force, Curtiss-Wright X-19][ref_nmusaf_x19] and [Vertipedia, Curtiss-Wright X-19][ref_vertipedia_x19].

## Comparison With Ground Prediction

**There is no flight data from cruise or from completed conversion**, because the aircraft never reached either. There is, however, a small amount of data from the first half of the conversion, and the [final report][research_fluk_1967_2] records it with the company's own predictions beside it. On Flight 50 the pilot estimated an angle of attack of 7 degrees at 80 knots with the nacelles at 65 degrees, and 10 degrees at 90 knots with the nacelles at 55 degrees, and the report states that its calculated steady condition at 55 degrees of tilt was 90 knots at 10 degrees. The trimmed model of the corridor section gives, at the same nacelle angles and speeds and at the 13,660-pound weight,

$$\alpha_{\text{model}}(65^{\circ}, 80 \ \text{kt}) = 4.9^{\circ}, \qquad \alpha_{\text{model}}(55^{\circ}, 90 \ \text{kt}) = 8.0^{\circ}$$

**which is about 2 degrees below both the pilot's estimates and the company's calculation.** The report also gives the design point at which the nacelles lock down, 160 knots at 13.5 degrees angle of attack and 13,660 pounds. With the nacelles at zero the model gives 9.3 degrees with the radial lift force and 13.1 degrees without it, and the wing alone gives

$$\alpha = \frac{W}{q S \bar{a}} = \frac{13{,}660}{(86.67)(154.6)(4.434)} = 0.2299 \ \text{rad} = 13.2^{\circ}$$

so the company's design figure sits closer to the model without the effect than with it. Two explanations are open. The model's recovery fraction may overstate the radial lift force at small shaft angles, or the angles may be measured from different references, since the report gives the forward and aft wing zero-lift lines at 2.3 and 0.9 degrees to the fuselage reference line without a convention this comparison can apply. The record does not separate the two, and the article's cruise and conversion figures carry that uncertainty.

**The company's own theory was validated where the model is weakest.** The final report's radial force section states that its strip theory agreed closely with tests of the X-100 propeller, with the largest difference, 10 to 15 percent above measurement, at a shaft angle of 15 degrees, and that the theory is accurate only to shaft angles of about 30 to 45 degrees, above which the company used test data for performance, loads and stability. The full-scale tunnel measurements of [Yaggy and Rogallo 1960][research_yaggy_rogallo_1960] supply such data to 85 degrees.

What also exists is the [X-100][ref_x100], which transitioned once on 13 April 1960 and which Curtiss-Wright regarded as proof. Its assessment states that the X-100 tests showed the propellers generating large radial force that could replace wing area in transition, on an aircraft whose wing loading made radial lift an important part of the total. It does not establish anything quantitative about the X-19, which was heavier and differently proportioned.

The wind tunnel record for adjacent configurations is comparatively rich. Tilt-wing and four-propeller models appear in [Grunwald 1961][research_grunwald_1961], [Newsom and Tosti 1959][research_newsom_tosti_1959], [Tosti 1962][research_tosti_1962] and [Winston and Huston 1962][research_winston_huston_1962], slipstream effects on performance and stability in [Goland et al 1964][research_goland_1964] and [Butler et al 1966][research_butler_1966], and a tandem-wing configuration in ground effect in [Harry and Trobaugh 1966][research_harry_trobaugh_1966]. **None of it is the X-19**, and the two flight points above are the only measurements that bear on this airframe's aerodynamics in conversion.

## What the Data Changed

Very little, and the reasons are worth separating.

The radial lift force did not enter subsequent practice as a sizing principle. No later production aircraft was given a wing sized on the assumption that its propellers would carry three tenths of the lift slope. The [tiltrotor][ref_tiltrotor] line that eventually reached service in the [V-22][ref_v22] took the opposite approach, using large rotors and a conventional wing.

The tandem-wing arrangement did not propagate either, though it was studied afterward and the canard interference literature of the 1970s, [Gloss and McKinney 1973][research_gloss_mckinney_1973], [Gloss 1974][research_gloss_1974], [Gloss 1975][research_gloss_1975], [Gloss and Washburn 1977][research_gloss_washburn_1977] and [Gloss et al 1978][research_gloss_1978], covers the same physics in a different application.

**What the final report offers as lessons are about loads and drives rather than lift.** Its propeller section concludes that the vibratory harmonics of a propeller in transition dynamically couple it to the airframe and are controlling design loads for the propeller, the nacelle housings and the tilt mechanism, which no method of the day could compute and which only flight measurement could find. Its assessment concludes that a VTOL transmission should be designed for the full torque a throttle can impose and for weight growth, and that the nacelle system should be designed for infinite life at the largest combined control deflection. Each of those is a statement the last flight made at the cost of the airframe. The tri-service programme's other tilt aircraft, the [XC-142][ref_xc142] and the [X-22][ref_x22], also carried interconnected drives.

The most useful thing the X-19 changed may be the sharpest and the least flattering. **A programme that flies under four hours in twenty-one months is not testing an aircraft**, and the tri-service VTOL effort produced several such programmes at once.

## The Contemporary Literature

The X-18 article that precedes this one closed on a configuration that came back because the constraint that killed it dissolved. **This article cannot make that claim and should not try to.**

The X-19's keystone was never wrong. A propeller meeting the flow obliquely develops a force normal to its own axis, it did so in 1963, and it does so now. Nothing dissolved it and nothing needed to. What changed is the thing that actually destroyed the aircraft, and the change there is more radical than anything that happened to the aerodynamics.

The survey below is organised by this article's own analysis, so that each modern field can be set against the quantity it addresses.

### The Keystone Became a Routine Term

**The most telling thing about the modern literature on propeller normal force is how little of it there is.** Fourteen recent papers on the transition trajectory are cited below, and on this subject there are three, in [Kong et al 2020, Finite State Coaxial Rotor Inflow][research_kong_2020_2], [Stokkermans and Veldhuis 2021][research_stokkermans_veldhuis_2021], [Patience and Nahon 2024][research_patience_nahon_2024].

That is not neglect. It is the signature of a solved problem. A simplified model for propeller thrust in oblique flow, and a treatment of propeller performance at large angle of attack for compound helicopters, are the shape the subject now takes, which is a term to be included in a simulation rather than a question to be settled.

**Curtiss-Wright's claim about the steady force was correct and is now uncontroversial.** The company's misfortune was that the same oblique flow also produced unsteady loads that it could not compute and that broke the aircraft.

### The Configuration Is Common Now

The X-19's arrangement, several propellers at more than one longitudinal station with a small wing, is no longer unusual. It is close to a description of much of the current electric vertical take-off field, in [Burton et al 2026][research_burton_2026], [Chaohui et al 2026][research_chaohui_2026], [Choi et al 2026][research_choi_2026], [Critchfield and Ning 2026][research_critchfield_ning_2026], [Hong et al 2026][research_hong_2026], [Hou et al 2026][research_hou_2026], [Jokar and Khoshnood 2026][research_jokar_khoshnood_2026], [Kim et al 2026][research_kim_2026], [Liang et al 2026][research_liang_2026], [May et al 2026][research_may_2026], [Min et al 2026][research_min_2026], [Shubert et al 2026][research_shubert_2026], [Spadão et al 2026][research_spadao_2026], [Wang et al 2026][research_wang_2026], [Xue et al 2026, An efficient transition trajectory][research_xue_2026_2], [Yanev and Staack 2026][research_yanev_staack_2026].

**Tilt-wing, tilt-rotor, lift-plus-cruise and compound layouts are all represented**, and several address the exact problems this article computes by hand, including rotor sizing for tilt-wing vehicles, the aerodynamics of a compound tilt-wing during tilt transition, and the effect of a failure during a backward transition.

### The Corridor Is an Optimisation Problem

This article computes a corridor at ten nacelle angles and reads its continuity off a table. The modern treatment optimises a trajectory through it under constraints, in [Shimizu and Miwa 2019][research_shimizu_miwa_2019], [Wang et al 2019, Research on Dynamic Modeling and T][research_wang_2019_2], [Sakai and Abiko 2020][research_sakai_abiko_2020], [Chen 2023, Controller design for transition f][research_chen_2023_4], [Gupta et al 2023, Optimal Transition Trajectory of a][research_gupta_2023_2], [Kulhánek et al 2023][research_kulhanek_2023], [Hsu et al 2024][research_hsu_2024], [Li et al 2024, Short Takeoff and Vertical Landing][research_li_2024_6], [Zanotti et al 2024, Aerodynamic interaction between ta][research_zanotti_2024_2], [Xiang et al 2025][research_xiang_2025], [Yang et al 2025][research_yang_2025], [Zhu et al 2025][research_zhu_2025], [Lee et al 2026][research_lee_2026], [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026].

**The shape of the answer is unchanged and the method is unrecognisable.** A conversion schedule is now the output of a constrained optimisation rather than a line on a pilot's card, and the constraints include quantities the X-19's designers never had to write down.

### Wing Loading and Disc Loading Are Still the Trade

The X-19 pushed wing loading to 88 pounds per square foot to buy speed and paid for it with a conversion that could not complete below 117 knots. The same trade is made now with different variables, in [Alfares 2026][research_alfares_2026], [Bosch et al 2026][research_bosch_2026], [Gholamian and Beik 2026][research_gholamian_beik_2026], [Golombek et al 2026][research_golombek_2026], [Hu et al 2026][research_hu_2026], [Jiang et al 2026][research_jiang_2026], [Jiao and Yang 2026][research_jiao_yang_2026], [Lee and Kim 2026][research_lee_kim_2026], [Li et al 2026][research_li_2026], [Makeev 2026, Blade Twist and Disc Loading Effec][research_makeev_2026_2], [Pan et al 2026][research_pan_2026], [Park and Park 2026][research_park_park_2026], [Qiao and Zhou 2026][research_qiao_zhou_2026], [Cui et al 2027][research_cui_2027].

**What has changed is which quantity binds.** The X-19 was limited by installed power and by the conversion speed its wing permitted. A battery-powered vehicle is limited by stored energy, which inverts the sizing problem, and the disc loading that once determined hover power now determines how long the vehicle can hover at all.

### Blades, Solidity and the Advance Ratio

The wide blade the X-19 carried for radial force, on a propeller that had to change speed between hover and cruise, is a design problem the field still has, in [Bacchini et al 2021][research_bacchini_2021], [Baek et al 2021][research_baek_2021], [Fan et al 2021][research_fan_2021], [Kovačević et al 2021][research_kovacevic_2021], [Maung et al 2021][research_maung_2021], [Wang et al 2022, Control of centrally-powered varia][research_wang_2022_2], [Jardin et al 2023][research_jardin_2023], [Nozaki et al 2023][research_nozaki_2023], [Sinha 2025][research_b_tech_1st_year_2025], [Goyal et al 2025, Estimation of Rotor Blade Loading][research_goyal_2025_2], [Li and Li 2025][research_li_li_2025], [Liu et al 2025][research_liu_2025], [Shao et al 2025][research_shao_2025], [Yu et al 2026][research_yu_2026].

**The X-19's particular version of it has eased.** Each of its propellers had to hover a quarter of the aircraft at 1,204 revolutions per minute and cruise toward 400 knots at 957, a speed ratio of $1{,}204/957 = 1.26$. Distributing lift across more, smaller rotors relaxes both ends of that requirement, and a vehicle that does not attempt 400 knots relaxes the tip-speed cap that the cruise imposed.

### The Drive Was Deleted and the Propeller Loads Were Not

**This is the section that matters, and it is where the X-19 differs from every other aircraft in this series so far.**

The X-19's drive existed because two engines had to drive four propellers, which requires an interconnected transmission with cross-shafts and gearing at every nacelle. This article computes the torque that shaft carries and observes that the interconnection was not optional, since losing one side is four times full roll control, and the final report records that the transmission was the most argued-over component of the design.

**Electric propulsion does not improve that transmission. It removes it.** Each rotor takes its own motor, there is no cross-shaft, there is no combining gearbox, and there is no propeller reduction box to fail. The literature reflects the change, in [Bai and Zhou 2024][research_bai_zhou_2024], [Lee et al 2024][research_lee_2024], [Lee and Yee 2024, Novel Electric Propulsion System A][research_lee_yee_2024_2], [Li et al 2024, Research on Cogging Torque Reducti][research_li_2024_5], [Chen et al 2025][research_chen_2025], [Machado et al 2025][research_machado_2025], [Nguyen et al 2025, Comprehensive Modeling of Electric][research_nguyen_2025_2], [Ni and Lee 2025][research_ni_lee_2025], [Shang et al 2025][research_shang_2025], [Yu et al 2025][research_yu_2025], [Böhnisch et al 2026][research_bohnisch_2026], [Granata et al 2026][research_granata_2026], [Koshel et al 2026][research_koshel_2026].

**That removes the component the X-19's designers argued over most, but not the one that failed.** The housing that broke carried a propeller, and it broke under the vibratory loads of that propeller in oblique flow. A tilting propeller on an electric aircraft still meets oblique flow in conversion, and the steady and vibratory hub loads that come with it still have to reach the airframe through a nacelle structure, which is a statement of the physics rather than a finding of the papers above. That is a different outcome from the one the X-18 article described. The X-18's keystone was dissolved by a technology that made its central quantity irrelevant. The X-19's keystone survives untouched, its drive was designed out, and the loads that destroyed it are now computed rather than discovered in flight.

### Redundancy Replaced Mechanical Interconnection

Removing the cross-shaft removes what the cross-shaft was for. The X-19 needed mechanical interconnection because an engine failure would otherwise be an unrecoverable rolling moment. With enough independent motors the same failure is a control-allocation problem, in [Antonakis and Biannic 2024][research_antonakis_biannic_2024], [Du et al 2024][research_du_2024], [Kang et al 2024][research_kang_2024], [Mabboux et al 2024][research_mabboux_2024], [Zhao et al 2024, Active Fault-Tolerant Strategy for][research_zhao_2024_3], [Atmaca et al 2025][research_atmaca_2025], [Hung and Dai 2025][research_hung_dai_2025], [Jing and Ma 2025][research_jing_ma_2025], [Ruggia 2025][research_ruggia_2025], [Choi and Suk 2026][research_choi_suk_2026], [Han and Pei 2026][research_han_pei_2026], [Strampe and Klingauf 2026][research_strampe_klingauf_2026].

**The engine-out case stopped being a mechanical problem and became a software one**, which is a change in the kind of engineering required rather than in its difficulty. The one engine inoperative case is still studied, still hard, and no longer solved with a shaft.

### Handling Qualities Became Criteria

The hover yaw authority that the final report itself calls unacceptable for an operational aircraft would today be measured against a published criterion rather than against judgement, in [Biernacki and Lewkowicz 2024][research_biernacki_lewkowicz_2024], [Deng et al 2024][research_deng_2024], [Ducard and Carughi 2024][research_ducard_carughi_2024], [He et al 2024][research_he_2024], [Antonakis 2025][research_antonakis_2025], [Saetti 2025][research_saetti_2025], [Yan et al 2025][research_yan_2025], [Yang 2025, Aircraft Pilot Workload Assessment][research_yang_2025_2], [Yang et al 2025, Fully autonomous anti-interference][research_yang_2025_3], [Cavalcanti et al 2026][research_cavalcanti_2026], [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026], [Janetzko et al 2026][research_janetzko_2026], [Kang et al 2026][research_kang_2026], [Yi 2026][research_yi_2026].

**Simplified vehicle operations, meaning an aircraft a non-professional can fly, is now a design objective**, which would have been an extraordinary claim while the X-19 was being flown four or five minutes at a time by test pilots.

### Certification Is Where the Constraint Now Lives

This is the largest single difference between the X-19's world and the present. A 1963 research aircraft needed to fly. A modern powered-lift aircraft needs to fly, to be certified against a category that had to be invented for it, and to operate in shared airspace, in [Dudziak et al 2020][research_dudziak_2020], [Feng 2022][research_feng_2022], [Schweiger and Preis 2022][research_schweiger_preis_2022], [Takacs and Haidegger 2022][research_takacs_haidegger_2022], [Zhou 2022][research_zhou_2022], [Kim et al 2023][research_kim_2023], [Park et al 2023][research_park_2023], [Dong et al 2024][research_dong_2024], [Zhang and Zhou 2024][research_zhang_zhou_2024], [Chen et al 2025, Model-free adaptive flow control o][research_chen_2025_2], [Farooqui 2025][research_farooqui_2025], [Lee and Ko 2025][research_lee_ko_2025], [Laplante et al 2026][research_laplante_2026], [Park 2026][research_park_2026].

**The X-19 was destroyed by a propeller housing and cancelled four months later.** Its descendants are more often delayed by a means-of-compliance document, and an article treating only the aerodynamics would miss where the difficulty now lies.

### Noise, Which the X-19 Never Had to Face

A 1963 military transport testbed had no acoustic constraint whatever. A vehicle intended to operate from a city rooftop has one that may bind before any aerodynamic limit does, in [Araghizadeh et al 2025][research_araghizadeh_2025], [W. Bauer 2025][research_bauer_2025], [Bergmann et al 2025][research_bergmann_2025], [Boucher 2025][research_boucher_2025], [Czech et al 2026][research_czech_2026], [Gandhi et al 2026][research_gandhi_2026], [Georgiou et al 2026][research_georgiou_2026], [Hummel et al 2026][research_hummel_2026], [Marques et al 2026][research_marques_2026], [Page et al 2026][research_page_2026], [Pascioni et al 2026][research_pascioni_2026], [Rizzi et al 2026][research_rizzi_2026], [Tinney and Valdez 2026][research_tinney_valdez_2026], [Voropayev et al 2026][research_voropayev_2026].

**This is a genuinely new constraint rather than an old one made stricter**, and it interacts directly with the quantity this article derives. Tip speed was capped here by cruise Mach number in cruise and raised for hover. It is capped now by community noise, which bears hardest on hover, the condition in which the X-19 ran its propellers fastest.

### Ground Effect, Download and the Vertiport

The download this article computes at 14.1 percent of gross weight is a wing-area penalty, and the outwash it implies is now an infrastructure question, in [García Crespillo et al 2024][research_crespillo_2025], [Guo et al 2025][research_guo_2025], [Guo et al 2025, Research of Hierarchical Vertiport][research_guo_2025_2], [Jung et al 2025][research_jung_2025], [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_3], [Zhang and Hwang 2025][research_zhang_hwang_2025], [Zhao et al 2025, UAV Operations and Vertiport Capac][research_zhao_2025_3], [Li et al 2026, Urban air mobility vertiports][research_li_2026_2], [Lyu and Feng 2026][research_lyu_feng_2026], [Mirković et al 2026][research_mirkovic_2026], [Nagrare and Lieb 2026][research_nagrare_lieb_2026], [Park and Kim 2026][research_park_kim_2026].

**A vehicle at 26 pounds per square foot of disc loading needs a prepared surface**, and the modern field calls that a vertiport and regulates it, which is the same requirement with a name and a standard attached.

### Methods, Autonomy and What Replaced the Wind Tunnel

The interference this article estimates with a downwash gradient and a contraction factor is now simulated directly, in [H. Dabaghian et al 2025][research_dabaghian_2025], [Hakim et al 2025][research_hakim_2025], [Liu et al 2025, Supersonic aircraft aerodynamic pe][research_liu_2025_3], [Lopez and Biancolini 2025][research_lopez_biancolini_2025], [Sadiq Ali Mir et al 2025][research_mir_2025], [Sastre et al 2025][research_sastre_2025], [Wang et al 2025][research_wang_2025], [Yan and Shi 2025][research_yan_shi_2025], [Cai et al 2026][research_cai_2026], [Claro et al 2026][research_claro_2026], [Qin 2026][research_qin_2026], [Shen et al 2026, A multi-fidelity workflow for conc][research_shen_2026_2], [Suo et al 2026][research_suo_2026], [Zhang et al 2026, Optimization of rotor aerodynamic][research_zhang_2026_3].

**The 0.444 downwash gradient that costs this aircraft 1.90 degrees of attitude is not a quantity a modern analysis would need to approximate.** It would be resolved, and so would the propeller-wing interference that sits behind the keystone.

### What the Survey Shows

Three things, and the third is the one worth keeping.

**The aerodynamics were right.** The radial lift force is real, is still used, and is no longer argued about.

**The configuration was reasonable.** Multiple propellers at two longitudinal stations with a small wing describes a large fraction of the current field.

**The loads were the problem, and they are now a computed quantity.** The X-19 was lost to a vibratory propeller load in conversion that its designers could not calculate and found only in flight, while its transmission, the part everyone argued about, is not what failed. Electric motors abolished the transmission, and modern methods resolve the interference flow from which such loads arise. **An aircraft can be correct in the argument it makes about the steady force and still be destroyed by the unsteady one.**

## Where the Framing Breaks Down

**Treating the X-19 through the radial lift force can overstate what the radial lift force decided.** The corridor computed above is continuous with the effect switched off. The keystone framing is correct about what the aircraft was sold on, about what its wing area required and, within the model, about the speeds it actually flew at its nacelle angles, and it is wrong if it suggests the configuration depended on the effect for feasibility.

**The keystone framing also underweights what killed the aircraft.** The steady radial lift force did not break anything. Its vibratory companion at twice propeller frequency did, and a momentum analysis of the steady force has nothing to say about that load. An article built around an aerodynamic keystone will underweight the structural dynamics that determined the outcome, and this one would too if the point were not made explicitly.

**The comparison with the X-18 can be pushed too far.** The two aircraft look adjacent and are adjacent in the designation sequence, but their governing quantities have nothing in common. Immersed fraction is meaningless for the X-19 and propeller normal force is nearly meaningless for the X-18, whose propellers stay roughly aligned with the flow because the whole wing rotates with them.

**This article's own model has a limit.** The in-plane momentum picture treats the disc as an actuator turning a stream tube, which is defensible while the disc is moderately inclined and indefensible once it is close to broadside, where a propeller is a bluff body shedding a wake and no linear proportionality to $\sin\alpha_d$ has any basis. The condition to test is the disc incidence, which is the nacelle angle plus the angle of attack.

$$\alpha_d = i + \alpha \le 60^{\circ}$$

**Five of the ten corridor rows above violate it**, reaching 89.5 degrees at the hover end, so the low-speed half of the corridor should be read as indicative rather than quantitative. The [final report][research_fluk_1967] draws the line lower for its own strip theory, at shaft angles of about 30 to 45 degrees, and against 45 degrees seven of the ten rows fail. The full-scale measurements of [Yaggy and Rogallo 1960][research_yaggy_rogallo_1960], which found normal force nearly linear in shaft angle over large ranges, are the evidence that the linear form does not fail abruptly at either limit. This is the same discipline the X-15 article applied when it found its own perfect-gas arithmetic valid to Mach 7.06 against an aircraft that flew at 6.70.

## The Source Base

The vehicle's own literature is small, and outside one document it is encyclopaedic. The keystone's literature is the opposite, being deep, primary, and two decades older than the aircraft.

That inversion is the defining feature here. [Ribner 1943][research_ribner_1943], [Ribner 1943, Formulas for propellers in yaw and][research_ribner_1943_2], [Ribner 1943, Proposal for a propeller side-forc][research_ribner_1943_3], [Ribner 1945][research_ribner_1945] and [Ribner 1945, Propellers in yaw][research_ribner_1945_2] are wartime and immediately post-war work on a stability nuisance, and they are the strongest citations in this article. The X-19 exists because someone read that literature and asked whether the nuisance could be a feature.

The tilt-wing and convertiplane design literature of the late 1950s is well populated, in [McCormick and Mallen 1956][research_mccormick_mallen_1956], [McCormick and Mallen 1957][research_mccormick_mallen_1957], [Stepniewski 1957][research_stepniewski_1957], [Mallen and Dancik 1959][research_mallen_dancik_1959], [Dallas and Irvin 1956][research_dallas_irvin_1956] and [McCormick 1956][research_mccormick_w_1956], with the aeroelastic problems in [Loewy and Yntema 1958][research_loewy_yntema_1958].

**The vehicle's primary record is the final report, AFFDL-TR-66-195**, [Fluk et al 1967, Volume I][research_fluk_1967] and [Fluk et al 1967, Volume II][research_fluk_1967_2], which Curtiss-Wright wrote for the Air Force after the flight test contract ended as a critical review of the whole technology. It covers the history from the X-100, the radial force theory and its correlation with test, the propellers, the control system, the tandem wing, ground effect, the wind tunnel programme, structural loads, power-off flight, the flight test summary with the account of the last flight, and the company's own assessment. It is a contractor's report, and its notice page states that publication does not constitute Air Force approval of its findings. The documents it cites for the flights themselves, Curtiss-Wright X-19 Flight Test Reports Nos. 8 to 50 and the accident submissions, are not available in the public archives, so the flight-by-flight record rests on the report's summary of them. [Yaggy and Rogallo 1960][research_yaggy_rogallo_1960] is the independent NASA measurement of the keystone force on a full-scale Curtiss-Wright propeller.

### The Shape of the Reference Base

**The research survey admits a record only when a person reading its title finds it on this article's subject.** Its 398 records come from NASA's Technical Reports Server, the Defense Technical Information Center and the journal literature indexed by Crossref. Of these, 48.0 percent are report-server records, and their median year is 1984.

**Naval architecture is the principal homonym of this subject.** A propeller in oblique inflow is a live research subject there, where it means a ship screw meeting the wake of a hull at an angle, and that literature uses the same words as this article. Its records are excluded, and some of them cannot be recognised from the words of the title alone. A paper on the normal force of a rudder behind a controllable-pitch propeller, a David Taylor Model Basin method for calculating the spindle torque of a controllable-pitch propeller, and a report on the four-quadrant characteristics of propeller 4739, designed for the dock landing ship LSD-41, are all ship work, and report-server records carry no journal name that would reveal the venue. The phrase controllable pitch also resembles the vocabulary of controllability and handling qualities. Redundancy also names a topic in biomechanics, and a motor fault also arises in road vehicles, so records that share only those words are excluded. Correction, erratum, retraction and withdrawal notices, figure, table and supplementary-material records, peer-review reports and journal front matter are excluded as well, because a survey counts research works and those are parts of works or editorial events rather than works.

**Some records of doubtful relevance are kept.** Papers on permanent-magnet machines, a counter-rotating compressor, turbine vane cooling with one engine inoperative and rotating detonation engines are cited in the modern survey for the motors, blades, engine-out case and design methods of present vertical flight. Each shares machinery or method with that field rather than its aerodynamics, so each is kept and a reader may weigh it accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.**

**The keystone's modern literature is small, and that is a result rather than a gap.** A quantity that is settled stops generating publications, so the thinness is evidence that Curtiss-Wright's aerodynamic claim is no longer contested.

**One topic is genuinely thin.** Aircraft moments of inertia and radii of gyration are scarcely represented in the archives, because mass-properties reports are working documents that archives rarely index. The three inertias in this article are therefore not quoted from a mass-properties source. They are the quotients of the design control moments and angular accelerations that the final report gives, which is the inertia the designers worked with at 12,300 pounds.

## Epistemic State

**Historical fact, from the primary record.** The X-19 made 50 flights totalling 3 hours 45 minutes, with 84 lift-offs, all on serial 62-12197. Flights before Flight 38 were made at Caldwell, New Jersey, and the rest at the National Aviation Facilities Experimental Center at Pomona, New Jersey, where the aircraft was lost on Flight 50. The conversion envelope reached 100 knots with the nacelles at 45 degrees, and the aircraft never flew with its nacelles fully down. Flight 50 ended when the cast magnesium housing carrying the No. 2 propeller failed under vibratory loads at twice propeller frequency, an emergency manoeuvre and a stress concentration the analysis had underestimated. Both crew ejected at about 400 feet and 120 knots and survived. The second airframe never flew. The aircraft began as Curtiss-Wright's Model 200 executive transport, was redesigned around two T55-L-5 engines after a management change, and was funded under a tri-service agreement. The X-100 preceded it and made a single transition on 13 April 1960.

**Historical fact, from secondary sources only.** The first hover on 20 November 1963 and the cancellation four months after the loss come from the museum and Vertipedia accounts. The X-100's construction and hover dates come from the Smithsonian.

**Published figures taken as given.** From the final report, gross weight 13,660 pounds, wing areas 56.1 and 98.5 square feet, spans to the nacelle centrelines of 19.5 and 21.5 feet, chords of 34.5 and 55.0 inches, a quarter-chord separation of 23 feet 4.1 inches, four three-blade propellers of 13 feet with 8.4 square feet of blade area per blade and an activity factor of 168, propeller speeds of 1,204 revolutions per minute in hover and 957 in cruise, cruise at 325 knots at 15,000 feet, and the design hover control moments and accelerations. From the Jane's-derived specification, two engines of 2,650 shaft horsepower and a maximum speed of 400 knots at 20,000 feet. That specification names the T55-L-7 while the final report names the T55-L-5 and gives no rating, so the installed power rests on a source whose engine designation the primary record contradicts.

**Engineering analysis.** Wing loading of 88.4 pounds per square foot, stall at 136.5 knots, download of 14.1 percent, hover induced velocity of 78.6 feet per second, permitted cruise tip speed of 644.2 feet per second, blade loading of 0.097 in hover, in-plane recovery fraction of 0.263, cruise lift share of 29.0 percent, equivalent plain wing of 215 to 216 square feet, the corridor table, the model's angles of attack at the documented flight points, tandem attitude penalty of 1.90 degrees, control accelerations, cross-shaft torques, and the free-fall budget are all computed here from the documented geometry and are not quoted from any source. The derived cruise propeller speed of 946 revolutions per minute agrees with the record's 957 to 1.1 percent.

**Assumed quantities, each of which moves the answers.** Maximum lift coefficient of 1.4, helical tip Mach limit of 0.90, blade loading limit of 0.14 used only as a reference, hover figure of merit of 0.70, download drag coefficient of 1.20 with slipstream factor 1.5, propeller efficiency of 0.80 at maximum speed, span efficiencies, an effective tandem aspect ratio of 6.0, and the use of the quarter-chord separation for the propeller station separation. The inertias are those implied by the design control powers at 12,300 pounds and are applied at 13,660. That the 8.4 square feet of blade area is per blade is an inference from the activity factor.

**One modelling inconsistency is carried openly.** The momentum model treats the hover figure of merit and the propeller efficiency at maximum speed as a single quantity, yet the calculation assumes 0.70 for the one and 0.80 for the other. Evaluated across both values, the corridor's low-speed boundaries are identical while its high-speed boundaries move by about 5 percent. The figure of merit implied by the qualification schedule's hover power is 0.647, below both.

**The corridor needs both equilibrium equations.** Solving the vertical balance for thrust and then testing that same balance is satisfied identically at any speed, and it would place the lower boundary near zero at every nacelle angle. Eliminating thrust between the vertical and horizontal balances is what gives the corridor its lower boundaries.

**The model disagrees with the record by about 2 degrees.** At the two documented conversion points the model's angle of attack is about 2 degrees below the pilot's estimates and the company's calculation, and at the 160-knot design point it is 4.2 degrees below the company's figure. Whether the model overstates the radial lift force or the angles are referred to different datums is not settled by the record.

**Inference, not established.** That the conditions actually flown depended on the radial lift force holds within this model only. That the seats fired the crew partly toward the ground is inferred from the recorded roll angle.

**Unresolved conflict in the record.** The final report gives the contract flight time as 3 hours 44 minutes in one place and 3 hours 38 minutes in another. Its company account of the crash places the impact in a swamp and its theodolite analysis in a dried reservoir bed. The X-100's flight time is 10 hours in the final report and fourteen in the Smithsonian's account. The final report states the speed objective as 400 miles an hour and as Mach 0.65, which cannot both hold.

**Written from present knowledge.** The contemporary material postdates the editorial date of this article.

## Out of Scope

Blade element analysis of the propellers, including the twist distribution and the compressibility behaviour of a wide chord at the tip. Structural design of the wings and the nacelle pivots. Aeroelastic behaviour of a heavy nacelle on a short wing, which [Loewy and Yntema 1958][research_loewy_yntema_1958] indicates is not trivial. Gear tooth stress and lubrication, and the fatigue analysis of the propeller housing, which the final report treats only in summary. Acoustic behaviour, which the M-200 design meant to keep low with lightly loaded propellers at low tip speed. The autorotation and engine-out descent case. Ground effect and recirculation during vertical landing, which [Huston and Winston 1960][research_huston_winston_1960], [O'Bryan 1961][research_o_bryan_1961], [Pruyn and Taylor 1970][research_pruyn_taylor_1970] and [Renselaer 1975][research_renselaer_1975] address for adjacent configurations. Cockpit workload and the pilot's task during a conversion that was never completed.

## Conclusion

The X-19 asked whether a propeller could be counted on for lift, and the answer this article computes is that it can, to the tune of about thirty percent of the lift slope in cruise, which is enough to build a wing loading of 88 pounds per square foot on where 63 would otherwise be needed. Curtiss-Wright's own design figure was at least 20 percent of the cruise lift.

**That answer was never confirmed in cruise by the aircraft that asked the question.** Fifty flights and 3 hours 45 minutes took the conversion to 100 knots with the nacelles at 45 degrees and no further, and the airframe was destroyed before the nacelles were ever fully down. The two conversion points the final report documents fall inside the model's corridor only when the radial lift force is counted, and the model's angles of attack there run about 2 degrees below what the pilot and the company estimated. The confirmation of a complete conversion belongs to the X-100, a smaller and lighter demonstrator that transitioned once in 1960.

Three conclusions survive the analysis and two do not. The wide propeller blade was bought for radial force, as the final report states, and hovering at a higher propeller speed than it cruised at kept that blade lightly loaded. The tandem layout supplied for nothing the pitch control that the [X-18][related_post_a315_hiller_x18] required a turbojet to obtain, and supplied a hover yaw control that its own designers judged unacceptable for an operational aircraft. The interconnected drive cured the X-18's fatal engine-out asymmetry, at the cost of a transmission that had to be uprated beyond the weight it was drawn for.

The first conclusion that does not survive is the one the marketing rested on. The radial lift force did not make this aircraft possible. The corridor closes without it at higher speeds. What it made possible was a smaller wing and, in the model, the slower conversion speeds the aircraft actually flew. The second is the familiar account of the loss. **The X-19 was not destroyed by its gearbox.** The final report names a cast magnesium propeller housing that failed under vibratory loads at twice propeller frequency, loads that arose in conversion, that were as large as the steady load beside them, and that no method of the period could calculate.

The contemporary literature adds a final observation that changes the verdict on the programme rather than on the physics. **Every argument Curtiss-Wright made about the steady force has held.** The radial lift force is real and is now a routine term. The configuration of several propellers at two longitudinal stations with a small wing describes a large part of the current electric vertical take-off field, and electric motors have abolished the transmission that the company argued over most. What destroyed the aircraft was the unsteady side of the same oblique flow that produces the radial lift force, which is now a quantity to be computed rather than discovered in flight.

**An aircraft can be correct in the argument it makes about the steady force and still be destroyed by the unsteady one.**

## References

### Books

- [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003]
- [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]

[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_miller_2001]: https://openlibrary.org/works/OL7006680W

### Reference

- [Curtiss-Wright][ref_curtiss_wright]
- [Curtiss-Wright X-100][ref_x100]
- [Curtiss-Wright X-19][ref_x19]
- [National Museum of the United States Air Force, Curtiss-Wright X-19][ref_nmusaf_x19]
- [Smithsonian National Air and Space Museum, Curtiss-Wright X-100][ref_si_x100]
- [tiltrotor][ref_tiltrotor]
- [V-22][ref_v22]
- [Vertipedia, Curtiss-Wright X-100][ref_vertipedia_x100]
- [Vertipedia, Curtiss-Wright X-19][ref_vertipedia_x19]
- [X-22][ref_x22]
- [XC-142][ref_xc142]

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

### Related Post

- [X-1][related_post_a298_bell_x1]
- [X-10][related_post_a307_north_american_x10]
- [X-11][related_post_a308_convair_x11]
- [X-12][related_post_a309_convair_x12]
- [X-13][related_post_a310_ryan_x13]
- [X-14][related_post_a311_bell_x14]
- [X-15][related_post_a312_north_american_x15]
- [X-16][related_post_a313_bell_x16]
- [X-17][related_post_a314_lockheed_x17]
- [X-18][related_post_a315_hiller_x18]
- [X-2][related_post_a299_bell_x2]
- [X-3][related_post_a300_douglas_x3]
- [X-4][related_post_a301_northrop_x4]
- [X-5][related_post_a302_bell_x5]
- [X-6][related_post_a303_convair_x6]
- [X-7][related_post_a304_lockheed_x7]
- [X-8][related_post_a305_aerojet_x8]
- [X-9][related_post_a306_bell_x9]
- [X-Planes series][related_post_a297_xplanes_framing]

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

### Research

- [Aiken et al 1977][research_aiken_1977]
- [Albachten 1956][research_albachten_1956]
- [Alfares 2026][research_alfares_2026]
- [Anderson 1960][research_anderson_1960]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Applin et al 1994][research_applin_1994]
- [Araghizadeh et al 2025][research_araghizadeh_2025]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashkenas 1965, A Study of Conventional Airplane H][research_ashkenas_1965_2]
- [Atmaca et al 2025][research_atmaca_2025]
- [Sinha 2025][research_b_tech_1st_year_2025]
- [Bacchini et al 2021][research_bacchini_2021]
- [Badgley and Laskin 1970][research_badgley_laskin_1970]
- [Baek et al 2021][research_baek_2021]
- [Bai and Zhou 2024][research_bai_zhou_2024]
- [Bartie et al 1986][research_bartie_1986]
- [Batina 1985][research_batina_1985]
- [Battles 1975][research_battles_1975]
- [W. Bauer 2025][research_bauer_2025]
- [Bellinger 1972][research_bellinger_1972]
- [Bencze et al 1978][research_bencze_1978]
- [Bennett 1984][research_bennett_1984]
- [Beppu et al 1966][research_beppu_1966]
- [Bergmann et al 2025][research_bergmann_2025]
- [Biernacki and Lewkowicz 2024][research_biernacki_lewkowicz_2024]
- [Blaser 1969][research_blaser_1969]
- [Boatwright and Clingan 1969][research_boatwright_clingan_1969]
- [Bober and Mitchell 1980][research_bober_mitchell_1980]
- [Bobo 1972][research_bobo_1972]
- [Borst 1978][research_borst_1978]
- [Bosch et al 2026][research_bosch_2026]
- [Boucher 2025][research_boucher_2025]
- [Bradley 1956][research_bradley_1956]
- [Brenckmann 1958][research_brenckmann_1958]
- [Breul 1963][research_breul_1963]
- [Brewer and May 1948][research_brewer_may_1948]
- [Brown and Timmerman 1991][research_brown_timmerman_1991]
- [Brusse and Cronk 1965][research_brusse_cronk_1965]
- [Burton et al 2026][research_burton_2026]
- [Butler et al 1966][research_butler_1966]
- [Böhnisch et al 2026][research_bohnisch_2026]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_ca_1969]
- [Cai et al 2026][research_cai_2026]
- [Carlson 1958][research_carlson_1958]
- [Carpenter and Paulnock 1949][research_carpenter_paulnock_1949]
- [Castles and Durham 1956][research_castles_durham_1956]
- [Castles and Gray 1951][research_castles_gray_1951]
- [Cavalcanti et al 2026][research_cavalcanti_2026]
- [Cavcar 2011][research_cavcar_2011]
- [Budd Co Fort Washington Pa Technical Center 1978][research_center_1978]
- [Chaohui et al 2026][research_chaohui_2026]
- [Chawla 1952][research_chawla_1952]
- [Chen 2023, Controller design for transition f][research_chen_2023_4]
- [Chen and Schweikhard 1985][research_chen_schweikhard_1985]
- [Chen et al 2025][research_chen_2025]
- [Chen et al 2025, Model-free adaptive flow control o][research_chen_2025_2]
- [Chiang 1980][research_chiang_1980]
- [Chiocchia and Pignataro 1995][research_chiocchia_pignataro_1995]
- [Choi and Suk 2026][research_choi_suk_2026]
- [Choi et al 2026][research_choi_2026]
- [Churchill and Harrington 1959][research_churchill_harrington_1959]
- [Clark et al 1963][research_clark_1963]
- [Claro et al 2026][research_claro_2026]
- [Corless and Blanken 1983][research_corless_blanken_1983]
- [Corliss et al 1977][research_corliss_1977]
- [Coward 1955][research_coward_1955]
- [Coy et al 1988][research_coy_1988]
- [Craig et al 1991][research_craig_1991]
- [García Crespillo et al 2024][research_crespillo_2025]
- [Crigler and Gilman 1949][research_crigler_gilman_1949]
- [Crigler and Gilman 1952][research_crigler_gilman_1952]
- [Crimi 1975][research_crimi_1975]
- [Critchfield and Ning 2026][research_critchfield_ning_2026]
- [Cui et al 2027][research_cui_2027]
- [Curtiss 1965][research_curtiss_c_1965]
- [Curtiss et al 1967][research_curtiss_1967]
- [Curtiss et al 1985][research_curtiss_1985]
- [Czech et al 2026][research_czech_2026]
- [H. Dabaghian et al 2025][research_dabaghian_2025]
- [Dallas and Irvin 1956][research_dallas_irvin_1956]
- [Delano 1947][research_delano_1947]
- [Delany 1942][research_delany_1942]
- [Dempsey et al 2013][research_dempsey_2013]
- [Deng et al 2024][research_deng_2024]
- [Detore and Sambell 1975][research_detore_sambell_1975]
- [Division 1966][research_division_1966]
- [Doetsch and Mark 1953][research_doetsch_mark_1953]
- [Dong et al 2024][research_dong_2024]
- [Donlan 1976, Factors affecting static longitudi][research_donlan_1976_2]
- [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962]
- [Drinkwater and Rolls 1963][research_drinkwater_rolls_1963]
- [Driver 1958][research_driver_1958]
- [Du et al 2024][research_du_2024]
- [Ducard and Carughi 2024][research_ducard_carughi_2024]
- [Dudziak et al 2020][research_dudziak_2020]
- [Dunham and Gentry 1989][research_dunham_gentry_1989]
- [Dunham and Gentry 1989, The Effect of Solidity on Propelle][research_dunham_gentry_1989_2]
- [Er-El 1988][research_er_el_1988]
- [Fan et al 2021][research_fan_2021]
- [Farooqui 2025][research_farooqui_2025]
- [Feistel et al 1981][research_feistel_1981]
- [Feng 2022][research_feng_2022]
- [Fisher and McCroskey 1971][research_fisher_mccroskey_1971]
- [Fluk et al 1967, Volume I][research_fluk_1967]
- [Fluk et al 1967, Volume II][research_fluk_1967_2]
- [Fry et al 1966][research_fry_1966]
- [Gabel and Tarzanin 1972][research_gabel_tarzanin_1972]
- [Gandhi et al 2026][research_gandhi_2026]
- [Garren 1961][research_garren_1961]
- [Garren and Kelly 1965][research_garren_kelly_1965]
- [Garren et al 1965][research_garren_1965]
- [Gazzaniga and Rose 1992][research_gazzaniga_rose_1992]
- [Gebhard 1953][research_gebhard_1953]
- [Gentry et al 1991][research_gentry_1991]
- [Gentry et al 1994][research_gentry_1994]
- [Georgiou et al 2026][research_georgiou_2026]
- [Gerken 1979][research_gerken_1979]
- [Gholamian and Beik 2026][research_gholamian_beik_2026]
- [Gilchrist 1983][research_gilchrist_1983]
- [Gloss 1974][research_gloss_1974]
- [Gloss 1975][research_gloss_1975]
- [Gloss and McKinney 1973][research_gloss_mckinney_1973]
- [Gloss and Washburn 1977][research_gloss_washburn_1977]
- [Gloss and Washburn 1979][research_gloss_washburn_1979]
- [Gloss et al 1978][research_gloss_1978]
- [Goland et al 1964][research_goland_1964]
- [Goldstein 1982][research_goldstein_1982]
- [Golombek et al 2026][research_golombek_2026]
- [Goodrich et al 1989][research_goodrich_1989]
- [Goodson 1961][research_goodson_1961]
- [Goodson 1966][research_goodson_1966]
- [Goodson 1966, Comparison of wind-tunnel and flig][research_goodson_1966_2]
- [Goyal et al 2025, Estimation of Rotor Blade Loading][research_goyal_2025_2]
- [Granata et al 2026][research_granata_2026]
- [Gross and Mawhinney 1970][research_gross_mawhinney_1970]
- [Grunwald 1961][research_grunwald_1961]
- [Guo et al 2025][research_guo_2025]
- [Guo et al 2025, Research of Hierarchical Vertiport][research_guo_2025_2]
- [Gupta et al 2023, Optimal Transition Trajectory of a][research_gupta_2023_2]
- [Gur and Rosen 2005][research_gur_rosen_2005]
- [Hagerman 1947][research_hagerman_1947]
- [Hakim et al 2025][research_hakim_2025]
- [Han and Pei 2026][research_han_pei_2026]
- [Hargraves 1961][research_hargraves_1961]
- [Harris 1996][research_harris_1996]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hawker and Payne 1979][research_hawker_payne_1979]
- [Hayden and Keller 1974][research_hayden_keller_1974]
- [He et al 2024][research_he_2024]
- [Hegarty et al 1965][research_hegarty_1965]
- [Henry 1995][research_henry_1995]
- [Hickey 1956][research_hickey_1956]
- [Hickey et al 1966][research_hickey_1966]
- [Hirsch 1954][research_hirsch_1954]
- [Hodell and Rosner 1957][research_hodell_rosner_1957]
- [Hoffman 1969][research_hoffman_1969]
- [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_2]
- [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_3]
- [Hoffman et al 1970][research_hoffman_1970]
- [Hohenemser and Prelewicz 1974][research_hohenemser_prelewicz_1974]
- [Hong et al 2026][research_hong_2026]
- [Hou et al 2026][research_hou_2026]
- [Howard and Miley 1989][research_howard_miley_1989]
- [Howard et al 1985][research_howard_1985]
- [Howland 1979][research_howland_1979]
- [Hsu et al 2024][research_hsu_2024]
- [Hu et al 2026][research_hu_2026]
- [Hummel et al 2026][research_hummel_2026]
- [Hung and Dai 2025][research_hung_dai_2025]
- [Huston and Winston 1960][research_huston_winston_1960]
- [Huston et al 1989][research_huston_1989]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Janetzko et al 2026][research_janetzko_2026]
- [Jardin et al 2023][research_jardin_2023]
- [Jiang et al 2026][research_jiang_2026]
- [Jiao and Yang 2026][research_jiao_yang_2026]
- [Jing and Ma 2025][research_jing_ma_2025]
- [Johnson and White 1983][research_johnson_white_1983]
- [Johnson et al 1991][research_johnson_1991]
- [Jokar and Khoshnood 2026][research_jokar_khoshnood_2026]
- [Jung et al 2025][research_jung_2025]
- [Kang et al 2024][research_kang_2024]
- [Kang et al 2026][research_kang_2026]
- [Katz et al 1980][research_katz_1980]
- [Katzoff 1940][research_katzoff_1940]
- [Keith and Selberg 1984][research_keith_selberg_1984]
- [Kelley 1962][research_kelley_1962]
- [Kidd and Bull 1963][research_kidd_bull_1963]
- [Kim et al 2023][research_kim_2023]
- [Kim et al 2026][research_kim_2026]
- [Kirby 1956][research_kirby_1956]
- [Kirby 1961][research_kirby_1961]
- [Koenig and Quigley 1960][research_koenig_quigley_1960]
- [Kong et al 2020, Finite State Coaxial Rotor Inflow][research_kong_2020_2]
- [Korzun 1976][research_korzun_1976]
- [Koshel et al 2026][research_koshel_2026]
- [Kovačević et al 2021][research_kovacevic_2021]
- [Krantz 1994][research_krantz_1994]
- [Kuhn 1957][research_kuhn_1957]
- [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960]
- [Kuhn and Grunwald 1961][research_kuhn_grunwald_1961]
- [Kulhánek et al 2023][research_kulhanek_2023]
- [Kvaternik 1973][research_kvaternik_1973]
- [Lange and McLemore 1950][research_lange_mclemore_1950]
- [Laplante et al 2026][research_laplante_2026]
- [Laskin et al 1968][research_laskin_1968]
- [Latham 1957][research_latham_1957]
- [Lee and Kim 2026][research_lee_kim_2026]
- [Lee and Ko 2025][research_lee_ko_2025]
- [Lee and Yee 2024, Novel Electric Propulsion System A][research_lee_yee_2024_2]
- [Lee et al 2024][research_lee_2024]
- [Lee et al 2026][research_lee_2026]
- [Leishman 1966][research_leishman_1966]
- [Leonard, III 2001][research_leonard_iii_2001]
- [Li and Li 2025][research_li_li_2025]
- [Li et al 2024, Research on Cogging Torque Reducti][research_li_2024_5]
- [Li et al 2024, Short Takeoff and Vertical Landing][research_li_2024_6]
- [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_3]
- [Li et al 2026][research_li_2026]
- [Li et al 2026, Urban air mobility vertiports][research_li_2026_2]
- [Liang et al 2026][research_liang_2026]
- [Liiva 1968][research_liiva_1968]
- [Linnell 1963][research_linnell_1963]
- [Liu et al 2025][research_liu_2025]
- [Liu et al 2025, Supersonic aircraft aerodynamic pe][research_liu_2025_3]
- [Loewy and Yntema 1958][research_loewy_yntema_1958]
- [Lofland 1980][research_lofland_1980]
- [Lopez and Biancolini 2025][research_lopez_biancolini_2025]
- [Lottati 1984][research_lottati_1984]
- [Lundry 1967][research_lundry_1967]
- [Lyu and Feng 2026][research_lyu_feng_2026]
- [Mabboux et al 2024][research_mabboux_2024]
- [Machado et al 2025][research_machado_2025]
- [Makeev 2026, Blade Twist and Disc Loading Effec][research_makeev_2026_2]
- [Mallen and Dancik 1959][research_mallen_dancik_1959]
- [Mancini 1983][research_mancini_1983]
- [Manzuk 1970][research_manzuk_1970]
- [Margason 1966][research_margason_1966]
- [Marques et al 2026][research_marques_2026]
- [Maung et al 2021][research_maung_2021]
- [May et al 2026][research_may_2026]
- [McKinney and Newsom 1962][research_mc_kinney_newsom_1962]
- [McCormick 1969][research_mccormick_1969]
- [McCormick and Mallen 1956][research_mccormick_mallen_1956]
- [McCormick and Mallen 1957][research_mccormick_mallen_1957]
- [McCormick 1956][research_mccormick_w_1956]
- [Meyer and Falabella 1953][research_meyer_falabella_1953]
- [Miley et al 1985][research_miley_1985]
- [Miley et al 1986][research_miley_1986]
- [Milla and Blick 1966][research_milla_blick_1966]
- [Miller 1948][research_miller_1948]
- [Min et al 2026][research_min_2026]
- [Sadiq Ali Mir et al 2025][research_mir_2025]
- [Mirković et al 2026][research_mirkovic_2026]
- [Mitchell 1991][research_mitchell_1991]
- [Mitchell and Mikkelson 1982][research_mitchell_mikkelson_1982]
- [Morisset 1977][research_morisset_1977]
- [Morse and Newhouse 1960][research_morse_newhouse_1960]
- [NACA 1960][research_naca_1960]
- [NACA 1960, Conference on V/Stol Aircraft a Co][research_naca_1960_2]
- [NACA 1961][research_naca_1961]
- [NACA 1982][research_naca_1982]
- [Nagrare and Lieb 2026][research_nagrare_lieb_2026]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Naumowicz and Smith 1992][research_naumowicz_smith_1992]
- [Newsom 1962][research_newsom_1962]
- [Newsom 1962, Force-test Investigation of the St][research_newsom_1962_2]
- [Newsom and Tosti 1959][research_newsom_tosti_1959]
- [Nguyen et al 2025, Comprehensive Modeling of Electric][research_nguyen_2025_2]
- [Ni and Lee 2025][research_ni_lee_2025]
- [Nissen et al 1948][research_nissen_1948]
- [Nozaki et al 2023][research_nozaki_2023]
- [O'Bryan 1961][research_o_bryan_1961]
- [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]
- [Ostowari and Naik 1986][research_ostowari_naik_1986]
- [Page et al 2026][research_page_2026]
- [Pan et al 2026][research_pan_2026]
- [Park 2026][research_park_2026]
- [Park and Kim 2026][research_park_kim_2026]
- [Park and Park 2026][research_park_park_2026]
- [Park et al 2023][research_park_2023]
- [Parker et al 1972][research_parker_1972]
- [Pascioni et al 2026][research_pascioni_2026]
- [Patience and Nahon 2024][research_patience_nahon_2024]
- [Pauer 2018][research_pauer_2018]
- [Payne 1958][research_payne_1958]
- [Perisho 1959][research_perisho_1959]
- [Phillips 1985][research_phillips_1985]
- [Pitkin 1943][research_pitkin_1943]
- [Prabhu and Tiwari 1983][research_prabhu_tiwari_1983]
- [Pruyn and Taylor 1970][research_pruyn_taylor_1970]
- [Purser and Spear 1946][research_purser_spear_1946]
- [Purser and Spear 1947][research_purser_spear_1947]
- [Putman 1961][research_putman_1961]
- [Qiao and Zhou 2026][research_qiao_zhou_2026]
- [Qin 2026][research_qin_2026]
- [Qin et al 2017][research_qin_2017]
- [Queijo et al 1953][research_queijo_1953]
- [Quigley and Koenig 1961][research_quigley_koenig_1961]
- [Ramasamy 2015][research_ramasamy_2015]
- [Rangwalla and Wilson 1987][research_rangwalla_wilson_1987]
- [Reader 1980][research_reader_1980]
- [Reeder 1958][research_reeder_1958]
- [Renselaer 1975][research_renselaer_1975]
- [Ribner 1943][research_ribner_1943]
- [Ribner 1943, Formulas for propellers in yaw and][research_ribner_1943_2]
- [Ribner 1943, Proposal for a propeller side-forc][research_ribner_1943_3]
- [Ribner 1945][research_ribner_1945]
- [Ribner 1945, Propellers in yaw][research_ribner_1945_2]
- [Rizk 1980][research_rizk_1980]
- [Rizzi et al 2026][research_rizzi_2026]
- [Rolls 1965][research_rolls_1965]
- [Ruggia 2025][research_ruggia_2025]
- [Rumph et al 1942][research_rumph_1942]
- [Saari and Sorin 1946][research_saari_sorin_1946]
- [Saetti 2025][research_saetti_2025]
- [Sakai and Abiko 2020][research_sakai_abiko_2020]
- [Sambell 1976][research_sambell_1976]
- [Sastre et al 2025][research_sastre_2025]
- [Savage and Lewicki 1991][research_savage_lewicki_1991]
- [Schuldenfrei 1944][research_schuldenfrei_1944]
- [Schweiger and Preis 2022][research_schweiger_preis_2022]
- [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]
- [Shang et al 2025][research_shang_2025]
- [Shao et al 2025][research_shao_2025]
- [Shen et al 2026, A multi-fidelity workflow for conc][research_shen_2026_2]
- [Shimizu and Miwa 2019][research_shimizu_miwa_2019]
- [Shubert et al 2026][research_shubert_2026]
- [Slaughter 1958][research_slaughter_1958]
- [Sleeman 1953][research_sleeman_1953]
- [Sleeman 1957][research_sleeman_1957]
- [Smith 1958][research_smith_1958]
- [Smith 1959][research_smith_1959]
- [Smith 1977][research_smith_1977]
- [Spadão et al 2026][research_spadao_2026]
- [Spreemann and Kuhn 1956][research_spreemann_kuhn_1956]
- [Stack et al 1950][research_stack_1950]
- [Stech 1977][research_stech_1977]
- [Stepniewski 1957][research_stepniewski_1957]
- [Stokkermans and Veldhuis 2021][research_stokkermans_veldhuis_2021]
- [Strampe and Klingauf 2026][research_strampe_klingauf_2026]
- [Strand and Levinsky 1969][research_strand_levinsky_1969]
- [Suo et al 2026][research_suo_2026]
- [Takacs and Haidegger 2022][research_takacs_haidegger_2022]
- [Takallu and Lessard 1991][research_takallu_lessard_1991]
- [Talbot et al 1994][research_talbot_1994]
- [Tapscott 1960][research_tapscott_1960]
- [Tapscott 1960, Criteria for Control and Response][research_tapscott_1960_2]
- [Lockwood Taylor 1942][research_taylor_1942]
- [Thoren and Johnson 1940][research_thoren_johnson_1940]
- [Tinney and Valdez 2026][research_tinney_valdez_2026]
- [Tosti 1962][research_tosti_1962]
- [Townsend et al 1976][research_townsend_1976]
- [Trenka 1967][research_trenka_1967]
- [Vaicaitis 1980][research_vaicaitis_1980]
- [Velkoff 1981][research_velkoff_1981]
- [Vidal et al 1960][research_vidal_1960]
- [Vollo and Brassaw 1956][research_vollo_brassaw_1956]
- [Voropayev et al 2026][research_voropayev_2026]
- [Wang et al 2019, Research on Dynamic Modeling and T][research_wang_2019_2]
- [Wang et al 2022, Control of centrally-powered varia][research_wang_2022_2]
- [Wang et al 2025][research_wang_2025]
- [Wang et al 2026][research_wang_2026]
- [Warsett 1953][research_warsett_1953]
- [Watts and Biggers 1972][research_watts_biggers_1972]
- [Watts et al 1947][research_watts_1947]
- [Weil and Sleeman 1948][research_weil_sleeman_1948]
- [Welge and Crowder 1978][research_welge_crowder_1978]
- [Welge et al 1981][research_welge_1981]
- [White 1985][research_white_1985]
- [White et al 1960][research_white_1960]
- [Widdison et al 1974][research_widdison_1974]
- [Winston and Huston 1962][research_winston_huston_1962]
- [Winston et al 1975][research_winston_1975]
- [Wood and Woodward 1944][research_wood_woodward_1944]
- [Xiang et al 2025][research_xiang_2025]
- [Xue et al 2026, An efficient transition trajectory][research_xue_2026_2]
- [Yaggy and Rogallo 1960][research_yaggy_rogallo_1960]
- [Yamauchi and Johnson 1994][research_yamauchi_johnson_1994]
- [Yan and Shi 2025][research_yan_shi_2025]
- [Yan et al 2025][research_yan_2025]
- [Yanev and Staack 2026][research_yanev_staack_2026]
- [Yang 2025, Aircraft Pilot Workload Assessment][research_yang_2025_2]
- [Yang et al 2025][research_yang_2025]
- [Yang et al 2025, Fully autonomous anti-interference][research_yang_2025_3]
- [Yi 2026][research_yi_2026]
- [Yu et al 2025][research_yu_2025]
- [Yu et al 2026][research_yu_2026]
- [Zanotti et al 2024, Aerodynamic interaction between ta][research_zanotti_2024_2]
- [Zhang and Hwang 2025][research_zhang_hwang_2025]
- [Zhang and Zhou 2024][research_zhang_zhou_2024]
- [Zhang et al 2026, Optimization of rotor aerodynamic][research_zhang_2026_3]
- [Zhao et al 2014][research_zhao_2014]
- [Zhao et al 2024, Active Fault-Tolerant Strategy for][research_zhao_2024_3]
- [Zhao et al 2025, UAV Operations and Vertiport Capac][research_zhao_2025_3]
- [Zhou 2022][research_zhou_2022]
- [Zhu et al 2025][research_zhu_2025]

[research_aiken_1977]: https://ntrs.nasa.gov/citations/19780011162
[research_albachten_1956]: https://doi.org/10.21236/ad0116273
[research_alfares_2026]: https://doi.org/10.3390/en19081931
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19980223619
[research_antonakis_2025]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_applin_1994]: https://ntrs.nasa.gov/citations/19940032994
[research_araghizadeh_2025]: https://doi.org/10.1063/5.0288862
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_ashkenas_1965_2]: https://doi.org/10.21236/ad0627989
[research_atmaca_2025]: https://doi.org/10.2514/1.g009147
[research_b_tech_1st_year_2025]: https://doi.org/10.71058/jodac.v9i8017
[research_bacchini_2021]: https://doi.org/10.1016/j.ast.2020.106429
[research_badgley_laskin_1970]: https://doi.org/10.21236/ad0869822
[research_baek_2021]: https://doi.org/10.46300/91010.2021.15.3
[research_bai_zhou_2024]: https://doi.org/10.1515/tjj-2022-0065
[research_bartie_1986]: https://ntrs.nasa.gov/citations/19880016983
[research_batina_1985]: https://ntrs.nasa.gov/citations/19850010651
[research_battles_1975]: https://doi.org/10.21236/ada015521
[research_bauer_2025]: https://doi.org/10.3397/in_2025_1076556
[research_bellinger_1972]: https://doi.org/10.4050/jahs.17.35
[research_bencze_1978]: https://ntrs.nasa.gov/citations/19790041868
[research_bennett_1984]: https://doi.org/10.2514/6.1984-2500
[research_beppu_1966]: https://doi.org/10.21236/ad0640945
[research_bergmann_2025]: https://doi.org/10.1007/s13272-025-00839-w
[research_biernacki_lewkowicz_2024]: https://doi.org/10.1016/j.apergo.2024.104268
[research_blaser_1969]: https://doi.org/10.2514/6.1969-197
[research_boatwright_clingan_1969]: https://doi.org/10.2514/6.1969-228
[research_bober_mitchell_1980]: https://doi.org/10.2514/6.1980-225
[research_bobo_1972]: https://ntrs.nasa.gov/citations/19730004301
[research_bohnisch_2026]: https://doi.org/10.1016/j.ast.2025.110763
[research_borst_1978]: https://ntrs.nasa.gov/citations/19790004876
[research_bosch_2026]: https://doi.org/10.1007/s13272-025-00917-z
[research_boucher_2025]: https://doi.org/10.1121/10.0038350
[research_bradley_1956]: https://doi.org/10.4050/jahs.1.32
[research_brenckmann_1958]: https://doi.org/10.2514/8.7650
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_brewer_may_1948]: https://ntrs.nasa.gov/citations/19930082266
[research_brown_timmerman_1991]: https://doi.org/10.2514/6.1991-3167
[research_brusse_cronk_1965]: https://ntrs.nasa.gov/citations/19660010796
[research_burton_2026]: https://doi.org/10.1115/1.4070771
[research_butler_1966]: https://doi.org/10.21236/ad0629637
[research_ca_1969]: https://doi.org/10.21236/ada319985
[research_cai_2026]: https://doi.org/10.3390/drones10050325
[research_carlson_1958]: https://doi.org/10.4050/jahs.3.11
[research_carpenter_paulnock_1949]: https://ntrs.nasa.gov/citations/20090026503
[research_castles_durham_1956]: https://doi.org/10.4050/jahs.1.17
[research_castles_gray_1951]: https://ntrs.nasa.gov/citations/19930083181
[research_cavalcanti_2026]: https://doi.org/10.2514/1.c038528
[research_cavcar_2011]: https://doi.org/10.2514/1.c031351
[research_center_1978]: https://doi.org/10.21236/ada076373
[research_chaohui_2026]: https://doi.org/10.23940/ijpe.26.05.p1.237244
[research_chawla_1952]: https://doi.org/10.2514/8.2357
[research_chen_2023_4]: https://doi.org/10.54254/2755-2721/9/20230018
[research_chen_2025]: https://doi.org/10.3390/drones9090662
[research_chen_2025_2]: https://doi.org/10.1063/5.0281974
[research_chen_schweikhard_1985]: https://doi.org/10.2514/3.45179
[research_chiang_1980]: https://doi.org/10.21236/ada092721
[research_chiocchia_pignataro_1995]: https://doi.org/10.1017/s0001924000028578
[research_choi_2026]: https://doi.org/10.2514/1.c038503
[research_choi_suk_2026]: https://doi.org/10.5139/jksas.2026.54.1.105
[research_churchill_harrington_1959]: https://ntrs.nasa.gov/citations/19980228291
[research_clark_1963]: https://doi.org/10.21236/ad0419126
[research_claro_2026]: https://doi.org/10.1016/j.ast.2026.112259
[research_corless_blanken_1983]: https://ntrs.nasa.gov/citations/19840001967
[research_corliss_1977]: https://ntrs.nasa.gov/citations/19770052109
[research_coward_1955]: https://doi.org/10.21236/ad0101718
[research_coy_1988]: https://ntrs.nasa.gov/citations/19880007257
[research_craig_1991]: https://doi.org/10.2514/6.1991-3120
[research_crespillo_2025]: https://doi.org/10.1007/s13272-024-00749-3
[research_crigler_gilman_1949]: https://ntrs.nasa.gov/citations/19930085544
[research_crigler_gilman_1952]: https://ntrs.nasa.gov/citations/19930083122
[research_crimi_1975]: https://ntrs.nasa.gov/citations/19750023949
[research_critchfield_ning_2026]: https://doi.org/10.2514/1.c038445
[research_cui_2027]: https://doi.org/10.1016/j.ress.2026.113157
[research_curtiss_1967]: https://doi.org/10.21236/ad0663848
[research_curtiss_1985]: https://ntrs.nasa.gov/citations/19860063840
[research_curtiss_c_1965]: https://doi.org/10.21236/ad0628669
[research_czech_2026]: https://doi.org/10.3397/nc_2026_0042
[research_dabaghian_2025]: https://doi.org/10.1063/5.0271761
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_delano_1947]: https://ntrs.nasa.gov/citations/20050019462
[research_delany_1942]: https://ntrs.nasa.gov/citations/20090016408
[research_dempsey_2013]: https://ntrs.nasa.gov/citations/20150021366
[research_deng_2024]: https://doi.org/10.3390/drones8100560
[research_detore_sambell_1975]: https://ntrs.nasa.gov/citations/19750013184
[research_division_1966]: https://ntrs.nasa.gov/citations/19660015317
[research_doetsch_mark_1953]: https://doi.org/10.21236/ad0016744
[research_dong_2024]: https://doi.org/10.61935/acetr.4.1.2024.p130
[research_donlan_1976_2]: https://ntrs.nasa.gov/citations/19770022129
[research_drinkwater_rolls_1962]: https://ntrs.nasa.gov/citations/19620002530
[research_drinkwater_rolls_1963]: https://ntrs.nasa.gov/citations/19630002717
[research_driver_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_du_2024]: https://doi.org/10.1016/j.ijheatfluidflow.2024.109304
[research_ducard_carughi_2024]: https://doi.org/10.3390/drones8120727
[research_dudziak_2020]: https://doi.org/10.20858/sjsutst.2020.108.3
[research_dunham_gentry_1989]: https://ntrs.nasa.gov/citations/19900058369
[research_dunham_gentry_1989_2]: https://doi.org/10.4271/892205
[research_er_el_1988]: https://doi.org/10.2514/3.45535
[research_fan_2021]: https://doi.org/10.2514/1.c035832
[research_farooqui_2025]: https://doi.org/10.15332/19090528.10832
[research_feistel_1981]: https://ntrs.nasa.gov/citations/19810058335
[research_feng_2022]: https://doi.org/10.1049/icp.2022.1595
[research_fisher_mccroskey_1971]: https://ntrs.nasa.gov/citations/19710050390
[research_fluk_1967]: http://web.archive.org/web/20250202082452/https://apps.dtic.mil/sti/tr/pdf/AD0826319.pdf
[research_fluk_1967_2]: http://web.archive.org/web/20250202085427/https://apps.dtic.mil/sti/tr/pdf/AD0826318.pdf
[research_fry_1966]: https://ntrs.nasa.gov/citations/19660015334
[research_gabel_tarzanin_1972]: https://doi.org/10.2514/6.1972-958
[research_gandhi_2026]: https://doi.org/10.2514/1.c038602
[research_garren_1961]: https://ntrs.nasa.gov/citations/20040006489
[research_garren_1965]: https://ntrs.nasa.gov/citations/19650012141
[research_garren_kelly_1965]: https://ntrs.nasa.gov/citations/19650025398
[research_gazzaniga_rose_1992]: https://ntrs.nasa.gov/citations/19920071535
[research_gebhard_1953]: https://doi.org/10.21236/ad0015832
[research_gentry_1991]: https://ntrs.nasa.gov/citations/19920003820
[research_gentry_1994]: https://ntrs.nasa.gov/citations/19940025432
[research_georgiou_2026]: https://doi.org/10.1121/10.0042533
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_gholamian_beik_2026]: https://doi.org/10.1109/ojpel.2026.3664337
[research_gilchrist_1983]: https://doi.org/10.2514/6.1983-2465
[research_gloss_1974]: https://ntrs.nasa.gov/citations/19740020361
[research_gloss_1975]: https://ntrs.nasa.gov/citations/19750015442
[research_gloss_1978]: https://ntrs.nasa.gov/citations/19790005842
[research_gloss_mckinney_1973]: https://ntrs.nasa.gov/citations/19740003706
[research_gloss_washburn_1977]: https://ntrs.nasa.gov/citations/19770022153
[research_gloss_washburn_1979]: https://ntrs.nasa.gov/citations/19790007731
[research_goland_1964]: https://doi.org/10.21236/ad0608186
[research_goldstein_1982]: https://ntrs.nasa.gov/citations/19820015335
[research_golombek_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_goodrich_1989]: https://ntrs.nasa.gov/citations/19890014097
[research_goodson_1961]: https://ntrs.nasa.gov/citations/19980232220
[research_goodson_1966]: https://ntrs.nasa.gov/citations/19660007635
[research_goodson_1966_2]: https://ntrs.nasa.gov/citations/19660015322
[research_goyal_2025_2]: https://doi.org/10.2514/1.j064736
[research_granata_2026]: https://doi.org/10.1016/j.ast.2026.112734
[research_gross_mawhinney_1970]: https://doi.org/10.2514/6.1970-1213
[research_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227988
[research_guo_2025]: https://doi.org/10.1016/j.urbmob.2025.100117
[research_guo_2025_2]: https://doi.org/10.3390/aerospace12080672
[research_gupta_2023_2]: https://doi.org/10.1016/j.ifacol.2023.10.1230
[research_gur_rosen_2005]: https://doi.org/10.2514/1.6564
[research_hagerman_1947]: https://ntrs.nasa.gov/citations/19930082015
[research_hakim_2025]: https://doi.org/10.1016/j.rineng.2025.107358
[research_han_pei_2026]: https://doi.org/10.1109/maes.2025.3566023
[research_hargraves_1961]: https://doi.org/10.21236/ad0268350
[research_harris_1996]: https://ntrs.nasa.gov/citations/19960047059
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hawker_payne_1979]: https://doi.org/10.21236/ada068614
[research_hayden_keller_1974]: https://ntrs.nasa.gov/citations/19740023835
[research_he_2024]: https://doi.org/10.3390/aerospace11030195
[research_hegarty_1965]: https://ntrs.nasa.gov/citations/19650007734
[research_henry_1995]: https://ntrs.nasa.gov/citations/19950023117
[research_hickey_1956]: https://ntrs.nasa.gov/citations/19930088539
[research_hickey_1966]: https://ntrs.nasa.gov/citations/19660015324
[research_hirsch_1954]: https://doi.org/10.4050/sm_wf_1954-3180
[research_hodell_rosner_1957]: https://doi.org/10.21236/ad0142103
[research_hoffman_1969]: https://ntrs.nasa.gov/citations/19690030645
[research_hoffman_1969_2]: https://ntrs.nasa.gov/citations/19690027125
[research_hoffman_1969_3]: https://ntrs.nasa.gov/citations/19700011131
[research_hoffman_1970]: https://ntrs.nasa.gov/citations/19710006223
[research_hohenemser_prelewicz_1974]: https://doi.org/10.4050/sm_dyn_1974-5453
[research_hong_2026]: https://doi.org/10.1007/s42405-025-01020-7
[research_hou_2026]: https://doi.org/10.1109/tie.2026.3661006
[research_howard_1985]: https://ntrs.nasa.gov/citations/19860053764
[research_howard_miley_1989]: https://ntrs.nasa.gov/citations/19890062695
[research_howland_1979]: https://doi.org/10.21236/ada072444
[research_hsu_2024]: https://doi.org/10.4050/jahs.69.022003
[research_hu_2026]: https://doi.org/10.1016/j.ast.2026.112874
[research_hummel_2026]: https://doi.org/10.3397/nc_2026_0026
[research_hung_dai_2025]: https://doi.org/10.1080/24721840.2025.2464115
[research_huston_1989]: https://ntrs.nasa.gov/citations/19890059402
[research_huston_winston_1960]: https://ntrs.nasa.gov/citations/19980227777
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_janetzko_2026]: https://doi.org/10.1007/s10111-026-00883-4
[research_jardin_2023]: https://doi.org/10.1177/1475472x221150181
[research_jiang_2026]: https://doi.org/10.1016/j.enconman.2025.120778
[research_jiao_yang_2026]: https://doi.org/10.1007/s11581-026-07214-7
[research_jing_ma_2025]: https://doi.org/10.1016/j.isatra.2025.08.016
[research_johnson_1991]: https://ntrs.nasa.gov/citations/19910068310
[research_johnson_white_1983]: https://ntrs.nasa.gov/citations/19830068372
[research_jokar_khoshnood_2026]: https://doi.org/10.1007/s11370-026-00704-7
[research_jung_2025]: https://doi.org/10.2514/1.c038132
[research_kang_2024]: https://doi.org/10.1177/09544100231220471
[research_kang_2026]: https://doi.org/10.4050/jahs.71.042006
[research_katz_1980]: https://doi.org/10.2514/6.1980-1872
[research_katzoff_1940]: https://ntrs.nasa.gov/citations/19930091767
[research_keith_selberg_1984]: https://ntrs.nasa.gov/citations/19840035377
[research_kelley_1962]: https://ntrs.nasa.gov/citations/19630000326
[research_kidd_bull_1963]: https://doi.org/10.21236/ad0400265
[research_kim_2023]: https://doi.org/10.5762/kais.2023.24.12.96
[research_kim_2026]: https://doi.org/10.1007/s42405-026-01180-0
[research_kirby_1956]: https://ntrs.nasa.gov/citations/19930084546
[research_kirby_1961]: https://ntrs.nasa.gov/citations/20040047148
[research_koenig_quigley_1960]: https://ntrs.nasa.gov/citations/19630004820
[research_kong_2020_2]: https://doi.org/10.4050/jahs.65.022008
[research_korzun_1976]: https://doi.org/10.21236/ada026247
[research_koshel_2026]: https://doi.org/10.2478/tar-2026-0008
[research_kovacevic_2021]: https://doi.org/10.1108/aeat-03-2021-0091
[research_krantz_1994]: https://ntrs.nasa.gov/citations/19940032949
[research_kuhn_1957]: https://ntrs.nasa.gov/citations/19930084858
[research_kuhn_grunwald_1960]: https://ntrs.nasa.gov/citations/19980227804
[research_kuhn_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227771
[research_kulhanek_2023]: https://doi.org/10.1088/1742-6596/2526/1/012001
[research_kvaternik_1973]: https://ntrs.nasa.gov/citations/19730020244
[research_lange_mclemore_1950]: https://ntrs.nasa.gov/citations/19930082674
[research_laplante_2026]: https://doi.org/10.3846/aviation.2026.26878
[research_laskin_1968]: https://doi.org/10.21236/ad0675458
[research_latham_1957]: https://doi.org/10.1098/rspb.1957.0039
[research_lee_2024]: https://doi.org/10.1115/1.4063934
[research_lee_2026]: https://doi.org/10.1109/taes.2026.3714382
[research_lee_kim_2026]: https://doi.org/10.1109/access.2026.3698794
[research_lee_ko_2025]: https://doi.org/10.31818/jknst.2025.12.8.4.803
[research_lee_yee_2024_2]: https://doi.org/10.2514/1.c037225
[research_leishman_1966]: https://doi.org/10.21236/ad0638632
[research_leonard_iii_2001]: https://doi.org/10.21236/ada430859
[research_li_2024_5]: https://doi.org/10.3390/en17071583
[research_li_2024_6]: https://doi.org/10.1142/s2737480724500195
[research_li_2025_3]: https://doi.org/10.3390/aerospace12100927
[research_li_2026]: https://doi.org/10.1016/j.ast.2025.111519
[research_li_2026_2]: https://doi.org/10.1016/j.urbmob.2026.100265
[research_li_li_2025]: https://doi.org/10.1049/elp2.70088
[research_liang_2026]: https://doi.org/10.1016/j.cja.2025.103898
[research_liiva_1968]: https://doi.org/10.2514/6.1968-58
[research_linnell_1963]: https://doi.org/10.21236/ad0408661
[research_liu_2025]: https://doi.org/10.3390/electronics14183627
[research_liu_2025_3]: https://doi.org/10.1063/5.0282257
[research_loewy_yntema_1958]: https://doi.org/10.4050/jahs.3.1.35
[research_lofland_1980]: https://ntrs.nasa.gov/citations/19800015008
[research_lopez_biancolini_2025]: https://doi.org/10.3390/app15020846
[research_lottati_1984]: https://doi.org/10.2514/3.45051
[research_lundry_1967]: https://doi.org/10.2514/3.43797
[research_lyu_feng_2026]: https://doi.org/10.1016/j.tranpol.2026.104345
[research_mabboux_2024]: https://doi.org/10.1016/j.ast.2023.108778
[research_machado_2025]: https://ntrs.nasa.gov/citations/20250002297
[research_makeev_2026_2]: https://doi.org/10.1590/jatm.v18.1440
[research_mallen_dancik_1959]: https://doi.org/10.4050/jahs.4.15
[research_mancini_1983]: https://ntrs.nasa.gov/citations/19830011853
[research_manzuk_1970]: https://doi.org/10.2514/6.1970-1211
[research_margason_1966]: https://ntrs.nasa.gov/citations/19660015330
[research_marques_2026]: https://doi.org/10.1177/1475472x261419107
[research_maung_2021]: https://doi.org/10.1016/j.compstruct.2020.112961
[research_may_2026]: https://doi.org/10.2514/1.c038391
[research_mc_kinney_newsom_1962]: https://ntrs.nasa.gov/citations/19620001441
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mccormick_mallen_1957]: https://doi.org/10.4050/jahs.2.49
[research_mccormick_w_1956]: https://doi.org/10.21236/ad0159429
[research_meyer_falabella_1953]: https://doi.org/10.2514/8.2557
[research_miley_1985]: https://ntrs.nasa.gov/citations/19860031586
[research_miley_1986]: https://ntrs.nasa.gov/citations/19860064384
[research_milla_blick_1966]: https://doi.org/10.2514/3.43785
[research_miller_1948]: https://doi.org/10.2514/8.11623
[research_min_2026]: https://doi.org/10.1016/j.ast.2026.112840
[research_mir_2025]: https://doi.org/10.61359/11.2106-2549
[research_mirkovic_2026]: https://doi.org/10.1016/j.urbmob.2025.100181
[research_mitchell_1991]: https://ntrs.nasa.gov/citations/19920031828
[research_mitchell_mikkelson_1982]: https://ntrs.nasa.gov/citations/19820018343
[research_morisset_1977]: https://ntrs.nasa.gov/citations/19780009099
[research_morse_newhouse_1960]: https://doi.org/10.21236/ad0248356
[research_naca_1960]: https://ntrs.nasa.gov/citations/19740076580
[research_naca_1960_2]: https://ntrs.nasa.gov/citations/19630004807
[research_naca_1961]: https://ntrs.nasa.gov/citations/20040006318
[research_naca_1982]: https://ntrs.nasa.gov/citations/19820015334
[research_nagrare_lieb_2026]: https://doi.org/10.3390/aerospace13010109
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_naumowicz_smith_1992]: https://doi.org/10.2514/6.1992-4255
[research_newsom_1962]: https://ntrs.nasa.gov/citations/19620005161
[research_newsom_1962_2]: https://ntrs.nasa.gov/citations/19620005247
[research_newsom_tosti_1959]: https://ntrs.nasa.gov/citations/19980228402
[research_nguyen_2025_2]: https://doi.org/10.5139/jksas.2025.53.3.239
[research_ni_lee_2025]: https://doi.org/10.1115/1.4067960
[research_nissen_1948]: https://ntrs.nasa.gov/citations/19930091981
[research_nozaki_2023]: https://doi.org/10.1299/jsmermd.2023.2a1-d11
[research_o_bryan_1961]: https://ntrs.nasa.gov/citations/20040008178
[research_ostheimer_giguere_1963]: https://doi.org/10.21236/ad0402379
[research_ostowari_naik_1986]: https://ntrs.nasa.gov/citations/19860041891
[research_page_2026]: https://doi.org/10.3397/nc_2026_0192
[research_pan_2026]: https://doi.org/10.1016/j.ast.2026.112250
[research_park_2023]: https://doi.org/10.5139/jksas.2023.51.7.497
[research_park_2026]: https://doi.org/10.5139/jksas.2026.54.3.329
[research_park_kim_2026]: https://doi.org/10.1080/0305215x.2025.2602679
[research_park_park_2026]: https://doi.org/10.1016/j.ast.2025.110745
[research_parker_1972]: https://doi.org/10.21236/ad0751463
[research_pascioni_2026]: https://doi.org/10.2514/1.c038487
[research_patience_nahon_2024]: https://doi.org/10.32388/wg08lv.2
[research_pauer_2018]: https://ntrs.nasa.gov/citations/20180007130
[research_payne_1958]: https://doi.org/10.1108/eb032941
[research_perisho_1959]: https://doi.org/10.4050/jahs.4.2.4
[research_phillips_1985]: https://ntrs.nasa.gov/citations/19850007384
[research_pitkin_1943]: https://ntrs.nasa.gov/citations/19930092563
[research_prabhu_tiwari_1983]: https://ntrs.nasa.gov/citations/19840010103
[research_pruyn_taylor_1970]: https://doi.org/10.4050/sm_env_1970-2300
[research_purser_spear_1946]: https://ntrs.nasa.gov/citations/19930081810
[research_purser_spear_1947]: https://ntrs.nasa.gov/citations/19930082127
[research_putman_1961]: https://doi.org/10.21236/ad0270217
[research_qiao_zhou_2026]: https://doi.org/10.1016/j.ast.2025.110825
[research_qin_2017]: https://doi.org/10.1016/j.ast.2017.06.012
[research_qin_2026]: https://doi.org/10.1142/s021812662642017x
[research_queijo_1953]: https://ntrs.nasa.gov/citations/20050080793
[research_quigley_koenig_1961]: https://ntrs.nasa.gov/citations/20030004848
[research_ramasamy_2015]: https://doi.org/10.4050/jahs.60.032005
[research_rangwalla_wilson_1987]: https://ntrs.nasa.gov/citations/19870063073
[research_reader_1980]: https://doi.org/10.21236/ada080953
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_renselaer_1975]: https://ntrs.nasa.gov/citations/19750034271
[research_ribner_1943]: https://ntrs.nasa.gov/citations/19930093307
[research_ribner_1943_2]: https://ntrs.nasa.gov/citations/19930093304
[research_ribner_1943_3]: https://ntrs.nasa.gov/citations/19930093306
[research_ribner_1945]: https://ntrs.nasa.gov/citations/19930091896
[research_ribner_1945_2]: https://ntrs.nasa.gov/citations/19930091897
[research_rizk_1980]: https://ntrs.nasa.gov/citations/19800038563
[research_rizzi_2026]: https://doi.org/10.2514/1.c038188
[research_rolls_1965]: https://ntrs.nasa.gov/citations/19660013004
[research_ruggia_2025]: https://doi.org/10.1016/j.robot.2025.105176
[research_rumph_1942]: https://doi.org/10.2514/8.10936
[research_saari_sorin_1946]: https://ntrs.nasa.gov/citations/20030065899
[research_saetti_2025]: https://doi.org/10.4050/jahs.70.032005
[research_sakai_abiko_2020]: https://doi.org/10.1299/jsmermd.2020.2a2-b01
[research_sambell_1976]: https://ntrs.nasa.gov/citations/19760015087
[research_sastre_2025]: https://doi.org/10.1108/hff-11-2024-0855
[research_savage_lewicki_1991]: https://ntrs.nasa.gov/citations/19910021219
[research_schuldenfrei_1944]: https://ntrs.nasa.gov/citations/19930092564
[research_schweiger_preis_2022]: https://doi.org/10.3390/drones6070179
[research_setiawarman_sasongko_2026]: https://doi.org/10.1142/s2737480726400078
[research_shang_2025]: https://doi.org/10.1049/pel2.70134
[research_shao_2025]: https://doi.org/10.3390/aerospace12100859
[research_shen_2026_2]: https://doi.org/10.1016/j.compfluid.2026.107153
[research_shimizu_miwa_2019]: https://doi.org/10.1299/jsmermd.2019.1p2-o04
[research_shubert_2026]: https://doi.org/10.4050/jahs.71.042008
[research_slaughter_1958]: https://doi.org/10.4050/jahs.3.9
[research_sleeman_1953]: https://ntrs.nasa.gov/citations/20050028463
[research_sleeman_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_smith_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smith_1959]: https://ntrs.nasa.gov/citations/19980228302
[research_smith_1977]: https://doi.org/10.21236/ada069198
[research_spadao_2026]: https://doi.org/10.3390/dynamics6020021
[research_spreemann_kuhn_1956]: https://ntrs.nasa.gov/citations/19930084788
[research_stack_1950]: https://ntrs.nasa.gov/citations/19930092056
[research_stech_1977]: https://doi.org/10.21236/ada036035
[research_stepniewski_1957]: https://doi.org/10.1017/s2753447200003528
[research_stokkermans_veldhuis_2021]: https://doi.org/10.2514/1.j059509
[research_strampe_klingauf_2026]: https://doi.org/10.2514/1.g009745
[research_strand_levinsky_1969]: https://doi.org/10.21236/ad0698355
[research_suo_2026]: https://doi.org/10.1002/eng2.70658
[research_takacs_haidegger_2022]: https://doi.org/10.3390/buildings12060747
[research_takallu_lessard_1991]: https://ntrs.nasa.gov/citations/19910057112
[research_talbot_1994]: https://ntrs.nasa.gov/citations/20010123403
[research_tapscott_1960]: https://ntrs.nasa.gov/citations/19630004822
[research_tapscott_1960_2]: https://ntrs.nasa.gov/citations/20150018614
[research_taylor_1942]: https://doi.org/10.1108/eb030921
[research_thoren_johnson_1940]: https://doi.org/10.2514/8.1190
[research_tinney_valdez_2026]: https://doi.org/10.1121/10.0042016
[research_tosti_1962]: https://ntrs.nasa.gov/citations/19620003850
[research_townsend_1976]: https://ntrs.nasa.gov/citations/19760008977
[research_trenka_1967]: https://doi.org/10.21236/ad0661087
[research_vaicaitis_1980]: https://doi.org/10.2514/3.57877
[research_velkoff_1981]: https://ntrs.nasa.gov/citations/19820010285
[research_vidal_1960]: https://doi.org/10.21236/ad0246522
[research_vollo_brassaw_1956]: https://doi.org/10.21236/ad0102193
[research_voropayev_2026]: https://doi.org/10.1177/1475472x261419081
[research_wang_2019_2]: https://doi.org/10.3390/app9224937
[research_wang_2022_2]: https://doi.org/10.1016/j.ast.2021.107245
[research_wang_2025]: https://doi.org/10.3390/drones9080537
[research_wang_2026]: https://doi.org/10.2514/1.g009139
[research_warsett_1953]: https://doi.org/10.21236/ad0015981
[research_watts_1947]: https://doi.org/10.1126/science.105.2735.583
[research_watts_biggers_1972]: https://doi.org/10.4050/sm_vstol_1972-3031
[research_weil_sleeman_1948]: https://ntrs.nasa.gov/citations/19930082414
[research_welge_1981]: https://ntrs.nasa.gov/citations/19810021547
[research_welge_crowder_1978]: https://ntrs.nasa.gov/citations/19790016853
[research_white_1960]: https://doi.org/10.21236/ad0251154
[research_white_1985]: https://ntrs.nasa.gov/citations/19870002355
[research_widdison_1974]: https://ntrs.nasa.gov/citations/19750022072
[research_winston_1975]: https://doi.org/10.2514/6.1975-1215
[research_winston_huston_1962]: https://ntrs.nasa.gov/citations/19630000659
[research_wood_woodward_1944]: https://doi.org/10.4271/440036
[research_xiang_2025]: https://doi.org/10.3390/drones9080522
[research_xue_2026_2]: https://doi.org/10.1007/s42401-026-00523-9
[research_yaggy_rogallo_1960]: https://ntrs.nasa.gov/citations/19890068078
[research_yamauchi_johnson_1994]: https://ntrs.nasa.gov/citations/19970001814
[research_yan_2025]: https://doi.org/10.1049/icp.2024.2894
[research_yan_shi_2025]: https://doi.org/10.56028/aetr.14.1.1702.2025
[research_yanev_staack_2026]: https://doi.org/10.3390/aerospace13070566
[research_yang_2025]: https://doi.org/10.1088/1742-6596/3126/1/012052
[research_yang_2025_2]: https://doi.org/10.54097/hhzrf702
[research_yang_2025_3]: https://doi.org/10.1088/1361-6501/adb98a
[research_yi_2026]: https://doi.org/10.61173/pevv1749
[research_yu_2025]: https://doi.org/10.3390/aerospace12040355
[research_yu_2026]: https://doi.org/10.1115/1.4071704
[research_zanotti_2024_2]: https://doi.org/10.1016/j.ast.2024.109017
[research_zhang_2026_3]: https://doi.org/10.1016/j.cja.2026.104268
[research_zhang_hwang_2025]: https://doi.org/10.3390/systems13070607
[research_zhang_zhou_2024]: https://doi.org/10.1088/1742-6596/2820/1/012041
[research_zhao_2014]: https://doi.org/10.2514/1.c032570
[research_zhao_2024_3]: https://doi.org/10.1109/taes.2023.3333763
[research_zhao_2025_3]: https://doi.org/10.3390/drones9090621
[research_zhou_2022]: https://doi.org/10.26855/ea.2022.12.003
[research_zhu_2025]: https://doi.org/10.3390/machines13121130
