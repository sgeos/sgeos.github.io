---
layout: post
mathjax: true
comments: true
title:  "Single Parameter Equation for a  Sphere"
date:   2016-09-02 10:48:07 +0000
categories: 3d parametric math
---

<!-- A41 -->
<script>console.log("A41");</script>

This post covers some equations I found when playing around with plotting 3D parametric trigonometric functions.
The goal was to create a sphere with one parameter.

This is a parametric equation for a single parameter "spiral" sphere.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^0 t}\right) \\
\notag t & \in \mathbb{R}, 0 \le t \le 2 \pi \\
\notag c & \in \mathbb{R}, 1 \le c \\
\end{aligned} \\
\tag{1}
$$

This version gives a "beachball" sphere.

$$
\begin{aligned}
x & = \left(\sin {c^1 t}\right) \left(\sin {c^0 t}\right) \\
\notag y & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{2}
$$

$\bbox[cyan] {x = \sin t, y = \cos t}$ is the parametric equation for a circle.
$\bbox[cyan] {z = \cos t, x = y = \sin t}$ is just the circle again, but this adds a third dimension.
Another term $\bbox[cyan] {w = \cos t, x = y = z = \sin t}$ could probably be used for a 4D hypersphere.

$c^n$, a constant, is the relative revolution speed of each layer.
Increasing $c$ will add more revolutions when tracing the sphere.
This gives a better visual appearance.
The important thing is that one layer is moving relatively faster than the other.
If another layer were added, it would have a speed of $c^2$.
The constants $c^0$ and $c^1$ are indeed 1 and $c$, respectively.

Any value can be used for $c$.
The "spiral" version starts to look like a sphere when $c$ is at least 12, and the "beachball" when $c$ is at least 6.
Values of less than one $\bbox[cyan] {\left\lvert  c \right \rvert \lt 1}$ are relatively broken.
When $c=\infty$, the function *is* a sphere.
The "spiral" scans a complete circle from the top of the sphere to the bottom $\bbox[cyan] {z \in 1 \to -1}$,
and the "beachball" rotates a circle around the z axis.

The following equation is a solid 2D circle when $c$ is $\infty$.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{3}
$$

One of these is probably the equation for a solid sphere.

$$
\begin{aligned}
x & = \left(\sin {c^2 t}\right) \left(\cos {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\end{aligned} \\
\tag{4}
$$

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\sin {c^2 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{5}
$$

A circle is formed in the xy, xz and yz planes.
xy is traced faster than xz, and xz faster than xy.
This may not actually be a volume filled sphere.
The free online 3D plotting tools are not very good for visualizing something like this.

The function for the spiral sphere can be modified to get different shapes.
$\bbox[cyan] {\star}$ is used to indicate modifications to the spiral sphere.

An hourglass.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{6}
$$

Rounded hourglass.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {\frac {c^0 t} {2}}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{7}
$$

An hourglass from one direction and a circle from the other two.
$cos$ or $sin$ can be used for $z$.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{8}
$$

A tornado.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left|\sin {c^0 t}\right| - 1 & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{9}
$$

Top or turnip.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left(\sin {\frac {c^0 t} {2}}\right) - 1 & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{10}
$$

This spirals up from the inside center, down around the outside, and then in up through the center.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{11}
$$

This spirals down from the center and up around the outside instead.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = -\left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{12}
$$

A tall rounded hill.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{13}
$$

This strange shape is round when plotted in xz, a square in xy, and an hourglass in yz.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\cos {c^0 t}\right) \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\notag z & = \left(\cos {c^0 t}\right) \\
\end{aligned} \\
\tag{14}
$$

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 14 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 14, 0 are established and 14 are bespoke.
Every curve is traced by the single parameter $t$ in radians, and the dimensionless constant $c$ sets the relative revolution speed of each layer, so a curve approaches the surface it describes only as $c$ grows large.

*Equation 1, Bespoke Single Parameter Spiral Sphere.*
The article constructs a sphere from one parameter by letting the azimuth turn $c$ times faster than the polar angle, so the curve spirals from pole to pole and covers the surface only as $c$ grows.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^0 t}\right) \\
\notag t & \in \mathbb{R}, 0 \le t \le 2 \pi \\
\notag c & \in \mathbb{R}, 1 \le c \\
\end{aligned} \\
\tag{1}
$$

*Equation 2, Bespoke Single Parameter Beachball Sphere.*
Exchanging the two speeds of the spiral sphere makes the polar angle the fast layer, so the construction rotates a great circle slowly about the vertical axis.

$$
\begin{aligned}
x & = \left(\sin {c^1 t}\right) \left(\sin {c^0 t}\right) \\
\notag y & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{2}
$$

*Equation 3, Bespoke Single Parameter Solid Disc.*
Dropping the vertical coordinate of the spiral sphere projects it onto the plane, a construction the article states fills a solid disc as $c$ tends to infinity.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{3}
$$

*Equation 4, Bespoke First Candidate Solid Sphere.*
The article proposes three layers with speeds $1$, $c$ and $c^2$ paired across the three coordinates as a candidate for a filled sphere, and it leaves open whether the curve fills the volume.

$$
\begin{aligned}
x & = \left(\sin {c^2 t}\right) \left(\cos {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\end{aligned} \\
\tag{4}
$$

*Equation 5, Bespoke Second Candidate Solid Sphere.*
The article nests a third layer of speed $c^2$ inside the spiral sphere as a second candidate for a filled sphere, and it leaves open whether the curve fills the volume.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\sin {c^2 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{aligned} \\
\tag{5}
$$

*Equation 6, Bespoke Hourglass.*
Replacing the cosine in the vertical coordinate of the spiral sphere with a sine turns the sphere into an hourglass.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{6}
$$

*Equation 7, Bespoke Rounded Hourglass.*
Halving the frequency of the vertical cosine in the spiral sphere gives a rounded hourglass.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {\frac {c^0 t} {2}}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{7}
$$

*Equation 8, Bespoke Hourglass with Circular Projections.*
Driving the vertical coordinate of the spiral sphere at the fast speed $c$ gives a shape that appears as an hourglass from one direction and as a circle from the other two.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{8}
$$

*Equation 9, Bespoke Tornado.*
Setting the vertical coordinate of the spiral sphere to an affinely rescaled absolute sine gives a funnel the article calls a tornado.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left|\sin {c^0 t}\right| - 1 & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{9}
$$

*Equation 10, Bespoke Top or Turnip.*
Setting the vertical coordinate of the spiral sphere to a rescaled sine of half the slow angle gives a shape the article calls a top or turnip.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left(\sin {\frac {c^0 t} {2}}\right) - 1 & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{10}
$$

*Equation 11, Bespoke Upward Inner Spiral.*
Doubling the frequency of a vertical sine in the spiral sphere makes the curve rise through the centre, descend around the outside and rise through the centre again.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{11}
$$

*Equation 12, Bespoke Downward Inner Spiral.*
Negating the vertical coordinate of the upward inner spiral reverses its direction, so the curve descends from the centre and rises around the outside.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = -\left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{12}
$$

*Equation 13, Bespoke Tall Rounded Hill.*
Doubling the frequency of the vertical cosine in the spiral sphere gives a tall rounded hill.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{aligned} \\
\tag{13}
$$

*Equation 14, Bespoke Shape with Round, Square and Hourglass Projections.*
Replacing the slow sine in the second coordinate of the spiral sphere with a cosine gives a shape that the article reports is round in one plane, square in another and an hourglass in the third.

$$
\begin{aligned}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\cos {c^0 t}\right) \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\notag z & = \left(\cos {c^0 t}\right) \\
\end{aligned} \\
\tag{14}
$$

### Notation

- $t$, the single parameter that traces the curve, in radians
- $c$, the constant that sets the relative revolution speed of each layer, so that layer $n$ turns at speed $c^n$
- $\bbox[cyan] {\star}$, a marker on the coordinate modified from the spiral sphere

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### General Sources

- "Parametric Curves in 3D." n.d. Accessed October 25, 2026. [http://www.math.uri.edu/~bkaskosz/flashmo/parcur/][parametric]
- "Wolfram Alpha 3D Plot A." n.d.-a. Accessed October 25, 2026. [https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(9+t)sin(3+t)sin(1+t),+sin(9+t)sin(3+t)cos(1+t),+sin(9+t)cos(3+t)),+t%3D0..2pi][wolfram_3d_a]
- "Wolfram Alpha 3D Plot B." n.d.-b. Accessed October 25, 2026. [https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(1+t)sin(5+t)sin(25+t),+sin(1+t)sin(5+t)cos(25+t),+sin(1+t)cos(5+t)),+t%3D0..2pi][wolfram_3d_b]
- "Wolfram Alpha 3D Plot C." n.d.-c. Accessed October 25, 2026. [https://www.wolframalpha.com/input/?i=parametric+plot+%7C+sin(t)(sin(5+t)cos(25+t),+sin(5+t)sin(25+t)cos(t),+sin(t)cos(5+t)sin(25+t)),+t%3D0..2pi][wolfram_3d_c]

[parametric]: http://www.math.uri.edu/~bkaskosz/flashmo/parcur/
[wolfram_3d_a]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(9+t)sin(3+t)sin(1+t),+sin(9+t)sin(3+t)cos(1+t),+sin(9+t)cos(3+t)),+t%3D0..2pi
[wolfram_3d_b]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(1+t)sin(5+t)sin(25+t),+sin(1+t)sin(5+t)cos(25+t),+sin(1+t)cos(5+t)),+t%3D0..2pi
[wolfram_3d_c]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+sin(t)(sin(5+t)cos(25+t),+sin(5+t)sin(25+t)cos(t),+sin(t)cos(5+t)sin(25+t)),+t%3D0..2pi
