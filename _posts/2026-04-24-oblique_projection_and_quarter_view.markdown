---
layout: post
mathjax: true
comments: true
title:  "Oblique Projection and the Quarter View"
date:   2026-04-24 09:00:00 +0000
categories: games graphics projection
series: two_dimensional_projection
series_title: Two-Dimensional Projection in Games
series_index: 7
---
<!-- A179 -->
<script>console.log("A179");</script>

The opening article of the second cluster
moves from the Cartesian projections
of the previous cluster
to the oblique projection
that tilts the depth axis
at an angle of the engine's choosing.
The world remains a three-dimensional grid
of objects at world positions $(w_x, w_y, w_z)$.
The screen remains a two-dimensional pixel grid.
The forward map gains
a depth-mixing direction
controlled by an angle $\phi$
and a foreshortening factor $\alpha$
that the engine chooses
to produce the visual style
the game requires.
Belt-scroll
from the previous article
is the limit case
where the depth-mixing direction
points straight up the screen.
Oblique projection in this article
permits the depth-mixing direction
to point in any direction on the screen,
producing a richer family of projection styles
and the foundation for axonometric projection
that the next article treats.

The quarter view of the article title
refers to the visual style
that historic engineering drawing
calls oblique projection
and that game designers
have used since the early arcade era
to render a small world strip
with apparent depth.
The quarter view shows three faces of a cuboid object simultaneously,
the front face directly,
the top face foreshortened upward,
and the side face foreshortened to the side.
The viewer reads the depth axis
as the offset between the front face
and the corresponding edges of the top and side faces.
The depth-mixing direction
is the screen-space direction
of that offset.

The article distinguishes two classical variants,
cavalier projection
that preserves the depth lines at their full world length
and cabinet projection
that halves the depth lines.
Cavalier preserves measurement accuracy
at the cost of an artificially deep appearance.
Cabinet sacrifices measurement accuracy
for a more naturalistic appearance.
The Worked Example
treats both variants in turn.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a three-dimensional-to-two-dimensional affine map
with an oblique-shear factor.
The delivery mechanism
chooses how the engine
renders the depth-shifted sprites
and resolves the picking ambiguity
that the underdetermined inverse map admits.

## A Brief History of the Mode

Oblique projection
in technical drawing
dates to the seventeenth century
as a convention for depicting fortifications
and machinery.
The eighteenth-century engineering schools
formalised the cabinet and cavalier variants
under those names.
The technique entered industrial design
and architectural drawing
in the nineteenth and twentieth centuries
as a parallel-projection alternative
to perspective drawing.

The video-game adoption of oblique projection
arrives with the personal-computer era.
[Habitat][ref_habitat]
on the Commodore 64 in 1986
gave the mass-market personal computer
its first networked persistent world
with an oblique-projection visual style.
Avatars and rooms
rendered in a cabinet-style oblique view
that conveyed the depth of each room
without departing from the limited graphics capabilities
of the Commodore 64.

[Populous][ref_populous]
from Bullfrog in 1989
gave the genre of strategy games
its canonical cabinet-oblique terrain.
The player viewed a small section
of a deformable terrain
from a fixed cabinet angle
that tilted the depth axis
into the upper-left of the screen.
The Populous visual style
defined the god-game subgenre
that the studio later extended
through Powermonger and the Bullfrog catalogue.

[Ultima VII, The Black Gate][ref_ultima_7]
from Origin in 1992
brought oblique projection
to the mass-market personal-computer role-playing game.
The Avatar walked across a continuous oblique-projected world
where each tile was an oblique cuboid
and where building walls and trees
rendered with cabinet-style depth shifts
that the player read as depth.
The Ultima VII engine
became the visual template
for several Origin titles
across the early 1990s.

The technique recedes from the canon
after the mid-1990s
as the personal-computer industry
moves to hardware-accelerated three-dimensional rendering.
Games that retained a tilted-view aesthetic
moved predominantly to the axonometric and isometric styles
of the next article in the cluster.
The axonometric style
that the next article treats
continued to flourish
through the late nineties
in strategy and role-playing games
that found the rotational symmetry
of axonometric more useful than oblique.

## The Forward Map

The world coordinate
is a three-dimensional position
$\mathbf{p}\_{\text{world}} = (w_x, w_y, w_z)$,
with the $y$-down convention
of the previous articles.
The screen coordinate
is a two-dimensional pixel position
$\mathbf{p}\_{\text{screen}} = (s_x, s_y)$.
The camera position
is a three-dimensional world coordinate
$\mathbf{c} = (c_x, c_y, c_z)$.
The zoom factor
is a positive scalar $z$.
The depth-mixing direction
is parameterised by an angle $\phi$
in the open interval $(0, \pi)$,
giving the screen-space direction
in which the depth axis tilts.
The foreshortening factor
is a positive scalar $\alpha$
giving the screen-space length
of one unit of depth
along the depth-mixing direction.

The forward map is

$$
s_x = z\, (w_x - c_x) + \alpha\, z\, (w_z - c_z)\, \cos\phi + W/2,
\tag{1}
$$

$$
s_y = z\, (w_y - c_y) - \alpha\, z\, (w_z - c_z)\, \sin\phi + H/2,
\tag{2}
$$

where $W$ and $H$ are the screen width and height
in pixels.

Writing $\mathbf{d}(\phi) = (\cos\phi,\ -\sin\phi)$
for the screen-space depth-direction unit vector,
the forward map writes in vector form as

$$
\mathbf{p}_{\text{screen}} = z\, \big((w_x, w_y) - (c_x, c_y)\big) + \alpha\, z\, (w_z - c_z)\, \mathbf{d}(\phi) + \mathbf{o}.
\tag{3}
$$

The first term
is the side-scrolling forward map of the second cluster article
applied to the camera-relative lateral and vertical coordinates.
The second term
is the depth-driven screen-space shift
along the direction $\mathbf{d}(\phi)$
with magnitude $\alpha z \lvert w_z - c_z \rvert$.

The sign convention
matches the $y$-down screen convention.
The negative sign on the $\sin\phi$ term
ensures that increasing depth $w_z$
shifts the screen position upward on the screen,
which the visual reader expects of objects
further back in the world.

The screen-space separation
between two world objects
at the same lateral and vertical coordinates
but different depths
follows from the linearity of the forward map,

$$
\Delta \mathbf{p}_{\text{screen}} = \alpha\, z\, (w_{z,1} - w_{z,2})\, \mathbf{d}(\phi).
\tag{4}
$$

The separation is parallel to $\mathbf{d}(\phi)$,
has magnitude $\alpha z \lvert w_{z,1} - w_{z,2} \rvert$,
and is independent of the lateral and vertical coordinates.
The depth-direction screen-shift
is the operational reading
of the foreshortening factor $\alpha$
and the depth angle $\phi$.

In homogeneous form
the forward map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & \alpha\, z\, \cos\phi & W/2 - z\, c_x - \alpha\, z\, c_z\, \cos\phi \\ 0 & z & -\alpha\, z\, \sin\phi & H/2 - z\, c_y + \alpha\, z\, c_z\, \sin\phi \\ 0 & 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \\ 1 \end{bmatrix}.
\tag{5}
$$

The matrix is a three-by-four affine matrix
acting on the four-component augmented world coordinate.
The matrix is the parallel projection
from the three-dimensional world
onto the two-dimensional screen
with the oblique-projection angle
that the parameters $\alpha$ and $\phi$ encode.

The factorisation pattern
from the opener
extends to the oblique case
as a composition of
a two-axis depth-mixing shear,
an orthogonal projection from three dimensions to two,
a uniform scale,
and a screen-centre translation,

$$
F = T(\mathbf{o})\, S(z)\, P_z\, K(\alpha, \phi)\, T(-\mathbf{c}),
\tag{6}
$$

where $K(\alpha, \phi)$
is the three-by-three two-axis shear matrix
that adds the depth-driven shifts
to the screen-x and screen-y components,

$$
K(\alpha, \phi) =
\begin{bmatrix} 1 & 0 & \alpha\, \cos\phi \\ 0 & 1 & -\alpha\, \sin\phi \\ 0 & 0 & 1 \end{bmatrix},
\tag{7}
$$

and $P_z$
is the two-by-three orthogonal projection
that drops the depth component,

$$
P_z =
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}.
\tag{8}
$$

The two-axis shear
generalises the single-axis shear of the previous article.
The belt-scroll case
is the limit
$\phi = \pi/2$
where the depth-mixing direction
points straight up the screen
and $\cos\phi = 0$
zeroes the screen-x contribution
of the depth axis.
Setting $\alpha = \beta$
and $\phi = \pi/2$
recovers the belt-scroll forward map
of the previous article exactly.

The cavalier and cabinet variants
correspond to specific choices of $\alpha$.
The cavalier variant
sets $\alpha = 1$
and preserves the world length of depth lines
in the screen image.
A unit depth shift
appears as a unit pixel shift
along the depth-mixing direction.
The depth axis
appears stretched compared to natural perspective
since true perspective foreshortens distant objects.
The cavalier variant
is appropriate for engineering drawings
where measurement accuracy matters
and for game scenes
where the designer wants
the depth axis to feel pronounced.

The cabinet variant
sets $\alpha = 1/2$
and halves the screen-space length
of depth lines
relative to their world length.
A unit depth shift
appears as a half-pixel shift along the depth-mixing direction.
The depth axis appears foreshortened
in a way that approximates true perspective
more closely than cavalier does
without abandoning the affine-projection family.
The cabinet variant is appropriate for game scenes
where the designer wants
a more naturalistic depth appearance.

Other choices of $\alpha$
are uncommon
but mathematically valid.
A value of $\alpha = 2/3$
sits between cavalier and cabinet
and is sometimes used
when the designer wants slightly more depth pronouncement
than cabinet provides.
The article treats the cavalier and cabinet cases
as the canonical variants.

The angle $\phi$
typically takes values
of $\pi/6$, $\pi/4$, or $\pi/3$
matching 30, 45, or 60 degrees
from the screen-horizontal axis.
The most common quarter-view angle
in classic games is $\pi/4$,
producing a depth axis
that tilts at 45 degrees on the screen.

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
\tag{9}
$$

The sprite-shadow decomposition writes
the airborne-sprite screen position
as the shadow screen position
shifted upward by the height-driven vertical offset,

$$
\mathbf{p}_{\text{screen}}^{\text{sprite}} = \mathbf{p}_{\text{screen}}^{\text{shadow}} - (0,\ z\, h),
\tag{10}
$$

with the magnitude of the vertical screen-space separation

$$
\Delta s_y = z\, h.
\tag{11}
$$

The depth-mixing direction $\mathbf{d}(\phi)$
plays no role in the height shift
because the height axis stays
parallel to the gravity-aligned screen-y axis
regardless of the depth angle.
The shadow-drop convention
is identical in form
to the belt-scroll and decoupled-vertical-axis cases.

## The Inverse Map

The forward map's matrix
takes three world inputs $(w_x, w_y, w_z)$
and produces two screen outputs $(s_x, s_y)$.
The system is underdetermined,
as in the belt-scroll article.

Solving the forward map for the world coordinates
in terms of the screen coordinates
yields

$$
w_x + \alpha\, w_z\, \cos\phi = \frac{s_x - W/2}{z} + c_x + \alpha\, c_z\, \cos\phi,
\tag{12}
$$

$$
w_y - \alpha\, w_z\, \sin\phi = \frac{s_y - H/2}{z} + c_y - \alpha\, c_z\, \sin\phi.
\tag{13}
$$

The two linear combinations
$w_x + \alpha w_z \cos\phi$
and $w_y - \alpha w_z \sin\phi$
are uniquely determined.
The three world coordinates
$(w_x, w_y, w_z)$ individually
are not determined.
The pre-image of a screen pixel
is a line
in the three-dimensional world,
the picking ray of oblique projection.

The candidate set
is therefore

$$
\{ (w_x,\ w_y,\ w_z) : w_x = u_x - \alpha\, w_z\, \cos\phi,\ w_y = u_y + \alpha\, w_z\, \sin\phi,\ w_z \in \mathbb{R} \},
\tag{14}
$$

where $u_x = (s_x - W/2)/z + c_x + \alpha c_z \cos\phi$
and $u_y = (s_y - H/2)/z + c_y - \alpha c_z \sin\phi$
are the determined linear combinations.
The line is parameterised by the depth $w_z$
along the picking ray.

The engine resolves the ambiguity
through one of three conventions
parallel to the conventions of the previous article.

The first is the ground-plane assumption.
The engine treats the click
as referring to the ground at $w_y = w_y^{\text{ground}}$
and solves for $w_z$,

$$
w_z = c_z + \frac{w_y^{\text{ground}} - c_y - (s_y - H/2)/z}{\alpha\, \sin\phi}.
\tag{15}
$$

The recovered $w_x$ follows from the first equation,

$$
w_x = \frac{s_x - W/2}{z} + c_x + \alpha\, (c_z - w_z)\, \cos\phi.
\tag{16}
$$

The convention is appropriate
when the click is interpreted as a movement command
to walk to a ground position.

The second is the known-depth assumption.
The engine treats the click
as referring to an object at a known depth $w_z^{\text{known}}$.
The recovered $w_x$ and $w_y$ follow from the inverse-map equations
with $w_z$ replaced by $w_z^{\text{known}}$.

The third is the screen-space sprite hit test.
The engine ignores the world coordinates entirely
and tests the clicked screen pixel
against the screen-space bounding rectangles
of every visible sprite.

The visible region of the world
on the ground plane $w_y = w_y^{\text{ground}}$
is the image of the screen rectangle
under the per-pixel ground-plane inverse map.
The region is a parallelogram in the $(w_x, w_z)$ plane.
The depth-axis edge of the parallelogram
runs along the world $w_z$ axis
with half-extent $H/(2\alpha\, z\, \sin\phi)$ in world units.
The lateral edge runs along the world $w_x$ axis
with half-extent $W/(2z)$ in world units,
shifted at each depth $w_z$
by the depth-dependent screen-space x offset
of the ground-plane inverse map.
The centre of the parallelogram
is the world point
that the screen centre $(W/2, H/2)$ inverts to,

$$
\mathbf{p}_{\text{world}}^{\text{centre}} = \left(c_x - (w_y^{\text{ground}} - c_y)\, \cot\phi,\ w_y^{\text{ground}},\ c_z + \tfrac{w_y^{\text{ground}} - c_y}{\alpha\, \sin\phi}\right).
\tag{17}
$$

The engine clips world content
to the visible parallelogram
when culling for rendering.

## A Worked Example

Consider an oblique-projection role-playing game
with the following parameters.
The screen is 320 pixels wide
and 200 pixels tall,
matching a typical late-1980s personal-computer resolution.
The zoom factor is $z = 1$,
one world unit per pixel.
The depth-mixing angle is $\phi = \pi/4$,
a 45-degree tilt.
The foreshortening factor is $\alpha = 1/2$,
the cabinet variant.
The ground-plane vertical world coordinate is $w_y^{\text{ground}} = 100$.
The camera position is $\mathbf{c} = (200, 80, 0)$.
The screen-centre offset is $\mathbf{o} = (160, 100)$.

For $\phi = \pi/4$,
$\cos\phi = \sin\phi = \sqrt{2}/2 \approx 0.7071$.
The depth-mixing direction
tilts equally into screen-x and negative screen-y
at the 45-degree angle.
A unit of world depth
shifts the screen position by
$\alpha \cos\phi = 0.5 \cdot 0.7071 \approx 0.3536$ pixels
along screen-x
and by $-\alpha \sin\phi \approx -0.3536$ pixels along screen-y
under cabinet projection.

A character on the ground
at world position $(200, 100, 0)$
projects to

$$
s_x = 1 \cdot (200 - 200) + 0.5 \cdot 1 \cdot (0 - 0) \cdot 0.7071 + 160 = 160,
\tag{18}
$$

$$
s_y = 1 \cdot (100 - 80) - 0.5 \cdot 1 \cdot (0 - 0) \cdot 0.7071 + 100 = 20 + 100 = 120.
\tag{19}
$$

The character renders at screen $(160, 120)$.

A character at the back of the playfield
at world position $(200, 100, 40)$
projects to

$$
s_x = 1 \cdot 0 + 0.5 \cdot 1 \cdot 40 \cdot 0.7071 + 160 = 14.14 + 160 \approx 174,
\tag{20}
$$

$$
s_y = 1 \cdot 20 - 0.5 \cdot 1 \cdot 40 \cdot 0.7071 + 100 = 20 - 14.14 + 100 \approx 106.
\tag{21}
$$

The back character renders at approximately screen $(174, 106)$.
The screen position has shifted
both to the right and upward
compared to the player at world depth zero,
matching the 45-degree quarter-view tilt.

A character at the front of the playfield
at world position $(200, 100, -20)$
projects to

$$
s_x \approx 1 \cdot 0 + 0.5 \cdot (-20) \cdot 0.7071 + 160 \approx -7.07 + 160 \approx 153,
\tag{22}
$$

$$
s_y \approx 20 - 0.5 \cdot (-20) \cdot 0.7071 + 100 \approx 20 + 7.07 + 100 \approx 127.
\tag{23}
$$

The front character renders at approximately $(153, 127)$,
shifted to the left and downward
relative to the player.

The cavalier variant
with $\alpha = 1$
doubles the per-unit screen shift
of the cabinet variant.
The back character at world $(200, 100, 40)$
under cavalier projection
would render at approximately
$(160 + 28.28,\ 120 - 28.28) = (188, 92)$
instead of $(174, 106)$.
The cavalier variant produces
a more pronounced depth shift
on the screen
for the same world depth offset.

The round-trip identity holds
along the ground plane
under either variant,

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
\tag{24}
$$

where $\varepsilon$ is the floating-point precision of the engine.

The Y-sort criterion of the previous article
extends to oblique projection
through the same back-to-front
ground-projection screen-y comparison.
A character at larger $w_z$
has a smaller ground-projection $s_y$
and is drawn earlier in the frame.
The criterion writes as

$$
\text{draw } i \text{ before } j \iff s_{y,i}^{\text{ground}} < s_{y,j}^{\text{ground}} \iff w_{z,i} > w_{z,j},
\tag{25}
$$

which is the same comparison
the belt-scroll article introduced.
Oblique projection introduces no new sort criterion
beyond what belt-scroll already required.

## Variations Within the Mode

The oblique-projection framework
admits several variations
that engines have explored.

A cavalier-variant scene
sets $\alpha = 1$ everywhere.
The depth axis appears pronounced
in the screen image.
The variant is rare in games
because the visual stretch is unattractive.
Engineering drawings use cavalier
where measurement accuracy is required.

A cabinet-variant scene
sets $\alpha = 1/2$ everywhere.
The depth axis appears foreshortened.
The variant is the dominant choice
in oblique-projection games.

A mixed-angle scene
varies $\phi$ between scenes
to reflect changes in the world geometry
or in the camera orientation.
The variant is rare in classic games
because the discontinuity in depth-mixing direction
disorients the player.

A per-object foreshortening variant
allows each object
to use its own $\alpha$
that the engine chooses
based on the object class.
Small foreground objects might use $\alpha = 1$
to emphasise their position
while large background structures use $\alpha = 1/2$
to recede into the scene.
The variant breaks the projection invariant
and is mathematically inconsistent
but appears in stylised games
that prioritise visual hierarchy over geometric accuracy.

A two-axis foreshortening variant
allows different foreshortening factors
along the $w_z$ axis
and along an additional rotated axis.
The variant approaches axonometric projection
where the world axes themselves
take rotated screen-space angles.
The next article in the cluster
treats the axonometric generalisation.

A non-zero $w_y$ contribution from the depth axis
appears when the camera tilts
to look down at the scene
in addition to looking obliquely.
The variant combines oblique projection
with a tilted camera frame
and produces an effect midway between
cabinet oblique and isometric.
The article treats it
as a generalised oblique with two independent shear angles.

A wrapping world boundary
applies the modulo operation
to the world coordinates
before the forward map,
producing an infinite oblique terrain
from a small content tile.
Strategy games such as Populous
use the wrapping variant
to render a much larger apparent world
than the world data holds.

## Delivery Mechanisms

The oblique-projection forward map
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
through the late 1980s and early 1990s
and on the personal-computer titles of the era
including Populous and Ultima VII.

The second is sprite-on-tile-background
with pre-tilted tile graphics.
The engine paints each background tile
already in its oblique-projected form
into a tile-grid background layer
that the hardware scrolls
without further per-tile transformation.
The sprites for moving objects
sit above the background
at engine-computed oblique screen positions.
The mechanism saves runtime computation
at the cost of tile-set storage
for the pre-tilted tiles.
Period console oblique games used this technique.

The third is line-by-line oblique scroll modulation.
The engine updates the horizontal scroll register
during the horizontal-blank interrupt
to produce a per-scanline horizontal shift
that simulates the oblique projection
for a single-layer background.
The technique appears
on the Nintendo Entertainment System
in games that wanted oblique effects
but had only the single-background-layer hardware.
The mechanism is rare in pure oblique games
and more common in stylised hybrids.

The fourth is pre-rendered oblique sprite atlases.
The engine pre-renders each sprite
at the oblique angle
and stores the result as a sprite atlas.
The runtime renderer
draws the appropriate atlas frame
without computing the forward map per frame
because the sprite frame already encodes the oblique transformation.
The mechanism is common in console role-playing games
of the early 1990s
where the central-processing-unit budget
could not support runtime sprite tilting.

The fifth is graphics-processing-unit-accelerated quad rendering.
Modern game engines
such as Unity, Godot, and Unreal
render the oblique world
as textured quads
in three-dimensional world space
with a camera transform
that produces the desired oblique projection.
The graphics processing unit
performs the depth sort
through its built-in depth buffer
and produces the screen image.
The depth buffer enforces the back-to-front sort
at the rasterisation level
without requiring the engine
to maintain a per-frame sprite sort list.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
the tile-set storage budget,
the central-processing-unit budget for runtime transformation,
the sprite-atlas storage budget,
and the achievable frame rate.

## Where the Framing Breaks Down

The oblique-projection framing is insufficient
when any of the following conditions hold.

When the world axes themselves
take rotated screen-space angles
rather than remaining parallel to the screen,
the projection becomes axonometric
and the next article in the cluster
treats the case.
Oblique projection
keeps the world's $x$ and $y$ axes
parallel to the screen.
Axonometric projection
rotates the world axes
so that all three world axes
take different screen-space angles.

When the depth axis must show
true perspective foreshortening
proportional to inverse distance,
the affine projection of this article
is insufficient.
The sprite-scaling article later in the series
treats the depth-dependent sprite scaling case.
The synthesis closer of the series
treats the full projective generalisation.

When the camera tilts so steeply
that the floor case
becomes a top-down view,
the foreshortening factor $\alpha$ approaches $1$
and the depth axis collapses into screen y.
The article treats this as the belt-scroll limit
already covered in the previous article.

When the camera rotates around the depth axis,
the depth-mixing direction $\phi$
rotates with it,
which the article treats as a per-frame change
in the forward map's $\phi$ parameter.
The variant is uncommon
but mathematically straightforward.

When the world has a non-flat ground,
the oblique projection
still applies to each point
but the visible terrain
deviates from the simple ground rectangle
of the worked example.
The engine renders the terrain
through a triangulated mesh
that the forward map projects
on a per-vertex basis.

## The Canon

The following games
use oblique projection
as their primary projection mode.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Habitat][ref_habitat]
on the Commodore 64 in 1986
gave the personal computer
its first networked-persistent-world social game
through a cabinet-oblique room-and-avatar rendering style.
The world was a set of rooms
each rendered as a cabinet-oblique cuboid
that the avatars walked around in
under the constraints of the Commodore 64's graphics.

[Populous][ref_populous]
from Bullfrog in 1989
gave the strategy genre
its canonical cabinet-oblique terrain
and the god-game subgenre.
The deformable terrain
rendered as a small portion of a wrapping world map
through a cabinet projection
that tilted the depth axis
into the upper-left of the screen.

[Ultima VII, The Black Gate][ref_ultima_7]
from Origin in 1992
brought oblique projection
to the mass-market personal-computer role-playing game
through a continuous oblique-projected world
of tile-based oblique cuboids,
trees and buildings with cabinet-style depth shifts,
and an interactive object system
that became the visual template
for several subsequent Origin titles.

Each game in the canon
uses an oblique projection
with a different choice of $\phi$ and $\alpha$,
a different camera policy,
and a different choice of delivery mechanism
appropriate to the target hardware.

## Out of Scope

The article does not cover
the following.

Axonometric projection
where the world axes themselves
take rotated screen-space angles
is the subject of the next article in the cluster.
Isometric, dimetric, and trimetric variants
all fall under the axonometric framework
that the article does not treat here.

True perspective projection
with a perspective denominator
is the subject of the synthesis closer of the series.
Oblique projection is a parallel projection
without perspective foreshortening.

Sprite scaling along the depth axis
is the subject of the sprite-scaling article
later in the series.
The classic oblique projection
does not scale sprites with depth.

The full Y-sort framework
including tie-breaking rules
and the Z-sort alternative
is the subject of a later cross-cutting article.
The article treats the Y-sort criterion
in its simplest form
matching the belt-scroll article's treatment.

The full pick-disambiguation framework
including the sprite-scale-and-rotate hit-test
is the subject of a later cross-cutting article.
The article presents the three baseline conventions
parallel to the belt-scroll article's treatment.

The choice between oblique and isometric
for a given game
is a design question
the series does not adjudicate.
Each projection has games for which it is the right choice
and games for which it is the wrong choice.

## Conclusion

Oblique projection
extends the belt-scroll forward map of the previous article
by allowing the depth-mixing direction
to take any screen-space angle.
The forward map gains
a two-axis shear factor
controlled by an angle $\phi$
and a foreshortening factor $\alpha$.
The cavalier and cabinet variants
correspond to $\alpha = 1$ and $\alpha = 1/2$ respectively,
trading measurement accuracy
for naturalistic appearance.
The inverse map is underdetermined
and admits the three disambiguation conventions
that the belt-scroll article introduced.
The Y-sort criterion
applies unchanged
because both belt-scroll and oblique projection
share the same depth-to-screen-y relationship.
The mode reached its visual peak
on the personal-computer titles of the early 1990s
before the industry moved
to hardware-accelerated three-dimensional rendering.
The next article in the cluster
generalises the oblique-shear matrix
to a full axonometric rotation
in which all three world axes
take distinct screen-space angles.
Isometric, dimetric, and trimetric projection
are the cases the next article distinguishes.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 25 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 25, 25 are established and 0 are bespoke.
World coordinates take $w_y$ increasing downward and $w_z$ increasing into the screen, the depth angle is in radians measured so that depth tilts toward positive screen $x$ and negative screen $y$, and the foreshortening factor is the screen length in world units of one unit of depth before the zoom.

**Equation 1, Oblique Forward Map for Screen X.**
The horizontal screen coordinate adds to the side-scrolling term a depth shift of the foreshortening factor times the cosine of the depth angle.

$$
s_x = z\, (w_x - c_x) + \alpha\, z\, (w_z - c_z)\, \cos\phi + W/2,
\tag{1}
$$

**Equation 2, Oblique Forward Map for Screen Y.**
The vertical screen coordinate subtracts from the side-scrolling term a depth shift of the foreshortening factor times the sine of the depth angle.

$$
s_y = z\, (w_y - c_y) - \alpha\, z\, (w_z - c_z)\, \sin\phi + H/2,
\tag{2}
$$

**Equation 3, Oblique Forward Map in Vector Form.**
The oblique forward map is the side-scrolling map plus the scaled depth offset along a fixed screen-space unit direction set by the depth angle.

$$
\mathbf{p}_{\text{screen}} = z\, \big((w_x, w_y) - (c_x, c_y)\big) + \alpha\, z\, (w_z - c_z)\, \mathbf{d}(\phi) + \mathbf{o}.
\tag{3}
$$

**Equation 4, Screen Separation of Two Depths.**
By linearity, two points differing only in depth separate on screen along the depth direction by the foreshortening factor times the zoom times their depth difference.

$$
\Delta \mathbf{p}_{\text{screen}} = \alpha\, z\, (w_{z,1} - w_{z,2})\, \mathbf{d}(\phi).
\tag{4}
$$

**Equation 5, Oblique Forward Map as a Three-by-Four Matrix.**
The forward map acts on the augmented world coordinate through a three-by-four affine matrix whose depth column holds the two depth-direction components.

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & \alpha\, z\, \cos\phi & W/2 - z\, c_x - \alpha\, z\, c_z\, \cos\phi \\ 0 & z & -\alpha\, z\, \sin\phi & H/2 - z\, c_y + \alpha\, z\, c_z\, \sin\phi \\ 0 & 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ w_z \\ 1 \end{bmatrix}.
\tag{5}
$$

**Equation 6, Factorisation with Two-Axis Shear.**
The forward map factors as a camera translation, a two-axis depth shear, an orthogonal projection that drops depth, a uniform scale and a screen-centre translation.

$$
F = T(\mathbf{o})\, S(z)\, P_z\, K(\alpha, \phi)\, T(-\mathbf{c}),
\tag{6}
$$

**Equation 7, Two-Axis Depth Shear Matrix.**
The shear adds the depth-driven shifts to both the horizontal and vertical components, generalising the single-axis shear of the belt-scroll mode.

$$
K(\alpha, \phi) =
\begin{bmatrix} 1 & 0 & \alpha\, \cos\phi \\ 0 & 1 & -\alpha\, \sin\phi \\ 0 & 0 & 1 \end{bmatrix},
\tag{7}
$$

**Equation 8, Orthogonal Projection Dropping Depth.**
The two-by-three orthogonal projection keeps the horizontal and vertical components and discards depth.

$$
P_z =
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}.
\tag{8}
$$

**Equation 9, Vertical World Coordinate of an Airborne Character.**
An airborne character sits above the ground by its height, which under the downward vertical convention subtracts from the ground coordinate.

$$
w_y = w_y^{\text{ground}} - h.
\tag{9}
$$

**Equation 10, Airborne Sprite Offset from Its Shadow.**
The airborne sprite is drawn at the shadow screen position shifted up the screen by the height times the zoom.

$$
\mathbf{p}_{\text{screen}}^{\text{sprite}} = \mathbf{p}_{\text{screen}}^{\text{shadow}} - (0,\ z\, h),
\tag{10}
$$

**Equation 11, Screen Separation of Sprite and Shadow.**
The vertical pixel separation between an airborne sprite and its shadow is the height multiplied by the zoom factor, independent of the depth direction.

$$
\Delta s_y = z\, h.
\tag{11}
$$

**Equation 12, Inverse Constraint from Screen X.**
The horizontal screen coordinate fixes only the combination of the horizontal world coordinate and the depth along the cosine of the depth angle.

$$
w_x + \alpha\, w_z\, \cos\phi = \frac{s_x - W/2}{z} + c_x + \alpha\, c_z\, \cos\phi,
\tag{12}
$$

**Equation 13, Inverse Constraint from Screen Y.**
The vertical screen coordinate fixes only the combination of the vertical world coordinate and the depth along the sine of the depth angle.

$$
w_y - \alpha\, w_z\, \sin\phi = \frac{s_y - H/2}{z} + c_y - \alpha\, c_z\, \sin\phi.
\tag{13}
$$

**Equation 14, Picking Line of Oblique Projection.**
The world points that project to one pixel form a line parameterised by depth, the picking ray of oblique projection.

$$
\{ (w_x,\ w_y,\ w_z) : w_x = u_x - \alpha\, w_z\, \cos\phi,\ w_y = u_y + \alpha\, w_z\, \sin\phi,\ w_z \in \mathbb{R} \},
\tag{14}
$$

**Equation 15, Depth Recovered under the Ground-Plane Convention.**
Setting the vertical world coordinate to the ground resolves the picking line to a single depth through the vertical constraint.

$$
w_z = c_z + \frac{w_y^{\text{ground}} - c_y - (s_y - H/2)/z}{\alpha\, \sin\phi}.
\tag{15}
$$

**Equation 16, Horizontal Coordinate Recovered on the Ground Plane.**
Substituting the recovered depth into the horizontal constraint gives the horizontal world coordinate of the ground point.

$$
w_x = \frac{s_x - W/2}{z} + c_x + \alpha\, (c_z - w_z)\, \cos\phi.
\tag{16}
$$

**Equation 17, World Point under the Screen Centre.**
Inverting the screen centre onto the ground plane gives the centre of the visible ground parallelogram.

$$
\mathbf{p}_{\text{world}}^{\text{centre}} = \left(c_x - (w_y^{\text{ground}} - c_y)\, \cot\phi,\ w_y^{\text{ground}},\ c_z + \tfrac{w_y^{\text{ground}} - c_y}{\alpha\, \sin\phi}\right).
\tag{17}
$$

**Equation 18, Worked Screen X of a Grounded Character.**
With unit zoom, an illustrative camera at $(200, 80, 0)$, a depth angle of $\pi/4$ and the cabinet foreshortening of one half, a character at $(200, 100, 0)$ lands at screen $x = 160$.

$$
s_x = 1 \cdot (200 - 200) + 0.5 \cdot 1 \cdot (0 - 0) \cdot 0.7071 + 160 = 160,
\tag{18}
$$

**Equation 19, Worked Screen Y of a Grounded Character.**
The same character lands at screen $y = 120$, since its depth equals that of the camera.

$$
s_y = 1 \cdot (100 - 80) - 0.5 \cdot 1 \cdot (0 - 0) \cdot 0.7071 + 100 = 20 + 100 = 120.
\tag{19}
$$

**Equation 20, Worked Screen X of a Rear Character.**
A character forty units deeper is shifted about fourteen pixels right to screen $x \approx 174$.

$$
s_x = 1 \cdot 0 + 0.5 \cdot 1 \cdot 40 \cdot 0.7071 + 160 = 14.14 + 160 \approx 174,
\tag{20}
$$

**Equation 21, Worked Screen Y of a Rear Character.**
The rear character is shifted about fourteen pixels up to screen $y \approx 106$.

$$
s_y = 1 \cdot 20 - 0.5 \cdot 1 \cdot 40 \cdot 0.7071 + 100 = 20 - 14.14 + 100 \approx 106.
\tag{21}
$$

**Equation 22, Worked Screen X of a Front Character.**
A character twenty units nearer is shifted about seven pixels left to screen $x \approx 153$.

$$
s_x \approx 1 \cdot 0 + 0.5 \cdot (-20) \cdot 0.7071 + 160 \approx -7.07 + 160 \approx 153,
\tag{22}
$$

**Equation 23, Worked Screen Y of a Front Character.**
The front character is shifted about seven pixels down to screen $y \approx 127$.

$$
s_y \approx 20 - 0.5 \cdot (-20) \cdot 0.7071 + 100 \approx 20 + 7.07 + 100 \approx 127.
\tag{23}
$$

**Equation 24, Round Trip along the Ground Plane.**
For a point on the ground plane, the forward map followed by the ground-plane inverse returns the original world position up to floating-point precision.

$$
F^{-1}_{\text{ground}}(F(\mathbf{p}_{\text{world}}^{\text{ground}})) = \mathbf{p}_{\text{world}}^{\text{ground}} + O(\varepsilon),
\tag{24}
$$

**Equation 25, Y-Sort Draw Order Criterion.**
An object is drawn before another exactly when its ground-projection screen $y$ is smaller, which is equivalent to its lying deeper.

$$
\text{draw } i \text{ before } j \iff s_{y,i}^{\text{ground}} < s_{y,j}^{\text{ground}} \iff w_{z,i} > w_{z,j},
\tag{25}
$$

### Notation

- $w_z$, the depth into the screen
- $c_z$, the depth component of the camera position $(c_x, c_y, c_z)$
- $z$, the zoom factor
- $\alpha$, the foreshortening factor, the screen length of one unit of depth along the depth-mixing direction
- $\phi$, the depth-mixing angle, in the open interval from zero to $\pi$
- $\mathbf{d}(\phi)$, the screen-space depth-direction unit vector $(\cos\phi, -\sin\phi)$
- $\mathbf{o}$, the screen centre offset $(W/2, H/2)$ in pixels
- $K(\alpha, \phi)$, the three-by-three two-axis depth shear matrix
- $P_z$, the two-by-three orthogonal projection that drops depth
- $w_y^{\text{ground}}$, the vertical world coordinate of the ground plane
- $h$, the height of an airborne character above the ground
- $u_x$, the horizontal constraint value fixed by the screen $x$ of a click
- $u_y$, the vertical constraint value fixed by the screen $y$ of a click
- $\varepsilon$, the floating-point precision of the engine

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "Habitat (Video Game)." 2026. Wikipedia. Last modified June 7, at 04:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Habitat\_(video\_game)&oldid=1358188343][ref_habitat]
- "Populous (Video Game)." 2026. Wikipedia. Last modified May 19, at 02:35 (UTC). [https://en.wikipedia.org/w/index.php?title=Populous\_(video\_game)&oldid=1354942904][ref_populous]
- "Ultima VII: The Black Gate." 2026. Wikipedia. Last modified June 26, at 08:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Ultima\_VII%3A\_The\_Black\_Gate&oldid=1361194463][ref_ultima_7]

[ref_habitat]: https://en.wikipedia.org/w/index.php?title=Habitat_(video_game)&oldid=1358188343
[ref_populous]: https://en.wikipedia.org/w/index.php?title=Populous_(video_game)&oldid=1354942904
[ref_ultima_7]: https://en.wikipedia.org/w/index.php?title=Ultima_VII%3A_The_Black_Gate&oldid=1361194463
