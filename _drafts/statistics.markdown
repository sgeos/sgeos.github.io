---
layout: post
mathjax: true
comments: true
title:  "Statistics"
date:   2016-10-28 12:35:48 +0000
categories: math statistics probability
---
## Probability

Normal approximation of binomial distribution.
Event probability $P(x)$, trials $n$, successes $k$, success rate $p$, failure rate $q$,
population mean $\mu$, population standard deviation $\sigma$, Z-score $Z$.

$$
\begin{align}
& P(x = k) = \binom{n}{k} p^k q^{n-k} & \binom{n}{k}= {_nC_k} = \frac{n!}{(n-k)!k!} \\
& 1 = p + q & q = 1 - p\\
& 5 \le \mu_T=np & 5 \le \mu_F=nq \\
& \mu=np \\
& \sigma = \sqrt{npq}  \\
& Z = \frac{x-\mu}{\sigma} \\
& \text{if } P(x \lt k) & P(x \le k - 0.5) \\
& \text{if } P(x \le k) & P(x \le k + 0.5) \\
& \text{if } P(x = k) & P(k - 0.5 \le x \le k + 0.5) \\
& \text{if } P(k \le x) & P(k - 0.5 \le x) \\
& \text{if } P(k \lt x) & P(k + 0.5 \le x) \\
& \text{Ex. } P\left(\frac{x - \mu}{\sigma} \lt \frac{k - 0.5 - \mu}{\sigma}\right) & P\left(Z \le \frac{k - 0.5 - \mu}{\sigma}\right) \\
\end{align}
$$

## Statistics

$x$ Variable of interest.
$\bar{x}$ Sample mean.
$s^2_x$ Sample variance with respect to $x$.
$s_x$ Sample standard deviation with respect to $x$.
$\mu$ Population mean.
$\sigma^2$ Population variance.
$\sigma$ Population standard deviation.

$$
\begin{align}
& \bar{x} = \sum_{i=1}^n\frac{x_i}{n} \\
& s^2_x = \sum_{i=1}^n\frac{(x_i - \bar{x})^2}{n-1} \\
& s_x = \sqrt{\sum_{i=1}^n\frac{(x_i - \bar{x})^2}{n-1}} \\
& \sigma^2 = \sum_{i=1}^n\frac{(x_i - \mu)^2}{n} \\
& \sigma = \sqrt{\sum_{i=1}^n\frac{(x_i - \mu)^2}{n}} \\
\end{align}
$$

$\hat{p}$ 

Confidence interval for population variance $\sigma^2$ and population standard deviation $\sigma$.
Uses sample standard deviation $s$ and a chi-squared distribution $\chi^2$ with $n-1$ degrees of freedom.
Used to find a $(1-\alpha)100\%$ confidence interval.

$$
\begin{align}
& \chi^2 = \frac{(n-1)s^2}{\sigma^2} \\
& \frac{(n-1)s^2}{\chi^2_{\alpha/2}} \lt \sigma^2 \lt \frac{(n-1)s^2}{\chi^2_{1 - \alpha/2}} \\
& \sqrt{\frac{(n-1)s^2}{\chi^2_{\alpha/2}}} \lt \sigma \lt \sqrt{\frac{(n-1)s^2}{\chi^2_{1 - \alpha/2}}} \\
\end{align}
$$

## References:

- [Statistics, Binomial Calculator][statistics-binomial-calculator]
- [Statistics, Z-Table][statistics-z-table]
- [YouTube, The Normal Approximation of the Binomial Distribution][youtube-normal-binomial]
- [Wikipedia, Notation in Probability and Statistics][wikipedia-notation]
- [MathJax Preview][mathjax-preview]

[statistics-binomial-calculator]: http://stattrek.com/online-calculator/binomial.aspx
[statistics-z-table]: http://www.sjsu.edu/faculty/gerstman/EpiInfo/z-table.htm
[youtube-normal-binomial]: https://www.youtube.com/watch?v=k9nRcadQYsU
[wikipedia-notation]: https://en.wikipedia.org/wiki/Notation_in_probability_and_statistics
[mathjax-preview]: https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic-2.html

