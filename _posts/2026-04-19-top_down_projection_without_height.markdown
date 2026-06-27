---
layout: post
mathjax: true
comments: true
title:  "Top-Down Projection Without Height"
date:   2026-04-19 09:00:00 +0000
categories: games graphics projection
---

<!-- A174 -->
<script>console.log("A174");</script>

The simplest projection mode
in the two-dimensional game canon
is the top-down view
of a flat world without height.
The camera looks straight down
at the world.
The world is a plane.
The screen is a window
onto a portion of that plane.
The forward map
is a camera-relative translation
followed optionally by a zoom.
The inverse map
is the inverse of that translation
and zoom,
and is therefore trivially obtainable.
Picking is straightforward.
Drawing is straightforward.
The challenge for the programmer
lies not in the math
but in the camera policy,
in the tile coordinate system,
and in the choice of delivery mechanism
appropriate to the target platform.

This article opens the Cartesian cluster
of the series.
It treats the top-down view
as the floor case
on top of which every subsequent projection mode
adds structure.
The next article in the cluster
adds a decoupled vertical axis
that lets characters jump
and that lets shadows drop to the ground
beneath jumping objects.
The article after that
swaps the camera orientation
to look at the world horizontally
rather than from above.
The cluster after that
introduces parallax,
explicit depth,
and the oblique and axonometric viewing angles
that dominate strategy games and role-playing games.

The framing the series carries
from the opener
is that every two-dimensional game
must compute
both a forward map
and an inverse map.
The forward map
takes the world state
and produces the screen image.
The inverse map
takes a screen coordinate
and produces the world object
the player selected.
Top-down without height
makes both maps as cheap
as they can be.
The article treats them in turn,
walks a concrete worked example,
covers the variations
that real games introduce on top of the floor case,
enumerates the delivery mechanisms
period hardware used,
and closes with the canonical games
that defined the mode.

## A Brief History of the Mode

The earliest commercial top-down game
is debated
in the same way the earliest of anything
is debated,
but the [Atari 2600 release of Adventure][ref_adventure] in 1980
is widely cited
as the first top-down action game
on a home console.
[Pac-Man][ref_pacman]
in the same year
gave the arcade
its most enduring top-down maze.
[Bomberman][ref_bomberman]
in 1983
brought the grid-tile maze
to the home computer.
[Gauntlet][ref_gauntlet]
in 1985
gave the arcade
its top-down dungeon crawl.
[The Legend of Zelda][ref_zelda]
in 1986
gave the home console
its top-down adventure template.
[Pokemon Red and Blue][ref_pokemon_rb]
in 1996
gave the handheld
its top-down role-playing template,
which the franchise has now carried
through nine main generations.

Independent and modern releases
have kept the mode alive.
[The Binding of Isaac][ref_binding_of_isaac] in 2011,
[Hotline Miami][ref_hotline_miami] in 2012,
and [Stardew Valley][ref_stardew_valley] in 2016
all use a pure top-down without height
as their primary projection.
The roguelike tradition
from [NetHack][ref_nethack] forward
has used the top-down view
in either tile or character form
since the genre's earliest releases.

The mode persists
because the rendering cost is minimal,
the input handling is simple,
the player's spatial reasoning is unambiguous,
and the camera-and-world coupling
is the simplest possible.

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

In homogeneous form
the same map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & -z\, c_x + W/2 \\ 0 & z & -z\, c_y + H/2 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ 1 \end{bmatrix}.
$$

The matrix is the product
of three more elementary affine matrices,
a translation by $-\mathbf{c}$,
a uniform scale by $z$,
and a translation by $\mathbf{o}$.
Writing $T(\mathbf{v})$ for translation by $\mathbf{v}$
and $S(z)$ for uniform scale by $z$,
the forward map factors as

$$
F = T(\mathbf{o})\, S(z)\, T(-\mathbf{c}).
$$

The composition rule for affine matrices
from the opener
expresses the forward map
as a single matrix
that the engine stores
and applies per drawn object.
The factorisation is the pattern
every projection mode in the series inherits,
with the choice of $S$
and the order of factors
distinguishing one mode from another.

The $y$-axis convention deserves an explicit note.
The world coordinate $y$
in this article
is taken to increase downward,
matching the screen $y$ direction
that the raster display imposes.
A reader designing a new engine
who prefers world-$y$ up
should negate the second row of the scale matrix
to get

$$
\mathbf{p}_{\text{screen}} = \begin{bmatrix} z & 0 \\ 0 & -z \end{bmatrix} (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o}.
$$

Either convention works.
The choice must be made once per project
and held consistently
across the rendering,
the input,
and the asset authoring.

## The Inverse Map

The forward map's matrix
is square,
two-by-two before the homogeneous augmentation,
and full rank
since $z > 0$.
The inverse therefore exists in closed form
and returns a unique world point
for every screen pixel.
Subtracting the screen centre offset
and dividing by the zoom yields

$$
\mathbf{p}_{\text{world}} = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \mathbf{c}.
$$

This is the floor case
of the inverse map family.
There is no missing dimension,
no ambiguity,
and no candidate set.
Every click corresponds to one world point.

The visible region of the world
is the pre-image of the screen rectangle
under the inverse map.
Substituting the screen corners
yields the world-space viewport

$$
\mathbf{p}_{\text{world}} \in \mathbf{c} + \frac{1}{z}\, \left[ -\tfrac{W}{2},\ \tfrac{W}{2} \right] \times \left[ -\tfrac{H}{2},\ \tfrac{H}{2} \right].
$$

This rectangle
is what the renderer iterates over
when culling invisible objects,
and is what the engine clamps the camera against
when the camera reaches a map boundary.

The picking step
takes the inverse-mapped world point
and resolves it
to a world-space object.
Three resolution strategies appear in practice.

The first is a hit-test
against the bounding rectangle
of each drawn object.
The engine iterates the visible objects
in reverse draw order,
and returns the first object
whose bounding rectangle
contains the clicked world point.
The cost is linear
in the number of visible objects
and is acceptable
when the visible count is small.

The second is a tile lookup.
The world is partitioned
into a uniform grid
of tile-sized cells.
The clicked world point
maps to a tile coordinate

$$
\mathbf{t} = \lfloor \mathbf{p}_{\text{world}} / s_{\text{tile}} \rfloor,
$$

where $s_{\text{tile}}$
is the tile size in world units.
The engine looks up the object
at that tile cell
in constant time.
Tile lookup is the canonical strategy
for grid-aligned games such as
Pokemon and Bomberman.

The third is a spatial index
such as a quadtree
or a uniform grid of object lists.
The engine queries the index
with the clicked world point
and receives a short list of candidates
to test against bounding rectangles.
Spatial indexing is appropriate
when the visible object count
exceeds a few dozen
and a linear scan
is too slow.

The series treats picking edge cases
in the dedicated cross-cutting article
later in the series.
For the floor case
the three strategies above
suffice.

## A Worked Example

Consider a top-down role-playing game
with the following parameters.
The screen is 800 pixels wide
and 600 pixels tall.
The zoom factor is $z = 1$,
one world unit per pixel.
The camera is centred on the player at world position
$\mathbf{c} = (500, 400)$.
The tile size is $s_{\text{tile}} = 32$ world units.

The forward map
for a tree
at world position $\mathbf{p}_{\text{world}} = (600, 350)$
proceeds as follows.
The camera-relative world position is
$(600 - 500, 350 - 400) = (100, -50)$.
The zoom multiplies each component by $1$,
giving $(100, -50)$.
The screen offset $\mathbf{o} = (400, 300)$
gives the final screen position

$$
\mathbf{p}_{\text{screen}} = (400 + 100, 300 + (-50)) = (500, 250).
$$

The inverse map
for a click at screen position $(500, 250)$
proceeds in reverse.
The screen-centre-relative pixel position is
$(500 - 400, 250 - 300) = (100, -50)$.
The reciprocal zoom multiplies each component by $1$,
giving $(100, -50)$.
Adding the camera position yields

$$
\mathbf{p}_{\text{world}} = (100 + 500, -50 + 400) = (600, 350).
$$

This is the tree's world position,
as expected.

The tile lookup
for the clicked world position $(600, 350)$
proceeds as follows.
Dividing by the tile size
gives $(600/32, 350/32) = (18.75, 10.9375)$.
The floor operation yields tile coordinate
$\mathbf{t} = (18, 10)$.
The engine looks up the world object at tile $(18, 10)$
and returns it.

Verifying the round-trip
shows that the forward map
followed by the inverse map
returns the original world position
within floating-point precision,

$$
F^{-1}(F(\mathbf{p}_{\text{world}})) = \mathbf{p}_{\text{world}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.
This invariant holds
for every projection mode in the series
and is the simplest correctness test
the engine can run.

## Variations Within the Mode

Real games introduce variations
on top of the floor case.
The variations affect the engine
but not the conceptual model.

A smooth camera
interpolates the camera position $\mathbf{c}$
between its current and target values
each frame,

$$
\mathbf{c}_{n+1} = \mathbf{c}_n + \alpha\, (\mathbf{c}_{\text{target}} - \mathbf{c}_n),
$$

where $\alpha \in (0, 1]$
is the interpolation factor per frame.
An $\alpha$ near $1$
snaps the camera to the target
in a few frames.
An $\alpha$ near $0$
produces a slow drift
that lags player motion
and emphasises a slower-paced gameplay feel.
The forward map is unchanged.
The picking pipeline
must use the rendered-frame camera position
rather than the target position,
since the rendered frame
is what the player saw
when the click occurred.

A camera with bounds
clamps the camera position
to keep the visible window inside the map,

$$
\mathbf{c} = \mathrm{clamp}\left( \mathbf{c}_{\text{target}},\ \mathbf{m}_{\min} + \tfrac{\mathbf{v}}{2},\ \mathbf{m}_{\max} - \tfrac{\mathbf{v}}{2} \right),
$$

where $\mathbf{m}_{\min}$ and $\mathbf{m}_{\max}$
are the world-space corners of the map
and $\mathbf{v} = (W/z,\ H/z)$
is the viewport size in world units.
The forward map is unchanged.
The clamping
introduces edge cases
near the map boundary
where the player is not at the screen centre
because the camera could not follow further.
The picking pipeline
is unaffected
as long as it uses the clamped camera position.

A dead-zone camera
moves the camera only when the player exits
a central rectangle
on the screen.
The forward map is unchanged.
The camera position
is updated lazily
in response to player motion.
The picking pipeline
is unaffected.

A look-ahead camera
offsets the camera position
in the direction of player motion
to show more of what is ahead.
The forward map is unchanged.
The camera position
includes a player-velocity-dependent offset.
The picking pipeline
must use the actual rendered camera position
including the look-ahead offset.

Tile-aligned movement
restricts the player position
to integer multiples of the tile size.
The forward map is unchanged.
The world coordinates
are discrete rather than continuous.
The picking pipeline
benefits from tile lookup
as the canonical strategy.

Sub-pixel positioning
permits the world position
to be a non-integer
even though the screen position
must round to integer pixels.
The forward map is unchanged.
The pixel-quantisation step from the opener
applies after the forward map
and discards the fractional part
for display.
Sub-pixel positioning matters
for smooth motion at low frame rates
and at low resolutions.

Discrete zoom levels
allow the zoom factor $z$
to take a small set of values,
typically powers of two,
selected by the player or by game state.
The forward map is unchanged.
The matrix recomputes
when the zoom changes.

A wrapping world
treats the world plane as a torus
where moving past one edge
returns the player to the opposite edge.
The forward map is unchanged
modulo the world dimensions.
The picking pipeline
must consider that the same world position
may appear on multiple parts of the screen
if the camera is near a wrapping edge.

## Delivery Mechanisms

The forward map
is so simple
that almost any rendering pipeline
can deliver it.
Period hardware
used the following five mechanisms.

The first is a tile-grid background layer
with hardware scroll registers.
The Nintendo Entertainment System
provided four background tile layers
and a scroll register
that the renderer added to the layer position
to produce the camera-relative offset.
The Super Nintendo Entertainment System
extended this with four background layers
and per-layer scroll registers.
The Sega Genesis
provided two background layers
with similar scroll-register support.
The math the hardware computed
was exactly the forward map of this article
with $z = 1$.

The second is sprite-on-tile-background
where the moving objects
are object-attribute-memory sprites
positioned in screen coordinates
that the engine recomputes per frame
from the world coordinates.
The background layer scrolls
as the camera moves.
The sprite layer
positions each sprite
at the camera-relative screen coordinate.
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
on personal computers
without dedicated tile-and-sprite hardware
and remained the dominant mechanism
for top-down games on the IBM PC
through the early 1990s.

The fourth is graphics-processing-unit-accelerated quad rendering.
Modern game engines such as
Unity,
Godot,
and Unreal
render the world
as a collection of textured quads
positioned by a camera transform
that is the forward map of this article.
The graphics processing unit
applies the matrix
in hardware
and produces the screen image.

The fifth is software-emulated tile rendering
on hardware with neither tile-and-sprite hardware
nor a graphics processing unit.
This delivery mechanism
appears on 8-bit microcomputers
without picture-processing-unit support
and on early handheld devices.
The engine maintains a tile map in central-processing-unit memory
and writes pixels to a frame buffer
through a software inner loop
that the engine has optimised for the target architecture.

All five
compute the same forward map
and are interchangeable
from the perspective of the picking pipeline.
The choice
trades implementation complexity,
memory budget,
and achievable frame rate.

## Where the Framing Breaks Down

Top-down without height is the wrong projection mode
when any of the following conditions hold.

When the gameplay requires height
the floor case loses the vertical axis
that platforming,
jumping,
or shadow-projecting objects
need.
The next article in the series
adds a decoupled vertical axis
that the floor case lacks.

When the world has explicit depth into the screen
the floor case loses the depth axis
that belt-scrolling
and three-quarter views need.
The third Cartesian-cluster article
adds an explicit depth axis
through belt-scrolling.

When the camera rotates with the player
the forward map gains an additional rotation matrix
between the camera-relative offset
and the screen offset.
This is the rotated-camera variant
of top-down
and is usually treated as a special case of axonometric projection
in the series.

When parallax is needed
to communicate depth
the floor case lacks the layered structure
that parallax requires.
The parallax variant of side-scrolling
provides the closest analogue.

When the visual style demands oblique elevation buildings
on a top-down map
the floor case is insufficient.
The hybrid projection
that the Mother series uses
is the closest match
and is treated in the stylised-hybrid article
later in the series.

When objects must occlude one another
in a way the camera-relative position alone cannot determine
the floor case requires augmentation
with an explicit draw order.
The draw-order article in the series
treats the painter's algorithm
and the Y-sort and Z-sort variants
in detail.

## The Canon

The following games
use top-down without height
as their primary projection mode.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Adventure][ref_adventure]
on the Atari 2600 in 1980
gave the home console
its first top-down action game.

[Pac-Man][ref_pacman]
in 1980
gave the arcade
its top-down maze.

[Bomberman][ref_bomberman]
in 1983
gave the home computer
its grid-tile maze.

[Gauntlet][ref_gauntlet]
in 1985
gave the arcade
its top-down dungeon crawl.

[The Legend of Zelda][ref_zelda]
on the Famicom and Nintendo Entertainment System in 1986
gave the home console
its top-down adventure template.

[NetHack][ref_nethack],
first released in 1987
and descended from earlier roguelikes,
gave the personal computer
its top-down character-grid dungeon.

[Pokemon Red and Blue][ref_pokemon_rb]
on the Game Boy in 1996
gave the handheld
its top-down role-playing template.

[The Binding of Isaac][ref_binding_of_isaac]
on Microsoft Windows in 2011
gave the modern independent game
its top-down roguelike template.

[Hotline Miami][ref_hotline_miami]
on Microsoft Windows in 2012
gave the modern independent game
its top-down combat template.

[Stardew Valley][ref_stardew_valley]
on Microsoft Windows in 2016
gave the modern independent game
its top-down farming-and-life-simulation template.

Each game in the canon
exercises a different subset of the variations
that the section above enumerated.
Pac-Man uses a fixed camera
with no zoom.
The Legend of Zelda uses flip-screen scrolling
with a snapped camera
at room boundaries.
Stardew Valley uses a smoothly-tracking camera
with sub-pixel positioning.
The forward map and the inverse map
remain the same equations
across the canon.

## Out of Scope

The article does not cover
the following.

Tile-based pathfinding,
including A-star,
Dijkstra's algorithm,
and the navigation-mesh variants,
is a separate algorithmic subject
that the series defers.

Procedural generation
of top-down maps,
including dungeon generators,
wave-function collapse,
and noise-based terrain,
is a content-authoring subject
adjacent to but distinct from
the projection math.

Rendering optimisation techniques
such as dirty-rectangle redraw,
view-frustum culling,
and texture atlasing
are implementation concerns
the series treats only at the level
of the delivery-mechanism sidebar.

The choice between top-down and first-person
for a given game
is a design question
the series does not adjudicate.
Each projection mode
has games
for which it is the right choice
and games
for which it is the wrong choice.

The dual case where the world is top-down
but objects use side-elevation art
is the stylised hybrid
of the [Mother][ref_mother_1] series
and is treated later in the series.

## Conclusion

Top-down without height
is the floor case of the projection canon.
The forward map
is a camera-relative translation
followed by a uniform zoom
and a screen-centre offset.
The inverse map
is the closed-form inverse
of the same transformation.
Picking
reduces to a hit test
against the bounding rectangle,
a tile lookup,
or a spatial index query,
depending on the world structure.
The math is simple
and the implementation
admits five distinct delivery mechanisms
on period hardware.
The next article in the series
adds a decoupled vertical axis
to the floor case
and treats the height-dependent forward map,
the height-introduced ambiguity in the inverse map,
and the shadow-drop convention
that makes the height axis legible to the player.

## References

- [Reference, Adventure][ref_adventure]
- [Reference, Bomberman][ref_bomberman]
- [Reference, Gauntlet][ref_gauntlet]
- [Reference, Hotline Miami][ref_hotline_miami]
- [Reference, Mother][ref_mother_1]
- [Reference, NetHack][ref_nethack]
- [Reference, Pac-Man][ref_pacman]
- [Reference, Pokemon Red and Blue][ref_pokemon_rb]
- [Reference, Stardew Valley][ref_stardew_valley]
- [Reference, The Binding of Isaac][ref_binding_of_isaac]
- [Reference, The Legend of Zelda][ref_zelda]

[ref_adventure]: https://en.wikipedia.org/wiki/Adventure_(1980_video_game)
[ref_binding_of_isaac]: https://en.wikipedia.org/wiki/The_Binding_of_Isaac_(video_game)
[ref_bomberman]: https://en.wikipedia.org/wiki/Bomberman_(1983_video_game)
[ref_gauntlet]: https://en.wikipedia.org/wiki/Gauntlet_(1985_video_game)
[ref_hotline_miami]: https://en.wikipedia.org/wiki/Hotline_Miami
[ref_mother_1]: https://en.wikipedia.org/wiki/EarthBound_Beginnings
[ref_nethack]: https://en.wikipedia.org/wiki/NetHack
[ref_pacman]: https://en.wikipedia.org/wiki/Pac-Man
[ref_pokemon_rb]: https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red_and_Blue
[ref_stardew_valley]: https://en.wikipedia.org/wiki/Stardew_Valley
[ref_zelda]: https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)
