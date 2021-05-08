# Crack individual key-byte

> **What will this section cover?**
>
> * Loading our saved power traces
> * Calculating [Pearson correlation
>   coefficients][PCC CPA] in [Python]
> * Finding the highest [Pearson correlation
>   coefficient][PCC CPA] for a byte of the key used

After creating files containing multiple power traces in the [previous
section](./capture.md), we can now start analyzing our traces and attempt to
crack some bytes with the leakage model we defined in [Modeling
AES](./modeling.md).

So what did we have for our leakage model up until now?

```python
{{#include code/common.py:start}}
```

We are going to take this as a starting point of a new [Python] script. This
walkthrough is will refer to that [Python] file as `crack.py`. We can thus run
this script from our shell using `python3 crack.py`.

## Loading back in our traces

In order to load the power traces we created in the [previous
section](./capture.md), we can add the follow few lines which will load in the
[NumPy] arrays. If for any reason making power traces did not work out or you
don't own a [ChipWhisperer] board, but you still want to continue, you can
download some pre-made traces from
[here](https://github.com/coastalwhite/intro-power-analysis/tree/main/datasets/aes/premade).

```python
{{#include code/common.py:load_data}}
```

Now we can use our `traces`, we know how many traces we have (`num_traces`),
and how many points in time we have per trace (`num_points`).

## Implementing Pearson Correlation Coefficients

As explained in the section on [Correlation Power Analysis](./cpa.md), we are
going to be using [Pearson Correlation Coefficients][PCC CPA] to detect whether
our power trace is similar to our leakage model. So let us implement [Pearson
Correlation Coefficients][PCC CPA] in [Python].

```python
{{#include code/unoptimized_common.py:pearson_basic}}
```

Although this code is very inefficient, and does a lot of unnecessary and double
calculations, it will serve well for now. We are going to be optimizing this
code in [Sidenote: optimizing our algorithm](./optimization.md).

## Cracking a single byte of the key

As explained in [Modeling AES](./modeling.md), we can — using [power analysis] —
__crack the [AES] key byte by byte__. So let us start with a single one. We are
going to go through every possibility and see which byte one provides the
highest [correlation coefficient] between the actual power trace and our modeled
power usage. The important realization here is that we are doing a correlation
between all individual power trace points and the hypothetical power consumption
and we will select the maximum correlation coefficient for all sub-key guesses.
This is because we still have no idea where within the power trace the first
round actually takes place. If we look at all points of each power trace, the
location where the first round takes place should have the highest correlation.
We will demonstrate this later on.

```python
{{#include code/single_byte.py:additional_imports}}

{{#include code/unoptimized_common.py:calc_correlations}}

{{#include code/single_byte.py:loop_single_byte}}
```

This will determine the maximum [correlation coefficients] for all sub-key guesses.
If we plot this we get the following graph.

```python
{{#include code/single_byte.py:plot_single_byte}}
```

![Maximum Correlation Coefficients
AES](../assets/aes_max_correlation_coefficients.png)

_Figure 1: The [AES] Correlation Coefficients for the first sub-key values_

Remember I used the key `H4ck3rm4n-l33t42`, where `H` or ASCII 72 is the first
sub-key byte. If you used a different key, your plot will most probably look
different and there will be a high spike at the ASCII value of your first
sub-key.

Well done! We have cracked our first sub-key! Now that we know how to load in
our power traces and we have successfully cracked one of the bytes of the
encryption key, we can move on to cracking the entire key.

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
[PCC CPA]: ./cpa.md#pearson-correlation-coefficients
