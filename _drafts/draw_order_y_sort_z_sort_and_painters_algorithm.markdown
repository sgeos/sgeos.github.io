---
layout: post
mathjax: true
comments: true
title:  "Draw Order, Y-Sort, Z-Sort, and the Painter's Algorithm"
date:   2026-04-30 09:00:00 +0000
categories: games graphics projection
---

<!-- A185 -->
<script>console.log("A185");</script>

The first article of the cross-cutting cluster
treats draw order management
across the projection modes
that the previous clusters covered.
Draw order matters
whenever two world objects
project to overlapping screen regions.
The renderer must decide
which object appears in front
and which appears behind.
A wrong decision
produces a wall in front of the character
when the character should be in front of the wall,
a treetop behind a building
when the building should occlude the tree,
or a flickering ordering
that flips between adjacent frames.

The article treats four related techniques.
The painter's algorithm
provides the general framework
of back-to-front sorting
that every two-dimensional renderer applies.
Y-sort uses the screen-y position of each object's anchor
as the sort key.
Z-sort uses the world depth coordinate
as the sort key.
The hybrid Y-then-Z sort
combines the two
for projection modes where neither alone
produces a fully-correct order.

The previous articles in the series
introduced Y-sort
in the belt-scroll,
oblique,
and axonometric articles
through the operational comparison
on the ground-projection screen-y.
The article here
treats the full framework,
including tie-breaking rules,
the Z-sort alternative,
floating-point conditioning,
and the hybrid sort
that production engines use.
The pass-through bug
that classic top-down role-playing games sometimes exhibit
is the article's running case study
of what goes wrong
when Y-sort is misapplied.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a sort criterion
that the engine applies to a list of renderable objects.
The delivery mechanism
chooses the sort algorithm
and the data structure
that the engine uses
to maintain the sorted order
across frames.

## A Brief History of Draw Order

The painter's algorithm
appears in computer graphics literature
in Newell, Newell, and Sancha's 1972 paper
on hidden-surface removal
for three-dimensional polygon rendering.
The technique
sorts polygons by their depth from the camera
and renders them in back-to-front order,
relying on the later-rendered polygons
to overwrite the earlier-rendered ones
in the frame buffer.

The two-dimensional game adoption
of the painter's algorithm
emerges with the multi-sprite scenes
of the late 1970s and early 1980s arcade games.
The Nintendo Entertainment System sprite hardware
maintained a 64-entry object attribute memory
that the engine wrote in the desired draw order,
with lower-index sprites rendered in front of higher-index ones.
Console sprite hardware of the era
provided per-sprite priority bits or layer fields
that the engine wrote per frame
to control the visual front-to-back layering.

The Y-sort technique
emerges with the isometric and oblique-projected games
of the late 1980s and the 1990s.
Knight Lore in 1984
used Y-sort
for the small isometric rooms
that the player navigated.
The Y-sort convention
became universal in axonometric role-playing games
through the 1990s
including [Diablo II][ref_diablo_2]
from Blizzard in 2000
which is widely cited as the canonical Y-sort case
in the game-development tradition.

The Z-sort alternative
emerges in the same era
as the natural choice
for games that track an explicit world depth coordinate
for each object.
Tactical role-playing games
with discrete height tiers
including [Disgaea, Hour of Darkness][ref_disgaea]
from Nippon Ichi Software in 2003
use Z-sort
to layer characters and obstacles
across the multi-level battlefield.

The hybrid Y-then-Z sort
emerges in production engines
that need to handle both ground-aligned objects
and stacked-height objects
in the same scene.
The combination
catches cases that either sort alone
fails to resolve correctly.

The pass-through bug
that classic top-down role-playing and adventure games sometimes exhibit
is documented in many period titles
where an NPC sprite
appears to overlap the wrong side of a wall sprite
due to a sort-key misconfiguration.
The bug
is the canonical Y-sort failure case
in the engineering tradition.

The modern era
uses graphics-processing-unit depth buffers
that displace the painter's algorithm
for true three-dimensional rendering.
The two-dimensional game
continues to use Y-sort and its variants
because the depth buffer requires per-pixel depth values
that two-dimensional sprites do not naturally provide.

## The Painter's Algorithm

The painter's algorithm
sorts a list of renderable objects
by a per-object sort key $k_i$
and renders them in decreasing order of $k_i$.
The first-rendered object
sits at the back of the scene
and the last-rendered object
sits at the front.
Each subsequent render
overwrites the frame buffer
at the pixels where the new object covers existing content,
giving the last-rendered objects
visual priority over the earlier ones.

The sort criterion is the comparison

$$
\text{draw } i \text{ before } j \iff k_i > k_j.
$$

The sort key $k_i$
encodes the back-to-front depth
that the projection mode produces.
For top-down projection,
the natural sort key
is the world-y coordinate
or equivalently the screen-y of the ground anchor.
For belt-scroll, oblique, and axonometric projection,
the sort key is the ground-projection screen-y
that the cluster articles introduced.
For sprite scaling,
the sort key is the world depth from the camera.

The algorithmic complexity
is dominated by the sort.
A comparison-based sort runs in $O(n \log n)$ time
for $n$ visible objects.
The rendering pass runs in $O(n)$ time
plus the per-pixel cost of drawing each sprite.
The total per-frame cost is

$$
T_{\text{painter}}(n) = O(n \log n) + O\left( \sum_{i=1}^{n} A_i \right),
$$

where $A_i$ is the screen-space area of object $i$.

The painter's algorithm assumes
that the sort key is well-defined for each object
and that the sorted order
produces a correct visible result.
The assumption fails
when two objects' sort keys are equal
or when the sort key
does not correctly capture the depth relationship
between objects with overlapping screen extents.
The tie-breaking and conditioning rules
of the following sections
address these failures.

## The Y-Sort Criterion

The Y-sort criterion
uses each object's anchor screen-y
as the primary sort key,

$$
k_i^{\, Y} = s_{y, i}^{\text{anchor}}.
$$

The comparison
selects the smaller anchor screen-y
for earlier rendering,

$$
\text{draw } i \text{ before } j \iff s_{y, i}^{\text{anchor}} < s_{y, j}^{\text{anchor}}.
$$

For ground-aligned objects in any of the projection modes
of the previous clusters,
the smaller anchor screen-y
corresponds to a position
further back in the world from the camera.
The Y-sort criterion produces the correct back-to-front rendering order.

The anchor convention
matters for Y-sort correctness.
The canonical convention
places the anchor at the object's foot
or at the bottom-centre of the sprite,
which is the world position
where the object touches the ground.
Two characters
whose feet are at different world positions
sort correctly by foot-anchor screen-y.

When two objects have equal anchor screen-y,
the primary Y-sort criterion is ambiguous.
The engine selects a tie-breaker
from several common choices.

The first tie-breaker
uses the world depth coordinate $w_z$
of each object,

$$
\text{draw } i \text{ before } j \text{ when tied} \iff w_{z, i} > w_{z, j}.
$$

The deeper object
draws first.
The Y-then-Z hybrid sort below
formalises this tie-breaker.

The second tie-breaker
uses the object's creation order
through a stable sort algorithm,

$$
\text{draw } i \text{ before } j \text{ when tied} \iff t_{\text{created}, i} < t_{\text{created}, j}.
$$

The older object
draws first.
The stable-sort approach
prevents flicker between frames
because the order does not change
unless the gameplay state changes.

The third tie-breaker
uses a unique object identifier,

$$
\text{draw } i \text{ before } j \text{ when tied} \iff \text{id}(i) < \text{id}(j).
$$

The identifier provides a deterministic order
that does not depend on gameplay state.
The convention is rare in practice
because the order does not correspond to any meaningful spatial relationship.

The pass-through bug
arises when the Y-sort anchor convention
does not match the visual occlusion expectation.
A wall sprite anchored at its base
and a character sprite anchored at its feet
sort correctly when the character is in front of the wall.
The bug appears
when the character's feet anchor screen-y
exceeds the wall's base anchor screen-y
by a small amount
that does not match the visual depth relationship.
The character renders on top of the wall
because of the Y-sort criterion,
giving the visual impression
of walking through the wall.
The fix
either changes the wall's anchor convention
or adds a secondary sort key
that distinguishes the wall from the character explicitly.

## The Z-Sort Criterion

The Z-sort criterion
uses the world depth coordinate
as the sort key directly,

$$
k_i^{\, Z} = w_{z, i}.
$$

The comparison
selects the larger world depth
for earlier rendering,

$$
\text{draw } i \text{ before } j \iff w_{z, i} > w_{z, j}.
$$

The criterion is more direct than Y-sort
because the world depth
does not depend on the projection.
A change of projection mode
does not change the world depth coordinate
of the object.

The criterion requires that the engine
track each object's world depth
in addition to its world position.
For projection modes
where the world depth is one of the world coordinates,
the requirement is automatic.
For projection modes
where the depth is computed from the world coordinates
through the projection matrix,
the engine computes the depth value once per object per frame.

Floating-point conditioning
becomes a concern when two objects
have nearly equal world depths.
The comparison

$$
w_{z, i} > w_{z, j}
$$

can flip between adjacent frames
if the depth difference is smaller than the floating-point precision $\varepsilon$,

$$
|w_{z, i} - w_{z, j}| < \varepsilon.
$$

The flip produces visible flicker
where the rendered order changes between frames
even though the world configuration is approximately stable.

The conditioning fix
uses an epsilon-tolerance comparison
that treats nearly-equal depths
as tied
and falls back to a secondary criterion,

$$
\text{draw } i \text{ before } j \iff
\begin{cases}
w_{z, i} > w_{z, j} & \text{if } |w_{z, i} - w_{z, j}| \geq \varepsilon \\
\text{secondary criterion} & \text{otherwise}.
\end{cases}
$$

A typical secondary criterion
uses the object identifier or the creation order
to break the near-tie deterministically.
A quantised-depth alternative
rounds the world depth values
to a fixed-point grid
that eliminates the near-tie cases entirely,

$$
\hat{w}_{z, i} = \mathrm{round}(w_{z, i} / \Delta) \cdot \Delta,
$$

where $\Delta$ is the quantisation step.
The quantisation
introduces a maximum sort-key error of $\Delta/2$
in exchange for stable cross-frame ordering.

## The Hybrid Y-Then-Z Sort

The hybrid Y-then-Z sort
combines the Y-sort and Z-sort criteria
through a case-based comparison
that uses the anchor screen-y as the primary key in increasing order
and the world depth as the secondary key in decreasing order,

$$
\text{draw } i \text{ before } j \iff
\begin{cases}
s_{y, i}^{\text{anchor}} < s_{y, j}^{\text{anchor}} & \text{if not tied on } Y \\
w_{z, i} > w_{z, j} & \text{if tied on } Y \text{ and not tied on } Z \\
\text{tertiary criterion} & \text{if tied on both}.
\end{cases}
$$

The tertiary criterion
typically uses object identifier or creation order
to break the doubly-tied case.

The hybrid sort
handles both the canonical Y-sort cases
where objects are spread across the ground plane
and the stacked-height cases
where objects share the same ground anchor
but have different vertical positions.
The hybrid is the production-engine default
in two-dimensional games
that combine ground characters with airborne projectiles
or stacked vertical structures.

The Disgaea series
uses a variant of the hybrid sort
where the primary key is the Z-axis layer
that the tactical battlefield assigns
and the secondary key is the Y position
within the layer.
The variant inverts the Y-then-Z order
to layer-by-layer rendering
that matches the discrete-height tactical map.

## A Worked Example

Consider a Diablo-II-style axonometric action role-playing game
with the following parameters.
The screen is 800 pixels wide and 600 pixels tall.
The forward map uses game-iso
with zoom factor $z = 32$
and screen offset $\mathbf{o} = (400, 300)$.
The camera position is $\mathbf{c} = (0, 0, 0)$.
The forward-map matrix is

$$
M = \begin{bmatrix} 32 & 0 & -32 \\ 16 & 32 & 16 \end{bmatrix}.
$$

Three world objects populate the scene
on the ground plane at $w_y = 0$.
The first is a tree
at world position $(5, 0, 3)$.
The second is a sign
at world position $(4, 0, 4)$.
The third is the player character
at world position $(6, 0, 5)$.

The anchor screen positions follow
from applying $M$ to each world position.

The tree projects to

$$
\mathbf{p}_{\text{screen}}^{\text{tree}} = (32 \cdot 5 - 32 \cdot 3,\ 16 \cdot 5 + 0 + 16 \cdot 3) + (400, 300) = (64, 128) + (400, 300) = (464, 428).
$$

The sign projects to

$$
\mathbf{p}_{\text{screen}}^{\text{sign}} = (32 \cdot 4 - 32 \cdot 4,\ 16 \cdot 4 + 0 + 16 \cdot 4) + (400, 300) = (0, 128) + (400, 300) = (400, 428).
$$

The player projects to

$$
\mathbf{p}_{\text{screen}}^{\text{player}} = (32 \cdot 6 - 32 \cdot 5,\ 16 \cdot 6 + 0 + 16 \cdot 5) + (400, 300) = (32, 176) + (400, 300) = (432, 476).
$$

The Y-sort criterion
applied to the three anchor screen-y values gives

$$
\big( s_y^{\text{tree}},\ s_y^{\text{sign}},\ s_y^{\text{player}} \big) = (428,\ 428,\ 476).
$$

The tree and the sign tie at $s_y = 428$.
The player has $s_y = 476$
and renders after both tied objects.

The tie-break on world depth $w_z$ gives
$w_z^{\text{tree}} = 3$ and $w_z^{\text{sign}} = 4$.
The sign has the larger depth
and renders before the tree
under the Z-sort criterion
that draws larger-depth objects first.

The hybrid Y-then-Z sort
produces the draw order

$$
\text{sign} \to \text{tree} \to \text{player}.
$$

The sign renders first at the back.
The tree renders second over any sign pixels it overlaps.
The player renders last at the front
on top of any sign or tree pixels it overlaps.

A flying projectile
above the player at world position $(6, -2, 5)$
shares the player's lateral and depth coordinates
but has $w_y = -2$
indicating a position two world tiles above the ground.
The projectile's anchor screen position is

$$
\mathbf{p}_{\text{screen}}^{\text{projectile}} = (32 \cdot 6 - 32 \cdot 5,\ 16 \cdot 6 + 32 \cdot (-2) + 16 \cdot 5) + (400, 300) = (32, 112) + (400, 300) = (432, 412).
$$

The projectile renders at screen $(432, 412)$,
64 pixels above the player's screen anchor.
The Y-sort criterion
produces the projectile's anchor screen-y as 412,
smaller than the player's 476.
The projectile would render before the player
and appear behind it
under the Y-sort criterion alone.

The hybrid Y-then-Z sort
fixes this case
by using the player's shadow screen-y
or by including the world height $w_y$ in the sort key.
A Y-sort variant
that uses the shadow screen-y
sets the projectile's effective Y-sort key
to the screen-y of its ground projection,

$$
s_y^{\text{projectile, shadow}} = 16 \cdot 6 + 0 + 16 \cdot 5 + 300 = 476.
$$

The projectile's shadow Y-sort key
matches the player's anchor Y-sort key,
and the Z-sort tie-breaker
distinguishes them
through the world $w_y$ comparison.

The round-trip identity
of the sort
is that the sort order is stable
across frames
when the world configuration is stable,

$$
\sigma_{n}(\{k_i\}_{i=1}^{n}) = \sigma_{n+1}(\{k_i\}_{i=1}^{n}) \text{ when } k_i \text{ unchanged},
$$

where $\sigma_n$ is the sorted order at frame $n$.
The stable-sort guarantee
prevents cross-frame flicker
when the gameplay state has not changed
the sort keys
between adjacent frames.

## Variations Within the Mode

The draw-order framework
admits several variations
that engines have explored.

A static-priority variant
assigns each object a fixed priority value
that does not change with the object's world position.
Background objects use low priority
and foreground objects use high priority.
The variant is mathematically the simplest
and works well for games
where each object has a clear front-or-back role
that the gameplay does not change.

A layered-sort variant
divides objects into discrete layers
and sorts within each layer independently.
The layers render bottom-to-top.
The criterion is a case-based comparison
on the layer index $\ell_i$ as the primary key
and the within-layer criterion as the secondary key,

$$
\text{draw } i \text{ before } j \iff
\begin{cases}
\ell_i < \ell_j & \text{if } \ell_i \neq \ell_j \\
\text{within-layer criterion}(i, j) & \text{if } \ell_i = \ell_j.
\end{cases}
$$

The within-layer criterion
is typically Y-sort, Z-sort, or the hybrid Y-then-Z sort.
The variant is common in tile-based games
where background tiles, mid-ground objects, sprites, and overlays
each form a layer.
The layers do not interact across boundaries.

A camera-projected-depth variant
uses the camera-frame depth
of each object
as the sort key,

$$
k_i = (R\, \mathbf{p}_{\text{world}, i})_z,
$$

where $R$ is the camera rotation matrix.
The variant generalises Z-sort
to projection modes
where the world depth axis
is not directly $w_z$.

A bounding-box-overlap-resolving variant
detects pairs of objects
whose screen-space bounding boxes overlap
and applies the sort criterion only to overlapping pairs.
The variant
reduces the cost of unnecessary sort comparisons
in scenes with many widely-separated objects.

A topological-sort variant
allows the engine to declare
explicit ordering relationships between specific object pairs.
The engine performs a topological sort
of the resulting directed acyclic graph.
The variant
handles cases
where neither Y-sort, Z-sort, nor the hybrid
captures the correct order.

A hand-authored-order variant
permits the level designer
to manually specify the draw order
for each scene.
The variant is common in cinematic scenes
where the designer's artistic intent
overrides any algorithmic sort.

A depth-buffer alternative
replaces the per-object sort
with per-pixel depth comparison.
The graphics processing unit
maintains a depth buffer
that stores the closest depth value
at each screen pixel,

$$
\text{paint pixel} \iff d_{\text{new}} < d_{\text{stored}}.
$$

The depth buffer
removes the need for a per-object sort
and handles per-pixel occlusion correctly
including the cases
where two objects' screen rectangles intersect.
Modern two-and-three-dimensional engines
use the depth buffer when graphics processing unit support permits.

## Delivery Mechanisms

The draw-order management
permits five distinct delivery mechanisms
on period hardware.

The first is hardware sprite priority bits
on console picture-processing-unit hardware.
The Nintendo Entertainment System sprite list
included a per-sprite priority bit
that placed each sprite in front of or behind the background.
The Super Nintendo Entertainment System
extended this to four priority levels.
The Sega Genesis sprite list
used per-sprite link fields
that determined the rendering order.
The mechanism
provided hardware-supported draw order
at the cost of limited sprite count and limited priority levels.

The second is per-frame engine-software sort
on a general-purpose central processing unit.
The engine maintains a list of visible objects
and sorts them
once per frame
through a software sort algorithm
that the engine chooses.
The mechanism scales with the central-processing-unit budget
and is the dominant delivery
on the personal computer
and on modern console hardware
that exposes a general-purpose programming model.

The third is incremental sort maintenance
through a stable insertion-sorted list
that the engine updates
as objects move.
The variant exploits the temporal coherence
of object positions
across adjacent frames.
The sort cost amortises
to $O(n)$ per frame
when most objects do not change relative position.
The variant is rare in retro games
but common in modern engines.

The fourth is graphics-processing-unit shader sort
through compute shaders
that perform parallel sort algorithms
across the visible object list.
The variant trades programming complexity
for the parallel throughput
of modern graphics processing units.
The variant is dominant in modern engines
that use shader-based pipelines.

The fifth is depth-buffer-based per-pixel resolution
that the previous section described.
The depth buffer
displaces the sort
for projection modes
where per-object sorting is insufficient.

All five mechanisms
implement back-to-front rendering
with different trade-offs.
The choice trades hardware requirements,
implementation complexity,
the maximum supported object count,
the depth-buffer memory budget,
and the achievable frame rate.

## Where the Framing Breaks Down

The painter's algorithm and its sort criteria
are insufficient
when any of the following conditions hold.

When the visible scene contains
two objects whose screen rectangles intersect
such that each contains some pixels
in front of the other,
no per-object sort can produce a correct rendering.
The classic case
is two crossing rectangles in three dimensions
where one half is in front of the other
and the other half is behind.
The depth-buffer alternative resolves the case correctly.

When the scene contains transparent objects
that should partially blend with the background,
the painter's algorithm
must render the transparent objects
after the opaque background
in a separate pass.
The depth-buffer alternative
handles the case
through careful sort and blending rules
that the article does not treat in detail.

When the scene contains shadows
that two objects cast on each other,
the sort criterion
must respect both the object's depth from the camera
and the shadow's projection onto the receiving surface.
Period games typically simplified the shadow rendering
to avoid the complexity.

When the camera moves rapidly between frames,
the temporal coherence
that incremental sort maintenance relies on
breaks down.
The engine must fall back to a full sort
that the variant cost saves only during periods of camera stability.

When the gameplay introduces new sort-affecting objects
mid-frame,
the sort
must update before the rendering pass
to include the new objects.
The engine must handle the synchronisation
between gameplay state updates and the sort.

## The Canon

The following games
use specific draw-order techniques
that distinguish their visual style
or that became canonical for the subgenre.

[Diablo II][ref_diablo_2]
on Microsoft Windows in 2000
uses Y-sort
as the canonical axonometric action-role-playing-game convention.
The Diablo II sprite stack
includes the player character,
multiple monster sprites,
projectile effects,
and environmental objects
all sorted by ground-anchor screen-y per frame.

[Disgaea, Hour of Darkness][ref_disgaea]
on the PlayStation 2 in 2003
uses Z-sort
on the discrete-height tactical battlefield
where characters and obstacles occupy explicit elevation tiers.
The discrete-Z layered sort
is a special case of the Z-sort criterion
that suits the tactical-grid gameplay.

Classic top-down role-playing and adventure games
of the Famicom and Super Nintendo Entertainment System era
exhibited the pass-through bug
at corner cases of the Y-sort criterion.
The bugs
are the canonical illustrations
of what goes wrong
when the anchor convention
or the tie-breaker
is insufficient.

Each game in the canon
exercises a specific draw-order technique
and reveals
the trade-offs
that the projection mode
and the gameplay requirements
impose on the engine.

## Out of Scope

The article does not cover
the following.

The full painter's algorithm
for three-dimensional polygon rendering
including the polygon-clipping cases
that the original Newell paper introduced
is outside the article's two-dimensional scope.
The graphics-processing-unit depth-buffer
displaces the polygon-painter's algorithm
on modern hardware.

The full pick-disambiguation framework
that builds on the draw order
to identify the clicked object
is the subject of the next cross-cutting article.
The article presents draw order
without the corresponding picking treatment.

True three-dimensional rendering
with arbitrary camera placement
and per-pixel depth resolution
is the subject of the synthesis closer of the series.
The painter's algorithm is the two-dimensional approximation
that pre-Z-buffer hardware required.

The internal data structures
that production engines use
for incremental sort maintenance
are implementation details
that the article treats only at the level
of the delivery-mechanism sidebar.

The shader programming techniques
for parallel sort on the graphics processing unit
are implementation details
adjacent to but distinct from
the sort criterion math.

## Conclusion

Draw order management
is a cross-cutting concern
that the projection-mode articles
each touched briefly through their Y-sort sections.
The article gathers the full framework here.
The painter's algorithm
sorts a list of renderable objects
by a depth-related sort key
and renders them in back-to-front order.
Y-sort uses the anchor screen-y as the sort key.
Z-sort uses the world depth coordinate.
The hybrid Y-then-Z sort
combines the two
through a lexicographic comparison
that handles both ground-aligned and stacked-height cases.
Floating-point conditioning
prevents cross-frame flicker
through epsilon tolerance or depth quantisation.
The depth-buffer alternative
displaces the per-object sort
on hardware that supports per-pixel depth resolution.
Production engines
typically use the hybrid sort
for retro-style two-dimensional games
and the depth buffer
for three-dimensional and two-and-a-half-dimensional games.
The next article in the series
treats the cross-cutting picking framework
that uses the draw-order structure
to identify the clicked object.

## References

- [Reference, Diablo II][ref_diablo_2]
- [Reference, Disgaea, Hour of Darkness][ref_disgaea]
- [Reference, Painter's Algorithm][ref_painters_algorithm]
- [Reference, Z-Buffering][ref_z_buffering]

[ref_diablo_2]: https://en.wikipedia.org/wiki/Diablo_II
[ref_disgaea]: https://en.wikipedia.org/wiki/Disgaea:_Hour_of_Darkness
[ref_painters_algorithm]: https://en.wikipedia.org/wiki/Painter%27s_algorithm
[ref_z_buffering]: https://en.wikipedia.org/wiki/Z-buffering
