---
layout: post
mathjax: true
comments: true
title:  "Trigonometry"
date:   2016-09-03 19:48:34 +0000
categories: math trigonometry
---

<!-- A42 -->
<script>console.log("A42");</script>

A list of trigonometric formulae and tables.

![image of arc length]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_002.png)
![image of circumference]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_001.png)

Trigonometric functions in polar coordinate form- radius $\rho$, azimuth $\phi$.
Hypotenuse is $\rho$, adjacent is x and opposite is y.

$$
\begin{aligned}
& y = \rho \sin \phi \\
& x = \rho \cos \phi \\
& \rho = \sqrt {x^2 + y^2} \\
& \phi = \arctan {\frac {y} {x}} & \phi = \operatorname{atan2}(y,x) \\
\end{aligned}
\tag{1}
$$

![image of sin and cos]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_003.png)

$\sin \phi$ and $\cos \phi$ get the $y$ and $x$ components of $\rho$.

$$
\begin{aligned}
& \sin {\phi} = \left( \frac {1} {\csc {\phi}} \right) = \left( \frac {y} {\rho} \right) & \left( \arcsin \frac {y} {\rho} \right) = \left( \sin ^{-1} \frac {y} {\rho} \right) = {\phi} \\
& \cos {\phi} = \left( \frac {1} {\sec {\phi}} \right) = \left( \frac {x} {\rho} \right) & \left( \arccos \frac {x} {\rho} \right) = \left( \cos ^{-1} \frac {x} {\rho} \right) = {\phi} \\
\end{aligned}
\tag{2}
$$

![image of sec and tan]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_004.png)

$\tan \phi$ and $\sec \phi$ get $y$ and $\rho$ from $x$.

$$
\begin{aligned}
& \tan {\phi} = \left( \frac {1} {\cot {\phi}} \right) = \left( \frac {y} {x} \right) & \left( \arctan \frac {y} {x} \right) = \left( \tan ^{-1} \frac {y} {x} \right) = {\phi} \\
& \sec {\phi} = \left( \frac {1} {\cos {\phi}} \right) = \left( \frac {\rho} {x} \right) & \left( \operatorname{arcsec} \frac {\rho} {x} \right) = \left( \sec ^{-1} \frac {\rho} {x} \right) = {\phi} \\
\end{aligned}
\tag{3}
$$

![image of csc and cot]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_005.png)

$\cot \phi$ and $\csc \phi$ get $x$ and $\rho$ from $y$.

$$
\begin{aligned}
& \cot {\phi} = \left( \frac {1} {\tan {\phi}} \right) = \left( \frac {x} {y} \right) & \left( \operatorname{arccot} \frac {x} {y} \right) = \left( \cot ^{-1} \frac {x} {y} \right) = {\phi} \\
& \ csc {\phi} = \left( \frac {1} {\sin {\phi}} \right) = \left( \frac {\rho} {y} \right) & \left( \operatorname{arccsc} \frac {\rho} {y} \right) = \left( \ csc ^{-1} \frac {\rho} {y} \right) = {\phi} \\
\end{aligned}
\tag{4}
$$

Trigonometric function values as a function of $\phi$.
If the point is 0 or $\infty$, the $\pm$ and $\mp$ signs indicate the
value of the function to either side of the specified point.
Lower values of $\phi$ indicated by the sign on the top.

$$
\begin{array}{c|cccccc}
\phi & \sin & \cos & \tan & \csc & \sec & \cot \\
\hline
\frac {0} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\frac {1} {2} \pi & +1 & \pm0 & \pm\infty & +1 & \pm\infty & \pm0 \\
\frac {2} {2} \pi & \pm0 & -1 & \mp0 & \pm\infty & -1 & \mp\infty \\
\frac {3} {2} \pi & -1 & \mp0 & \pm\infty & -1 & \mp\infty & \pm0 \\
\frac {4} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\end{array} \\
\tag{5}
$$

Transposed version.

$$
\begin{array}{c|ccccc}
\phi & \frac {0} {2} \pi & \frac {1} {2} \pi & \frac {2} {2} \pi & \frac {3} {2} \pi & \frac {4} {2} \pi \\
\hline
\sin & \mp0 & +1 & \pm0 & -1 & \mp0 \\
\cos & +1 & \pm0 & -1 & \mp0 & +1 \\
\tan & \mp0 & \pm\infty & \mp0 & \pm\infty & \mp0 \\
\csc & \mp\infty & +1 & \pm\infty & -1 & \mp\infty \\
\sec & +1 & \pm\infty & -1 & \mp\infty & +1 \\
\cot & \mp\infty & \pm0 & \mp\infty & \pm0 & \mp\infty \\
\end{array}
\tag{6}
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
\tag{7}
$$

Reciprocal and quotient identities.

$$
\begin{aligned}
& \tan = \left( \frac {1} {\cot \phi} \right) = \left( \frac {\sin \phi} {\cos \phi} \right) = \left( \frac {\sec \phi} {\csc \phi} \right) = \sin \phi \cdot \sec \phi = \left( \frac {1} {\csc \phi \cdot \cos \phi} \right) =\left( \frac {y} {\rho} \cdot  \frac {\rho} {x} \right) = \left( \frac {y} {x} \right) \\
& \cot = \left( \frac {1} {\tan \phi} \right) = \left( \frac {\cos \phi} {\sin \phi} \right) = \left( \frac {\csc \phi} {\sec \phi} \right) = cos \phi \cdot \csc \phi = \left( \frac {1} {\sec \phi \cdot \sin \phi} \right) = \left( \frac {x} {\rho} \cdot \frac { \rho} {y} \right) = \left( \frac {x} {y} \right) \\
& \sin = \left( \frac {1} {\csc \phi} \right) = \left( \frac {\tan \phi} {\sec \phi} \right) = \left( \frac {\cos \phi} {\cot \phi} \right) = \tan \phi \cdot \cos \phi = \left( \frac {1} {\cot \phi \cdot \sec \phi} \right) = \left( \frac {y} {x} \cdot \frac {x} {\rho} \right) = \left( \frac {y} {\rho} \right) \\
& \csc = \left( \frac {1} {\sin \phi} \right) = \left( \frac {\sec \phi} {\tan \phi} \right) = \left( \frac {\cot \phi} {\cos \phi} \right) = \sec \phi \cdot \cot \phi = \left( \frac {1} {\cos \phi \cdot \tan \phi} \right) = \left( \frac {\rho} {x} \cdot \frac {x} {y} \right) = \left( \frac {\rho} {y} \right) \\
& \cos = \left( \frac {1} {\sec \phi} \right) = \left( \frac {\cot \phi} {\csc \phi} \right) = \left( \frac {\sin \phi} {\tan \phi} \right) = \cot \phi \cdot \sin \phi = \left( \frac {1} {\tan \phi \cdot \csc \phi} \right) = \left( \frac {x} {y} \cdot \frac {y} {\rho} \right) = \left( \frac {x} {\rho} \right) \\
& \sec = \left( \frac {1} {\cos \phi} \right) = \left( \frac {\csc \phi} {\cot \phi} \right) = \left( \frac {\tan \phi} {\sin \phi} \right) = \csc \phi \cdot \tan \phi = \left( \frac {1} {\sin \phi \cdot \cot \phi} \right) = \left( \frac {\rho} {y} \cdot \frac {y} {x} \right) = \left( \frac {\rho} {x} \right) \\
\end{aligned}
\tag{8}
$$

Cofunction identities.  All take the form $\operatorname{f} \left( \frac {\pi} {2} - {\phi} \right) = \operatorname{cof} {\phi}$ and vice versa.

$$
\begin{aligned}
& \sin \left( \frac {\pi} {2} - {\phi} \right) = \cos {\phi} & \cos \left( \frac {\pi} {2} - {\phi} \right) = \sin {\phi} \\
& \tan \left( \frac {\pi} {2} - {\phi} \right) = \cot {\phi} & \cot \left( \frac {\pi} {2} - {\phi} \right) = \tan {\phi} \\
& \sec \left( \frac {\pi} {2} - {\phi} \right) = \csc {\phi} & \csc \left( \frac {\pi} {2} - {\phi} \right) = \sec {\phi} \\
\end{aligned}
\tag{9}
$$

Odd and even function identities.  $\cos$ and $\sec$ are even.  The rest are odd.

$$
\begin{aligned}
& \sin ({- \phi}) = - \sin ({\phi}) & \csc ({- \phi}) = - \csc ({\phi}) \\
& \cos ({- \phi}) = \cos ({\phi}) & \sec ({- \phi}) = \sec ({\phi}) \\
& \tan ({- \phi}) = - \tan ({\phi}) & \cot ({- \phi}) = - \cot ({\phi}) \\
\end{aligned}
\tag{10}
$$

Pythagorean identities.  These cover all three sets of functions.

$$
\begin{aligned}
& \sin^2 \phi + \cos^2 \phi = 1 \\
& 1 + \tan^2 \phi = \sec^2 \phi \\
& 1 + \cot^2 \phi = \csc^2 \phi \\
\end{aligned}
\tag{11}
$$

Trigonometric identities.

$$
\begin{aligned}
& \cos (\phi) \cos (\theta) = \left( \frac {\cos (\phi+\theta) + \cos (\phi-\theta)} {2} \right) \\
& \sin (\phi) \sin (\theta) = \left( \frac {\cos (\phi-\theta) - \cos (\phi+\theta)} {2} \right) \\
& \sin (\phi) \cos (\theta) = \left( \frac {\sin (\phi+\theta) + \sin (\phi-\theta)} {2} \right) \\
& \cos (\phi) \sin (\theta) = \left( \frac {\sin (\phi+\theta) - \sin (\phi-\theta)} {2} \right) \\
& \cos (\phi) \sin (\theta) = \sin (\theta) \cos (\phi) \\
\\
& \sin (\phi) + \sin (\theta) = 2 \sin \left( \frac {\phi + \theta} {2} \right) \cos \left( \frac {\phi - \theta} {2} \right) \\
& \sin (\phi) - \sin (\theta) = 2 \cos \left( \frac {\phi + \theta} {2} \right) \sin \left( \frac {\phi - \theta} {2} \right) \\
& \cos (\phi) + \cos (\theta) = 2 \cos \left( \frac {\phi + \theta} {2} \right) \cos \left( \frac {\phi - \theta} {2} \right) \\
& \cos (\phi) - \cos (\theta) = -2 \sin \left( \frac {\phi + \theta} {2} \right) \sin \left( \frac {\phi - \theta} {2} \right) \\
\end{aligned}
\tag{12}
$$

Sum and difference formulas.

$$
\begin{aligned}
& \sin(\phi + \theta) = \sin\phi \cos\theta + \cos\phi \sin\theta \\
& \sin(\phi - \theta) = \sin\phi \cos\theta - \cos\phi \sin\theta \\
& \cos(\phi + \theta) = \cos\phi \cos\theta - \sin\phi \sin\theta \\
& \cos(\phi - \theta) = \cos\phi \cos\theta + \sin\phi \sin\theta \\
& \tan(\phi + \theta) = \left( \frac {\tan\phi + \tan\theta} {1 - \tan\phi\tan\theta} \right) \\
& \tan(\phi - \theta) = \left( \frac {\tan\phi - \tan\theta} {1 + \tan\phi\tan\theta} \right) \\
\end{aligned}
\tag{13}
$$

Double angle identities.

$$
\begin{aligned}
& \sin(2 \phi) = 2 \sin\phi \cos\phi \\
& \cos(2 \phi) = \cos^2 \phi - \sin^2 \phi \\
& \cos(2 \phi) = 2 \cos^2 \phi - 1 \\
& \cos(2 \phi) = 1 - 2 \sin^2 \phi \\
& \tan(2 \phi) = \left( \frac {2 \tan \phi} {1 - \tan^2 \phi} \right) \\
\end{aligned}
\tag{14}
$$

Half angle identities.

$$
\begin{aligned}
& \sin \left( \frac {\phi} {2} \right) = \left( \frac {1} {\csc (\phi / 2)} \right) = \pm \sqrt{ \frac {1 - \cos \phi} {2} } \\
& \cos \left( \frac {\phi} {2} \right) = \left( \frac {1} {\sec (\phi / 2)} \right) = \pm \sqrt{ \frac {1 + \cos \phi} {2} } \\
& \tan \left( \frac {\phi} {2} \right) = \left( \frac {1} {\cot (\phi / 2)} \right) = \frac {\sin \phi} {1 + \cos \phi} = \frac {1 - \cos \phi} {\sin \phi} \\
& \csc \left( \frac {\phi} {2} \right) = \left( \frac {1} {\sin (\phi / 2)} \right) = \pm \sqrt{ \frac {2} {1 - \cos \phi} } \\
& \sec \left( \frac {\phi} {2} \right) = \left( \frac {1} {\cos (\phi / 2)} \right) = \pm \sqrt{ \frac {2} {1 + \cos \phi} } \\
& \cot \left( \frac {\phi} {2} \right) = \left( \frac {1} {\tan (\phi / 2)} \right) = \frac {1 + \cos \phi} {\sin \phi} = \frac {\sin \phi} {1 - \cos \phi} \\
\end{aligned}
\tag{15}
$$

Power reducing identities.

$$
\begin{aligned}
& \sin^2 \phi = \left( \frac {1} {csc^2 \phi} \right) = \left( \frac {1 - \cos 2\phi} {2} \right) \\
& \cos^2 \phi = \left( \frac {1} {sec^2 \phi} \right) = \left( \frac {1 + \cos 2\phi} {2} \right) \\
& \tan^2 \phi = \left( \frac {1} {cot^2 \phi} \right) = \left( \frac {1 - \cos 2\phi} {1 + \cos 2\phi} \right) \\
& \csc^2 \phi = \left( \frac {1} {sin^2 \phi} \right) = \left( \frac {2} {1 - \cos 2\phi} \right) \\
& \sec^2 \phi = \left( \frac {1} {cos^2 \phi} \right) = \left( \frac {2} {1 + \cos 2\phi} \right) \\
& \cot^2 \phi = \left( \frac {1} {tan^2 \phi} \right) = \left( \frac {1 + \cos 2\phi} {1 - \cos 2\phi} \right) \\
\end{aligned}
\tag{16}
$$

Spherical coordinates- radius $\rho$, inclination $\theta$, azimuth $\phi$.

$$
\begin{aligned}
& x = \rho \sin \theta \cos \phi \\
& y = \rho \sin \theta \sin \phi \\
& z = \rho \cos \theta \\
& \rho = \sqrt {x^2 + y^2 + z^2} \\
& \theta = \arccos {\frac {z} {\sqrt {x^2 + y^2 + z^2}}} = \arccos  {\frac {z} {\rho}} \\
& \phi = \arctan {\frac {y} {x}} \\
\end{aligned}
\tag{17}
$$

Polar form of a complex number.

$$
\begin{aligned}
& z = a + bi \\
& z = \rho \cos \phi + (\rho \sin \phi)i \\
& z = \rho (\cos \phi + i \sin \phi) \\
& \rho = |z| = \sqrt {a^2 + b^2} \\
& a = \rho \cos \phi \\
& b = \rho \sin \phi \\
& \phi = \tan^{-1} \left( \frac b a \right), 0 \le a \\
& \phi = \tan^{-1} \left( \frac b a \right) + \pi, a \lt 0 \\
& z_1 z_2 = r_1 r_2 (\cos(\phi_1 +\phi_2) + i \sin(\phi_1 + \phi_2)) \\
& \left( \frac {z_1} {z_2} \right) =
  \left( \frac {r_1} {r_2} \right) (\cos(\phi_1 -\phi_2) + i \sin(\phi_1 - \phi_2)) \\
\end{aligned}
\tag{18}
$$

DeMoivre's Theorem.  $z^n$ is a complex number raised to the power of $n$.

$$
\begin{aligned}
&z^n = \left[\rho(\cos \phi + i \sin \phi)\right]^n = \rho^n \left(\cos(n\phi)+i \sin(n\phi)\right) \\
\end{aligned}
\tag{19}
$$

The nth root of a number.
There are $n$ complex roots for positive values of $n$.
$k$ is used to calculate each root in turn.

$$
\begin{aligned}
& z = \rho \left( \cos {\phi} + i \sin {\phi} \right) \\
& ^n\sqrt z_k = z^{1/n}_k = \rho^{1/n} \left( \cos \left( \frac {\phi} {n} + \frac {2\pi k} {n} \right) + i \sin \left( \frac {\phi} {n} + \frac {2\pi k} {n} \right) \right) & 0\lt n; k=0,1,2,\cdots,n-1\\
\end{aligned}
\tag{20}
$$

Orthogonal decomposition.

$$
\begin{aligned}
& \vec{v}^\parallel = \operatorname{proj}_{\vec \rho} \vec{v} = \left( \frac {\vec{v} \cdot \vec{\rho}} {\vec{\rho} \cdot \vec{\rho}}  \right) \vec {\rho} \\
& \vec{v}^\bot = \vec {v} - \vec{v}^\parallel \\
\end{aligned}
\tag{21}
$$

Triangulation.

![image of triangulation]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_006.png)
![image of triangualtion with obtuse angle]({{ site.url }}/assets/image/post_trigonometry/trig_diagrams_007.png)

Angles from two locations- $\phi$, $\theta$.
Baseline distance between locations- $\rho$.
Shortest distance from baseline to target object- $y$.
Distance along baseline from respective measuring points to point in front of
target object- $x_\phi$, $x_\theta$.
Distance from respective measuring points to target object- $d_\phi$, $d_\theta$.
**NOTE:** $\phi$ and $\theta$ are interior angles.

$$
\begin{aligned}
& y = \rho \sin \phi \sin \theta \csc (\phi + \theta) & y = \left( \frac {\rho \sin \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\phi = \rho \cos \phi \sin \theta \csc (\phi + \theta) & x_\phi = \left( \frac {\rho \cos \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\theta = \rho \sin \phi \cos \theta \csc (\phi + \theta) & x_\theta = \left( \frac {\rho \sin \phi \cos \theta} {\sin (\phi + \theta)} \right) \\
& d_\phi = \rho \sin \theta \csc (\phi + \theta) & d_\phi = \left( \frac {\rho \sin \theta} {\sin (\phi + \theta)} \right) \\
& d_\theta = \rho \sin \phi \csc (\phi + \theta) & d_\theta = \left( \frac {\rho \sin \phi} {\sin (\phi + \theta)} \right) \\
& \theta = \pi - \theta_{\text{exterior angle}} \\
\end{aligned}
\tag{22}
$$

Tangent line on circle of radius $\rho$ at angle $\phi$, simple rotations and mirrors.

$$
\begin{aligned}
& y = -\cot^{-1}\phi (x - \rho \cos \phi) + \rho \sin \phi & \text{$\phi$ tangent line} \\
& y = \tan^{-1}\phi (x + \rho \sin \phi) + \rho \cos \phi & \text{$\phi+\frac {\pi} {2}$ tangent line, quarter revolution CCW} \\
& y = \tan^{-1}\phi (x - \rho \sin \phi) - \rho \cos \phi & \text{$\phi-\frac {\pi} {2}$ tangent line, quarter revolution CW} \\
& y = -\cot^{-1}\phi (x + \rho \cos \phi) - \rho \sin \phi & \text{$\phi \pm\pi$ tangent line, half revolution} \\
& y = \cot^{-1}\phi (x + \rho \cos \phi) + \rho \sin \phi & \text{$\pi-\phi$ tangent line, mirror along $y=0$} \\
& y = \cot^{-1}\phi (x - \rho \cos \phi) - \rho \sin \phi & \text{$-\phi$ tangent line, mirror along $x=0$} \\
& y = -\tan^{-1}\phi (x - \rho \sin \phi) + \rho \cos \phi & \text{$\frac {\pi} {2} - \phi$ or $-\frac {3\pi} {2} - \phi$ TL, mirror along $y=x$} \\
& y = -\tan^{-1}\phi (x + \rho \sin \phi) - \rho \cos \phi & \text{$\frac {3\pi} {2} - \phi$ or $-\frac {\pi} {2} - \phi$ TL, mirror along $y=-x$} \\
\end{aligned}
\tag{23}
$$

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 23 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 23, 23 are established and 0 are bespoke.
Every angle is in radians, the radius $\rho$ is the hypotenuse of the reference triangle, and the inclination $\theta$ of spherical coordinates is measured from the positive $z$ axis while the azimuth $\phi$ is measured in the $xy$ plane.

**Equation 1, Polar Coordinates.**
A point at radius $\rho$ and azimuth $\phi$ has Cartesian components $\rho \cos \phi$ and $\rho \sin \phi$, and the inverse uses the two-argument arctangent to recover the quadrant.

$$
\begin{aligned}
& y = \rho \sin \phi \\
& x = \rho \cos \phi \\
& \rho = \sqrt {x^2 + y^2} \\
& \phi = \arctan {\frac {y} {x}} & \phi = \operatorname{atan2}(y,x) \\
\end{aligned}
\tag{1}
$$

**Equation 2, Sine and Cosine as Ratios with Their Inverses.**
The sine and cosine are the ratios of the opposite and adjacent sides to the hypotenuse, the reciprocals of the cosecant and secant, and their inverse functions return the angle.

$$
\begin{aligned}
& \sin {\phi} = \left( \frac {1} {\csc {\phi}} \right) = \left( \frac {y} {\rho} \right) & \left( \arcsin \frac {y} {\rho} \right) = \left( \sin ^{-1} \frac {y} {\rho} \right) = {\phi} \\
& \cos {\phi} = \left( \frac {1} {\sec {\phi}} \right) = \left( \frac {x} {\rho} \right) & \left( \arccos \frac {x} {\rho} \right) = \left( \cos ^{-1} \frac {x} {\rho} \right) = {\phi} \\
\end{aligned}
\tag{2}
$$

**Equation 3, Tangent and Secant as Ratios with Their Inverses.**
The tangent and secant are the ratios of the opposite side and of the hypotenuse to the adjacent side, and their inverse functions return the angle.

$$
\begin{aligned}
& \tan {\phi} = \left( \frac {1} {\cot {\phi}} \right) = \left( \frac {y} {x} \right) & \left( \arctan \frac {y} {x} \right) = \left( \tan ^{-1} \frac {y} {x} \right) = {\phi} \\
& \sec {\phi} = \left( \frac {1} {\cos {\phi}} \right) = \left( \frac {\rho} {x} \right) & \left( \operatorname{arcsec} \frac {\rho} {x} \right) = \left( \sec ^{-1} \frac {\rho} {x} \right) = {\phi} \\
\end{aligned}
\tag{3}
$$

**Equation 4, Cotangent and Cosecant as Ratios with Their Inverses.**
The cotangent and cosecant are the ratios of the adjacent side and of the hypotenuse to the opposite side, and their inverse functions return the angle.

$$
\begin{aligned}
& \cot {\phi} = \left( \frac {1} {\tan {\phi}} \right) = \left( \frac {x} {y} \right) & \left( \operatorname{arccot} \frac {x} {y} \right) = \left( \cot ^{-1} \frac {x} {y} \right) = {\phi} \\
& \ csc {\phi} = \left( \frac {1} {\sin {\phi}} \right) = \left( \frac {\rho} {y} \right) & \left( \operatorname{arccsc} \frac {\rho} {y} \right) = \left( \ csc ^{-1} \frac {\rho} {y} \right) = {\phi} \\
\end{aligned}
\tag{4}
$$

**Equation 5, Values of the Six Functions at Quarter Turns.**
The table gives each function at multiples of $\pi/2$, with the upper of a paired sign giving the side approached from smaller angles.

$$
\begin{array}{c|cccccc}
\phi & \sin & \cos & \tan & \csc & \sec & \cot \\
\hline
\frac {0} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\frac {1} {2} \pi & +1 & \pm0 & \pm\infty & +1 & \pm\infty & \pm0 \\
\frac {2} {2} \pi & \pm0 & -1 & \mp0 & \pm\infty & -1 & \mp\infty \\
\frac {3} {2} \pi & -1 & \mp0 & \pm\infty & -1 & \mp\infty & \pm0 \\
\frac {4} {2} \pi & \mp0 & +1 & \mp0 & \mp\infty & +1 & \mp\infty \\
\end{array} \\
\tag{5}
$$

**Equation 6, Transposed Values at Quarter Turns.**
The same quarter-turn values are set out with the functions as rows and the angles as columns.

$$
\begin{array}{c|ccccc}
\phi & \frac {0} {2} \pi & \frac {1} {2} \pi & \frac {2} {2} \pi & \frac {3} {2} \pi & \frac {4} {2} \pi \\
\hline
\sin & \mp0 & +1 & \pm0 & -1 & \mp0 \\
\cos & +1 & \pm0 & -1 & \mp0 & +1 \\
\tan & \mp0 & \pm\infty & \mp0 & \pm\infty & \mp0 \\
\csc & \mp\infty & +1 & \pm\infty & -1 & \mp\infty \\
\sec & +1 & \pm\infty & -1 & \mp\infty & +1 \\
\cot & \mp\infty & \pm0 & \mp\infty & \pm0 & \mp\infty \\
\end{array}
\tag{6}
$$

**Equation 7, Domains and Ranges of the Functions and Their Inverses.**
The table gives the domain and range of the six functions and the principal ranges of their inverses, which begin at $-\pi/2$ or at zero depending on the function.

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
\tag{7}
$$

**Equation 8, Reciprocal and Quotient Identities.**
Each of the six functions is written as the reciprocal of its partner, as quotients and products of the others, and as a ratio of the sides $x$, $y$ and $\rho$.

$$
\begin{aligned}
& \tan = \left( \frac {1} {\cot \phi} \right) = \left( \frac {\sin \phi} {\cos \phi} \right) = \left( \frac {\sec \phi} {\csc \phi} \right) = \sin \phi \cdot \sec \phi = \left( \frac {1} {\csc \phi \cdot \cos \phi} \right) =\left( \frac {y} {\rho} \cdot  \frac {\rho} {x} \right) = \left( \frac {y} {x} \right) \\
& \cot = \left( \frac {1} {\tan \phi} \right) = \left( \frac {\cos \phi} {\sin \phi} \right) = \left( \frac {\csc \phi} {\sec \phi} \right) = cos \phi \cdot \csc \phi = \left( \frac {1} {\sec \phi \cdot \sin \phi} \right) = \left( \frac {x} {\rho} \cdot \frac { \rho} {y} \right) = \left( \frac {x} {y} \right) \\
& \sin = \left( \frac {1} {\csc \phi} \right) = \left( \frac {\tan \phi} {\sec \phi} \right) = \left( \frac {\cos \phi} {\cot \phi} \right) = \tan \phi \cdot \cos \phi = \left( \frac {1} {\cot \phi \cdot \sec \phi} \right) = \left( \frac {y} {x} \cdot \frac {x} {\rho} \right) = \left( \frac {y} {\rho} \right) \\
& \csc = \left( \frac {1} {\sin \phi} \right) = \left( \frac {\sec \phi} {\tan \phi} \right) = \left( \frac {\cot \phi} {\cos \phi} \right) = \sec \phi \cdot \cot \phi = \left( \frac {1} {\cos \phi \cdot \tan \phi} \right) = \left( \frac {\rho} {x} \cdot \frac {x} {y} \right) = \left( \frac {\rho} {y} \right) \\
& \cos = \left( \frac {1} {\sec \phi} \right) = \left( \frac {\cot \phi} {\csc \phi} \right) = \left( \frac {\sin \phi} {\tan \phi} \right) = \cot \phi \cdot \sin \phi = \left( \frac {1} {\tan \phi \cdot \csc \phi} \right) = \left( \frac {x} {y} \cdot \frac {y} {\rho} \right) = \left( \frac {x} {\rho} \right) \\
& \sec = \left( \frac {1} {\cos \phi} \right) = \left( \frac {\csc \phi} {\cot \phi} \right) = \left( \frac {\tan \phi} {\sin \phi} \right) = \csc \phi \cdot \tan \phi = \left( \frac {1} {\sin \phi \cdot \cot \phi} \right) = \left( \frac {\rho} {y} \cdot \frac {y} {x} \right) = \left( \frac {\rho} {x} \right) \\
\end{aligned}
\tag{8}
$$

**Equation 9, Cofunction Identities.**
Each function of the complementary angle $\pi/2 - \phi$ equals its cofunction of $\phi$.

$$
\begin{aligned}
& \sin \left( \frac {\pi} {2} - {\phi} \right) = \cos {\phi} & \cos \left( \frac {\pi} {2} - {\phi} \right) = \sin {\phi} \\
& \tan \left( \frac {\pi} {2} - {\phi} \right) = \cot {\phi} & \cot \left( \frac {\pi} {2} - {\phi} \right) = \tan {\phi} \\
& \sec \left( \frac {\pi} {2} - {\phi} \right) = \csc {\phi} & \csc \left( \frac {\pi} {2} - {\phi} \right) = \sec {\phi} \\
\end{aligned}
\tag{9}
$$

**Equation 10, Odd and Even Function Identities.**
The cosine and secant are even functions of the angle, and the other four are odd.

$$
\begin{aligned}
& \sin ({- \phi}) = - \sin ({\phi}) & \csc ({- \phi}) = - \csc ({\phi}) \\
& \cos ({- \phi}) = \cos ({\phi}) & \sec ({- \phi}) = \sec ({\phi}) \\
& \tan ({- \phi}) = - \tan ({\phi}) & \cot ({- \phi}) = - \cot ({\phi}) \\
\end{aligned}
\tag{10}
$$

**Equation 11, Pythagorean Identities.**
The squares of sine and cosine sum to one, and dividing that identity by the square of the cosine or of the sine gives the other two.

$$
\begin{aligned}
& \sin^2 \phi + \cos^2 \phi = 1 \\
& 1 + \tan^2 \phi = \sec^2 \phi \\
& 1 + \cot^2 \phi = \csc^2 \phi \\
\end{aligned}
\tag{11}
$$

**Equation 12, Product to Sum and Sum to Product Identities.**
Products of sines and cosines of two angles are written as half sums or differences of functions of the sum and difference angles, and the reverse identities convert sums into products.

$$
\begin{aligned}
& \cos (\phi) \cos (\theta) = \left( \frac {\cos (\phi+\theta) + \cos (\phi-\theta)} {2} \right) \\
& \sin (\phi) \sin (\theta) = \left( \frac {\cos (\phi-\theta) - \cos (\phi+\theta)} {2} \right) \\
& \sin (\phi) \cos (\theta) = \left( \frac {\sin (\phi+\theta) + \sin (\phi-\theta)} {2} \right) \\
& \cos (\phi) \sin (\theta) = \left( \frac {\sin (\phi+\theta) - \sin (\phi-\theta)} {2} \right) \\
& \cos (\phi) \sin (\theta) = \sin (\theta) \cos (\phi) \\
\\
& \sin (\phi) + \sin (\theta) = 2 \sin \left( \frac {\phi + \theta} {2} \right) \cos \left( \frac {\phi - \theta} {2} \right) \\
& \sin (\phi) - \sin (\theta) = 2 \cos \left( \frac {\phi + \theta} {2} \right) \sin \left( \frac {\phi - \theta} {2} \right) \\
& \cos (\phi) + \cos (\theta) = 2 \cos \left( \frac {\phi + \theta} {2} \right) \cos \left( \frac {\phi - \theta} {2} \right) \\
& \cos (\phi) - \cos (\theta) = -2 \sin \left( \frac {\phi + \theta} {2} \right) \sin \left( \frac {\phi - \theta} {2} \right) \\
\end{aligned}
\tag{12}
$$

**Equation 13, Sum and Difference Formulas.**
The sine, cosine and tangent of a sum or difference of two angles are expressed through the functions of each angle.

$$
\begin{aligned}
& \sin(\phi + \theta) = \sin\phi \cos\theta + \cos\phi \sin\theta \\
& \sin(\phi - \theta) = \sin\phi \cos\theta - \cos\phi \sin\theta \\
& \cos(\phi + \theta) = \cos\phi \cos\theta - \sin\phi \sin\theta \\
& \cos(\phi - \theta) = \cos\phi \cos\theta + \sin\phi \sin\theta \\
& \tan(\phi + \theta) = \left( \frac {\tan\phi + \tan\theta} {1 - \tan\phi\tan\theta} \right) \\
& \tan(\phi - \theta) = \left( \frac {\tan\phi - \tan\theta} {1 + \tan\phi\tan\theta} \right) \\
\end{aligned}
\tag{13}
$$

**Equation 14, Double Angle Identities.**
Setting the two angles of the sum formulas equal gives the sine, cosine and tangent of twice an angle.

$$
\begin{aligned}
& \sin(2 \phi) = 2 \sin\phi \cos\phi \\
& \cos(2 \phi) = \cos^2 \phi - \sin^2 \phi \\
& \cos(2 \phi) = 2 \cos^2 \phi - 1 \\
& \cos(2 \phi) = 1 - 2 \sin^2 \phi \\
& \tan(2 \phi) = \left( \frac {2 \tan \phi} {1 - \tan^2 \phi} \right) \\
\end{aligned}
\tag{14}
$$

**Equation 15, Half Angle Identities.**
Each function of half an angle is written through the cosine and sine of the whole angle, with the sign of each square root set by the quadrant of $\phi/2$.

$$
\begin{aligned}
& \sin \left( \frac {\phi} {2} \right) = \left( \frac {1} {\csc (\phi / 2)} \right) = \pm \sqrt{ \frac {1 - \cos \phi} {2} } \\
& \cos \left( \frac {\phi} {2} \right) = \left( \frac {1} {\sec (\phi / 2)} \right) = \pm \sqrt{ \frac {1 + \cos \phi} {2} } \\
& \tan \left( \frac {\phi} {2} \right) = \left( \frac {1} {\cot (\phi / 2)} \right) = \frac {\sin \phi} {1 + \cos \phi} = \frac {1 - \cos \phi} {\sin \phi} \\
& \csc \left( \frac {\phi} {2} \right) = \left( \frac {1} {\sin (\phi / 2)} \right) = \pm \sqrt{ \frac {2} {1 - \cos \phi} } \\
& \sec \left( \frac {\phi} {2} \right) = \left( \frac {1} {\cos (\phi / 2)} \right) = \pm \sqrt{ \frac {2} {1 + \cos \phi} } \\
& \cot \left( \frac {\phi} {2} \right) = \left( \frac {1} {\tan (\phi / 2)} \right) = \frac {1 + \cos \phi} {\sin \phi} = \frac {\sin \phi} {1 - \cos \phi} \\
\end{aligned}
\tag{15}
$$

**Equation 16, Power Reducing Identities.**
The square of each function is written through the cosine of twice the angle, which removes the power.

$$
\begin{aligned}
& \sin^2 \phi = \left( \frac {1} {csc^2 \phi} \right) = \left( \frac {1 - \cos 2\phi} {2} \right) \\
& \cos^2 \phi = \left( \frac {1} {sec^2 \phi} \right) = \left( \frac {1 + \cos 2\phi} {2} \right) \\
& \tan^2 \phi = \left( \frac {1} {cot^2 \phi} \right) = \left( \frac {1 - \cos 2\phi} {1 + \cos 2\phi} \right) \\
& \csc^2 \phi = \left( \frac {1} {sin^2 \phi} \right) = \left( \frac {2} {1 - \cos 2\phi} \right) \\
& \sec^2 \phi = \left( \frac {1} {cos^2 \phi} \right) = \left( \frac {2} {1 + \cos 2\phi} \right) \\
& \cot^2 \phi = \left( \frac {1} {tan^2 \phi} \right) = \left( \frac {1 + \cos 2\phi} {1 - \cos 2\phi} \right) \\
\end{aligned}
\tag{16}
$$

**Equation 17, Spherical Coordinates.**
A point at radius $\rho$, inclination $\theta$ from the $z$ axis and azimuth $\phi$ has the stated Cartesian components, and the inverse relations recover the three coordinates.

$$
\begin{aligned}
& x = \rho \sin \theta \cos \phi \\
& y = \rho \sin \theta \sin \phi \\
& z = \rho \cos \theta \\
& \rho = \sqrt {x^2 + y^2 + z^2} \\
& \theta = \arccos {\frac {z} {\sqrt {x^2 + y^2 + z^2}}} = \arccos  {\frac {z} {\rho}} \\
& \phi = \arctan {\frac {y} {x}} \\
\end{aligned}
\tag{17}
$$

**Equation 18, Polar Form of a Complex Number.**
A complex number $a + bi$ is written by its modulus $\rho$ and argument $\phi$, so that multiplication multiplies the moduli and adds the arguments while division divides the moduli and subtracts them.

$$
\begin{aligned}
& z = a + bi \\
& z = \rho \cos \phi + (\rho \sin \phi)i \\
& z = \rho (\cos \phi + i \sin \phi) \\
& \rho = |z| = \sqrt {a^2 + b^2} \\
& a = \rho \cos \phi \\
& b = \rho \sin \phi \\
& \phi = \tan^{-1} \left( \frac b a \right), 0 \le a \\
& \phi = \tan^{-1} \left( \frac b a \right) + \pi, a \lt 0 \\
& z_1 z_2 = r_1 r_2 (\cos(\phi_1 +\phi_2) + i \sin(\phi_1 + \phi_2)) \\
& \left( \frac {z_1} {z_2} \right) =
  \left( \frac {r_1} {r_2} \right) (\cos(\phi_1 -\phi_2) + i \sin(\phi_1 - \phi_2)) \\
\end{aligned}
\tag{18}
$$

**Equation 19, De Moivre's Theorem.**
Raising a complex number in polar form to the power $n$ raises its modulus to that power and multiplies its argument by $n$.

$$
\begin{aligned}
&z^n = \left[\rho(\cos \phi + i \sin \phi)\right]^n = \rho^n \left(\cos(n\phi)+i \sin(n\phi)\right) \\
\end{aligned}
\tag{19}
$$

**Equation 20, Complex nth Roots.**
A complex number has $n$ distinct $n$th roots, each with modulus $\rho^{1/n}$ and with arguments spaced $2\pi/n$ apart and indexed by $k$.

$$
\begin{aligned}
& z = \rho \left( \cos {\phi} + i \sin {\phi} \right) \\
& ^n\sqrt z_k = z^{1/n}_k = \rho^{1/n} \left( \cos \left( \frac {\phi} {n} + \frac {2\pi k} {n} \right) + i \sin \left( \frac {\phi} {n} + \frac {2\pi k} {n} \right) \right) & 0\lt n; k=0,1,2,\cdots,n-1\\
\end{aligned}
\tag{20}
$$

**Equation 21, Orthogonal Decomposition of a Vector.**
A vector is split into its projection onto $\vec{\rho}$ and the remainder, which is perpendicular to $\vec{\rho}$.

$$
\begin{aligned}
& \vec{v}^\parallel = \operatorname{proj}_{\vec \rho} \vec{v} = \left( \frac {\vec{v} \cdot \vec{\rho}} {\vec{\rho} \cdot \vec{\rho}}  \right) \vec {\rho} \\
& \vec{v}^\bot = \vec {v} - \vec{v}^\parallel \\
\end{aligned}
\tag{21}
$$

**Equation 22, Triangulation from a Baseline.**
The law of sines applied to the triangle formed by a baseline of length $\rho$ and the two interior angles to a target gives the perpendicular distance, the distances along the baseline and the direct distances to the target.

$$
\begin{aligned}
& y = \rho \sin \phi \sin \theta \csc (\phi + \theta) & y = \left( \frac {\rho \sin \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\phi = \rho \cos \phi \sin \theta \csc (\phi + \theta) & x_\phi = \left( \frac {\rho \cos \phi \sin \theta} {\sin (\phi + \theta)} \right) \\
& x_\theta = \rho \sin \phi \cos \theta \csc (\phi + \theta) & x_\theta = \left( \frac {\rho \sin \phi \cos \theta} {\sin (\phi + \theta)} \right) \\
& d_\phi = \rho \sin \theta \csc (\phi + \theta) & d_\phi = \left( \frac {\rho \sin \theta} {\sin (\phi + \theta)} \right) \\
& d_\theta = \rho \sin \phi \csc (\phi + \theta) & d_\theta = \left( \frac {\rho \sin \phi} {\sin (\phi + \theta)} \right) \\
& \theta = \pi - \theta_{\text{exterior angle}} \\
\end{aligned}
\tag{22}
$$

**Equation 23, Tangent Lines to a Circle with Rotations and Mirrors.**
The point-slope form of the line tangent to a circle of radius $\rho$ at angle $\phi$ is given with its images under quarter and half turns and under reflection in the axes and diagonals.

$$
\begin{aligned}
& y = -\cot^{-1}\phi (x - \rho \cos \phi) + \rho \sin \phi & \text{$\phi$ tangent line} \\
& y = \tan^{-1}\phi (x + \rho \sin \phi) + \rho \cos \phi & \text{$\phi+\frac {\pi} {2}$ tangent line, quarter revolution CCW} \\
& y = \tan^{-1}\phi (x - \rho \sin \phi) - \rho \cos \phi & \text{$\phi-\frac {\pi} {2}$ tangent line, quarter revolution CW} \\
& y = -\cot^{-1}\phi (x + \rho \cos \phi) - \rho \sin \phi & \text{$\phi \pm\pi$ tangent line, half revolution} \\
& y = \cot^{-1}\phi (x + \rho \cos \phi) + \rho \sin \phi & \text{$\pi-\phi$ tangent line, mirror along $y=0$} \\
& y = \cot^{-1}\phi (x - \rho \cos \phi) - \rho \sin \phi & \text{$-\phi$ tangent line, mirror along $x=0$} \\
& y = -\tan^{-1}\phi (x - \rho \sin \phi) + \rho \cos \phi & \text{$\frac {\pi} {2} - \phi$ or $-\frac {3\pi} {2} - \phi$ TL, mirror along $y=x$} \\
& y = -\tan^{-1}\phi (x + \rho \sin \phi) - \rho \cos \phi & \text{$\frac {3\pi} {2} - \phi$ or $-\frac {\pi} {2} - \phi$ TL, mirror along $y=-x$} \\
\end{aligned}
\tag{23}
$$

### Notation

- $\rho$, the radius, the hypotenuse of the reference triangle, the modulus of a complex number, or the baseline in triangulation
- $\phi$, the azimuth, or one interior angle in triangulation
- $\theta$, the inclination from the $z$ axis in spherical coordinates, a second angle in the identities, or the other interior angle in triangulation
- $x_\phi$, the distance along the baseline from the point that measures $\phi$ to the foot of the perpendicular from the target
- $d_\phi$, the distance from the point that measures $\phi$ to the target
- $k$, the index of a complex root, or an integer that labels the intervals of a domain
- $\vec{v}^\parallel$, the component of $\vec{v}$ parallel to $\vec{\rho}$
- $\vec{v}^\bot$, the component of $\vec{v}$ perpendicular to $\vec{\rho}$

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### General Sources

- "Domain and Range of the Trigonometric Functions." n.d. Accessed October 25, 2026. [http://users.math.msu.edu/users/systeven/mth103/t3.7.pdf][trig_range]
- "Dynamic Preview of Textarea with MathJax Content." n.d. Accessed October 25, 2026. [https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html][mathjax_preview]
- "Polar Form of a Complex Number." n.d. Accessed October 25, 2026. [http://hotmath.com/hotmath\_help/topics/polar-form-of-a-complex-number.html][polar_complex]
- "Product and Sum Formulas." n.d. Accessed October 25, 2026. [http://www.sosmath.com/trig/prodform/prodform.html][trig_sum]
- "Trigonometric Indentities." n.d. Accessed October 25, 2026. [http://math2.org/math/trig/identities.htm][trig_ident]
- "WolframAlpha, Multi Function Plot." n.d. Accessed October 25, 2026. [https://www.wolframalpha.com/input/?i=Plot%5B%7Bx%5E2%2By%5E2%3D5%5E2,y%3D-atan(pi%2F6)(x-(5+sin+(pi%2F6)))+%2B+(5+cos+(pi%2F6)),y%3D-atan(pi%2F6)(x%2B(5+sin+(pi%2F6)))+-+(5+cos+(pi%2F6))%7D%5D][wolfram_alpha_multi]
- "WolframAlpha, Parametric Plot." n.d. Accessed October 25, 2026. [http://www.wolframalpha.com/input/?i=parametric+plot+(cot+t,+(t%2Fpi)+tan+t),+-2pi+%3C%3D+t+%3C%3D+2pi][wolfram_alpha_param]
- "WolframAlpha, Plot." n.d. Accessed October 25, 2026. [http://www.wolframalpha.com/input/?i=csc+x+-+sec+x,+-pi+%3C%3D+x+%3C%3D+pi][wolfram_alpha]
- "WolframAlpha, Polar Plot." n.d. Accessed October 25, 2026. [http://www.wolframalpha.com/input/?i=polar+plot+r%3Dcot(phi)+\*+tan(phi)+%2B+phi+%2F+pi,+-pi+%3C%3D+phi+%3C%3D+pi][wolfram_alpha_polar]

### Tertiary Sources

- "List of Trigonometric Identities." 2016. Wikipedia. Last modified August 31, at 16:19 (UTC). [https://en.wikipedia.org/w/index.php?title=List\_of\_trigonometric\_identities&oldid=737075237][wiki_trig]
- "Polar Coordinate System." 2016. Wikipedia. Last modified August 19, at 10:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Polar\_coordinate\_system&oldid=735225069][wiki_polar]
- "Spherical Coordinate System." 2016. Wikipedia. Last modified August 11, at 20:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Spherical\_coordinate\_system&oldid=734052692][wiki_sphere]

[mathjax_preview]: https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html
[polar_complex]: http://hotmath.com/hotmath_help/topics/polar-form-of-a-complex-number.html
[trig_ident]: http://math2.org/math/trig/identities.htm
[trig_range]: http://users.math.msu.edu/users/systeven/mth103/t3.7.pdf
[trig_sum]: http://www.sosmath.com/trig/prodform/prodform.html
[wiki_polar]: https://en.wikipedia.org/w/index.php?title=Polar_coordinate_system&oldid=735225069
[wiki_sphere]: https://en.wikipedia.org/w/index.php?title=Spherical_coordinate_system&oldid=734052692
[wiki_trig]: https://en.wikipedia.org/w/index.php?title=List_of_trigonometric_identities&oldid=737075237
[wolfram_alpha]: http://www.wolframalpha.com/input/?i=csc+x+-+sec+x,+-pi+%3C%3D+x+%3C%3D+pi
[wolfram_alpha_multi]: https://www.wolframalpha.com/input/?i=Plot%5B%7Bx%5E2%2By%5E2%3D5%5E2,y%3D-atan(pi%2F6)(x-(5+sin+(pi%2F6)))+%2B+(5+cos+(pi%2F6)),y%3D-atan(pi%2F6)(x%2B(5+sin+(pi%2F6)))+-+(5+cos+(pi%2F6))%7D%5D
[wolfram_alpha_param]: http://www.wolframalpha.com/input/?i=parametric+plot+(cot+t,+(t%2Fpi)+tan+t),+-2pi+%3C%3D+t+%3C%3D+2pi
[wolfram_alpha_polar]: http://www.wolframalpha.com/input/?i=polar+plot+r%3Dcot(phi)+*+tan(phi)+%2B+phi+%2F+pi,+-pi+%3C%3D+phi+%3C%3D+pi
