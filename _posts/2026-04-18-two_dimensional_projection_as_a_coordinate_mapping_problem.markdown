---
layout: post
mathjax: true
comments: true
title:  "Two-Dimensional Projection as a Coordinate Mapping Problem"
date:   2026-04-18 09:00:00 +0000
categories: games graphics projection
series: two_dimensional_projection
series_title: Two-Dimensional Projection in Games
series_index: 1
---
<!-- A173 -->
<script>console.log("A173");</script>

Every two-dimensional game
must answer two coordinate questions
on every frame.
The first question
is where each object in the game world
appears on the screen.
The second question
is what object the player has selected
when the player clicks,
taps,
or fires a light gun
at a screen coordinate.
These two questions
are duals of one another.
The rendering pipeline
computes the first.
The input pipeline
computes the second.
Both pipelines
use the same mathematical apparatus
running in opposite directions.

This series treats the projection math
behind the two-dimensional game canon.
It covers the forward map
from world coordinates
to screen coordinates
that the renderer needs,
and the inverse map
from screen coordinates
back to world coordinates
that the input handler needs.
The treatment is mathematical
rather than historical,
although historical examples
anchor each projection mode.
The mathematics is implementation-agnostic.
A separate concern,
addressed throughout the series
under the label of delivery mechanism,
is how the math gets executed on actual hardware,
whether by software loops
on a general-purpose central processing unit,
by dedicated picture-processing-unit registers,
by background-layer affine transforms,
by software rotation
followed by sprite-memory blitting,
or by modern graphics-processing-unit shaders.
The distinction matters
because the same math
can be delivered by any of these mechanisms
with the conceptual model unchanged.

The opener establishes the framing.
The fourteen follow-on articles
walk the canon of two-dimensional projection modes
one at a time.
Each article carries
the forward map,
the inverse map,
a worked numerical example,
the picking math,
the recurring delivery-mechanism sidebar,
and a closing list of canonical games.
Two cross-cutting articles
cover draw order
and picking edge cases.
A closing article unifies the entire series
under the affine and projective matrix framework
that modern graphics-processing-unit hardware
made the standard pipeline.

## The Two-Question Problem

Every two-dimensional game
must compute two coordinate mappings
during the same frame.
The first mapping
takes the state of the world,
the position and pose of every visible object,
and produces a list of screen pixels
to be coloured.
This is the forward map.
It is the central computation
of the rendering pipeline.
The second mapping
takes a screen pixel,
typically supplied by a mouse,
a touchscreen,
a controller crosshair,
or a light gun,
and produces the world-space object,
or set of candidate objects,
that the pixel corresponds to.
This is the inverse map.
It is the central computation
of the input handling pipeline.

The two mappings
are not independent.
They are duals
in the formal sense.
The forward map
is a function from world coordinates to screen coordinates.
The inverse map
is the pre-image of the forward map
under the same set of parameters.
Whatever rotation,
scaling,
translation,
or shearing
the forward map applied to a sprite
when the renderer drew it,
the inverse map
must undo
to determine which sprite a click selected.

The duality has three consequences
that this series returns to repeatedly.
First,
the engine must persist
the forward-map parameters
used to draw each visible object on each frame,
because the picking pipeline
will need to invert those exact parameters
when an input event arrives,
possibly several frames later.
Second,
the picking ambiguities
that arise from the inverse map being lossy
can be analysed in advance
and resolved by explicit policy
rather than by ad-hoc heuristics.
Third,
the cost trade-offs
of different delivery mechanisms
can be evaluated
without changing the picking code,
because the picking code
depends only on the abstract transform,
not on its implementation.

## A Brief Historical Sketch

The two-dimensional game canon
has accumulated projection modes
incrementally over five decades.
The first generation of arcade games
used pure frontal projection
where the world is the screen,
exemplified by [Pong][ref_pong] in 1972
and [Space Invaders][ref_space_invaders] in 1978.
The early home-computer and arcade era
added side-scrolling,
with [Donkey Kong][ref_donkey_kong] in 1981
and [Super Mario Bros][ref_super_mario_bros] in 1985.
Top-down projection
arrived with [Pac-Man][ref_pacman] in 1980
and matured with [Adventure][ref_adventure]
on the Atari 2600 the same year,
and with [The Legend of Zelda][ref_zelda] in 1986.
Oblique and quarter-view projection
appeared in late-1980s personal-computer role-playing games,
with [Ultima IV][ref_ultima_iv] in 1985
and [SimCity][ref_simcity] in 1989.
Axonometric projection
became commercially dominant
with [SimCity 2000][ref_simcity_2000] in 1993,
[Civilization II][ref_civ2] in 1996,
and [Diablo][ref_diablo] in 1996.

Layered parallax
matured on the Sega Genesis
with [Sonic the Hedgehog][ref_sonic] in 1991.
Belt-scrolling,
sometimes called side-with-depth,
arrived with [Renegade][ref_renegade] in 1986
and matured with [Double Dragon][ref_double_dragon] in 1987,
[Final Fight][ref_final_fight] in 1989,
and [Streets of Rage][ref_streets_of_rage] in 1991.
The affine ground plane
known as [Mode 7][ref_mode_7]
launched with [F-Zero][ref_f_zero] in 1990
and [Super Mario Kart][ref_mario_kart] in 1992.
Raycasting
arrived with [Wolfenstein 3D][ref_wolfenstein] in 1992.
Sprite-scaling pseudo-three-dimensional
preceded all of these in the arcade,
with [Pole Position][ref_pole_position] in 1982
and [Space Harrier][ref_space_harrier] in 1985,
and reached its first-person form
with [Battle Clash][ref_battle_clash]
on the Super Nintendo Entertainment System in 1992.
Stylised hybrid projections
that combine orthographic ground
with side-elevation buildings
arrived with [Mother][ref_mother_1]
on the Famicom in 1989.

This sketch is incomplete.
Many minor variations exist
within each named family.
The series treats each named family
in its own article,
with the math derived from first principles
and the canonical games named for context.

## The Forward Map and Its Inverse

A projection in this series
is a function
that maps world coordinates
to screen coordinates.
The general affine form
is

$$
\mathbf{p}_{\text{screen}} = A\, \mathbf{p}_{\text{world}} + \mathbf{t},
$$

where $\mathbf{p}_{\text{world}}$
is the position of the object in the game world,
$\mathbf{p}_{\text{screen}}$
is the position of its image on the screen,
$A$ is a matrix
that encodes rotation,
scaling,
and shearing,
and $\mathbf{t}$ is a translation
that accounts for camera position
and screen origin.

When the world is two-dimensional
and the screen is two-dimensional,
the matrix $A$ is a two-by-two
with four entries.
When the world is three-dimensional
and the screen is two-dimensional,
the matrix is a two-by-three
with six entries.
In components,
the three-into-two affine projection
is

$$
\begin{bmatrix} s_x \\ s_y \end{bmatrix} =
\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \end{bmatrix} +
\begin{bmatrix} t_x \\ t_y \end{bmatrix}.
$$

The matrix entries
depend on the projection mode.
A top-down projection without height
collapses to the identity
on the $(x, y)$ subspace.
An axonometric projection
encodes a rotation
followed by a non-uniform scale.
An oblique projection
encodes an axis-aligned shear.
The affine ground plane
known as Mode 7
encodes a per-frame rotation,
scale,
and translation
applied uniformly to a textured plane.
Raycasting
encodes a perspective projection
sampled along discrete screen columns.
Each named projection mode in the series
is a particular family of choices
for the matrix entries.

The projective generalisation,
which captures the perspective division
that the polygon era made standard,
writes positions in homogeneous form
$\tilde{\mathbf{p}} = [\, p_x,\ p_y,\ p_z,\ 1 \,]^{\mathsf T}$
and produces

$$
\tilde{\mathbf{p}}_{\text{clip}} = P\, \tilde{\mathbf{p}}_{\text{world}},
$$

where $P$ is a four-by-four projection matrix.
The on-screen coordinate
is obtained from the clip-space output
by dividing the first two components
by the fourth component,

$$
\mathbf{p}_{\text{screen}} =
\frac{1}{\tilde{p}_{\text{clip},4}}
\begin{bmatrix} \tilde{p}_{\text{clip},1} \\ \tilde{p}_{\text{clip},2} \end{bmatrix}.
$$

The affine form
is the projective form
with the fourth component of the result
constant across the scene.
The series treats only the affine form
and the constant-depth slice of the projective form,
since the polygon-era projective pipeline
is a separate body of literature.

The affine form
is conveniently written in homogeneous coordinates
by appending a unit row to the matrix
and a unit entry to each position vector,

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} a_{11} & a_{12} & t_x \\ a_{21} & a_{22} & t_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ 1 \end{bmatrix}.
$$

The translation
becomes part of the matrix,
and the composition of two affine transforms
is the product of their matrices.
A world-to-screen transform
that wants to compose
an object-local-to-world matrix $M$,
a world-to-camera matrix $V$,
and a camera-to-screen matrix $C$,
writes the composed forward map as

$$
F = C\, V\, M,
$$

with the inverse

$$
F^{-1} = M^{-1}\, V^{-1}\, C^{-1}.
$$

The series uses the non-homogeneous form
for clarity at first introduction of each projection mode,
and uses the homogeneous form
when transforms must be composed
across an object hierarchy
or across frames.
The closing article unifies the composition framework
under the projective generalisation
that modern graphics-processing-unit hardware made standard.

The forward map
is well-defined.
Every world coordinate
has exactly one screen coordinate.
The map may project multiple world coordinates
to the same screen coordinate,
since the dimension reduction
from world to screen
is one-to-many in general,
but each individual world coordinate
goes to exactly one screen pixel.

The inverse map
is fundamentally lossy.
The forward map collapses one or more dimensions.
The inverse therefore returns
one of three things,
depending on the projection mode.

In the strict two-dimensional case
where world coordinates are also two-dimensional
and the projection matrix $A$ is square and invertible,
the inverse returns a unique world point

$$
\mathbf{p}_{\text{world}} = A^{-1}\, (\mathbf{p}_{\text{screen}} - \mathbf{t}).
$$

In the projection-with-depth cases
where world coordinates are three-dimensional
and the projection matrix is two-by-three,
the inverse returns a line in the world

$$
\mathbf{p}_{\text{world}}(s) = \mathbf{p}_0 + s\, \mathbf{d},
$$

parameterised by a depth scalar $s$
along a direction $\mathbf{d}$
through a known reference point $\mathbf{p}_0$.

In the projection-with-ambiguity cases
where the depth coordinate is decoupled
and multiple world configurations
project to the same screen pixel,
the inverse returns an explicit set
of candidate world points,
each of which the picking pipeline must test
against the list of visible objects.

The practical inverse
is always the same algorithm
in three steps.
First,
compute the analytical pre-image
of the screen coordinate under the projection,
parameterised by the missing dimension or dimensions.
Second,
intersect that pre-image
with the list of visible objects,
in reverse draw order,
until a hit is found.
Third,
return the hit object
and its world-space hit position.

## The Math-Versus-Delivery Distinction

A theme that recurs throughout the series
is the distinction
between the projection mathematics
and the rendering pipeline
that delivers it to the screen.
The projection mathematics
is the conceptual model.
The rendering pipeline
is the implementation.

The same affine matrix
can be executed
by at least five different delivery mechanisms
on period hardware.

The first is software computation
on a general-purpose central processing unit,
with the result written to video memory
each frame.
This was the universal delivery mechanism
on personal computers
without dedicated graphics hardware,
and remained the dominant mechanism
for any projection
too complex for the picture-processing-unit registers.

The second is hardware sprite scaling or rotation
supported natively by the picture-processing-unit object layer.
Arcade hardware
from the mid-1980s onward,
and home consoles
starting with the Super Nintendo Entertainment System,
provided dedicated registers
for these transforms.

The third is affine background transformation
applied to a background layer
whose content the renderer treats
as a single large sprite.
The Super Nintendo Mode 7 background
is the canonical example,
used both for actual ground planes
and for individual transformed objects
where the object-layer hardware was insufficient.

The fourth is pre-rendered transform frames
stored in read-only memory
and selected at runtime
by quantising the desired parameters
to the nearest available frame.
This delivery mechanism
trades cartridge memory
for central-processing-unit cycles,
and was the standard approach
for sprite rotation
on hardware that did not support the transform natively.

The fifth is co-processor acceleration,
such as the Super FX,
the digital signal processor coprocessors,
or the CX4,
executing the matrix math
off the main central processing unit
and returning the transformed bitmap.

All five
compute the same forward map.
The hardware path
determines the achievable frame rate,
the achievable precision,
and the memory budget.
The hardware path
does not determine
the projection math the game is performing.

This distinction matters
for two reasons.
First,
it lets the article series
treat the math
without conflating it
with whichever delivery mechanism
happens to be canonical
for a particular game console.
Second,
it lets the picking pipeline
work the same way
regardless of how the forward map was rendered.
The inverse map
depends only on the transform parameters,
not on whether those parameters
were computed in software
or by hardware registers.

The recurring sidebar in each article
names two or three delivery mechanisms
for the mode at hand,
without expanding into a full implementation survey,
since the series scope
is the projection math
rather than the rendering pipeline.

## Notation Conventions for the Series

Vectors are written in bold lowercase.
Matrices in uppercase italic.
Scalars in italic lowercase.
World coordinates use the subscript "world",
and screen coordinates use the subscript "screen".
Where the world is two-dimensional,
the coordinates are $(x, y)$.
Where the world includes height or depth,
the coordinates are $(x, y, z)$,
with the convention that $z$
is the dimension perpendicular to the ground plane
in top-down views,
and perpendicular to the screen
in side views.

Screen coordinates
use the convention that $y$ increases downward,
matching the orientation of every two-dimensional raster device
since the introduction of the cathode-ray tube.
World coordinates
use the convention that $y$ increases upward
when the world is conceptually three-dimensional,
and increases downward
when the world is conceptually two-dimensional
and tracks the screen.
This dual convention
is the most common source of off-by-sign errors
in projection code,
and is explicitly called out
in each article.

The mapping between
the math-frame screen coordinate
with origin at the centre and $y$ increasing upward,
and the raster-frame screen coordinate
with origin at the top-left and $y$ increasing downward,
is

$$
\mathbf{p}_{\text{raster}} =
\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \mathbf{p}_{\text{math}} +
\begin{bmatrix} W/2 \\ H/2 \end{bmatrix},
$$

where $W$ and $H$ are the screen width and height in pixels.
This affine matrix
is itself an instance of the general form
the series treats,
and the inverse of it
is the first inverse map
the reader will compute by hand.

The continuous screen coordinate
becomes a discrete pixel address
by componentwise quantisation,

$$
\mathbf{p}_{\text{pixel}} = \lfloor \mathbf{p}_{\text{screen}} + \tfrac{1}{2}\, \mathbf{1} \rfloor,
$$

where $\mathbf{1}$ is the all-ones vector
and the floor function
is applied componentwise.
Sub-pixel positioning,
anti-aliasing,
and gamma correction
are downstream concerns
that the series treats only where relevant.

Time is treated as discrete frames.
The forward map at frame $n$ is denoted $F_n$,
and the inverse map at frame $n$ is denoted $F_n^{-1}$.
When a game must store transform parameters
from a past frame
for use by the input handler
several frames later,
the storage cost is explicitly noted.

Sprite-local coordinates use the subscript "local",
and represent the untransformed pixel positions
inside a sprite's authoring frame.
The forward transform
from sprite-local to screen
composes with the forward transform
from world to screen,
giving a single combined matrix
per drawn instance.

## The Series Roadmap

The fifteen articles
are organised into five clusters.

The opener
is the present article,
framing the problem
and setting notation.

The Cartesian cluster
carries five articles
on rectilinear projections.
These cover
top-down without height,
top-down with a decoupled vertical axis,
side-scrolling without depth,
side-scrolling with parallax layers,
and the belt-scroll variant
with explicit depth.

The oblique-and-axonometric cluster
carries two articles
on stylised three-quarter views.
These cover
oblique projection
in cavalier and cabinet variants
and the quarter view,
then isometric,
dimetric,
and trimetric axonometric projection.

The affine-and-projective cluster
carries three articles
on projections
that simulate three-dimensional motion
within a two-dimensional pipeline.
These cover
the affine ground plane known as Mode 7,
sprite-scaling pseudo-three-dimensional,
and raycasting.

A stylised-hybrid article
handles projections
that violate the affine matrix model.
This covers
the Mother-series ground-and-elevation hybrid,
per-scene projection switching,
layered silhouette projections,
and curved-world projections.

Two cross-cutting articles
treat draw order
and picking edge cases.
The closer
formalises the entire series
under the projection matrix framework
that modern graphics-processing-unit hardware
made standard.

Each article carries
a forward map,
an inverse map,
a worked numerical example,
the recurring math-versus-delivery sidebar,
and a closing list of canonical games.
Each article stands on its own
and may be read in isolation.
Read in sequence,
the articles compose
into a unified treatment
of the projection canon.

## Epistemic State

This article and the fourteen that follow
make claims of three kinds,
and the reader should evaluate each kind
on its own terms.

Mathematical claims
about projection matrices,
their inverses,
their conditioning,
and their composition
are derived from standard linear algebra
and from the standard computer-graphics literature.
These claims are fully verifiable
and should be treated as authoritative,
subject only to the reader's ability
to follow the derivations.

Historical claims
about which games introduced or popularised
which projection mode
are sourced primarily
from the published encyclopaedia article for each named game
and from the secondary literature on video-game history.
These claims are subject to the usual caveats
about precedence in software history,
where multiple games
developed similar techniques in parallel,
and the first published example
may not be the first developed example.
The series treats these claims as accurate
but flags individual cases
where the historical record is contested.

Implementation claims
about how specific hardware platforms
delivered specific projection modes
are sourced from the published hardware documentation
where it exists,
and from reverse-engineering work
by the homebrew and emulation communities
where the official documentation is incomplete.
Implementation claims about specific games,
particularly which delivery mechanism a given game used,
are flagged as inference
where the source is not authoritative.
A research-agent verification pass
is performed before publication
on the implementation claims
that have load-bearing analytical weight.

The series does not make normative claims
about which projection mode is better.
Each mode answers a particular set of design constraints,
and each has games
for which it is the right choice
and games
for which it is the wrong choice.

## Out of Scope

The series does not cover
the following.

True polygonal three-dimensional rendering.
The polygon pipeline
that became dominant with the PlayStation in 1994
and matured into the modern graphics-processing-unit pipeline
is the subject of a separate body of literature.
The series treats only
two-dimensional and pseudo-three-dimensional projections
that operate on raster sprite data.

Voxel rendering.
Comanche and similar height-map renderers
operate on a fundamentally different data model
and use techniques
that do not generalise
to the sprite-based two-dimensional canon.

Vector display rendering.
[Asteroids][ref_asteroids],
[Battlezone][ref_battlezone],
and similar vector games
use a fundamentally different rasterisation model
that does not have a per-pixel projection at all.

Binary space partition and portal rendering.
[Doom][ref_doom] and the [Build engine][ref_build_engine]
use projection math
that generalises raycasting
in ways that warrant their own treatment.
The series notes them as adjacent territory
in the raycasting article
but does not derive them.

Modern shader-based two-dimensional rendering.
While the math
is the same as the historical cases,
the implementation surface
is large enough to warrant its own series.
The math-versus-delivery sidebar in each article
notes when a given projection
is now typically delivered by a fragment shader.

Audio spatialisation.
The acoustic projection problem
is closely related to the visual projection problem
and uses similar mathematics,
but is a distinct subject
worth its own treatment.

## Conclusion

Every two-dimensional game
must compute a forward map
from world coordinates to screen coordinates
each frame,
and an inverse map
from screen coordinates back to world objects
each click or tap.
These two computations
are duals of one another.
The series treats them
as a unified mathematical problem,
across the projection modes
the two-dimensional game canon has accumulated.
The fourteen follow-on articles
walk the canon
one projection mode at a time.
The math is implementation-agnostic.
The delivery mechanism is treated as a separate concern
that can vary independently.
By the end of the series
the reader should be able to recognise
any two-dimensional game's projection mode on sight,
derive the forward and inverse maps for it from first principles,
and select an appropriate delivery mechanism
for a new implementation.

## References

- [Book, Computer Graphics Principles and Practice][ref_foley_van_dam]
- [Reference, 2D Computer Graphics][ref_2d_computer_graphics]
- [Reference, Adventure][ref_adventure]
- [Reference, Affine Transformation][ref_affine_transformation]
- [Reference, Asteroids][ref_asteroids]
- [Reference, Battle Clash][ref_battle_clash]
- [Reference, Battlezone][ref_battlezone]
- [Reference, Build Engine][ref_build_engine]
- [Reference, Civilization II][ref_civ2]
- [Reference, Diablo][ref_diablo]
- [Reference, Donkey Kong][ref_donkey_kong]
- [Reference, Doom][ref_doom]
- [Reference, Double Dragon][ref_double_dragon]
- [Reference, F-Zero][ref_f_zero]
- [Reference, Final Fight][ref_final_fight]
- [Reference, Linear Algebra Projection][ref_projection_linear_algebra]
- [Reference, Mode 7][ref_mode_7]
- [Reference, Mother][ref_mother_1]
- [Reference, Pac-Man][ref_pacman]
- [Reference, Pole Position][ref_pole_position]
- [Reference, Pong][ref_pong]
- [Reference, Renegade][ref_renegade]
- [Reference, SimCity][ref_simcity]
- [Reference, SimCity 2000][ref_simcity_2000]
- [Reference, Sonic the Hedgehog][ref_sonic]
- [Reference, Space Harrier][ref_space_harrier]
- [Reference, Space Invaders][ref_space_invaders]
- [Reference, Streets of Rage][ref_streets_of_rage]
- [Reference, Super Mario Bros][ref_super_mario_bros]
- [Reference, Super Mario Kart][ref_mario_kart]
- [Reference, The Legend of Zelda][ref_zelda]
- [Reference, Ultima IV][ref_ultima_iv]
- [Reference, Wolfenstein 3D][ref_wolfenstein]

[ref_2d_computer_graphics]: https://en.wikipedia.org/wiki/2D_computer_graphics
[ref_adventure]: https://en.wikipedia.org/wiki/Adventure_(1980_video_game)
[ref_affine_transformation]: https://en.wikipedia.org/wiki/Affine_transformation
[ref_asteroids]: https://en.wikipedia.org/wiki/Asteroids_(video_game)
[ref_battle_clash]: https://en.wikipedia.org/wiki/Battle_Clash
[ref_battlezone]: https://en.wikipedia.org/wiki/Battlezone_(1980_video_game)
[ref_build_engine]: https://en.wikipedia.org/wiki/Build_(game_engine)
[ref_civ2]: https://en.wikipedia.org/wiki/Civilization_II
[ref_diablo]: https://en.wikipedia.org/wiki/Diablo_(video_game)
[ref_donkey_kong]: https://en.wikipedia.org/wiki/Donkey_Kong_(arcade_game)
[ref_doom]: https://en.wikipedia.org/wiki/Doom_(1993_video_game)
[ref_double_dragon]: https://en.wikipedia.org/wiki/Double_Dragon_(arcade_game)
[ref_f_zero]: https://en.wikipedia.org/wiki/F-Zero_(video_game)
[ref_final_fight]: https://en.wikipedia.org/wiki/Final_Fight
[ref_foley_van_dam]: https://en.wikipedia.org/wiki/Computer_Graphics:_Principles_and_Practice
[ref_mario_kart]: https://en.wikipedia.org/wiki/Super_Mario_Kart
[ref_mode_7]: https://en.wikipedia.org/wiki/Mode_7
[ref_mother_1]: https://en.wikipedia.org/wiki/EarthBound_Beginnings
[ref_pacman]: https://en.wikipedia.org/wiki/Pac-Man
[ref_pole_position]: https://en.wikipedia.org/wiki/Pole_Position_(video_game)
[ref_pong]: https://en.wikipedia.org/wiki/Pong
[ref_projection_linear_algebra]: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
[ref_renegade]: https://en.wikipedia.org/wiki/Renegade_(video_game)
[ref_simcity]: https://en.wikipedia.org/wiki/SimCity_(1989_video_game)
[ref_simcity_2000]: https://en.wikipedia.org/wiki/SimCity_2000
[ref_sonic]: https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_(1991_video_game)
[ref_space_harrier]: https://en.wikipedia.org/wiki/Space_Harrier
[ref_space_invaders]: https://en.wikipedia.org/wiki/Space_Invaders
[ref_streets_of_rage]: https://en.wikipedia.org/wiki/Streets_of_Rage_(video_game)
[ref_super_mario_bros]: https://en.wikipedia.org/wiki/Super_Mario_Bros.
[ref_ultima_iv]: https://en.wikipedia.org/wiki/Ultima_IV:_Quest_of_the_Avatar
[ref_wolfenstein]: https://en.wikipedia.org/wiki/Wolfenstein_3D
[ref_zelda]: https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)
