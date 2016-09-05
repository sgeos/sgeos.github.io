---
layout: post
mathjax: true
comments: true
title:  "Trigonometry"
date:   2016-09-03 19:48:34 +0000
categories: math trigonometry
---
A list of trigonometric formulae and tables.

Trigonometric functions in polar coordinate form- radius $\rho$, azimuth $\phi$.
Hypotenuse is $\rho$, adjacent is x and opposite is y.

$$
\begin{align}
& \sin {\phi} = \left( \frac {1} {\csc {\phi}} \right) = \left( \frac {y} {\rho} \right) & \left( \arcsin \frac {y} {\rho} \right) = \left( \sin ^{-1} \frac {y} {\rho} \right) = {\phi} \\
& \cos {\phi} = \left( \frac {1} {\sec {\phi}} \right) = \left( \frac {x} {\rho} \right) & \left( \arccos \frac {x} {\rho} \right) = \left( \cos ^{-1} \frac {x} {\rho} \right) = {\phi} \\
& \tan {\phi} = \left( \frac {1} {\cot {\phi}} \right) = \left( \frac {y} {x} \right) & \left( \arctan \frac {y} {x} \right) = \left( \tan ^{-1} \frac {y} {x} \right) = {\phi} \\
& \ csc {\phi} = \left( \frac {1} {\sin {\phi}} \right) = \left( \frac {\rho} {y} \right) & \left( \operatorname{arccsc} \frac {\rho} {y} \right) = \left( \ csc ^{-1} \frac {\rho} {y} \right) = {\phi} \\
& \sec {\phi} = \left( \frac {1} {\cos {\phi}} \right) = \left( \frac {\rho} {x} \right) & \left( \operatorname{arcsec} \frac {\rho} {x} \right) = \left( \sec ^{-1} \frac {\rho} {x} \right) = {\phi} \\
& \cot {\phi} = \left( \frac {1} {\tan {\phi}} \right) = \left( \frac {x} {y} \right) & \left( \operatorname{arccot} \frac {x} {y} \right) = \left( \cot ^{-1} \frac {x} {y} \right) = {\phi} \\
& x = \rho \cos \phi \\
& y = \rho \sin \phi \\
& \rho = \sqrt {x^2 + y^2} \\
& \phi = \arctan {\frac {y} {x}} & \phi = \operatorname{atan2}(y,x) \\
\end{align}
$$

Trigonometric function values as a function of $\phi$.
If the point is 0 or $\infty$, the $\pm$ and $\mp$ signs indicate the
value of the function to either side of the specified point.
Lower values of $\phi$ indicated by the sign on the top.

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

Domain and range tables.
Note that the range of the inverse trigonometric functions starts at either $-\frac \pi 2$ or 0, depending on the function.

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
\cos^{-1} & \left[-1, +1\right] & \left[0,+\pi\right] \\
\tan^{-1} & \left(-\infty, +\infty\right) & \left(-\frac \pi 2,+\frac \pi 2\right) \\
\csc^{-1} & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) & \left[-\frac \pi 2,0\right) \cup \left(0,+\frac \pi 2\right] \\
\sec^{-1} & \left(-\infty,-1\right] \cup \left[+1,+\infty\right) & \left[0, +\frac \pi 2\right) \cup \left(+\frac \pi 2,\pi\right] \\
\cot^{-1} & \left(-\infty, +\infty\right) & \left(0,+\pi\right) \\
\end{array}
$$

Trigonometric identities.

$$
\begin{align}
& \cos (a) \cos (b) = \left( \frac {\cos (a+b) + \cos (a-b)} {2} \right) \\
& \sin (a) \sin (b) = \left( \frac {\cos (a-b) - \cos (a+b)} {2} \right) \\
& \sin (a) \cos (b) = \left( \frac {\sin (a+b) + \sin (a-b)} {2} \right) \\
& \cos (a) \sin (b) = \left( \frac {\sin (a+b) - \sin (a-b)} {2} \right) \\
& \cos (a) \sin (b) = \sin (b) \cos (a) \\
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

Polar form of a complex number.

$$
\begin{align}
& z = a + bi \\
& z = \rho \cos \phi + (\rho \sin \phi)i \\
& z = \rho (\cos \phi + i \sin \phi) \\
& \rho = |z| = \sqrt {a^2 + b^2} \\
& a = \rho \cos \phi \\
& b = \rho \sin \phi \\
& \phi = \tan^{-1} \left( \frac b a \right), 0 \le a \\
& \phi = \tan^{-1} \left( \frac b a \right) + \pi, a \lt 0 \\
\end{align}
$$

Triangulation.
Angles from two locations- $\phi$, $\theta$.
Baseline distance between locations- $\rho$.
Shortest distance from baseline to target object- $y$.
Distance along baseline from respective measuring points to point in front of
target object- $x_\phi$, $x_\theta$.
Distance from respective measuring points to target object- $d_\phi$, $d_\theta$.
**NOTE:** $\phi$ and $\theta$ are interior angles.

$$
\begin{align}
& y = \rho \sin \phi \sin \theta \csc (\phi + \theta) & y = \left( \frac {\rho \sin \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\phi = \rho \cos \phi \sin \theta \csc (\phi + \theta) & x_\phi = \left( \frac {\rho \cos \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\theta = \rho \sin \phi \cos \theta \csc (\phi + \theta) & x_\theta = \left( \frac {\rho \sin \phi \cos \theta} {\sin (\phi + \theta)} \right) \\
& d_\phi = \rho \sin \theta \csc (\phi + \theta) & d_\phi = \left( \frac {\rho \sin \theta} {\sin (\phi + \theta)} \right) \\
& d_\theta = \rho \sin \phi \csc (\phi + \theta) & d_\theta = \left( \frac {\rho \sin \phi} {\sin (\phi + \theta)} \right) \\
& \theta = \pi - \theta_{\text{exterior angle}} \\
\end{align}
$$

Tangent line on circle of radius $\rho$ at angle $\phi$, simple rotations and mirrors.

$$
\begin{align}
& y = -\cot^{-1}\phi (x - \rho \cos \phi) + \rho \sin \phi & \text{$\phi$ tangent line} \\
& y = \tan^{-1}\phi (x + \rho \sin \phi) + \rho \cos \phi & \text{$\phi+\frac {\pi} {2}$ tangent line, quarter revolution CCW} \\
& y = \tan^{-1}\phi (x - \rho \sin \phi) - \rho \cos \phi & \text{$\phi-\frac {\pi} {2}$ tangent line, quarter revolution CW} \\
& y = -\cot^{-1}\phi (x + \rho \cos \phi) - \rho \sin \phi & \text{$\phi \pm\pi$ tangent line, half revolution} \\
& y = \cot^{-1}\phi (x + \rho \cos \phi) + \rho \sin \phi & \text{$\pi-\phi$ tangent line, mirror along $y=0$} \\
& y = \cot^{-1}\phi (x - \rho \cos \phi) - \rho \sin \phi & \text{$-\phi$ tangent line, mirror along $x=0$} \\
& y = -\tan^{-1}\phi (x - \rho \sin \phi) + \rho \cos \phi & \text{$\frac {\pi} {2} - \phi$ or $-\frac {3\pi} {2} - \phi$ TL, mirror along $y=x$} \\
& y = -\tan^{-1}\phi (x + \rho \sin \phi) - \rho \cos \phi & \text{$\frac {3\pi} {2} - \phi$ or $-\frac {\pi} {2} - \phi$ TL, mirror along $y=-x$} \\
\end{align}
$$

## Links:

- [Wikipedia, List of Trigonometric Identities][wiki-trig]
- [Wikipedia, Polar Coordinate System][wiki-polar]
- [Wikipedia, Spherical Coordinate System][wiki-sphere]
- [Domain and Range of the Trigonometric Functions][trig-range]
- [Trigonometric Identities][trig-ident]
- [Product and Sum Formulas][trig-sum]
- [Polar Form of a Complex Number][polar-complex]
- [WolframAlpha, Plot][wolfram-alpha]
- [WolframAlpha, Parametric Plot][wolfram-alpha-param]
- [WolframAlpha, Polar Plot][wolfram-alpha-polar]
- [WolframAlpha, Multi Function Plot][wolfram-alpha-multi]
- [MathJax Preview][mathjax-preview]

[wiki-trig]: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
[wiki-polar]: https://en.wikipedia.org/wiki/Polar_coordinate_system
[wiki-sphere]: https://en.wikipedia.org/wiki/Spherical_coordinate_system#Cartesian_coordinates
[trig-range]: http://users.math.msu.edu/users/systeven/mth103/t3.7.pdf
[trig-ident]: http://math2.org/math/trig/identities.htm
[trig-sum]: http://www.sosmath.com/trig/prodform/prodform.html
[polar-complex]: http://hotmath.com/hotmath_help/topics/polar-form-of-a-complex-number.html
[wolfram-alpha]: http://www.wolframalpha.com/input/?i=csc+x+-+sec+x,+-pi+%3C%3D+x+%3C%3D+pi
[wolfram-alpha-param]: http://www.wolframalpha.com/input/?i=parametric+plot+(cot+t,+(t%2Fpi)+tan+t),+-2pi+%3C%3D+t+%3C%3D+2pi
[wolfram-alpha-polar]: http://www.wolframalpha.com/input/?i=polar+plot+r%3Dcot(phi)+*+tan(phi)+%2B+phi+%2F+pi,+-pi+%3C%3D+phi+%3C%3D+pi
[wolfram-alpha-multi]: https://www.wolframalpha.com/input/?i=Plot%5B%7Bx%5E2%2By%5E2%3D5%5E2,y%3D-atan(pi%2F6)(x-(5+sin+(pi%2F6)))+%2B+(5+cos+(pi%2F6)),y%3D-atan(pi%2F6)(x%2B(5+sin+(pi%2F6)))+-+(5+cos+(pi%2F6))%7D%5D
[mathjax-preview]: https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html

