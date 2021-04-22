# How AES Works

In order to do break [AES] with power analysis, we need a reasonably detailed
understanding of how [AES] works. So let us do a crash course.

The [AES] algorithm is a subset of the [Rijndael block cipher] algorithm and
has basically become synonymous with it. As the name [Rijndael block cipher]
implies, we apply the encryption to fixed-size blocks of plain text. With the
size of the blocks being equal to the key size. The encryption is based on
alternating [XOR] operations and shuffling the bytes of the blocks. Let dive
into each individual component of the algorithm.

## The Plan

As said previously, the [AES] algorithm works by alternating [XOR] operations
with the shuffling of the bytes of the blocks. The algorithm specifies that this
is done in rounds. Since [AES] has 3 different key sizes (128, 192 and 256
bits), each different key size also has a different number of rounds. The amount
of rounds are 10, 12, and 14, respectively.

How does a round look like? Although the first round and the last round have
small differences to the rest we can divide all the rounds up into two sections the
shuffling of bytes and the [XOR] operation. Let us first have a look at the
[XOR] operations.

## XOR operations

The [XOR] operation is essentially the mixing in of the key and is what makes the
running of the [AES] algorithm different depending on what key is used. Firstly,
in order to make reversal even more different, we __create multiple new keys from
the original key__. This is called the
[AES key schedule](https://en.wikipedia.org/wiki/AES_key_schedule). This
walkthrough will not go into detail on how this key-expansion works, but if
interested one can look up details. The part which is important to this walkthrough
is that after this expansion we have as many new keys as we have rounds. We will
number all the from \\(k_0\\) to \\(k_{10}\\) (assuming we are using 128 bit [AES]).
Here \\(k_0\\) is the original key and \\(k_1\\) till \\(k_{10}\\) are
the expanded keys.

![AES Key Schedule](../assets/AES_Key_Schedule.svg)

_Figure 1: The AES Key Schedule_

With these keys we performs a [XOR] on a block. The [XOR] operation is a
notorious one way operation. This is due to the lack of information the output
shares about the input. When we do a one bit [XOR] operation and we receive 1 as
an output, the input could have been (0,1) or (1,0). We also have two options
when we get 0 as output. In the case of one bit, this is not that useful.
However, when we a lot of bits the [XOR] operator is impossible to instantly
reverse for every output and brute forcing time is equal to trying every option
divided by two. Mathematically this caused by the [XOR] operation being
non-[injective]. When we have
the outcome and one of the inputs however, this step is extremely easy to
reverse. These two properties make it ideal for a lot of encryption algorithms.

![XOR Non Injective](../assets/XOR_NonInjectivity.svg)

_Figure 2: The non [injective] nature of the [XOR] operation_

## Shuffling of bytes

Next let us have a look at the other parts of each round. The shuffling of
the block bytes. [Rijndael block cipher]s have 3 distinct shuffling techniques:
__substitution, shifting, and mixing__. We are going to have a look at all three
of these shuffling techniques, but let us first have a look at how [Rijndael
block cipher]s view each block.

### Block-of-blocks?

Rijndael looks at blocks as a matrix of bytes. For the key sizes of key sizes of
128, 192 and 256 bits, we have 4 by 4, 6 by 6 and 8 by 8 matrices, respectively.
This would mean that a 128 bit key with bytes \\(b_0, ..., b_{15}\\) is turned
into \\[
\begin{bmatrix}
b_0 & b_4 & b_8 & b_{12} \\\\
b_1 & b_5 & b_9 & b_{13} \\\\
b_2 & b_6 & b_{10} & b_{14} \\\\
b_3 & b_7 & b_{11} & b_{15}
\end{bmatrix}
\\]
Turning a long string of bytes into a matrix allows for matrix operations, which
are common operations for computers. This provides both clarity and speed.

### Substitution

Now comes one of the most genius but strange parts of the Rijndael block
cipher. This is the substitution box. A substitution box is basically a lookup
table to replace (or substitute) a byte with the one from the lookup table. Some
demands for such a lookup table (when used in encryption algorithms) may be:
- __Reverseable__: In order to find back the original byte, we want to be able
   to reverse the process.
- __Non-Linear__: In order to make resistant to
   [linear](https://en.wikipedia.org/wiki/Linear_cryptanalysis) and
   [differential](https://en.wikipedia.org/wiki/Differential_cryptanalysis)
   cryptanalysis, the lookup should be very difficult to approximate with a
   linear function.
- __Fixed Output Sizing__: In order to reduce the complexity and loss of excess
   data, we want to output to have a fixed bit size (preferably the same as the
   input).

The [Rijndael S-Box] does all these things. Since it has all of these
properties, how it specifically looks is not important. Every implementation of
[AES] can save the Substitution-Box and its inverse in static memory since it is
public knowledge.

Here is the [Rijndael S-Box] as a [Python] array.  

```python
{{#include code/common.py:sbox}}
```

### Shifting

The most plain, but equally important, round step is the shifting of the rows.
This step prevents the columns (4 consecutive bytes in the case of the 128 bit
variant) from being __encrypted and decrypted separately__. The step consists of
shifting the first row of the matrix by zero, the second by one, the third by
two and the fourth by three spaces. This is depicted in _Figure 3_.

![Shift Rows](../assets/Shift_Rows.svg)

_Figure 3: [Rijndael block cipher]'s Shift Row_

### Mixing

The last shuffling step mixes the columns in order create [cryptographic
diffusion](https://en.wikipedia.org/wiki/Confusion_and_diffusion), which makes
it __resistant to [statistical analysis
attacks](https://en.wikipedia.org/wiki/Frequency_analysis)__. The step works by
multiplying each column with the following inversable matrix (multiplication
meaning modulo multiplication and addition meaning [XOR]): \\[ \begin{bmatrix} 2
& 3 & 1 & 1 \\\\ 1 & 2 & 3 & 1 \\\\ 1 & 1 & 2 & 3 \\\\ 3 & 1 & 1 & 2
\end{bmatrix} \\]

## Overview

Let us now provide a overview for how a typical [AES] encryption looks. One can
imagine that the decryption is just the inverse of these actions we will
therefore gloss over that part.

As said before, the [AES] encryption process works in rounds. With every round
needing a separate expanded key. Therefore the first step is to create these key
expansions as described in [XOR Operations](#xor-operations). Immediately
following this we that the initial round key \\(k_0\\) and apply the [XOR] with
it to each block.

After the summation with the initial round key we will start applying rounds (9,
11 and 13 rounds for key sizes 128, 192 and 256 bits, respectively). These
rounds apply steps in the following order: Firstly, we do a [substitution with the
Rijndael S-Box](#substitution). Secondly, we [shift the rows of the
matrix](#shifting). Thirdly, we [mix the columns of the matrix up](#mixing).
Lastly, we [add the round key for that round](#xor-operations).

If you are counting along, you will notice that the final round is missing. This
is because the final round is a little bit different. The only difference being
that we __skip the [mixing of
columns](#mixing)__ step, since it serves no purpose in last round.

This all results in the following process:

1. [Key Expansion](#xor-operations)
2. [Apply \\(k_0\\) by XOR](#xor-operations)
3. Apply 9, 11, or 13 rounds
    1. [Substitution with the Rijndael S-Box](#substitution)
    2. [Shift the rows](#shifting)
    3. [Mix the columns](#mixing)
    4. [Apply \\(k_n\\) by XOR with \\(n\\) being the round
       number](#xor-operations)
4. Final round
    1. [Substitution with the Rijndael S-Box](#substitution)
    2. [Shift the rows](#shifting)
    4. [Apply \\(k_n\\) by XOR with \\(n\\) being the round
       number](#xor-operations)

After reading this section should have a basic overview and understanding of how
[AES] works, which you will need for your [Power analysis]. If you want a more
visual explanation, you could watch [AES Explained by
Computerphile](https://www.youtube.com/watch?v=O4xNJsjtN6E).

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
