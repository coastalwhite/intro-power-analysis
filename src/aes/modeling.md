# Modeling AES

> **What will this section cover?**
>
> * Creating a leakage model for AES
> * Implementing a leakage model for AES in Python

In order to make sensible statements about the power usage of [AES], we are
going to make a [leakage model] of the [AES] algorithm.
To do this, we need some to determine the optimal memory state to target. When
we determined that we are going to implement that [leakage model] in [Python]

## Hamming Distance and Hamming Weight

Remember that we covered both the [Hamming Distance] and [Hamming Weight] hypotheses
of looking that [memory-based leakage model in Correlation Power
Analysis][leakage models]. In this walkthrough, we are going to go
through a software implementation of [AES]. The `.hex` file of the algorithm for
ChipWhisperer targets can be found
[here](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware/simpleserial-aes).
Since we are using a software implementation, this walkthrough is going to focus
on the [Hamming Weight-based leakage model](./cpa.md#hamming-weight).

We can easily calculate [Hamming Weight] with the following lambda function.

```python
{{#include code/common.py:hamming_fns}}
```

Although it can be worth it to save this to memory, to speed to computation time
later on.

```python
{{#include code/common.py:hamming_precompute}}
```

## Finding a memory state

Suppose we have an input block \\(Input\\) and an output block \\(Output\\),
which is a reasonably common situation. If we would want to check whether a
supposed \\(Key\\) is the key used, we could run through the entire algorithm to
check whether \\(\text{AES}(Input, Key) = Output\\). This is quite inefficient
and is no better than brute forcing the key. Knowing what we now about the
memory state of [AES] we can however do two extreme optimizations.

### Shortcutting calculations

The first optimization we can do has to do with identifying the first memory state
where the key and the \\(Input\\) are combined. If we can identify this memory
state in the power trace, we can determine a probability a certain key was used.
There are two problems with this however. Firstly, identifying the presence or
the location of this memory state is non-trivial. It is very difficult to
manually look at a power trace and tell something about memory states. This is
is mostly due to the variances in baseline power consumption but also due to
noise and other factors. Some of these factors however can be nullified if we
look at multiple power traces instead of one. In order to make it even easier,
we also also look at different input blocks. This allows us to shortcut
calculation time by a lot, since we don't have to do multiple rounds. But we
still have to brute force through every key option.

### Limiting the amount of keys

If we have done the first optimization, there is another optimization which
would lower the amount of possible keys. For the 128 (\\(2^{128}\\) different
keys), 192 (\\(2^{192}\\) different keys) and 256 (\\(2^{256}\\) different keys)
bits key variants, this leaves just \\(2^{12}\\), \\((3 \cdot 2^{11})\\) and
\\(2^{13}\\) key possibilities left, respectively. These are massive
differences, which will allow us to break [AES] in just a few seconds.

How does it work? Please read back [How AES Works -
Shifting](./workings.md#shifting) for one second and see if you find what we can
exploit, when have a value before this step happens. As it mentions this, step
is needed to prevent __attacking each column individually__. Since we can now
produce a value before this step is done. We can attempt to break parts of the
key one at the time. The parts of this key are called sub-keys and they are 1
byte in size. This means we can take sum of different values for the sub-keys
instead of the product.

## Putting this together

Let us make a model of the memory states power usage. This model should provide
us with a number that should [correlate] with the power traces at the point of
which this first [SBox](./workings.md#substitution) step is done. This leaves us
with a longstanding memory state which is dependant on both the key and the
input string. Two items we both preferred for our [leakage model] as explained in
[Memory-based models](./cpa.md#memory-based-models). The [Python] code for
performing our model on a single byte input string using a single byte from the
key (also called a subkey) is the following.

```python
{{#include code/common.py:hyp_fn}}
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
[RAM]: https://en.wikipedia.org/wiki/Random-access_me,mory
[Hamming Distance]: https://en.wikipedia.org/wiki/Hamming_distance
[Hamming Weight]: https://en.wikipedia.org/wiki/Hamming_weight
[Sum of absolute differences]: https://en.wikipedia.org/wiki/Sum_of_absolute_differences
[Absolute]: https://en.wikipedia.org/wiki/Absolute_value
[Leakage Model]: ./cpa.md#leakage-models
