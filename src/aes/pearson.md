# Pearson correlation

You might ask yourself, how did it do that? It looks a bit magical with all
these correlations. So let us try to visualize what is actually happening.

We are calculating all the [correlation coefficients] for all the points within
all traces. So let us compare the result of this calculation between the correct
and a wrong sub-key. Again, for me the first sub-key is `H` (ASCII 72 or hex
`0x48`). If you chose a different key, you should adjust this in the following
code.

```python
{{#include code/single_byte.py:plot_pearson_expl}}
```

This will show the following graph.

![AES Pearson Correlation
Explaination](../assets/aes_correlation_visualization.png)

_Figure 1: A visualization of [Pearson Correlation Coefficient] for [AES]_

So what does this graph show? This has the [correlation] between our modeling
power consumption on the *y-axis* and the different power traces on the *x-axis*.
You can see that correlation coefficient remains reasonably consistent for the
wrong sub-key. It never goes above \\(\sim 0.4\\). The correct follows the same
pattern — never really reaching above \\(\sim 0.4\\) — except for one or two
spikes. At these spikes apparently our model matches the actual power
consumption very closely.

These spikes are what we are interested in. We assume that at the highest of
these spikes the microprocessor was executing the the first round of the [AES]
algorithm. The memory state based power model we created should match the
pattern of the actual power consumption at that specific point.

Just looking at the results, our assumption was most probably correct.

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[C]: https://en.wikipedia.org/wiki/Python_(programming_language)
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[AES]: https://nl.wikipedia.org/wiki/Advanced_Encryption_Standard
[XOR]: https://en.wikipedia.org/wiki/Exclusive_or
[Rijndael block cipher]: https://nl.wikipedia.org/wiki/Advanced_Encryption_Standard
[Power analysis]: https://en.wikipedia.org/wiki/Power_analysis
[ChipWhisperer]: https://github.com/newaetech/chipwhisperer
[Side-Channel analysis]: https://en.wikipedia.org/wiki/Side-channel_attack
[TQDM]: https://github.com/tqdm/tqdm
[NumPy]: https://numpy.org/
[Ubuntu]: https://en.wikipedia.org/wiki/Ubuntu
[Debian]: https://en.wikipedia.org/wiki/Debian
[ArchLinux]: https://en.wikipedia.org/wiki/Arch_Linux
[Manjaro]: https://en.wikipedia.org/wiki/Manjaro
[matplotlib]: https://matplotlib.org/
[pip]: https://pypi.org/project/pip/
[make]: https://en.wikipedia.org/wiki/Make_(software)
[libusb]: https://en.wikipedia.org/wiki/Libusb
[SimpleSerial C Template]: https://github.com/coastalwhite/simpleserial-c-template
[SimpleSerial]: https://chipwhisperer.readthedocs.io/en/latest/simpleserial.html
[CW Lite ARM]: https://www.newae.com/products/NAE-CWLITE-ARM
[ARM toolchain]: https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads
[Simple Power analysis]: https://en.wikipedia.org/wiki/Power_analysis#Simple_power_analysis
[Differential Power analysis]: https://en.wikipedia.org/wiki/Power_analysis#Differential_power_analysis
[injective]: https://en.wikipedia.org/wiki/Injective_function
[Rijndael S-Box]: https://en.wikipedia.org/wiki/Rijndael_S-box
[correlate]: https://en.wikipedia.org/wiki/Correlation_and_dependence
[correlation]: https://en.wikipedia.org/wiki/Correlation_and_dependence
[correlation coefficient]: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
[pearson correlation coefficient]: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
[covariance]: https://en.wikipedia.org/wiki/Covariance
[standard deviation]: https://en.wikipedia.org/wiki/Standard_deviation
[mean]: https://en.wikipedia.org/wiki/Mean
