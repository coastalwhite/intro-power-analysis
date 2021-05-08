# Breaking AES

> **What will this chapter cover?**
>
> * Describe what [Correlation Power Analysis](./aes/cpa.md) is
> * Explain in full detail [how AES works](./aes/workings.md)
> * Explain [creating a leakage model for AES](./aes/modeling.md) in full
>   detail
> * Cover [how to capture multiple traces](./aes/capture.md) with the
>   [ChipWhisperer] framework
> * Explain [how to crack individual key-bytes](./aes/key-bytes.md) from power
>   traces
> * Describe in which way we can [automate the cracking
>   process and crack whole keys](./aes/automate.md)

[AES] or the _Advanced Encryption Standard_, is one of the most used
symmetric encryption algorithms in today's world. It is used for most encrypted
conversations between computers or applications. It is used by your chat apps
and by your password manager. [AES] has the advantage of being relatively fast and
easy to understand.

Since [AES] is very widely used, any found vulnerability should be taken extremely
serious. It is widely considered that [AES] is mathematically secure and
therefore _perfect implementations_ of the algorithms should not be vulnerable to
most standard attacks. You may see a caveat here:

__Have we created perfect implementations of the AES algorithm?__

Although there are some [AES] implementations that have existed for over 2
decades[^openssl]. There are still regular updates to these libraries, because
from time to time people find new mistakes in the implementation of these
algorithms. Code is messy, people make mistakes or are ignorant. [Side-Channel
analysis] is a attack-vector that is often overlooked or ignored since it
requires physical access to the device.

In this section we will have a look at how [AES] works, cracking a naive
implementation of the algorithm and see how [Power Analysis] can be used to
expose the key used.

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

[^openssl]: OpenSSL has been copyrighted since 1999 &mdash; <https://www.openssl.org/>
