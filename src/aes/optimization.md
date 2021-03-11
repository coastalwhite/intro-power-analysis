# Sidenote: Optimizing our algorithm

As you may have noticed our algorithm is now really slow. This is due to the
calculation of Pearson Correlation Coefficients. We can speed this up by a lot
if we notice a couple of things.

1. \\(\sqrt{a}\sqrt{b}=\sqrt{a b}\\). Since square rooting is a very expensive
   operation, we can optimize the calculation of \\(\sigma_x \sigma_y\\) from
   two square root calculations to one.
2. We are recalculating a lot of averages and standard deviations. We can
   precompute these averages and standard deviations and them fetch them instead
   of recomputing them.
3. Since we only care about the maximum correlation coefficient and have no
   interest in the value itself, we can stop doing any factorization.

In the following code we have created a function which applies these three
optimized functions when calculating the correlation coefficients.

```python
{{#include code/optimized_common.py:optimized_calc_correlations}}
```
