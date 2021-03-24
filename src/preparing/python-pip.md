# Python and Pip

As previously mentioned, we are going to be heavily relying on Python to do most
of our measurements. We are also going to do some data analysis using Python.
Therefore, we need to install Python along with some packages for it. These
packages being [`numpy`](https://numpy.org/),
[`matplotlib`](https://matplotlib.org/) and
[`tqdm`](https://github.com/tqdm/tqdm).

## Installing Python

The code provided by this walkthrough uses __Python 3__ and will __NOT__ work on
Python 2. Installing Python is a platform dependent workflow. Here are some
common operating systems, for other operating systems a simple [Google
search](https://letmegooglethat.com/?q=installing+python) or a glance at
[Python.org](https://www.python.org/) should do the trick.

### Windows

For Windows, download and run the _Windows installer_ from
[Python.org](https://www.python.org/downloads/windows/). For most people the
64-bit version should be the one.

### macOS

For Mac, you can either install python using [Homebrew](https://brew.sh/) with
the
following shell command.

```bash
brew install python3
```

Or you can install Python via the [macOS
Installer](https://www.python.org/downloads/mac-osx/). Depending on whether on
whether you own a Intel-based macOS device or a ARM-based macOS, you can select
the 64-bit Intel or 64-bit universal2 installer, respectively.

### GNU/Linux

For __Debian__ based systems, including Ubuntu, you can use the following commands.

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

For __ArchLinux__ based systems, including Manjaro, you can use the following
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

## NumPy

One of the most common packages used in Python is the
[NumPy](https://numpy.org/) package. We are also going to be using it here to do
some data transformations. To install NumPy we can use PIP.

```bash
pip install numpy
```

## PyPlot

With our data it may be handy to plot our data. Most of the plots have a
provided example, however. This package is therefore recommended, but optional.
Installing is also via PIP.

```bash
python -m pip install -U matplotlib
```

## TQDM

To have a better overview of the progress our calculations are making, this
walkthrough uses the progress bars from [TQDM](https://github.com/tqdm/tqdm).
This is also optional, but indeed very handy. Installation can be done via PIP.

```bash
pip install tqdm
```

