# Pearson correlation

You might ask yourself, how did it do that? It looks a bit magical with all
these correlations. So let us try to visualize what is actually happening.

We are calculating all the correlation coefficients for all the points within
all traces. So let us compare the result of this calculation between the correct
and a wrong subkey. Again, for me the first subkey is `H` (ASCII 72 or hex
`0x48`). If you chose a different key, you should adjust this in the following
code.

```python
{{#include code/single_byte.py:plot_pearson_expl}}
```

This will show the following graph.

![AES Pearson Correlation
Explaination](../assets/aes_correlation_visualization.png)

_Figure 1: A visualization of Pearson Correlation Coefficient for AES_

So what does this graph show? This has the correlation between our modeling
power consumption on the y-axis and the different power traces on the x-axis.
You can see that correlation coefficient remains reasonably consistant for the
wrong subkey. It never goes above \\(\sim 0.4\\). The correct follows the same
pattern — never really reaching above \\(\sim 0.4\\) — except for one or two
spikes. At these spikes apparently our model matches the actual power
consumption very closely.

These spikes are what we are interested in. We assume that at the highest of
these spikes the microprocessor was executing the the first round of the _AES_
algorithm. The memory state based power model we created should match the
pattern of the actual power consumption at that specific point.

Just looking at the results, our assumption was most probably correct.
