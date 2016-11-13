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

$H_0$ Null hypothesis.
$H_A$ or $H_1$ Alternate hypothesis.
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

Confidence interval for difference of population means.  First population $x_1$.  Second population $x_2$.  Population mean $\bar{x}$.  Standard deviation $\sigma$.  Sample size $n$.  Z-score for value $v$ below the curve $z_v$.  Confidence interval percentage $\alpha$.

$$
\begin{align}
& (\bar{x_1} - \bar{x_2}) \mp z_{(1-\alpha/2)} \sqrt{\frac{\sigma^2_1}{n_1} + \frac{\sigma^2_2}{n_2}} \\
\end{align}
$$

Proportion $p$.
Estimated proportion $\hat{p}$.

Rejecting the null hypothesis $H_0$ when it is true is a **type 1 error**.
Failing to reject the null hypothesis when the alternate hypothesis $H_A$ is true is a **type 2 error**.
The significance level $\alpha$ is also the type 1 error rate.
The type 2 error rate $\beta$ is related to the power of a test $(1 - \beta)$.

Standard normal distribution $N(\mu = 0, \sigma = 1)$.

Observation $x$.  Population mean $\mu$.  Standard deviation $\sigma$.
$$
\begin{align}
& Z = \frac {x - \mu}{\sigma} \\
\end{align}
$$

Point estimate $\hat{x}$.
Hypothesis null value ${x_0}$.
Standard error of point estimate $SE_{\hat{x}}$.

$$
\begin{align}
& Z = \frac{\hat{x}-x_0}{SE_{\hat{x}}} \\
\end{align}
$$

Point estimate $\hat{x}$.
Selected confidence level $z^\star$.
Standard error of point estimate $SE_{\hat{x}}$.
Margin of error $ME_{\hat{x}}$.

$$
\begin{align}
& \hat{x} \mp z^\star SE_{\hat{x}} & \text{one tailed confidence interval} \\
& \hat{x} \mp z^\star SE_{\hat{x}} & \text{two tailed confidence interval} \\
& ME_{\hat{x}} = z^\star SE_{\hat{x}} & \text{margin of error} \\
\end{align}
$$

Proportion estimate $\hat{p}$, near normal distribution. Standard error of proportion estimate $SE_{\hat{p}}$.  True proportion $p$. Sample size $n$.  Independent observations.  At least ten successes $10 \le np$ and ten failures $10 \le n(1-p)$.  For confidence intervals, $\hat{p}$ is generally used instead of $p$.  For hypothesis tests, the null value $p_0$ is used instead of $p$.

$$
\begin{align} \\
& SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} \\
\end{align}
$$

Sample size $n$.
Margin of error $ME_{\hat{x}}$.
Selected confidence level $z^\star$.
Standard error $SE_{\hat{x}}$.
Proportion $p$ with worst case estimate of 0.5.

$$
\begin{align} \\
& ME_{\hat{x}} = z^\star SE_{\hat{x}} & \text{margin of error} \\
& \frac{(z^\star)^2p(1-p)}{(ME_{\hat{x}})^2} \le n & \text{proportion sample size} \\
\end{align}
$$

Significance level $\alpha$.

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

