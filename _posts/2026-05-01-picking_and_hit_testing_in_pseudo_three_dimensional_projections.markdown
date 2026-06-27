---
layout: post
mathjax: true
comments: true
title:  "Picking and Hit Testing in Pseudo-Three-Dimensional Projections"
date:   2026-05-01 09:00:00 +0000
categories: games graphics projection
---

<!-- A186 -->
<script>console.log("A186");</script>

The second article of the cross-cutting cluster
treats picking and hit testing
across the projection modes
that the previous clusters covered.
Picking is the operation
that converts a screen pixel
into a world position or a gameplay object identifier.
The screen pixel
comes from a mouse click,
a touchscreen tap,
a light-gun trigger pull,
or any other input event
that names a single screen location.
The engine
applies the inverse of the forward projection
to recover the world coordinates,
then identifies which gameplay object
the click corresponds to.

The previous articles
introduced inverse maps for each projection mode
and three disambiguation strategies
for the cases where the inverse is underdetermined.
The decoupled-vertical-axis article
introduced the ground-plane assumption,
the known-depth assumption,
and the screen-space sprite hit test.
The belt-scroll, oblique, and axonometric articles
extended these to their respective projection modes.
The draw-order article
introduced the topmost-in-draw-order convention
for resolving overlapping sprites.
The article here
gathers the full framework,
treats the numerical stability of the inverse
through the condition number,
gives the area-scaling interpretation of the determinant,
treats the canonical sprite-scale-and-rotate hit test
that Battle Clash and Metal Combat used
for the Super Scope light-gun gameplay,
and discusses light-gun picking
as the historical realisation
of the abstract picking operation.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is the inverse-map equation
that converts the screen pixel
into a world position.
The delivery mechanism
chooses the input device
that produces the screen pixel
and the algorithm
that identifies the gameplay object.

## A Brief History of Picking

Picking in computer graphics
dates to the 1960s
as part of the interactive systems
that the early graphics laboratories built.
The video-game adoption
arrives with the home and arcade systems
that supported direct screen input.

The light-gun lineage
begins with the Magnavox Odyssey light gun in 1972
which provided an analogue photodiode
that fired when pointed at a bright cathode-ray-tube screen pixel.
The technique
became universal in arcade and console games
through the late 1970s and 1980s.
The [NES Zapper][ref_zapper]
shipped with the Nintendo Entertainment System in 1985
and powered Duck Hunt
along with several subsequent titles
through the standard photodiode mechanism.

[Operation Wolf][ref_operation_wolf]
from Taito in 1987
brought light-gun shooting
to the arcade
with a mounted machine-gun controller
that the player aimed at on-screen enemies.
[Operation Thunderbolt][ref_operation_thunderbolt]
from Taito in 1988
followed with a similar mounted-gun cooperative gameplay format.

The Super Scope
released as a separately-purchased accessory
for the Super Nintendo Entertainment System in 1992
and powered the Super Scope shooter subgenre.
[Battle Clash][ref_battle_clash]
from Nintendo and Intelligent Systems in 1992
brought the canonical sprite-scale-and-rotate hit-test case
to the home console.
[Metal Combat, Falcon's Revenge][ref_metal_combat]
from Nintendo and Intelligent Systems in 1993
extended the format
with additional enemy mecha and gameplay scenarios.

The arcade light-gun tradition
continued through the 1990s
with [The House of the Dead][ref_house_of_the_dead]
from Sega in 1996
which combined three-dimensional polygon rendering
with light-gun targeting
in the survival-horror format.

The mouse-driven picking tradition
runs in parallel
with point-and-click adventure games
of the mid-1980s
that the article treats as a parallel lineage
to the light-gun games.
The modern era
combines mouse, touchscreen, and motion-controller input
through a common abstract picking framework
that the article describes.

## The Inverse Map Framework

The forward map of a projection mode
takes a world coordinate $\mathbf{p}_{\text{world}}$
to a screen coordinate $\mathbf{p}_{\text{screen}}$.
The inverse map
takes a screen coordinate
to a world coordinate or to a candidate set
when the inverse is underdetermined,

$$
\mathbf{p}_{\text{screen}} \xrightarrow{F^{-1}} \{\mathbf{p}_{\text{world}}^{(k)}\}_k.
$$

The candidate set
has a single element
when the forward map is a bijection
on the relevant world region,
as in the floor-case top-down
and the side-scrolling modes.
The candidate set
has multiple elements
when the inverse is underdetermined,
as in the decoupled-vertical-axis,
belt-scroll,
oblique,
and axonometric modes.

The three disambiguation strategies
that the previous articles introduced
reduce the candidate set
to a single element
through a contextual assumption.

The ground-plane assumption
sets the vertical world coordinate
to the ground level
$w_y = w_y^{\text{ground}}$
and recovers the remaining coordinates
through the projection mode's inverse,

$$
\mathbf{p}_{\text{world}}^{\text{ground}} = F^{-1}_{\text{ground}}(\mathbf{p}_{\text{screen}}).
$$

The convention is appropriate
for movement commands
where the click identifies a ground destination.

The known-depth assumption
sets the depth coordinate
to a value $w_z^{\text{known}}$
that the gameplay context provides
and recovers the remaining coordinates,

$$
\mathbf{p}_{\text{world}}^{\text{known-depth}} = F^{-1}_{w_z = w_z^{\text{known}}}(\mathbf{p}_{\text{screen}}).
$$

The convention is appropriate
when the engine knows the gameplay-relevant depth
through the object list and the object's current state.

The screen-space sprite hit test
ignores the world coordinates entirely
and tests the clicked screen pixel
against the screen-space bounding rectangles
of every visible sprite,

$$
\text{hit}(i) \iff \mathbf{p}_{\text{screen}} \in B_i^{\text{screen}},
$$

where $B_i^{\text{screen}}$
is the screen-space bounding box
of sprite $i$.
The convention is appropriate
for direct sprite selection
including light-gun targeting and cursor-driven gameplay.

The topmost-in-draw-order convention
of the draw-order article
extends the screen-space hit test
by iterating the visible sprites
in front-to-back order,

$$
\text{pick} = \arg\min_{i : \text{hit}(i)} \text{depth}_i,
$$

where $\text{depth}_i$
is the depth from camera of sprite $i$.
The closest sprite that the click hits
is returned.

For piecewise projections of the stylised-hybrid article,
the inverse map is itself piecewise.
The engine first identifies
which region or game state the click belongs to
based on the screen position
or on the current game state,
then applies the corresponding region's inverse.

The full picking framework
combines these elements
into a per-click algorithm
that the engine executes
on each input event.
The algorithm
identifies the projection mode active in the click region,
applies the appropriate inverse map,
runs the appropriate disambiguation strategy,
and returns the world position
or the gameplay object identifier.

## Condition Number and Numerical Stability

The inverse map
for projection modes
where the matrix is two-by-two and invertible
involves solving a linear system $A \mathbf{x} = \mathbf{b}$
for $\mathbf{x}$
given the matrix $A$
and the right-hand side $\mathbf{b}$.
The numerical stability of the solution
depends on the condition number of $A$.

The condition number
is the ratio of the largest singular value
to the smallest,

$$
\kappa(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}.
$$

An equivalent expression
uses the operator two-norm,

$$
\kappa(A) = \|A\|_2\, \|A^{-1}\|_2.
$$

The condition number bounds
how input perturbations
propagate to output perturbations.
If $\mathbf{b}$ is perturbed by $\Delta \mathbf{b}$,
the resulting perturbation
$\Delta \mathbf{x}$ in the solution satisfies

$$
\frac{\|\Delta \mathbf{x}\|}{\|\mathbf{x}\|} \leq \kappa(A)\, \frac{\|\Delta \mathbf{b}\|}{\|\mathbf{b}\|}.
$$

A condition number near $1$
indicates a well-conditioned inverse
where small input perturbations
produce small output perturbations.
A large condition number
indicates an ill-conditioned inverse
where small input perturbations
produce large output perturbations
and the inverse becomes numerically unreliable.

The condition number values
for the projection modes of the previous clusters
are typically small.
The sprite scale-and-rotate matrix
$A = s\, R(\theta)$
has $\kappa(A) = 1$
because rotation and uniform scaling
preserve angles.
A rotation alone or a uniform scale alone
has $\kappa = 1$.

The game-iso ground-plane matrix

$$
A_{\text{game-iso}} = z\begin{bmatrix} 1 & -1 \\ 1/2 & 1/2 \end{bmatrix}
$$

has singular values
$z\sqrt{2}$ and $z/\sqrt{2}$
with $\kappa(A_{\text{game-iso}}) = 2$
independent of the zoom factor.

The belt-scroll ground-plane matrix
with depth-mixing slope $\beta$
has

$$
A_{\text{belt-scroll}} = z\begin{bmatrix} 1 & 0 \\ 0 & -\beta \end{bmatrix},
$$

singular values $z$ and $\beta z$,
and condition number $\kappa = 1/\beta$.
For typical $\beta = 1/2$,
$\kappa = 2$.

The Mode 7 per-scanline matrix
$M(s_y) = z(s_y) R(\theta)$
has $\kappa(M(s_y)) = 1$
at every scanline
because rotation and uniform scaling
remain conformal under the per-scanline scaling factor.

The two-dimensional projection modes of the series
all produce well-conditioned inverses
with $\kappa$ on the order of unity.
Numerical issues
do not arise in standard gameplay
because the floating-point precision of modern engines
is far below the condition-number threshold
that would degrade the inverse.

## The Determinant as Area Scale

The determinant of the forward map's two-by-two matrix
gives the screen-space area
that a unit world-space rectangle covers
under the projection.
For a forward map $\mathbf{p}_{\text{screen}} = A \mathbf{p}_{\text{world}} + \mathbf{o}$,
the screen-space area $A_{\text{screen}}$
covered by a world-space rectangle of area $A_{\text{world}}$
is

$$
A_{\text{screen}} = |\det(A)|\, A_{\text{world}}.
$$

The sprite scale-and-rotate matrix
has $\det(s R(\theta)) = s^2$
because $\det(R) = 1$ and the scaling factor enters quadratically.
A sprite at twice the distance from the camera
covers a quarter of the screen area
of the same sprite at unit distance,
matching the quadratic area law
of the sprite-scaling article.

The game-iso ground-plane matrix
has $\det(A_{\text{game-iso}}) = z^2 (1 \cdot 1/2 - (-1)(1/2)) = z^2$,
so a unit ground-tile area
covers $z^2$ screen pixels.
For $z = 32$,
each unit tile covers $32^2 = 1024$ screen pixels,
matching the diamond tile area
of game-iso forward map.

The Mode 7 per-scanline matrix
has $\det(M(s_y)) = z(s_y)^2$,
which varies per scanline.
The variation
produces the apparent shrinkage of texture content
at distant scanlines
and the apparent magnification of texture content
at near scanlines.
The article on Mode 7
treats the per-scanline scaling in detail.

The belt-scroll ground-plane matrix
has $\det(A_{\text{belt-scroll}}) = -\beta z^2$
with $|\det| = \beta z^2$.
A unit ground-tile area
covers $\beta z^2$ screen pixels,
which is smaller than the top-down case
by the factor $\beta$.
The reduction
reflects the foreshortening
of the depth axis in the belt-scroll projection.

The determinant
also appears in the picking density.
The world-space area sampled by a screen-space area $\Delta A_{\text{screen}}$
is the inverse of the area-scaling relationship,

$$
\Delta A_{\text{world}} = \frac{\Delta A_{\text{screen}}}{|\det(A)|}.
$$

A larger determinant
gives finer picking precision
through smaller world-space area per screen pixel
at the cost of larger screen-space coverage per world unit.

A vanishing determinant
indicates that the forward map is singular
and the inverse does not exist.
The picking ray
then samples a one-dimensional curve
in the world space
rather than a two-dimensional area.
The case
arises at extreme camera tilt
or at degenerate viewing angles
where the projection collapses one of the world axes
onto the screen plane.

## Sprite Scale-and-Rotate Hit Test

The canonical sprite-scale-and-rotate hit test
of the Battle Clash and Metal Combat Super Scope shooters
inverts the sprite-scaling forward map
of the sprite-scaling article
to recover the sprite-local pixel position
from the screen click.

The forward map for a sprite
at screen anchor position $\mathbf{c}$
with scaling factor $s$
and orientation angle $\theta$
maps a sprite-local pixel $\mathbf{p}_{\text{local}}$
to a screen pixel
$\mathbf{p}_{\text{screen}} = \mathbf{c} + s R(\theta) \mathbf{p}_{\text{local}}$.

The inverse map
recovers the sprite-local position
from the screen click,

$$
\mathbf{p}_{\text{local}} = \frac{1}{s}\, R(-\theta)\, (\mathbf{p}_{\text{screen}} - \mathbf{c}).
$$

The hit test
then checks the sprite-local position
against the sprite's local bounding rectangle,

$$
\text{hit} \iff |u| \leq \frac{w_{\text{sprite}}}{2}\, \land\, |v| \leq \frac{h_{\text{sprite}}}{2}.
$$

A refined hit test
samples the sprite's alpha value
at the local pixel position
to distinguish opaque from transparent sprite regions,

$$
\text{hit, opaque} \iff \alpha(\mathbf{p}_{\text{local}}) > \alpha_{\text{threshold}},
$$

where $\alpha(\mathbf{p}_{\text{local}})$
is the sprite's alpha at the rounded local pixel coordinates
and $\alpha_{\text{threshold}}$
is the engine's transparency threshold.
The refined test
rejects clicks
on the sprite's transparent border
and accepts only clicks
on the sprite's drawn content.

For Battle Clash specifically,
the giant enemy mecha
renders through Mode 7 background hardware
treated as a single rotating-scaling sprite.
The cartridge software
maintains the current Mode 7 matrix entries
that determine the scale and rotation
of the mecha sprite.
The Super Scope hit
reads as a screen pixel,
and the cartridge software
inverts the Mode 7 matrix
to recover the sprite-local position
on the mecha sprite.
The sprite-local position
identifies which part of the mecha was hit,
which drives the damage modelling
and visual effects.

When multiple sprites are visible,
the hit test iterates the sprites
in front-to-back depth order
through the topmost-in-draw-order convention
of the previous article.
The first sprite
whose inverse-mapped click pixel
falls within the sprite's local rectangle
and on an opaque pixel
is returned.
Sprites behind the hit sprite
are not tested further.

## Light-Gun Picking

The light-gun input device
makes the picking operation literal.
The player physically aims a gun-shaped controller
at the cathode-ray-tube display
and pulls the trigger.
A photodiode in the gun
fires when the cathode ray
sweeps across the gun's pointed pixel.

The console
synchronises the photodiode reading
with the cathode-ray-tube raster scan
to determine which screen pixel
the gun was pointed at
when the trigger fired.
The standard implementation
uses a two-frame approach.

In the first frame,
the console draws the entire scene normally.
The player aims the gun and pulls the trigger.

In the second frame,
the console flashes a bright field
at each potential hit target's screen position.
The photodiode in the gun
fires when the gun is pointed at one of these bright fields,
and the console records the timing
of the photodiode pulse.

The pulse timing
identifies which screen scanline
and which horizontal pixel
the gun was pointed at,
because the cathode-ray-tube raster
sweeps the screen in a known pattern.
The console
maps the timing
to the screen pixel coordinates $(s_x, s_y)$.

The screen pixel coordinates
then enter the inverse map framework
to identify the world position or gameplay object.
For Battle Clash,
the inverse map applies the Mode 7 sprite-scale-and-rotate hit test
to determine which part of the mecha was hit.
For Duck Hunt,
the inverse map applies the screen-space hit test
to determine which duck was hit.

The light-gun framework
is a special case of the general picking framework
where the input device
delivers the screen pixel
through hardware rather than through software cursor tracking.
The downstream inverse map and hit test
follow the same algorithm
as cursor-driven or touchscreen-driven picking.

Modern flat-panel displays
do not support the cathode-ray-tube light gun
because the display update mechanism differs.
Modern light-gun-style games
use camera-based or accelerometer-based input
that the article treats as the modern equivalent
of the cathode-ray-tube light gun.

## A Worked Example

Consider a Battle Clash-style Super Scope shooter
with the following parameters.
The screen is 256 pixels wide
and 224 pixels tall.
The mecha boss sprite
is 64 pixels wide and 64 pixels tall
in sprite-local coordinates
with extent $|u| \leq 32$, $|v| \leq 32$.
The sprite's current screen anchor is $\mathbf{c} = (160, 140)$.
The sprite's current scale factor is $s = 2$.
The sprite's current orientation is $\theta = \pi/6$
matching 30 degrees counterclockwise rotation.

The Super Scope reports a hit at screen pixel $\mathbf{p}_{\text{screen}} = (200, 150)$.
The cartridge software
computes the sprite-local hit position
through the inverse forward map.

The screen-space offset from the sprite anchor is

$$
\mathbf{p}_{\text{screen}} - \mathbf{c} = (200 - 160,\ 150 - 140) = (40, 10).
$$

The inverse rotation by $-\pi/6$
uses $\cos(-\pi/6) = \sqrt{3}/2 \approx 0.866$
and $\sin(-\pi/6) = -1/2$.
The rotation matrix is

$$
R(-\pi/6) = \begin{bmatrix} 0.866 & 0.5 \\ -0.5 & 0.866 \end{bmatrix}.
$$

Applying the rotation to the screen-space offset gives

$$
R(-\pi/6) \cdot (40, 10) = (0.866 \cdot 40 + 0.5 \cdot 10,\ -0.5 \cdot 40 + 0.866 \cdot 10) = (39.6, -11.3).
$$

Dividing by $s = 2$
gives the sprite-local hit position,

$$
\mathbf{p}_{\text{local}} = (39.6/2,\ -11.3/2) = (19.8, -5.7).
$$

The bounding-box test
verifies $|19.8| \leq 32$ and $|-5.7| \leq 32$.
Both conditions hold,
so the click hits the sprite.

The determinant of the forward map
gives $\det(s R(\theta)) = 4$,
so a unit area in sprite-local coordinates
covers four screen pixels.
The sprite's screen area
is $64 \cdot 64 \cdot 4 = 16{,}384$ screen pixels.

The condition number of the forward map
is $\kappa(s R(\theta)) = 1$
because rotation and uniform scaling
preserve angles.
The inverse is well-conditioned
and the hit-position computation
is numerically reliable.

A refined alpha test
samples the sprite's alpha value
at sprite-local pixel coordinates $(20, -6)$
after rounding the inverse result to the nearest integer.
The sample
returns the alpha value
from the sprite atlas at that pixel.
If the value exceeds the transparency threshold,
the hit registers as opaque
and the engine reports a hit on the mecha.

The round-trip identity
holds within the sprite,

$$
F_{\text{sprite}}^{-1}(F_{\text{sprite}}(\mathbf{p}_{\text{local}})) = \mathbf{p}_{\text{local}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

A second sprite at the same screen anchor
but with scale $s = 1$ and zero rotation
would have its own inverse map
applied to the same screen click.
The smaller sprite
covers less screen area
and the click at $(200, 150)$
at offset $(40, 10)$ from the anchor
falls outside its local extent $|u| \leq 32$.
The smaller sprite does not register a hit.

When both sprites are visible,
the topmost-in-draw-order convention
returns the closer sprite
that the click hits.
The larger mecha sprite at scale $s = 2$
returns as the hit.

## Variations Within the Framework

The picking framework
admits several variations
that engines have explored.

A cursor-driven variant
uses a mouse pointer or touchscreen tap
to deliver the screen pixel
to the picking algorithm.
The variant
applies the same inverse map and hit test
as the light-gun variant
but with a software-tracked screen pixel
rather than a hardware-detected one.

A camera-based variant
uses an image sensor and a calibration light source
to track the controller's pointing direction.
The Wii Remote pairs a camera in the controller
with fixed infrared emitters on a sensor bar near the display.
The PlayStation Move pairs a camera near the display
with an illuminated orb on the controller.
The variant
translates the controller's pointed position
to a screen pixel
through a calibrated camera-to-screen transform.

A gaze-tracking variant
uses an eye-tracking camera
to determine where the player is looking
on the screen.
The pointed position
becomes the screen pixel
that the picking algorithm processes.

A motion-control variant
combines accelerometer and gyroscope data
to determine the controller's orientation
relative to a fixed forward direction.
The variant
projects the controller's orientation
onto the screen
to produce the screen pixel.

A pixel-level alpha-tested hit
samples the rendered alpha value
at the click position
to distinguish opaque from transparent sprite regions.
The variant
gives more precise hit detection
at the cost of additional texture-sampling work.

A bounding-volume-hierarchy variant
organises the visible sprites
into a spatial data structure
that accelerates the front-to-back iteration.
The variant
trades implementation complexity
for picking-iteration cost
in scenes with many sprites.

A multi-touch variant
processes multiple simultaneous touch points
through the same picking framework
applied per touch.
The variant
supports touchscreen gameplay
with multi-finger gestures.

## Delivery Mechanisms

The picking framework
permits five distinct delivery mechanisms
on period hardware.

The first is the cathode-ray-tube light gun
with hardware photodiode and raster-timing detection.
The NES Zapper,
the Super Scope,
and the arcade light-gun controllers
all use this mechanism
on cathode-ray-tube displays.

The second is mouse-driven cursor picking
on the personal computer.
The mouse driver
reports cursor screen positions
that the gameplay engine
applies to the picking algorithm.
The mechanism is the universal cursor-picking delivery
on the IBM PC and on subsequent personal computers.

The third is touchscreen tap picking
on handheld devices
including the Nintendo DS in 2004
and modern smartphones and tablets.
The touchscreen driver
reports tap positions
that the gameplay engine processes.

The fourth is camera-and-controller-based input
through image sensors and calibration light sources
that the system uses to track the controller's pointing.
The Wii Remote and the PlayStation Move
both use this mechanism
with different placements of camera and light source.

The fifth is graphics-processing-unit shader picking
on modern hardware
where a fragment shader
records the object identifier
at each screen pixel into a separate buffer
that the engine reads
to identify the picked object.
The mechanism
removes the per-object iteration
in favour of per-pixel storage.

All five mechanisms
deliver a screen pixel
to the inverse-map framework.
The choice trades hardware availability,
input-device cost,
implementation complexity,
and the achievable precision.

## Where the Framing Breaks Down

The picking framework
is insufficient
when any of the following conditions hold.

When the click falls on a sprite
whose visible pixels are partially transparent
and the engine cannot afford the pixel-level alpha test,
the bounding-box hit
may return a false positive.
The variant
must either restrict the hit detection
to clearly-opaque sprite content
or accept the false positives
as a design trade.

When multiple sprites overlap at the click position
with rapid temporal motion,
the picking decision
may flip between adjacent frames
based on the click timing.
The variant
must either lock the picking
to the gameplay tick rate
or accept the timing-dependent ambiguity.

When the projection mode
applies non-affine transformations
beyond the affine inverse that the framework supports,
the picking framework
must extend to per-pixel ray casting
that the article does not treat in detail.

When the picking must respect
the depth of the gameplay world
at sub-pixel precision,
the floating-point precision of the inverse
may become a binding constraint.
The condition number bounds
of the previous section
quantify the precision limit.

When the input device
delivers screen positions
that are themselves imprecise
through analogue noise or calibration drift,
the picking precision
is limited by the input device
rather than by the inverse map.
The variant
must include input-device error modelling
that the article does not treat.

## The Canon

The following games
use specific picking techniques
that distinguish their gameplay
or that became canonical for the subgenre.

[Operation Wolf][ref_operation_wolf]
in the arcade in 1987
gave the medium
its canonical mounted-gun light-gun shooter
through the Taito arcade hardware
and the integrated gun controller.

[Operation Thunderbolt][ref_operation_thunderbolt]
in the arcade in 1988
extended the format
with cooperative two-player gameplay.

[Battle Clash][ref_battle_clash]
on the Super Nintendo Entertainment System in 1992
brought the canonical sprite-scale-and-rotate hit-test case
to the home console
through the Super Scope light gun
and the Mode 7 background-as-sprite rendering.
The hit-detection cartridge code
is the canonical implementation
of the inverse map framework
in the engineering tradition.

[Metal Combat, Falcon's Revenge][ref_metal_combat]
on the same console in 1993
extended the Battle Clash formula
with additional enemy types and gameplay scenarios.

[The House of the Dead][ref_house_of_the_dead]
in the arcade in 1996
combined three-dimensional polygon rendering
with light-gun targeting
in the survival-horror format.
The hit-detection algorithm
applied per-polygon ray-mesh intersection
that the modern three-dimensional picking framework subsumes.

Each game in the canon
exercises a specific picking technique
that the projection mode and the gameplay
together impose on the engine.

## Out of Scope

The article does not cover
the following.

The full three-dimensional picking framework
through ray-mesh intersection
on arbitrary polygon meshes
is the subject of the synthesis closer of the series.
The article presents picking
in its two-dimensional and pseudo-three-dimensional forms
that the previous clusters covered.

The full input-device-error modelling
that accounts for analogue noise,
calibration drift,
and player-skill variability
is gameplay-systems territory
that the article does not treat.

The shader programming techniques
for graphics-processing-unit shader picking
including the object-identifier buffer
and the per-pixel readback
are implementation concerns
adjacent to but distinct from
the projection math.

The full alpha-test framework
including premultiplied alpha,
alpha-to-coverage,
and order-independent transparency
is rendering territory
that the article treats only at the level
of the sprite-local alpha sampling.

The hardware design of the cathode-ray-tube light gun
including the photodiode characteristics
and the raster-timing synchronisation circuits
is hardware-design territory
that the article treats only at the level
of the delivery-mechanism sidebar.

## Conclusion

The picking and hit-testing framework
gathers the inverse-map material
of the previous projection-mode articles
into a single cross-cutting treatment.
The framework
distinguishes the three disambiguation strategies
that the inverse map admits,
treats the numerical stability of the inverse
through the condition number $\kappa(A)$,
gives the area-scaling interpretation of the determinant $|\det(A)|$,
treats the canonical sprite-scale-and-rotate hit test
$\mathbf{p}_{\text{local}} = (1/s) R(-\theta) (\mathbf{p}_{\text{screen}} - \mathbf{c})$
that Battle Clash and Metal Combat used
for the Super Scope light-gun gameplay,
and discusses light-gun picking
as the historical realisation
of the abstract picking operation.
The remaining article in the series
treats the camera as a linear operator
in the synthesis closer
that subsumes the two-dimensional projection modes
of the previous clusters
into the projective generalisation
of the three-dimensional rendering pipeline.

## References

- [Reference, Battle Clash][ref_battle_clash]
- [Reference, Metal Combat, Falcon's Revenge][ref_metal_combat]
- [Reference, NES Zapper][ref_zapper]
- [Reference, Operation Thunderbolt][ref_operation_thunderbolt]
- [Reference, Operation Wolf][ref_operation_wolf]
- [Reference, The House of the Dead][ref_house_of_the_dead]

[ref_battle_clash]: https://en.wikipedia.org/wiki/Battle_Clash
[ref_house_of_the_dead]: https://en.wikipedia.org/wiki/The_House_of_the_Dead_(video_game)
[ref_metal_combat]: https://en.wikipedia.org/wiki/Metal_Combat:_Falcon%27s_Revenge
[ref_operation_thunderbolt]: https://en.wikipedia.org/wiki/Operation_Thunderbolt_(video_game)
[ref_operation_wolf]: https://en.wikipedia.org/wiki/Operation_Wolf
[ref_zapper]: https://en.wikipedia.org/wiki/NES_Zapper
