---
layout: post
mathjax: true
comments: true
title:  "Side-Scrolling with Parallax Layers"
date:   2026-04-22 09:00:00 +0000
categories: games graphics projection
---

<!-- A177 -->
<script>console.log("A177");</script>

The previous article in the Cartesian cluster
treated the side-scrolling view
with a single background layer
that scrolls at the same rate
as the play layer.
This article adds multiple background layers,
each scrolling at its own rate,
to produce a screen-space depth illusion
that the world geometry itself does not contain.
The forward map gains a per-layer scroll factor
that multiplies the camera-relative offset
by a number between zero and one for distant layers
and by a number greater than one for foreground layers.
The inverse map ceases to return a unique world point
across all layers
and instead returns a candidate set
indexed by the layer.
The engine resolves the ambiguity
by restricting picking
to the play layer,
to the topmost matching layer,
or to the screen-space sprite hit test
that the previous article introduced.

The mode is a fixture of the side-scrolling canon.
Backgrounds appear distant
because they slide past the camera
more slowly than the gameplay objects do.
Foregrounds appear close
because they slide past the camera
more quickly.
The illusion is psychologically convincing
even though the underlying world
remains a flat two-dimensional grid
on each layer.
The article frames parallax
as an approximation to true perspective projection,
discusses the relationship between scroll factor and implied depth,
and treats the picking ambiguity
that the multiplicity of layers introduces.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is a family of forward maps,
one per layer,
each parameterised by a scroll factor.
The delivery mechanism
chooses how the period hardware
or the modern engine
composites the layers
into a single rendered frame.
The math is shared
across delivery mechanisms.
The delivery
varies by hardware capability,
the number of independent scroll registers available,
and whether the engine can update those registers
during the horizontal-blank interval
that separates one scanline from the next.

## A Brief History of the Mode

The earliest commercial use of multi-layer parallax scrolling
is debated.
[Moon Patrol][ref_moon_patrol]
from Irem in 1982
is widely cited
as the first arcade game
with three independent scrolling background planes,
a near plane of foreground rocks,
a mid plane of distant mountains,
and a far plane of stars.
Each plane scrolled at its own rate,
producing a convincing depth illusion
that single-layer scrolling could not.

The technique spreads
through the arcade and console releases of the late 1980s.
[Forgotten Worlds][ref_forgotten_worlds]
from Capcom in 1988
provided a multi-plane arcade shoot-em-up
that exercised the three background scroll layers
of the Capcom CPS-1 system
alongside the sprite layer
to produce dense stacked-plane visuals.
The home-console era brings the technique
to constrained hardware.
[Castlevania III, Dracula's Curse][ref_castlevania_3]
on the Nintendo Entertainment System in 1989
used horizontal-blank scroll-register modulation
to produce parallax
on a system that nominally provided only one background layer,
trading central-processing-unit cycles
for visual fidelity.

[Sonic the Hedgehog][ref_sonic]
on the Sega Genesis in 1991
brought multi-layer parallax
into the canon of the platformer.
The Green Hill Zone
exposes four or more visually distinct depth planes
through a combination of the Genesis's two background layers
and per-scanline scroll-register modulation.
The technique becomes
a defining visual signature
of the early Sonic series.

[Earthworm Jim][ref_earthworm_jim]
from Shiny Entertainment in 1994
applied multi-layer parallax
to a cartoon visual style
that emphasised character animation
against richly layered backgrounds.
[Super Mario World 2, Yoshi's Island][ref_yoshis_island]
on the Super Nintendo Entertainment System in 1995
combined parallax
with affine background transformations
and a hand-drawn pastel art style
that defined the late sixteen-bit aesthetic.

The technique reaches the modern independent game
through titles such as
[Ori and the Blind Forest][ref_ori]
on Microsoft Windows in 2015
and [Hollow Knight][ref_hollow_knight]
on Microsoft Windows in 2017.
Both titles use shader-driven per-layer rendering
that the modern graphics processing unit
applies as separate transforms per layer.
The math has not changed
since Moon Patrol.

## The Forward Map

The world is partitioned
into a finite set of layers
indexed by $l \in \{0, 1, \dots, L - 1\}$.
Each layer carries its own world content,
its own scroll factor $\sigma_l$,
and its own draw-order priority.
The play layer
is the layer on which the player character
and the interactive gameplay objects reside.
The play layer's scroll factor
is fixed at $\sigma_{\text{play}} = 1$
by convention,
matching the unmodified camera-relative offset
of the previous article.

The forward map
for layer $l$
is

$$
\mathbf{p}_{\text{screen}}^{(l)} = z\, (\mathbf{p}_{\text{world}}^{(l)} - \sigma_l\, \mathbf{c}) + \mathbf{o},
$$

where $z$ is the zoom factor,
$\mathbf{c}$ is the camera position,
and $\mathbf{o}$ is the screen-centre offset.
A scroll factor of $\sigma_l = 1$
recovers the unmodified forward map
from the previous article.
A scroll factor of $0 < \sigma_l < 1$
makes the layer appear distant.
A scroll factor of $\sigma_l > 1$
makes the layer appear close.
A scroll factor of $\sigma_l = 0$
fixes the layer to the screen
and the layer ceases to scroll at all,
which is the canonical implementation
of heads-up-display overlays.

The factorisation pattern from the opener
extends to the parallax case
through a per-layer scaled translation,

$$
F^{(l)} = T(\mathbf{o})\, S(z)\, T(-\sigma_l\, \mathbf{c}).
$$

The three rightmost matrices
share their structure
with the previous article's factorisation.
The only change
is the multiplication of the camera position
by the per-layer scroll factor.
In homogeneous form
the same map writes as

$$
\begin{bmatrix} s_x \\ s_y \\ 1 \end{bmatrix} =
\begin{bmatrix} z & 0 & W/2 - z\, \sigma_l\, c_x \\ 0 & z & H/2 - z\, \sigma_l\, c_y \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} w_x^{(l)} \\ w_y^{(l)} \\ 1 \end{bmatrix}.
$$

The matrix
is the planar affine matrix of the previous article
with the camera-position columns scaled by $\sigma_l$.
The side-scrolling parallax map
shares the matrix structure
with the single-layer side-scrolling map
and differs only
in the scaling of the camera position.

The operational interpretation
of the scroll factor
follows from the partial derivative of the forward map
with respect to the camera position.
A world-stationary object on layer $l$
appears to move on the screen
at a rate proportional to the camera velocity
and to the layer's scroll factor,

$$
\frac{d \mathbf{p}_{\text{screen}}^{(l)}}{dt} = -z\, \sigma_l\, \mathbf{v}_c,
$$

where $\mathbf{v}_c = d\mathbf{c}/dt$
is the camera velocity in world units per second.
A play-layer object moves at $-z \mathbf{v}_c$,
the full screen-space camera shift.
A background object at $\sigma_l = 1/2$
moves at half the rate.
A fixed-screen object at $\sigma_l = 0$
does not move on the screen at all.

The depth interpretation
relates the scroll factor
to an implied per-layer distance from the camera.
If layer $l$ is modelled
as a plane parallel to the camera
at distance $d_l$ from the camera,
and the play layer
at distance $d_{\text{play}}$,
true perspective projection gives the scroll factor as

$$
\sigma_l = \frac{d_{\text{play}}}{d_l}.
$$

The play layer at distance $d_{\text{play}}$
gives $\sigma_{\text{play}} = 1$,
a layer at twice the distance gives $\sigma_l = 1/2$,
and a layer at infinite distance
gives $\sigma_l = 0$.
The parallax illusion
approximates true perspective
to the extent that the layered approximation
matches the perspective denominator.
The synthesis closer of the series
treats the projective generalisation
that recovers the perspective denominator exactly.

The vertical parallax case
allows the scroll factor
to take a different value
along the vertical axis
than along the horizontal axis.
Writing $\boldsymbol{\sigma}_l = (\sigma_l^x,\ \sigma_l^y)$
for the per-axis scroll-factor vector,
and writing $\odot$
for the component-wise product,
the generalised forward map is

$$
\mathbf{p}_{\text{screen}}^{(l)} = z\, (\mathbf{p}_{\text{world}}^{(l)} - \boldsymbol{\sigma}_l \odot \mathbf{c}) + \mathbf{o}.
$$

Most side-scrollers
set $\sigma_l^y = 0$
for backgrounds
because the vertical camera motion
is small or non-existent.
Modern platformers with two-axis cameras
often set $\sigma_l^y = \sigma_l^x$
to keep the layer-implied depth consistent
across both axes.

## The Inverse Map

The forward map for layer $l$
is invertible in closed form,

$$
\mathbf{p}_{\text{world}}^{(l)} = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \sigma_l\, \mathbf{c}.
$$

The inverse returns a unique world point
for the specified layer.
There is no within-layer ambiguity,
no candidate set per layer,
and no missing dimension within a layer.

The ambiguity arises
across layers.
A screen pixel
does not by itself tell the engine
which layer the click refers to.
The candidate set is therefore

$$
\{ (\mathbf{p}_{\text{world}}^{(l)},\ l) : l \in \{0, 1, \dots, L - 1\} \},
$$

with $\mathbf{p}_{\text{world}}^{(l)}$
given by the per-layer inverse map above.
The inverse map is layer-restricted
in the sense
that picking only resolves the click
when the engine commits to a layer.

The engine resolves the ambiguity
through one of three conventions.

The first is play-layer-only picking.
The engine treats every click
as a gameplay action
on the play layer
and applies the floor-case inverse
with $\sigma = 1$,

$$
\mathbf{p}_{\text{world}}^{\text{play}} = \frac{1}{z}\, (\mathbf{p}_{\text{screen}} - \mathbf{o}) + \mathbf{c}.
$$

This is the dominant convention
for action-platformer gameplay
where the player input is gamepad-driven
and the only meaningful picking
is for cursor-based debug tools
or level-editor interaction
on the play layer.

The second is topmost-layer picking.
The engine iterates the layers
in front-to-back draw order,
evaluates the per-layer inverse
to find the world point on that layer,
and tests that point
against the bounding rectangles
of the layer's drawn objects.
The first matching object
in the iteration order is returned.
The strategy is appropriate
for editor environments
where the user expects to click
on whichever rendered layer
is visible at the screen position.

The third is screen-space sprite hit test.
The engine ignores the layer structure entirely
and tests the clicked screen pixel
against the screen-space bounding rectangles
of every visible sprite,
returning the topmost sprite in draw order.
The strategy is identical to the screen-space hit test
introduced in the decoupled-vertical-axis article
and is appropriate
for cursor-driven gameplay
and for light-gun targeting
that the cross-cutting picking article
treats in detail later in the series.

The visible region of the world
for layer $l$
is the pre-image of the screen rectangle
under the per-layer inverse map,

$$
\mathbf{p}_{\text{world}}^{(l)} \in \sigma_l\, \mathbf{c} + \frac{1}{z}\, \left[ -\tfrac{W}{2},\ \tfrac{W}{2} \right] \times \left[ -\tfrac{H}{2},\ \tfrac{H}{2} \right].
$$

The visible rectangle
sits at the scaled camera position $\sigma_l \mathbf{c}$
in the layer's world frame.
A distant layer
moves slowly through its world content
as the camera moves through the play layer's world,
because the visible rectangle's centre
moves at the rate $\sigma_l$
relative to the camera motion.

## A Worked Example

Consider a Sega Genesis side-scrolling platformer
with three layers.
The screen is 320 pixels wide
and 224 pixels tall,
matching the Genesis output resolution.
The zoom factor is $z = 1$,
one world unit per pixel.
The screen-centre offset is $\mathbf{o} = (160, 112)$.
The camera position is
$\mathbf{c} = (1000, 200)$.

Layer 0 is the play layer
with scroll factor $\sigma_0 = 1$.
Layer 1 is a mid-distance hills layer
with scroll factor $\sigma_1 = 1/2$.
Layer 2 is a far sky layer
with scroll factor $\sigma_2 = 1/4$.

Consider a tree on the play layer
at world position $\mathbf{p}_{\text{world}}^{(0)} = (1050, 200)$.
The forward map gives the tree's screen position as

$$
\mathbf{p}_{\text{screen}}^{(0)} = (1050 - 1 \cdot 1000,\ 200 - 1 \cdot 200) + (160, 112) = (50,\ 0) + (160, 112) = (210,\ 112).
$$

Consider a hill on layer 1
at world position $\mathbf{p}_{\text{world}}^{(1)} = (550, 100)$.
The forward map gives the hill's screen position as

$$
\mathbf{p}_{\text{screen}}^{(1)} = (550 - \tfrac{1}{2} \cdot 1000,\ 100 - \tfrac{1}{2} \cdot 200) + (160, 112) = (50,\ 0) + (160, 112) = (210,\ 112).
$$

The hill on layer 1
appears at the same screen position $(210, 112)$
as the tree on the play layer.
The hill's world coordinates
are half of what they would need to be
on the play layer
to produce the same screen position,
because the layer-1 forward map
scales the camera by $1/2$.

Consider a star on layer 2
at world position $\mathbf{p}_{\text{world}}^{(2)} = (300, 50)$.
The forward map gives the star's screen position as

$$
\mathbf{p}_{\text{screen}}^{(2)} = (300 - \tfrac{1}{4} \cdot 1000,\ 50 - \tfrac{1}{4} \cdot 200) + (160, 112) = (50,\ 0) + (160, 112) = (210,\ 112).
$$

The star on layer 2
also appears at $(210, 112)$.
Three world objects on three different layers
project to the same screen pixel.

Now consider the camera moving to $\mathbf{c} = (1100, 200)$,
a horizontal shift of $\Delta c_x = 100$ world units to the right.
The play-layer tree at world $(1050, 200)$
now projects to

$$
\mathbf{p}_{\text{screen}}^{(0)} = (1050 - 1100,\ 0) + (160, 112) = (-50,\ 0) + (160, 112) = (110,\ 112).
$$

The play-layer tree has moved
$100$ pixels left on the screen,
a screen-space shift of $-100$ pixels
matching $-\sigma_0\, \Delta c_x = -1 \cdot 100 = -100$.

The layer-1 hill at world $(550, 100)$
now projects to

$$
\mathbf{p}_{\text{screen}}^{(1)} = (550 - \tfrac{1}{2} \cdot 1100,\ 0) + (160, 112) = (0,\ 0) + (160, 112) = (160,\ 112).
$$

The hill has moved
$50$ pixels left,
matching $-\sigma_1\, \Delta c_x = -\tfrac{1}{2} \cdot 100 = -50$.

The layer-2 star at world $(300, 50)$
now projects to

$$
\mathbf{p}_{\text{screen}}^{(2)} = (300 - \tfrac{1}{4} \cdot 1100,\ 0) + (160, 112) = (25,\ 0) + (160, 112) = (185,\ 112).
$$

The star has moved
$25$ pixels left,
matching $-\sigma_2\, \Delta c_x = -\tfrac{1}{4} \cdot 100 = -25$.

Three world objects
initially coincident at one screen pixel
fan apart
as the camera moves,
with the foreground object moving farthest
and the distant object moving least.
The relative screen shift between any two layers
matches the scroll-factor difference
times the camera shift,

$$
\Delta \mathbf{p}_{\text{screen}}^{(l_1)} - \Delta \mathbf{p}_{\text{screen}}^{(l_2)} = -z\, (\sigma_{l_1} - \sigma_{l_2})\, \Delta \mathbf{c}.
$$

The play layer and the sky layer in this example
separate by $-100 + 25 = -75$ screen pixels,
matching $-(1 - 1/4) \cdot 100 = -75$.
The fanning effect
is what the player's visual system reads
as parallax depth.

Click-picking at screen pixel $(210, 112)$
returns three different world points,
one per layer,

$$
\mathbf{p}_{\text{world}}^{(0)} = (1050,\ 200),
$$

$$
\mathbf{p}_{\text{world}}^{(1)} = (550,\ 100),
$$

$$
\mathbf{p}_{\text{world}}^{(2)} = (300,\ 50).
$$

The play-layer-only convention
returns the play-layer point.
The topmost-layer convention
returns whichever layer's object
is drawn in front.
The screen-space sprite hit-test convention
returns the topmost sprite at $(210, 112)$
regardless of layer assignment.

The round-trip identity
holds within each layer,

$$
F^{(l), -1}(F^{(l)}(\mathbf{p}_{\text{world}}^{(l)})) = \mathbf{p}_{\text{world}}^{(l)} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.
The identity is the per-layer specialisation
of the round-trip identity from the previous articles
and is the simplest correctness test
the engine can run per layer.

## Variations Within the Mode

The per-layer scroll factor framework
admits several variations
that engines have explored.

A fixed background layer
sets $\sigma_l = 0$
so the layer does not scroll.
The layer renders at the same screen position
on every frame
regardless of camera motion.
Heads-up-display elements,
score readouts,
and lifebars use this convention.

A foreground layer
sets $\sigma_l > 1$
so the layer scrolls faster than the play layer.
Foreground vegetation
and atmospheric particles
use this convention
to suggest objects passing in front of the camera.

A wrapping layer
gives the layer's world content a finite repeat width $w_l$
and applies the modulo operation
to the layer's effective world position,

$$
w_x^{(l), \text{eff}} = w_x^{(l)} \bmod w_l.
$$

The wrapped layer
can render an infinitely repeating background
from a small content tile.
Most arcade and console parallax backgrounds
use wrapping
to avoid storing wide tilemaps for distant layers.

A per-scanline scroll factor
varies the scroll factor as a function of the screen vertical coordinate,

$$
\sigma_l(s_y) = \sigma_l^{\text{base}} + k_l\, (s_y - s_y^{\text{horizon}}),
$$

where $s_y^{\text{horizon}}$ is the screen y of the apparent horizon
and $k_l$ is a per-scanline gradient.
The variation produces a graduated parallax effect
where ground-plane scanlines closer to the camera
scroll faster than scanlines further away.
The technique anticipates the affine ground-plane treatment
of the Mode 7 article later in the series
but operates within the affine-translation forward-map family
of this article.

A swap-layer event
changes the player's layer assignment
when the player crosses a gameplay-defined boundary.
The swap is rare
in pure side-scrolling
and is the defining feature
of the 2.5D side-scrolling variant
of the stylised-hybrid article
later in the series.
Pure parallax side-scrolling
keeps the player on a single play layer.

A correlated-camera variant
uses a single camera position $\mathbf{c}$
across all layers
and varies only the scroll factor $\sigma_l$.
The variant is the standard formulation
and is the case the article treats.
A decorrelated-camera variant
uses a different camera position per layer
and exposes additional design flexibility
at the cost of mathematical simplicity.
The decorrelated case is rare in practice
and is mentioned for completeness.

A scaled-content layer
multiplies the layer's drawn content
by a scale factor
in addition to applying the scroll factor.
The scaled content
combines parallax with sprite scaling
in a way that anticipates the sprite-scaling article
later in the series
and that the article does not treat further here.

## Delivery Mechanisms

The forward map's per-layer structure
permits five distinct delivery mechanisms
on period hardware.

The first is multiple hardware background layers
with independent scroll registers.
The Super Nintendo Entertainment System
provided four background layers
each with its own horizontal and vertical scroll registers.
The Sega Genesis
provided two background layers
each with its own scroll registers.
The arcade hardware of the era
often provided more layers,
with the Capcom CPS-1 system supporting
three background scroll layers
and Forgotten Worlds exploiting the full set.
Each layer's hardware scroll register
holds the value $-z\, \sigma_l\, c_x$
that the rendering pipeline applies
during background fetch.

The second is horizontal-blank scroll-register modulation.
The engine updates the scroll register
during the horizontal-blank interrupt
that separates one scanline from the next,
which lets a single hardware background layer
produce different horizontal offsets
at different scanlines.
The technique multiplies the effective parallax layer count
beyond the hardware's nominal layer count.
Castlevania III on the Nintendo Entertainment System
uses horizontal-blank modulation
to produce parallax
on a system that nominally provided one background layer.
Sonic the Hedgehog on the Sega Genesis
uses the same technique
to extend the Genesis's two-layer hardware
to four or more visually distinct depth planes.
The central-processing-unit cost
of the horizontal-blank interrupt handler
is non-trivial
and is the engineering trade
that the technique requires.

The third is software composition
on a general-purpose central processing unit.
The engine maintains a frame buffer
and renders each layer
through a layer-specific software blit
that respects the layer's scroll factor.
The technique was universal
on the IBM PC running the Microsoft Disk Operating System
through the early 1990s
and remains the dominant mechanism
on modern independent-game engines
that render to a software frame buffer
or to a graphics-processing-unit texture
in a software-style pipeline.

The fourth is pre-rendered parallax frames.
The engine stores
the pre-composited multi-layer image
as a single wide background
that the camera scrolls across with a unified scroll register.
The technique
removes the per-layer flexibility
in exchange for storage efficiency
and visual fidelity
that the runtime compositor could not match.
Donkey Kong Country on the Super Nintendo Entertainment System in 1994
used pre-rendered backgrounds
in this style.

The fifth is graphics-processing-unit-accelerated quad rendering
with one textured quad per layer.
Modern game engines
such as Unity, Godot, and Unreal
render each layer as a separate textured quad
with the appropriate per-layer transform
that includes the layer's scroll factor.
The graphics processing unit
applies the transforms
in hardware
and produces the screen image.

All five mechanisms
compute the same per-layer forward map
and produce the same visible result.
The choice trades implementation complexity,
the hardware's nominal layer count,
the central-processing-unit budget for interrupt handlers,
the storage budget for pre-rendered backgrounds,
and the achievable frame rate.

## Where the Framing Breaks Down

The parallax framing is insufficient
when any of the following conditions hold.

When the depth illusion must be exact
rather than approximate,
the layered approximation is insufficient.
The synthesis closer of the series
treats the projective generalisation
where the perspective denominator
recovers the true depth dependence
rather than the discrete scroll-factor approximation.

When the player must move
between layers as a gameplay action,
the floor case is insufficient.
The 2.5D side-scrolling variant
of the stylised-hybrid article
adds explicit layer-switching
as a gameplay feature.
[Klonoa, Door to Phantomile][ref_klonoa]
on the Sony PlayStation in 1997
is the canonical example.

When the world is rendered
through per-column ray casting
of a height-mapped grid,
the projection is no longer affine
and the parallax illusion
arises from the ray-cast geometry rather than from per-layer scroll factors.
The raycasting article later in the series
treats the technique.

When the camera rotates with the player,
the per-layer forward map gains rotation,
and the parallax effect
must be computed against the rotated frame.
The rotated camera
appears in the affine-ground-plane Mode 7 case
and is treated in the Mode 7 article.

When the layered background must respect a non-flat ground,
the parallax illusion
does not extend cleanly
to a ground that bends.
The stylised-hybrid article
treats the special cases
where the ground itself
is rendered through a different projection
than the background layers.

When the layers represent
genuinely-three-dimensional objects
rather than parallel planes,
the scroll-factor abstraction
breaks down.
The synthesis closer
treats the synthesis case.

## The Canon

The following games
use multi-layer parallax scrolling
as a primary visual technique.
The list is selective
rather than exhaustive
and emphasises the games
that defined the technique
or extended it
at a given moment.

[Moon Patrol][ref_moon_patrol]
in the arcade in 1982
gave the medium
its first widely-cited three-plane parallax,
a foreground rock layer,
a mid-distance mountain layer,
and a far star layer
that scrolled at distinct rates.

[Forgotten Worlds][ref_forgotten_worlds]
in the arcade in 1988
exercised the three background scroll layers
of the Capcom CPS-1 hardware
in a horizontally-scrolling shoot-em-up
where every layer carried distinct content.

[Castlevania III, Dracula's Curse][ref_castlevania_3]
on the Nintendo Entertainment System in 1989
extended the eight-bit hardware
beyond its nominal single-background-layer ceiling
through horizontal-blank scroll-register modulation,
producing parallax on a system
that the chip designers had not provided it for.

[Sonic the Hedgehog][ref_sonic]
on the Sega Genesis in 1991
brought multi-layer parallax
into the canon of the platformer.
The Green Hill Zone
exposes four or more visually distinct depth planes
through the combination of the Genesis's two background layers
and per-scanline scroll-register modulation.

[Earthworm Jim][ref_earthworm_jim]
on the Sega Genesis in 1994
extended the technique
to a cartoon-animation visual style
where the parallax layers
carried richly drawn detail
behind the animated player character.

[Super Mario World 2, Yoshi's Island][ref_yoshis_island]
on the Super Nintendo Entertainment System in 1995
combined per-layer parallax
with affine background transformations
and a hand-drawn pastel art style
that defined the late sixteen-bit aesthetic
the system supported.

[Ori and the Blind Forest][ref_ori]
on Microsoft Windows in 2015
and [Hollow Knight][ref_hollow_knight]
on Microsoft Windows in 2017
brought multi-layer parallax
into the modern independent game
through graphics-processing-unit shader rendering
with one quad per layer
and many layers per scene.

Each game in the canon
exercises a different subset
of the per-layer scroll factor space
and uses a different delivery mechanism
appropriate to its target hardware.
The forward map and the per-layer inverse map
remain the same equations
across the canon.

## Out of Scope

The article does not cover
the following.

The affine ground-plane treatment
of Mode 7 and the affine background transformations
of the late sixteen-bit hardware
is the subject of a later article in the series.
Mode 7's per-scanline affine matrix
generalises the per-scanline scroll factor
of this article
to a per-scanline two-by-two transform
rather than a per-scanline scalar.

Raycasting
through a two-dimensional height-mapped world
to produce screen-space wall slices
with apparent depth
is the subject of a later article in the series.
The depth illusion is genuine in raycasting
rather than approximate.

The projective generalisation
where the perspective denominator
recovers true depth-from-camera relationships
is the subject of the synthesis closer
of the series.
The parallax framing of this article
is a discrete approximation
to the projective case.

The 2.5D side-scrolling games
where the player switches between two or three depth planes
through a gameplay-triggered swap event
are treated in the stylised-hybrid article.
The pure parallax framing of this article
keeps the player on a single play layer.

The compositing-system implementation details
such as Z-buffer order,
hardware sprite-priority bits,
and graphics-processing-unit shader programs
are implementation concerns
adjacent to but distinct from
the projection math.

## Conclusion

Side-scrolling with parallax layers
adds a per-layer scroll factor
to the side-scrolling forward map of the previous article.
The forward map per layer
is the previous article's map
with the camera position scaled by $\sigma_l$.
The factorisation
remains the affine translate-scale-translate of the opener.
The inverse map per layer
returns a unique world point
on that layer,
and the candidate set across layers
is the inverse-map equivalent
of the layered scene structure.
The depth illusion
that parallax produces
is psychologically convincing
and approximates true perspective projection
to the extent that the layered model
matches the perspective denominator.
The synthesis closer of the series
treats the projective generalisation
that the parallax framing approximates.
The math is simple
and the delivery
admits five distinct mechanisms
on period hardware and modern engines.
The next article in the cluster
introduces an explicit depth axis
that the player can navigate,
which is the belt-scroll mode.

## References

- [Reference, Castlevania III, Dracula's Curse][ref_castlevania_3]
- [Reference, Earthworm Jim][ref_earthworm_jim]
- [Reference, Forgotten Worlds][ref_forgotten_worlds]
- [Reference, Hollow Knight][ref_hollow_knight]
- [Reference, Klonoa, Door to Phantomile][ref_klonoa]
- [Reference, Moon Patrol][ref_moon_patrol]
- [Reference, Ori and the Blind Forest][ref_ori]
- [Reference, Sonic the Hedgehog][ref_sonic]
- [Reference, Super Mario World 2, Yoshi's Island][ref_yoshis_island]

[ref_castlevania_3]: https://en.wikipedia.org/wiki/Castlevania_III:_Dracula%27s_Curse
[ref_earthworm_jim]: https://en.wikipedia.org/wiki/Earthworm_Jim_(video_game)
[ref_forgotten_worlds]: https://en.wikipedia.org/wiki/Forgotten_Worlds
[ref_hollow_knight]: https://en.wikipedia.org/wiki/Hollow_Knight
[ref_klonoa]: https://en.wikipedia.org/wiki/Klonoa:_Door_to_Phantomile
[ref_moon_patrol]: https://en.wikipedia.org/wiki/Moon_Patrol
[ref_ori]: https://en.wikipedia.org/wiki/Ori_and_the_Blind_Forest
[ref_sonic]: https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_(1991_video_game)
[ref_yoshis_island]: https://en.wikipedia.org/wiki/Super_Mario_World_2:_Yoshi%27s_Island
