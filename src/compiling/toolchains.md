# Installing Toolchains

> **What will this section cover?**
>
> * Installing the ARM toolchain
> * Compiling code

In order to compile code which is usable for our specific microprocessor
architecture, we need the toolchain for that specific architecture. As said in
the [introduction chapter](../intro.md), this walkthrough is using the
[ChipWhisperer Lite ARM][CW LITE ARM] board. Therefore, this section will show
how to install the [ARM toolchain]. For other toolchains, have a look at the
[ChipWhisperer
documentation](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html#compilers).

## Installing the ARM toolchain

Information on the ARM toolchain can be found
[here](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).

### Windows and macOS

For *Windows* and *macOS*, the installer on the [ARM developer
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
used on [ChipWhisperer] *targets*. All SimpleSerial resources mentioned in the
the [Existing resources](./resources.md) section contain a *Makefile* in their
root directory. This file provides the computer instructions on how to compile
source code. In order to create `.hex` files &mdash; which is the format used to
program [ChipWhisperer] targets &mdash; from our source, we can simply run the
following command from the root directory of our project, replacing `<PLATFORM>`
with the [proper
platform](https://raw.githubusercontent.com/coastalwhite/simpleserial-c-template/main/PLATFORMS.md).

```bash
PLATFORM=<PLATFORM> make
```

This should create the `.hex` file in the root directory.

We have now installed the proper toolchain and learned how to compile our own
source code. Next up, we want to know how to properly write our source code, so
we can best do our measurements.

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
