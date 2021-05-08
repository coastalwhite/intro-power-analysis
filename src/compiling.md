# Compiling your own algorithms

> **What will this chapter cover?**
>
> * Installing toolchains necessary for compiling code for a [ChipWhisperer]
>   target
> * Getting started with the SimpleSerial protocol
> * Some useful resources for target algorithms

This walkthrough provides sources for most of the precompiled code you might
need. However, in order to some experimentation yourself, you might want to
compile some implementation of an algorithm. To do this, there are two things we
need: the toolchain to compile to our specific microprocessor architecture and
the low-level source code to compile.

The following section will cover how to install the toolchains for the ARM
architecture. Following that section, will some things to keep in mind when
writing source code for our target. Then, there will be a section on some useful
resources concerning [ChipWhisperer] and algorithms for our target.

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
