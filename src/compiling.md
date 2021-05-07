# Compiling your own algorithms

This walkthrough provides most of the precompiled code you might need. However,
in order to do some of the provided exercises and do some experimentation
yourself, you might want to compile some algorithm. To do this, there are two
things we need. The toolchain to compile to our specific microprocessor
architecture and the low-level source code to compile.

## Toolchains

In order to compile code which is usable for our specific microprocessor
architecture, we need to toolchain for that architecture. As said in the
[introduction chapter](../intro.md), this walkthrough is using the [CW Lite Arm]
variant and therefore here we will show how to install the [ARM toolchain]. For
other toolchains, have a look at the [ChipWhisperer
documentation](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html#compilers).

## Installing the ARM toolchain

Information on the ARM can be found
[here](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).

### Windows and macOS

por *Windows* and *macOS*, the installer on the [ARM developer
website](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
should be enough to install the ARM embedded toolchain.

### GNU/Linux

For [Debian] based systems, including [Ubuntu], we can use the following command
to install the ARM embedded toolchain.

```bash
sudo apt install gcc-arm-none-eabi
```

For [ArchLinux] based systems, including [Manjaro], we can use the following
command to install the ARM embedded toolchain.

```bash
sudo pacman -S arm-none-eabi-gcc
```

## Compiling binaries

With the proper toolchain installed, we can compile binaries which are going to
used on the [ChipWhisperer] *targets*. Take a look at [Simpleserial C Template].
It explains how to create and compile your own binaries. Or have a look at [the
ChipWhisperer GitHub
repository](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware)
for some examples of prewritten algorithms.

> _Note:_ [SimpleSerial] is the protocol [ChipWhisperer] utilizes to describe p
> communicating between the host machine (e.g. a laptop), through the *scope*,
> and the *target*. Some documentation on the [C] library on it can be found
> [here](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware/simpleserial).

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[C]: https://en.wikipedia.org/wiki/Python_(programming_language)
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
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
