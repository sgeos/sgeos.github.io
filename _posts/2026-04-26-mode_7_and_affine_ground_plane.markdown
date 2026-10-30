---
layout: post
mathjax: true
comments: true
title:  "Mode 7 and the Affine Ground Plane"
date:   2026-04-26 09:00:00 +0000
categories: games graphics projection
series: two_dimensional_projection
series_title: Two-Dimensional Projection in Games
series_index: 9
---
<!-- A181 -->
<script>console.log("A181");</script>

The opening article of the affine-and-projective cluster
treats the Mode 7 graphics feature
of the Super Nintendo Entertainment System.
Mode 7 provides hardware-accelerated affine transformation
of a single tile-based background layer.
The hardware applies a two-by-two matrix
per rendered scanline,
with the matrix updated during the horizontal-blank interval
that separates one scanline from the next.
By updating the matrix per scanline,
the engine produces the appearance
of a flat ground plane
viewed in perspective from above.
The Mode 7 ground plane
became the canonical pseudo-three-dimensional rendering technique
on sixteen-bit hardware
and the visual signature
of the racing,
flight,
and cinematic genres
on the Super Nintendo Entertainment System.

The trick is not true three-dimensional rendering.
Mode 7 transforms a single two-dimensional texture
that the engine treats as a ground plane,
rather than projecting genuinely three-dimensional geometry.
The illusion of depth
arises from the per-scanline scaling
that the affine matrix encodes.
Distant scanlines toward the horizon
use a small scale that makes the texture appear far.
Near scanlines toward the bottom of the screen
use a large scale that makes the texture appear close.
The continuous scale gradient
across the rendered frame
gives the player the impression of looking forward
at a ground plane that recedes into the distance.

The article frames Mode 7
as a perspective-approximating affine projection
where the affine matrix
is modulated per scanline
to encode the inverse-distance scaling
that true perspective projection would produce.
The Mode 7 hardware
permits arbitrary affine transforms,
including rotation and shear,
in addition to scaling.
The classical Mode 7 ground plane
combines the per-scanline scaling
with a rotation
that the player or the engine can update
to turn the apparent view.
The article works through the per-scanline matrix
in detail
and walks a concrete F-Zero-like example.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a per-scanline two-by-two affine matrix
applied as a backward sampling map
from screen coordinates to texture coordinates.
The delivery mechanism
is the Super Nintendo Entertainment System hardware
that the SNES designers built specifically for the technique,
the horizontal-blank interrupt
that the engine uses to update the matrix per scanline,
and the software emulation
that other contemporary systems used
to approximate the same effect
through central-processing-unit cycles.

## A Brief History of the Mode

The Super Nintendo Entertainment System launched
in Japan in November 1990
and in North America in August 1991.
The hardware shipped with eight background-rendering modes
numbered zero through seven,
of which Mode 7 was the only one
to support per-scanline affine transformation
of the single background layer.
The mode trades the multiple-background-layer capability
of modes zero through six
for hardware-accelerated transformation
of one background layer.

The Mode 7 launch titles
demonstrated the technique
across multiple game genres.
[F-Zero][ref_f_zero]
from Nintendo in 1990
gave the medium
its canonical Mode 7 racing game.
The player piloted a futuristic anti-gravity vehicle
at high speed around a banked track
rendered as a Mode 7 ground plane
that rotated with the player's steering input.
The Mode 7 ground plane
gave the track its apparent depth
and the rotation gave the player's view its responsiveness.

[Pilotwings][ref_pilotwings]
from Nintendo in 1990
gave the medium
its canonical Mode 7 flight simulator.
The player flew a hang glider,
a small aeroplane,
or a parachuting figure
across a Mode 7 landscape
that tilted and rotated
as the player manoeuvred.
Pilotwings demonstrated
the full Mode 7 affine capability
including tilt simulation
through per-scanline matrix variation
that exceeded the canonical ground-plane formulation.

[Super Castlevania IV][ref_castlevania_4]
from Konami in 1991
applied Mode 7 to dramatic environmental rotation effects
within an otherwise side-scrolling platformer.
The rotating room sequences
displayed the Mode 7 hardware's general affine capability
beyond the ground-plane formulation
of the racing and flight genres.

[ActRaiser][ref_actraiser]
from Quintet and Enix in 1990
combined a side-scrolling action mode
with a top-down strategy mode
that used Mode 7 rotation
to convey movement across the world map.
The strategy sections
demonstrated Mode 7 as a navigational aid
rather than only as a perspective effect.

[Super Mario Kart][ref_super_mario_kart]
from Nintendo in 1992
extended the F-Zero racing formula
into the kart racing subgenre
that the title established.
The Mode 7 track
combined per-scanline scaling
with track-aligned scrolling
and sprite-based opponents.
The Super Mario Kart visual style
defined the kart racing subgenre
for two decades.

[Final Fantasy VI][ref_ff6]
from Square in 1994
used Mode 7
for the airship cinematic sequences
that book-ended the major plot beats of the game.
The airship sequences
combined Mode 7 ground plane
with sprite-based cloud and structure overlays
to give the player a sense of cinematic movement.
The airship visual style
became the template
for cinematic interludes
in subsequent Square role-playing games.

The technique persists
in modern indie and retro releases
through software emulation
of the Mode 7 algorithm
on hardware that lacks the original chip support.
Modern graphics-processing-unit pipelines
render the equivalent effect
through true perspective projection
of a textured ground plane,
which produces a visually similar result
through different mathematics.

## The Forward Map

The Mode 7 hardware
works through backward sampling
rather than through a forward map.
The renderer iterates over screen pixels
and computes the texture coordinate
to sample at each pixel.
The article therefore treats the backward map
as the primary equation
and derives the forward map
as the inverse where needed.

The world model
is a single two-dimensional ground plane
at vertical world coordinate $w_y = w_y^{\text{ground}}$
in the $y$-down convention
of the previous articles.
The ground plane carries a texture
that the engine treats as the world content.
World positions on the ground
are described by the two coordinates
$(w_x, w_z)$
giving the lateral and depth coordinates respectively.
The camera position is a three-dimensional world coordinate
$\mathbf{c} = (c_x, c_y, c_z)$
with the camera height above the ground
given by

$$
h = w_y^{\text{ground}} - c_y > 0.
\tag{1}
$$

The camera looks forward at the horizon
along the world $w_z$ axis
with a yaw rotation angle $\theta$
that the player or the engine can update.
The screen coordinate is a two-dimensional pixel position
$\mathbf{p}\_{\text{screen}} = (s_x, s_y)$
with $W$ and $H$ the screen width and height in pixels.
The focal length $f$
is a positive scalar in pixels
that the engine chooses
to set the field of view.
The horizontal field of view subtended by the screen
follows from the focal length and the screen width as

$$
\mathrm{FOV} = 2\, \arctan\left( \frac{W}{2 f} \right).
\tag{2}
$$

A small focal length gives a wide field of view
and an aggressive perspective.
A large focal length gives a narrow field of view
and a flatter perspective.

The horizon screen-y $s_y^{\text{horizon}}$
is the screen row
at which the camera ray points horizontally,
parallel to the ground plane.
A pixel above the horizon
$s_y < s_y^{\text{horizon}}$
does not intersect the ground plane
and the renderer leaves it untextured.
A pixel below the horizon
$s_y > s_y^{\text{horizon}}$
intersects the ground at some finite distance from the camera.

The per-scanline scaling factor
captures the inverse-distance relationship
that perspective projection introduces.
For a pixel at screen row $s_y$
below the horizon,
the world-space depth from the camera
along the camera's forward axis
is

$$
d(s_y) = \frac{f\, h}{s_y - s_y^{\text{horizon}}}.
\tag{3}
$$

The scaling factor
that the per-scanline matrix uses
is the world distance per screen pixel
at the scanline's depth,

$$
z(s_y) = \frac{d(s_y)}{f} = \frac{h}{s_y - s_y^{\text{horizon}}}.
\tag{4}
$$

The factor is proportional to $d(s_y)$
and inversely proportional to the scanline offset from the horizon.
Distant scanlines near the horizon have large $z(s_y)$,
so one screen pixel covers many world units
and the texture content there appears compressed.
Near scanlines toward the bottom of the screen have small $z(s_y)$,
so one screen pixel covers few world units
and the texture content there appears stretched.
The continuous variation
across screen rows
produces the perspective illusion.

The per-scanline gradient of the scale factor
varies hyperbolically with the scanline offset,

$$
\frac{d\, z(s_y)}{d\, s_y} = -\frac{h}{(s_y - s_y^{\text{horizon}})^2}.
\tag{5}
$$

The gradient is large near the horizon
where the scale factor changes rapidly between adjacent scanlines
and small toward the bottom of the screen
where the scale factor changes slowly.
The engine precomputes the per-scanline matrix entries
in a lookup table
that the horizontal-blank-direct-memory-access transfer
writes to the Mode 7 registers
between scanlines.

The per-scanline affine matrix
that the Super Nintendo Entertainment System applies
combines the per-scanline scaling
with the camera-yaw rotation,

$$
M(s_y) = z(s_y)\, R(\theta) =
\frac{h}{s_y - s_y^{\text{horizon}}}
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}.
\tag{6}
$$

The matrix has four entries
that the SNES designers named
$A(s_y) = D(s_y)$ for the scaled cosine,
and $B(s_y) = -C(s_y)$ for the scaled sine,
matching the rotation-and-scale structure.
The engine updates these four entries
once per scanline
through the horizontal-blank interrupt
that fires between consecutive scanlines.

The backward map
from screen pixel to world ground position
is

$$
\begin{bmatrix} w_x - c_x \\ w_z - c_z \end{bmatrix} =
M(s_y)
\begin{bmatrix} s_x - W/2 \\ f \end{bmatrix}.
\tag{7}
$$

Written out by component,

$$
w_x = c_x + \frac{h}{s_y - s_y^{\text{horizon}}}\, \big( (s_x - W/2)\, \cos\theta - f\, \sin\theta \big),
\tag{8}
$$

$$
w_z = c_z + \frac{h}{s_y - s_y^{\text{horizon}}}\, \big( (s_x - W/2)\, \sin\theta + f\, \cos\theta \big).
\tag{9}
$$

The backward map
is the equation the SNES renderer evaluates
at every screen pixel below the horizon.
The result is the world ground position
whose texture content
the renderer samples and writes to the frame buffer.

The forward map
from world ground position to screen pixel
inverts the backward map
through the perspective relationship
that the backward map encodes.
Writing $(\tilde{w}\_x, \tilde{w}\_z)$
for the camera-frame ground coordinates,

$$
\begin{bmatrix} \tilde{w}_x \\ \tilde{w}_z \end{bmatrix} =
R(-\theta)
\begin{bmatrix} w_x - c_x \\ w_z - c_z \end{bmatrix},
\tag{10}
$$

the forward map writes as

$$
s_x = \frac{W}{2} + \frac{f\, \tilde{w}_x}{\tilde{w}_z},
\tag{11}
$$

$$
s_y = s_y^{\text{horizon}} + \frac{f\, h}{\tilde{w}_z}.
\tag{12}
$$

The forward map
contains a division by $\tilde{w}\_z$
that the affine framework of the previous articles
does not include.
The division
is the perspective denominator
that the synthesis closer of the series
treats in full generality.
Mode 7 implements the perspective denominator
for the ground plane
through the per-scanline scaling.
The depth from camera is constant across a scanline,
so the per-scanline matrix
captures the exact perspective division
for any point on the ground plane at that scanline
without requiring per-pixel division.
The technique is exact for the ground plane
and approximate only in the sense
that it cannot represent above-ground or below-ground geometry.

The Mode 7 forward map
holds only for world points on the ground plane
$w_y = w_y^{\text{ground}}$.
World content above or below the ground plane
falls outside the Mode 7 hardware's capability.
Period games typically rendered above-ground content
through the sprite hardware
overlaid on top of the Mode 7 background.

## The Inverse Map

The backward map of the previous section
is the operational inverse map
that the Mode 7 hardware computes.
Every screen pixel below the horizon
recovers a unique ground-plane world position.
Above the horizon
the backward map returns no ground intersection
and the renderer treats the pixel as sky.

The ambiguity that earlier articles treated
through known-depth or ground-plane assumptions
does not arise in Mode 7
because the world model is two-dimensional
rather than three-dimensional.
The single ground plane
gives a unique world position per pixel
without requiring a height assumption.

Picking against the Mode 7 ground plane
uses the backward map directly.
The clicked screen pixel
inverts to a unique world position
that the engine compares
against gameplay objects positioned in world coordinates.

The visible region of the world
on the ground plane
is the image of the screen rectangle below the horizon
under the backward map.
The region is a trapezoid
in the $(w_x, w_z)$ world plane,
narrow at the back near the horizon
and wide at the front near the bottom of the screen.
The trapezoid widens linearly
with the inverse of $(s_y - s_y^{\text{horizon}})$,
which is the canonical perspective foreshortening
that gives Mode 7 its visual style.

## A Worked Example

Consider an F-Zero-style Super Nintendo Entertainment System racing game
with the following parameters.
The screen is 256 pixels wide
and 224 pixels tall,
matching the Super Nintendo Entertainment System resolution.
The horizon sits at screen row $s_y^{\text{horizon}} = 80$.
The camera height above the ground is $h = 16$ world units.
The focal length is $f = 96$ pixels,
giving a horizontal field of view
$\mathrm{FOV} = 2 \arctan(128/96) \approx 106$ degrees
across the screen width.
The camera yaw is $\theta = 0$,
looking straight ahead along the world $w_z$ axis.
The camera position is $\mathbf{c} = (0, w_y^{\text{ground}} - 16, 0)$,
placing the camera at the origin
of the lateral and depth axes
with the camera height $h = 16$ above the ground.

The per-scanline scaling factor at screen row $s_y$ below the horizon is

$$
z(s_y) = \frac{16}{s_y - 80}.
\tag{13}
$$

At screen row $s_y = 100$,
just below the horizon,
$z(100) = 16/20 = 0.8$,
giving a far-field scale
where one screen pixel covers $0.8$ world units.

At the bottom of the screen $s_y = 223$,
$z(223) = 16/143 \approx 0.112$,
giving a near-field scale
where one screen pixel covers about a tenth of a world unit.

The depth from camera at each scanline is

$$
d(s_y) = \frac{f\, h}{s_y - 80} = \frac{96 \cdot 16}{s_y - 80} = \frac{1536}{s_y - 80}.
\tag{14}
$$

At $s_y = 100$, $d = 1536 / 20 = 76.8$ world units.
At $s_y = 200$, $d = 1536 / 120 = 12.8$ world units.
At $s_y = 223$, $d = 1536 / 143 \approx 10.74$ world units.

The backward map at screen pixel $(128, 100)$
with $\theta = 0$,
$\cos\theta = 1$, $\sin\theta = 0$,
gives

$$
w_x - c_x = z(100) \cdot (128 - 128) \cdot 1 = 0,
\tag{15}
$$

$$
w_z - c_z = z(100) \cdot 96 \cdot 1 = 0.8 \cdot 96 = 76.8.
\tag{16}
$$

The pixel at the centre of the screen just below the horizon
samples the world position $(0, 76.8)$,
which is $76.8$ world units forward of the camera
and matches the scanline depth $d(100) = 76.8$.

At the screen edge $(0, 100)$
with the same $\theta = 0$,

$$
w_x - c_x = 0.8 \cdot (0 - 128) \cdot 1 = -102.4,
\tag{17}
$$

$$
w_z - c_z = 0.8 \cdot 96 = 76.8.
\tag{18}
$$

The pixel at the upper-left of the visible ground
samples world position $(-102.4, 76.8)$,
which is $102.4$ units to the left of the camera
and $76.8$ units forward.

A rotation of $\theta = \pi/2$
turns the camera 90 degrees clockwise as viewed from above.
$\cos\theta = 0$, $\sin\theta = 1$,
and the per-scanline matrix becomes

$$
M(s_y) = z(s_y)
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}.
\tag{19}
$$

The pixel at the centre of the screen just below the horizon
now samples the world position

$$
w_x - c_x = 0.8 \cdot \big( 0 \cdot 0 - 96 \cdot 1 \big) = -76.8,
\tag{20}
$$

$$
w_z - c_z = 0.8 \cdot \big( 0 \cdot 1 + 96 \cdot 0 \big) = 0.
\tag{21}
$$

The same pixel now samples the world position $(-76.8, 0)$,
$76.8$ units to the left of the camera
along the original lateral axis.
The rotation has reoriented the apparent forward direction
from the original $+w_z$ axis
to the $-w_x$ axis.

The forward map verifies the round trip.
A world point at $(0, w_y^{\text{ground}}, 76.8)$
with $\theta = 0$
gives $\tilde{w}\_x = 0$, $\tilde{w}\_z = 76.8$,
and the forward map yields

$$
s_x = 128 + \frac{96 \cdot 0}{76.8} = 128,
\tag{22}
$$

$$
s_y = 80 + \frac{96 \cdot 16}{76.8} = 80 + 20 = 100.
\tag{23}
$$

The forward map returns the screen pixel $(128, 100)$
that the backward map sampled the world position from,
confirming the round-trip identity,

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
\tag{24}
$$

where $\varepsilon$ is the floating-point precision of the engine.
The identity is exact
within the affine ground-plane model.

## Variations Within the Mode

The Mode 7 framework
admits several variations
that engines have explored.

A camera-yaw variant
updates $\theta$ each frame
based on player input
or based on a scripted camera path.
F-Zero and Super Mario Kart
both use the camera-yaw variant
to allow the player
to steer the track view.
The per-scanline matrix recomputes
on every $\theta$ change.

A camera-pitch variant
introduces an additional rotation
around the lateral axis
to allow the camera to tilt forward and backward.
The variant modifies the per-scanline scaling factor
to depend on the pitch angle
in addition to the screen row.
Pilotwings uses the camera-pitch variant
to simulate the pitching of an aeroplane.

A camera-roll variant
introduces a rotation around the forward axis
to allow the camera to bank left and right.
The variant modifies the per-scanline matrix
to include a roll component.
F-Zero and Super Mario Kart use camera roll
during sharp turns
and during track banking
to give the player a feeling of vehicle dynamics.

A horizon-translation variant
moves the horizon screen row $s_y^{\text{horizon}}$
during play
to simulate the camera looking up or down.
The variant
is mathematically equivalent
to the camera-pitch variant
but is sometimes implemented as a separate parameter
for ease of authoring.

A non-uniform-scale variant
allows the per-scanline scaling factor
along the lateral and depth axes
to differ from each other,

$$
M(s_y) = z(s_y)
\begin{bmatrix} z_x \cos\theta & -z_x \sin\theta \\ z_z \sin\theta & z_z \cos\theta \end{bmatrix}.
\tag{25}
$$

The variant produces stylised perspective effects
where horizontal foreshortening differs from depth foreshortening.
Period games rarely used the non-uniform variant
because the visual asymmetry
is unusual to players accustomed to natural perspective.

A texture-scrolling variant
animates the ground texture
by scrolling the texture content
in addition to the per-scanline matrix update.
F-Zero uses the texture-scrolling variant
to suggest forward motion
when the player's forward velocity
exceeds what the camera position change alone would convey.

A ground-tile-deformation variant
modifies the per-scanline matrix
to include a banking effect
that simulates the road tilting left or right
without rotating the player's vehicle.
Super Mario Kart uses ground-tile deformation
during banked turns
to give the appearance of the kart tilting into the curve.

A pure-rotation variant
sets the scaling factor to a constant value
and varies only the rotation,
producing a flat top-down view that rotates with the player.
The variant is used in
ActRaiser and Super Castlevania IV
for navigation and dramatic effect respectively.

## Delivery Mechanisms

The Mode 7 forward map
permits four distinct delivery mechanisms
on period and modern hardware.

The first is the Super Nintendo Entertainment System Mode 7 hardware
that the SNES Picture Processing Unit provided natively.
The hardware applies the four scanline matrix entries
$A, B, C, D$
read from registers
during the rendering of each scanline.
The engine updates the registers
through horizontal-blank-direct-memory-access transfers
that fire between scanlines
without requiring central-processing-unit involvement
during the active rendering period.
The mechanism allows real-time per-scanline matrix update
at the full frame rate
without consuming central-processing-unit budget.

The second is software emulation
on contemporary sixteen-bit hardware
that lacked the SNES's affine background hardware.
The Sega Genesis,
the NEC PC Engine,
and other contemporary consoles
emulated Mode 7 effects
through software that computed the per-scanline matrix
on the central processing unit
and wrote pre-transformed tile data
into the frame buffer.
The mechanism produced visually similar results
at significant central-processing-unit cost
and at reduced frame rates
compared to the SNES's native hardware support.

The third is software composition
on a general-purpose central processing unit
on an IBM PC running the Microsoft Disk Operating System.
The personal-computer ports of SNES Mode 7 games
typically implemented the technique
through software that computed each screen pixel's
backward-mapped world coordinates
on the central processing unit.
The mechanism scaled to higher resolutions
at proportional central-processing-unit cost.

The fourth is graphics-processing-unit-accelerated perspective projection
on modern hardware.
The modern engine
renders the ground plane
as a textured polygon in three-dimensional world space
with a perspective camera transform
that produces the Mode 7 effect
through true perspective projection
rather than per-scanline affine approximation.
The graphics processing unit
handles the perspective division per pixel
through its built-in fragment shader.
The result is visually indistinguishable
from authentic Mode 7
but uses fundamentally different mathematics.

All four mechanisms
produce the appearance of a Mode 7 ground plane.
The choice trades hardware availability,
central-processing-unit budget,
implementation complexity,
and the achievable resolution and frame rate.

## Where the Framing Breaks Down

The Mode 7 framing is insufficient
when any of the following conditions hold.

When the world contains
significant above-ground or below-ground content
that the renderer must depict in true perspective,
the single ground plane of Mode 7
is insufficient.
Period games handled above-ground content
through the sprite hardware
overlaid on top of the Mode 7 background.
Modern games handle the case
through full three-dimensional rendering.

When the ground itself bends
or has elevation that varies smoothly,
the Mode 7 ground plane formulation
is insufficient
because the affine matrix
encodes a flat ground plane only.
The sprite-scaling article later in the series
treats the related case
of pseudo-three-dimensional sprite scaling
on hardware without Mode 7 support.

When the gameplay requires
camera positions and orientations
beyond the canonical above-ground forward-looking setup,
the Mode 7 backward map
loses its perspective accuracy.
Pilotwings already pushed the boundaries
of what Mode 7 could handle
through its tilt and roll variants.
Games beyond Pilotwings's flexibility
typically migrated to true three-dimensional rendering.

When the player must interact
with three-dimensional geometry
beyond the ground plane
through gameplay actions such as flying obstacles,
the Mode 7 framework
is insufficient.
The sprite-based overlay system
that Period Mode 7 games used
adds limited three-dimensional gameplay
but does not extend the Mode 7 math.

When the rendering must scale
to a resolution beyond what the SNES hardware supports,
the modern graphics-processing-unit pipeline
displaces the classic Mode 7 mechanism.
The graphics-processing-unit-accelerated perspective projection
mechanism above
bridges classic Mode 7
to modern three-dimensional rendering.

## The Canon

The following games
use Mode 7
as a defining visual feature.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[F-Zero][ref_f_zero]
on the Super Nintendo Entertainment System in 1990
gave the medium
its canonical Mode 7 racing game.
The high-speed banked-track gameplay
demonstrated the Mode 7 ground plane
at its visual peak.

[Pilotwings][ref_pilotwings]
on the same console in 1990
gave the medium
its canonical Mode 7 flight simulator.
The full range of Mode 7 variations
including tilt and roll
appeared in this title.

[ActRaiser][ref_actraiser]
on the same console in 1990
gave the medium
a Mode 7 strategic-map view
that combined the action-platformer mode
with a top-down strategy mode.

[Super Castlevania IV][ref_castlevania_4]
on the same console in 1991
applied Mode 7 to dramatic environmental rotation effects
within an otherwise side-scrolling platformer.

[Super Mario Kart][ref_super_mario_kart]
on the same console in 1992
extended the F-Zero racing formula
into the kart racing subgenre.
The Super Mario Kart visual style
defined the kart racing subgenre
for two decades.

[Final Fantasy VI][ref_ff6]
on the same console in 1994
used Mode 7
for the airship cinematic sequences
that book-ended the major plot beats of the game.

Each game in the canon
uses Mode 7
with a different combination of variations
appropriate to the gameplay it supports.
The forward map and the backward map
are the same equations
across the canon.

## Out of Scope

The article does not cover
the following.

True three-dimensional rendering
with a perspective camera
through a graphics-processing-unit pipeline
is the canonical modern technique
that the synthesis closer of the series treats.
Mode 7 is the affine approximation
to perspective projection
that the SNES hardware made affordable
in 1990.

Sprite scaling along the depth axis
to suggest distance-dependent object size
is the subject of the sprite-scaling article
later in the series.
The Mode 7 hardware
does not handle sprite scaling
and the sprite overlay system
of period Mode 7 games
used separate hardware support for sprite size variation.

Raycasting through a height-mapped two-dimensional grid
to produce three-dimensional-looking walls
is the subject of the raycasting article
later in the series.
Raycasting and Mode 7
produced superficially similar effects
on different hardware
through entirely different mathematics.

The full perspective generalisation
that recovers the perspective denominator
for arbitrary three-dimensional geometry
is the subject of the synthesis closer.
Mode 7 is a per-scanline approximation
to the projective synthesis.

The horizontal-blank-direct-memory-access programming
required to update the Mode 7 registers
between scanlines
is a hardware implementation detail
that the article treats only at the level
of the delivery-mechanism sidebar.

## Conclusion

Mode 7 is the Super Nintendo Entertainment System hardware feature
that provides per-scanline affine transformation
of a single background layer.
The per-scanline matrix
combines a scaling factor proportional to $h/(s_y - s_y^{\text{horizon}})$
with a yaw rotation $R(\theta)$
to produce the appearance
of a flat ground plane
viewed in perspective.
The hardware updates the matrix entries
through horizontal-blank-direct-memory-access transfers
that the engine schedules between scanlines.
The Mode 7 backward map
samples the ground texture at the world position
that the scanline matrix recovers from each screen pixel.
The forward map
contains a perspective denominator
that the per-scanline scaling approximates
within the affine projection framework.
The mode defined the racing,
flight,
and cinematic genres
on the Super Nintendo Entertainment System
through F-Zero, Pilotwings, Super Mario Kart, and Final Fantasy VI.
The next article in the cluster
treats sprite scaling
as the pre-Mode 7 lineage
of pseudo-three-dimensional rendering
that arcade hardware demonstrated
in the early 1980s.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 25 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 25, 25 are established and 0 are bespoke.
The focal length and every screen coordinate are in pixels, world positions and the camera height are in world units with $w_y$ increasing downward, so the per-scanline scale is in world units per pixel, and the yaw angle is in radians.

**Equation 1, Camera Height above the Ground.**
Under the downward vertical convention, the camera height is the ground coordinate minus the vertical camera coordinate, which must be positive.

$$
h = w_y^{\text{ground}} - c_y > 0.
\tag{1}
$$

**Equation 2, Horizontal Field of View from Focal Length.**
The horizontal field of view is twice the arctangent of half the screen width divided by the focal length.

$$
\mathrm{FOV} = 2\, \arctan\left( \frac{W}{2 f} \right).
\tag{2}
$$

**Equation 3, Ground Depth of a Scanline.**
By similar triangles, a scanline below the horizon meets the ground at a depth equal to the focal length times the camera height divided by the row offset from the horizon.

$$
d(s_y) = \frac{f\, h}{s_y - s_y^{\text{horizon}}}.
\tag{3}
$$

**Equation 4, Per-Scanline Scale Factor.**
The world distance covered by one pixel on a scanline is its ground depth divided by the focal length, inversely proportional to the row offset from the horizon.

$$
z(s_y) = \frac{d(s_y)}{f} = \frac{h}{s_y - s_y^{\text{horizon}}}.
\tag{4}
$$

**Equation 5, Gradient of the Per-Scanline Scale.**
The scale factor changes with the scanline at a rate that falls with the square of the row offset, so it changes fastest near the horizon.

$$
\frac{d\, z(s_y)}{d\, s_y} = -\frac{h}{(s_y - s_y^{\text{horizon}})^2}.
\tag{5}
$$

**Equation 6, Per-Scanline Mode 7 Matrix.**
The matrix the Super Nintendo Entertainment System applies on each scanline is the per-scanline scale times the camera yaw rotation.

$$
M(s_y) = z(s_y)\, R(\theta) =
\frac{h}{s_y - s_y^{\text{horizon}}}
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}.
\tag{6}
$$

**Equation 7, Backward Map from Pixel to Ground.**
The ground position sampled by a pixel is the camera position plus the per-scanline matrix applied to the horizontal pixel offset and the focal length.

$$
\begin{bmatrix} w_x - c_x \\ w_z - c_z \end{bmatrix} =
M(s_y)
\begin{bmatrix} s_x - W/2 \\ f \end{bmatrix}.
\tag{7}
$$

**Equation 8, Backward Map for the Lateral Ground Coordinate.**
Written out, the lateral ground coordinate combines the rotated horizontal pixel offset and focal length scaled by the per-scanline factor.

$$
w_x = c_x + \frac{h}{s_y - s_y^{\text{horizon}}}\, \big( (s_x - W/2)\, \cos\theta - f\, \sin\theta \big),
\tag{8}
$$

**Equation 9, Backward Map for the Depth Ground Coordinate.**
The depth ground coordinate combines the same two terms with the other row of the rotation.

$$
w_z = c_z + \frac{h}{s_y - s_y^{\text{horizon}}}\, \big( (s_x - W/2)\, \sin\theta + f\, \cos\theta \big).
\tag{9}
$$

**Equation 10, Camera-Frame Ground Coordinates.**
Rotating the camera-relative ground position by the negated yaw expresses it in the frame of the camera.

$$
\begin{bmatrix} \tilde{w}_x \\ \tilde{w}_z \end{bmatrix} =
R(-\theta)
\begin{bmatrix} w_x - c_x \\ w_z - c_z \end{bmatrix},
\tag{10}
$$

**Equation 11, Perspective Forward Map for Screen X.**
The horizontal screen coordinate is the screen centre plus the focal length times the camera-frame lateral coordinate divided by the camera-frame depth.

$$
s_x = \frac{W}{2} + \frac{f\, \tilde{w}_x}{\tilde{w}_z},
\tag{11}
$$

**Equation 12, Perspective Forward Map for Screen Y.**
The vertical screen coordinate is the horizon row plus the focal length times the camera height divided by the camera-frame depth, the division that makes the map projective.

$$
s_y = s_y^{\text{horizon}} + \frac{f\, h}{\tilde{w}_z}.
\tag{12}
$$

**Equation 13, Worked Per-Scanline Scale.**
With an illustrative horizon at row eighty and a camera height of sixteen units, the per-scanline scale is sixteen divided by the row offset.

$$
z(s_y) = \frac{16}{s_y - 80}.
\tag{13}
$$

**Equation 14, Worked Scanline Depth.**
With an illustrative focal length of ninety-six pixels, the scanline depth is one thousand five hundred and thirty-six divided by the row offset.

$$
d(s_y) = \frac{f\, h}{s_y - 80} = \frac{96 \cdot 16}{s_y - 80} = \frac{1536}{s_y - 80}.
\tag{14}
$$

**Equation 15, Worked Lateral Coordinate at the Screen Centre.**
At zero yaw the centre pixel of row one hundred samples zero lateral offset from the camera.

$$
w_x - c_x = z(100) \cdot (128 - 128) \cdot 1 = 0,
\tag{15}
$$

**Equation 16, Worked Depth Coordinate at the Screen Centre.**
The same pixel samples a depth of seventy-six point eight world units, matching the scanline depth.

$$
w_z - c_z = z(100) \cdot 96 \cdot 1 = 0.8 \cdot 96 = 76.8.
\tag{16}
$$

**Equation 17, Worked Lateral Coordinate at the Screen Edge.**
The left-edge pixel of the same row samples a lateral offset of minus one hundred and two point four world units.

$$
w_x - c_x = 0.8 \cdot (0 - 128) \cdot 1 = -102.4,
\tag{17}
$$

**Equation 18, Worked Depth Coordinate at the Screen Edge.**
The left-edge pixel samples the same depth as the centre pixel, since depth depends only on the scanline at zero yaw.

$$
w_z - c_z = 0.8 \cdot 96 = 76.8.
\tag{18}
$$

**Equation 19, Worked Per-Scanline Matrix at a Quarter-Turn Yaw.**
A yaw of ninety degrees turns the rotation into the quarter-turn matrix scaled by the per-scanline factor.

$$
M(s_y) = z(s_y)
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}.
\tag{19}
$$

**Equation 20, Worked Lateral Coordinate after a Quarter Turn.**
After the quarter turn the centre pixel samples a lateral offset of minus seventy-six point eight world units.

$$
w_x - c_x = 0.8 \cdot \big( 0 \cdot 0 - 96 \cdot 1 \big) = -76.8,
\tag{20}
$$

**Equation 21, Worked Depth Coordinate after a Quarter Turn.**
After the quarter turn the same pixel samples zero depth offset, the view having swung onto the lateral axis.

$$
w_z - c_z = 0.8 \cdot \big( 0 \cdot 1 + 96 \cdot 0 \big) = 0.
\tag{21}
$$

**Equation 22, Worked Forward Map for Screen X.**
Projecting the sampled ground point forward at zero yaw returns the centre column one hundred and twenty-eight.

$$
s_x = 128 + \frac{96 \cdot 0}{76.8} = 128,
\tag{22}
$$

**Equation 23, Worked Forward Map for Screen Y.**
Projecting the same point forward returns row one hundred, the row it was sampled from.

$$
s_y = 80 + \frac{96 \cdot 16}{76.8} = 80 + 20 = 100.
\tag{23}
$$

**Equation 24, Round Trip along the Ground Plane.**
For a point on the ground plane, the forward map followed by the backward map returns the original world position up to floating-point precision.

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
\tag{24}
$$

**Equation 25, Per-Scanline Matrix with Unequal Axis Scales.**
Separate lateral and depth scale factors inside the per-scanline matrix let horizontal foreshortening differ from depth foreshortening for stylised effects.

$$
M(s_y) = z(s_y)
\begin{bmatrix} z_x \cos\theta & -z_x \sin\theta \\ z_z \sin\theta & z_z \cos\theta \end{bmatrix}.
\tag{25}
$$

### Notation

- $h$, the camera height above the ground in world units
- $w_y^{\text{ground}}$, the vertical world coordinate of the ground plane
- $f$, the focal length in pixels
- $W$, the screen width in pixels
- $\mathrm{FOV}$, the horizontal field of view
- $s_y^{\text{horizon}}$, the screen row of the horizon
- $d(s_y)$, the ground depth from the camera along its forward axis at scanline $s_y$
- $z(s_y)$, the per-scanline scale factor, the world distance per screen pixel at scanline $s_y$
- $\theta$, the camera yaw angle
- $R(\theta)$, the two-dimensional rotation by the yaw angle
- $M(s_y)$, the per-scanline Mode 7 matrix
- $\tilde{w}_x$, the camera-frame lateral ground coordinate
- $\tilde{w}_z$, the camera-frame depth ground coordinate
- $z_x$, the lateral scale factor of the anisotropic variant
- $z_z$, the depth scale factor of the anisotropic variant
- $\varepsilon$, the floating-point precision of the engine

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "ActRaiser." 2026. Wikipedia. Last modified May 10, at 14:46 (UTC). [https://en.wikipedia.org/w/index.php?title=ActRaiser&oldid=1353479041][ref_actraiser]
- "F-Zero (Video Game)." 2026. Wikipedia. Last modified June 20, at 01:36 (UTC). [https://en.wikipedia.org/w/index.php?title=F-Zero\_(video\_game)&oldid=1360225771][ref_f_zero]
- "Final Fantasy VI." 2026. Wikipedia. Last modified June 9, at 19:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Final\_Fantasy\_VI&oldid=1358599300][ref_ff6]
- "Mode 7." 2026. Wikipedia. Last modified June 9, at 17:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Mode\_7&oldid=1358589212][ref_mode_7]
- "Pilotwings." 2026. Wikipedia. Last modified June 6, at 09:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Pilotwings&oldid=1358061462][ref_pilotwings]
- "Super Castlevania IV." 2026. Wikipedia. Last modified March 27, at 17:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Super\_Castlevania\_IV&oldid=1345707448][ref_castlevania_4]
- "Super Mario Kart." 2026. Wikipedia. Last modified June 26, at 18:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Super\_Mario\_Kart&oldid=1361251845][ref_super_mario_kart]

[ref_actraiser]: https://en.wikipedia.org/w/index.php?title=ActRaiser&oldid=1353479041
[ref_castlevania_4]: https://en.wikipedia.org/w/index.php?title=Super_Castlevania_IV&oldid=1345707448
[ref_f_zero]: https://en.wikipedia.org/w/index.php?title=F-Zero_(video_game)&oldid=1360225771
[ref_ff6]: https://en.wikipedia.org/w/index.php?title=Final_Fantasy_VI&oldid=1358599300
[ref_mode_7]: https://en.wikipedia.org/w/index.php?title=Mode_7&oldid=1358589212
[ref_pilotwings]: https://en.wikipedia.org/w/index.php?title=Pilotwings&oldid=1358061462
[ref_super_mario_kart]: https://en.wikipedia.org/w/index.php?title=Super_Mario_Kart&oldid=1361251845
