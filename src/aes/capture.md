# Capture multiple traces

> **What will this section cover?**
>
> * Setting up our ChipWhisperer scope and target
> * Running AES on our ChipWhisperer target
> * Doing a power trace of a run of our algorithm
> * Saving multiple power traces to a file

Cracking the key used by [AES] with [Power Analysis] is a lot more complex than
was the case with [RSA]. Looking at one trace of a [RSA] decryption can
potentially give you all the information you need to crack the private key.
With [AES] and, more generally, with [Correlation Power Analysis], it is
necessary to take multiple traces and average those power traces out. In this
chapter we are going to have a look at how we can set up a [ChipWhisperer] to
measure power traces. Afterwards, we are going to do some traces and learn how
to save them so we can later do more detailed analysis on them.

## Base setup

Assuming that you have correctly [setup your environment](../preparing.md), we
first have to connect to the *scope* and the *target*. The scope being the
measuring device and the target being the microprocessor, which is going to run
the encryption algorithm. In order to connect to the scope and the target, we
need the following code.

```python
{{#include code/capture.py:setup}}
```

In order to disconnect them again, we can use the following code.

```python
{{#include code/first_trace.py:disconnect}}
```

## Flashing the source code

Depending on what target we are using, we need different software. We can
compile this ourselves, but most compiled code can also be found online. The
compiled code for [AES] can be found
[here](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware/simpleserial-aes).

We always have the flash the source code onto the [CW Lite ARM] using the [Intel
Hex format](https://en.wikipedia.org/wiki/Intel_HEX). Therefore, assuming we are
using the [ChipWhisperer] Lite 32-bit ARM-edition, we can the `CWLITEARM` hex file.
in order to upload the program to the target, we can use the following [Python]
code.

```python
{{#include code/capture.py:program}}
```

## Capturing a trace

In order to run our first trace, we need a key and some plain text. The program
we are using is based on _128 bit AES_ and therefore we should provide a
128 bit key and a multiple or 128 bits for our plain text. We can quite easily
create our first trace, with the following code.

```python
{{#include code/first_trace.py:single_trace}}
```

> **NOTE:** Within the [SimpleSerial] protocol &mdash; which is used under the
> hood by the [ChipWhisperer] devices &mdash; the
> [`capture_trace`](https://chipwhisperer.readthedocs.io/en/latest/api.html?highlight=capture_trace#chipwhisperer.capture_trace)
> function corresponds with a couple of steps (arming the [ChipWhisperer],
> sending the key/plaintext and retrieving the trace data, etc.). This can
> become important when implementing your own algorithms. There it may be
> important to replace w this one function with its individual steps to get more
> control over the commands send. This can be seen in the [Python] code of the
> [SimpleSerial C
> template](https://github.com/coastalwhite/simpleserial-c-template).

This is very interesting, but we don't really have any confirmation or
visualization. So let us visualize it with [matplotlib].

```python
{{#include code/first_trace.py:plot_single_trace}}
```

This should look something like _Figure 1_.

![AES Single Power Trace](../assets/aes_single_trace_plot.png)

_Figure 1: [AES] Single Power Trace_

## Capturing more than one trace

We can turn this into multiple traces with a simple `for` loop. Here we are
going to be using the [TQDM] library to have a nice progress bar. So let us
create 100 traces with random input text and save all relevant data into a
[numpy] arrays.  This way we can save the eventual traces and plain texts to a
file.

First we define a function for creating random plain text strings.

```python
{{#include code/multiple_traces.py:random_str_fn}}
```

Then we capture some traces.

```python
{{#include code/multiple_traces.py:multiple_traces}}
```

Then we turn this into numpy arrays.

```python
{{#include code/multiple_traces.py:to_np_arrays}}
```

Then we can save it to a file.

```python
{{#include code/multiple_traces.py:save_np_arrays}}
```

This way we can later load it.

> For more information on how to do scripting with the [ChipWhisperer] python
> module have a look over [here](https://wiki.newae.com/Making_Scripts).
> __Disclaimer:__ This is quite heavy.

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
[Correlation Power Analysis]: ./cpa.md
