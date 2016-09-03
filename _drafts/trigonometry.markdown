---
layout: post
mathjax: true
comments: true
title:  "Trigonometry"
date:   2016-09-03 19:48:34 +0000
categories: math trigonometry
---
A list of trigonometric formulae and tables.

Trigonometric functions.

$$
\begin{align}
& \sin {\theta} = \left( \frac {1} {\csc {\theta}} \right) = \left( \frac {o} {h} \right) & \left( \arcsin \frac {o} {h} \right) = \left( \sin ^{-1} \frac {o} {h} \right) = {\theta} \\
& \cos {\theta} = \left( \frac {1} {\sec {\theta}} \right) = \left( \frac {a} {h} \right) & \left( \arccos \frac {a} {h} \right) = \left( \cos ^{-1} \frac {a} {h} \right) = {\theta} \\
& \tan {\theta} = \left( \frac {1} {\cot {\theta}} \right) = \left( \frac {o} {a} \right) & \left( \arctan \frac {o} {a} \right) = \left( \tan ^{-1} \frac {o} {a} \right) = {\theta} \\
& \ csc {\theta} = \left( \frac {1} {\sin {\theta}} \right) = \left( \frac {h} {o} \right) & \left( arccsc \frac {h} {o} \right) = \left( \ csc ^{-1} \frac {h} {o} \right) = {\theta} \\
& \sec {\theta} = \left( \frac {1} {\cos {\theta}} \right) = \left( \frac {h} {a} \right) & \left( arcsec \frac {h} {a} \right) = \left( \sec ^{-1} \frac {h} {a} \right) = {\theta} \\
& \cot {\theta} = \left( \frac {1} {\tan {\theta}} \right) = \left( \frac {a} {o} \right) & \left( arccot \frac {a} {o} \right) = \left( \cot ^{-1} \frac {a} {o} \right) = {\theta} \\
\end{align}
$$

Trigonometric function values as a function of $\phi$.
If the point is 0 or $\infty$, the $\pm$ and $\mp$ signs indicate the
value of the function to either side of the specified point.
Lowers values of $\phi$ indicated by the sign on the top.

$$
\begin{array}{c|lcr}
\phi & \sin & \cos & \tan & \csc & \sec & \cot \\
\hline
\frac {0} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\frac {1} {2} \pi & +1 & \pm0 & \pm\infty & +1 & \pm\infty & \pm0 \\
\frac {2} {2} \pi & \pm0 & -1 & \mp0 & \pm\infty & -1 & \mp\infty \\
\frac {3} {2} \pi & -1 & \mp0 & \pm\infty & -1 & \mp\infty & \pm0 \\
\frac {4} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\end{array} \\
$$

Transposed version.

$$
\begin{array}{c|lcr}
\phi & \frac {0} {2} \pi & \frac {1} {2} \pi & \frac {2} {2} \pi & \frac {3} {2} \pi & \frac {4} {2} \pi \\
\hline
\sin & \mp0 & +1 & \pm0 & -1 & \mp0 \\
\cos & +1 & \pm0 & -1 & \mp0 & +1 \\
\tan & \mp0 & \pm\infty & \mp0 & \pm\infty & \mp0 \\
\csc & \mp\infty & +1 & \pm\infty & -1 & \mp\infty \\
\sec & +1 & \pm\infty & -1 & \mp\infty & +1 \\
\cot & \mp\infty & \pm0 & \mp\infty & \pm0 & \mp\infty \\
\end{array}
$$

Domain and range tables.  Range of inverse trigonometric functions may be $\left[-\frac \pi 2,+\frac \pi 2\right]$ or $\left[0,+\pi\right]$ with discontinuities, if present, at $0$ or $\pm\frac \pi 2$.

$$
\begin{array}{c|lcr}
\text{Function} & \text{Domain} & \text{Range} \\
\hline
\sin & \left(-\infty,+\infty\right) & \left[-1, +1\right] \\
\cos & \left(-\infty,+\infty\right) & \left[-1, +1\right] \\
\tan & \bigcup\limits_{k \in \mathbb{Z}} \left(\frac{(2k+1)\pi} {2},\frac{(2k+3)\pi} {2}\right) & \left(-\infty, +\infty\right) \\
\csc & \bigcup\limits_{k \in \mathbb{Z}} \left(k\pi,(k+1)\pi\right) & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) \\
\sec & \bigcup\limits_{k \in \mathbb{Z}} \left(\frac{(2k+1)\pi} {2},\frac{(2k+3)\pi} {2}\right) & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) \\
\cot & \bigcup\limits_{k \in \mathbb{Z}} \left(k\pi,(k+1)\pi\right) & \left(-\infty, +\infty\right) \\
\hline
\sin^{-1} & \left[-1, +1\right] & \left[-\frac \pi 2,+\frac \pi 2\right]\\
\cos^{-1} & \left[-1, +1\right] & \left[-\frac \pi 2,+\frac \pi 2\right] \\
\tan^{-1} & \left(-\infty, +\infty\right) & \left(-\frac \pi 2,+\frac \pi 2\right) \\
\csc^{-1} & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) & \left[-\frac \pi 2,0\right) \cup \left(0,+\frac \pi 2\right] \\
\sec^{-1} & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) & \left(-\frac \pi 2,+\frac \pi 2\right) \\
\cot^{-1} & \left(-\infty, +\infty\right) & \left[-\frac \pi 2,0\right) \cup \left(0,+\frac \pi 2\right] \\
\end{array}
$$

Polar coordinates- radius $\rho$, azimuth $\phi$.

$$
\begin{align}
& x = \rho \cos \phi \\
& y = \rho \sin \phi \\
& \rho = \sqrt {x^2 + y^2} \\
& \phi = \arctan {\frac {y} {x}} \\
\end{align}
$$

Spherical coordinates- radius $\rho$, inclination $\theta$, azimuth $\phi$.

$$
\begin{align}
& x = \rho \sin \theta \cos \phi \\
& y = \rho \sin \theta \sin \phi \\
& z = \rho \cos \theta \\
& \rho = \sqrt {x^2 + y^2 + z^2} \\
& \theta = \arccos {\frac {z} {\sqrt {x^2 + y^2 + z^2}}} = \arccos  {\frac {z} {\rho}} \\
& \phi = \arctan {\frac {y} {x}} \\
\end{align}
$$

## Links:

- [Wikipedia, List of Trigonometric Identities][wiki-trig]
- [Wikipedia, Polar Coordinate System][wiki-polar]
- [Wikipedia, Spherical Coordinate System][wiki-sphere]
- [WolframAlpha][wolfram-alpha]
- [MathJax Preview][mathjax-preview]

[wiki-trig]: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
[wiki-polar]: https://en.wikipedia.org/wiki/Polar_coordinate_system
[wiki-sphere]: https://en.wikipedia.org/wiki/Spherical_coordinate_system#Cartesian_coordinates
[wolfram-alpha]: http://www.wolframalpha.com/input/?i=y+%3D+cot+x,+0+%3C%3D+x+%3C%3D+2+pi
[mathjax-preview]: https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html

