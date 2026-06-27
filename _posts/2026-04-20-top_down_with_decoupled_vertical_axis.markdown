---
layout: post
mathjax: true
comments: true
title:  "Top-Down with Decoupled Vertical Axis"
date:   2026-04-20 09:00:00 +0000
categories: games graphics projection
---

<!-- A175 -->
<script>console.log("A175");</script>

The top-down view of the previous article
has a single ground plane.
Every world object sits on it.
Every screen pixel maps to a single world point.
A new gameplay feature,
the ability for an object to leave the ground plane,
breaks both invariants.
The article adds a vertical axis
decoupled from the two horizontal axes
that the floor case treats.
The forward map gains a height-to-screen-offset term
that shifts the rendered object
upward on the screen
in proportion to its height above the ground.
The inverse map ceases to return a unique world point
and instead returns a family of candidates
indexed by height.
The engine resolves the ambiguity
through a convention
that makes the height axis legible to the player,
the shadow drop.

The mode is recognisable
in nearly every top-down action game
that lets the player jump.
The camera still looks straight down
at a horizontal world plane.
The world coordinates still divide
into two horizontal components
that the player navigates with the directional pad.
The third component,
height,
evolves independently
under the player's jump button
or under the game's physics
when the object is airborne.
The shadow trails the object
along the ground plane
and lets the player see
where the object will land.

The framing the series carries
from the opener
distinguishes the math
from the delivery mechanism.
The math of the decoupled vertical axis
is a single scalar height
that produces a single vertical screen offset.
The delivery
is the choice of how the engine
splits the rendered object
between a sprite at the offset position
and a shadow sprite at the unoffset position,
and how the engine
animates the height value across frames.
The math is shared
between every game in the canon below.
The delivery
varies by hardware capability,
art direction,
and gameplay feel.

## A Brief History of the Mode

The decoupled vertical axis emerges
with the introduction of jumping
into the otherwise flat top-down view.
[StarTropics][ref_startropics]
on the Nintendo Entertainment System in 1990
gave the home console
one of the earliest top-down games
with a player-character jump
and a visible shadow
under the airborne protagonist.
The jump
crosses gaps between tiles
in a way the flat top-down view of [The Legend of Zelda][ref_zelda]
on the same console
in 1986
could not express.

[The Legend of Zelda, A Link to the Past][ref_link_to_the_past]
on the Super Nintendo Entertainment System
in 1991
introduced the multi-level ground plane
into the top-down Zelda formula.
Link does not jump on a button
but falls from upper ledges to lower ones
and is moved up and down
by gameplay events.
The stepped ground heights
the engine renders
are the discrete-ground variation
of the decoupled vertical axis
treated in the section below.

[The Legend of Zelda, Link's Awakening][ref_links_awakening]
on the Game Boy in 1993
gave the handheld
its canonical jump mechanic
via the Roc's Feather item.
The shadow on the ground
beneath the jumping Link
is the player's only cue
to where the jump will land.
The Game Boy's lack of colour
and the small screen
made the shadow especially valuable
as a visual signal.

The convention reaches the modern independent game
through titles such as
[Hyper Light Drifter][ref_hyper_light_drifter]
on Microsoft Windows in 2016.
The drifter renders with a persistent ground shadow
that the engine offsets briefly
during dashes across pits
and during projectile attacks.
The framing has not changed
in three decades of top-down design.

The shadow-drop convention itself
is older than the gameplay use of it.
Animation studios used drop shadows
to ground their characters in space
well before any video game existed.
The video-game-specific innovation
is the use of the shadow
as a gameplay-readable signal
of the underlying height value
that the player otherwise cannot see.

## The Forward Map

The world coordinate
of a jumping object
is now three-dimensional.
The horizontal position
remains the two-dimensional world point
$\mathbf{p}_{\text{world}} = (w_x, w_y)$
from the floor case.
The height above the ground
is a non-negative scalar $h$
in the same world units
as the horizontal position.

The forward map
for the object sprite
adds the height-to-screen offset
to the floor-case forward map,

$$
\mathbf{p}_{\text{screen}}^{\text{obj}} = z\, (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o} - (0,\ z\, h),
$$

where $z$ is the zoom factor,
$\mathbf{c}$ is the camera position,
and $\mathbf{o}$ is the screen centre offset
from the previous article.
The negative sign on the height term
reflects the screen $y$ convention
where the $y$ axis increases downward
and the height axis increases upward.
A higher object sits closer to the top of the screen.

The forward map
for the shadow sprite
omits the height term entirely,

$$
\mathbf{p}_{\text{screen}}^{\text{shadow}} = z\, (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o}.
$$

The shadow sprite
sits at the screen position
the object would occupy
if its height were zero.
The vertical separation between the object sprite and the shadow sprite
in screen-space pixels is therefore

$$
\Delta s_y = z\, h.
$$

The pixel separation grows
linearly with the height value
and linearly with the zoom factor.
A doubled zoom
doubles the apparent jump height,
which is the desired behaviour
since the world has merely been viewed more closely.

The factorisation pattern from the opener
extends to the height case
by treating the height-induced shift
as an additional translation
applied after the floor-case forward map.
Writing $T_v(h) = T(0,\ -z\, h)$
for the height-driven vertical shift in screen space,
the forward map for the object factors as

$$
F_{\text{obj}} = T_v(h)\, T(\mathbf{o})\, S(z)\, T(-\mathbf{c}).
$$

The forward map for the shadow
is the same composition
with $T_v(0)$
in place of $T_v(h)$,

$$
F_{\text{shadow}} = T(\mathbf{o})\, S(z)\, T(-\mathbf{c}).
$$

The two factorisations share
the right-hand three matrices,
which is the engine's reason
for computing the floor-case position once
and applying the height shift only to the object sprite.

The homogeneous form
aggregates the same forward map
into a single three-by-four matrix
acting on the four-component augmented world coordinate
$(w_x,\ w_y,\ h,\ 1)$,

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & 0 & W/2 - z\, c_x \\ 0 & z & -z & H/2 - z\, c_y \\ 0 & 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x \\ w_y \\ h \\ 1 \end{bmatrix}.
$$

The matrix is the affine specialisation
of the four-by-four projective generalisation
established in the opener,
where the projective coefficients in the lower rows have been zeroed
and the orthographic projection from three world dimensions
to two screen dimensions is the resulting map.
The shadow forward map shares the matrix
with one entry changed,

$$
M_{\text{shadow}} =
\begin{bmatrix} z & 0 & 0 & W/2 - z\, c_x \\ 0 & z & 0 & H/2 - z\, c_y \\ 0 & 0 & 0 & 1 \end{bmatrix}.
$$

The shadow matrix and the object matrix
differ in exactly the one entry
that encodes the height-to-screen offset,
the entry $-z$ in position $(2, 3)$.
The article therefore frames the decoupled vertical axis
as the simplest non-trivial parallel projection
from a three-dimensional world
onto a two-dimensional screen
in the series.

When the height varies over time,
the time-evolution of $h$
is governed by gameplay physics
and not by the forward map.
A canonical parabolic jump uses

$$
h(t) = h_0 + v_0\, t - \tfrac{1}{2}\, g\, t^2,
$$

where $h_0$ is the launch height,
$v_0$ is the launch vertical velocity,
$g$ is the gravity constant in world units per second squared,
and $t$ is the elapsed time since launch.
The forward map applies the current $h(t)$
to the object sprite
on every rendered frame.
The horizontal coordinates $(w_x, w_y)$
evolve independently
under whatever horizontal-motion rule
the gameplay specifies.
This independence
is the operational meaning
of the term decoupled vertical axis.

## The Inverse Map

The forward map for the object sprite
takes three world inputs $(w_x, w_y, h)$
and produces two screen outputs $(s_x, s_y)$.
The system is underdetermined.
No closed-form inverse exists
that recovers all three world inputs
from the two screen outputs alone.
Algebraically,
the inverse map returns a one-parameter family of world candidates
indexed by an unknown height.

Solving the forward map for the world coordinates
in terms of the screen coordinates and the height yields

$$
w_x = \frac{s_x - o_x}{z} + c_x,
$$

$$
w_y = \frac{s_y - o_y + z\, h}{z} + c_y = \frac{s_y - o_y}{z} + c_y + h.
$$

The horizontal world coordinate $w_x$
is uniquely determined.
The vertical world coordinate $w_y$
depends linearly on the unknown height $h$.
A larger assumed height
shifts the candidate world position
further from the top of the screen
in the world frame,
which corresponds to objects further back
along the ground plane
beneath higher airborne objects.

When the height is known
the inverse map collapses to a single point
expressible in vector form as

$$
\mathbf{p}_{\text{world}}(h) = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \mathbf{c} + (0,\ h).
$$

The ground-plane case at $h = 0$
reduces to the floor-case inverse from the previous article.
The airborne case at $h > 0$
shifts the inverse-mapped world point
southward by $h$ world units
relative to the floor case.

The candidate set is therefore

$$
\{ (w_x, w_y, h) : w_y = \frac{s_y - o_y}{z} + c_y + h,\ h \geq 0 \}.
$$

The engine resolves the ambiguity
through one of three conventions.

The first is the ground-plane assumption.
The engine treats the click
as referring to the ground
and sets $h = 0$.
The recovered world point is

$$
\mathbf{p}_{\text{world}}^{\text{ground}} = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \mathbf{c},
$$

which is exactly the floor-case inverse map
from the previous article.
The convention is appropriate
when the click is interpreted as a movement command
or a ground-targeted action.

The second is the shadow-tracking assumption.
If a shadow sprite is rendered
beneath every airborne object,
the engine can search
for an object whose shadow sprite
contains the clicked screen pixel.
The shadow sprite sits at the floor-case screen position
of the object,
so the search is identical
to the floor-case picking strategy from the previous article.
The convention is appropriate
when the player is selecting an airborne object
by clicking its shadow on the ground.

The third is the screen-space hit test.
The engine ignores the world height entirely
and tests the clicked screen pixel
against the screen-space bounding rectangle
of every visible sprite.
This convention recovers the screen-rendered object
rather than the world-space ground point,
and is appropriate for direct sprite selection
such as cursor-driven gameplay
or light-gun targeting.
The screen-space hit test is treated
in detail in the cross-cutting picking article
later in the series.

The candidate set
collapses to a small finite set
or to a bounded one-parameter segment
in three practically important cases.

The first is when the engine maintains
a known list of airborne objects
and their current heights.
The inverse evaluates once per object
using the vector form above
with the object's height substituted.
The closest hit in screen distance
is returned.

The second is when the game restricts jumps
to a single discrete height $h_{\text{jump}}$.
The candidate set has cardinality at most two,

$$
\{(w_x,\ w_y^{(0)},\ 0),\ (w_x,\ w_y^{(1)},\ h_{\text{jump}})\},
$$

where $w_y^{(0)} = (s_y - o_y)/z + c_y$ is the ground candidate
and $w_y^{(1)} = (s_y - o_y)/z + c_y + h_{\text{jump}}$ is the airborne candidate.
The engine tests both candidates
against the world's object list
and returns the matching object.

The third is when the game caps the height
at a maximum value $h_{\max}$.
The candidate set is a bounded line segment
in three-dimensional world space,

$$
\{(w_x,\ w_y,\ h) : h \in [0,\ h_{\max}],\ w_y = (s_y - o_y)/z + c_y + h\},
$$

parameterised uniquely by the height $h$.
The engine intersects the segment
with the bounding volumes of airborne candidates
to identify a match.

The visible region of the world
for an object at a known height $h$
is the pre-image of the screen rectangle
under the inverse map evaluated at that height,

$$
\mathbf{p}_{\text{world}}(h) \in \mathbf{c} + (0,\ h) + \left[ -\tfrac{W}{2z},\ \tfrac{W}{2z} \right] \times \left[ -\tfrac{H}{2z},\ \tfrac{H}{2z} \right].
$$

The rectangle is the floor-case viewport from the previous article
shifted southward in the world frame
by $h$ world units.
A renderer that must include
every potentially-visible airborne object
with height in the range $[0, h_{\max}]$
queries the union of the per-height rectangles,

$$
\mathbf{p}_{\text{world}} \in \mathbf{c} + \left[ -\tfrac{W}{2z},\ \tfrac{W}{2z} \right] \times \left[ -\tfrac{H}{2z},\ \tfrac{H}{2z} + h_{\max} \right].
$$

The extended rectangle adds a strip of width $h_{\max}$
along the south edge of the floor-case viewport
to capture the world points
whose ground projection
sits below the visible screen
but whose airborne projection
sits within it.

## A Worked Example

Consider the same top-down role-playing game
from the previous article's worked example.
The screen is 800 pixels wide and 600 pixels tall.
The zoom factor is $z = 1$.
The camera is centred on the player at world position
$\mathbf{c} = (500, 400)$.
The screen offset is $\mathbf{o} = (400, 300)$.
The player executes a jump
from world position $\mathbf{p}_{\text{world}} = (520, 410)$
with launch velocity $v_0 = 60$ world units per second
and gravity $g = 200$ world units per second squared.

The jump duration
from the parabolic trajectory equation
is $t_{\text{end}} = 2\, v_0 / g = 0.6$ seconds,
during which the height
peaks at $h_{\text{max}} = v_0^2 / (2\, g) = 9$ world units.

At $t = 0.3$ seconds,
the apex,
the height is $h = 9$.
The forward map for the object sprite gives

$$
\mathbf{p}_{\text{screen}}^{\text{obj}} = (400 + 20,\ 300 + 10 - 9) = (420,\ 301).
$$

The forward map for the shadow sprite gives

$$
\mathbf{p}_{\text{screen}}^{\text{shadow}} = (400 + 20,\ 300 + 10) = (420,\ 310).
$$

The two sprites differ by $\Delta s_y = 9$ pixels,
matching $z\, h = 1 \times 9 = 9$.
The shadow is nine pixels below the object on the screen
and tracks the horizontal motion of the object exactly.

Now consider a click at screen position $(420,\ 301)$
at the same moment.
The ground-plane inverse gives

$$
\mathbf{p}_{\text{world}}^{\text{ground}} = (520,\ 401),
$$

which is a world point one unit below the jumping player's horizontal position.
A movement command at this world point
would walk toward the click.
The click is not interpreted as a selection of the airborne player.

The shadow-tracking strategy
searches for an object whose shadow sprite contains $(420,\ 301)$.
The shadow sprite is at $(420,\ 310)$,
which is nine pixels away,
so the click misses the shadow.
The strategy returns no airborne object.

The screen-space hit test
searches the rendered sprites
for one whose bounding rectangle contains $(420,\ 301)$.
The jumping player's sprite,
rendered at $(420,\ 301)$,
contains the click.
The hit test returns the jumping player.

The three inverse strategies
return different answers
for the same click.
The engine must pick one strategy
appropriate to the gameplay action being requested.
A movement command should use the ground-plane inverse.
A selection of an airborne object should use the screen-space hit test
or the shadow-tracking strategy.

Verifying the round-trip
with the height value known
shows that the forward map for the object
followed by the inverse map at the same height
returns the original world position
within floating-point precision,

$$
F_{\text{obj},\,h}^{-1}(F_{\text{obj}}(\mathbf{p}_{\text{world}},\ h)) = \mathbf{p}_{\text{world}} + O(\varepsilon).
$$

The same identity holds for the shadow map
with the height fixed at zero,

$$
F_{\text{shadow}}^{-1}(F_{\text{shadow}}(\mathbf{p}_{\text{world}})) = \mathbf{p}_{\text{world}} + O(\varepsilon),
$$

which is the round-trip identity from the previous article.
Both identities hold
for every projection mode in the series
and serve as the simplest correctness tests
the engine can run.

## Variations Within the Mode

The shadow-drop convention
admits several variations
that engines have explored
without changing the underlying math.

A scaled shadow
shrinks the shadow sprite
as the height increases
to suggest the spreading of light
beneath a rising object.
The math is a per-frame uniform scale
of the shadow sprite by a factor

$$
s_{\text{shadow}} = \max(s_{\min},\ 1 - k\, h),
$$

where $k > 0$ is a scaling constant
and $s_{\min} > 0$ ensures the shadow remains visible.
The forward map for the shadow position is unchanged.

A faded shadow
reduces the shadow sprite's opacity
as the height increases,

$$
\alpha_{\text{shadow}} = \max(\alpha_{\min},\ 1 - k\, h).
$$

The combination of scaling and fading
is the dominant convention
in modern independent games
that need to render shadows on uneven terrain.

A multi-level ground plane
introduces discrete ground heights $h_{\text{ground}}(w_x, w_y)$
that the world allows.
The shadow sits at the ground beneath the object,

$$
\mathbf{p}_{\text{screen}}^{\text{shadow}} = z\, (\mathbf{p}_{\text{world}} - \mathbf{c}) + \mathbf{o} - (0,\ z\, h_{\text{ground}}(w_x, w_y)),
$$

and the object sprite uses
the effective height $h - h_{\text{ground}}(w_x, w_y)$
or absolute height,
depending on the engine's convention.
A Link to the Past uses this variation
to drop Link to a lower terrace
when he steps off a ledge.

A capped height
limits how high an object can rise above the ground.
The simplest cap is a maximum height $h_{\max}$
that the gameplay enforces.
The forward map is unchanged.
The cap matters
because the engine knows
that the candidate set in the inverse map
has bounded height,
which helps disambiguation.

A discrete jump
restricts the height to a finite set of values,
typically zero and a single airborne height.
The inverse map then has at most two candidates per click.
A discrete jump
appears in games where the gameplay logic
treats jumping as a binary state
rather than a continuous physical motion.

A scripted jump trajectory
replaces the parabolic motion
with a designer-authored animation curve.
The horizontal position
may also follow a designer-authored curve,
which means the horizontal axes
are no longer player-controlled
during the jump.
The forward map is unchanged
but the inputs to it
are driven by an animation system
rather than by player input.

A wall-climbing or rope-climbing motion
treats the height value
as the player's primary input
while the horizontal world coordinates are pinned.
The forward map is unchanged.
The decoupling is total
and inverted from the jumping case.

A free-fall from ledges
sets $v_0 = 0$ in the trajectory
and lets gravity pull the object down
to the next ground level.
The same parabolic trajectory equation applies
with negative launch velocity replaced by free fall.

A hookshot or grappling motion
moves the object
along a straight line
from a launch point to a target point in screen space.
The world horizontal coordinates evolve
while the height value
remains zero throughout the motion.
The shadow remains directly beneath the object
and the visual effect is a straight-line dash.

A swimming or flying mode
treats the world entirely above the ground plane
and renders no shadow at all,
or renders a shadow at a designer-chosen depth
that does not correspond to the floor.

## Delivery Mechanisms

The forward map's two-sprite structure,
one for the object and one for the shadow,
permits five distinct delivery mechanisms
on period hardware.

The first is a dedicated shadow sprite
in object attribute memory.
The hardware draws a separate sprite for the shadow
at the floor-case screen position.
The shadow sprite is typically a small dark ellipse
or a simple silhouette
that the engine treats as semi-transparent
through the picture-processing-unit's transparency or palette tricks.
The Super Nintendo Entertainment System
supports this through colour-add and colour-subtract effects
on the sprite layer.
The Nintendo Entertainment System
supports it through black silhouette sprites
that share a palette slot with the background.

The second is a tile-modified background
where the engine writes a shadow tile
into the background tile map
beneath each airborne object.
The shadow appears as a static element of the background
and disappears when the object lands.
The technique was used on the early home computers
that had tile-based backgrounds
but limited sprite counts.

The third is software composition
on a general-purpose central processing unit.
The engine renders the shadow sprite
into the frame buffer before the object sprite
and then renders the object sprite at the offset position.
This is the universal mechanism
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s
and on modern independent-game engines
that render to a software frame buffer
or to a graphics-processing-unit texture in a software-style pipeline.

The fourth is a per-sprite height attribute
in the object attribute memory
where the hardware applies the height-driven vertical offset
directly during sprite rendering.
The Sega Genesis sprite hardware
permits an arbitrary screen position for each sprite,
so the engine writes the offset position directly
and the hardware does not need to know about the height.
Period arcade hardware
with sufficient sprite-attribute precision
supports the same approach.

The fifth is a graphics-processing-unit-accelerated quad pair
where the modern game engine
renders the shadow quad and the object quad
as two textured quads
with the appropriate vertical offset between them.
The graphics processing unit
applies the matrix from the forward map factorisation
in hardware
and produces the screen image.

All five mechanisms
compute the same forward map
and produce the same visible result.
The choice trades implementation complexity,
sprite-budget pressure,
and the visual fidelity of the shadow effect.

## Where the Framing Breaks Down

The decoupled-vertical-axis framing is insufficient
when any of the following conditions hold.

When the height axis is fully integrated
with the camera projection,
which is to say
when the camera tilts to look at a true three-dimensional scene,
the decoupling is no longer mathematical.
The article is no longer the right model.
The series treats this case
in the affine-and-projective cluster
and in the synthesis closer.

When the gameplay requires
that the airborne object cast a shadow
on a vertical surface
such as a wall or a cliff face,
the simple ground-plane shadow drop
is insufficient.
The engine must compute the shadow's projection
onto a surface other than the floor,
which is a more involved geometric problem
that the article does not treat.

When multiple light sources
illuminate the airborne object,
multiple shadows must be drawn.
The shadow-drop convention
remains the floor case for each light source
but the engine must run the forward map
once per light source per object.

When the gameplay treats the height axis
as fully player-controlled,
which is to say
when the player has independent control of all three world axes,
the floor case for jumping is insufficient.
The mode becomes the belt-scroll mode
treated later in the cluster,
or the oblique mode
treated in the next cluster.

When the height axis is large enough
that the height-to-screen offset
moves the object off the screen,
the engine must zoom the camera out
or follow the object vertically.
The forward map is unchanged.
The camera policy
becomes the dominant gameplay-feel concern.

When the world has a curved ground surface
such as a hilltop or a slope,
the shadow drops onto the ground at a non-trivial geometric location.
The engine must trace
from the object's world position downward
to the world's first ground intersection
to compute the shadow position.
The article assumes a flat ground plane
throughout.

## The Canon

The following games
use the decoupled vertical axis
as a primary gameplay feature
of an otherwise top-down view.
The list is selective
rather than exhaustive.

[StarTropics][ref_startropics]
on the Nintendo Entertainment System in 1990
gave the home console
one of its earliest top-down adventures
with a player-character jump
and a visible shadow under the airborne protagonist.

[The Legend of Zelda, A Link to the Past][ref_link_to_the_past]
on the Super Nintendo Entertainment System
in 1991
introduced the multi-level ground plane
into the top-down Zelda formula.
Link falls from upper ledges to lower ones
across discrete ground heights
without a per-frame shadow on the falling sprite.
The multi-level convention
is the discrete-ground variation
treated above.

[The Legend of Zelda, Link's Awakening][ref_links_awakening]
on the Game Boy in 1993
generalised the Roc's Feather jump
as a canonical handheld example
of the decoupled vertical axis.
The shadow on the ground
remains legible
in spite of the Game Boy's monochrome display.

[Hyper Light Drifter][ref_hyper_light_drifter]
on Microsoft Windows in 2016
brought the convention into the modern independent game.
The drifter carries a persistent ground shadow
that the engine offsets briefly
during dashes across pits
and during airborne projectile sequences.

Each game in the canon
uses a variant of the height-augmented forward map.
The differences lie in the camera policy,
the art direction,
the gameplay rules
governing how height changes,
the use or omission of the per-frame shadow,
and the choice of delivery mechanism
appropriate to the target hardware.

## Out of Scope

The article does not cover
the following.

True three-dimensional shadows
that respect surface normals
and that change shape on uneven terrain
are a deferred subject
that the affine-and-projective cluster
of the series treats.

Volumetric shadow effects
such as soft shadows,
penumbra rendering,
and shadow mapping
are the domain of three-dimensional rendering
and are outside the series scope entirely.

Physics simulation
beyond the simple parabolic trajectory
is treated as a separate subject
that the series does not adjudicate.
Damped trajectories,
wind effects,
and inter-object collision during flight
are gameplay-physics questions
that the projection math does not depend on.

The dual case
where the world has an explicit depth axis
in addition to the height axis
is the belt-scroll mode
treated later in the Cartesian cluster.
The cases are distinguished
by whether the camera looks at the world
straight down,
which is the decoupled-vertical case,
or at an angle,
which is the belt-scroll case.

The use of height as a stealth or detection mechanic
in games where the airborne object
is hidden from enemies on the ground
is a gameplay-design question
the series does not treat.

The dedicated picking treatment
for stacked sprites at different heights
is deferred to the cross-cutting picking article
at the end of the series.

## Conclusion

Top-down with a decoupled vertical axis
adds a single scalar height
to the floor case of the previous article.
The forward map gains a height-to-screen vertical offset
that shifts the object sprite upward on the screen
in proportion to the height value and the zoom factor.
The shadow sprite renders at the unoffset floor-case position
and gives the player a legible cue
to the object's horizontal location and height.
The inverse map is no longer single-valued
and instead returns a candidate set
indexed by the unknown height,
which the engine resolves through one of three conventions,
the ground-plane assumption,
the shadow-tracking strategy,
or the screen-space hit test.
The math is the simplest non-trivial decoupling in the series,
a single new world dimension
producing a single new screen offset.
The next article in the cluster
swaps the camera orientation
from looking straight down at the world
to looking across the world horizontally,
which is the side-scrolling mode.

## References

- [Reference, Hyper Light Drifter][ref_hyper_light_drifter]
- [Reference, Projectile Motion][ref_projectile_motion]
- [Reference, Shadow][ref_shadow]
- [Reference, StarTropics][ref_startropics]
- [Reference, The Legend of Zelda][ref_zelda]
- [Reference, The Legend of Zelda, A Link to the Past][ref_link_to_the_past]
- [Reference, The Legend of Zelda, Link's Awakening][ref_links_awakening]

[ref_hyper_light_drifter]: https://en.wikipedia.org/wiki/Hyper_Light_Drifter
[ref_link_to_the_past]: https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past
[ref_links_awakening]: https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Link%27s_Awakening
[ref_projectile_motion]: https://en.wikipedia.org/wiki/Projectile_motion
[ref_shadow]: https://en.wikipedia.org/wiki/Shadow
[ref_startropics]: https://en.wikipedia.org/wiki/StarTropics
[ref_zelda]: https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)
