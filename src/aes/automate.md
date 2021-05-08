# Automate the cracking process

> **What will this section cover?**
>
> * Automatically selection which sub-key is optimal
> * Cracking all sub-keys

In this section we are going to expand upon the [previous
section](./key-bytes.md) by automating the cracking process for single bytes and
then making the process work on the entire key. Most of what is discussed in
this section is quite trivial. If you feel quite comfortable with what was
discussed in the previous chapters, by all means skip this chapter and attempt
to implement it yourself. If you get stuck, you can always come here to get a
hint.

## Where were we?

At the moment we have code for modeling the [AES] memory based power state,
calculating [correlation coefficients][correlation coefficient] between our
leakage model and the power traces and a piece of code to plot the results.

```python
{{#include code/unoptimized_common.py:additional_imports}}
{{#include code/single_byte.py:additional_imports}}

{{#include code/common.py:all}}

{{#include code/unoptimized_common.py:manual_analysis}}

{{#include code/single_byte.py:manual_analysis}}
```

## Automatically picking the best subkey guess

At the moment we plot the graph of the maximum [correlation coefficient]s and we
determine from there what is the correct option. We can easily automate this
using the observation that the correct option has the highest [correlation
coefficient]. For this we can use the [numpy
`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)
function.

Replace the code for plotting with the following code.

```python
{{#include code/single_byte.py:auto_best}}
```

Now the code will automatically print out the option with the highest
[correlation coefficient].

> _Note:_ If we have done only a few traces and our correlation coefficients are
> a bit less reliable, we can use
> [`np.argsort(...)[::-1]`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html?highlight=argsort#numpy.argsort)
> to select multiple options. With this we can, for example, try to brute force
> with the top 5.

## Cracking the entire key

In order for us to crack the entire key, we can just add another `for` loop.
This loop will go through all sub-keys.

This will turn the first following code into the second piece of code.

```python
{{#include code/single_byte.py:loop_single_byte_wrapped}}

{{#include code/single_byte.py:auto_best_wrapped}}
```

```python
{{#include code/multiple_bytes.py:extra_loop}}
```

> _Note:_ Our code is not very efficient and thus is might take quite a
> bit of time for it to crack entire key. This will be optimized in [Sidenote:
> optimizing our code](./optimization.md).

This should output the following.

```text
Best guess:
48 34 63 6b 33 72 6d 34 6e 2d 6c 33 33 74 34 32
H4ck3rm4n-l33t42
```

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
