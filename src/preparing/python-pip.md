# Python and Pip

We are going to be heavily relying on [Python] to do most of our measurements.
We are also going to do some data analysis using [Python]. Because of this heavy
reliance on [Python], we need to install [Python] along with some packages for it.
Two will be manditory: [NumPy] and the [ChipWhisperer] library (which will be
covered in [ChipWhisper](./chipwhisperer.md)) and two are optional but very
useful: [matplotlib] which is used for data plotting and [TQDM] which is used
for visual feedback whilst cracking.

## Installing Python

The code provided by this walkthrough uses [Python] 3 and will __NOT__ work on
[Python] 2. Installing [Python] is a platform dependent workflow. Here are some
common operating systems, for other operating systems a simple [Google
search](https://letmegooglethat.com/?q=installing+python) or a glance at
[Python.org](https://www.python.org/) should do the trick.

### Windows

For *Windows*, download and run the *Windows installer* from
[Python.org](https://www.python.org/downloads/windows/). For most people the
64-bit version should be the one.

### macOS

For *macOS*, you can either install [Python] using [Homebrew](https://brew.sh/)
with the following shell command.

```bash
brew install python3
```

Or you can install [Python] via the [macOS
Installer](https://www.python.org/downloads/mac-osx/). Depending on whether on
whether you own an Intel-based macOS device or an ARM-based macOS, you can
select the 64-bit Intel or 64-bit universal2 installer, respectively.

> *Note:* [Python] on *macOS* tends to give a lot of problems. There is a big
> chance that [Python] is already installed or that only [Python] 2 is
> installed.

### GNU/Linux

For [Debian] based systems, including [Ubuntu], you can use the following commands.

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

For [ArchLinux] based systems, including [Manjaro], you can use the following
command.

```bash
sudo pacman -S python python-pip
```

### Validating your installation

To check whether your installation was successful, restart your shell and run
the following command.

```bash
python3 --version
```

For most installations, this should have also installed `pip`. We can verify
this with.

```bash
pip3 help
```

> *Note:* If [pip] is not installing by default when you install Python. A
> simple google search should do the trick.

## NumPy

One of the most common packages used in [Python] is the [NumPy] package. We are
also going to be using it here to do some data transformations. To install
[NumPy] we can use [pip].

```bash
pip install numpy
```

## PyPlot

With our data it may be handy to plot our data. Most of the plotting done in
this walkthrough has the image attached with it, however. [Matplotlib] is
therefore recommended, but optional.  Installing is also via [pip].

```bash
python -m pip install -U matplotlib
```

## TQDM

To have a better overview of the progress our calculations are making, this
walkthrough uses the progress bars from [TQDM].
This is also optional, but indeed very handy. Installation can be done via [pip].

```bash
pip install tqdm
```

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
