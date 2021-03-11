# Manual Analysis

With the power usage model we described in the previous chapter, we can now
start to do some analysis of our power traces.

Let look what we have up until now.

```python
{{#include code/common.py:start}}
```

In order to load the data we created with our trace we can add the follow few
lines which will load in the numpy arrays.

```python
{{#include code/common.py:load_data}}
```

## Are we data-scientists yet?

We want to change the data in such a way that it makes it easier to identify
whether a our __modeled power usage is similar to the actual power usage__. We
need multiple power traces for this. The most important of which is the [Pearson
correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).

### Pearson correlation coefficient

We have an difficult task here. Again, we want to know how likely it is that our
modeled power usage has a similar pattern to the actual power usage. In
statistics this is known as the modeled power usage and the actual power usage
having a high __correlation__. If two functions are in perfect correlation,
one function should always rise when the other rises and one function
should always decline when the other declines.

This is what the [Pearson correlation
coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
indicates. We provide it with two functions and it will give us a value between
\\(-1\\) and \\(1\\), indicating whether the two functions correlate. \\(1\\)
meaning (unrealistic) levels of correlation, \\(0\\) meaning no correlation and
\\(-1\\) meaning a inverse correlation. How the Pearson correlation coefficient
manages to do this is not as important for us, but reading the Wikipedia page
can be very interesting. What is important for us is the formula so we can use
it in our code.

\\[
\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y}
\\]

This may not be entirely clear to most people without knowledge of
statistics. So let us break it down.

- \\(\rho\\) is the letter commonly used to represent the Pearson correlation
  coefficient.
- \\(X\\) and \\(Y\\) are our functions and can actually be represented as a
  finite list of numbers in our case. This means \\(X = { x_0, \ldots, x_n }\\) and
  \\(Y = { y_0, \ldots, y_n }\\) with \\(n\\) being an integers greater or
  equal to zero.
- \\(\text{cov}(X,Y)\\) is the covariance of \\(X\\) and \\(Y\\). This can be
  calculated with \\(\text{cov}(X,Y)=\mathbb{E}[(X - \mu_X)(Y - \mu_Y)] =
  \frac{1}{n} \sum_{i=0}^n (x_i - \mu_X)(y_i - \mu_Y) \\), with
  \\(\mu_X\\) and \\(\mu_Y\\) being the mean of \\(X\\) and \\(Y\\),
  respectively.
- \\(\sigma_X\\) and \\(\sigma_Y\\) being the standard deviation of \\(X\\) and
  \\(Y\\), respectively. The standard deviation can be calculated with
  \\(\sigma_X = \sqrt{\frac{1}{n} \sum_{i=0}^n (x_i - \mu_X)^2}\\) with
  \\(\mu_X\\) being the mean of \\(X\\).

Let us move these formulas to python.

```python
{{#include code/unoptimized_common.py:pearson_basic}}
```

Although this code is very inefficient, and does a lot of unnecessary and double
calculations, it will serve well for now.

### Cracking a single byte

As explained in [Modeling AES](./modeling.md), we can — using power analysis —
__crack the _AES_ key byte by byte__. So let us start with a single one. We are
going to go through every possibility and see which byte one provides the
highest correlation coefficient between the actual power trace and our modeled
power usage. The important realisation here is that we are doing a correlation
between all individual power trace points and the hypothetical power
consumption and we will select the maximum correlation coefficient for all
subkey guesses. This is because we still have no idea where the first round
actually takes place. If we look at all points of each power trace, the location
where the first round takes place should have the highest correlation. We will
demonstrate this later on.

```python
{{#include code/single_byte.py:additional_imports}}

{{#include code/unoptimized_common.py:calc_correlations}}

{{#include code/single_byte.py:loop_single_byte}}
```

This will determine the maximum correlation coefficients for all subkey guesses.
If we plot this we get the following graph.

```python
{{#include code/single_byte.py:plot_single_byte}}
```

![Maximum Correlation Coefficients
AES](../assets/aes_max_correlation_coefficients.png)

_Figure 1: The AES Correlation Coefficients for the first subkey values_

Remember I used the key `H4ck3rm4n-l33t42`, where `H` or ASCII 72 is the first
subkey byte. If you used a different key, your plot will most probably look
different and there will be a high spike at the ASCII value of your first
subkey.

Well done! We have cracked our first subkey!
