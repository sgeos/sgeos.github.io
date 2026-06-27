---
layout: post
mathjax: true
comments: true
title:  "The Camera as Linear Operator, Affine and Projective Synthesis"
date:   2026-05-02 09:00:00 +0000
categories: games graphics projection
---

<!-- A187 -->
<script>console.log("A187");</script>

The closing article of the series
treats the camera as a linear operator
in projective space
and recovers each previous article's projection mode
as a restricted case
of the modern graphics-processing-unit rendering pipeline.
The pipeline expresses the forward map
as a composition of three matrices
that the engine applies in sequence
to each world vertex,

$$
\mathbf{p}_{\text{clip}} = P\, V\, M\, \mathbf{p}_{\text{world}}.
$$

The model matrix $M$
transforms model-local coordinates
into world coordinates.
The view matrix $V$
transforms world coordinates
into camera-frame coordinates.
The projection matrix $P$
transforms camera-frame coordinates
into clip-space coordinates
that the graphics hardware
maps to the screen.

The perspective division
follows the matrix multiplication
and converts the four-component clip-space coordinate
into a three-component normalised-device coordinate
through division by the fourth component.
The division
is the operational meaning of perspective foreshortening
and is the new mathematical content
that distinguishes the projective synthesis
from the affine projection modes
of the previous articles.

The article frames each previous projection mode
as a specific choice of $P$, $V$, and $M$
that produces the visual signature of the mode.
Top-down projection
uses an orthographic $P$.
Side-scrolling, belt-scroll, oblique, and axonometric projections
all use orthographic $P$
with different model or view transforms.
Mode 7
uses an orthographic $P$
with a per-scanline view transform.
Sprite scaling
uses a per-sprite model transform
that approximates the perspective division.
Raycasting
uses a per-column ray
that the perspective division produces directly.
Each restricted case
falls out of the projective framework
as a limit, a constraint,
or a per-fragment approximation.

The framing the series carries
from the opener
distinguishes the projection math
from the delivery mechanism.
The projection math
is the projective matrix pipeline
that the article describes.
The delivery mechanism
is the modern graphics-processing-unit pipeline
that the article credits
as the modern realisation
of the projective framework.

## A Brief History of the Projective Synthesis

The projective interpretation of perspective drawing
dates to the Renaissance.
Filippo Brunelleschi's perspective experiments
in 1413 Florence
demonstrated the use of a fixed vanishing point
and the linear convergence of parallel lines.
Leon Battista Alberti's 1435 treatise On Painting
formalised the technique
as a mathematical procedure
that the painter could follow
to construct geometrically-correct perspective drawings.

The projective geometry of lines and planes
emerged in the seventeenth century
through Girard Desargues's work on conics
and Blaise Pascal's hexagon theorem.
The nineteenth century
saw the development of projective geometry
as a formal mathematical discipline
distinct from Euclidean geometry,
with Jean-Victor Poncelet's 1822 treatise
On the Projective Properties of Figures
establishing the field.

Computer graphics adopts the projective framework
in the mid-twentieth century
through the work of Larry Roberts in 1963
on hidden-surface removal
and James Blinn and Martin Newell in the 1970s
on transformation matrices for shading and texturing.
The OpenGL and Direct3D standards
of the 1990s
codified the matrix pipeline
that modern graphics-processing-unit hardware accelerates.

The video-game adoption
of true projective perspective rendering
arrives in the early 1990s
through arcade hardware that supported polygon rendering
and through home consoles
with cartridge coprocessors
that accelerated the matrix arithmetic.

[Star Fox][ref_star_fox]
from Nintendo and Argonaut Software in 1993
on the Super Nintendo Entertainment System
used the Super FX chip
to render polygons
in true perspective projection.
The game ran at low frame rates
on the SNES central processing unit
but demonstrated three-dimensional polygon gameplay
that the pre-coprocessor SNES hardware
could not have produced.

[Doom][ref_doom]
from id Software in 1993
on the IBM PC
used a binary-space-partition rendering technique
that the previous article on raycasting
identified as outside the raycasting framework.
Doom's rendering
is sometimes described as two-and-a-half-dimensional
because the camera could not tilt or roll
and the levels did not contain rooms above rooms.

[Quake][ref_quake]
from id Software in 1996
on the IBM PC
brought true projective perspective rendering
to the mass-market personal computer.
The Quake engine
implemented the full three-dimensional pipeline
including arbitrary camera placement,
fully three-dimensional geometry,
and the perspective division per pixel
that the modern pipeline requires.

The modern era
from the late 1990s onward
runs the projective pipeline
on graphics-processing-unit hardware
that handles the matrix arithmetic
and the perspective division
at the hardware-rasterisation level.
The article treats the modern pipeline
as the universal projection framework
that subsumes the affine and pseudo-three-dimensional modes
of the previous articles.

## The PVM Pipeline

The world coordinate of a vertex
is a three-dimensional position
$\mathbf{p}_{\text{world}} = (w_x, w_y, w_z)$
in the $y$-down convention of the previous articles.
The homogeneous augmentation
adds a fourth component
that the projective framework requires,

$$
\tilde{\mathbf{p}}_{\text{world}} = (w_x, w_y, w_z, 1).
$$

The fourth component
distinguishes points
that have a finite location in space
from directions
that extend to infinity.
A point at finite location has $w = 1$.
A direction vector has $w = 0$.

The pipeline applies three matrices
to the homogeneous world coordinate.

The model matrix $M$ is a four-by-four matrix
that transforms model-local coordinates
into world coordinates.
For a single object,
$M$ encodes the object's position, orientation, and scale
in the world frame,

$$
\tilde{\mathbf{p}}_{\text{world}} = M\, \tilde{\mathbf{p}}_{\text{model}}.
$$

The view matrix $V$ is a four-by-four matrix
that transforms world coordinates
into camera-frame coordinates,

$$
\tilde{\mathbf{p}}_{\text{view}} = V\, \tilde{\mathbf{p}}_{\text{world}}.
$$

The view matrix
encodes the camera's position and orientation
in the world frame.
A camera at the origin looking along $+w_z$
into the screen
has $V$ as the identity matrix
under the series's depth-into-screen convention.

The projection matrix $P$ is a four-by-four matrix
that transforms camera-frame coordinates
into clip-space coordinates,

$$
\tilde{\mathbf{p}}_{\text{clip}} = P\, \tilde{\mathbf{p}}_{\text{view}}.
$$

The projection matrix
encodes the camera's lens parameters
including the field of view,
the aspect ratio,
and the near and far clipping planes.

The full pipeline is

$$
\tilde{\mathbf{p}}_{\text{clip}} = P\, V\, M\, \tilde{\mathbf{p}}_{\text{model-local}}.
$$

When the article treats the world coordinate
as the model-local input
without an explicit model transform,
the pipeline simplifies to

$$
\tilde{\mathbf{p}}_{\text{clip}} = P\, V\, \tilde{\mathbf{p}}_{\text{world}}.
$$

The series typically uses this simplified form
for projection-mode comparisons.

## The Perspective Division

The clip-space coordinate
is a four-component vector
$\tilde{\mathbf{p}}_{\text{clip}} = (x_c, y_c, z_c, w_c)$.
The perspective division
converts the clip-space coordinate
into a three-component normalised-device coordinate
through division by the fourth component,

$$
\mathbf{p}_{\text{ndc}} = \left( \frac{x_c}{w_c},\ \frac{y_c}{w_c},\ \frac{z_c}{w_c} \right).
$$

The division
is the operational meaning of perspective foreshortening.
A vertex further from the camera
has a larger $w_c$
and a correspondingly smaller normalised-device coordinate
in the screen plane.
The smaller coordinate
maps to a smaller screen-space position
that the viewer reads as further away.

The viewport transformation
converts the normalised-device coordinate
into screen pixel coordinates,

$$
s_x = \frac{W}{2}\, (x_{\text{ndc}} + 1),\quad s_y = \frac{H}{2}\, (y_{\text{ndc}} + 1),
$$

where $W$ and $H$ are the screen width and height in pixels.
The $y$ sign convention
matches the screen $y$-down convention
that the series uses throughout,
where positive NDC $y$ corresponds to a position
below the screen centre.

A projection matrix
with the fourth row $(0, 0, 0, 1)$
produces $w_c = 1$ for every input vertex.
The perspective division
becomes a division by one,
which is the identity.
The projection
collapses to an affine map
without perspective foreshortening.
The article calls this case
the orthographic projection.

A projection matrix
with the fourth row $(0, 0, 1, 0)$
produces $w_c = z_v$
where $z_v$ is the view-space depth.
The perspective division
divides by the depth,
producing the inverse-distance scaling
that the projective framework requires.
The article calls this case
the perspective projection.

The canonical perspective projection matrix
takes the form

$$
P_{\text{persp}} =
\begin{bmatrix}
f / a & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & A & B \\
0 & 0 & 1 & 0
\end{bmatrix},
$$

where $f = 1 / \tan(\phi/2)$ is the focal length factor
for vertical field of view $\phi$,
$a = W/H$ is the aspect ratio,
and $A$ and $B$ are constants
that map the view-space depth
to the normalised-device-coordinate depth
within the visible range.

The canonical orthographic projection matrix
takes the form

$$
P_{\text{ortho}} =
\begin{bmatrix}
1/r & 0 & 0 & 0 \\
0 & 1/t & 0 & 0 \\
0 & 0 & 2/(z_f - z_n) & -(z_f + z_n)/(z_f - z_n) \\
0 & 0 & 0 & 1
\end{bmatrix},
$$

where $r$ and $t$ are the half-widths of the viewing volume
along the lateral and vertical axes
and $z_n$ and $z_f$ are the near and far clipping distances.
The article uses $z_n$ and $z_f$ for the clipping planes
to avoid the symbol clash with the focal length factor $f$
in the perspective matrix above.

## Reduction to Affine Special Cases

Each projection mode of the previous clusters
emerges from the projective framework
as a specific choice of $P$, $V$, and $M$.

The top-down floor case of the first cluster
uses an orthographic $P$
with the view matrix
oriented to look straight down at the world.
The forward map of the top-down article
follows from the projection matrix multiplication
without the perspective division
because $P_{\text{ortho}}$ produces $w_c = 1$.

The decoupled-vertical-axis case
uses the same orthographic $P$
with an additional model transform
that translates the object by its height above the ground.
The shadow-drop forward map of the decoupled-vertical-axis article
follows from the model transform
combined with the orthographic projection.

The side-scrolling case
uses an orthographic $P$
with the view matrix
oriented to look horizontally at the world.
The view matrix encodes the lateral camera position
that the side-scrolling article treated
as the canonical right-bias camera.

The parallax variant
uses multiple model matrices
each with a different scale factor on the camera position.
The per-layer scroll factor of the parallax article
is the per-layer scaling
that the model matrix encodes.

The belt-scroll case
uses an orthographic $P$
with a shear in the view matrix
that adds the depth coordinate
to the screen-y direction.
The depth-mixing slope of the belt-scroll article
is the shear coefficient in the view matrix.

The oblique projection of the second cluster
uses an orthographic $P$
with a two-axis shear in the view matrix
that the oblique article treated.

The axonometric projection
uses an orthographic $P$
with a rotation in the view matrix
that aligns the camera direction
with the body-diagonal direction
in the case of strict isometric.

The Mode 7 case
uses an orthographic $P$
with a per-scanline view matrix
that the engine updates
through horizontal-blank scroll register modulation.
The per-scanline scaling
approximates the perspective division
that the projective framework provides directly.

The sprite-scaling case
uses a perspective $P$
applied per sprite anchor
combined with a per-sprite scaling factor in the model matrix.
The scaling factor $s = f/d$
of the sprite-scaling article
is the inverse-depth scaling
that the perspective division produces
for the sprite anchor.

The raycasting case
uses a perspective $P$
applied to a degenerate world model
where the world is a two-dimensional grid
extruded vertically by the wall height.
The per-column ray cast
of the raycasting article
is the perspective division
applied per screen column.

The Mode 7, sprite-scaling, and raycasting modes
all use forms of inverse-distance scaling
that emerge from the same perspective division.
For a vertex at view-space depth $d$,
the perspective division
produces an inverse-distance scaling factor

$$
k(d) = \frac{1}{d}.
$$

The Mode 7 per-scanline scaling factor $z(s_y) = h/(s_y - s_y^{\text{horizon}})$,
the sprite-scaling factor $s = f/d$,
and the raycasting wall-slice height $h_{\text{slice}} = f/d_{\text{perp}}$
all specialise this unifying inverse-distance factor
to their respective projection contexts.

The piecewise projections of the stylised-hybrid article
combine multiple choices of $P$, $V$, and $M$
in a single scene
based on world region or game state.
The Mother hybrid
uses an orthographic $P$ with a top-down view matrix
for the ground tiles
and an orthographic $P$ with a side-elevation view matrix
for the building sprites.
The two projections share the same screen output
through the artistic convention
that the previous article described.

The painter's algorithm and Y-sort framework
of the draw-order article
are independent of the choice of $P$, $V$, and $M$
and apply to any forward map
that produces a back-to-front sort key.

The picking framework
of the previous article
uses the inverse of the same projection matrix
that the forward map applied.
For an affine $P$,
the inverse is the standard matrix inverse.
For a perspective $P$,
the inverse map
includes the inverse of the perspective division
which the article calls unprojection.

## The Inverse Projective Map and Picking

The inverse of the projective pipeline
takes a screen pixel and a depth value
back to a world coordinate.
The screen pixel
inverts through the viewport transformation
to a normalised-device coordinate,

$$
x_{\text{ndc}} = \frac{2\, s_x}{W} - 1,\quad y_{\text{ndc}} = 1 - \frac{2\, s_y}{H}.
$$

The depth value
either comes from the depth buffer
that the graphics-processing-unit pipeline maintains
or from a gameplay-context assumption
such as the ground-plane assumption
of the earlier articles.

The clip-space coordinate
follows from the inverse perspective division,

$$
\tilde{\mathbf{p}}_{\text{clip}} = w_c\, (x_{\text{ndc}},\ y_{\text{ndc}},\ z_{\text{ndc}},\ 1),
$$

where $w_c$ is the clip-space fourth component
that the depth and the projection matrix together determine.
The world-coordinate inverse
follows from applying the inverses of $P$, $V$, and $M$
in reverse order,

$$
\tilde{\mathbf{p}}_{\text{world}} = M^{-1}\, V^{-1}\, P^{-1}\, \tilde{\mathbf{p}}_{\text{clip}}.
$$

The full inverse-projective pipeline
gives the world coordinate
of the click pixel at the given depth.
The picking framework of the previous article
applies the inverse pipeline
followed by the per-projection-mode disambiguation strategies
to identify the gameplay object.

For two-dimensional games
that use only an orthographic $P$,
the inverse projective map
reduces to the affine inverse
that the projection-mode articles introduced.

For three-dimensional games
that use a perspective $P$,
the inverse projective map
requires the depth value
to identify a unique world position.
The depth buffer of the graphics-processing-unit pipeline
provides this value
through hardware-accelerated per-pixel depth storage.

## A Worked Example

Consider a single world vertex at world position
$\mathbf{p}_{\text{world}} = (10, 5, 50)$
in the $y$-down convention.
The screen is 800 pixels wide
and 600 pixels tall
with aspect ratio $a = 800/600 = 4/3$.

The view matrix
places the camera at the origin
looking along $+w_z$ axis,

$$
V = I.
$$

The orthographic projection matrix
uses lateral half-width $r = 20$,
vertical half-height $t = 15$,
near plane $z_n = 1$,
and far plane $z_f = 100$,

$$
P_{\text{ortho}} =
\begin{bmatrix}
1/20 & 0 & 0 & 0 \\
0 & 1/15 & 0 & 0 \\
0 & 0 & 2/99 & -101/99 \\
0 & 0 & 0 & 1
\end{bmatrix}.
$$

The clip-space coordinate
through the orthographic pipeline is

$$
\tilde{\mathbf{p}}_{\text{clip, ortho}} = P_{\text{ortho}}\, (10, 5, 50, 1) = (1/2,\ 1/3,\ -1/99,\ 1).
$$

The perspective division divides by $w_c = 1$
and produces the normalised-device coordinate

$$
\mathbf{p}_{\text{ndc, ortho}} = (1/2,\ 1/3,\ -1/99).
$$

The viewport transformation
gives the screen pixel coordinate

$$
\mathbf{p}_{\text{screen, ortho}} = \big( 400\, (1/2 + 1),\ 300\, (1/3 + 1) \big) = (600,\ 400).
$$

The vertex projects to screen $(600, 400)$
under the orthographic projection.

The perspective projection matrix
uses focal length factor $f = 1$
for a 90-degree vertical field of view,

$$
P_{\text{persp}} =
\begin{bmatrix}
3/4 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & A & B \\
0 & 0 & 1 & 0
\end{bmatrix},
$$

where $A$ and $B$ map the view-space depth to normalised-device-coordinate depth.

The clip-space coordinate
through the perspective pipeline is

$$
\tilde{\mathbf{p}}_{\text{clip, persp}} = P_{\text{persp}}\, (10, 5, 50, 1) = (7.5,\ 5,\ A \cdot 50 + B,\ 50).
$$

The perspective division divides by $w_c = 50$.
The normalised-device coordinate is

$$
\mathbf{p}_{\text{ndc, persp}} = \left( \frac{7.5}{50},\ \frac{5}{50},\ \frac{A \cdot 50 + B}{50} \right) = (0.15,\ 0.10,\ z_{\text{ndc}}).
$$

The viewport transformation
gives the screen pixel coordinate

$$
\mathbf{p}_{\text{screen, persp}} = \big( 400\, (0.15 + 1),\ 300\, (0.10 + 1) \big) = (460,\ 330).
$$

The vertex projects to screen $(460, 330)$
under the perspective projection.

The two projections produce different screen positions
for the same world point.
The orthographic projection
maps the lateral and vertical world coordinates
directly to screen pixels
without any depth dependence.
The perspective projection
applies the inverse-depth scaling
that the perspective division produces
to map the same world coordinates
through the foreshortening factor that depth introduces.

A second vertex at world position $(10, 5, 25)$
is half as far from the camera
as the first vertex.
Under the perspective projection,
the second vertex's clip-space $w_c = 25$
gives a normalised-device coordinate
twice as far from the screen centre
as the first vertex,

$$
\mathbf{p}_{\text{ndc, persp, near}} = (7.5/25,\ 5/25,\ z_{\text{ndc}}) = (0.3,\ 0.2,\ z_{\text{ndc}}).
$$

The screen position is $(520, 360)$,
further from the screen centre
than the first vertex at $(460, 330)$.
The closer vertex
appears further from the centre on screen,
matching the perspective expansion
that the projective framework produces.

Under the orthographic projection,
both vertices at $(10, 5, 50)$ and $(10, 5, 25)$
project to the same screen pixel $(600, 400)$
because the orthographic projection
discards the depth coordinate
from the screen-position computation.

The round-trip identity
holds within each projection,

$$
F^{-1}(F(\mathbf{p}_{\text{world}})) = \mathbf{p}_{\text{world}} + O(\varepsilon),
$$

where $\varepsilon$ is the floating-point precision of the engine.
For the perspective projection,
the round-trip requires the depth value
that the depth buffer or gameplay context provides.

## Variations Within the Mode

The projective framework
admits several variations
that engines have explored.

A perspective-camera variant
uses the canonical perspective projection matrix
with adjustable field of view,
aspect ratio,
and near and far clipping planes.
The variant is the default
in three-dimensional graphics-processing-unit pipelines.

An orthographic-camera variant
uses the canonical orthographic projection matrix
without the perspective division.
The variant is the default
in two-dimensional games and in technical drawing.

An off-axis perspective variant
shifts the projection's principal point
away from the screen centre
to produce asymmetric viewing volumes.
The variant
appears in stereo rendering
and in head-tracked virtual reality
where the two eyes
have slightly different projection matrices.

A frustum-symmetric variant
forces the projection volume to be symmetric
around the camera's principal axis.
The variant
simplifies the matrix arithmetic
at the cost of flexibility.

A reverse-Z variant
maps the near plane to clip-space $z = 1$
and the far plane to clip-space $z = 0$
rather than the conventional opposite mapping.
The variant
improves depth-buffer precision
for distant objects.

A linear-Z variant
maps the view-space depth linearly
into clip-space depth
rather than through the standard non-linear mapping.
The variant
simplifies depth-buffer arithmetic
at the cost of standard pipeline compatibility.

A non-pinhole-camera variant
applies a non-rectangular projection
such as a fisheye or panoramic mapping
through a per-pixel shader
that replaces the matrix-and-division pipeline.
The variant
produces non-rectilinear visual effects
including dramatic curvature distortions
that the standard projection cannot reproduce.

A motion-blur variant
samples the projection at multiple time points
within a single frame
and accumulates the results
to produce temporal anti-aliasing
or motion-blur effects.
The variant
is rendering-pipeline territory
beyond the projection math.

## Delivery Mechanisms

The projective pipeline
permits five distinct delivery mechanisms
on period and modern hardware.

The first is software vertex-and-pixel processing
on a general-purpose central processing unit.
The engine
computes the matrix multiplication and the perspective division
in software
and writes the resulting pixels to the frame buffer.
The mechanism was the universal delivery
on personal computers through the mid-1990s
including Quake and the early three-dimensional first-person shooters.

The second is fixed-function vertex hardware
on early graphics-processing-unit accelerator cards.
The 3dfx Voodoo, the NVIDIA RIVA TNT,
and similar mid-1990s hardware
implemented the projective pipeline
in fixed-function silicon
that the engine drove through a standard API.
The mechanism
removed the central-processing-unit cost
of matrix arithmetic
and the perspective division.

The third is programmable shader hardware
on modern graphics processing units.
A vertex shader
computes the projective matrix multiplication per vertex.
A fragment shader
computes the per-pixel colour
including any non-linear projection effects.
The mechanism is the dominant delivery
on contemporary graphics-processing-unit hardware.

The fourth is cartridge coprocessor hardware
on home consoles
of the early 1990s.
The Super FX chip
in the Star Fox cartridge
provided polygon-rendering computations
that the standard SNES hardware
could not produce.
The mechanism
brought three-dimensional rendering to the home console
before the dedicated three-dimensional graphics-processing-unit era.

The fifth is dedicated three-dimensional rendering hardware
on arcade systems
of the early and mid-1990s.
The Sega Model 1 board in 1992
and the Sega Model 2 board in 1993
demonstrated polygon rendering
at frame rates and visual quality
that home-console hardware
could not match.

All five mechanisms
implement the same projective pipeline.
The choice trades hardware availability,
implementation complexity,
the maximum polygon throughput,
and the achievable resolution and frame rate.

## Where the Framing Breaks Down

The projective framework
is insufficient
when any of the following conditions hold.

When the rendering must produce
non-photorealistic stylised output
that the projective camera does not produce,
the engine
augments the projective pipeline
with post-processing shaders
that transform the rendered image
into the desired style.
The Limbo and Inside aesthetic
that the previous article on hybrid projections treated
is an example of this case.

When the world contains
genuinely infinite or unbounded content
that cannot fit within a finite far plane,
the projective framework's far-plane parameter
limits the visible distance.
The engine must either
extend the far plane to a large but finite value
or augment the projective pipeline
with techniques such as logarithmic depth buffers
or cascaded depth representations.

When the rendering must depict
relativistic effects
such as the apparent contraction of objects at high speed
or the aberration of light,
the standard projective pipeline is insufficient.
The engine must implement a per-vertex aberration computation
that the pipeline does not provide natively.

When the gameplay requires
camera positions or orientations
that the standard pinhole camera cannot produce,
the engine must extend the pipeline
with custom projection mathematics.
The 360-degree panoramic camera
of virtual-reality applications
is the canonical example.

When the rendering must scale
to extremely large or extremely small object dimensions
that exceed the depth buffer's precision,
the engine must implement
specialised depth-precision techniques
such as the reverse-Z variant
or the cascaded shadow-map techniques
that the article does not treat in detail.

When the gameplay requires
arbitrary non-linear visual effects
that the matrix-based pipeline cannot produce,
the engine must implement the effects
through pixel-shader programs
that operate after the projection
or instead of it.

## The Canon

The following games
established the projective synthesis
in the consumer video-game tradition.
The list is selective
rather than exhaustive
and emphasises the games
that defined the mode at a given moment.

[Star Fox][ref_star_fox]
on the Super Nintendo Entertainment System in 1993
brought polygon-based three-dimensional rendering
to the home console
through the Super FX cartridge coprocessor.
The on-rails space shooter
established that home console hardware
could deliver real-time polygon rendering
with the assistance of cartridge silicon.

[Doom][ref_doom]
on the IBM PC in 1993
brought a binary-space-partition rendering technique
to the mass-market personal computer
that produced visually three-dimensional gameplay
without the full projective pipeline.
The article treats Doom's rendering
as a precursor to the full projective synthesis
that subsequent titles delivered.

[Quake][ref_quake]
on the IBM PC in 1996
brought true three-dimensional polygon rendering
with the full projective pipeline
to the mass-market personal computer.
The Quake engine
established the visual template
for the first-person shooter genre
and for the consumer three-dimensional engines
that the late 1990s saw.

[Half-Life][ref_half_life]
on Microsoft Windows in 1998
extended the Quake engine
with scripted-sequence gameplay
and a more cohesive single-player campaign
that the polygon-based engine could deliver.

The subsequent decades
produced an essentially uncountable list
of three-dimensional games
that the projective pipeline rendered.
The article treats the modern era
as the universal projective synthesis
that subsumes all earlier projection modes.

Each game in the canon
exercises the projective pipeline
with different choices of $P$, $V$, and $M$.
The differences lie in the gameplay mechanics,
the art style,
and the choice of delivery hardware
appropriate to the target platform.

## Out of Scope

The article does not cover
the following.

The full graphics-processing-unit shader programming framework
including the vertex and fragment shader stages,
the texture-sampling rules,
the depth and stencil buffer operations,
and the blending and compositing rules
is rendering-pipeline territory
adjacent to but distinct from
the projection math.

The non-Euclidean geometry
that some experimental games employ
including the hyperbolic geometry of HyperRogue in 2011
and the spherical geometry of Antichamber in 2013
is outside the standard projective framework
that the article treats.

The animation pipeline
including skeletal animation,
morph targets,
and procedural animation
applies before the projective pipeline
and is rendering-systems territory
that the article does not cover.

The lighting and shading models
including the Phong, Blinn-Phong,
physically-based,
and image-based rendering models
operate after the projective pipeline
on the rendered pixels
and are outside the projection math.

The full ray-tracing framework
that real-time ray tracing hardware
of the late 2010s and 2020s enabled
is an alternative rendering approach
that bypasses the projective rasterisation pipeline
and uses per-pixel ray-mesh intersection
that the article does not treat.

The general history of the personal-computer and console industries
across the late 1990s and 2000s
is outside the article's scope.
The article treats the modern era
through its projective-pipeline lens
without surveying the broader industry history.

## Conclusion

The projective synthesis
gathers the projection-mode articles of the series
into a single matrix-based framework
that the modern graphics-processing-unit pipeline implements.
The forward map
applies three matrices to each world vertex,

$$
\mathbf{p}_{\text{clip}} = P\, V\, M\, \mathbf{p}_{\text{world}},
$$

followed by the perspective division
that produces the normalised-device coordinate
and the viewport transformation
that produces the screen pixel.
Each previous projection mode
emerges as a specific choice
of the projection matrix $P$,
the view matrix $V$,
and the model matrix $M$.
Top-down, side-scrolling, decoupled-vertical-axis, belt-scroll,
oblique, axonometric, parallax, Mode 7, sprite-scaling,
raycasting, and stylised-hybrid projections
all reduce to restricted cases
of the projective framework.
The draw-order, picking, and hit-test articles
provide cross-cutting concerns
that apply to any forward map
that the framework produces.
The series began with the floor-case top-down projection
of a two-dimensional world
and closes with the projective synthesis
that subsumes all the modes
the cluster articles introduced.
The mathematics
runs from the simplest affine map
of the floor case
to the full projective pipeline
of modern three-dimensional games,
and the journey
illustrates how the camera as linear operator
encodes everything
from the simplest two-dimensional view
to the rich three-dimensional rendering
that contemporary games produce.

## References

- [Reference, Doom][ref_doom]
- [Reference, Half-Life][ref_half_life]
- [Reference, Quake][ref_quake]
- [Reference, Star Fox][ref_star_fox]

[ref_doom]: https://en.wikipedia.org/wiki/Doom_(1993_video_game)
[ref_half_life]: https://en.wikipedia.org/wiki/Half-Life_(video_game)
[ref_quake]: https://en.wikipedia.org/wiki/Quake_(video_game)
[ref_star_fox]: https://en.wikipedia.org/wiki/Star_Fox_(1993_video_game)
