---
layout: post
mathjax: true
comments: true
title:  "Single Parameter Equation for a  Sphere"
date:   2016-09-02 10:48:07 +0000
categories: 3d parametric math
---
This post covers some equations I found when playing around with plotting 3D parametric trigonometric functions.
The goal was to create a sphere with one parameter.

This is a parametric equation for a single parameter "spiral" sphere.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^0 t}\right) \\
\notag t & \in \mathbb{R}, 0 \le t \le 2 \pi \\
\notag c & \in \mathbb{R}, 1 \le c \\
\end{align} \\
$$

This version gives a "beachball" sphere.

$$
\begin{align}
x & = \left(\sin {c^1 t}\right) \left(\sin {c^0 t}\right) \\
\notag y & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) \\
\end{align} \\
$$

$\bbox[cyan] {x = \sin t, y = \cos t}$ is the parametric equation for a circle.
$\bbox[cyan] {z = \cos t, x = y = \sin t}$ is just the circle again, but this adds a third dimension.
Another term $\bbox[cyan] {w = \cos t, x = y = z = \sin t}$ could probably be used for a 4D hypersphere.

$c^n$, a constant, is the relative revolution speed of each layer.
Increasing $c$ will add more revolutions when tracing the sphere.
This gives a better visual appearance.
The important thing is that one layer is moving relatively faster than the other.
If another layer were added, it would have have a speed of $c^2$.
The constants $c^0$ and $c^1$ are indeed 1 and $c$, respectively.

Any value can be used for $c$.
The "spiral" version starts to look like a sphere when $c$ is at least 12, and the "beachball" when $c$ is at least 6.
Values of less than one $\bbox[cyan] {\left| c \right| \lt 1}$ are relatively broken.
When $c=\infty$, the function *is* a sphere.
The "spiral" scans a complete circle from the top of the sphere to the bottom $\bbox[cyan] {z \in 1 \to -1}$,
and the "beachball" rotates a circle around the z axis.

The following equation is a solid 2D circle when $c$ is $\infty$.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{align} \\
$$

One of these is probably the equation for a solid sphere.

$$
\begin{align}
x & = \left(\sin {c^2 t}\right) \left(\cos {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^1 t}\right) \left(\cos {c^0 t}\right) \\
\end{align} \\
$$

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\sin {c^2 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \left(\cos {c^2 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\end{align} \\
$$

A circle is formed in the xy, xy and yz planes.
xy is traced faster than xz, and xz faster than xy.
This may not actually be a volume filled sphere.
The free online 3D plotting tools are not very good for visualizing something like this.

The function for the spiral sphere can be modified to get different shapes.
$\bbox[cyan] {\star}$ is used to indicate modifications to the spiral sphere.

An hourglass.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {c^0 t}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

Rounded hourglass.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {\frac {c^0 t} {2}}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

An hourglass from one directection and a circle from the other two.
$cos$ or $sin$ can be used for $z$.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

A tornado.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left|\sin {c^0 t}\right| - 1 & \bbox[cyan] {\star} \\
\end{align} \\
$$

Top or turnip.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = 2 \left(\sin {\frac {c^0 t} {2}}\right) - 1 & \bbox[cyan] {\star} \\
\end{align} \\
$$

This spirals up from the inside center, down around the outside, and then in up through the center.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

This spirals down from the center and up around the outside instead.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = -\left(\sin {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

A tall rounded hill.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\sin {c^0 t}\right) \left(\cos {c^1 t}\right) \\
\notag z & = \left(\cos {2 c^0 t}\right) & \bbox[cyan] {\star} \\
\end{align} \\
$$

This strange shape is round when plotted in xz, a square in xy, and an hourglass in yz.

$$
\begin{align}
x & = \left(\sin {c^0 t}\right) \left(\sin {c^1 t}\right) \\
\notag y & = \left(\cos {c^0 t}\right) \left(\cos {c^1 t}\right) & \bbox[cyan] {\star} \\
\notag z & = \left(\cos {c^0 t}\right) \\
\end{align} \\
$$

## Links:

- [Parametric Curves in 3D][parametric]
- [Wolfram Alpha 3D Plot A][wolfram-3d-a]
- [Wolfram Alpha 3D Plot B][wolfram-3d-b]
- [Wolfram Alpha 3D Plot C][wolfram-3d-c]

[parametric]: http://www.math.uri.edu/~bkaskosz/flashmo/parcur/
[wolfram-3d-a]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(9+t)sin(3+t)sin(1+t),+sin(9+t)sin(3+t)cos(1+t),+sin(9+t)cos(3+t)),+t%3D0..2pi
[wolfram-3d-b]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+(sin(1+t)sin(5+t)sin(25+t),+sin(1+t)sin(5+t)cos(25+t),+sin(1+t)cos(5+t)),+t%3D0..2pi
[wolfram-3d-c]: https://www.wolframalpha.com/input/?i=parametric+plot+%7C+sin(t)(sin(5+t)cos(25+t),+sin(5+t)sin(25+t)cos(t),+sin(t)cos(5+t)sin(25+t)),+t%3D0..2pi

