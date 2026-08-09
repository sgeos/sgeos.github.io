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

**The scale of that literature is the strongest evidence that the X-19's premise was not eccentric.** Wind tunnel investigation of how a running propeller moves an aeroplane's neutral point was a standing programme at the National Advisory Committee for Aeronautics, hereafter NACA, through the 1940s and 1950s, in [Delany 1942][research_delany_1942], [Pitkin 1943][research_pitkin_1943], [Schuldenfrei 1944][research_schuldenfrei_1944], [Purser and Spear 1947][research_purser_spear_1947], [Hagerman 1947][research_hagerman_1947], [Weil and Sleeman 1948][research_weil_sleeman_1948], [Brewer and May 1948][research_brewer_may_1948], [Lange and Mclemore 1950][research_lange_mclemore_1950], [Queijo et al 1953][research_queijo_1953], [Sleeman 1953][research_sleeman_1953], [VOLLO and BRASSAW 1956][research_vollo_brassaw_1956], [Sleeman 1957][research_sleeman_1957], [Goodson 1961][research_goodson_1961], [Donlan 1976, Factors affecting static longitudi][research_donlan_1976_2], [Nagy and Kirsten 1976][research_nagy_kirsten_1976], [Ostowari and Naik 1986][research_ostowari_naik_1986].

Every one of those reports treats the propeller force as a correction to be predicted and designed around. **Curtiss-Wright's proposal was to change its sign in the accounting rather than its magnitude in the physics.**

### Why This Was the Binding Unknown in 1960

The competing configurations of the moment each had a defect that was already visible. The tail-sitter of the [X-13][related_post_a310_ryan_x13] required the pilot to land looking backward and upward. The tilt-wing of the [X-18][related_post_a315_hiller_x18] stalled the un-immersed part of its wing throughout conversion. The deflected slipstream arrangements studied by [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960] and [Grunwald 1961][research_grunwald_1961] paid a large download penalty.

The tilt-propeller avoided all three. Nothing about it requires the wing to stall, nothing requires the pilot to fly backward, and the wing is small enough that the download is modest. The competing arrangements were compared against one another continuously in the design literature of the period, in [Hickey 1956][research_hickey_1956], [Koenig and Quigley 1960][research_koenig_quigley_1960], [Quigley and Koenig 1961][research_quigley_koenig_1961], [PUTMAN 1961][research_putman_1961], [Hargraves 1961][research_hargraves_1961], [Newsom 1962][research_newsom_1962], [Newsom 1962, FORCE-TEST INVESTIGATION OF THE ST][research_newsom_1962_2], [Breul 1963][research_breul_1963], [Goodson 1966][research_goodson_1966], [Goodson 1966, Comparison of wind-tunnel and flig][research_goodson_1966_2], [Beppu et al 1966][research_beppu_1966], [Curtiss et al 1967][research_curtiss_1967], [Strand and Levinsky 1969][research_strand_levinsky_1969], [Kvaternik 1973][research_kvaternik_1973], [Widdison et al 1974][research_widdison_1974], [Detore and Sambell 1975][research_detore_sambell_1975], [Sambell 1976][research_sambell_1976], [Morisset 1977][research_morisset_1977], [Bartie et al 1986][research_bartie_1986], [Huston et al 1989][research_huston_1989]. **The unknown was not whether the configuration could hover or cruise. It was whether the propeller force that made the small wing defensible was real at the size claimed.**

That question had an answer in the literature and the answer was not obviously encouraging. [Ribner 1943][research_ribner_1943] and its final form [Ribner 1945, Propellers in yaw][research_ribner_1945_2] give a theory calibrated against experiment, and [Crigler and Gilman 1949][research_crigler_gilman_1949] and [Crigler and Gilman 1952][research_crigler_gilman_1952] give methods for computing the forces on a propeller in pitch or yaw. The forces are real. Whether they are large enough to size an aircraft around is a question of magnitude, and magnitude is what this article computes.

## Programme Origin

The X-19 did not begin as a military aircraft and did not begin with that designation. [Curtiss-Wright][ref_curtiss_wright] developed it as a civil executive transport under the company designations X-200 and M-200, carrying four passengers, funded from company research money.

Before the transport there was a demonstrator. The [Curtiss-Wright X-100][ref_x100] was built to test two things at once, the radial lift force itself and the gimballed nacelles a tilt-propeller needs. Construction began in February 1958. Tethered hovering started on 20 April 1959, free hover followed in September 1959, and **the first and only transition from vertical to high-speed flight was made on 13 April 1960**. Curtiss-Wright declared the concept proven, handed the aircraft to the National Aeronautics and Space Administration, hereafter NASA, in October 1960 for tests at Langley, and it went afterward to the Smithsonian, where [Smithsonian National Air and Space Museum, Curtiss-Wright X-100][ref_si_x100] and [Vertipedia, Curtiss-Wright X-100][ref_vertipedia_x100] record it.

Then the company's management changed and the new management declined to keep spending research funds on it. The two aircraft were offered to the Tri-Service vertical take-off and landing programme, hereafter VTOL, a joint Army, Navy and Air Force office, and the Air Force contracted for conversion of two prototypes to military standard under the Tri-Service Assault Transport programme. The changes were substantial and none of them were aerodynamic. Ejection seats, a rescue hoist, a mock refuelling probe, and a fuselage stretch for passenger access.

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

**This regime has its own literature and the draft of this article did not touch it**, because the draft discussed only the hover. The high-speed propeller was a continuous research subject from the wartime compressibility work to the advanced turboprop programmes, in [Wood and Woodward 1944][research_wood_woodward_1944], [Stack et al 1950][research_stack_1950], [DOETSCH and MARK 1953][research_doetsch_mark_1953], [Perisho 1959][research_perisho_1959], [Watts and Biggers 1972][research_watts_biggers_1972], [Hohenemser and Prelewicz 1974][research_hohenemser_prelewicz_1974], [Reader 1980][research_reader_1980], [BOBER and MITCHELL 1980][research_bober_mitchell_1980], [Mitchell and Mikkelson 1982][research_mitchell_mikkelson_1982], [GILCHRIST 1983][research_gilchrist_1983], [Takallu and Lessard 1991][research_takallu_lessard_1991], [Gazzaniga and Rose 1992][research_gazzaniga_rose_1992], [Harris 1996][research_harris_1996], [Gur and Rosen 2005][research_gur_rosen_2005], [Cavcar 2011][research_cavcar_2011].

Two of those bear directly on the X-19. Wind tunnel measurement of two-blade propellers to forward Mach numbers of 0.725 established where efficiency begins to fall, which is the constraint that sets the tip speed above. A later reanalysis of early high-speed propellers applied explicitly to civil tiltrotor configurations is the same question asked again for the configuration the X-19 anticipated.

### Hover Then Demands an Extraordinary Blade

A propeller that turns slowly must be large in blade area to produce thrust, because thrust scales with the square of tip speed. Hovering thrust must also exceed weight, since the wings sit under the discs and are pushed down by the slipstream.

Compute the download first. With the nacelles at the tips, the disc reaches inboard by one radius from each tip, so the immersed fraction of a semi-span is the radius over the semi-span whenever the disc does not reach the root.

$$f_{\text{imm}} = \frac{R}{b/2} = \frac{2R}{b}$$

which is 0.667 forward and 0.553 aft, and the immersed area is the sum over the two surfaces.

$$S_{\text{imm}} = \sum_j f_{\text{imm},j} S_j = 91.9 \ \text{ft}^2 = 59.4\% \ \text{of the wing}$$

The download and the flow it comes from were measured for adjacent configurations rather than calculated, in [WHITE et al 1960][research_white_1960], [Curtiss et al 1985][research_curtiss_1985], [Chen and Schweikhard 1985][research_chen_schweikhard_1985], [Leonard and III 2001][research_leonard_iii_2001], [Qin et al 2017][research_qin_2017].

The slipstream velocity at the wing is a multiple $\lambda$ of the induced velocity, and the download is that dynamic pressure acting on the immersed area with a normal-flow drag coefficient.

$$D_{\text{down}} = \tfrac{1}{2} \rho \left( \lambda v_i \right)^2 S_{\text{imm}} C_{D,\perp}$$

Thrust and download depend on each other through $v_i$, so they solve together. Substituting the momentum-theory induced velocity into the download makes the pair LINEAR in thrust rather than requiring iteration, because $v_i^2$ is proportional to $T$.

$$T = W + \frac{\lambda^{2} S_{\text{imm}} C_{D,\perp}}{4 A} \, T \quad \Longrightarrow \quad T = \frac{W}{1 - \lambda^{2} S_{\text{imm}} C_{D,\perp} / 4A}$$

The coefficient is 0.1168, so the download is **1,807 pounds, or 13.2 percent of gross weight**, and the required thrust is 15,467 pounds. Momentum theory then gives the induced velocity, where $A$ is the total disc area of 530.9 square feet.

$$v_i = \sqrt{\frac{T}{2 \rho A}} = 78.28 \ \text{ft/s}$$

Ideal power in hover is the thrust acting through the induced velocity, and the figure of merit is what converts it into a shaft requirement.

$$P_{\text{ideal}} = T v_i = 2{,}201 \ \text{hp}, \qquad P_{\text{req}} = \frac{P_{\text{ideal}}}{\text{FM}} = 3{,}145 \ \text{hp}$$

Against 5,300 installed that is a comfortable margin. The momentum-theory result and its experimental corrections are long established, in [Castles and Gray 1951][research_castles_gray_1951], [Warsett 1953][research_warsett_1953], [BLASER 1969][research_blaser_1969], [BOATWRIGHT and CLINGAN 1969][research_boatwright_clingan_1969], [Parker et al 1972][research_parker_1972], [Velkoff 1981][research_velkoff_1981], [NAUMOWICZ and SMITH 1992][research_naumowicz_smith_1992], [Talbot et al 1994][research_talbot_1994], [Zhao et al 2014][research_zhao_2014], [Ramasamy 2015][research_ramasamy_2015], and one of those addresses a high disc loading propeller in CROSS FLOW by vortex-lattice methods, which is the keystone condition approached by a different route entirely.

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

The blade loading limit that produced it is not an arbitrary number. Stall on a heavily loaded rotor blade was measured and modelled repeatedly, and the solidity that follows from it is the classical design variable, in [Saari and Sorin 1946][research_saari_sorin_1946], [Delano 1947][research_delano_1947], [Chawla 1952][research_chawla_1952], [Meyer and Falabella 1953][research_meyer_falabella_1953], [Hirsch 1954][research_hirsch_1954], [Castles and Durham 1956][research_castles_durham_1956], [Bradley 1956][research_bradley_1956], [LIIVA 1968][research_liiva_1968], [Fisher and Mccroskey 1971][research_fisher_mccroskey_1971], [Bobo 1972][research_bobo_1972], [GABEL and TARZANIN 1972][research_gabel_tarzanin_1972], [Bellinger 1972][research_bellinger_1972], [Crimi 1975][research_crimi_1975], [Borst 1978][research_borst_1978], [Gentry et al 1991][research_gentry_1991], [Yamauchi and Johnson 1994][research_yamauchi_johnson_1994].

**One of those is the precise experiment this article's argument needs.** A wind-tunnel investigation of the effect of HIGH SOLIDITY on propeller characteristics at high forward speed asks exactly the question the X-19's blade answers, and it was published in 1947, sixteen years before the aircraft flew.

### The Wide Blade Is Demanded Twice

Photographs of the X-19 show propellers of remarkable width, and the usual explanation is that the wide chord was chosen to maximise radial lift. The calculation above reaches the same blade **without invoking radial lift at all**. Hovering at a tip speed the 400-knot cruise permits requires it on its own.

This matters for how the configuration should be judged. The wide blade is not a cost incurred to obtain the radial lift force. It is a consequence of two requirements that were going to be imposed anyway, and the radial lift force comes with it. [Dunham and Gentry 1989][research_dunham_gentry_1989] and [Dunham and Gentry 1989, The Effect of Solidity on Propelle][research_dunham_gentry_1989_2] address exactly this coupling, since solidity is the quantity blade chord expresses and normal force is what it produces.

Feeding the chord back gives the projected side area and the recovery fraction.

$$S_f = \frac{2}{\pi}(3)(1.436)(6.5) = 17.83 \ \text{ft}^2 \ \text{per propeller}$$

With a blade lift-curve slope of 4.214 per radian at aspect ratio 4.53, the recovery fraction is

$$k = \frac{(17.83)(4.214)}{2(132.73)} = 0.283$$

**The disc removes about 28 percent of the in-plane momentum that passes through it.** The value is physically admissible, being safely below unity, and it was obtained from geometry rather than chosen.

The coupling the argument rests on, that solidity and normal force move together, is the subject of direct measurement rather than inference. Later work reports the effect of solidity and inclination on propeller-nacelle force coefficients, which is the same pairing this section derives by hand. **A quantity this article obtains from a fin analogy and a projected area is a quantity somebody else measured.**

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

The mutual interference between a propeller and the surface behind it is the older half of the same subject, and it was worked continuously from the 1940s onward, in [Katzoff 1940][research_katzoff_1940], [THOREN and JOHNSON 1940][research_thoren_johnson_1940], [Purser and Spear 1946][research_purser_spear_1946], [Spreemann and Kuhn 1956][research_spreemann_kuhn_1956], [Kuhn 1957][research_kuhn_1957], [BRENCKMANN 1958][research_brenckmann_1958], [VIDAL et al 1960][research_vidal_1960], [Kuhn and Grunwald 1961][research_kuhn_grunwald_1961], [Welge and Crowder 1978][research_welge_crowder_1978], [Bencze et al 1978][research_bencze_1978], [Rizk 1980][research_rizk_1980], [Welge et al 1981][research_welge_1981], [Johnson and White 1983][research_johnson_white_1983], [Miley et al 1985][research_miley_1985], [Howard et al 1985][research_howard_1985], [Miley et al 1986][research_miley_1986], [Howard and Miley 1989][research_howard_miley_1989], [Johnson et al 1991][research_johnson_1991], [Applin et al 1994][research_applin_1994], [Gentry et al 1994][research_gentry_1994].

**The X-19 sits at an unusual point in that literature.** A tilt-wing or a deflected-slipstream aircraft wants the slipstream ON the wing, and most of the work above is about arranging that. The X-19 wants lift from the disc itself and treats the slipstream over the wing as a secondary effect, which inverts the usual emphasis without leaving the field.

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

**The induced part of that split is not a detail for an aircraft with two wings.** Trim on a multi-surface aeroplane costs drag in a way a single wing does not, because the two surfaces can be loaded against each other, and that cost has a literature of its own in [Taylor 1942][research_taylor_1942], [Nissen et al 1948][research_nissen_1948], [Payne 1958][research_payne_1958], [Churchill and Harrington 1959][research_churchill_harrington_1959], [MILLA and BLICK 1966][research_milla_blick_1966], [LUNDRY 1967][research_lundry_1967], [KATZ et al 1980][research_katz_1980], [Lottati 1984][research_lottati_1984], [BENNETT 1984][research_bennett_1984], [Goodrich et al 1989][research_goodrich_1989], [Chiocchia and Pignataro 1995][research_chiocchia_pignataro_1995]. One of those gives a closed-form trim solution minimising drag for aircraft with multiple longitudinal control surfaces, and another treats the induced drag reduction available from propeller and wing interaction directly.

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

**Every band satisfies it, so a continuous path from hover to cruise exists.**

Corridors of this kind were computed and flown for most of the configurations of the period, and the body of work is large, in [Smith 1958][research_smith_1958], [Smith 1959][research_smith_1959], [NACA 1960][research_naca_1960], [NACA 1960, Conference on V/Stol Aircraft a Co][research_naca_1960_2], [Tapscott 1960][research_tapscott_1960], [Anderson 1960][research_anderson_1960], [Tapscott 1960, Criteria for Control and Response][research_tapscott_1960_2], [Kirby 1961][research_kirby_1961], [NACA 1961][research_naca_1961], [Garren 1961][research_garren_1961], [Kelley 1962][research_kelley_1962], [Drinkwater and Rolls 1962][research_drinkwater_rolls_1962], [Drinkwater and Rolls 1963][research_drinkwater_rolls_1963], [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963], [Linnell 1963][research_linnell_1963], [Rolls 1965][research_rolls_1965], [Garren et al 1965][research_garren_1965], [Hegarty et al 1965][research_hegarty_1965], [Garren and Kelly 1965][research_garren_kelly_1965], [Hickey et al 1966][research_hickey_1966], [Margason 1966][research_margason_1966], [Division 1966][research_division_1966], [Fry et al 1966][research_fry_1966], [Trenka 1967][research_trenka_1967]. The narrowest point is at 50 degrees of nacelle, 45 knots wide. The top speed at zero nacelle at sea level is 325 knots, which is consistent with the 400-knot figure quoted at 20,000 feet rather than in conflict with it.

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

Interference between two lifting surfaces in line is a well-populated subject, though most of it arrives under the word canard rather than tandem, in [GEBHARD 1953][research_gebhard_1953], [Kirby 1956][research_kirby_1956], [Driver 1958][research_driver_1958], [MORSE and NEWHOUSE 1960][research_morse_newhouse_1960], [Mc Kinney and Newsom 1962][research_mc_kinney_newsom_1962], [Clark et al 1963][research_clark_1963], [Curtiss and C. 1965][research_curtiss_c_1965], [WINSTON et al 1975][research_winston_1975], [Gloss and Washburn 1979][research_gloss_washburn_1979], [Feistel et al 1981][research_feistel_1981], [Prabhu and Tiwari 1983][research_prabhu_tiwari_1983], [Keith and Selberg 1984][research_keith_selberg_1984], [Phillips 1985][research_phillips_1985], [Batina 1985][research_batina_1985], [Rangwalla and Wilson 1987][research_rangwalla_wilson_1987], [Er-El 1988][research_er_el_1988], [BROWN and TIMMERMAN 1991][research_brown_timmerman_1991], [CRAIG et al 1991][research_craig_1991].

**Three of those are about this exact machine or its close relatives.** Experimental research on four-duct tandem vertical take-off configurations, an investigation of control and stability augmentation for tandem tilting ducted-propeller aircraft, and downwash tests of dual tandem ducted-propeller research aircraft all address a four-propulsor tandem layout. The ducts are the difference, and the longitudinal arrangement is not.

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

The criteria themselves were an active subject rather than a settled one while the X-19 was being built, and the body of work behind them is substantial, in [Carpenter and Paulnock 1949][research_carpenter_paulnock_1949], [Kidd and Bull 1963][research_kidd_bull_1963], [Ashkenas 1965][research_ashkenas_1965], [Ashkenas 1965, A STUDY OF CONVENTIONAL AIRPLANE H][research_ashkenas_1965_2], [Hoffman 1969][research_hoffman_1969], [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_2], [Hoffman 1969, Control power requirements of VTOL][research_hoffman_1969_3], [CA 1969][research_ca_1969], [McCormick 1969][research_mccormick_1969], [Hoffman et al 1970][research_hoffman_1970], [Aiken et al 1977][research_aiken_1977], [Corliss et al 1977][research_corliss_1977], [Smith 1977][research_smith_1977], [Gerken 1979][research_gerken_1979], [Goldstein 1982][research_goldstein_1982], [NACA 1982][research_naca_1982], [Corless and Blanken 1983][research_corless_blanken_1983].

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

At 6,000 revolutions per minute that is 1,376 foot-pounds, at 3,000 it is 2,753, and at propeller speed of 946 it is **8,726 foot-pounds**. Shafts therefore run fast and every propeller needs its own reduction gearbox, which is why the drive system is the large item. The transmission literature of the following decade is about weight and life in exactly these components, in [Leishman 1966][research_leishman_1966], [Laskin et al 1968][research_laskin_1968], [Badgley and Laskin 1970][research_badgley_laskin_1970], [Hayden and Keller 1974][research_hayden_keller_1974], [Battles 1975][research_battles_1975], [Townsend et al 1976][research_townsend_1976], [Korzun 1976][research_korzun_1976], [Vaicaitis 1980][research_vaicaitis_1980], [Mancini 1983][research_mancini_1983], [White 1985][research_white_1985], [Coy et al 1988][research_coy_1988], [Mitchell 1991][research_mitchell_1991], [Savage and Lewicki 1991][research_savage_lewicki_1991], [Krantz 1994][research_krantz_1994], [Henry 1995][research_henry_1995], [Dempsey et al 2013][research_dempsey_2013].

**The shape of that literature is itself an argument.** It is dominated by helicopter transmissions, by failure analysis, by split-torque arrangements and by overhaul economics, which is what a field looks like once it has accepted that the drive system is the hard part. The X-19 met that conclusion early and at first hand.

**The cure for the X-18's disease became the X-19's cause of death.** That sentence is the article's central historical claim and the flight test record is what supports it.

### The Propellers Themselves

Disc loading is where the tilt-propeller beats the tilt-wing outright.

$$\frac{W}{A} = \frac{13{,}660}{530.93} = 25.7 \ \text{lb/ft}^2$$

against 82.1 for the X-18. Four thirteen-foot propellers present a great deal more disc than two sixteen-foot ones, and the penalty for disc loading is explicit once the induced velocity is substituted into the ideal power.

$$\frac{P_{\text{ideal}}}{W} = v_i = \sqrt{\frac{1}{2\rho} \cdot \frac{W}{A}}$$

**Induced power per pound scales with the square root of disc loading**, so the X-19 pays $\sqrt{25.7/82.1} = 0.56$ of what the X-18 pays for every pound it holds up. Power loading follows.

$$\frac{W}{P_{\text{req}}} = \frac{13{,}660}{3{,}145} = 4.34 \ \text{lb/hp}$$

Pitch control of the blades is the mechanism every axis depends on, and the blade forces that mechanism must overcome are treated in [Valentine and Kader 1976][research_valentine_kader_1976], with static thrust estimation in [COWARD 1955][research_coward_1955] and [Brusse and Cronk 1965][research_brusse_cronk_1965].

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

**The seat is the reason there is anything to reconstruct.** Escape at low altitude from an uncontrolled attitude was the hardest case the ejection-seat literature of the period addressed, and it was addressed at length, in [Watts et al 1947][research_watts_1947], [HODELL and ROSNER 1957][research_hodell_rosner_1957], [Latham 1957][research_latham_1957], [MANZUK 1970][research_manzuk_1970], [GROSS and MAWHINNEY 1970][research_gross_mawhinney_1970], [Stech 1977][research_stech_1977], [Center 1978][research_center_1978], [Howland 1979][research_howland_1979], [Hawker and Payne 1979][research_hawker_payne_1979], [Lofland 1980][research_lofland_1980], [Chiang 1980][research_chiang_1980], [Pauer 2018][research_pauer_2018].

Two of those are contemporaneous with the design of the seat that saved this crew. Rocket-track ejection testing at Edwards and a study of seat ejection treated as body ballistics both date from 1957, six years before the X-19 first flew. **An inverted ejection at a few hundred feet sits outside the envelope any of that work would have certified**, which is the honest way to state what happened rather than calling it routine.

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

## The Contemporary Literature

The X-18 article that precedes this one closed on a configuration that came back because the constraint that killed it dissolved. **This article cannot make that claim and should not try to.**

The X-19's keystone was never wrong. A propeller meeting the flow obliquely develops a force normal to its own axis, it did so in 1963, and it does so now. Nothing dissolved it and nothing needed to. What changed is the thing that actually destroyed the aircraft, and the change there is more radical than anything that happened to the aerodynamics.

The survey below is organised by this article's own analysis, so that each modern field can be set against the quantity it addresses.

### The Keystone Became a Routine Term

**The most telling thing about the modern literature on propeller normal force is how little of it there is.** A search that returns hundreds of papers on transition corridors returns a handful here, in [Kong et al 2020, Finite State Coaxial Rotor Inflow][research_kong_2020_2], [Stokkermans and Veldhuis 2021][research_stokkermans_veldhuis_2021], [Patience and Nahon 2024][research_patience_nahon_2024].

That is not neglect. It is the signature of a solved problem. A simplified model for propeller thrust in oblique flow, and a treatment of propeller performance at large angle of attack for compound helicopters, are the shape the subject now takes, which is a term to be included in a simulation rather than a question to be settled.

**Curtiss-Wright's claim was correct and is now uncontroversial.** The company's misfortune was to be right about the aerodynamics and wrong about everything mechanical.

### The Configuration Is Common Now

The X-19's arrangement, several propellers at more than one longitudinal station with a small wing, is no longer unusual. It is close to a description of much of the current electric vertical take-off field, in [Burton et al 2026][research_burton_2026], [Chaohui et al 2026][research_chaohui_2026], [Choi et al 2026][research_choi_2026], [Critchfield and Ning 2026][research_critchfield_ning_2026], [Hong et al 2026][research_hong_2026], [Hou et al 2026][research_hou_2026], [Jokar and Khoshnood 2026][research_jokar_khoshnood_2026], [Kim et al 2026][research_kim_2026], [LIANG et al 2026][research_liang_2026], [May et al 2026][research_may_2026], [Min et al 2026][research_min_2026], [Shubert et al 2026][research_shubert_2026], [Spadão et al 2026][research_spadao_2026], [Wang et al 2026][research_wang_2026], [Xue et al 2026, An efficient transition trajectory][research_xue_2026_2], [Yanev and Staack 2026][research_yanev_staack_2026].

**Tilt-wing, tilt-rotor, lift-plus-cruise and compound layouts are all represented**, and several address the exact problems this article computes by hand, including rotor sizing for tilt-wing vehicles, the aerodynamics of a compound tilt-wing during tilt transition, and the effect of a failure during a backward transition.

### The Corridor Is an Optimisation Problem

This article computes a corridor at ten nacelle angles and reads its continuity off a table. The modern treatment optimises a trajectory through it under constraints, in [SHIMIZU and MIWA 2019][research_shimizu_miwa_2019], [Wang et al 2019, Research on Dynamic Modeling and T][research_wang_2019_2], [SAKAI and ABIKO 2020][research_sakai_abiko_2020], [Chen 2023, Controller design for transition f][research_chen_2023_4], [Gupta et al 2023, Optimal Transition Trajectory of a][research_gupta_2023_2], [Kulhánek et al 2023][research_kulhanek_2023], [Hsu et al 2024][research_hsu_2024], [Li et al 2024, Short Takeoff and Vertical Landing][research_li_2024_6], [Zanotti et al 2024, Aerodynamic interaction between ta][research_zanotti_2024_2], [Xiang et al 2025][research_xiang_2025], [Yang et al 2025][research_yang_2025], [Zhu et al 2025][research_zhu_2025], [Lee et al 2026][research_lee_2026], [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026].

**The shape of the answer is unchanged and the method is unrecognisable.** A conversion schedule is now the output of a constrained optimisation rather than a line on a pilot's card, and the constraints include quantities the X-19's designers never had to write down.

### Wing Loading and Disc Loading Are Still the Trade

The X-19 pushed wing loading to 88 pounds per square foot to buy speed and paid for it with a conversion that could not complete below 114 knots. The same trade is made now with different variables, in [Alfares 2026][research_alfares_2026], [Bosch et al 2026][research_bosch_2026], [Gholamian and Beik 2026][research_gholamian_beik_2026], [Golombek et al 2026][research_golombek_2026], [Hu et al 2026][research_hu_2026], [Jiang et al 2026][research_jiang_2026], [Jiao and Yang 2026][research_jiao_yang_2026], [Lee and Kim 2026][research_lee_kim_2026], [Li et al 2026][research_li_2026], [Makeev 2026, Blade Twist and Disc Loading Effec][research_makeev_2026_2], [Pan et al 2026][research_pan_2026], [Park and Park 2026][research_park_park_2026], [Qiao and Zhou 2026][research_qiao_zhou_2026], [Cui et al 2027][research_cui_2027].

**What has changed is which quantity binds.** The X-19 was limited by installed power and by the conversion speed its wing permitted. A battery-powered vehicle is limited by stored energy, which inverts the sizing problem, and the disc loading that once determined hover power now determines how long the vehicle can hover at all.

### Blades, Solidity and the Advance Ratio

The wide blade this article derives from a capped tip speed is a design problem the field still has, in [Bacchini et al 2021][research_bacchini_2021], [Baek et al 2021][research_baek_2021], [Fan et al 2021][research_fan_2021], [Kovačević et al 2021][research_kovacevic_2021], [Maung et al 2021][research_maung_2021], [Wang et al 2022, Control of centrally-powered varia][research_wang_2022_2], [Jardin et al 2023][research_jardin_2023], [NOZAKI et al 2023][research_nozaki_2023], [B.tech 1st Year 2025][research_b_tech_1st_year_2025], [Goyal et al 2025, Estimation of Rotor Blade Loading][research_goyal_2025_2], [Li and Li 2025][research_li_li_2025], [Liu et al 2025][research_liu_2025], [Shao et al 2025][research_shao_2025], [Yu et al 2026][research_yu_2026].

**The X-19's particular version of it has eased.** Its blade was wide because one propeller had to hover a quarter of the aircraft and then cruise at 400 knots. Distributing lift across more, smaller rotors relaxes both ends of that requirement, and a vehicle that does not attempt 400 knots relaxes the tip-speed cap that forced the chord.

### The Failure Mode Was Deleted Rather Than Improved

**This is the section that matters, and it is where the X-19 differs from every other aircraft in this series so far.**

The X-19 was destroyed by a gearbox. The gearbox existed because two engines had to drive four propellers, which requires an interconnected transmission with a combining box, a cross-shaft and a reduction gearbox at every propeller. This article computes the torque that shaft carries and observes that the interconnection was not optional, since losing one side is 1.67 times full roll control.

**Electric propulsion does not improve that transmission. It removes it.** Each rotor takes its own motor, there is no cross-shaft, there is no combining gearbox, and there is no propeller reduction box to fail. The literature reflects the change, in [Bai and Zhou 2024][research_bai_zhou_2024], [Lee et al 2024][research_lee_2024], [Lee and Yee 2024][research_lee_yee_2024], [Lee and Yee 2024, Novel Electric Propulsion System A][research_lee_yee_2024_2], [Li et al 2024, Research on Cogging Torque Reducti][research_li_2024_5], [Chen et al 2025][research_chen_2025], [Machado et al 2025][research_machado_2025], [Nguyen et al 2025, Comprehensive Modeling of Electric][research_nguyen_2025_2], [Ni and Lee 2025][research_ni_lee_2025], [Shang et al 2025][research_shang_2025], [Yu et al 2025][research_yu_2025], [Böhnisch et al 2026][research_bohnisch_2026], [Granata et al 2026][research_granata_2026], [Koshel et al 2026][research_koshel_2026].

**The cure that killed this aircraft is absent from the modern configuration rather than better engineered within it.** That is a different kind of progress from the one the X-18 article described, and it is worth naming the difference. A315's keystone was dissolved by a technology that made its central quantity irrelevant. A316's keystone survives untouched and its cause of death was designed out.

### Redundancy Replaced Mechanical Interconnection

Removing the cross-shaft removes what the cross-shaft was for. The X-19 needed mechanical interconnection because an engine failure would otherwise be an unrecoverable rolling moment. With enough independent motors the same failure is a control-allocation problem, in [Antonakis and Biannic 2024][research_antonakis_biannic_2024], [Du et al 2024][research_du_2024], [Kang et al 2024][research_kang_2024], [Mabboux et al 2024][research_mabboux_2024], [Ren et al 2024][research_ren_2024], [Zhao et al 2024, Active Fault-Tolerant Strategy for][research_zhao_2024_3], [Atmaca et al 2025][research_atmaca_2025], [Hung and Dai 2025][research_hung_dai_2025], [Jing and Ma 2025][research_jing_ma_2025], [Keir and Mulla 2025][research_keir_mulla_2025], [Ruggia 2025][research_ruggia_2025], [Choi and Suk 2026][research_choi_suk_2026], [Han and Pei 2026][research_han_pei_2026], [Strampe and Klingauf 2026][research_strampe_klingauf_2026].

**The engine-out case stopped being a mechanical problem and became a software one**, which is a change in the kind of engineering required rather than in its difficulty. The one engine inoperative case is still studied, still hard, and no longer solved with a shaft.

### Handling Qualities Became Criteria

The yaw authority this article finds an order of magnitude short would today be measured against a published criterion rather than against judgement, in [Biernacki and Lewkowicz 2024][research_biernacki_lewkowicz_2024], [Deng et al 2024][research_deng_2024], [Ducard and Carughi 2024][research_ducard_carughi_2024], [He et al 2024][research_he_2024], [Antonakis 2025][research_antonakis_2025], [Saetti 2025][research_saetti_2025], [Yan et al 2025][research_yan_2025], [Yang 2025, Aircraft Pilot Workload Assessment][research_yang_2025_2], [Yang et al 2025, Fully autonomous anti-interference][research_yang_2025_3], [Cavalcanti et al 2026][research_cavalcanti_2026], [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026], [Janetzko et al 2026][research_janetzko_2026], [Kang et al 2026][research_kang_2026], [Yi 2026][research_yi_2026].

**Simplified vehicle operations, meaning an aircraft a non-professional can fly, is now a design objective**, which would have been an extraordinary claim while the X-19 was being flown four minutes at a time by test pilots.

### Certification Is Where the Constraint Now Lives

The largest single difference between the X-19's world and the present. A 1963 research aircraft needed to fly. A modern powered-lift aircraft needs to fly, to be certified against a category that had to be invented for it, and to operate in shared airspace, in [DUDZIAK et al 2020][research_dudziak_2020], [Feng 2022][research_feng_2022], [Schweiger and Preis 2022][research_schweiger_preis_2022], [Takacs and Haidegger 2022][research_takacs_haidegger_2022], [Zhou 2022][research_zhou_2022], [Kim et al 2023][research_kim_2023], [Park et al 2023][research_park_2023], [Dong et al 2024][research_dong_2024], [Zhang and Zhou 2024][research_zhang_zhou_2024], [Chen et al 2025, Model-free adaptive flow control o][research_chen_2025_2], [Farooqui 2025][research_farooqui_2025], [Lee and Ko 2025][research_lee_ko_2025], [Laplante et al 2026][research_laplante_2026], [Park 2026][research_park_2026].

**The X-19 was destroyed by a gearbox and cancelled four months later.** Its descendants are more often delayed by a means-of-compliance document, and an article treating only the aerodynamics would miss where the difficulty now lies.

### Noise, Which the X-19 Never Had to Face

A 1963 military transport testbed had no acoustic constraint whatever. A vehicle intended to operate from a city rooftop has one that may bind before any aerodynamic limit does, in [Araghizadeh et al 2025][research_araghizadeh_2025], [Bauer 2025][research_bauer_2025], [Bergmann et al 2025][research_bergmann_2025], [Boucher 2025][research_boucher_2025], [Czech et al 2026][research_czech_2026], [Gandhi et al 2026][research_gandhi_2026], [Georgiou et al 2026][research_georgiou_2026], [Hummel et al 2026][research_hummel_2026], [Marques et al 2026][research_marques_2026], [Page et al 2026][research_page_2026], [Pascioni et al 2026][research_pascioni_2026], [Rizzi et al 2026][research_rizzi_2026], [Tinney and Valdez 2026][research_tinney_valdez_2026], [Voropayev et al 2026][research_voropayev_2026].

**This is a genuinely new constraint rather than an old one made stricter**, and it interacts directly with the quantity this article derives. Tip speed was capped here by cruise Mach number. It is capped now by community noise, at a lower value, which would make the X-19's already extraordinary blade wider still.

### Ground Effect, Download and the Vertiport

The download this article computes at 13.2 percent of gross weight is a wing-area penalty, and the outwash it implies is now an infrastructure question, in [Crespillo et al 2025][research_crespillo_2025], [Guo et al 2025][research_guo_2025], [Guo et al 2025, Research of Hierarchical Vertiport][research_guo_2025_2], [Jung et al 2025][research_jung_2025], [Li et al 2025, Sand Ingestion Behavior of Helicop][research_li_2025_3], [Zhang and Hwang 2025][research_zhang_hwang_2025], [Zhao et al 2025, UAV Operations and Vertiport Capac][research_zhao_2025_3], [Li et al 2026, Urban air mobility vertiports][research_li_2026_2], [Lyu and Feng 2026][research_lyu_feng_2026], [Mirković et al 2026][research_mirkovic_2026], [Nagrare and Lieb 2026][research_nagrare_lieb_2026], [Park and Kim 2026][research_park_kim_2026].

**A vehicle at 26 pounds per square foot of disc loading needs a prepared surface**, and the modern field calls that a vertiport and regulates it, which is the same requirement with a name and a standard attached.

### Methods, Autonomy and What Replaced the Wind Tunnel

The interference this article estimates with a downwash gradient and a contraction factor is now simulated directly, in [Dabaghian et al 2025][research_dabaghian_2025], [Hakim et al 2025][research_hakim_2025], [Liu et al 2025, Supersonic aircraft aerodynamic pe][research_liu_2025_3], [Lopez and Biancolini 2025][research_lopez_biancolini_2025], [Mir 2025][research_mir_2025], [Sastre et al 2025][research_sastre_2025], [Wang et al 2025][research_wang_2025], [Yan and Shi 2025][research_yan_shi_2025], [Cai et al 2026][research_cai_2026], [Claro et al 2026][research_claro_2026], [Qin 2026][research_qin_2026], [Shen et al 2026, A multi-fidelity workflow for conc][research_shen_2026_2], [Suo et al 2026][research_suo_2026], [ZHANG et al 2026, Optimization of rotor aerodynamic][research_zhang_2026_3].

**The 0.444 downwash gradient that costs this aircraft 1.65 degrees of attitude is not a quantity a modern analysis would need to approximate.** It would be resolved, and so would the propeller-wing interference that sits behind the keystone.

### What the Survey Shows

Three things, and the third is the one worth keeping.

**The aerodynamics were right.** The radial lift force is real, is still used, and is no longer argued about.

**The configuration was reasonable.** Multiple propellers at two longitudinal stations with a small wing describes a large fraction of the current field.

**The mechanical architecture was the problem, and it was not solved but abolished.** The X-19 needed a transmission because it had two engines and four propellers, and that requirement disappeared the moment electric motors became a credible way to turn a rotor. **An aircraft can be correct in every argument it makes and still be destroyed by the thing nobody was arguing about.**

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

### The Shape of the Reference Base

The coverage audit that preceded this pass found **both kinds of gap at once, in different topics**, which has not happened before in this series. A314's audit found a genuine shortage of material and A315's found a pool holding everything while the draft used only its earliest part. A316 has both, and they have opposite fixes.

**Five topics were genuinely thin because the draft harvest was never aimed at them, and all five carry relations the equation pass added.** High advance ratio propellers stood at seven records, blade loading and solidity at five, ejection systems at two, aircraft inertias at two, and drag at twelve with none cited. A targeted harvest took the first four to 29, 31, 25 and five. **That is the inter-pass dependency A315 identified, arriving on schedule rather than as a surprise.**

**The remaining topics were deep and barely used, which no search would have fixed.** Transition held 268 records against 18 cited, the slipstream 96 against eight, the tandem wing 69 against six, control power 71 against four. Spreading the selection was the whole of the work there.

**Two references were removed after the sweep rather than added by it, and the reason is worth stating.** A propeller in oblique inflow is a live research subject in NAVAL ARCHITECTURE, where it means a ship screw meeting the wake of a hull at an angle, and that literature uses the same words as this article. The first selection run returned eight candidates for the keystone topic and **all eight were marine**. Filtering on the journal rather than the title removed them, and one of them, a paper on the normal force of a rudder behind a controllable-pitch propeller, carries no marine word in its title at all.

**Two still got through, and both were caught by reading rather than by any rule.** A method for calculating the spindle torque of a controllable-pitch propeller is David Taylor Model Basin work on ship propellers, and a report on four-quadrant open-water characteristics concerns propeller 4739 designed for LSD-41, a dock landing ship. The second reached a section on vertical-flight handling qualities because the selection pattern for controllability matched the phrase controllable pitch. **Archive records carry no journal name, so the venue filter that caught the other eight could not see these two.**

**The contemporary sweep found the keystone's modern literature to be small, and that is a result rather than a gap.** Transition corridors return hundreds of recent papers and propeller normal force returns a handful. A quantity that is settled stops generating publications, so the thinness is evidence that Curtiss-Wright's aerodynamic claim is no longer contested.

**One topic remains genuinely thin and is reported rather than padded.** Aircraft moments of inertia and radii of gyration returned five records after a targeted search, because mass-properties reports are working documents that archives rarely index. The three inertias in this article therefore rest on radii of gyration assumed as fractions of length and span, and that assumption is named in the Epistemic State rather than supported by citation.

## Epistemic State

**Historical fact.** The X-19 first flew on 20 November 1963 and was destroyed on 25 August 1965. It made 50 flights totalling four hours and never transitioned. Both crew ejected and survived. The programme was cancelled and the second airframe was never completed. The X-100 preceded it, first hovered free in September 1959, and made a single transition on 13 April 1960. The aircraft began as the company-funded X-200 or M-200 and was adopted by the Tri-Service VTOL programme.

**Published figures taken as given.** Gross weight 13,660 pounds, wing areas 56.1 and 98.5 square feet, spans 19.5 and 23.5 feet, four propellers of 13 feet, two Lycoming T55-L-7 engines of 2,650 shaft horsepower, length 44 feet, maximum speed 400 knots at 20,000 feet, cruise 347.6 knots at 15,000 feet.

**Engineering analysis.** Wing loading of 88.4 pounds per square foot, stall at 136.5 knots, download of 13.2 percent, hover induced velocity of 78.3 feet per second, permitted tip speed of 644.2 feet per second, derived blade chord of 17.2 inches, in-plane recovery fraction of 0.283, cruise lift share of 29.8 percent, equivalent plain wing of 218 to 225 square feet, the corridor table, tandem attitude penalty of 1.65 degrees, control accelerations, cross-shaft torques, and the free-fall budget are all computed here from published geometry and are not quoted from any source.

**Assumed quantities, each of which moves the answers.** Maximum lift coefficient of 1.4, helical tip Mach limit of 0.90, blade loading limit of 0.14, hover figure of merit of 0.70, download drag coefficient of 1.20 with slipstream factor 1.5, propeller efficiency of 0.80 at maximum speed, span efficiencies, an effective tandem aspect ratio of 6.0, a propeller station separation of 20 feet, and radii of gyration at 0.30, 0.30 and 0.35 of the relevant dimension. **The propeller rotational speed is not in the public record and was derived from the cruise requirement rather than taken from a source.**

**A model inconsistency found and fixed rather than carried.** An earlier version of the calculation used a figure of merit of 0.70 in one place and a propeller efficiency of 0.80 in another for what the momentum model treats as a single quantity. The corridor is now reported across both values, and the low-speed boundaries are identical while the high-speed boundaries move by about 5 percent.

**Two errors the equation review exposed, both in the drafted text.** The pitch-moment relation was displayed as $M = fT\ell$, which evaluates to twice the 15,467 foot-pounds quoted in the prose beside it. The quoted value was right and the displayed algebra carried a spurious factor of two, so the article contradicted itself in a way every automated check passed. The yaw inertia was transcribed as 100,565 slug feet squared against a computed 100,690, which left the acceleration built on it correct and the stated inertia wrong. **Writing the relation down has now caught a wrong claim in twelve consecutive articles in this series.** A third defect was introduced by the review itself, an unterminated display block that would have rendered as broken mathematics, and the style checker was extended to catch that class.

**A defect that no automated check would have caught.** The first corridor formulation solved the vertical equilibrium equation for thrust and then tested the same equation, which is satisfied identically at any speed down to zero. It returned 0.6 knots at every nacelle angle below 60 degrees. Nothing flagged it. It was caught by reading the output and finding it absurd, which is the same way A315's 454-knot crossover speed was caught.

**A structural defect from the draft pass, found in the publication review.** The research-aircraft genre carries three sections beyond the standard twelve, and this article was drafted with only two. **The Contemporary Literature section was missing entirely** and every automated check passed the article, because sections were counted rather than identified. The section is now present and the checker now names the three it requires.

**Three acronyms were used before being expanded**, namely NACA, NASA and the vertical take-off and landing abbreviation, the last used some thirty thousand characters before its expansion. All three are corrected.

**A false-positive family this article had to learn.** The naval architecture literature on propellers in oblique inflow uses this article's exact vocabulary, and it contaminated the keystone topic completely on the first pass. Eight candidates were removed by filtering on journal name and two more by reading. **No pattern over titles would have found the last two**, because archive records carry no journal and the titles contain no marine word.

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

The contemporary literature adds a final observation that changes the verdict on the programme rather than on the physics. **Every aerodynamic argument Curtiss-Wright made has held.** The radial lift force is real and is now a routine term. The configuration of several propellers at two longitudinal stations with a small wing describes a large part of the current electric vertical take-off field. The company was right about the hard part and lost the aircraft to the transmission, which is the part nobody was arguing about, and which its descendants do not have because electric motors abolished the need for it rather than because anyone made gearboxes better.

**An aircraft can be correct in every argument it makes and still be destroyed by the thing nobody was arguing about.**

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
[research_keir_mulla_2025]: https://doi.org/10.1123/mc.2024-0127
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
[research_lee_yee_2024]: https://doi.org/10.2514/1.c037225.c1
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
[research_ren_2024]: https://doi.org/10.1016/j.mechatronics.2024.103266
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
[research_valentine_kader_1976]: https://doi.org/10.21236/ada035756
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
