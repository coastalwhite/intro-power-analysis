# ChipWhisperer

The ChipWhisperer framework has a Python library to interact with its devices.
This library is definitely a necessity if you plan on doing your own traces.

## Installing the dependencies

The ChipWhisperer python library has some dependencies. Mainly, these
dependencies are `libusb` and `make`. Let us go over the different operating
systems and what needs to be done there.

> __Note:__ If something here is not working correctly, one can refer back to
> [this](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html)
> documentation page.

### Windows

For __Windows__, we mainly need to install `make`. There are multiple ways to do
this. I suggest installing [MinGW](https://letmegooglethat.com/?q=MinGW) and
adding `MinGW\msys\1.0\bin` to your `PATH` environment variable.

### macOS

For __macOS__, `make` should already be installed. To install `libusb`, we can
use [Homebrew](https://brew.sh/).

```bash
brew install libusb
```

### GNU/Linux

For __Debian__ based systems, including Ubuntu, we can install both `make` and
`libusb` using the following command.

```bash
sudo apt install libusb-dev make
```

For __ArchLinux__ based systems, including Manjaro, we can install both `make`
and `libusb` using the following command.

```bash
sudo pacman -S libusb make
```

## Installing the python library

To install the ChipWhisperer, we can use PIP. We install it with the following
command.

```bash
pip install chipwhisperer
```

## Verifying installation

To verify that the installation succeeded, we can start python3 in interactive
mode using the `python3` shell command. Then we should see something such as the
following.

```text
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

We can use the following python code to attempt to import the chipwhisperer
python library.

```python3
import chipwhisperer as cw
```

If we don't receive any error messages, we have succesfully installed the
ChipWhisperer python library!

## Note for GNU/Linux users

When we are going to start doing traces, one might run into a __permissions__ error.
This has to do with the `udev` rules. How to solve this, refer to the
[ChipWhisperer
docs](https://chipwhisperer.readthedocs.io/en/latest/prerequisites.html#hardware-drivers).
This should solve having to run everything with `sudo`, which is not preferred.

