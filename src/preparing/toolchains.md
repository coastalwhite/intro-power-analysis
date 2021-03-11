# Compiling your own algorithms

This walkthrough provides most of the precompiled code you might need. However,
in order to do some of the provided exercises and do some experimentation
yourself, you might want to compile some algorithm. To do this, there are two
things we need. The toolchain to compile to our specific microprocessor
architecture and the source code to compile.

## Toolchains

In order to compile code which is usable for our specific microprocessor
architecture, we need to toolchain for that architecture. As said in the
[introduction chapter](../intro.md), this walkthrough is using the CW Lite Arm
variant and therefore here we will show how to install the ARM toolchain. For
other toolchains, have a look at the [ChipWhisperer
documentation](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html#compilers).

## Installing the ARM toolchain

Information on the ARM can be found
[here](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads).

### Windows and macOS

For Windows and macOS, the installer on the [ARM developer
website](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
should be enough to install the ARM embedded toolchain.

### GNU/Linux

For __Debian__ based systems, including Ubuntu, we can use the following command
to install the ARM embedded toolchain.

```bash
sudo apt install gcc-arm-none-eabi
```

For __ArchLinux__ based systems, including Manjaro, we can use the following
command to install the ARM embedded toolchain.

```bash
sudo pacman -S arm-none-eabi-gcc
```

## Compiling binaries

With the proper toolchain installed, we can compile binaries to be used on our
ChipWhisperer targets. Take a look at [Simpleserial
Template](https://github.com/coastalwhite/simpleserial-c-template) on how to
create and compile your own binaries. Or have a look at [the ChipWhisperer
GitHub
repository](https://github.com/newaetech/chipwhisperer/tree/develop/hardware/victims/firmware)
for some examples.

> __Note:__ SimpleSerial is the protocol ChipWhisperer has defined to describe
> communicating between the host machine (e.g. a laptop) and the target. Some
> documentation on it can be found
> [here](https://chipwhisperer.readthedocs.io/en/latest/simpleserial.html).
