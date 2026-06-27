---
layout: post
mathjax: true
comments: true
title:  "Belt-Scroll, Side-Scrolling with Explicit Depth"
date:   2026-04-23 09:00:00 +0000
categories: games graphics projection
---

<!-- A178 -->
<script>console.log("A178");</script>

The third article in the Cartesian cluster
adds an explicit depth axis
to the side-scrolling view.
The world becomes a strip
of finite depth
along which the player walks
toward or away from the camera
while also moving laterally
across the strip.
The screen shows the strip
from a slightly elevated angle
that maps the depth axis
onto a vertical screen offset.
A character at the back of the strip
appears higher on the screen.
A character at the front of the strip
appears lower on the screen.
The forward map gains a depth-to-screen-y term
controlled by a slope coefficient
that quantifies how steeply the depth axis tilts
into the rendered image.
The inverse map ceases to return a unique world point
and instead returns a family of candidates
indexed by the depth-or-height assumption
that the engine commits to.
Picking ambiguity arises
when multiple sprites stack
along the depth axis at the same lateral position.
The Y-sort criterion
that the cross-cutting article on draw order treats later in the series
gets its first introduction here.

The mode is the foundation of the beat-em-up genre.
The player walks on a flat field
viewed from a slightly tilted camera.
Enemies approach from both sides
and from both depth directions.
Punches,
kicks,
and weapon swings
must connect with enemies
at the same depth as the player
since hits across depth
are not possible
without a depth-discriminating collision system.
The depth axis
is the new dimension
that gameplay must respect
and that the projection map must encode.

The framing the series carries
from the opener
distinguishes the projection math
from the gameplay rules.
The projection math
is a three-dimensional-to-two-dimensional affine map
with a depth-mixing term.
The gameplay rules
choose how to handle collision across depth,
how to render shadows and impacts,
and how to sort overlapping sprites on the screen.
The article treats each component in turn,
walks a concrete worked example,
introduces the Y-sort criterion in its simplest form,
covers the variations
that classic and modern belt-scrolls have explored,
enumerates the delivery mechanisms
period hardware used,
and closes with the canonical games
that defined the mode.

## A Brief History of the Mode

The earliest belt-scroll beat-em-up
is widely cited
as [Renegade][ref_renegade]
from Technōs Japan in 1986.
The game introduced the explicit depth axis
into the side-scrolling beat-em-up format
that earlier titles such as
[Kung-Fu Master][ref_kung_fu_master]
from Irem in 1984
had constrained to a single axis.
The protagonist
walks across a flat field
toward and away from the camera
while fighting enemies at multiple depths
along the strip.

[Double Dragon][ref_double_dragon]
from Technōs in 1987
refined the formula
with two-player cooperative gameplay,
a wider depth-mixing slope,
and a wider repertoire of attacks.
The arcade success of Double Dragon
established the belt-scroll beat-em-up
as a viable arcade subgenre.

[Final Fight][ref_final_fight]
from Capcom in 1989
codified the genre.
The game ran on the Capcom CPS-1 arcade system
and combined large character sprites
with a deep playfield strip
and a depth-mixing slope
that produced a strong oblique-projection feel.
Final Fight became the template
that subsequent belt-scrolls inherited
across the late 1980s and the early 1990s.

[Streets of Rage][ref_streets_of_rage]
on the Sega Genesis in 1991
brought the genre
to home consoles
with a Genesis-quality belt-scroll
that approached arcade visual density.
The Streets of Rage series
ran across three Genesis entries
and reached a fourth entry on modern hardware
in 2020.

[Battletoads][ref_battletoads]
on the Nintendo Entertainment System in 1991
extended the belt-scroll formula
beyond pure beat-em-up gameplay
through level variety
that included vehicle stages,
auto-scrolling sequences,
and platform-style stages.
The Battletoads belt-scroll segments
demonstrated the formula's viability
on the eight-bit hardware
of the previous console generation.

The mode persists
through modern independent and revival releases.
[Streets of Rage 4][ref_streets_of_rage_4]
on Microsoft Windows in 2020
brought the genre into a hand-drawn modern art style
while preserving the underlying projection math
of the earlier entries.

## The Forward Map

The world coordinate
is a three-dimensional position
$\mathbf{p}_{\text{world}} = (w_x, w_y, w_z)$,
where $w_x$ is the lateral position,
$w_y$ is the vertical position
in the gravity-aligned screen-down convention
of the previous articles,
and $w_z$ is the depth into the screen.
The screen coordinate
is a two-dimensional pixel position
$\mathbf{p}_{\text{screen}} = (s_x, s_y)$.
The camera position
is a three-dimensional world coordinate
$\mathbf{c} = (c_x, c_y, c_z)$.
The zoom factor
is a positive scalar $z$
giving the number of screen pixels
that correspond to one world unit
along the $w_x$ and $w_y$ axes.
The depth-mixing slope
is a non-negative scalar $\beta$
giving the screen-y shift
per unit of depth offset from the camera.

The forward map is

$$
s_x = z\, (w_x - c_x) + W/2,
$$

$$
s_y = z\, (w_y - c_y) - \beta\, z\, (w_z - c_z) + H/2,
$$

where $W$ and $H$ are the screen width and height
in pixels.

The lateral term
matches the side-scrolling forward map of the previous articles.
The vertical term
combines the gravity-aligned vertical world coordinate
with the depth coordinate
through the depth-mixing slope.
A character at the back of the playfield
has a larger $w_z$
and a smaller $s_y$,
appearing higher on the screen.
A character at the front
has a smaller $w_z$
and a larger $s_y$,
appearing lower on the screen.

The depth-mixing slope $\beta$
is the design parameter
that distinguishes belt-scroll
from its degenerate special cases.
Setting $\beta = 0$
recovers the side-scrolling forward map of the previous articles,
in which the depth axis collapses
and the world is effectively two-dimensional.
Setting $\beta = 1$
and dropping the gravity-aligned $w_y$ contribution
recovers a top-down view
in which the depth axis maps directly onto the screen vertical axis,
which is the floor-case forward map of the first cluster article.
Belt-scroll uses a slope $\beta$
in the open interval $(0, 1)$,
with classic arcade and console belt-scrolls
choosing values around one half,
to combine both axes
into a single screen-y coordinate.

In homogeneous form
the forward map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & 0 & W/2 - z\, c_x \\ 0 & z & -\beta\, z & H/2 - z\, c_y + \beta\, z\, c_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \\ 1 \end{bmatrix}.
$$

The matrix is a three-by-four affine matrix
acting on the four-component augmented world coordinate
and producing the three-component augmented screen coordinate.
The matrix is the parallel projection
from a three-dimensional world
onto a two-dimensional screen
with the oblique-projection angle
that the slope $\beta$ encodes.
The synthesis closer of the series
treats the more general projective projection
of which the belt-scroll forward map
is an affine specialisation.

The factorisation pattern
from the opener
extends to the belt-scroll case
as a composition of
a depth-mixing shear,
an orthogonal projection from three dimensions to two,
a uniform scale,
and a screen-centre translation,

$$
F = T(\mathbf{o})\, S(z)\, P_z\, K_z(-\beta)\, T(-\mathbf{c}),
$$

where $K_z(-\beta)$
is the three-by-three shear matrix
that adds $-\beta\, w_z$
to the second component
of the camera-relative world coordinate,

$$
K_z(-\beta) =
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -\beta \\ 0 & 0 & 1 \end{bmatrix},
$$

and $P_z$
is the two-by-three orthogonal projection
that drops the depth component,

$$
P_z =
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}.
$$

The shear and the orthogonal projection
are the new factors
that belt-scroll introduces
above and beyond the previous articles' factorisations.
Subsequent articles in the series
generalise the shear matrix
into rotation matrices
and the orthogonal projection
into perspective projection.

A character on the ground at the camera's depth $w_z = c_z$
projects to screen y

$$
s_y^{\text{ground at camera depth}} = z\, (w_y - c_y) + H/2,
$$

which is the side-scrolling forward map of the previous article
without any depth contribution.
The article treats the depth term
as a screen-y offset
that the engine adds
to the side-scrolling screen-y
for characters not at the camera's depth.

When a character jumps,
the height-above-ground convention
of the decoupled-vertical-axis article
applies unchanged.
Writing $h \geq 0$
for the character's height above the ground
and $w_y^{\text{ground}}$
for the ground-plane vertical world coordinate,
the airborne character's $w_y$ is

$$
w_y = w_y^{\text{ground}} - h,
$$

with the subtraction reflecting the $y$-down convention
in which higher airborne objects sit at smaller $w_y$.
The shadow renders at $w_y = w_y^{\text{ground}}$
for any $h$,
and the airborne sprite renders at $w_y = w_y^{\text{ground}} - h$.
The sprite-shadow decomposition writes
the airborne-sprite screen position
as the shadow screen position
shifted upward
by the height-driven vertical offset,

$$
\mathbf{p}_{\text{screen}}^{\text{sprite}} = \mathbf{p}_{\text{screen}}^{\text{shadow}} - (0,\ z\, h),
$$

with the magnitude of the vertical screen-space separation

$$
\Delta s_y = z\, h.
$$

The shadow-drop convention
of the decoupled-vertical-axis article
extends to belt-scroll without modification.

## The Inverse Map

The forward map's matrix
takes three world inputs $(w_x, w_y, w_z)$
and produces two screen outputs $(s_x, s_y)$.
The system is underdetermined,
as in the decoupled-vertical-axis article.
No closed-form inverse exists
that recovers all three world inputs
from the two screen outputs alone.

Solving the forward map for the world coordinates
in terms of the screen coordinates
yields

$$
w_x = \frac{s_x - W/2}{z} + c_x,
$$

$$
w_y - \beta\, w_z = \frac{s_y - H/2}{z} + c_y - \beta\, c_z.
$$

The horizontal world coordinate $w_x$
is uniquely determined.
The vertical and depth world coordinates
appear only through their linear combination
$w_y - \beta\, w_z$.
The combination is determined.
The individual coordinates are not.

The candidate set
is a one-parameter family
along a line in the $(w_y, w_z)$ plane
parameterised by either $w_y$ or $w_z$,

$$
\{ (w_x,\ w_y,\ w_z) : w_y = \beta\, w_z + \frac{s_y - H/2}{z} + c_y - \beta\, c_z \}.
$$

The line is the pre-image of the screen pixel
in the three-dimensional world,
also called the picking ray of belt-scroll.

The engine resolves the ambiguity
through one of three conventions.

The first is the ground-plane assumption.
The engine treats the click
as referring to the ground
and sets $w_y = w_y^{\text{ground}}$.
The recovered depth is

$$
w_z = \frac{w_y^{\text{ground}} - c_y - (s_y - H/2)/z}{\beta} + c_z.
$$

The convention is appropriate
when the click is interpreted as a movement command
to walk to a ground position.

The second is the known-depth assumption.
The engine treats the click
as referring to an object at a known depth $w_z^{\text{known}}$.
The recovered vertical world coordinate is

$$
w_y = \beta\, (w_z^{\text{known}} - c_z) + \frac{s_y - H/2}{z} + c_y.
$$

The convention is appropriate
when the engine has a list of airborne objects
and their current depths,
and the picking step
needs to match a click
against one of the candidates.

The third is the screen-space sprite hit test.
The engine ignores the world coordinates entirely
and tests the clicked screen pixel
against the screen-space bounding rectangles
of every visible sprite.
The strategy is identical to the screen-space hit test
introduced in the decoupled-vertical-axis article.

The visible region of the world
on the ground plane $w_y = w_y^{\text{ground}}$
is the pre-image of the screen rectangle
restricted to that plane.
Substituting $w_y = w_y^{\text{ground}}$
into the inverse-map system
gives

$$
\mathbf{p}_{\text{world}}^{\text{ground}} \in \left(c_x,\ w_y^{\text{ground}},\ c_z + \tfrac{w_y^{\text{ground}} - c_y}{\beta}\right) + \left[ -\tfrac{W}{2z},\ \tfrac{W}{2z} \right] \times \{0\} \times \left[ -\tfrac{H}{2 \beta z},\ \tfrac{H}{2 \beta z} \right].
$$

The visible depth range
is finite
and centred on the depth
at which the camera's centre-of-screen ray
intersects the ground plane.
The engine clips world content
to the visible ground rectangle
when culling for rendering.

## A Worked Example

Consider a Capcom CPS-1 belt-scroll
with the following parameters.
The screen is 384 pixels wide
and 224 pixels tall,
matching the CPS-1 output resolution.
The zoom factor is $z = 1$,
one world unit per pixel.
The depth-mixing slope is $\beta = 1/2$,
a moderate oblique tilt.
The ground-plane vertical world coordinate is $w_y^{\text{ground}} = 200$.
The camera position is $\mathbf{c} = (500, 100, 0)$.
The vertical camera coordinate $c_y = 100$
places the camera 100 world units above the ground
at $w_y^{\text{ground}} = 200$
in the $y$-down convention.
The depth coordinate $c_z = 0$
is the origin of the depth axis.
The choice produces a tilted view
where the ground sits
in the bottom portion of the screen.
The screen-centre offset is $\mathbf{o} = (192, 112)$.

A player character on the ground
at world position $\mathbf{p}_{\text{world}} = (500, 200, 0)$
projects to

$$
s_x = 1 \cdot (500 - 500) + 192 = 192,
$$

$$
s_y = 1 \cdot (200 - 100) - \tfrac{1}{2} \cdot 1 \cdot (0 - 0) + 112 = 100 + 112 = 212.
$$

The player sprite sits at screen $(192, 212)$,
near the bottom of the screen
where the camera's ground level renders.

An enemy at the back of the playfield
at world position $\mathbf{p}_{\text{world}} = (500, 200, 80)$
projects to

$$
s_x = 192,
$$

$$
s_y = 100 - \tfrac{1}{2} \cdot 80 + 112 = 100 - 40 + 112 = 172.
$$

The enemy renders at screen $(192, 172)$,
40 pixels higher on the screen than the player,
matching the depth-mixing slope $\beta = 1/2$
applied to the 80-unit depth offset.

An enemy in front of the player
at world position $\mathbf{p}_{\text{world}} = (500, 200, -40)$
projects to

$$
s_x = 192,
$$

$$
s_y = 100 - \tfrac{1}{2} \cdot (-40) + 112 = 100 + 20 + 112 = 232.
$$

The enemy renders at screen $(192, 232)$,
20 pixels lower on the screen than the player,
matching the negative depth offset
projected through the slope.

Three characters
share the same lateral and ground-plane vertical coordinates
$(w_x = 500, w_y = 200)$
but differ only in depth.
They project to three distinct screen rows
separated by depth.

Now consider a jumping player
at world position $\mathbf{p}_{\text{world}} = (500, 200 - 25, 0) = (500, 175, 0)$,
a height of $h = 25$ above the ground at the camera's depth.
The forward map gives

$$
s_y = 1 \cdot (175 - 100) - \tfrac{1}{2} \cdot 1 \cdot 0 + 112 = 75 + 112 = 187.
$$

The jumping player renders at screen $(192, 187)$.
The shadow at $w_y = 200$ renders at $s_y = 212$
as in the rest-position case.
The vertical separation
between the jumping player and the shadow
is $\Delta s_y = 25$ pixels,
matching $z\, h = 1 \cdot 25 = 25$.

Click-picking at screen pixel $(192, 172)$,
the back-enemy's screen position,
returns a candidate line
in the $(w_y, w_z)$ plane.
The ground-plane assumption
with $w_y^{\text{ground}} = 200$
returns

$$
w_z = \frac{200 - 100 - (172 - 112)/1}{1/2} + 0 = \frac{100 - 60}{1/2} = 80.
$$

The ground-plane inverse returns $w_z = 80$,
matching the back-enemy's world depth.
The picking step
then queries the world's object list
for an object at $(500, 200, 80)$
and returns the back enemy.

The round-trip identity
holds along the ground plane,
which is the same identity pattern
the earlier articles introduced,

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

## The Y-Sort Criterion

The depth axis introduces a draw-order question
that the previous articles' single-plane treatments did not need to answer.
Two world objects at different depths
may project to overlapping screen rectangles.
The renderer must decide
which object's sprite draws on top.

The Y-sort criterion
sorts objects by their ground-projection screen y,
which is the screen y at which the object's shadow renders.
For two ground-level objects
at world positions
$(w_{x,1}, w_y^{\text{ground}}, w_{z,1})$
and $(w_{x,2}, w_y^{\text{ground}}, w_{z,2})$,
the ground-projection screen-y values are

$$
s_{y,1}^{\text{ground}} = z\, (w_y^{\text{ground}} - c_y) - \beta\, z\, (w_{z,1} - c_z) + H/2,
$$

$$
s_{y,2}^{\text{ground}} = z\, (w_y^{\text{ground}} - c_y) - \beta\, z\, (w_{z,2} - c_z) + H/2.
$$

The object with the larger ground-projection $s_y$
is closer to the camera in depth,
because the depth-mixing term $-\beta z w_z$
makes deeper objects render at smaller $s_y$.
The draw-order criterion writes
as a comparison inequality
on the ground-projection screen-y values
and equivalently on the world depths,

$$
\text{draw } i \text{ before } j \iff s_{y,i}^{\text{ground}} < s_{y,j}^{\text{ground}} \iff w_{z,i} > w_{z,j}.
$$

The renderer therefore draws objects
in ascending order of ground-projection $s_y$,
or equivalently in descending order of world depth $w_z$,
from back to front.

The Y-sort criterion
generalises to airborne objects
by sorting on the shadow's screen y
rather than the sprite's screen y.
An airborne object
at world $(w_x, w_y^{\text{ground}} - h, w_z)$
has a sprite at $s_y = z(w_y^{\text{ground}} - h - c_y) - \beta z(w_z - c_z) + H/2$
and a shadow at $s_y^{\text{shadow}} = z(w_y^{\text{ground}} - c_y) - \beta z(w_z - c_z) + H/2$.
The shadow's screen y is independent of $h$
and determines the draw-order position
correctly across both ground and airborne objects.

The cross-cutting article on draw order
later in the series
treats the full Y-sort framework
including tie-breaking rules
for objects at the same depth,
the Z-sort alternative
for engines that track depth explicitly,
and the hybrid Y-then-Z sort
that combines the two.

## Pick Disambiguation for Stacked Sprites

Multiple sprites at different depths
may project to overlapping screen rectangles.
A click at a screen pixel
can fall inside more than one sprite's screen-space bounding box.
The engine must decide
which sprite the click selects.

Three pick-disambiguation conventions appear in practice.

The first is topmost-in-draw-order.
The engine iterates the visible sprites
in front-to-back draw order,
which is the reverse Y-sort order,
and returns the first sprite
whose screen-space bounding box contains the click.
The closest-to-camera sprite
is returned.
This is the dominant convention
for cursor-driven gameplay
and for the editor environments
in which most belt-scroll picking occurs.

The second is smallest-screen-area.
The engine iterates all visible sprites
whose screen-space bounding boxes contain the click
and returns the sprite with the smallest screen-space area.
The convention favours small sprites
that might otherwise be occluded
by larger sprites stacked behind them.
The convention is rare in pure belt-scroll
but appears in level-editor tools
that need to select hard-to-reach objects.

The third is world-space depth priority.
The engine inverts the click
under the ground-plane assumption,
gets a candidate depth $w_z^{\text{ground}}$,
and returns the sprite
whose world-space depth $w_z$
is closest to $w_z^{\text{ground}}$.
The convention is appropriate
when the click is interpreted as a movement command
to a ground position,
and the engine wants to identify
the object at that ground position
rather than the topmost-drawn object.

The cross-cutting article on picking
later in the series
treats the full pick-disambiguation framework
including the Battle Clash and Metal Combat
sprite-scale-and-rotate hit-test case
and the light-gun picking generalisation.

## Variations Within the Mode

The belt-scroll framework
admits several variations
that engines have explored.

A fixed-depth-camera variant
locks the camera at a single $c_z$
for the duration of the level.
The player walks on the strip
between $c_z + d_{\text{front}}$
and $c_z + d_{\text{back}}$
for fixed front and back boundaries.
The camera tracks the player only laterally,
matching the canonical side-scrolling camera policy
of the previous article
applied to belt-scroll.

A two-axis-depth-camera variant
also follows the player
in the depth axis,
so the camera $c_z$
tracks the player's $w_z$
with a smoothing or dead-zone policy.
The variant is rare in classic belt-scrolls
and more common in modern entries
that emphasise depth navigation
as a gameplay feature.

A discrete depth variant
restricts the player to a small set
of discrete depth values,
typically three or four lanes.
The player's $w_z$ changes
only when the player explicitly switches lanes
through gameplay input.
The variant simplifies collision detection
across depth
and is common in classic NES and Master System belt-scrolls
where the central processing unit budget
could not support continuous depth.

A continuous depth variant
permits any $w_z$ in the playfield strip.
The player moves smoothly along the depth axis
under directional pad input.
Most CPS-1 and Genesis belt-scrolls
use the continuous variant.

A scrolling-depth variant
moves the back boundary of the playfield strip
forward as the player advances laterally,
producing the illusion
that the world deepens
as the player moves to the right.
The variant is rare
and is mentioned for completeness.

A per-row scroll factor variant
introduces per-scanline horizontal scroll modulation
that simulates a per-row depth value,
which produces a stronger perspective approximation
than the constant $\beta$ allows.
The per-row scroll factor
anticipates the affine ground-plane treatment
of the Mode 7 article later in the series.

A sprite-scaling variant
scales the sprite size
in proportion to the inverse of the depth,

$$
s_{\text{sprite}}(w_z) = \frac{s_{\text{sprite}}^{(0)} \cdot d_{\text{ref}}}{w_z - c_z + d_{\text{ref}}},
$$

where $d_{\text{ref}}$ is a reference depth
and $s_{\text{sprite}}^{(0)}$ is the sprite size
at the reference depth.
The variant departs from the affine projection
of this article
into the sprite-scaling territory
of a later article in the series.
Pure belt-scroll
does not scale sprites with depth.

A foreground-occlusion variant
allows foreground sprites
at $w_z < c_z - d_{\text{occlude}}$
to occlude the playfield strip
from the player's view.
The occluding sprites
render through the same forward map
but at a depth in front of the play strip.
The variant produces the effect
of trees, signs, or fences
that the player walks behind.

## Delivery Mechanisms

The belt-scroll forward map
permits five distinct delivery mechanisms
on period hardware.

The first is software composition
on a general-purpose central processing unit.
The engine computes each sprite's screen position
through the forward map
and writes the sprites to the frame buffer
in Y-sort order.
The mechanism was the universal delivery
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s,
and remains the dominant mechanism
on modern independent-game engines
that render to a software frame buffer.

The second is sprite-on-tile-background
with per-sprite Y-sort.
The CPS-1 arcade hardware,
the Sega Genesis,
and the Super Nintendo Entertainment System
all provide object-attribute-memory sprite hardware
that the engine can drive
with per-sprite screen positions
computed through the belt-scroll forward map.
The background tile layer
renders the playfield strip
through the standard hardware scroll register.
The sprite priority
is set per sprite
to match the Y-sort order.

The third is hardware-sprite-drawing-order Y-sort.
The Sega Genesis sprite list
uses per-sprite link fields
that determine the traversal order during rendering.
The engine writes the link sequence
in Y-sort order
during the per-frame sprite list construction.
The hardware then renders sprites
in the link-traversal order automatically.
The mechanism trades engine flexibility
for hardware throughput.

The fourth is pre-baked depth-sorted sprite atlases.
The engine pre-renders the sprite frames
at each discrete depth
in the play-strip range
and selects the appropriate frame at render time
based on the sprite's current $w_z$.
The mechanism removes the per-frame depth-sort cost
at the cost of larger sprite memory.
The technique appears
in late-period sixteen-bit games
that needed to render many sprites at high frame rates.

The fifth is graphics-processing-unit-accelerated quad rendering.
Modern game engines
such as Unity, Godot, and Unreal
render the belt-scroll world
as textured quads
in three-dimensional world space
with a camera transform
that produces the desired oblique projection.
The graphics processing unit
performs the depth sort
through its built-in depth buffer
and produces the screen image.
The modern engine
does not need to enforce Y-sort manually
because the depth buffer enforces it
at the hardware-rasterisation level.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
the sprite-budget pressure,
the central-processing-unit budget for the per-frame sort,
the sprite-memory budget,
and the achievable frame rate.

## Where the Framing Breaks Down

The belt-scroll framing is insufficient
when any of the following conditions hold.

When the camera angle is steep enough
that perspective scaling
becomes visually significant,
the affine projection of this article
is insufficient.
The sprite-scaling article later in the series
treats the case
where the engine scales each sprite
by an inverse-depth factor.
The synthesis closer of the series
treats the full projective generalisation.

When the world has a non-flat ground,
the constant depth-mixing slope $\beta$
fails to track the visible ground level.
The Mode 7 article later in the series
treats the per-scanline affine matrix
that permits the ground plane to bend
under a more general projection.

When the playfield exposes truly three-dimensional geometry
rather than a flat strip with depth,
the oblique projection
of this article
is insufficient.
The synthesis closer of the series
treats the projective generalisation
that handles three-dimensional geometry
through the perspective denominator.

When the player can rotate the camera,
the depth axis ceases to point into the screen,
and the forward map gains a rotation matrix.
The axonometric and isometric articles in the next cluster
treat the rotated-camera case.

When the gameplay treats depth
as a discrete lane assignment
rather than a continuous coordinate,
the picking ambiguity collapses
because each lane has a discrete $w_z$
and the candidate set has cardinality at most equal to the lane count.
The discrete-depth variant above
is the relevant case.

When sprite scaling is needed
to convey the perspective accurately,
the affine projection of this article
is insufficient.
The classic belt-scroll
does not scale sprites
and instead lets the depth-mixing slope
carry the visual depth cue alone.
Modern belt-scrolls
sometimes scale sprites lightly
for visual interest,
crossing into the sprite-scaling territory.

## The Canon

The following games
use belt-scroll
as their primary projection mode.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Renegade][ref_renegade]
in the arcade in 1986
gave the medium
its first belt-scroll beat-em-up
with an explicit depth axis
that the side-scrolling beat-em-ups before it
did not provide.

[Double Dragon][ref_double_dragon]
in the arcade in 1987
refined the formula
with cooperative two-player gameplay
and a wider repertoire of attacks.

[Final Fight][ref_final_fight]
in the arcade in 1989
codified the genre
through the Capcom CPS-1 hardware's
sprite throughput
and the large-character art style
that subsequent belt-scrolls inherited.

[Streets of Rage][ref_streets_of_rage]
on the Sega Genesis in 1991
brought arcade-quality belt-scroll
to the home console
with a soundtrack and visual style
that the home-console audience embraced.

[Battletoads][ref_battletoads]
on the Nintendo Entertainment System in 1991
demonstrated the belt-scroll formula
on eight-bit hardware
through level variety
that mixed beat-em-up belt-scroll segments
with auto-scrolling vehicle stages
and platform-style stages.

[Streets of Rage 4][ref_streets_of_rage_4]
on Microsoft Windows in 2020
brought the genre into modern hardware
with a hand-drawn art style
that preserves the underlying projection math
of the earlier entries.

Each game in the canon
uses the belt-scroll forward map
with a different depth-mixing slope $\beta$,
a different camera policy
along the depth axis,
and a different choice of delivery mechanism
appropriate to the target hardware.

## Out of Scope

The article does not cover
the following.

Sprite scaling along the depth axis
is treated in the sprite-scaling article
later in the series.
The classic belt-scroll
uses uniform sprite size
without depth-dependent scaling.

The full Y-sort framework
including tie-breaking and Z-sort variants
is the subject of a later cross-cutting article.
The article introduces the Y-sort criterion
in its simplest form
and defers the full treatment.

The full pick-disambiguation framework
including the sprite-scale-and-rotate hit-test
of Battle Clash and Metal Combat
is the subject of a later cross-cutting article.
The article presents the three baseline conventions
and defers the full treatment.

Collision detection across depth
is gameplay-physics territory
that the projection math does not depend on.
The article treats projection only.

True three-dimensional rendering
of the belt-scroll world
through a graphics-processing-unit pipeline
with a perspective camera
is the modern delivery mechanism
that the article treats only briefly.
The mechanism produces the belt-scroll forward map
as a special case of perspective projection
but introduces depth buffering and shader programming
that the article does not depend on.

The axonometric and isometric viewing angles
that permit camera rotation
are treated in the next cluster
of the series.

## Conclusion

Belt-scroll side-scrolling with explicit depth
extends the side-scrolling view
of the previous article
with a depth axis
that the camera projects
through a depth-mixing slope $\beta$.
The forward map is a three-dimensional-to-two-dimensional affine projection
with a shear factor on the depth coordinate.
The inverse map is underdetermined
and admits three disambiguation conventions
parallel to the decoupled-vertical-axis article's conventions.
The Y-sort criterion
makes its first appearance in the series
as the sort-by-ground-projection-screen-y rule
that the renderer must enforce
to draw stacked sprites in the correct order.
The pick disambiguation
for stacked sprites
admits three conventions
that the engine selects
based on the gameplay action being requested.
The math is the simplest non-trivial three-dimensional projection
in the Cartesian cluster,
and the delivery
admits five distinct mechanisms
on period hardware and modern engines.
The next article in the series
swaps the camera orientation
from looking at the world along a primary axis
to looking at the world along a tilted axis,
which is the oblique view
of the quarter-view cluster.

## References

- [Reference, Battletoads][ref_battletoads]
- [Reference, Double Dragon][ref_double_dragon]
- [Reference, Final Fight][ref_final_fight]
- [Reference, Kung-Fu Master][ref_kung_fu_master]
- [Reference, Renegade][ref_renegade]
- [Reference, Streets of Rage][ref_streets_of_rage]
- [Reference, Streets of Rage 4][ref_streets_of_rage_4]

[ref_battletoads]: https://en.wikipedia.org/wiki/Battletoads_(video_game)
[ref_double_dragon]: https://en.wikipedia.org/wiki/Double_Dragon_(arcade_game)
[ref_final_fight]: https://en.wikipedia.org/wiki/Final_Fight
[ref_kung_fu_master]: https://en.wikipedia.org/wiki/Kung-Fu_Master_(video_game)
[ref_renegade]: https://en.wikipedia.org/wiki/Renegade_(video_game)
[ref_streets_of_rage]: https://en.wikipedia.org/wiki/Streets_of_Rage_(video_game)
[ref_streets_of_rage_4]: https://en.wikipedia.org/wiki/Streets_of_Rage_4
