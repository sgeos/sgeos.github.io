---
layout: post
mathjax: true
comments: true
title:  "Axonometric Projection, Isometric, Dimetric, Trimetric"
date:   2026-04-25 09:00:00 +0000
categories: games graphics projection
---

<!-- A180 -->
<script>console.log("A180");</script>

The second article of the oblique-and-axonometric cluster
generalises the previous article's oblique projection
by rotating the world before parallel projection
rather than tilting the depth axis on the screen.
The result is an axonometric projection
in which the three world axes
take three distinct screen-space directions
at angles that the rotation determines.
The article distinguishes three classical variants
by the equality of the foreshortening factors
on the three projected world axes.
Isometric projection
has all three foreshortening factors equal
and produces the symmetric three-axis view
that engineering drawing schools formalised
in the nineteenth century.
Dimetric projection
has two foreshortening factors equal
and one different.
Trimetric projection
has all three different.

The article also distinguishes the strict mathematical isometric
from the game-industry isometric
that classic action role-playing games used.
The strict isometric
has foreshortening factor $\sqrt{2/3}$ on each axis
and 120-degree angles between projected axes,
which requires the height axis to project upward on screen
and is incompatible with the $y$-down convention
used throughout the series.
The article presents an equal-foreshortening isometric variant
under the $y$-down convention
as the closest practical equivalent.
The game-industry isometric
has tiles drawn at a two-to-one width-to-height pixel ratio
that mathematically classifies as dimetric.
The article uses the term game-iso
for the latter
to avoid the ambiguity
that the inherited industry usage produces.

The mode is the canonical visual style
of the strategy game,
the action role-playing game,
and the tactical role-playing game
through the 1990s and into the 2000s.
The player views a tilted top-down world
with diamond-shaped ground tiles
and pre-rendered character sprites
that face the camera at all times.
Buildings, trees, and obstacles
rise above the ground
along a vertical world axis
that projects to a screen vertical direction.
The visual style permits
a rich environment
while keeping the rendering math
within the affine-projection family.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a three-dimensional-to-two-dimensional affine map
composed of a world-axis rotation,
an orthogonal projection,
and a non-uniform scale.
The delivery mechanism
chooses how the engine
renders the rotated sprites
and resolves the picking ambiguity
that the underdetermined inverse map admits.

## A Brief History of the Mode

Axonometric projection in technical drawing
dates to the early nineteenth century
as a generalisation of the older cabinet and cavalier oblique projections.
The German engineer William Farish formalised the term
in 1822
in a treatise on isometric drawing
for engineering education.
The technique entered architectural drawing,
machine design,
and military mapping
across the nineteenth and early twentieth centuries.

The video-game adoption of axonometric projection
begins in the arcade.
[Zaxxon][ref_zaxxon]
from Sega in 1982
is widely cited as the first commercially-released arcade game
with an axonometric world.
The player piloted a fighter aircraft
across an isometric three-dimensional landscape
of vertically-stacked enemy installations.
The Zaxxon visual style
demonstrated the depth conveyed by axonometric
in a way that single-axis side-scrolling could not.

[Knight Lore][ref_knight_lore]
from Ultimate Play the Game in 1984
brought axonometric projection
to the home-computer adventure game.
The original ZX Spectrum release
rendered a series of small isometric rooms
that the player explored
in search of items and exits.
Knight Lore established the visual template
for British home-computer isometric adventures
through the mid 1980s.

The strategy game adopts axonometric in the early 1990s.
[SimCity 2000][ref_simcity_2000]
from Maxis in 1993
followed the top-down original SimCity
with an isometric city-builder
that conveyed the vertical extent of buildings,
elevations of terrain,
and underground water and transportation networks.
SimCity 2000 became the visual template
for subsequent city-builder games.

[X-COM, UFO Defense][ref_xcom]
from MicroProse in 1994
brought axonometric to the tactical strategy game.
The player commanded a squad of soldiers
across an isometric battlefield
that exposed multi-level buildings,
indoor and outdoor environments,
and the elevation differences
that ranged-combat gameplay required.
The X-COM series ran for a decade
in its original form
and was rebooted with the same axonometric approach
in the 2010s.

The mid-1990s see a convergence
of the role-playing game
and the axonometric visual style.
[Diablo][ref_diablo]
from Blizzard in 1996
established the axonometric action role-playing game.
The player controlled a single hero
exploring procedurally-generated dungeons
across an isometric world
of tile-based corridors and rooms.
The Diablo visual style
became the dominant convention
for the action-role-playing-game subgenre
for two decades.

[Civilization II][ref_civilization_2]
from MicroProse in 1996
brought axonometric to the turn-based strategy game.
The top-down original Civilization
yielded to an isometric tile-based world map
that gave the strategy player
a richer visual sense
of the geography being managed.

[Fallout][ref_fallout]
from Interplay in 1997
applied axonometric to the post-apocalyptic role-playing game
with detailed pre-rendered backgrounds
and small character sprites
walking across a wasteland
of isometric tile-based ruins.

[Age of Empires II][ref_aoe2]
from Ensemble Studios in 1999
applied axonometric to the real-time strategy game
with large-scale armies
moving across an isometric battlefield
of mixed-elevation terrain.
The Age of Empires series
continued in the same visual style
through its sequels and remastered re-releases.

The mode persists
through the modern independent role-playing game.
Titles such as
Pillars of Eternity in 2015
and Disco Elysium in 2019
continue the axonometric tradition
on modern hardware
through graphics-processing-unit-accelerated rendering
that emulates the classic pre-rendered-tile visual style.

## The Forward Map

The world coordinate
is a three-dimensional position
$\mathbf{p}_{\text{world}} = (w_x, w_y, w_z)$,
with the $y$-down convention
of the previous articles.
The two horizontal world axes
are $w_x$ and $w_z$,
which together describe positions on the ground plane.
The vertical world axis
is $w_y$,
gravity-aligned downward,
matching the screen-down convention
of the earlier articles.
The screen coordinate
is a two-dimensional pixel position
$\mathbf{p}_{\text{screen}} = (s_x, s_y)$.
The camera position
is a three-dimensional world coordinate
$\mathbf{c} = (c_x, c_y, c_z)$.

The forward map factors as
a world-axis rotation $R$,
an orthogonal projection $P$,
a non-uniform scale $S$,
and a screen-centre translation,

$$
F = T(\mathbf{o})\, S\, P\, R\, T(-\mathbf{c}),
$$

where the rotation $R$
orients the world so that the view axis
of the camera points along the projection direction,
the orthogonal projection $P$ drops the projection-axis coordinate,
and the scale $S$
applies the per-axis foreshortening factors
that the chosen axonometric variant requires.

In practice
the forward map writes as a single two-by-three matrix $M$
acting on the camera-relative world coordinate,

$$
\mathbf{p}_{\text{screen}} = M\, (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o},
$$

where the columns of $M$
are the screen-space directions
of the three world-axis unit vectors,

$$
M =
\begin{bmatrix} m_{xx} & m_{xy} & m_{xz} \\ m_{yx} & m_{yy} & m_{yz} \end{bmatrix}.
$$

The first column $(m_{xx}, m_{yx})$
is the screen-space image of the world $x$ unit vector.
The second column $(m_{xy}, m_{yy})$
is the screen-space image of the world $y$ unit vector.
The third column $(m_{xz}, m_{yz})$
is the screen-space image of the world $z$ unit vector.

The per-axis foreshortening factor
is the screen-space magnitude
of the corresponding column,

$$
f_x = \sqrt{m_{xx}^2 + m_{yx}^2},
$$

$$
f_y = \sqrt{m_{xy}^2 + m_{yy}^2},
$$

$$
f_z = \sqrt{m_{xz}^2 + m_{yz}^2}.
$$

The three variants
of axonometric projection
correspond to three patterns
of equality among the foreshortening factors.
Isometric projection
sets $f_x = f_y = f_z$.
Dimetric projection
sets two of the three factors equal
and the third different,
typically $f_x = f_z \neq f_y$.
Trimetric projection
sets all three factors different.

In homogeneous form
the forward map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} m_{xx} & m_{xy} & m_{xz} & W/2 - m_{xx} c_x - m_{xy} c_y - m_{xz} c_z \\ m_{yx} & m_{yy} & m_{yz} & H/2 - m_{yx} c_x - m_{yy} c_y - m_{yz} c_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \\ 1 \end{bmatrix}.
$$

The matrix is the three-by-four affine matrix
that the homogeneous form requires.
The third row carries the homogeneous-coordinate constant.

The equal-foreshortening isometric variant
sets all three column magnitudes to a common value $z$,

$$
M_{\text{iso}} = z
\begin{bmatrix} \sqrt{3}/2 & 0 & -\sqrt{3}/2 \\ 1/2 & 1 & 1/2 \end{bmatrix}.
$$

A unit ground-plane tile
projects to a diamond
of width $\sqrt{3}\, z$ pixels
and height $z$ pixels,
giving a $\sqrt{3}\!:\!1$ tile aspect.
A unit cube in world space
projects to a regular hexagon
with all six sides equal.
The equal-foreshortening variant
satisfies the isometric property
in the foreshortening sense
of equal screen-space lengths
for the three world unit vectors.
Strict mathematical isometric
also requires the three projected world-axis directions
to lie at 120-degree intervals on the screen,
which the $y$-down convention used throughout the series
does not permit
because the height axis must project downward
to match the gravity direction.
The article presents the equal-foreshortening variant
as the closest practical equivalent
of strict mathematical isometric
under the series convention.

The game-industry isometric variant,
which the article calls game-iso,
uses a tile width-to-height pixel ratio of two to one,

$$
M_{\text{game-iso}} = z
\begin{bmatrix} 1 & 0 & -1 \\ 1/2 & 1 & 1/2 \end{bmatrix},
$$

with $z$ giving the half-tile-width in pixels.
A unit cell on the ground plane
projects to a diamond tile
of width $2z$ pixels
and height $z$ pixels.
The horizontal-axis foreshortening factors
are $f_x = f_z = z\sqrt{5}/2$.
The vertical-axis foreshortening factor
is $f_y = z$.
The variant is dimetric,
with the two horizontal axes
sharing a foreshortening factor
that differs from the vertical-axis factor
by a ratio of $\sqrt{5}/2$.

The general dimetric forward map
relaxes the two-to-one tile aspect
to an arbitrary aspect $r$,

$$
M_{\text{dimetric}}(r) = z
\begin{bmatrix} 1 & 0 & -1 \\ 1/r & 1 & 1/r \end{bmatrix}.
$$

Setting $r = 2$ recovers game-iso.
Setting $r = \sqrt{3}$ recovers a tile aspect
close to strict isometric
but with the two horizontal axes
treated symmetrically with each other
rather than with the vertical axis.

The general trimetric forward map
allows three independent column scalings,

$$
M_{\text{trimetric}} =
\begin{bmatrix} z_x \cos\alpha & 0 & -z_z \cos\gamma \\ z_x \sin\alpha & z_y & z_z \sin\gamma \end{bmatrix},
$$

where $z_x$, $z_y$, $z_z$ are the per-axis foreshortening factors
and $\alpha$, $\gamma$ are the angles
of the horizontal axes
below the screen horizontal.
The trimetric variant
provides three independent scalings
and two independent angles
for a total of five free parameters.
Period games rarely used the full trimetric flexibility.

The factorisation
of the axonometric forward map
into rotation, projection, and scale
generalises the previous article's factorisation
of the oblique forward map
by replacing the depth-axis shear
with a full world-axis rotation.
The oblique forward map
is a special case of axonometric
in which the rotation
leaves the world $x$ and $y$ axes
parallel to the screen
and only the $w_z$ axis takes a screen-space angle.
Setting the rotation to identity
in axonometric
recovers the side-scrolling forward map
where the depth axis is the projection direction.

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
w_y = w_y^{\text{ground}} - h.
$$

The sprite-shadow decomposition writes
the airborne-sprite screen position
as the shadow screen position
shifted upward by the height-driven offset,

$$
\mathbf{p}_{\text{screen}}^{\text{sprite}} = \mathbf{p}_{\text{screen}}^{\text{shadow}} - (m_{xy}, m_{yy})\, h.
$$

In game-iso
the column for world $y$
points straight downward on the screen,
so the shift reduces to

$$
\mathbf{p}_{\text{screen}}^{\text{sprite}} = \mathbf{p}_{\text{screen}}^{\text{shadow}} - (0,\ z\, h).
$$

The shadow-drop convention
remains identical in form
to the belt-scroll and decoupled-vertical-axis cases.

## The Inverse Map

The forward map's matrix
takes three world inputs $(w_x, w_y, w_z)$
and produces two screen outputs $(s_x, s_y)$.
The system is underdetermined,
as in the oblique and belt-scroll articles.

Solving the forward map for the world coordinates
in terms of the screen coordinates
yields two linear combinations
$m_{xx} w_x + m_{xy} w_y + m_{xz} w_z$
and $m_{yx} w_x + m_{yy} w_y + m_{yz} w_z$
that the screen pixel determines.
The three world coordinates individually
are not determined.
The pre-image of a screen pixel
is a line in three-dimensional world space,
the picking ray of axonometric projection.

The engine resolves the ambiguity
through one of three conventions
that the previous articles introduced.

The first is the ground-plane assumption.
The engine treats the click
as referring to the ground at $w_y = w_y^{\text{ground}}$.
Substituting and solving
yields a system of two equations
in the two unknowns $w_x$ and $w_z$,

$$
\begin{bmatrix} m_{xx} & m_{xz} \\ m_{yx} & m_{yz} \end{bmatrix}
\begin{bmatrix} w_x - c_x \\ w_z - c_z \end{bmatrix} =
\begin{bmatrix} s_x - W/2 \\ s_y - H/2 \end{bmatrix} -
m_{\text{col-}y}\, (w_y^{\text{ground}} - c_y),
$$

where $m_{\text{col-}y} = (m_{xy}, m_{yy})^T$.
The two-by-two matrix on the left
is invertible
as long as the projected $x$ and $z$ axes
are not collinear on the screen.
For game-iso and the equal-foreshortening isometric variant
the two axes are non-collinear by construction
and the inverse exists.

The second is the known-vertical-coordinate assumption.
The engine treats the click
as referring to an object
at a known $w_y = w_y^{\text{known}}$.
The same two-by-two inverse applies
with $w_y^{\text{ground}}$ replaced by $w_y^{\text{known}}$.

The third is the screen-space sprite hit test.
The engine ignores the world coordinates entirely
and tests the clicked screen pixel
against the screen-space bounding rectangles
of every visible sprite.

For game-iso
the ground-plane inverse simplifies
because the world $y$ column is $(0, z)$
and the ground-plane equation
reduces to a simpler form.
Substituting and solving
yields

$$
w_x - c_x = \frac{s_x - W/2 + 2 (s_y - H/2 - z (w_y^{\text{ground}} - c_y))}{2 z},
$$

$$
w_z - c_z = \frac{-(s_x - W/2) + 2 (s_y - H/2 - z (w_y^{\text{ground}} - c_y))}{2 z}.
$$

The inverse is fully closed-form
under the ground-plane assumption.
The engine evaluates the inverse per click
to identify the ground tile
that the player selected.

The visible region of the world
on the ground plane
is a parallelogram in the $(w_x, w_z)$ plane,
the image of the screen rectangle
under the per-pixel ground-plane inverse map.
The shape of the parallelogram
depends on the angles $\alpha$ and $\gamma$
between the projected axes and the screen horizontal.
For game-iso the parallelogram is a rhombus
because the two projected horizontal axes
have equal magnitude
and symmetric angles about the vertical screen axis.

## A Worked Example

Consider a game-iso strategy game
with the following parameters.
The screen is 800 pixels wide
and 600 pixels tall.
The zoom factor is $z = 32$,
giving a 64-by-32-pixel diamond tile.
The ground-plane vertical world coordinate is $w_y^{\text{ground}} = 0$.
The camera position is $\mathbf{c} = (0, 0, 0)$.
The screen-centre offset is $\mathbf{o} = (400, 300)$.

The forward-map matrix is

$$
M = \begin{bmatrix} 32 & 0 & -32 \\ 16 & 32 & 16 \end{bmatrix}.
$$

A tile at world position $(0, 0, 0)$
projects to screen $(0, 0)$ plus the screen-centre offset,
giving screen $(400, 300)$.

A tile at world position $(1, 0, 0)$,
one unit east of the origin,
projects to

$$
\mathbf{p}_{\text{screen}} = (32, 16) + (400, 300) = (432, 316).
$$

A tile at world position $(0, 0, 1)$,
one unit south of the origin,
projects to

$$
\mathbf{p}_{\text{screen}} = (-32, 16) + (400, 300) = (368, 316).
$$

A tile at world position $(1, 0, 1)$
projects to

$$
\mathbf{p}_{\text{screen}} = (32 - 32,\ 16 + 16) + (400, 300) = (0, 32) + (400, 300) = (400, 332).
$$

The four tiles
$(0,0,0)$, $(1,0,0)$, $(1,0,1)$, $(0,0,1)$
project to the diamond
$(400, 300)$, $(432, 316)$, $(400, 332)$, $(368, 316)$,
which has width 64 pixels
and height 32 pixels,
matching the $2\!:\!1$ game-iso aspect.

A building at world position $(0, -2, 0)$,
two units above the ground at the origin,
projects to

$$
\mathbf{p}_{\text{screen}} = (0,\ 0 + 32 \cdot (-2)) + (400, 300) = (0, -64) + (400, 300) = (400, 236).
$$

The building base coincides with the tile origin's screen position $(400, 300)$,
and the building roof at world $y = -2$
renders 64 pixels above the base
at screen $(400, 236)$.

A jumping character
at world position $(0, -1, 0)$,
one unit above the ground at the origin,
projects to

$$
\mathbf{p}_{\text{screen}} = (0, -32) + (400, 300) = (400, 268).
$$

The character renders 32 pixels above the ground-tile centre,
matching the height value $h = 1$
through the height-to-screen offset $z h = 32$.

Click-picking at screen $(432, 316)$
under the ground-plane assumption with $w_y^{\text{ground}} = 0$
returns

$$
w_x - c_x = \frac{(432 - 400) + 2 (316 - 300 - 0)}{2 \cdot 32} = \frac{32 + 32}{64} = 1,
$$

$$
w_z - c_z = \frac{-(432 - 400) + 2 (316 - 300)}{2 \cdot 32} = \frac{-32 + 32}{64} = 0.
$$

The ground-plane inverse returns world tile $(1, 0, 0)$,
matching the tile that the click targeted.

The round-trip identity
holds along the ground plane,

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

The Y-sort criterion of the belt-scroll and oblique articles
extends to axonometric projection
through the same back-to-front
ground-projection screen-y comparison.
For an axonometric projection
with matrix $M$,
the ground-projection screen-y
is a linear combination
of the two horizontal world coordinates
plus a constant
that does not affect ordering.
The variable part of the sort key
is

$$
\text{sort key}_i = m_{yx}\, w_{x,i} + m_{yz}\, w_{z,i}.
$$

The criterion writes
as the comparison inequality

$$
\text{draw } i \text{ before } j \iff s_{y,i}^{\text{ground}} < s_{y,j}^{\text{ground}} \iff m_{yx}\, w_{x,i} + m_{yz}\, w_{z,i} < m_{yx}\, w_{x,j} + m_{yz}\, w_{z,j}.
$$

For game-iso,
the equality $m_{yx} = m_{yz} = z/2$
reduces the sort key to $\frac{z}{2}(w_x + w_z)$,
proportional to the diagonal coordinate $w_x + w_z$.
For the equal-foreshortening isometric variant,
the same equality holds
and gives the same diagonal sort key.
For general dimetric and trimetric variants,
the sort key uses the matrix coefficients
appropriate to the chosen forward map.

## Variations Within the Mode

The axonometric framework
admits several variations
that engines have explored.

An equal-foreshortening isometric variant
uses the matrix with $\sqrt{3}\!:\!1$ tile aspect
and equal column magnitudes.
The variant is mathematically clean
but produces a tile aspect
that does not align cleanly with integer pixel grids.
Engineering drawings use the strict variant
of mathematical isometric
for measurement accuracy
and accept the constraint
that the height axis projects upward,
which game graphics typically invert
to the $y$-down convention used here.

A game-iso variant
uses a tile aspect of $2\!:\!1$
that aligns cleanly with the integer pixel grid.
The variant is dimetric mathematically
but is universally called isometric
in the game industry.
The vast majority of period role-playing games
and strategy games
used game-iso.

A general dimetric variant
chooses an arbitrary tile aspect $r$
to produce a stylised view
that the designer judges visually appealing.
Period games rarely used arbitrary $r$
because the $2\!:\!1$ aspect of game-iso
proved a strong attractor.

A trimetric variant
provides three independent foreshortening factors
and two independent axis angles.
The variant gives the designer full control
over the screen-space rotation of the world.
Period games rarely used trimetric
because the asymmetric appearance
is unfamiliar to players accustomed to isometric.

A free-rotation variant
permits the player or the engine
to rotate the world around the vertical axis
during gameplay.
The variant requires the engine
to recompute the forward map matrix $M$
at each camera-rotation event.
Sprites must be pre-rendered
at multiple rotation angles
for the rotation to look consistent.
[The Sims][ref_sims_1] from Maxis in 2000
used a four-step rotation
of 90-degree increments
around the vertical world axis
to let the player see different sides of a building.

A free-zoom variant
permits the player or the engine
to change the zoom factor $z$
during gameplay.
The variant requires the engine
to recompute the forward map matrix $M$
at each zoom event.
Sprites either pre-rendered at multiple sizes
or scaled at render time
to match the new zoom.

A multi-tier-elevation variant
permits the ground plane $w_y^{\text{ground}}$
to vary across the world
as a function of $(w_x, w_z)$.
Hills, valleys, and stair-stepped buildings
all use the multi-tier variant.
The forward map is unchanged
and the engine simply uses the local $w_y^{\text{ground}}$
when rendering each tile.
SimCity 2000, X-COM, and Age of Empires II
all use multi-tier elevation.

A pseudo-three-dimensional sprite variant
pre-renders character sprites
at multiple facing angles
that match the axonometric viewing angles.
A character facing north-east in the world
displays the north-east-facing sprite
without any runtime sprite rotation.
The variant trades sprite memory
for runtime performance.

A two-and-a-half-dimensional building variant
renders buildings as two-dimensional sprites
positioned at the building's ground location
and Y-sorted with the other objects.
The variant gives the appearance
of three-dimensional buildings
without requiring true three-dimensional rendering.

## Delivery Mechanisms

The axonometric forward map
permits five distinct delivery mechanisms
on period hardware.

The first is pre-rendered tile graphics.
The engine pre-renders each ground tile
already in its axonometric-projected form
and stores the result as a tile atlas.
The runtime renderer
positions the pre-rendered tile
at the camera-relative screen position
without computing the forward map per pixel.
The mechanism is the dominant delivery
for classic role-playing games and strategy games
including Diablo, Fallout, X-COM,
and SimCity 2000.

The second is sprite-on-tile-background
with per-sprite Y-sort.
The engine renders moving objects
as object-attribute-memory sprites
at engine-computed axonometric screen positions
above the pre-rendered tile background.
The sprite priority is set per sprite
to match the Y-sort order
that the axonometric world requires.

The third is software composition
on a general-purpose central processing unit.
The engine maintains a frame buffer
and writes each visible object
into the frame buffer
in Y-sort order.
The mechanism was the universal delivery
on the IBM PC running the Microsoft Disk Operating System
through the late 1980s and the 1990s,
and remains the dominant mechanism
on modern independent-game engines
that render to a software frame buffer.

The fourth is pre-rendered sprite atlases
at multiple facing angles.
The engine pre-renders character animations
at four or eight rotation angles
around the vertical world axis
and selects the appropriate atlas frame
based on the character's current facing.
The variant supports the pseudo-three-dimensional sprite style
without runtime sprite rotation.
Period role-playing games
and tactical games
commonly used eight-direction sprite atlases.

The fifth is graphics-processing-unit-accelerated quad rendering.
Modern game engines
such as Unity, Godot, and Unreal
render the axonometric world
as textured quads
in three-dimensional world space
with a camera transform
that produces the desired axonometric projection.
The graphics processing unit
performs the depth sort
through its built-in depth buffer
and produces the screen image.
The depth buffer enforces back-to-front rendering
at the rasterisation level
without requiring the engine
to maintain a per-frame sprite sort list.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
the tile-atlas storage budget,
the central-processing-unit budget for runtime sort,
the sprite-atlas storage budget,
and the achievable frame rate.

## Where the Framing Breaks Down

The axonometric framing is insufficient
when any of the following conditions hold.

When the depth axis must show
true perspective foreshortening
proportional to inverse distance,
the affine projection of this article
is insufficient.
The synthesis closer of the series
treats the full projective generalisation.
The axonometric projection
preserves the world parallelism
that perspective projection
breaks for visual realism.

When the camera position must move
to follow the player along the depth axis
in addition to the lateral axes,
the rotation $R$ must update with the camera.
The article treats $R$ as constant
for a given scene
and defers the dynamic-camera case
to the synthesis closer.

When the world has non-flat ground
with significant elevation variation,
the multi-tier-elevation variant above
extends the axonometric projection
to support per-tile ground elevation.
The forward map remains affine
but the rendering pipeline must sort tiles
by their per-tile elevation in addition to lateral position.

When the gameplay requires camera rotation
during play,
the engine must recompute the forward map matrix $M$
at each rotation event,
and sprites must be pre-rendered
at multiple rotation angles
for visual consistency.
The free-rotation variant above
treats this case.

When the gameplay requires sprite scaling with depth
to suggest distance-from-camera proportional to size,
the affine projection of this article
is insufficient.
The sprite-scaling article later in the series
treats the depth-dependent sprite scaling case.

When the world is genuinely three-dimensional
with arbitrary mesh geometry
rather than flat tiles with vertical extents,
the modern three-dimensional rendering pipeline
displaces the classic axonometric mechanism.
The graphics-processing-unit-accelerated quad rendering
mechanism above
bridges classic axonometric
to modern three-dimensional rendering.

## The Canon

The following games
use axonometric projection
as their primary projection mode.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Zaxxon][ref_zaxxon]
in the arcade in 1982
gave the medium
its first commercially-released axonometric arcade game
through a vertical-scrolling shooter
over an isometric three-dimensional landscape.

[Knight Lore][ref_knight_lore]
on the ZX Spectrum in 1984
brought axonometric projection
to the home-computer adventure game
through small isometric rooms
and a series of progress-blocking puzzles.

[SimCity 2000][ref_simcity_2000]
on the IBM PC and Apple Macintosh in 1993
gave the city-builder genre
its canonical isometric template
through deep terrain elevation,
underground networks,
and a wide repertoire of buildings.

[X-COM, UFO Defense][ref_xcom]
on the IBM PC in 1994
brought axonometric to the tactical strategy game
through multi-level buildings,
indoor and outdoor environments,
and the elevation differences
that ranged-combat gameplay required.

[Diablo][ref_diablo]
on Microsoft Windows in 1996
established the axonometric action role-playing game
through procedurally-generated dungeons
and tile-based corridors.
The Diablo visual style
became the dominant convention
for the action role-playing subgenre
for two decades.

[Civilization II][ref_civilization_2]
on the IBM PC in 1996
brought axonometric to the turn-based strategy game
through an isometric tile-based world map
that the prior top-down Civilization
had not used.

[Fallout][ref_fallout]
on Microsoft Windows in 1997
applied axonometric to the post-apocalyptic role-playing game
through detailed pre-rendered backgrounds
and small character sprites
walking across the wasteland.

[Age of Empires II][ref_aoe2]
on Microsoft Windows in 1999
applied axonometric to the real-time strategy game
through large-scale armies
on mixed-elevation isometric terrain.

Each game in the canon
uses some variant of the axonometric forward map.
Most use game-iso with $2\!:\!1$ tile aspect.
The differences lie in the foreshortening factor $z$,
the per-tile elevation handling,
the camera policy,
and the choice of delivery mechanism
appropriate to the target hardware.

## Out of Scope

The article does not cover
the following.

True perspective projection
with a perspective denominator
is the subject of the synthesis closer of the series.
Axonometric projection is a parallel projection
without perspective foreshortening.

Sprite scaling along the depth axis
is the subject of the sprite-scaling article
later in the series.
The classic axonometric projection
does not scale sprites with depth.

The full Y-sort framework
including tie-breaking rules
and the Z-sort alternative
is the subject of a later cross-cutting article.
The article treats the Y-sort criterion
in its simplest axonometric form.

The full pick-disambiguation framework
including the sprite-scale-and-rotate hit-test
is the subject of a later cross-cutting article.
The article presents the three baseline conventions
parallel to the previous articles' treatments.

The dynamic-camera case
where the rotation $R$ and the camera $\mathbf{c}$
update during play
is treated as a special case
in the variations above
but is not the article's primary concern.

The choice between axonometric and true three-dimensional rendering
for a given game
is a design question
the series does not adjudicate.
Each visual style has games
for which it is the right choice
and games for which it is the wrong choice.

## Conclusion

Axonometric projection
generalises the previous article's oblique projection
by rotating the world before parallel projection
rather than tilting only the depth axis on the screen.
The forward map factors as
a world-axis rotation,
an orthogonal projection,
and a non-uniform scale.
The three classical variants
are isometric, dimetric, and trimetric,
distinguished by the equality of the foreshortening factors.
The game-industry isometric style,
universally called isometric in industry usage,
is mathematically dimetric
with a $2\!:\!1$ tile aspect.
The equal-foreshortening isometric variant
uses a $\sqrt{3}\!:\!1$ tile aspect
under the $y$-down convention.
Strict mathematical isometric
with 120-degree intervals between projected axes
requires the height axis to project upward on screen
and is incompatible
with the gravity-aligned $y$-down convention
that the series uses throughout.
The mode reached its visual peak
on the personal-computer role-playing games and strategy games
of the 1990s
through pre-rendered tile graphics
and pre-rendered sprite atlases.
The next article in the series
opens the affine-and-projective cluster
with the Mode 7 affine ground plane
that the Super Nintendo Entertainment System pioneered.

## References

- [Reference, Age of Empires II][ref_aoe2]
- [Reference, Civilization II][ref_civilization_2]
- [Reference, Diablo][ref_diablo]
- [Reference, Fallout][ref_fallout]
- [Reference, Knight Lore][ref_knight_lore]
- [Reference, SimCity 2000][ref_simcity_2000]
- [Reference, The Sims][ref_sims_1]
- [Reference, X-COM, UFO Defense][ref_xcom]
- [Reference, Zaxxon][ref_zaxxon]

[ref_aoe2]: https://en.wikipedia.org/wiki/Age_of_Empires_II
[ref_civilization_2]: https://en.wikipedia.org/wiki/Civilization_II
[ref_diablo]: https://en.wikipedia.org/wiki/Diablo_(video_game)
[ref_fallout]: https://en.wikipedia.org/wiki/Fallout_(video_game)
[ref_knight_lore]: https://en.wikipedia.org/wiki/Knight_Lore
[ref_simcity_2000]: https://en.wikipedia.org/wiki/SimCity_2000
[ref_sims_1]: https://en.wikipedia.org/wiki/The_Sims_(video_game)
[ref_xcom]: https://en.wikipedia.org/wiki/UFO:_Enemy_Unknown
[ref_zaxxon]: https://en.wikipedia.org/wiki/Zaxxon
