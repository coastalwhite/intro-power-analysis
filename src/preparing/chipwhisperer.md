# ChipWhisperer

> **What will this section cover?**
>
> * Installing the ChipWhisperer Python Library for different Operating Systems
>   * [Windows](#windows)
>   * [macOS](#macos)
>   * [GNU/Linux](#gnulinux)
> * [Verifying that the installation was successful](#verifying-installation)

The [ChipWhisperer] framework has a [Python] library to interact with its
devices.  This library is definitely a necessity if you plan on doing your own
traces.

## Installing the dependencies

The [ChipWhisperer] python library has some dependencies. Mainly, these
dependencies are [libusb] and [make]. Let us go over the different operating
systems and what needs to be done there.

> _Note:_ If something here is not working correctly or not up to date. Refer
> back to the original [ChipWhisperer] documentation that can be found
> [here](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html).

### Windows

For _Windows_, we mainly need to install [make]. There are multiple ways to do
this. I suggest installing [MinGW](https://letmegooglethat.com/?q=MinGW) and
adding `MinGW\msys\1.0\bin` to your `PATH` environment variable.

### macOS

For _macOS_, [make] should already be installed. To install [libusb], we can
use [Homebrew](https://brew.sh/).

```bash
brew install libusb
```

### GNU/Linux

For [Debian] based systems, including [Ubuntu], we can install both [make] and
[libusb] using the following command.

```bash
sudo apt install libusb-dev make
```

For [ArchLinux] based systems, including [Manjaro], we can install both [make]
and [libusb] using the following command.

```bash
sudo pacman -S libusb make
```

## Installing the python library

To install the [ChipWhisperer] library, we can use [pip]. We install it with the following
command.

```bash
pip install chipwhisperer
```

## Linux udev rules

When we are going to start doing traces, one might run into a missing
__permissions__ error on Linux. This has to do with the `udev` rules. How to
solve this, refer to the [ChipWhisperer
docs](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html#hardware-drivers).
This should solve having to run everything with `sudo`, which is not preferred.

## Verifying installation

To verify that the installation succeeded, we can start [Python] in interactive
mode using the `python3` shell command. Then we should see something such as the
following.

```text
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

We can use the following [Python] code to attempt to import the [ChipWhisperer]
python library.

```python3
import chipwhisperer
```

If there aren't any error messages, we have successfully installed the
[ChipWhisperer] python library!

We have now correctly installed everything necessary to perform our own power
measurements using [ChipWhisperer] boards. Furthermore, we have also verified
our installation.

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
