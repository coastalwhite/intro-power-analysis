# SimpleSerial protocol

> **What will this section cover?**
>
> * What is the SimpleSerial protocol?
> * How to we write source code?
> * How do we trigger power traces to start and stop?

In order to run your own algorithms, they first have to be written as source
code. The [ChipWhisperer] framework mostly uses [C] as the language for the
source code of encryption algorithms. This means that any existing [C]
implementation of an encryption algorithms can (most of the time) easily be used
on the [ChipWhisperer] targets. There are a few things to take into account,
however. The protocol to send data back and forth between the capture board and
the target board, some recommendations when writing or choosing software,
and how to start and stop power traces. These will all be covered here.

## The SimpleSerial Protocol

In order to send data back and forth between the capture board and the target
board and tell the target to start running its algorithm, a specific
protocol is often used by [ChipWhisperer]. It is called the [SimpleSerial
protocol][SimpleSerial]. It basically explains how to send data to the target
(such as keys, plain texts, commands, etc.) and return data back from the target
(such as cipher texts, hashes, errors, etc.). Some documentation on the [C]
implementation of the algorithm can be found
[here](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware/simpleserial).
Although, if you use either the official
[simpleserial-base](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware/simpleserial-base)
or the
[simpleserial-c-template](https://github.com/coastalwhite/simpleserial-c-template),
you almost don't need to worry about the specifics.

## Writing / selecting your code

When writing your own algorithms for the [ChipWhisperer], it is recommended to
either not use the heap or use it sparingly. Most of the boards used as targets
by [ChipWhisperer] don't have a lot of RAM and thus using it sparingly is
preferred.

Also, when selecting existing implementations, it is recommended to use
embedded hardware or heapless implementations.
[MBedTLS](https://github.com/ARMmbed/mbedtls) contains some of the more used
encryption algorithms.

## Starting / Stopping power traces

On the [ChipWhisperer Lite ARM][CW LITE ARM] and on many other boards, we use the
`trigger_high` function to start a power trace and the `trigger_low` to stop a
power trace. Both of these functions are available from the `hal.h`, which is
also used by the [SimpleSerial protocol][SimpleSerial].

This means somewhere in your code it should look something like the following.

```c
// ...

trigger_high();

encrypt(...);
// or
decrypt(...);

trigger_low();

// ...
```

This way your entire encryption or decryption will be captured by the power
trace. You can also move the triggers to a specific point of the encryption or
decryption, if you want to focus on a specific part of the algorithm.

This should give you most of the information needed to write and/or compile your
own implementations of algorithms. The next section will contain some other
resources which can help you in this process.

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[C]: https://en.wikipedia.org/wiki/Python_(programming_language)
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[AES]: https://nl.wikipedia.org/wiki/Advanced_Encryption_Standard
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
