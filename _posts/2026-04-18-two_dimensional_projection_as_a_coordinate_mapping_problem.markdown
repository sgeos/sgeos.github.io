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
\tag{1}
$$

where $\mathbf{p}\_{\text{world}}$
is the position of the object in the game world,
$\mathbf{p}\_{\text{screen}}$
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
\tag{2}
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
\tag{3}
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
\tag{4}
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
\tag{5}
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
\tag{6}
$$

with the inverse

$$
F^{-1} = M^{-1}\, V^{-1}\, C^{-1}.
\tag{7}
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
\tag{8}
$$

In the projection-with-depth cases
where world coordinates are three-dimensional
and the projection matrix is two-by-three,
the inverse returns a line in the world

$$
\mathbf{p}_{\text{world}}(s) = \mathbf{p}_0 + s\, \mathbf{d},
\tag{9}
$$

parameterised by a depth scalar $s$
along a direction $\mathbf{d}$
through a known reference point $\mathbf{p}\_0$.

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
\tag{10}
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
\tag{11}
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

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 11 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 11, 11 are established and 0 are bespoke.
Screen coordinates are measured in pixels with $y$ increasing downward in the raster frame and upward in the centred mathematical frame, while world coordinates carry whatever units the game chooses, so the sign of every vertical term depends on which frame an equation is written in.

**Equation 1, General Affine Projection.**
A screen position is a linear map of the world position followed by a translation, the general affine form that every projection in the series specialises.

$$
\mathbf{p}_{\text{screen}} = A\, \mathbf{p}_{\text{world}} + \mathbf{t},
\tag{1}
$$

**Equation 2, Affine Projection of Three Dimensions into Two in Components.**
The affine projection from a three-dimensional world to a two-dimensional screen is written out with a two-by-three matrix of six entries and a two-component translation.

$$
\begin{bmatrix} s_x \\ s_y \end{bmatrix} =
\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \end{bmatrix} +
\begin{bmatrix} t_x \\ t_y \end{bmatrix}.
\tag{2}
$$

**Equation 3, Homogeneous Projection to Clip Space.**
A four-by-four projection matrix carries a homogeneous world position to a homogeneous clip-space position, as in a three-dimensional graphics pipeline.

$$
\tilde{\mathbf{p}}_{\text{clip}} = P\, \tilde{\mathbf{p}}_{\text{world}},
\tag{3}
$$

**Equation 4, Perspective Divide.**
The screen position is recovered by dividing the first two clip-space components by the fourth, the step that makes a perspective projection nonlinear.

$$
\mathbf{p}_{\text{screen}} =
\frac{1}{\tilde{p}_{\text{clip},4}}
\begin{bmatrix} \tilde{p}_{\text{clip},1} \\ \tilde{p}_{\text{clip},2} \end{bmatrix}.
\tag{4}
$$

**Equation 5, Two-Dimensional Affine Map in Homogeneous Coordinates.**
Appending a unit row to the matrix and a unit entry to each position folds the translation into a single three-by-three matrix product.

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} a_{11} & a_{12} & t_x \\ a_{21} & a_{22} & t_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ 1 \end{bmatrix}.
\tag{5}
$$

**Equation 6, Composed Forward Map.**
The forward map is the product of the camera-to-screen, world-to-camera and object-to-world matrices, applied from right to left.

$$
F = C\, V\, M,
\tag{6}
$$

**Equation 7, Inverse of the Composed Forward Map.**
The inverse of a product of invertible matrices is the product of their inverses in reverse order.

$$
F^{-1} = M^{-1}\, V^{-1}\, C^{-1}.
\tag{7}
$$

**Equation 8, Inverse of an Invertible Affine Map.**
When the world is two-dimensional and the matrix is square and invertible, subtracting the translation and applying the inverse matrix returns a unique world point.

$$
\mathbf{p}_{\text{world}} = A^{-1}\, (\mathbf{p}_{\text{screen}} - \mathbf{t}).
\tag{8}
$$

**Equation 9, Preimage Line of a Screen Point.**
When a three-dimensional world projects onto a two-dimensional screen, the preimage of a screen point is a line through a reference point along a direction, parameterised by a depth scalar.

$$
\mathbf{p}_{\text{world}}(s) = \mathbf{p}_0 + s\, \mathbf{d},
\tag{9}
$$

**Equation 10, Mathematical Frame to Raster Frame.**
Negating the vertical component and adding half the screen width and height moves the origin from the centre to the top-left corner and turns $y$ downward.

$$
\mathbf{p}_{\text{raster}} =
\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \mathbf{p}_{\text{math}} +
\begin{bmatrix} W/2 \\ H/2 \end{bmatrix},
\tag{10}
$$

**Equation 11, Pixel Quantisation by Rounding.**
A continuous screen coordinate becomes a discrete pixel address by adding one half to each component and taking the floor, which rounds to the nearest pixel.

$$
\mathbf{p}_{\text{pixel}} = \lfloor \mathbf{p}_{\text{screen}} + \tfrac{1}{2}\, \mathbf{1} \rfloor,
\tag{11}
$$

### Notation

- $\mathbf{p}_{\text{world}}$, the position of an object in the game world
- $\mathbf{p}_{\text{screen}}$, the position of the image of an object on the screen
- $A$, the projection matrix encoding rotation, scaling and shearing
- $\mathbf{t}$, the translation accounting for camera position and screen origin
- $P$, a four-by-four homogeneous projection matrix
- $M$, the object-local-to-world matrix
- $V$, the world-to-camera matrix
- $C$, the camera-to-screen matrix
- $F$, the composed forward map from object to screen
- $s$, the depth scalar parameterising the preimage line
- $\mathbf{d}$, the direction of the preimage line
- $\mathbf{p}_0$, a known reference point on the preimage line
- $W$, the screen width in pixels
- $H$, the screen height in pixels
- $\mathbf{1}$, the all-ones vector

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "2D Computer Graphics." 2026. Wikipedia. Last modified May 24, at 05:24 (UTC). [https://en.wikipedia.org/w/index.php?title=2D\_computer\_graphics&oldid=1355838514][ref_2d_computer_graphics]
- "Adventure (1980 Video Game)." 2026. Wikipedia. Last modified May 14, at 19:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Adventure\_(1980\_video\_game)&oldid=1354171370][ref_adventure]
- "Affine Transformation." 2026. Wikipedia. Last modified May 2, at 17:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Affine\_transformation&oldid=1352187787][ref_affine_transformation]
- "Asteroids (Video Game)." 2026. Wikipedia. Last modified June 18, at 06:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Asteroids\_(video\_game)&oldid=1359945798][ref_asteroids]
- "Battle Clash." 2026. Wikipedia. Last modified May 2, at 00:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Battle\_Clash&oldid=1352091262][ref_battle_clash]
- "Battlezone (1980 Video Game)." 2026. Wikipedia. Last modified June 23, at 01:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Battlezone\_(1980\_video\_game)&oldid=1360693691][ref_battlezone]
- "Build (Game Engine)." 2026. Wikipedia. Last modified June 4, at 20:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Build\_(game\_engine)&oldid=1357806026][ref_build_engine]
- "Civilization II." 2026. Wikipedia. Last modified June 4, at 22:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Civilization\_II&oldid=1357824807][ref_civ2]
- "Computer Graphics: Principles and Practice." 2026. Wikipedia. Last modified January 31, at 18:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Computer\_Graphics%3A\_Principles\_and\_Practice&oldid=1335880399][ref_foley_van_dam]
- "Diablo (Video Game)." 2026. Wikipedia. Last modified May 11, at 18:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Diablo\_(video\_game)&oldid=1353675675][ref_diablo]
- "Donkey Kong (1981 Video Game)." 2026. Wikipedia. Last modified June 27, at 00:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Donkey\_Kong\_(1981\_video\_game)&oldid=1361297817][ref_donkey_kong]
- "Doom (1993 Video Game)." 2026. Wikipedia. Last modified June 22, at 15:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Doom\_(1993\_video\_game)&oldid=1360613702][ref_doom]
- "Double Dragon (Video Game)." 2026. Wikipedia. Last modified May 10, at 20:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Double\_Dragon\_(video\_game)&oldid=1353533774][ref_double_dragon]
- "EarthBound Beginnings." 2026. Wikipedia. Last modified May 20, at 18:14 (UTC). [https://en.wikipedia.org/w/index.php?title=EarthBound\_Beginnings&oldid=1355235632][ref_mother_1]
- "F-Zero (Video Game)." 2026. Wikipedia. Last modified June 20, at 01:36 (UTC). [https://en.wikipedia.org/w/index.php?title=F-Zero\_(video\_game)&oldid=1360225771][ref_f_zero]
- "Final Fight." 2026. Wikipedia. Last modified May 24, at 13:36 (UTC). [https://en.wikipedia.org/w/index.php?title=Final\_Fight&oldid=1355885104][ref_final_fight]
- "The Legend of Zelda (Video Game)." 2026. Wikipedia. Last modified June 15, at 07:09 (UTC). [https://en.wikipedia.org/w/index.php?title=The\_Legend\_of\_Zelda\_(video\_game)&oldid=1359431616][ref_zelda]
- "Mode 7." 2026. Wikipedia. Last modified June 9, at 17:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Mode\_7&oldid=1358589212][ref_mode_7]
- "Pac-Man." 2026. Wikipedia. Last modified June 1, at 06:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Pac-Man&oldid=1357187372][ref_pacman]
- "Pole Position." 2026. Wikipedia. Last modified May 26, at 15:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Pole\_Position&oldid=1356240589][ref_pole_position]
- "Pong." 2026. Wikipedia. Last modified May 21, at 10:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Pong&oldid=1355352944][ref_pong]
- "Projection (Linear Algebra)." 2026. Wikipedia. Last modified May 17, at 09:13 (UTC). [https://en.wikipedia.org/w/index.php?title=Projection\_(linear\_algebra)&oldid=1354597494][ref_projection_linear_algebra]
- "Renegade (Video Game)." 2026. Wikipedia. Last modified May 9, at 02:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Renegade\_(video\_game)&oldid=1353246370][ref_renegade]
- "SimCity (1989 Video Game)." 2026. Wikipedia. Last modified May 25, at 05:31 (UTC). [https://en.wikipedia.org/w/index.php?title=SimCity\_(1989\_video\_game)&oldid=1356007402][ref_simcity]
- "SimCity 2000." 2026. Wikipedia. Last modified May 3, at 17:33 (UTC). [https://en.wikipedia.org/w/index.php?title=SimCity\_2000&oldid=1352345344][ref_simcity_2000]
- "Sonic the Hedgehog (1991 Video Game)." 2026. Wikipedia. Last modified June 25, at 07:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Sonic\_the\_Hedgehog\_(1991\_video\_game)&oldid=1361042922][ref_sonic]
- "Space Harrier." 2026. Wikipedia. Last modified June 24, at 02:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_Harrier&oldid=1360865377][ref_space_harrier]
- "Space Invaders." 2026. Wikipedia. Last modified June 24, at 19:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_Invaders&oldid=1360963933][ref_space_invaders]
- "Streets of Rage (Video Game)." 2026. Wikipedia. Last modified March 25, at 01:36 (UTC). [https://en.wikipedia.org/w/index.php?title=Streets\_of\_Rage\_(video\_game)&oldid=1345231413][ref_streets_of_rage]
- "Super Mario Bros." 2026. Wikipedia. Last modified June 24, at 21:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Super\_Mario\_Bros.&oldid=1360979955][ref_super_mario_bros]
- "Super Mario Kart." 2026. Wikipedia. Last modified June 26, at 18:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Super\_Mario\_Kart&oldid=1361251845][ref_mario_kart]
- "Ultima IV: Quest of the Avatar." 2026. Wikipedia. Last modified June 1, at 15:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Ultima\_IV%3A\_Quest\_of\_the\_Avatar&oldid=1357244143][ref_ultima_iv]
- "Wolfenstein 3D." 2026. Wikipedia. Last modified June 2, at 23:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Wolfenstein\_3D&oldid=1357494941][ref_wolfenstein]

[ref_2d_computer_graphics]: https://en.wikipedia.org/w/index.php?title=2D_computer_graphics&oldid=1355838514
[ref_adventure]: https://en.wikipedia.org/w/index.php?title=Adventure_(1980_video_game)&oldid=1354171370
[ref_affine_transformation]: https://en.wikipedia.org/w/index.php?title=Affine_transformation&oldid=1352187787
[ref_asteroids]: https://en.wikipedia.org/w/index.php?title=Asteroids_(video_game)&oldid=1359945798
[ref_battle_clash]: https://en.wikipedia.org/w/index.php?title=Battle_Clash&oldid=1352091262
[ref_battlezone]: https://en.wikipedia.org/w/index.php?title=Battlezone_(1980_video_game)&oldid=1360693691
[ref_build_engine]: https://en.wikipedia.org/w/index.php?title=Build_(game_engine)&oldid=1357806026
[ref_civ2]: https://en.wikipedia.org/w/index.php?title=Civilization_II&oldid=1357824807
[ref_diablo]: https://en.wikipedia.org/w/index.php?title=Diablo_(video_game)&oldid=1353675675
[ref_donkey_kong]: https://en.wikipedia.org/w/index.php?title=Donkey_Kong_(1981_video_game)&oldid=1361297817
[ref_doom]: https://en.wikipedia.org/w/index.php?title=Doom_(1993_video_game)&oldid=1360613702
[ref_double_dragon]: https://en.wikipedia.org/w/index.php?title=Double_Dragon_(video_game)&oldid=1353533774
[ref_f_zero]: https://en.wikipedia.org/w/index.php?title=F-Zero_(video_game)&oldid=1360225771
[ref_final_fight]: https://en.wikipedia.org/w/index.php?title=Final_Fight&oldid=1355885104
[ref_foley_van_dam]: https://en.wikipedia.org/w/index.php?title=Computer_Graphics%3A_Principles_and_Practice&oldid=1335880399
[ref_mario_kart]: https://en.wikipedia.org/w/index.php?title=Super_Mario_Kart&oldid=1361251845
[ref_mode_7]: https://en.wikipedia.org/w/index.php?title=Mode_7&oldid=1358589212
[ref_mother_1]: https://en.wikipedia.org/w/index.php?title=EarthBound_Beginnings&oldid=1355235632
[ref_pacman]: https://en.wikipedia.org/w/index.php?title=Pac-Man&oldid=1357187372
[ref_pole_position]: https://en.wikipedia.org/w/index.php?title=Pole_Position&oldid=1356240589
[ref_pong]: https://en.wikipedia.org/w/index.php?title=Pong&oldid=1355352944
[ref_projection_linear_algebra]: https://en.wikipedia.org/w/index.php?title=Projection_(linear_algebra)&oldid=1354597494
[ref_renegade]: https://en.wikipedia.org/w/index.php?title=Renegade_(video_game)&oldid=1353246370
[ref_simcity]: https://en.wikipedia.org/w/index.php?title=SimCity_(1989_video_game)&oldid=1356007402
[ref_simcity_2000]: https://en.wikipedia.org/w/index.php?title=SimCity_2000&oldid=1352345344
[ref_sonic]: https://en.wikipedia.org/w/index.php?title=Sonic_the_Hedgehog_(1991_video_game)&oldid=1361042922
[ref_space_harrier]: https://en.wikipedia.org/w/index.php?title=Space_Harrier&oldid=1360865377
[ref_space_invaders]: https://en.wikipedia.org/w/index.php?title=Space_Invaders&oldid=1360963933
[ref_streets_of_rage]: https://en.wikipedia.org/w/index.php?title=Streets_of_Rage_(video_game)&oldid=1345231413
[ref_super_mario_bros]: https://en.wikipedia.org/w/index.php?title=Super_Mario_Bros.&oldid=1360979955
[ref_ultima_iv]: https://en.wikipedia.org/w/index.php?title=Ultima_IV%3A_Quest_of_the_Avatar&oldid=1357244143
[ref_wolfenstein]: https://en.wikipedia.org/w/index.php?title=Wolfenstein_3D&oldid=1357494941
[ref_zelda]: https://en.wikipedia.org/w/index.php?title=The_Legend_of_Zelda_(video_game)&oldid=1359431616
