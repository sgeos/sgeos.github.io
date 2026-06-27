---
layout: post
mathjax: true
comments: true
title:  "Stylised and Hybrid Projections, the Inconsistent Frame"
date:   2026-04-29 09:00:00 +0000
categories: games graphics projection
---

<!-- A184 -->
<script>console.log("A184");</script>

The closing article of the affine-and-projective cluster
treats stylised and hybrid projections
that combine multiple projection modes
within a single game.
A game that uses a piecewise projection
applies one projection mode
in one part of the world or one game state
and a different projection mode
in another part.
The result is a visual inconsistency
that the player accepts
as a stylistic convention
even though the rendered scene
does not represent a single physical camera view.

The previous articles in the series
treated each projection mode in isolation
as if a game used only that mode.
Real games often combine modes.
A role-playing game
may render the overworld in a top-down view,
the towns in a top-down view at a higher zoom,
the battle scene in a side view,
and the menus as a flat overlay.
A platformer
may use a side-scrolling view for gameplay
and a top-down view for the world map.
A stylised independent release
may combine a side-scrolling projection
with atmospheric post-processing
that the projection math alone does not produce.

The article frames piecewise projection
as a forward map that depends
on the world region
or on the game state.
The Mother hybrid
where the ground renders in top-down view
and buildings render in side elevation
within the same scene
is the canonical example
of intra-scene inconsistency.
The Final Fantasy lineage
where the overworld, town, and battle
each render through their own projection
is the canonical example
of mode-based switching.
Asteroids and its successors
use a torus-wrap world topology
that makes the inverse map multi-valued
without changing the projection itself.
The modern stylised independent games
including Limbo and Inside
apply post-processing effects
to a side-scrolling projection
to produce a distinctive visual signature
beyond what the projection math contains.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a piecewise forward map
defined by region or by game state.
The delivery mechanism
chooses how the engine
switches between the pieces
and how the rendered output
combines into a single frame.

## A Brief History of the Mode

The earliest commercial use of hybrid projection
is debated.
[Asteroids][ref_asteroids]
from Atari in 1979
provided a flat-projection world
with a torus-wrap topology
that the player's ship exited at one edge
and reentered at the opposite edge.
The wrap was not strictly a hybrid projection
but a topology that the inverse map had to accommodate.
Pac-Man and other early arcade games
used similar wrap topologies
for the tunnel transitions
on the side of the maze.

[Final Fantasy][ref_final_fantasy_1]
from Square in 1987
on the Famicom and Nintendo Entertainment System
established the per-mode projection switching
that defined the Japanese role-playing game
across the late 1980s and 1990s.
The overworld used a top-down view
of a continent-scale map.
Towns used a top-down view at a closer zoom
with detailed tile graphics.
Dungeons used the same top-down view
in a constrained corridor format.
The battle scene used a side-view
with the player party on one side
and the enemy formation on the other side.
The menu and inventory used a flat overlay
that ignored the world geometry entirely.
Mode switches between gameplay scenes
transitioned the projection
through brief animations or scene fades
that hid the inconsistency from the player,
while the menu overlay
appeared instantly on button press
without an intervening transition.

[Mother][ref_mother_1]
from Ape and Pax Softnica in 1989 in Japan,
released internationally as EarthBound Beginnings in 2015,
introduced the intra-scene hybrid projection
that the series carried forward.
The overworld ground tiles rendered in a top-down view
but the buildings, trees, and obstacles
rendered in side-elevation view
as if the camera were looking horizontally
at the upright objects
while looking straight down at the ground.
The visual inconsistency
gave the Mother world
its distinctive flat-but-occupied feel
that subsequent Mother games inherited.

[EarthBound][ref_earthbound]
from Ape and HAL Laboratory in 1994 on the Super Nintendo Entertainment System
extended the Mother hybrid projection
into the sixteen-bit era
with richer tile graphics
and more visually complex buildings.
The hybrid projection remained
the visual signature of the Mother series
through the post-Famicom releases.

[Mother 3][ref_mother_3]
from HAL Laboratory and Brownie Brown in 2006 on the Game Boy Advance
continued the lineage
into the handheld portable era
with the same intra-scene hybrid projection
and a refined art style
that pushed the technique
toward an emotionally-resonant aesthetic
that the series became known for.

The modern stylised independent game
emerges with [Limbo][ref_limbo]
from Playdead in 2010 on the Xbox 360.
The side-scrolling puzzle-platformer
applies a monochrome silhouette aesthetic
with atmospheric depth-of-field
and particle effects
that distinguish the scene from a literal side view.
The projection math is the side-scrolling forward map of an earlier cluster article,
but the post-processing
produces a visual style
that the projection alone does not.

[Inside][ref_inside]
from Playdead in 2016 on Microsoft Windows
extended the Limbo formula
with three-dimensional rendering
projected through a side-scrolling camera
that produces visually two-and-a-half-dimensional gameplay.
The hybrid here is between
three-dimensional world geometry
and two-dimensional gameplay constraints,
which the article treats as a special case
of mode-based projection switching.

## The Forward Map

The world has a partition
into regions $R_1, R_2, \dots, R_n$
that the engine selects from
based on the world point's location
or on the current game state.
Each region $R_i$
carries its own projection forward map $F_i$
that the previous articles defined.
The piecewise forward map is

$$
F(\mathbf{p}_{\text{world}}) = F_{i(\mathbf{p}_{\text{world}})}(\mathbf{p}_{\text{world}}),
$$

where $i(\mathbf{p}_{\text{world}})$
identifies the region
that the world point falls into.
The function $i$
may depend on world coordinates,
on game state,
or on both.

The Mother hybrid
partitions the world by the vertical world coordinate $w_y$
in the $y$-down convention of the previous articles.
The ground plane at $w_y = w_y^{\text{ground}}$
uses the top-down forward map
of the first cluster article,

$$
F_{\text{ground}}(\mathbf{p}_{\text{world}}) = z\, (w_x - c_x,\ w_z - c_z) + \mathbf{o}.
$$

The objects above the ground at $w_y < w_y^{\text{ground}}$
use a hybrid map that combines
the top-down lateral and depth axes
with a side-elevation vertical extent
through the height-above-ground value $h = w_y^{\text{ground}} - w_y$,

$$
F_{\text{object}}(\mathbf{p}_{\text{world}}) = z\, (w_x - c_x,\ w_z - c_z) + \mathbf{o} - (0,\ z\, h).
$$

The forward map for objects
reproduces the decoupled-vertical-axis forward map
of an earlier cluster article.
The hybrid arises not from the equation
but from the artistic rendering convention
where the object sprites
depict the side-elevation view of the object
even though the world is otherwise rendered from above.
The viewer sees the building's walls,
windows, and roof,
while the ground underneath the building
is the same top-down tile texture
as elsewhere on the map.

The per-scene switching variant
partitions the world by game state $\sigma$
rather than by world coordinate.
The Final Fantasy overworld state
uses a top-down forward map at zoom $z_{\text{overworld}}$.
The town state
uses a top-down forward map at zoom $z_{\text{town}} > z_{\text{overworld}}$.
The battle state
uses a side-view forward map
with the world axes reassigned
to match the battle layout.
The menu state
uses a flat overlay
that the article treats as zero-zoom orthographic
where the world coordinates do not contribute to the screen position,

$$
F_{\text{menu}}(\mathbf{p}_{\text{world}}) = \mathbf{p}_{\text{screen}}^{\text{fixed}}.
$$

The forward map for the menu state
ignores the world position entirely
and uses a fixed screen position
that the menu layout designer chose.

The state-switching function
chooses among the four forward maps
based on the current game state,

$$
F(\mathbf{p}_{\text{world}}, \sigma) = \begin{cases}
F_{\text{overworld}}(\mathbf{p}_{\text{world}}) & \sigma = \text{overworld} \\
F_{\text{town}}(\mathbf{p}_{\text{world}}) & \sigma = \text{town} \\
F_{\text{battle}}(\mathbf{p}_{\text{world}}) & \sigma = \text{battle} \\
F_{\text{menu}}(\mathbf{p}_{\text{world}}) & \sigma = \text{menu}.
\end{cases}
$$

The transitions between states
typically run through a brief animation
that interpolates between the source and target projections
or simply masks the transition
with a fade or wipe.
The interpolating-transition variant
applies a time-dependent convex combination
of the source and target forward maps,

$$
F_{\text{transition}}(\mathbf{p}_{\text{world}},\ t) = (1 - \beta(t))\, F_{\text{from}}(\mathbf{p}_{\text{world}}) + \beta(t)\, F_{\text{to}}(\mathbf{p}_{\text{world}}),
$$

where $\beta(t) \in [0, 1]$
is the transition progress curve
that the engine animates from $0$ at the start to $1$ at the end.
A linear $\beta(t)$ produces a uniform-speed transition.
A smoothstep or sigmoid $\beta(t)$
produces ease-in and ease-out at the boundaries.
The interpolating variant
is rare in retro games
that prefer fade or wipe masking
but appears in modern releases
that emphasise visual continuity.

The torus-wrap topology
of Asteroids
applies a modulo operation
to the world coordinates
before the forward map,

$$
\mathbf{p}_{\text{world}}^{\text{eff}} = \mathbf{p}_{\text{world}} \bmod \mathbf{W}_{\text{world}},
$$

where $\mathbf{W}_{\text{world}} = (W_{\text{world}, x}, W_{\text{world}, z})$
is the world dimensions
along the two wrapping axes.
The forward map applies to the effective position,

$$
F(\mathbf{p}_{\text{world}}) = F_{\text{base}}(\mathbf{p}_{\text{world}}^{\text{eff}}).
$$

The base forward map $F_{\text{base}}$
is the floor-case top-down map
of the first cluster article
without modification.
The wrap topology affects only the world-coordinate input.

The stylised post-processing variant
of Limbo and Inside
applies a side-scrolling forward map of an earlier cluster article
followed by a post-rendering pass
that modifies the rendered image
through monochrome filtering,
depth-of-field blurring,
or particle compositing,

$$
\mathbf{I}_{\text{screen}} = P(F_{\text{side-scrolling}}(\mathbf{p}_{\text{world}})),
$$

where $P$ is the post-processing pipeline
that the engine applies after the projection
has placed pixels on the screen.
The post-processing
does not change the projection math
but contributes to the stylised visual identity
that the player associates with the game.

## The Inverse Map

The inverse map of a piecewise projection
is itself piecewise.
Given a screen pixel $\mathbf{p}_{\text{screen}}$,
the engine identifies which region
or game state
the click refers to
and applies the corresponding inverse,

$$
F^{-1}(\mathbf{p}_{\text{screen}}) = F_{i(\mathbf{p}_{\text{screen}})}^{-1}(\mathbf{p}_{\text{screen}}).
$$

The function $i(\mathbf{p}_{\text{screen}})$
that identifies the region from the screen pixel
is the dual of the world-region partition function.
For the Mother hybrid,
the engine knows whether each screen pixel
belongs to the ground or to a building sprite
from the per-sprite draw order
and the sprite's screen-space bounding rectangle.
Clicks on the ground tiles
use the top-down inverse.
Clicks on building sprites
use the building-sprite hit-test convention
of the decoupled-vertical-axis article.

For the per-scene switching variant,
the current game state $\sigma$
fully determines the inverse,

$$
F^{-1}(\mathbf{p}_{\text{screen}}, \sigma) = F_{\sigma}^{-1}(\mathbf{p}_{\text{screen}}).
$$

The engine knows the current state
and applies the appropriate inverse
without ambiguity.

The torus-wrap topology
makes the inverse multi-valued
when the visible world contains multiple wraps,

$$
F^{-1}_{\text{torus}}(\mathbf{p}_{\text{screen}}) = \{\mathbf{p}_{\text{world}}^{\text{base}} + (k_x \, W_{\text{world}, x},\ k_z \, W_{\text{world}, z}) : k_x, k_z \in \mathbb{Z}\},
$$

where $\mathbf{p}_{\text{world}}^{\text{base}}$
is the base inverse before wrap consideration
and $(k_x, k_z)$
runs over integer shift indices
that produce the equivalent wrapped positions.
The engine resolves the multi-valuedness
by choosing the closest wrap representative to the camera
or to the gameplay-relevant position.

The post-processing variant
does not affect the inverse map of the underlying projection.
The engine inverts the side-scrolling map
to recover the world position
and ignores the post-processing
when answering picking queries.

## A Worked Example

Consider an EarthBound-style Super Nintendo Entertainment System role-playing game
with the following parameters.
The screen is 256 pixels wide
and 224 pixels tall.
The zoom factor is $z = 16$ pixels per world tile,
giving 16-by-16-pixel ground tiles.
The screen-centre offset is $\mathbf{o} = (128, 112)$.
The camera position is $\mathbf{c} = (5, 5)$ world tiles.
The ground vertical world coordinate is $w_y^{\text{ground}} = 0$.

A ground tile at world position $\mathbf{p}_{\text{world}} = (5, 0, 5)$
projects through the top-down forward map to

$$
\mathbf{p}_{\text{screen}}^{\text{ground}} = 16 \cdot (5 - 5,\ 5 - 5) + (128, 112) = (128, 112).
$$

The tile renders at the screen centre.

A building anchored at world position $\mathbf{p}_{\text{world}} = (5, 0, 6)$
with height $h_{\text{building}} = 3$ world tiles
has its base at the screen position

$$
\mathbf{p}_{\text{screen}}^{\text{base}} = 16 \cdot (5 - 5,\ 6 - 5) + (128, 112) = (128, 128).
$$

The building sprite
extends upward on the screen
from the base by $z \cdot h_{\text{building}} = 16 \cdot 3 = 48$ pixels.
The building top edge appears at

$$
\mathbf{p}_{\text{screen}}^{\text{top}} = (128, 128) - (0, 48) = (128, 80).
$$

The building sprite extends from screen $(128, 80)$ at the top
to $(128, 128)$ at the base.
The Mother-style art renders the building
as a side-elevation view of the structure
within this screen-space extent.

A click at screen pixel $(128, 100)$
falls inside the building sprite's vertical extent.
The inverse map identifies the click
as a building-sprite hit
through the per-sprite bounding rectangle
of the building.
The local height of the click above the ground
follows from the screen-y position
relative to the building base,

$$
h_{\text{local}}(100) = \frac{128 - 100}{16} = 1.75 \text{ world tiles}.
$$

The recovered world coordinates
combine the building's ground anchor position
with the local height,

$$
\mathbf{p}_{\text{world}}^{\text{building-hit}} = (5,\ -1.75,\ 6).
$$

The negative vertical world coordinate
indicates a position above the ground
in the $y$-down convention
where the ground sits at $w_y^{\text{ground}} = 0$.

A click at screen pixel $(140, 130)$
falls below the building sprite
on a ground tile.
The inverse map identifies the click as a ground-tile hit
and applies the top-down inverse,

$$
\mathbf{p}_{\text{world}}^{\text{ground-hit}} = \frac{1}{16}\, (140 - 128,\ 130 - 112) + (5, 5) = (5.75,\ 6.125).
$$

The click corresponds to a position
slightly to the right and slightly forward
of the building's base.

A transition to battle mode
switches the projection state
from overworld to battle.
The battle screen uses a side-view forward map
with the party on the right
and the enemies on the left.
The world coordinates of the overworld
do not carry into the battle scene.
The battle scene
uses its own world frame
with the party and enemies
positioned along the battle's lateral axis.

The round-trip identity
holds within each region or state,

$$
F^{-1}_{\sigma}(F_{\sigma}(\mathbf{p}_{\text{world}})) = \mathbf{p}_{\text{world}} + O(\varepsilon),
$$

where $\sigma$ is the active state or region
and $\varepsilon$ is the floating-point precision of the engine.
The round-trip does not hold across regions or states.

## Variations Within the Mode

The piecewise projection framework
admits several variations
that engines have explored.

A spatial-partition variant
divides the world by world-coordinate region.
The Mother ground-and-building hybrid
is the canonical case.
A multi-storey building
might use one projection
for ground-level floors
and a different projection
for an upper floor's interior view.

A state-based variant
divides the projection by game state
without considering world coordinates.
The Final Fantasy mode-switching
is the canonical case.
A modern role-playing game
might have an exploration mode,
a combat mode,
a cutscene mode,
and a menu mode
each with its own projection.

A topological-wrap variant
applies modulo arithmetic
to the world coordinates
to create a wrapping world topology.
Asteroids and Pac-Man both use topological wrap.
The single-axis wrap
of Pac-Man's tunnel transitions
is mathematically simpler
than Asteroids' two-axis torus
but otherwise follows the same framework.

A post-processing variant
applies effects to the rendered image
after the projection
to produce a stylised visual identity.
Limbo and Inside both use post-processing variants.
The variant does not affect the projection math
but contributes to the visual style
that the player associates with the game.

A multi-projection-layer variant
renders the same world position
through multiple projections simultaneously,
combining the results into a single screen image.
A game might render the gameplay world through one projection
and overlay a minimap that shows the same world
through a different projection.
The combination is hybrid
even though each layer is consistent.

A cinematic-camera variant
switches the projection
during scripted cutscenes
to produce camera angles
that the gameplay projection cannot achieve.
A top-down strategy game
might switch to a cinematic third-person view
during cutscenes,
then return to top-down for gameplay.

A user-selectable projection variant
permits the player or the engine
to choose between projection modes
based on player preference
or based on accessibility settings.
The variant is rare in older games
and increasingly common in modern releases.

## Delivery Mechanisms

The piecewise projection
permits five distinct delivery mechanisms
on period hardware.

The first is multiple sprite layers
with different projection conventions
within a single hardware rendering pipeline.
The Mother games on the Nintendo Entertainment System
used the standard PPU sprite hardware
for both ground tiles and building sprites,
relying on artistic convention
to produce the hybrid visual style
rather than on different rendering paths.

The second is mode-switched rendering pipelines.
The Final Fantasy games on the Famicom and Nintendo Entertainment System
ran different rendering code paths
for the overworld, town, dungeon, battle, and menu modes.
The mode transitions
triggered the rendering pipeline change
at well-defined game-state boundaries.

The third is world-coordinate wrap arithmetic
in the gameplay simulation.
Asteroids on the Atari arcade hardware
performed the modulo operation
in the gameplay code
before the rendering pipeline
applied the standard top-down projection.
The wrap arithmetic
ran on the central processing unit
without requiring special graphics hardware support.

The fourth is post-processing image filters
applied after the projection-based rendering.
Limbo and Inside on the modern personal computer
apply the monochrome filter and depth-of-field
through graphics-processing-unit shaders
that run after the side-scrolling projection
has placed the pixels.
The mechanism trades the additional shader passes
for the distinctive visual identity.

The fifth is shader-based per-fragment projection variation
on modern hardware.
A modern engine
can implement a piecewise projection
through a fragment shader
that selects the projection map
based on the fragment's world coordinates
or the current game state.
The mechanism gives the engine
fine-grained control
over the projection per screen pixel.

All five mechanisms
support the piecewise projection abstraction.
The choice trades hardware requirements,
the implementation complexity of mode transitions,
and the achievable visual style.

## Where the Framing Breaks Down

The piecewise projection framing
is insufficient
when any of the following conditions hold.

When the game expects the player to read
a consistent three-dimensional world geometry
from the rendered scene,
the inconsistency of a piecewise projection
disrupts the spatial intuition.
The Mother hybrid works
because the player accepts the convention
that the ground is top-down
and the buildings are side-elevation
as a stylistic choice.
A game that needed accurate spatial reasoning
could not use the same hybrid.

When the gameplay requires
unique inverse mapping for picking,
the topological-wrap variant introduces ambiguity
that the engine must resolve through additional logic.
The torus-wrap inverse
returns an infinite candidate set
that the engine must reduce
to a single relevant world position.

When the gameplay physics
require a consistent world frame
for collision detection
and motion simulation,
the per-scene switching variant
introduces seams between scenes
that the engine must handle
through scene-transition logic.
The seams are usually invisible to the player
because the transitions are scripted.

When the visual style
must be consistent across all scenes
for narrative or thematic reasons,
the mode-switching variant
disrupts the consistency.
A game that wanted a uniformly grim visual style
through all gameplay scenes
could not switch projections freely.

When the rendering must scale
to support arbitrary new modes
without engine modification,
the static piecewise projection
of the article is insufficient.
A modern engine
might use a data-driven projection system
where new modes can be added
through configuration
without code changes.

## The Canon

The following games
use piecewise or stylised projections
as defining visual features.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Asteroids][ref_asteroids]
in the arcade in 1979
gave the medium
its first commercially-released torus-wrap world topology.
The flat-projection space
with edges that wrapped to opposite edges
became the visual template
for several arcade space-shooter contemporaries.

[Final Fantasy][ref_final_fantasy_1]
on the Famicom and Nintendo Entertainment System in 1987
established the per-mode projection switching
between overworld, town, dungeon, battle, and menu modes
that the Japanese role-playing game subgenre inherited.

[Mother][ref_mother_1]
on the Famicom in 1989
introduced the intra-scene hybrid projection
where ground tiles render in top-down view
and buildings render in side elevation.
The international release as EarthBound Beginnings in 2015
brought the original Famicom title
to a wider audience.

[EarthBound][ref_earthbound]
on the Super Nintendo Entertainment System in 1994
extended the Mother hybrid projection
into the sixteen-bit era
and became the most widely-played Mother-series game
in the West through its post-release cult following.

[Mother 3][ref_mother_3]
on the Game Boy Advance in 2006
continued the hybrid projection lineage
into the handheld portable era.

[Limbo][ref_limbo]
on the Xbox 360 in 2010
established the modern stylised side-scrolling
through a monochrome silhouette aesthetic
with atmospheric post-processing.

[Inside][ref_inside]
on Microsoft Windows in 2016
extended the Limbo formula
with three-dimensional rendering
projected through a side-scrolling camera.

Each game in the canon
combines projection math
with a stylistic convention
that the player accepts
even though the rendered scene
does not represent a single physical camera view.

## Out of Scope

The article does not cover
the following.

True three-dimensional rendering
with arbitrary camera placement
through a graphics-processing-unit pipeline
is the modern technique
that the synthesis closer of the series treats.
The piecewise projections of this article
are stylised choices
within the affine and projective projection families
that the cluster has covered.

The full Y-sort framework
and the full pick-disambiguation framework
are the subjects of the following cross-cutting articles.
The article presents picking
in its simplest piecewise form
and defers the full treatment.

The internal architecture of state transitions
between game modes
including save state management,
asset loading,
and gameplay state preservation
is gameplay-systems territory
adjacent to but distinct from
the projection math.

The choice of when to apply a piecewise projection
versus when to use a consistent projection
is a design question
that the series does not adjudicate.
Each visual style has games
for which it is the right choice
and games for which it is the wrong choice.

The shader programming techniques
that modern engines use
for post-processing effects
are implementation concerns
that the article treats only at the level
of the delivery-mechanism sidebar.

## Conclusion

Stylised and hybrid projections
combine multiple projection modes
within a single game
to produce a visual identity
that no single mode achieves alone.
The piecewise forward map
$F(\mathbf{p}_{\text{world}}) = F_{i(\mathbf{p}_{\text{world}})}(\mathbf{p}_{\text{world}})$
applies different projection modes
to different regions of the world
or different game states.
The Mother hybrid
where the ground renders in top-down view
and buildings render in side elevation
is the canonical example
of intra-scene inconsistency.
The Final Fantasy lineage
where the overworld, town, and battle each render through their own projection
is the canonical example
of mode-based switching.
Asteroids and its successors
use a torus-wrap world topology
that makes the inverse map multi-valued.
The modern stylised independent games
including Limbo and Inside
apply post-processing effects
to a side-scrolling projection
to produce a distinctive visual signature.
The article closes the affine-and-projective cluster
with the recognition that real games
mix projection modes freely
in service of artistic and gameplay goals.
The remaining articles in the series
treat cross-cutting concerns
that span the projection modes
of the previous clusters,
beginning with draw-order management
and the Y-sort algorithm
in the next article.

## References

- [Reference, Asteroids][ref_asteroids]
- [Reference, EarthBound][ref_earthbound]
- [Reference, Final Fantasy][ref_final_fantasy_1]
- [Reference, Inside][ref_inside]
- [Reference, Limbo][ref_limbo]
- [Reference, Mother][ref_mother_1]
- [Reference, Mother 3][ref_mother_3]

[ref_asteroids]: https://en.wikipedia.org/wiki/Asteroids_(video_game)
[ref_earthbound]: https://en.wikipedia.org/wiki/EarthBound
[ref_final_fantasy_1]: https://en.wikipedia.org/wiki/Final_Fantasy_(video_game)
[ref_inside]: https://en.wikipedia.org/wiki/Inside_(video_game)
[ref_limbo]: https://en.wikipedia.org/wiki/Limbo_(video_game)
[ref_mother_1]: https://en.wikipedia.org/wiki/EarthBound_Beginnings
[ref_mother_3]: https://en.wikipedia.org/wiki/Mother_3
