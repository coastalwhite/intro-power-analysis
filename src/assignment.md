# Assignment

As a final assignment for this walkthrough, there should detailed report on some
component of power analysis including a demonstration and what effect it has on
possible attack vectors. A few categories of what we can look at along with some
example topics:

- Breaking an encryption algorithm which is not demonstrated in this walkthrough.
  Possibly combined with some protections against power analysis. Have a look at
  the [Compiling your own algorithms](./preparing/toolchains.md) instructions.
  Some examples of interesting algorithms are:
  - Breaking the [Ed25519](https://en.wikipedia.org/wiki/Curve25519)
    algorithm and providing some protections against power analysis. (Have a look
    at the [following implementation](https://github.com/orlp/ed25519))
  - Breaking [ChaCha](https://en.wikipedia.org/wiki/Salsa20) stream ciphers and
    providing some protections against power analysis. (Have a look at the
    [following implementation](https://www.oryx-embedded.com/doc/chacha_8c_source.html))
- Providing multiple protections on [RSA] or [AES] along with analysis of their
  effectiveness and remaining attack vectors.
- Breaking algorithms by using the data power analysis provides us in new ways.
  - Apply machine learning to the data provides by a power-trace of an
    encryption algorithm and determine its effectiveness.
  - Look further into optimizing the amount traces needed to do a correlation
    power analysis attack. How many traces can reliably crack a certain
    algorithm? Can this be improved in some way?

These are just a few examples within the many possible topics. If another
creative idea pops up, feel free to give it a shot. The only requirements of the
report are a **reproducible demonstration and explanation of your method** and a
**description of (remaining) attack vectors through power analysis**.

## Grading / What will be looked at

There are a few important topics to which is going to be payed attention whilst
grading.

### Complexity and creativity of method

Most important is the complexity and creativity of your method. These are best
formulated by the following two questions:

1. What level of difficulty is your attack vector or method of execution?
2. How much of this method was already pre-done by other people?

This also leads to the point that **it is very important to cite sources for
your attacks.** Any found plagiarism will **not** be tolerated. If one uses a
piece of text, code or method (almost) directly copied or cited from a source,
cite that (primary) source. If one adapts a piece of text, code or method from a
source, cite as `Adapted from ...`.

### Level of explanation and writing

Apart from having a great and creative method, it is also very important to make
clear why and why your method was so great and creative. Go into depth on the
steps of your method and why those steps help reach the desired result. You can
assume that the reader has also followed this walkthrough and albeit has some
preliminary knowledge.

### Reproducibility

The final important part of your assignment on [power analysis] is going to be
reproducibility.  How easy is it for the people checking your assignment to
reproduce your method(/results). Is your code readable? Is there some clear
documentation on compiling code, executing an attack or installing dependencies?
It is not needed to write step by step instructions yourself for most of these
steps, but it is important to write an overview on installing dependencies
(linking to the installation guide of that dependency), compiling instructions
(when needed) and attack execution instructions.

Good luck and have fun!

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
