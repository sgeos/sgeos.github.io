---
layout: post
mathjax: true
comments: true
title:  "Raycasting, the Two-Dimensional Map Rendered as Three Dimensions"
date:   2026-04-28 09:00:00 +0000
categories: games graphics projection
---

<!-- A183 -->
<script>console.log("A183");</script>

The third article of the affine-and-projective cluster
treats raycasting
as a pseudo-three-dimensional rendering technique
that operates on a two-dimensional grid map.
Raycasting casts one ray per screen column
from the camera through the visible portion of the world
and computes the distance to the first wall the ray hits.
The wall is rendered as a vertical strip
with height inversely proportional to the distance.
The continuous variation of slice heights across screen columns
gives the player the impression
of looking forward at a three-dimensional corridor
even though the world is a flat two-dimensional grid
of wall and floor cells.

The technique pre-dates true three-dimensional polygon rendering
on consumer hardware
and shares the late-1980s and early-1990s era
with the sprite-scaling and Mode 7 techniques
of the previous articles.
Raycasting differs from both
in that the depth illusion arises
from per-column ray geometry
rather than from per-pixel affine scaling
or per-scanline matrix interpolation.
The result is a genuine first-person view
of a tile-based world,
which the canonical first-person shooters
of the early 1990s established
as the visual signature of the subgenre.

The article frames raycasting
as a per-column projection technique
where the projection math
maps each screen column
to a single ray
and computes the slice height
from the perpendicular distance to the wall.
The forward map produces the wall slice geometry
from the world configuration.
The inverse map recovers the wall hit point
from a screen pixel
for picking and gameplay interaction purposes.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a per-column inverse-distance scaling
combined with a fisheye correction
that the article derives.
The delivery mechanism
chooses how the engine
casts the rays
and how the renderer
draws the wall slices
that the rays produce.

## A Brief History of the Mode

Ray casting in computer graphics
dates to the 1960s
as a rendering technique
for displaying solid geometry
through ray-surface intersection.
The video-game adoption
arrives in the early 1990s
with the commercial first-person shooters of id Software.

[Hovertank 3D][ref_hovertank]
from id Software in 1991
gave the medium
its first commercially-released raycasting game.
The flat-shaded vehicle simulator
rendered walls without textures
and demonstrated the per-column raycasting algorithm
on personal-computer hardware
of the era.

[Catacomb 3-D][ref_catacomb_3d]
from id Software later in 1991
added texture mapping to the wall slices
through the per-column ray-grid intersection
that the texture-coordinate calculation requires.
The textured walls
gave the genre its first taste
of visually-rich tile-based environments.

[Wolfenstein 3D][ref_wolfenstein_3d]
from id Software in 1992
brought raycasting
to the mainstream personal-computer audience.
The first-person shooter gameplay
across a labyrinth of Nazi-themed levels
became the canonical raycasting visual style
and the template
for the subsequent first-person-shooter genre.
Wolfenstein 3D's commercial success
established the raycasting renderer
as a viable technique
for the early-1990s personal computer.

[Ken's Labyrinth][ref_kens_labyrinth]
from Ken Silverman and Epic MegaGames in 1993
extended the raycasting framework
with textured floors and ceilings
and additional gameplay features
beyond the wall-only Wolfenstein engine.

[Rise of the Triad][ref_rise_of_the_triad]
from Apogee Software in 1994
extended the Wolfenstein engine
with additional gameplay mechanics
including jumping and crouching
that pushed the raycasting framework's limits.

The technique recedes from the canon
after the mid-1990s
as the polygon-based rendering
of Doom in 1993
and the true three-dimensional engines of the late 1990s
displaced raycasting for first-person games.
Doom used binary-space-partition rendering,
and the Build engine of Duke Nukem 3D in 1996
extended the technique
with portal and sector rendering
that the article treats as outside the raycasting framework.

The technique persists
in modern independent retro releases
and in the educational tradition
where raycasting serves as an accessible introduction
to pseudo-three-dimensional rendering
on hardware without three-dimensional acceleration.

## The Forward Map

The world is a two-dimensional grid of cells
in the $(w_x, w_z)$ plane,
where the lateral axis $w_x$
and the depth axis $w_z$
both correspond to the floor plane
under the $y$-down convention
of the previous articles.
The vertical world axis $w_y$
is gravity-aligned downward.
Each grid cell
is either an open cell that the player can occupy
or a wall cell
that blocks the player and the ray.
Walls extend from the floor at $w_y = w_y^{\text{floor}}$
to the ceiling at $w_y = w_y^{\text{ceiling}}$
by the wall height $h_{\text{wall}} = w_y^{\text{floor}} - w_y^{\text{ceiling}}$
under the convention that the ceiling is above the floor
and therefore has smaller $w_y$ in the $y$-down frame.

The camera position is a two-dimensional world coordinate
$\mathbf{c} = (c_x, c_z)$
on the floor plane.
The camera's vertical position
is fixed at the midpoint between floor and ceiling,
$c_y = (w_y^{\text{floor}} + w_y^{\text{ceiling}})/2$.
The camera looks forward
along a unit-length direction vector
$\mathbf{d} = (d_x, d_z)$
with $|\mathbf{d}| = 1$.

The camera plane vector $\mathbf{p}$
is perpendicular to $\mathbf{d}$
with magnitude set by the horizontal field of view,

$$
|\mathbf{p}| = \tan\left( \frac{\mathrm{FOV}}{2} \right).
$$

For a 90-degree field of view,
$|\mathbf{p}| = 1$.
For a 66-degree field of view
common in early raycasters,
$|\mathbf{p}| \approx 0.66$.

The per-column ray cast
emits one ray per screen column $s_x \in \{0, 1, \dots, W-1\}$.
The normalised camera-x coordinate
runs from $-1$ at the left screen edge to $+1$ at the right edge,

$$
\mathrm{camx}(s_x) = \frac{2\, s_x}{W} - 1.
$$

The ray direction for column $s_x$ is

$$
\mathbf{r}(s_x) = \mathbf{d} + \mathrm{camx}(s_x) \cdot \mathbf{p}.
$$

The ray is not unit-length in general.
The central column has $\mathrm{camx} = 0$
and ray direction $\mathbf{d}$.
The screen edges have $\mathrm{camx} = \pm 1$
and rays that deviate from forward by the field-of-view angle.

The engine casts each ray
through the grid map
from the camera position $\mathbf{c}$
along the direction $\mathbf{r}$.
The standard algorithm
is the digital differential analyser,
which iterates through grid cells
along the ray
until a wall cell is encountered.
The article treats the algorithm as a primitive
without deriving the iteration details
and focuses instead on the projection math
that converts the wall hit
into the slice geometry.

The wall hit point is the world position
$\mathbf{h} = \mathbf{c} + t\, \mathbf{r}$
where $t > 0$ is the smallest ray parameter
at which the ray crosses a wall cell boundary.
The perpendicular distance from the camera plane to the wall
is the projection of the displacement onto the forward direction,

$$
d_{\text{perp}} = (\mathbf{h} - \mathbf{c}) \cdot \mathbf{d} = t.
$$

The simplification to $t$ holds
because $\mathbf{d}$ is unit-length
and $\mathbf{p}$ is perpendicular to $\mathbf{d}$,
so $\mathbf{r} \cdot \mathbf{d} = (\mathbf{d} + \mathrm{camx} \cdot \mathbf{p}) \cdot \mathbf{d} = 1$.
The perpendicular distance equals the ray parameter $t$ at the hit
without requiring an explicit trigonometric correction.

The wall slice height in pixels
follows from the inverse-distance scaling
that perspective projection introduces,

$$
h_{\text{slice}} = \frac{f \cdot h_{\text{wall}}}{d_{\text{perp}}},
$$

where $f$ is the vertical focal length in pixels per world unit
at unit distance.
For the canonical normalisation
where a wall of height $h_{\text{wall}} = 1$
fills the screen vertically when at distance $d_{\text{perp}} = f/H$,
the simplified formula is

$$
h_{\text{slice}} = \frac{f}{d_{\text{perp}}}.
$$

A wall at distance $d_{\text{perp}} = f$
has slice height $h_{\text{slice}} = 1$ pixel,
and a wall at distance $d_{\text{perp}} = f/H$
fills the screen with slice height $H$ pixels.

The wall slice is centred vertically around the horizon screen-y
$s_y^{\text{horizon}} = H/2$
under the assumption that the camera vertical position
sits at the wall midpoint.
The slice spans the vertical screen range

$$
s_y \in \left[ \frac{H}{2} - \frac{h_{\text{slice}}}{2},\ \frac{H}{2} + \frac{h_{\text{slice}}}{2} \right].
$$

The renderer writes the wall texture
into the screen frame buffer at each pixel
within this vertical range
at horizontal position $s_x$.
Above the slice
the renderer draws the ceiling.
Below the slice
the renderer draws the floor.

The texture coordinate
within the wall slice
follows from the wall hit position.
For a vertical wall at constant $w_z$,
the horizontal texture coordinate
is the fractional part of the hit's $w_x$,

$$
u_{\text{texture}} = w_x^{\text{hit}} - \lfloor w_x^{\text{hit}} \rfloor.
$$

For a wall at constant $w_x$,
the texture coordinate uses the $w_z$ fractional part instead.
The vertical texture coordinate
maps the slice screen-y to the wall's local vertical,

$$
v_{\text{texture}}(s_y) = \frac{s_y - (H/2 - h_{\text{slice}}/2)}{h_{\text{slice}}}.
$$

The vertical texture coordinate ranges from $0$ at the top of the slice
to $1$ at the bottom.

## The Fisheye Correction

The article uses the perpendicular distance $d_{\text{perp}}$
in the slice-height formula.
An engineer new to raycasting
might use the Euclidean distance instead,

$$
d_{\text{euc}} = |\mathbf{h} - \mathbf{c}| = \sqrt{(h_x - c_x)^2 + (h_z - c_z)^2}.
$$

The Euclidean distance and the perpendicular distance
are related by

$$
d_{\text{euc}} = \frac{d_{\text{perp}}}{\cos\alpha},
$$

where $\alpha$ is the angle between the ray and the forward direction,

$$
\cos\alpha = \frac{\mathbf{r} \cdot \mathbf{d}}{|\mathbf{r}|} = \frac{1}{|\mathbf{r}|} = \frac{1}{\sqrt{1 + \mathrm{camx}^2\, |\mathbf{p}|^2}}.
$$

Using $d_{\text{euc}}$ in the slice-height formula
gives slices at the screen edges
that are smaller than they should be,
because $d_{\text{euc}} > d_{\text{perp}}$
at any column other than the central one.
A flat wall perpendicular to the forward direction
would render with center slice tall
and edge slices short,
making the wall appear convex toward the viewer.
The community calls the artifact the fisheye effect.

The fisheye correction
replaces $d_{\text{euc}}$ with $d_{\text{perp}}$
in the slice-height formula,

$$
h_{\text{slice}} = \frac{f}{d_{\text{perp}}} = \frac{f \cos\alpha}{d_{\text{euc}}}.
$$

The corrected slice rendering
preserves flat walls as flat
across the screen.

The simplification of the previous section
in which $d_{\text{perp}} = t$
when $\mathbf{d}$ is unit-length
and $\mathbf{p}$ is perpendicular to $\mathbf{d}$
gives the fisheye correction for free.
The digital differential analyser
computes $t$ at the hit
and the engine uses $t$ directly as $d_{\text{perp}}$
without needing to compute $\cos\alpha$ separately.

## The Inverse Map

The forward map is per-column,
so the inverse map is per-pixel.
A click at screen pixel $(s_x, s_y)$
inverts in two steps.

The first step
identifies the column $s_x$
and looks up the ray that the column corresponds to.
The engine retrieves the wall hit point $\mathbf{h}$
and the perpendicular distance $d_{\text{perp}}$
that the forward map already computed
for that column.

The second step
distinguishes wall, ceiling, and floor pixels
based on the vertical position $s_y$
relative to the wall slice extent.

For a wall pixel,
the inverse is the wall hit point
combined with the texture coordinate at the click,

$$
\mathbf{p}_{\text{world}}^{\text{wall}} = (h_x,\ w_y^{\text{ceiling}} + v_{\text{texture}}(s_y) \cdot h_{\text{wall}},\ h_z).
$$

The vertical world coordinate
recovers from the wall slice position
through the texture-coordinate formula above.

For a floor pixel below the slice,
the inverse follows the ray to the floor plane $w_y = w_y^{\text{floor}}$.
The floor distance from the camera
along the camera-forward axis is

$$
d_{\text{floor}}(s_y) = \frac{f\, (w_y^{\text{floor}} - c_y)}{s_y - H/2},
$$

with the same inverse-screen-y form
as the Mode 7 ground-plane depth of the previous cluster article.
The floor world position at pixel $(s_x, s_y)$
follows from advancing along the per-column ray
by the floor distance,

$$
\mathbf{p}_{\text{world}}^{\text{floor}} = \big( c_x + d_{\text{floor}}(s_y)\, r_x(s_x),\ w_y^{\text{floor}},\ c_z + d_{\text{floor}}(s_y)\, r_z(s_x) \big),
$$

where $r_x(s_x)$ and $r_z(s_x)$ are the horizontal components
of the per-column ray direction.
The ray parameter at the floor hit
equals the perpendicular distance
because $\mathbf{r}(s_x) \cdot \mathbf{d} = 1$.

For a ceiling pixel above the slice,
the inverse follows the same form
with $w_y^{\text{ceiling}}$ replacing $w_y^{\text{floor}}$
and $s_y - H/2$ replaced by $H/2 - s_y$
to keep the distance positive.

The floor and ceiling inverses
use only the per-column ray $\mathbf{r}(s_x)$ of the forward map
together with the $s_y$-dependent distance.
The raycasting framework does not require
an explicit per-pixel ray construction
because the floor and ceiling planes
are at known constant $w_y$
and the depth from the camera
follows from the screen-y by inverse projection.

The visible region of the world
that raycasting renders
is the set of world points
that the rays can reach.
The visible region is bounded by walls
that the rays terminate at
and by the maximum ray-cast distance
that the engine permits.
For a closed map with no openings beyond the ray-cast distance,
the visible region is the union of cones
extending from the camera
through each of the visible open cells.

Picking against gameplay objects
positioned as sprites in the world
follows the depth-sorted sprite rendering of the previous article.
The engine computes each sprite's screen-space position
through the perspective projection of the previous article
and Y-sorts the sprites against the wall slices
through the per-column $d_{\text{perp}}$ values.
The click identification
iterates the visible sprites in front-to-back depth order
and tests the screen-space bounding rectangle
of each.
The first sprite whose rectangle contains the click
is returned.

## A Worked Example

Consider a Wolfenstein-3D-style first-person shooter
with the following parameters.
The screen is 320 pixels wide
and 200 pixels tall,
matching the personal-computer Mode 13h display
that early raycasters targeted.
The horizontal field of view is 66 degrees,
so the camera plane magnitude is
$|\mathbf{p}| = \tan(33°) \approx 0.65$.
The vertical focal length is $f = 200$ pixels per world unit at unit distance,
chosen so that a wall of height 1 at distance 1 fills the screen vertically.

The camera position is $\mathbf{c} = (5.5, 5.5)$ world units.
The camera looks forward along the $+w_x$ axis,
so $\mathbf{d} = (1, 0)$.
The camera plane vector,
perpendicular to $\mathbf{d}$ with magnitude $0.65$, is
$\mathbf{p} = (0, 0.65)$.
A wall cell occupies the grid column at $w_x = 10$,
so all walls at $w_x \in [10, 11]$ are solid.

The central screen column $s_x = 160$
has $\mathrm{camx} = 2 \cdot 160 / 320 - 1 = 0$
and ray direction $\mathbf{r}(160) = (1, 0) + 0 \cdot (0, 0.65) = (1, 0)$.
The ray hits the wall at world position $\mathbf{h} = (10, 5.5)$
with ray parameter $t = 4.5$.

The perpendicular distance is

$$
d_{\text{perp}} = (10 - 5.5, 5.5 - 5.5) \cdot (1, 0) = 4.5.
$$

The wall slice height is

$$
h_{\text{slice}} = \frac{200}{4.5} \approx 44 \text{ pixels}.
$$

The slice spans screen-y range
$[100 - 22, 100 + 22] = [78, 122]$.
The renderer writes the wall texture
into the column $s_x = 160$
at rows 78 through 122.

The leftmost screen column $s_x = 0$
has $\mathrm{camx} = -1$
and ray direction $\mathbf{r}(0) = (1, 0) + (-1)(0, 0.65) = (1, -0.65)$.
The ray hits the same wall at $w_x = 10$
at ray parameter $t = 4.5$
because the wall is perpendicular to the forward direction
and $t$ is the projection of the displacement onto $\mathbf{d}$.
The hit point is

$$
\mathbf{h} = (5.5, 5.5) + 4.5 \cdot (1, -0.65) = (10, 5.5 - 2.925) = (10, 2.575).
$$

The perpendicular distance is

$$
d_{\text{perp}} = (4.5, -2.925) \cdot (1, 0) = 4.5.
$$

The wall slice at column $s_x = 0$
has the same height as the central column,

$$
h_{\text{slice}} = \frac{200}{4.5} \approx 44 \text{ pixels}.
$$

The flat wall renders as a flat constant-height strip
across the screen,
which is the correct visual behaviour
for a wall perpendicular to the view direction.

To illustrate the fisheye effect,
consider what would happen
without the fisheye correction.
The Euclidean distance for the edge column is

$$
d_{\text{euc}} = \sqrt{4.5^2 + 2.925^2} = \sqrt{20.25 + 8.556} \approx 5.37.
$$

The uncorrected slice height would be

$$
h_{\text{slice}}^{\text{wrong}} = \frac{200}{5.37} \approx 37 \text{ pixels},
$$

which is shorter than the central column's 44 pixels.
A flat wall would render with the centre at full height
and the edges shortened,
giving the wall a bowed convex appearance.
The fisheye correction
restores the flat wall to a constant slice height
across the screen.

A click at screen pixel $(160, 100)$
falls in the central column's wall slice.
The inverse map identifies the column $s_x = 160$,
retrieves the wall hit $\mathbf{h} = (10, 5.5)$,
and recovers the vertical texture coordinate
through

$$
v_{\text{texture}} = \frac{100 - 78}{44} \approx 0.5.
$$

The click corresponds to the wall at world position
$(10, w_y^{\text{ceiling}} + 0.5 \cdot h_{\text{wall}}, 5.5)$,
which is the wall midpoint vertically.

The round-trip identity
holds per column,

$$
F^{-1}_{\text{wall}}(F(\mathbf{p}_{\text{world}}^{\text{wall}})) = \mathbf{p}_{\text{world}}^{\text{wall}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.

## Variations Within the Mode

The raycasting framework
admits several variations
that engines have explored.

A textured-floor-and-ceiling variant
extends the wall raycasting
with per-pixel floor and ceiling sampling.
For each pixel below the wall slice,
the engine computes the ray-floor intersection
and samples the floor texture at the intersection.
The variant requires per-pixel arithmetic
that exceeds the per-column cost
of wall-only raycasting.
Ken's Labyrinth used textured floors and ceilings
through this variant.

A variable-height-wall variant
permits walls to have heights
that vary by grid cell.
The wall slice formula
extends to non-unit wall heights
through the multiplication by $h_{\text{wall}}$
that the slice-height formula admits.
Rise of the Triad and later raycasters
used variable-height walls
to suggest more complex environments
than the uniform-height Wolfenstein labyrinth.

A jumping-and-crouching variant
permits the camera vertical position
to vary from the wall midpoint.
The wall slice positions vertically
according to the camera height,

$$
s_y^{\text{slice-center}} = \frac{H}{2} - \frac{f\, (c_y - c_y^{\text{midpoint}})}{d_{\text{perp}}}.
$$

Rise of the Triad used the jumping-and-crouching variant.

A look-up-and-down variant
permits the camera pitch
to vary from straight ahead.
The wall slice positions vertically
according to the pitch offset,

$$
s_y^{\text{slice-center}} = \frac{H}{2} - f\, \tan(\theta_{\text{pitch}}).
$$

The variant is mathematically an approximation
to true three-dimensional rotation
that the raycasting framework can support
within its per-column projection model.

A textured-wall variant
applies a texture map to each wall slice
indexed by the wall hit's horizontal texture coordinate
and the slice screen-y's vertical texture coordinate.
The variant is the default in all post-Hovertank raycasters.

A multi-level-grid variant
extends the two-dimensional grid
to a stack of grids
that the engine treats as multiple floors.
The variant approximates multi-storey environments
that pure raycasting cannot represent.
The Build engine of Duke Nukem 3D
extended this approach further
through portal rendering
that the article does not treat.

A transparent-wall variant
permits the ray to continue past a wall
if the wall texture has alpha-transparent regions.
The variant requires the engine
to sample the wall texture during the ray cast
and continue if the sample is transparent.
The transparent-wall variant
permits doorways, windows, and decorative grilles
within the otherwise-opaque wall framework.

## Delivery Mechanisms

The raycasting forward map
permits five distinct delivery mechanisms
on period hardware.

The first is software raycasting
on a general-purpose central processing unit.
The engine casts each ray
through the grid map
on the central processing unit
and writes the resulting wall slice
into the frame buffer.
The mechanism was the universal delivery
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s.
Wolfenstein 3D, Catacomb 3-D, Hovertank 3D,
Ken's Labyrinth, and Rise of the Triad
all used software raycasting.

The second is fixed-point arithmetic
within software raycasting
to avoid floating-point operations
on processors without hardware floating-point support.
The Intel 80386 and earlier central processing units
that the early-1990s personal computers used
either lacked hardware floating-point
or had it as an optional coprocessor.
Wolfenstein 3D used fixed-point arithmetic
for the ray-grid intersection and the slice-height calculation
to achieve real-time frame rates
on the era's hardware.

The third is precomputed lookup tables
for trigonometric functions and reciprocals.
The wall slice height
involves a division by the perpendicular distance,
and the per-column ray angle
involves a cosine for the fisheye correction.
The engine precomputes both as tables
indexed by the angle or by the distance,
trading memory for computation time.

The fourth is hardware texture mapping
on later-1990s personal-computer hardware
that included three-dimensional accelerator cards.
The engine casts the rays in software
but draws the wall slices
through hardware texture-mapped quads.
The variant transitions raycasting
to a hybrid software-and-hardware pipeline
that the late-1990s personal computer supported.

The fifth is graphics-processing-unit shader raycasting
on modern hardware.
A fragment shader
casts the rays in parallel across screen columns
and computes the wall slice geometry per fragment.
The mechanism takes the raycasting algorithm
to its computational extreme
through massive parallelism.
Modern indie retro-style raycasters
typically use graphics-processing-unit shader raycasting
to achieve high resolutions
that software raycasting on the central processing unit
could not match.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
the central-processing-unit budget,
the lookup-table memory budget,
and the achievable resolution and frame rate.

## Where the Framing Breaks Down

The raycasting framing is insufficient
when any of the following conditions hold.

When the world contains
non-axis-aligned walls
that cannot be represented
as full or empty grid cells,
the raycasting framework
is insufficient.
The portal-and-sector rendering
that the Build engine introduced
addresses this case
through sector polygons
that the article does not treat.

When the world contains
multiple floors at the same horizontal position,
the single-grid model
of pure raycasting is insufficient.
The multi-level-grid variant above
extends the framework partially,
and the portal-rendering frameworks
extend it further.

When the gameplay requires
true three-dimensional geometry
with arbitrary mesh structures,
the raycasting framework
is insufficient.
The polygon-based rendering
of Doom and its successors
addresses this case
through binary-space-partition trees
and explicit polygon rasterisation
that the article treats as outside its scope.

When the camera must pitch significantly
or roll around the forward axis,
the per-column projection of raycasting
loses its perpendicular-distance simplification.
The look-up-and-down variant
extends the framework with an approximation,
but significant pitch
warps the wall slices in a way
that purer perspective projection avoids.

When the wall textures must distort
with viewing angle
to suggest non-flat surfaces,
the per-column constant texture-x mapping
of raycasting is insufficient.
A genuinely curved wall
requires per-pixel ray-surface intersection
that the article does not treat.

## The Canon

The following games
use raycasting
as their primary rendering technique.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Hovertank 3D][ref_hovertank]
on the IBM PC in 1991
gave the medium
its first commercially-released raycasting game.
The flat-shaded walls
demonstrated the algorithm
without the texturing complexity
that subsequent games added.

[Catacomb 3-D][ref_catacomb_3d]
on the same hardware later in 1991
added wall texture mapping
to the raycasting framework
and brought visually-rich tile-based environments
to the genre.

[Wolfenstein 3D][ref_wolfenstein_3d]
on the same hardware in 1992
brought raycasting
to the mainstream personal-computer audience.
The first-person shooter became the canonical raycasting game
and the template for the first-person-shooter genre
that the polygon-based successors inherited.

[Ken's Labyrinth][ref_kens_labyrinth]
on the same hardware in 1993
extended the raycasting framework
with textured floors and ceilings,
demonstrating that the per-column algorithm
could carry additional visual fidelity
beyond Wolfenstein's wall-only treatment.

[Rise of the Triad][ref_rise_of_the_triad]
on the same hardware in 1994
extended the Wolfenstein engine
with jumping, crouching, and variable-height walls
that pushed the raycasting framework
to its visual upper bound.

Each game in the canon
uses the per-column raycasting forward map
with a different combination of variation choices
appropriate to the gameplay it supports.

## Out of Scope

The article does not cover
the following.

The binary-space-partition rendering
of Doom in 1993
and its successors
is outside the raycasting framework.
Doom used a precomputed binary-space-partition tree
to determine wall visibility
and rasterised polygons
through a different algorithmic path
than per-column raycasting.

The portal-and-sector rendering
of the Build engine
in Duke Nukem 3D and its contemporaries
extends raycasting toward sector polygons
that the article does not treat in detail.

True three-dimensional polygon rendering
through hardware-accelerated rasterisation
is the modern technique
that the synthesis closer of the series treats.
Raycasting is a per-column projection technique
that the synthesis closer subsumes
as a special case.

Voxel-based pseudo-three-dimensional rendering
of the Comanche series and other voxel terrain renderers
is a separate technique
that produces superficially similar visuals
through height-map-traversal rather than wall-grid raycasting.

The full picking framework
including the sprite-scale-and-rotate hit test
of the previous article
is the subject of a later cross-cutting article.
The article presents picking
in its simplest raycasting form
and defers the full treatment.

## Conclusion

Raycasting renders a two-dimensional grid map
as a three-dimensional first-person view
through per-column ray casting.
The forward map per column
emits a ray from the camera
in the direction $\mathbf{r}(s_x) = \mathbf{d} + \mathrm{camx}(s_x) \cdot \mathbf{p}$,
finds the wall the ray hits,
and renders a vertical wall slice
with height $h_{\text{slice}} = f/d_{\text{perp}}$
where $d_{\text{perp}}$ is the perpendicular distance from the camera plane.
The fisheye correction
uses the perpendicular distance
rather than the Euclidean distance
to preserve flat walls as flat across the screen.
The algorithm runs in real time
on early-1990s personal-computer hardware
through fixed-point arithmetic
and precomputed lookup tables.
The mode defined the first-person shooter genre
on the IBM PC
through Wolfenstein 3D and its contemporaries
before polygon-based rendering displaced it
in the mid-to-late 1990s.
The next article in the cluster
treats stylised and hybrid projections
that combine multiple projection modes
in a single game.

## References

- [Reference, Catacomb 3-D][ref_catacomb_3d]
- [Reference, Hovertank 3D][ref_hovertank]
- [Reference, Ken's Labyrinth][ref_kens_labyrinth]
- [Reference, Rise of the Triad][ref_rise_of_the_triad]
- [Reference, Wolfenstein 3D][ref_wolfenstein_3d]

[ref_catacomb_3d]: https://en.wikipedia.org/wiki/Catacomb_3-D
[ref_hovertank]: https://en.wikipedia.org/wiki/Hovertank_3D
[ref_kens_labyrinth]: https://en.wikipedia.org/wiki/Ken%27s_Labyrinth
[ref_rise_of_the_triad]: https://en.wikipedia.org/wiki/Rise_of_the_Triad
[ref_wolfenstein_3d]: https://en.wikipedia.org/wiki/Wolfenstein_3D
