---
layout: post
mathjax: true
comments: true
title: "Probability and Statistics Reference"
date: 2026-02-11 07:34:17 +0000
categories: math statistics probability
---

<!-- A80 -->
<script>console.log("A80");</script>

Statistics is the discipline of collecting, organizing, analyzing,
and interpreting data to make informed decisions under uncertainty.
Probability, the mathematical foundation of statistics,
quantifies how likely events are to occur.
Together they provide the tools for reasoning rigorously
about patterns in data, testing hypotheses,
and making predictions with measurable confidence.

These tools are relevant to software engineers
for reasons that go beyond data science.
Performance benchmarking requires confidence intervals.
A/B testing requires hypothesis tests.
Capacity planning requires an understanding of distributions.
Anomaly detection requires knowing what "normal" looks like statistically.
Any engineer who makes decisions based on data
benefits from a working knowledge of probability and statistics.

This article is a reference, not a tutorial.
It collects the formulas and definitions
most commonly needed in applied work,
organized for quick lookup.
Each section includes the notation, the formula,
and a brief explanation of when and why to use it.
The level corresponds to an introductory undergraduate course
in probability and statistics for engineers.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-11 07:34:17 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Claude Code Installation Versions
$ claude --version
2.1.37 (Claude Code)
```

## Notation

The following notation is used throughout this reference.

| Symbol | Meaning |
|--------|---------|
| $n$ | Sample size or number of trials |
| $k$ | Number of successes or events |
| $p$ | Probability of success on a single trial |
| $q$ | Probability of failure, $q = 1 - p$ |
| $\mu$ | Population mean |
| $\sigma$ | Population standard deviation |
| $\sigma^2$ | Population variance |
| $\bar{x}$ | Sample mean |
| $s$ | Sample standard deviation |
| $s^2$ | Sample variance |
| $\hat{p}$ | Sample proportion (point estimate of $p$) |
| $\alpha$ | Significance level |
| $Z$ | Standard normal Z-score |
| $z^\star$ | Critical value from the standard normal distribution |
| $t^\star_{df}$ | Critical value from the $t$-distribution with $df$ degrees of freedom |
| $\chi^2$ | Chi-squared statistic |
| $H_0$ | Null hypothesis |
| $H_A$ | Alternative hypothesis |
| $SE$ | Standard error |
| $ME$ | Margin of error |

## Probability Distributions

### Binomial Distribution

The binomial distribution models the number of successes $k$
in $n$ independent trials,
each with success probability $p$.

The Probability Mass Function (PMF) gives
the probability of exactly $k$ successes.

$$
P(X = k) = \binom{n}{k} p^k q^{n-k}, \quad \binom{n}{k} = \frac{n!}{(n-k)!\, k!}
$$

The mean and standard deviation of the binomial distribution are

$$
\mu = np, \quad \sigma = \sqrt{npq}.
$$

Use the binomial distribution when counting discrete successes
in a fixed number of independent trials
with constant success probability.

### Normal Distribution

The normal distribution is a continuous probability distribution
defined by its mean $\mu$ and standard deviation $\sigma$.
Its Probability Density Function (PDF) is

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right).
$$

The standard normal distribution has $\mu = 0$ and $\sigma = 1$.
Any normal random variable $X \sim N(\mu, \sigma^2)$
can be standardized to a Z-score.

$$
Z = \frac{x - \mu}{\sigma}
$$

The normal distribution arises throughout statistics
because of the Central Limit Theorem
and because many natural processes produce approximately normal data.

### Poisson Distribution

The Poisson distribution models the number of events $k$
occurring in a fixed interval of time or space,
given a known average rate $\lambda$.

$$
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots
$$

The mean and variance of the Poisson distribution are both equal to $\lambda$.

$$
\mu = \lambda, \quad \sigma^2 = \lambda
$$

Use the Poisson distribution for count data
where events occur independently at a constant average rate.
Common applications include modeling server request arrivals,
error counts per time period,
and rare event occurrences.

## Normal Approximation to the Binomial

When the number of trials $n$ is large enough,
the binomial distribution can be approximated by the normal distribution.
The approximation is valid when both

$$
np \geq 5 \quad \text{and} \quad nq \geq 5.
$$

Under these conditions, the binomial random variable $X$
is approximately normal with mean $\mu = np$ and standard deviation $\sigma = \sqrt{npq}$.

A continuity correction improves accuracy
when approximating a discrete distribution with a continuous one.
The correction adds or subtracts 0.5 from the boundary value.

| Discrete Probability | Normal Approximation |
|---------------------|---------------------|
| $P(X < k)$ | $P\left(Z \leq \dfrac{k - 0.5 - \mu}{\sigma}\right)$ |
| $P(X \leq k)$ | $P\left(Z \leq \dfrac{k + 0.5 - \mu}{\sigma}\right)$ |
| $P(X = k)$ | $P\left(\dfrac{k - 0.5 - \mu}{\sigma} \leq Z \leq \dfrac{k + 0.5 - \mu}{\sigma}\right)$ |
| $P(X \geq k)$ | $P\left(Z \geq \dfrac{k - 0.5 - \mu}{\sigma}\right)$ |
| $P(X > k)$ | $P\left(Z \geq \dfrac{k + 0.5 - \mu}{\sigma}\right)$ |

## Descriptive Statistics

### Sample Mean

The sample mean $\bar{x}$ estimates the population mean $\mu$.

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

### Sample Variance and Standard Deviation

The sample variance $s^2$ estimates the population variance $\sigma^2$.
The denominator uses $n - 1$ rather than $n$
to correct for the bias introduced by estimating the mean from the same sample.
This correction is known as Bessel's correction.

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2
$$

The sample standard deviation is $s = \sqrt{s^2}$.

### Population Variance and Standard Deviation

When the full population is known,
the population variance divides by $n$ rather than $n - 1$.

$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \mu)^2
$$

The population standard deviation is $\sigma = \sqrt{\sigma^2}$.

## The Law of Total Probability

The law of total probability expresses the probability of an event $E$
as a weighted sum over mutually exclusive conditions.
For two conditions $A$ and $B$ that partition the sample space,

$$
P(E) = P(E \mid A) \cdot P(A) + P(E \mid B) \cdot P(B).
$$

Rearranging to solve for a conditional probability or a partition probability,

$$
P(E \mid A) = \frac{P(E) - P(E \mid B) \cdot P(B)}{P(A)}, \quad
P(A) = \frac{P(E) - P(E \mid B) \cdot P(B)}{P(E \mid A)}.
$$

### Bayes' Theorem

Bayes' theorem relates a conditional probability
to its reverse conditional.
Given events $A$ and $B$ where $P(B) > 0$,

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}.
$$

The denominator can be expanded using the law of total probability.

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B \mid A) \cdot P(A) + P(B \mid \neg A) \cdot P(\neg A)}
$$

Bayes' theorem is the foundation of Bayesian statistics
and is used whenever prior knowledge
must be updated with new evidence.
Common applications include spam filtering,
medical diagnostic reasoning,
and anomaly detection.

## The Central Limit Theorem

The Central Limit Theorem (CLT) states that
the sampling distribution of the sample mean $\bar{x}$
approaches a normal distribution as the sample size $n$ increases,
regardless of the shape of the underlying population distribution.
Specifically,

$$
\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{approximately, for large } n.
$$

The standard error of the mean is

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}.
$$

In practice, $n \geq 30$ is a common rule of thumb
for the CLT approximation to be adequate,
though the required sample size depends on
how far the underlying distribution departs from normality.

The CLT justifies the widespread use of normal-based inference methods
even when the underlying data is not normally distributed.

## Hypothesis Testing

### Framework

A hypothesis test evaluates a claim about a population parameter.

The **null hypothesis** $H_0$ is the default assumption,
typically a statement of no effect or no difference.
The **alternative hypothesis** $H_A$ is the claim being tested.

The **significance level** $\alpha$ is the probability threshold
below which the null hypothesis is rejected.
Common choices are $\alpha = 0.05$ and $\alpha = 0.01$.

### Type I and Type II Errors

| Decision | $H_0$ True | $H_A$ True |
|----------|-----------|-----------|
| Reject $H_0$ | Type I Error (rate $\alpha$) | Correct |
| Fail to Reject $H_0$ | Correct | Type II Error (rate $\beta$) |

The **power** of a test is $1 - \beta$,
the probability of correctly rejecting $H_0$ when $H_A$ is true.

### Z-Test for a Population Mean

When the population standard deviation $\sigma$ is known,
the test statistic is

$$
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

where $\mu_0$ is the hypothesized population mean under $H_0$.

### T-Test for a Population Mean

When the population standard deviation is unknown
and must be estimated by the sample standard deviation $s$,
the test statistic follows a $t$-distribution with $n - 1$ degrees of freedom.

$$
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
$$

The $t$-distribution has heavier tails than the standard normal,
reflecting the additional uncertainty from estimating $\sigma$ with $s$.
As $n$ grows large, the $t$-distribution approaches the standard normal.

### Z-Test for a Proportion

For testing a hypothesis about a population proportion $p$,
the test statistic uses the null value $p_0$.

$$
Z = \frac{\hat{p} - p_0}{SE_{\hat{p}}}, \quad SE_{\hat{p}} = \sqrt{\frac{p_0(1 - p_0)}{n}}
$$

The normal approximation requires at least ten expected successes $np_0 \geq 10$
and ten expected failures $n(1 - p_0) \geq 10$.

### General Form

For any point estimate $\hat{\theta}$ and null value $\theta_0$,

$$
Z = \frac{\hat{\theta} - \theta_0}{SE_{\hat{\theta}}}.
$$

## Confidence Intervals

A confidence interval provides a range of plausible values
for a population parameter.
A $(1 - \alpha) \times 100\%$ confidence interval
means that if the procedure were repeated many times,
approximately $(1 - \alpha) \times 100\%$ of the intervals
would contain the true parameter value.

### General Form

$$
\hat{\theta} \pm z^\star \cdot SE_{\hat{\theta}}, \quad ME = z^\star \cdot SE_{\hat{\theta}}
$$

where $ME$ is the margin of error.

### Confidence Interval for a Mean (Known Variance)

$$
\bar{x} \pm z^\star_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

### Confidence Interval for a Mean (Unknown Variance)

When $\sigma$ is unknown, use the sample standard deviation $s$
and the $t$-distribution with $n - 1$ degrees of freedom.

$$
\bar{x} \pm t^\star_{\alpha/2,\, n-1} \cdot \frac{s}{\sqrt{n}}
$$

### Confidence Interval for a Variance

Uses the chi-squared distribution with $n - 1$ degrees of freedom.

$$
\frac{(n-1)s^2}{\chi^2_{\alpha/2}} < \sigma^2 < \frac{(n-1)s^2}{\chi^2_{1 - \alpha/2}}
$$

For the standard deviation,

$$
\sqrt{\frac{(n-1)s^2}{\chi^2_{\alpha/2}}} < \sigma < \sqrt{\frac{(n-1)s^2}{\chi^2_{1 - \alpha/2}}}
$$

### Confidence Interval for a Proportion

$$
\hat{p} \pm z^\star \cdot SE_{\hat{p}}, \quad SE_{\hat{p}} = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}
$$

The normal approximation requires at least ten successes $n\hat{p} \geq 10$
and ten failures $n(1 - \hat{p}) \geq 10$ in the sample.

### Confidence Interval for Difference of Means

For two independent populations with known variances,

$$
(\bar{x}_1 - \bar{x}_2) \pm z^\star_{\alpha/2} \cdot \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
$$

### Confidence Interval for Difference of Proportions

The standard error for the difference of two independent proportions is

$$
SE_{\hat{p}_1 - \hat{p}_2} = \sqrt{\frac{\hat{p}_1(1 - \hat{p}_1)}{n_1} + \frac{\hat{p}_2(1 - \hat{p}_2)}{n_2}}.
$$

The confidence interval is

$$
(\hat{p}_1 - \hat{p}_2) \pm z^\star_{\alpha/2} \cdot SE_{\hat{p}_1 - \hat{p}_2}.
$$

### Pooled Proportion for Hypothesis Testing

When testing $H_0: p_1 = p_2$,
the pooled proportion estimate uses the combined data from both samples.

$$
\hat{p} = \frac{\hat{p}_1 n_1 + \hat{p}_2 n_2}{n_1 + n_2}
$$

The pooled standard error uses $\hat{p}$ in place of the individual sample proportions.

$$
SE_{\text{pooled}} = \sqrt{\hat{p}(1 - \hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}
$$

## Sample Size Determination

The required sample size to achieve a desired margin of error
can be computed before data collection.

### Sample Size for Estimating a Proportion

$$
n \geq \frac{(z^\star)^2 \cdot p(1-p)}{ME^2}
$$

When no prior estimate of $p$ is available,
use $p = 0.5$ as the worst-case estimate.
This maximizes $p(1-p) = 0.25$
and guarantees that the actual margin of error
will not exceed the target.

### Sample Size for Estimating a Mean

$$
n \geq \left(\frac{z^\star \cdot \sigma}{ME}\right)^2
$$

This requires a preliminary estimate of $\sigma$,
which can come from a pilot study, prior research,
or the range divided by four as a rough approximation.

## Summary

This reference covers the probability distributions and statistical methods
most commonly used in applied work.
The binomial, normal, and Poisson distributions
model discrete counts, continuous measurements, and event rates respectively.
Confidence intervals and hypothesis tests
provide the framework for making decisions under uncertainty.
The Central Limit Theorem and the normal approximation to the binomial
justify the use of normal-based methods across a wide range of settings.

The formulas collected here are standard.
They appear in every introductory statistics textbook
and are implemented in every major statistical software package.
The value of knowing them directly
is that they make the assumptions and limitations of each method explicit.
A confidence interval for a proportion
requires at least ten successes and ten failures.
A $t$-test requires approximately normal data.
A chi-squared interval for variance requires normal data.
Understanding the formulas means understanding
when each method can and cannot be trusted.

## Future Reading

- [NIST Engineering Statistics Handbook][reference_nist],
  a comprehensive, freely available web-based reference
  covering statistical methods for engineers and scientists.

- [Seeing Theory][reference_seeing_theory] by Daniel Kunin at Brown University,
  an interactive visualization of fundamental statistics concepts
  including probability, distributions, and inference.

- [All of Statistics][book_wasserman] by Larry Wasserman,
  a concise graduate-level treatment covering
  probability, statistical inference, and nonparametric methods.

- [Practical Statistics for Data Scientists][book_bruce] by Peter Bruce,
  Andrew Bruce, and Peter Gedeck,
  a practitioner-oriented guide with examples in R and Python.

- [Introduction to Probability and Statistics for Engineers and Scientists][book_ross]
  by Sheldon M. Ross,
  the standard undergraduate textbook for engineering students.

## References

- [Book, All of Statistics][book_wasserman]
- [Book, Introduction to Probability and Statistics for Engineers and Scientists][book_ross]
- [Book, Practical Statistics for Data Scientists][book_bruce]
- [Reference, Khan Academy Statistics and Probability][reference_khan]
- [Reference, NIST Engineering Statistics Handbook][reference_nist]
- [Reference, Notation in Probability and Statistics][reference_notation]
- [Reference, Seeing Theory][reference_seeing_theory]
- [Tool, Binomial Distribution Calculator][tool_binomial]
- [Tool, Standard Normal Z-Table][tool_z_table]

[book_bruce]: https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/
[book_ross]: https://shop.elsevier.com/books/introduction-to-probability-and-statistics-for-engineers-and-scientists/ross/978-0-12-824346-6
[book_wasserman]: https://link.springer.com/book/10.1007/978-0-387-21736-9
[reference_khan]: https://www.khanacademy.org/math/statistics-probability
[reference_nist]: https://www.itl.nist.gov/div898/handbook/
[reference_notation]: https://en.wikipedia.org/wiki/Notation_in_probability_and_statistics
[reference_seeing_theory]: https://seeing-theory.brown.edu/
[tool_binomial]: https://stattrek.com/online-calculator/binomial
[tool_z_table]: https://www.sjsu.edu/faculty/gerstman/EpiInfo/z-table.htm
