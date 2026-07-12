---
layout: post
mathjax: true
comments: true
title:  "Sprite-Scaling Pseudo-Three-Dimensional, the Pre-Mode 7 Lineage"
date:   2026-04-27 09:00:00 +0000
categories: games graphics projection
series: two_dimensional_projection
series_title: Two-Dimensional Projection in Games
series_index: 10
---
<!-- A182 -->
<script>console.log("A182");</script>

The second article of the affine-and-projective cluster
treats sprite scaling
as a pseudo-three-dimensional rendering technique.
A sprite is a two-dimensional bitmap
that the engine renders at a scaled size
on the screen.
Sprite scaling
multiplies the bitmap dimensions
by a per-sprite factor
that the engine computes
from the sprite's depth from the camera.
A sprite further from the camera
appears smaller.
A sprite closer to the camera
appears larger.
The continuous depth-to-size relationship
produces a perspective illusion
that hardware-supported scaling
makes affordable at real-time frame rates.

The technique pre-dates the Mode 7 affine background of the previous article
by nearly a decade.
The Sega Super Scaler arcade boards
of the mid-1980s
demonstrated sprite scaling
through Space Harrier,
Out Run,
After Burner,
and Galaxy Force II.
The home console adoption
arrives with the Super Nintendo Entertainment System Mode 7 background hardware
repurposed as a single rotating-and-scaling sprite,
which Battle Clash and Metal Combat used
for the giant enemy mecha
in their Super Scope light-gun gameplay.
The arcade lineage
ran in parallel with
and informed the development of
the home console hardware
that the previous article treated.

The article frames sprite scaling
as a per-sprite affine transformation
that combines a scaling factor
with a sprite-plane rotation.
The forward map
takes a sprite-local pixel coordinate
to a screen pixel coordinate
through the combined transform.
The inverse map
returns to the sprite-local frame
for picking and hit-test purposes.
The inverse map is the canonical case
for the light-gun targeting
in the Battle Clash and Metal Combat lineage
that the cross-cutting picking article treats in detail later in the series.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a per-sprite affine transform
parameterised by a scaling factor and a rotation angle.
The delivery mechanism
chooses how the engine
computes the per-sprite scaling factor
and how the hardware
applies the scaling and rotation
during sprite rendering.

## A Brief History of the Mode

The earliest commercial sprite-scaling game
is widely cited as
[Pole Position][ref_pole_position]
from Namco in 1982.
The arcade game rendered
roadside billboards,
opposing race cars,
and the road itself
through pre-scaled sprite frames
that the hardware swapped
based on the car's distance from the player.
The pre-scaled approach
used a sprite atlas
at multiple discrete sizes
rather than continuous scaling,
but the visual effect
was the canonical depth-by-size pseudo-three-dimensional rendering
that subsequent games inherited.

The Sega Super Scaler arcade boards
of the mid-1980s
brought hardware-supported continuous sprite scaling
to commercial games.
[Space Harrier][ref_space_harrier]
from Sega in 1985
rendered hundreds of enemies
across a flying-through-a-world setting
through hardware sprite scaling
that the Super Scaler boards provided.
The technical achievement
was the simultaneous rendering of many sprites
at independent scaling factors
that the arcade hardware computed in real time.

[Out Run][ref_outrun]
from Sega in 1986
applied Super Scaler sprite scaling
to a driving game
across a continuous landscape.
The hilly roads and roadside scenery
all rendered through sprite scaling
that the hardware updated per-sprite per-frame.
Out Run became the visual template
for arcade driving games
through the late 1980s.

[After Burner][ref_after_burner]
from Sega in 1987
applied the same hardware
to a flight simulator
where the player piloted a jet fighter
through formation enemies
that the Super Scaler boards rendered.
[Galaxy Force II][ref_galaxy_force_ii]
from Sega in 1988
pushed the Super Scaler hardware further
through cinematic terrain
and large boss enemies
that demonstrated the upper limit
of pre-three-dimensional arcade rendering.

The home console era
adopted sprite scaling
through the Super Nintendo Entertainment System Mode 7 background hardware
of the previous article,
repurposed as a single large rotating-and-scaling sprite.
[Battle Clash][ref_battle_clash]
from Nintendo and Intelligent Systems in 1992
rendered each giant enemy mecha as a Mode 7 background,
treating the affine-background hardware
as a single sprite under software control.
The cartridge software
computed the Mode 7 matrix entries
per frame
based on the gameplay state.
The result was a Super Scope light-gun shooter
with rotating, scaling, and translating enemy sprites
that the player aimed at and shot.

[Metal Combat, Falcon's Revenge][ref_metal_combat]
from Nintendo and Intelligent Systems in 1993
extended the Battle Clash formula
with additional enemy types
and gameplay scenarios
through the same Mode 7 background-as-sprite technique.

[Yoshi's Safari][ref_yoshis_safari]
from Nintendo in 1993
combined a Mode 7 ground-and-environment background
with standard sprite hardware
to render a first-person Super Scope shooter
across pre-rendered cartoon environments.
The Mode 7 background advanced toward the player on rails
while sprite enemies at various pre-rendered sizes
appeared at corresponding depths.

The technique continues
in modern indie and retro releases
that emulate the arcade aesthetic
through software sprite scaling
or graphics-processing-unit shader scaling
that produces the same visual effect
through different mathematics.

## The Forward Map

A sprite is a two-dimensional bitmap
of width and height
$w_{\text{sprite}}$ and $h_{\text{sprite}}$
in sprite-local pixel coordinates.
The sprite-local coordinate system
has its origin
at the sprite's anchor point,
which is typically the centre of the sprite
or the bottom-centre
for ground-aligned characters.
A pixel of the sprite
has the local-frame position

$$
\mathbf{p}_{\text{local}} = (u, v),
$$

with $u$ and $v$ ranging over the sprite's pixel extent.

The sprite has a world position
$\mathbf{p}_{\text{world}}^{\text{sprite}} = (w_x, w_y, w_z)$
in the $y$-down convention
of the previous articles.
The camera is at world position
$\mathbf{c}_{\text{camera}} = (c_x, c_y, c_z)$
and looks forward along the world $w_z$ axis.
The depth from the camera to the sprite is

$$
d = w_z - c_{\text{camera},z} > 0.
$$

The focal length $f$
gives the per-world-unit-of-depth screen scaling at the camera's unit-distance plane,
as in the previous article.

The sprite scaling factor
is the inverse-depth ratio of focal length to depth,

$$
s = \frac{f}{d}.
$$

A sprite at depth $f$
renders at unit scale
with one sprite-local pixel
covering one screen pixel.
A sprite at depth $2f$
renders at half scale
with one sprite-local pixel
covering half a screen pixel.
A sprite at depth $f/2$
renders at double scale.

The sprite's screen-space anchor position
follows from the perspective projection of the previous article,

$$
\mathbf{c} = \left( \frac{W}{2} + s\, (w_x - c_{\text{camera},x}),\ s_y^{\text{horizon}} + s\, (w_y - c_{\text{camera},y}) \right).
$$

The point $\mathbf{c}$ is the screen position
of the sprite's anchor pixel
under the perspective camera.

The sprite has an orientation angle $\theta$
in the sprite-local plane,
which the engine updates each frame
to track the sprite's gameplay rotation.
The sprite-plane rotation matrix is

$$
R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}.
$$

The forward map
takes a sprite-local pixel coordinate
to a screen pixel coordinate
through the scaling and rotation,

$$
\mathbf{p}_{\text{screen}} = \mathbf{c} + s\, R(\theta)\, \mathbf{p}_{\text{local}}.
$$

The forward map applies the rotation
to the local-frame coordinate,
scales the rotated coordinate by $s$,
and translates by the sprite anchor's screen position $\mathbf{c}$.
The composition of scaling and rotation
is a two-by-two matrix
that the engine writes once per sprite per frame.

The Jacobian of the forward map
with respect to the sprite-local coordinates
is the matrix

$$
J = s\, R(\theta),
$$

with determinant

$$
\det J = s^2.
$$

The screen-space area
that the sprite covers
follows from the determinant as

$$
A_{\text{screen}} = s^2\, A_{\text{local}}.
$$

A sprite at twice the unit distance
covers a quarter of the screen-space area
of the same sprite at unit distance,
because $s$ halves and $s^2$ quarters.
The quadratic area law
is the canonical perspective foreshortening
applied to a finite sprite.

The factorisation pattern
from the opener
extends to the sprite-scaling case
as a composition of scaling, rotation, and translation,

$$
F_{\text{sprite}} = T(\mathbf{c})\, S(s)\, R(\theta).
$$

The composition acts on the sprite-local coordinate
to produce the screen coordinate.

## The Inverse Map

The forward map's matrix $sR(\theta)$
is a uniform scaling followed by rotation,
and is invertible
whenever $s > 0$.
The inverse map
returns to the sprite-local frame
as

$$
\mathbf{p}_{\text{local}} = \frac{1}{s}\, R(-\theta)\, (\mathbf{p}_{\text{screen}} - \mathbf{c}).
$$

The inverse undoes the translation,
the rotation,
and the scaling
in reverse order.
The inverse is single-valued
within a single sprite
because the per-sprite forward map
is bijective on the sprite's screen-space region.

Hit-testing for a click against a sprite
is the dominant use of the inverse map.
The engine takes the clicked screen pixel,
applies the per-sprite inverse,
and tests whether the recovered sprite-local pixel
falls within the sprite's local pixel rectangle,

$$
|u| \le w_{\text{sprite}}/2,\quad |v| \le h_{\text{sprite}}/2.
$$

The test succeeds if the click hits the sprite,
and fails otherwise.
The bounding-box test
is the simplest sprite hit test
and uses no information beyond the sprite's local extent.
A more refined test
samples the sprite's alpha or palette index
at $(u, v)$
to test against the sprite's transparent regions.

Picking a sprite from a stack
of overlapping sprites
follows the topmost-in-draw-order convention
of the belt-scroll and oblique articles.
The engine iterates the visible sprites
in front-to-back draw order
and returns the first sprite
whose inverse-mapped click pixel
falls within the sprite's local rectangle.
For sprites at distinct depths,
the front-to-back order
matches the increasing scaling factor $s$,
so the engine effectively returns
the sprite at the largest $s$
that the click intersects.

The Battle Clash and Metal Combat light-gun targeting
is the canonical use of the sprite inverse map.
The player aims the Super Scope light gun
at a screen pixel
that the SNES reports to the cartridge software.
The cartridge code
iterates the visible enemies,
applies the per-sprite inverse map
that the current Mode 7 matrix entries define,
and identifies which enemy the player hit.
The cross-cutting picking article later in the series
treats the full Battle Clash hit-test framework
including damage modelling
and multi-sprite enemy decomposition.

The visible region
that a sprite occupies on screen
is the image of the sprite's local rectangle
under the forward map.
The region is a rotated rectangle
with side lengths
$s\, w_{\text{sprite}}$ and $s\, h_{\text{sprite}}$
at orientation $\theta$.
For an axis-aligned sprite at $\theta = 0$,
the screen-space rectangle simplifies to

$$
\mathbf{p}_{\text{screen}}^{\text{sprite-extent}} \in \mathbf{c} + \left[ -\tfrac{s\, w_{\text{sprite}}}{2},\ \tfrac{s\, w_{\text{sprite}}}{2} \right] \times \left[ -\tfrac{s\, h_{\text{sprite}}}{2},\ \tfrac{s\, h_{\text{sprite}}}{2} \right].
$$

The renderer clips world content
to the visible region
when culling for rendering.

## A Worked Example

Consider a Super Nintendo Entertainment System Super Scope light-gun shooter
with the following parameters.
The screen is 256 pixels wide
and 224 pixels tall.
The focal length is $f = 100$ pixels.
The horizon sits at $s_y^{\text{horizon}} = 112$,
the screen vertical centre.
The camera position is $\mathbf{c}_{\text{camera}} = (0, 0, 0)$,
looking forward along the world $w_z$ axis.

A sprite is a 64-by-32-pixel enemy mecha
at sprite-local pixel extent
$|u| \le 32$, $|v| \le 16$.
The mecha's world position is
$\mathbf{p}_{\text{world}}^{\text{sprite}} = (15, 0, 50)$,
15 units to the right of the camera
on the horizon line
at depth 50 units.

The depth from camera is $d = 50$.
The scaling factor is

$$
s = \frac{100}{50} = 2.
$$

The sprite anchor on screen is

$$
\mathbf{c} = (128 + 2 \cdot 15,\ 112 + 2 \cdot 0) = (158, 112).
$$

The sprite has orientation $\theta = \pi/6$,
matching a 30-degree clockwise rotation.
$\cos(\pi/6) = \sqrt{3}/2 \approx 0.866$,
$\sin(\pi/6) = 1/2$.

The sprite's top-right corner
at sprite-local position $\mathbf{p}_{\text{local}} = (32, -16)$
maps to screen position

$$
\mathbf{p}_{\text{screen}} = (158, 112) + 2
\begin{bmatrix} 0.866 & -0.5 \\ 0.5 & 0.866 \end{bmatrix}
\begin{bmatrix} 32 \\ -16 \end{bmatrix}.
$$

Computing the matrix-vector product,

$$
\begin{bmatrix} 0.866 \cdot 32 - 0.5 \cdot (-16) \\ 0.5 \cdot 32 + 0.866 \cdot (-16) \end{bmatrix} =
\begin{bmatrix} 27.7 + 8 \\ 16 - 13.9 \end{bmatrix} =
\begin{bmatrix} 35.7 \\ 2.1 \end{bmatrix}.
$$

Scaling by $s = 2$ gives $(71.4,\ 4.2)$.
The top-right corner's screen position is

$$
\mathbf{p}_{\text{screen}} = (158 + 71.4,\ 112 + 4.2) = (229.4,\ 116.2).
$$

A second mecha sprite at depth 100
has $s = 100/100 = 1$.
At the same world horizontal offset,
its screen anchor is at $(128 + 15, 112) = (143, 112)$.
Its sprites cover half the screen area
of the first mecha
because the squared scaling factor ratio is $1/4$.

A click at screen pixel $(229, 116)$
falls within the first mecha's screen-space region.
The inverse map applied at $\theta = \pi/6$ and $s = 2$
gives

$$
\mathbf{p}_{\text{local}} = \frac{1}{2}
\begin{bmatrix} 0.866 & 0.5 \\ -0.5 & 0.866 \end{bmatrix}
\begin{bmatrix} 229 - 158 \\ 116 - 112 \end{bmatrix} =
\frac{1}{2}
\begin{bmatrix} 0.866 \cdot 71 + 0.5 \cdot 4 \\ -0.5 \cdot 71 + 0.866 \cdot 4 \end{bmatrix}.
$$

Computing,

$$
\begin{bmatrix} 61.5 + 2 \\ -35.5 + 3.5 \end{bmatrix} =
\begin{bmatrix} 63.5 \\ -32 \end{bmatrix},
$$

and dividing by 2 gives $(31.8,\ -16)$.

The inverse-mapped click
is at sprite-local position $(31.8, -16)$,
which lies within the sprite's local rectangle
$|u| \le 32$, $|v| \le 16$.
The bounding-box test succeeds
and the engine reports a hit on the first mecha.

The round-trip identity holds within a sprite,

$$
F_{\text{sprite}}^{-1}(F_{\text{sprite}}(\mathbf{p}_{\text{local}})) = \mathbf{p}_{\text{local}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

The Y-sort criterion of the belt-scroll and oblique articles
extends to sprite scaling
through the back-to-front comparison
on the sprite's depth from the camera.
The criterion writes as a comparison inequality
on the depths
and equivalently on the scaling factors,

$$
\text{draw } i \text{ before } j \iff d_i > d_j \iff s_i < s_j.
$$

A sprite at smaller world depth $w_z$
has a larger scaling factor $s$
and renders in front of sprites at larger depth.
The Y-sort
under sprite scaling
matches the depth-based sort
that perspective projection introduces.

## Variations Within the Mode

The sprite-scaling framework
admits several variations
that engines have explored.

A discrete-scale variant
quantises the scaling factor $s$
to a small set of values,
matching the available sprite-atlas sizes
that the hardware can store.
The variant approximates continuous scaling
through a small set of pre-rendered sprite frames.
Pole Position used the discrete-scale variant
because the early-1980s arcade hardware
could not support continuous scaling.

A continuous-scale variant
permits arbitrary $s$
through hardware-supported scaling
or through software scaling
that interpolates the sprite bitmap
at the target screen size.
The Sega Super Scaler boards
supported continuous scaling.

A discrete-rotation variant
quantises the rotation angle $\theta$
to a small set of values,
typically eight or sixteen evenly-spaced angles,
and uses a pre-rendered sprite atlas
for each angle.
The variant trades sprite memory
for runtime rotation cost.

A continuous-rotation variant
permits arbitrary $\theta$
through hardware-supported rotation
or through software bitmap rotation.
The Mode 7 background hardware in Battle Clash
supported continuous rotation
of the giant enemy mecha sprite
through per-frame matrix update
that the cartridge software computed.

A pseudo-three-dimensional-orientation variant
extends the rotation to three axes
including pitch and roll
in addition to the screen-plane yaw $\theta$.
The variant requires pre-rendered sprite atlases
covering the three-axis rotation space
or software bitmap warping
that the engine performs at render time.
After Burner and Galaxy Force II
used pre-rendered atlases
for pitch and roll variations of enemy aircraft.

A non-uniform-scale variant
permits independent scaling factors
along the sprite-local $u$ and $v$ axes,

$$
\mathbf{p}_{\text{screen}} = \mathbf{c} +
\begin{bmatrix} s_u & 0 \\ 0 & s_v \end{bmatrix}
R(\theta)\, \mathbf{p}_{\text{local}}.
$$

The variant produces squashed or stretched sprites
that the designer might use for visual effects
such as compression on impact
or directional stretch during fast motion.

A perspective-tilted-sprite variant
applies a full perspective transformation
to a flat sprite quad
so the sprite appears as a tilted rectangle in three-dimensional space.
The variant departs from the affine framework of this article
into the projective generalisation
that the synthesis closer of the series treats.
Modern graphics-processing-unit pipelines
implement this variant
through textured-quad rendering with perspective camera transforms.

A row-by-row sprite distortion variant
modifies the sprite scaling factor
per row of the sprite
to simulate three-dimensional sprite geometry
such as cylinders or spheres
that the bitmap alone cannot represent.
Period games rarely used the row-by-row variant
because the central-processing-unit cost
exceeded what most games could afford.

## Delivery Mechanisms

The sprite-scaling forward map
permits five distinct delivery mechanisms
on period hardware.

The first is dedicated arcade sprite-scaling hardware.
The Sega Super Scaler boards
of the mid-1980s
provided hardware-supported continuous sprite scaling
through dedicated graphics chips
that handled hundreds of sprites at independent scaling factors per frame.
Space Harrier, Out Run, After Burner, and Galaxy Force II
all ran on Super Scaler hardware.
The mechanism trades dedicated hardware cost
for the highest sprite throughput
of any technique in the period.

The second is cartridge coprocessor chips
on home console cartridges.
The Capcom CX4 chip
in Mega Man X2 in 1994
and Mega Man X3 in 1995
performed runtime scaling and rotation arithmetic
that the standard SNES sprite hardware
could not compute on its own.
The CX4 returned per-sprite screen positions
and orientation parameters
that the Super Nintendo Entertainment System Picture Processing Unit
applied during sprite rendering.
The Super FX chip
in Star Fox in 1993
and subsequent titles
provided polygon-rendering computations
that included sprite scaling
for various game elements.
The mechanism trades cartridge cost
for capabilities exceeding the standard console hardware.

The third is software sprite scaling
on a general-purpose central processing unit.
The engine computes the scaling factor $s$
and the rotation angle $\theta$
per sprite per frame
and applies the affine transform
to the sprite bitmap
through software pixel-by-pixel interpolation.
The mechanism was the universal delivery
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s
and on the early home computers
that lacked dedicated sprite-scaling hardware.
Modern independent-game engines
that emulate the classic sprite-scaling aesthetic
typically use software scaling
through the central-processing-unit
or through graphics-processing-unit shader passes.

The fourth is background-layer-as-sprite
using affine background hardware
to render a single large sprite.
The Super Nintendo Entertainment System Mode 7 background
of the previous article
could be repurposed
as a single large rotating-and-scaling sprite
for cinematic effects.
Final Fantasy VI used the technique
for the airship sequences
that combined a Mode 7 ground plane
with a Mode-7-rendered airship sprite
that the engine treated as a single large sprite
rather than as a ground texture.
The mechanism extends the Mode 7 capability
to objects above or below the ground plane.

The fifth is pre-rendered sprite atlases
at multiple discrete sizes and orientations.
The engine pre-renders the sprite bitmap
at each combination of scaling factor and rotation angle
that the gameplay might require
and stores the result as a sprite atlas
indexed by the gameplay parameters.
The runtime renderer
selects the appropriate atlas frame
without computing the forward map per pixel
because the sprite frame already encodes the scaling and rotation.
Pole Position used pre-rendered atlases
across multiple discrete sizes.
After Burner used pre-rendered atlases
across multiple rotation angles in addition.
The mechanism trades sprite-atlas storage
for runtime computational cost.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades hardware cost,
sprite-atlas storage,
central-processing-unit budget,
the maximum sprite count per frame,
and the achievable continuous-scale resolution.

## Where the Framing Breaks Down

The sprite-scaling framing is insufficient
when any of the following conditions hold.

When the sprite represents
a genuinely three-dimensional object
with visible internal structure
that varies with viewing angle,
the two-dimensional sprite bitmap
is insufficient.
Pre-rendered atlases at multiple angles
cover the case partially.
The synthesis closer of the series
treats the full projective rendering
that handles three-dimensional geometry
without atlas pre-rendering.

When the sprite must depict
true perspective foreshortening
within its own extent,
the affine scaling of this article
is insufficient.
A long object such as a road sign
should foreshorten near-end-large to far-end-small
within the sprite,
which the uniform scaling factor $s$ cannot produce.
The perspective-tilted-sprite variant above
addresses this case
through full projective rendering.

When many sprites at distinct depths
must render simultaneously,
the per-sprite forward map
imposes a per-sprite cost
that the hardware budget may not afford.
The Sega Super Scaler boards
addressed this through dedicated hardware
that could support hundreds of sprites at once.
Hardware without comparable support
must reduce the visible sprite count
or accept a lower frame rate.

When the gameplay requires the player
to interact with sprite-internal geometry
beyond the rectangular bounding box,
the affine sprite-scaling framework
provides only the inverse map for the bounding rectangle.
The cross-cutting picking article later in the series
treats the inverse for sprite-local pixel-level hit testing
that respects transparency
and per-pixel sprite shape.

When the sprite must occlude or be occluded by
a Mode 7 ground plane or a tilemap background,
the depth-buffer-aware sort
that modern hardware provides
displaces the manual Y-sort
that period sprite-scaling games used.

## The Canon

The following games
use sprite scaling
as their primary pseudo-three-dimensional technique.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Pole Position][ref_pole_position]
in the arcade in 1982
gave the medium
its first commercially-released sprite-scaling pseudo-three-dimensional racing game.
The pre-rendered scaled-sprite atlases
became the visual template
for arcade racing for the next decade.

[Space Harrier][ref_space_harrier]
in the arcade in 1985
gave the medium
its first hardware-continuous-scaling action shooter
through the Sega Super Scaler boards.
The high sprite throughput
demonstrated what dedicated arcade hardware
could deliver in the era.

[Out Run][ref_outrun]
in the arcade in 1986
applied Super Scaler hardware
to a driving game
across a continuous landscape
that became the visual standard
for arcade driving through the late 1980s.

[After Burner][ref_after_burner]
in the arcade in 1987
combined sprite scaling
with pre-rendered pitch and roll atlases
for a flight simulator
that the Super Scaler hardware could drive.

[Galaxy Force II][ref_galaxy_force_ii]
in the arcade in 1988
demonstrated the upper limit
of pre-three-dimensional arcade rendering
through cinematic terrain
and large boss enemies.

[Battle Clash][ref_battle_clash]
on the Super Nintendo Entertainment System in 1992
brought the Mode 7 background-as-sprite technique
to a Super Scope light-gun shooter.
The rotating-and-scaling enemy mecha
became the canonical case
for the sprite inverse map
that the cross-cutting picking article treats later in the series.

[Metal Combat, Falcon's Revenge][ref_metal_combat]
on the same console in 1993
extended the Battle Clash formula
with additional enemy types
and gameplay scenarios
through the same Mode 7 background-as-sprite technique.

[Yoshi's Safari][ref_yoshis_safari]
on the same console in 1993
combined a Mode 7 ground-and-environment background
with standard pre-rendered sprite atlases
for the enemies
in a first-person Super Scope shooter
across pre-rendered cartoon environments.

Each game in the canon
uses sprite scaling
with a different combination
of variation choices
appropriate to the gameplay it supports.

## Out of Scope

The article does not cover
the following.

True three-dimensional polygon rendering
of the kind that Star Fox
and later Super FX titles introduced
is the subject of the synthesis closer of the series.
Sprite scaling
is the affine pseudo-three-dimensional approximation
that the projective synthesis subsumes.

Raycasting through a two-dimensional grid
to produce three-dimensional-looking walls
is the subject of the next article in the cluster.
Raycasting and sprite scaling
both produced pseudo-three-dimensional visuals
on hardware of the late 1980s and early 1990s
through different mathematics.

The full Y-sort framework
including tie-breaking rules
and the Z-sort alternative
is the subject of a later cross-cutting article.
The article treats the Y-sort criterion
in its simplest sprite-scaling form.

The full pick-disambiguation framework
including the sprite-scale-and-rotate hit-test
for the Battle Clash and Metal Combat lineage
is the subject of a later cross-cutting article.
The article presents the inverse map
in its simplest form
and defers the full treatment.

The internal architecture of the Sega Super Scaler boards
and the SNES cartridge coprocessor chips
including CX4 and Super FX
is a hardware-design subject
that the article treats only at the level
of the delivery-mechanism sidebar.

## Conclusion

Sprite scaling
extends the affine projection family
of the previous articles
with a per-sprite scaling factor
that depends on the sprite's depth from the camera.
The forward map
combines a scaling factor $s = f/d$
with a sprite-plane rotation $R(\theta)$
to map the sprite-local pixel coordinate
to the screen pixel coordinate.
The inverse map
returns to the sprite-local frame
for hit-testing against the sprite's bounding rectangle.
The technique pre-dates the Mode 7 affine background of the previous article
by nearly a decade
and provided the visual signature
of arcade pseudo-three-dimensional games
across the mid-1980s and into the early 1990s.
The Battle Clash and Metal Combat lineage
brought the technique to home consoles
through the Mode 7 background hardware repurposed as a single sprite,
and established the canonical inverse-map case
for light-gun picking
that the cross-cutting picking article treats later in the series.
The next article in the cluster
treats raycasting
as the alternative pseudo-three-dimensional technique
that contemporary first-person shooters demonstrated
through entirely different mathematics.

## References

- [Reference, After Burner][ref_after_burner]
- [Reference, Battle Clash][ref_battle_clash]
- [Reference, Galaxy Force II][ref_galaxy_force_ii]
- [Reference, Metal Combat, Falcon's Revenge][ref_metal_combat]
- [Reference, Out Run][ref_outrun]
- [Reference, Pole Position][ref_pole_position]
- [Reference, Space Harrier][ref_space_harrier]
- [Reference, Yoshi's Safari][ref_yoshis_safari]

[ref_after_burner]: https://en.wikipedia.org/wiki/After_Burner_(video_game)
[ref_battle_clash]: https://en.wikipedia.org/wiki/Battle_Clash
[ref_galaxy_force_ii]: https://en.wikipedia.org/wiki/Galaxy_Force_II
[ref_metal_combat]: https://en.wikipedia.org/wiki/Metal_Combat:_Falcon%27s_Revenge
[ref_outrun]: https://en.wikipedia.org/wiki/Out_Run
[ref_pole_position]: https://en.wikipedia.org/wiki/Pole_Position_(video_game)
[ref_space_harrier]: https://en.wikipedia.org/wiki/Space_Harrier
[ref_yoshis_safari]: https://en.wikipedia.org/wiki/Yoshi%27s_Safari
