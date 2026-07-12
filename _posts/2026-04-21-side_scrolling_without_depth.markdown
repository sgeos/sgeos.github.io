---
layout: post
mathjax: true
comments: true
title:  "Side-Scrolling Without Depth"
date:   2026-04-21 09:00:00 +0000
categories: games graphics projection
series: two_dimensional_projection
series_title: Two-Dimensional Projection in Games
series_index: 4
---
<!-- A176 -->
<script>console.log("A176");</script>

The next article in the Cartesian cluster
swaps the camera orientation
from the straight-down view of the previous two articles
to a sideways view
that looks across the world horizontally.
The forward map and the inverse map
remain structurally identical to the floor case.
What changes is the interpretation
of the world's vertical axis,
the camera-policy choices the engine makes,
and the explicit appearance of gravity
as a force that pulls airborne objects toward the ground.

The mode is the foundation of the platformer genre.
A character moves left and right
on a world that the camera reveals
through horizontal scrolling.
The character jumps,
falls,
climbs ladders,
and collides with platforms
that the world geometry defines.
The screen shows
a horizontal slice of the world
that the camera centres on the player.
The vertical extent of the screen
shows the air above the ground
and possibly a strip of the ground itself.

The framing the series carries
from the opener
distinguishes the projection math
from the gameplay physics and the camera policy.
The projection math is a planar translation and zoom
identical to the top-down floor case.
The gameplay physics
adds gravity,
collision,
and jump motion.
The camera policy
chooses whether to follow the player vertically,
how to handle level boundaries,
and how to ratchet forward without backtracking
when the design demands it.
The article treats each component in turn,
walks a concrete worked example,
covers the camera-policy variations
that real games introduce,
enumerates the delivery mechanisms
period hardware used,
and closes with the canonical games
that defined the mode.

## A Brief History of the Mode

The earliest side-scrolling commercial release
is debated
in the same way the earliest of any genre is debated,
but the [Defender][ref_defender] arcade machine
from Williams in 1981
is widely cited
as the first horizontally-scrolling shoot-em-up
with a continuously scrolling world.
The player flies a ship
across a horizontally wrapping world
that the screen reveals through scrolling.
[Scramble][ref_scramble]
from Konami in the same year
provided a side-scrolling shooter
with a forced scroll
that pulled the camera forward
at a constant rate.

The side-elevation view itself
is older than the side-scrolling format.
[Donkey Kong][ref_donkey_kong]
from Nintendo in 1981
used the side-elevation view
in a single-screen game
without scrolling.
The player climbs ladders and jumps between platforms
on a fixed-screen layout
that the camera does not move across.
Donkey Kong established
the visual language of the platformer
that subsequent scrolling platformers inherited.

The canonical scrolling platformer
arrives with [Super Mario Bros][ref_super_mario_bros]
on the Nintendo Entertainment System in 1985.
The world scrolls horizontally
as Mario walks and runs to the right.
The camera follows the player horizontally
with a soft right-bias
that the level designer used
to teach the player to read what comes ahead.
The camera is locked vertically
to a ground-level position.
The Super Mario Bros camera policy
became the dominant template
for the genre.

[Castlevania][ref_castlevania]
on the Nintendo Entertainment System in 1986
established the action-platformer
with whip combat
in a side-scrolling castle.
The Castlevania camera
follows Simon Belmont
horizontally during flat sections
and vertically along the stairways
that connect the floor levels.
Stages end at boss arenas,
where the camera fixes
on a single screen.

[Mega Man][ref_mega_man]
on the same console in 1987
refined the side-scrolling action-platformer
with discrete room-to-room scroll transitions
within each level.
The camera scrolls smoothly within a room
and performs a brief directed scroll to the next room
when the player crosses a room boundary.

The genre proliferates
across the late 1980s and 1990s
through titles such as
[Super Mario Bros 3][ref_super_mario_bros_3] in 1988,
the Mega Man sequels,
the Castlevania sequels,
and dozens of platformers
that variations on the camera policy
and the level structure produced.

The modern independent game
keeps the mode alive
through titles such as
[Celeste][ref_celeste]
on Microsoft Windows in 2018.
Celeste uses a smooth-tracking camera
in both axes,
sub-pixel character motion,
and pixel-perfect framing
that depart from the strict tile-aligned scrolling
of period hardware
while preserving the side-scrolling forward-map structure.

## The Forward Map

The world coordinate
is a two-dimensional position
$\mathbf{p}_{\text{world}} = (w_x, w_y)$.
The screen coordinate
is a two-dimensional pixel position
$\mathbf{p}_{\text{screen}} = (s_x, s_y)$.
The camera position
is a world coordinate
$\mathbf{c} = (c_x, c_y)$
that the engine treats
as the world point
at the centre of the screen.
The zoom factor
is a positive scalar $z$
giving the number of screen pixels
that correspond to one world unit.

The forward map is

$$
\mathbf{p}_{\text{screen}} = z\, (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o},
$$

where $\mathbf{o} = (W/2, H/2)$
is the pixel coordinate
of the screen centre,
and $W$ and $H$ are the screen width and height
in pixels.

The form is identical
to the floor-case forward map of the previous article.
The interpretation differs in three ways.

First,
the second world coordinate $w_y$
is now a vertical position in a world with gravity.
The article maintains the $y$-down convention
established in the opener.
Under that convention,
larger $w_y$ values
correspond to positions lower in the world,
the ground level sits at a large positive $w_y$ value,
and gravity acts in the $+y$ direction.
A reader designing a new engine
who prefers $y$-up
for compatibility with physics conventions
should negate the second row of the scale matrix
to get

$$
\mathbf{p}_{\text{screen}} = \begin{bmatrix} z & 0 \\ 0 & -z \end{bmatrix} (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o}.
$$

Either convention works.
The sign choice
affects only the world-coordinate interpretation
and is held consistently across the engine.

Second,
the camera position
is driven by a different policy
in side-scrolling than in top-down.
The horizontal camera position $c_x$
typically follows the player position $w_{x,\text{player}}$
with a small right-bias offset
that the level designer used
to reveal what comes ahead.
The vertical camera position $c_y$
is often locked
to a fixed value $c_y^{(0)}$
that the level designer chose
to keep the ground at the bottom of the screen.
The horizontal-only-scroll variant of the camera
is

$$
\mathbf{c}(t) = (c_x(t),\ c_y^{(0)}),
$$

with $c_x(t)$ evolving over time
and $c_y^{(0)}$ fixed.
The variations section later treats
the policies for releasing the vertical lock.

The canonical side-scrolling camera policy
specialises the horizontal-only-scroll variant
to a player-tracking horizontal position.
Writing $d_{\text{bias}} > 0$
for the right-bias offset in world units,
the canonical camera position is

$$
\mathbf{c}(t) = (w_{x,\text{player}}(t) - d_{\text{bias}},\ c_y^{(0)}).
$$

Super Mario Bros chooses $d_{\text{bias}}$
so that the player sprite appears
in the left third of the screen
during forward motion,
which leaves the right two thirds of the screen
to show approaching terrain.

Third,
the world objects in the side-scrolling view
behave under gameplay physics
that the top-down view does not need.
The player character
is subject to gravity,
collision with the ground,
and friction.
A canonical jump trajectory
for the player position
under constant gravity
is

$$
\mathbf{p}_{\text{world}}(t) = \mathbf{p}_{\text{world}}^{(0)} + (v_x,\ -v_y^{(0)})\, t + (0,\ \tfrac{1}{2}\, g)\, t^2,
$$

where $v_x$ is the horizontal launch velocity,
$v_y^{(0)} > 0$ is the upward launch velocity
under the $y$-down convention,
and $g > 0$ is the gravitational acceleration
in world units per second squared.
The trajectory is parabolic
in the $(w_x, w_y)$ plane.
The forward map applies to the time-evolving world position
on every rendered frame.
The trajectory itself
is gameplay physics
and is treated only as input to the projection
in this article.

The factorisation pattern from the opener
applies to the side-scrolling forward map
without modification,

$$
F = T(\mathbf{o})\, S(z)\, T(-\mathbf{c}).
$$

The factorisation is the same as the floor-case factorisation
and is the pattern
every projection mode in the series inherits.
The side-scrolling specialisation
restricts the time-evolution of $\mathbf{c}$
to a horizontal-dominant pattern
and lets the world physics
animate the $w_y$ coordinate of the player
through gravity and jumping.

In homogeneous form
the same map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & W/2 - z\, c_x \\ 0 & z & H/2 - z\, c_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ 1 \end{bmatrix}.
$$

The matrix is the planar affine matrix of the floor case
and is the two-dimensional restriction
of the opener's four-by-four projective generalisation.
The side-scrolling map shares the matrix structure
with the top-down floor case
and differs only in the interpretation of $w_y$
and in the camera policy that updates $\mathbf{c}$ over time.

## The Inverse Map

The forward map's matrix
is square and full rank,
and the inverse exists in closed form,

$$
\mathbf{p}_{\text{world}} = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \mathbf{c}.
$$

Every screen pixel corresponds to one world point.
There is no ambiguity,
no candidate set,
and no missing dimension.
The inverse is mathematically identical to the floor-case inverse
of the previous article.

The visible region of the world
is the pre-image of the screen rectangle
under the inverse map,

$$
\mathbf{p}_{\text{world}} \in \mathbf{c} + \frac{1}{z}\, \left[ -\tfrac{W}{2},\ \tfrac{W}{2} \right] \times \left[ -\tfrac{H}{2},\ \tfrac{H}{2} \right].
$$

The rectangle is what the renderer iterates over
when culling invisible objects,
and is what the engine clamps the camera against
when the camera reaches a level boundary.

The picking pipeline
takes the inverse-mapped world point
and resolves it
to a world-space object.
The three resolution strategies from the floor case apply unchanged.
A hit-test against bounding rectangles in reverse draw order
returns the topmost visible object containing the click.
A tile lookup
divides the clicked world point by the tile size
and returns the world object at the resulting tile cell.
A spatial index queries the index
with the clicked world point
and returns a short list of candidates
to test against bounding rectangles.

Side-scrolling picking
is most commonly used
for level-editor interaction,
for mouse-driven gameplay overlays,
and for cursor-based debug tools.
The mainstream gameplay does not use picking
in the same way the top-down view does
since the side-scrolling player
controls the character through gamepad input
rather than through a screen cursor.
Picking remains a valid operation
that the engine must support
and that the inverse map makes trivially available.

## A Worked Example

Consider a side-scrolling platformer
with the following parameters.
The screen is 256 pixels wide
and 240 pixels tall,
matching the Nintendo Entertainment System resolution.
The zoom factor is $z = 1$,
one world unit per pixel.
The ground-level vertical world coordinate is $w_y^{\text{ground}} = 200$.
The vertical camera position is locked at $c_y^{(0)} = 120$,
which places the ground at the bottom of the screen.
The horizontal camera position
follows the player position
with a fixed right-bias of $-32$,
so $c_x = w_{x,\text{player}} - 32$.

The player stands at world position $\mathbf{p}_{\text{world}} = (300, 200)$
with $w_y = 200$ matching the ground.
The camera position is therefore $\mathbf{c} = (268, 120)$.
The forward map gives the player's screen position as

$$
\mathbf{p}_{\text{screen}}^{\text{player}} = (300 - 268,\ 200 - 120) + (128, 120) = (32,\ 80) + (128, 120) = (160,\ 200).
$$

The player sprite
sits at screen $(160, 200)$,
which is offset right of centre by 32 pixels
due to the right-bias,
and at the bottom strip of the screen
where the ground sits.

The player executes a jump
with launch upward velocity $v_y^{(0)} = 150$ world units per second
and horizontal velocity $v_x = 50$ world units per second.
Gravity is $g = 600$ world units per second squared.

The jump duration to apex
is $t_{\text{apex}} = v_y^{(0)} / g = 0.25$ seconds.
The apex height above the ground
is $\Delta_y^{\max} = (v_y^{(0)})^2 / (2\, g) = 18.75$ world units.

At $t = 0.25$ seconds,
the apex,
the player position is

$$
\mathbf{p}_{\text{world}}(0.25) = (300 + 12.5,\ 200 - 18.75) = (312.5,\ 181.25).
$$

The camera horizontal position
follows the player,
giving $c_x(0.25) = 312.5 - 32 = 280.5$.
The vertical camera position remains $c_y^{(0)} = 120$.
The forward map gives the player's screen position
at the apex as

$$
\mathbf{p}_{\text{screen}}^{\text{player}}(0.25) = (312.5 - 280.5,\ 181.25 - 120) + (128, 120) = (32 + 128,\ 61.25 + 120) = (160,\ 181.25).
$$

The player sprite stays at screen $x = 160$
because the camera tracks the horizontal motion exactly.
The vertical screen position moves from $200$ to $181.25$,
a screen-space rise of $18.75$ pixels,
matching the world-space height gain.

The round-trip identity
holds in the side-scrolling case
exactly as in the floor case,

$$
F^{-1}(F(\mathbf{p}_{\text{world}})) = \mathbf{p}_{\text{world}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

## Variations Within the Mode

The camera policy is where side-scrolling games differ.
The variations affect the engine
without changing the projection math.

A vertically-locked camera
fixes $c_y = c_y^{(0)}$
and updates $c_x$ to track the player horizontally.
Super Mario Bros uses this policy.
The vertical lock keeps the ground at the bottom of the screen
and makes the level layout
predictable for the player.
Jumps stay within the visible band
because the level designer
chose maximum platform heights
within the screen's vertical reach.

A vertical dead-zone camera
keeps $c_y$ locked
while the player's vertical position
stays within a band $\pm d_v$
around the camera centre.
When the player exits the band,
the camera updates,

$$
c_y \leftarrow w_{y,\text{player}} \mp d_v.
$$

The dead-zone variant lets the player explore vertically
within a level
without the camera tracking every jump.

A smooth two-axis camera
interpolates the camera position
toward the player position
on every frame,

$$
\mathbf{c}_{n+1} = \mathbf{c}_n + \alpha\, (\mathbf{c}_{\text{target}} - \mathbf{c}_n),
$$

where $\mathbf{c}_{\text{target}} = \mathbf{p}_{\text{player}}$
and $\alpha \in (0, 1]$ is the interpolation factor.
Celeste and other modern platformers
use a smooth two-axis camera
in some sections of the game.

A forced-scroll camera
moves the camera at a fixed horizontal velocity
regardless of player motion,

$$
c_x(t) = c_x(0) + v_{\text{scroll}}\, t.
$$

The player must keep up with the scroll
or be pushed off the screen.
Gradius,
R-Type,
and the Super Mario Bros auto-scroll levels
use this policy.

A one-way scroll lock
allows the camera to advance
when the player moves forward
but prevents the camera from retreating,

$$
c_x \leftarrow \max(c_x,\ w_{x,\text{player}} - d_{\text{bias}}).
$$

The original Super Mario Bros uses one-way scrolling
to prevent the player from returning to passed sections,
which simplifies the rendering pipeline
by allowing the engine
to discard background tiles
that have scrolled off the left edge.

A screen-flip scroll
snaps the camera position
to a multiple of the screen width
when the player crosses a screen boundary,

$$
c_x \leftarrow W\, \lfloor w_{x,\text{player}} / W \rfloor + W/2.
$$

[Pitfall][ref_pitfall]
on the Atari 2600 in 1982
uses screen-flip transitions
between adjacent rooms.
Mega Man approximates the same room-coordinate snap
with a brief directed scroll
that visually softens the transition
while leaving the room coordinate discrete.
The screen flip
is the camera-policy generalisation
of the room-to-room transition
in top-down Zelda.

A sub-pixel scroll
permits the camera position
to be a non-integer
even though the screen position
must round to integer pixels.
The pixel-quantisation step from the opener
applies after the forward map
and discards the fractional part
for display.
Sub-pixel scroll matters
for smooth motion at low frame rates
and at low world-zoom factors.

A bounded camera
clamps the camera position
to keep the visible window inside the level,

$$
\mathbf{c} = \mathrm{clamp}\left( \mathbf{c}_{\text{target}},\ \mathbf{m}_{\min} + \tfrac{\mathbf{v}}{2},\ \mathbf{m}_{\max} - \tfrac{\mathbf{v}}{2} \right),
$$

where $\mathbf{m}_{\min}$ and $\mathbf{m}_{\max}$
are the world-space corners of the level
and $\mathbf{v} = (W/z,\ H/z)$
is the viewport size in world units.
The clamping
introduces edge cases
near the level boundary
where the player is not at the screen centre
because the camera could not follow further.

A look-ahead scroll
offsets the camera position
in the direction of player motion
to show more of what is ahead,

$$
c_x \leftarrow c_x^{\text{base}} + k\, v_{x,\text{player}},
$$

where $k > 0$ is a look-ahead constant
and $v_{x,\text{player}}$ is the player's horizontal velocity.

A discrete zoom
allows the zoom factor $z$
to take a small set of values
selected by the game state.
The zoomed-in boss-encounter framing
in late-period sixteen-bit and modern indie platformers
is the canonical use of this variant.

## Delivery Mechanisms

The forward map is simple
and almost any rendering pipeline
can deliver it.
Period hardware used five distinct mechanisms.

The first is a tile-grid background layer
with a hardware horizontal scroll register.
The Nintendo Entertainment System
provided two background nametables
and a horizontal scroll register
that the renderer added to the layer position
to produce the camera-relative offset.
The Super Nintendo Entertainment System
provided four background layers
each with its own scroll registers.
The Sega Genesis
provided two background layers
with similar scroll-register support.
The math the hardware computed
was exactly the forward map of this article
with $z = 1$.

The second is sprite-on-tile-background
where the player and the enemies
are object-attribute-memory sprites
that the engine positions at camera-relative screen coordinates.
The background tile layer scrolls
under the hardware scroll register.
The sprite layer
positions each sprite
at the camera-relative screen coordinate
that the engine computes per frame.
This is the standard delivery mechanism
on the Nintendo Entertainment System,
the Super Nintendo Entertainment System,
the Sega Genesis,
and most arcade hardware of the era.

The third is software composition
on a general-purpose central processing unit.
The engine maintains a frame buffer
and writes each visible object
into the frame buffer
at its camera-relative screen coordinate.
This was the universal delivery mechanism
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s
and remains the mechanism
for many modern independent games
that render to a software frame buffer.

The fourth is horizontal-blank scroll-register modulation,
a delivery mechanism
where the engine updates the scroll register
during the horizontal-blank interrupt
that separates one scanline from the next.
The technique is most often used
to produce parallax scrolling
and is treated in the next article.
Without parallax,
the same technique can produce
strip-by-strip waviness effects
and split-screen effects
that single-register scrolling cannot.

The fifth is graphics-processing-unit-accelerated quad rendering.
Modern game engines
such as Unity, Godot, and Unreal
render the world
as a collection of textured quads
positioned by a camera transform
that is the forward map of this article.
The graphics processing unit
applies the matrix
in hardware
and produces the screen image.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
memory budget,
and achievable frame rate.

## Where the Framing Breaks Down

The side-scrolling-without-depth framing
is insufficient when any of the following conditions hold.

When the engine renders multiple background layers
that scroll at different rates
to suggest depth,
the floor case is insufficient.
The parallax variant
treated in the next article
introduces a per-layer scroll factor.

When the gameplay introduces an explicit depth axis
that the player can navigate,
the floor case loses the third axis.
The belt-scroll mode
of the third Cartesian-cluster article
adds an explicit depth dimension
to side-scrolling.

When the camera rotates with the player,
the forward map gains an additional rotation matrix.
The rotated camera
is usually treated as a special case
of axonometric or oblique projection
in the next cluster.

When the gameplay treats some objects
as orthographic side-views
and others as top-down icons,
the floor case is insufficient.
The hybrid projection
of the Mother series
is the closest analogue
and is treated in the stylised-hybrid article
later in the series.

When the level scrolls in two dimensions
simultaneously and continuously,
the camera policy generalises
to a two-axis tracking variant
that the variations section already covers.
The math is unchanged.
The framing is not really broken,
only stretched
to include the two-axis case.

When the world is structurally vertical
rather than horizontal,
as in [Ice Climber][ref_ice_climber] or in some shoot-em-up sub-genres,
the math is the side-scrolling math
with the dominant scroll axis rotated by ninety degrees.
The article frames vertical scrolling
as a rotated side-scrolling case
rather than as a separate mode.

## The Canon

The following games
use side-scrolling without depth
as their primary projection mode.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Defender][ref_defender]
in the arcade in 1981
gave the genre
its first continuously-scrolling horizontal shoot-em-up
on a single-plane world.

[Donkey Kong][ref_donkey_kong]
in the arcade in 1981
established the side-elevation view
of the platformer
on a single-screen layout
without scrolling.
Subsequent scrolling platformers
inherited the visual language.

[Super Mario Bros][ref_super_mario_bros]
on the Nintendo Entertainment System in 1985
gave the home console
its canonical scrolling platformer
with the vertically-locked,
horizontally-tracking,
one-way-locked camera
that became the genre template.

[Castlevania][ref_castlevania]
on the Nintendo Entertainment System in 1986
gave the home console
its canonical action-platformer
with combined horizontal and vertical scrolling
along the stairways of the castle.

[Mega Man][ref_mega_man]
on the same console in 1987
refined the side-scrolling action-platformer
with structured level progression
across discrete rooms
and brief directed-scroll transitions between them.

[Super Mario Bros 3][ref_super_mario_bros_3]
on the same console in 1988
expanded the camera-policy repertoire of the Mario series
with two-axis tracking in dedicated level types,
a world map between levels,
and a wider set of camera policies
that subsequent platformers inherited.

[Celeste][ref_celeste]
on Microsoft Windows in 2018
brought the side-scrolling platformer
into the modern independent game
with a smooth two-axis camera,
sub-pixel character motion,
and a pixel-perfect framing
that recalls the period hardware
without strictly emulating it.

Each game in the canon
exercises a different subset of the camera-policy variations
above.
The forward map and inverse map
are the same equations
across the canon.

## Out of Scope

The article does not cover
the following.

Parallax scrolling,
including multi-plane background tracks,
per-layer scroll factors,
and the screen-space depth illusion
that parallax produces,
is the subject of the next article.

Belt-scrolling,
which adds an explicit depth axis
to the side-scrolling view,
is treated later in the Cartesian cluster.

Platformer physics
beyond the simple parabolic trajectory,
including variable jump height,
double jumps,
wall jumps,
air control,
and momentum systems,
is gameplay-physics territory
that the projection math does not depend on.

Level design,
including tile-based level construction,
chunk-based streaming,
and procedural level generation,
is content-authoring territory
adjacent to but distinct from
the projection math.

The 2.5D and pseudo-three-dimensional hybrids
that some side-scrollers use,
such as the multi-plane depth in [Klonoa][ref_klonoa]
and the rendered-three-dimensional-on-a-two-dimensional-plane gameplay
of the Pandemonium era,
are treated in the stylised-hybrid article
later in the series.

The choice between side-scrolling and top-down
for a given game
is a design question
the series does not adjudicate.

## Conclusion

Side-scrolling without depth
is the second mode in the Cartesian cluster.
The forward map and the inverse map
are structurally identical
to the top-down floor case.
What distinguishes the side-scrolling mode
is the interpretation of the world vertical axis
as a gravity-aligned axis,
the camera-policy choices the engine makes
to follow the player horizontally
while keeping the ground at a stable screen position,
and the appearance of gravity and jump trajectories
as inputs to the projection
from the gameplay-physics layer.
The math is simple.
The interesting work
sits in the camera policy
and in the choice of delivery mechanism
appropriate to the target platform.
The next article in the cluster
adds parallax scrolling
to the side-scrolling view
through multiple background layers
that scroll at different rates
to suggest depth.

## References

- [Reference, Castlevania][ref_castlevania]
- [Reference, Celeste][ref_celeste]
- [Reference, Defender][ref_defender]
- [Reference, Donkey Kong][ref_donkey_kong]
- [Reference, Ice Climber][ref_ice_climber]
- [Reference, Klonoa][ref_klonoa]
- [Reference, Mega Man][ref_mega_man]
- [Reference, Pitfall][ref_pitfall]
- [Reference, Scramble][ref_scramble]
- [Reference, Super Mario Bros][ref_super_mario_bros]
- [Reference, Super Mario Bros 3][ref_super_mario_bros_3]

[ref_castlevania]: https://en.wikipedia.org/wiki/Castlevania_(1986_video_game)
[ref_celeste]: https://en.wikipedia.org/wiki/Celeste_(video_game)
[ref_defender]: https://en.wikipedia.org/wiki/Defender_(1981_video_game)
[ref_donkey_kong]: https://en.wikipedia.org/wiki/Donkey_Kong_(arcade_game)
[ref_ice_climber]: https://en.wikipedia.org/wiki/Ice_Climber
[ref_klonoa]: https://en.wikipedia.org/wiki/Klonoa:_Door_to_Phantomile
[ref_mega_man]: https://en.wikipedia.org/wiki/Mega_Man_(1987_video_game)
[ref_pitfall]: https://en.wikipedia.org/wiki/Pitfall!
[ref_scramble]: https://en.wikipedia.org/wiki/Scramble_(video_game)
[ref_super_mario_bros]: https://en.wikipedia.org/wiki/Super_Mario_Bros.
[ref_super_mario_bros_3]: https://en.wikipedia.org/wiki/Super_Mario_Bros._3
