# Modeling AES

In order to make sensible statements about the power usage of _AES_, it can be
handy to make a model of the _AES_ algorithm. To do this, we need some
understanding about how computers use power and how the _AES_ algorithm
functions. The first we will discuss here and the second is discussed in the
chapter [How AES Works](./workings.md).

## Hamming Distance and Hamming Weight

Remember that computers are just emergent properties that we get when we have a
ton of transitors, capacitors, wires, etc. in the correct setup. This means that
if we look at the capacitors level, there should be some capacitors that
represents the state of a bit. Here mainly the internal state of memory. Since,
we know that capacitors represents a binary 1 with a certain amount of charge
and a binary 0 with (almost) no charge. We can ask ourselves the question, does
it cost more power to set or maintain memory which involves more binary 1's than
0's. In fact, it indeed does. This gives us two models for looking at the power
usage of memory. __Looking at how much power it would take to set memory, which is
known as the Hamming Distance model. Or we can look at how much power it would
take to maintain memory, which is known as the Hamming Weight model.__ Hamming
Distance meaning the amount of bitflips needed to turn one memory state into
another, and Hamming Distance meaning the amount of 1's in a certain memory
state.

We can easily create a python function, which would identify the Hamming weight
or Hamming distance.

```python
{{#include code/common.py:hamming_fns}}
```

Although it can be worth it to save this to memory, to speed to computation time
later on.

```python
{{#include code/common.py:hamming_precompute}}
```

Although both models work for power usage, mainly to avoid repetition, from
__here on out we will be using the Hamming Weight model__.

## Making a statement about AES's memory state

Suppose we have an input block \\(Input\\) and an output block \\(Output\\),
which is a reasonably common situation. If we would want to check whether a
supposed key is valid, we could run through the entire algorithm to check
whether \\(\text{AES}(Input, Key) = Output\\). This is quite inefficient and is
no better than brute forcing the key. Knowing what we now about the memory state
of _AES_ we can however do two extreme optimizations.

### Shortcutting calculations

The first optimization we can do has to do with identifying the first memory state
where the key and the \\(Input\\) are combined. If we can identify this memory
state in the power trace, we can determine a probability a certain key was used.
There are two problems with this however. Firstly, identifying the presence or
the location of this memory state is non-trivial. It is very difficult to
manually look at a power trace and tell something about memory states. This is
is mostly due to the variances in baseline power consumption but also due to
noise and other factors. Some of these factors however can be nullified if we
look at multiple power traces instead of one. In order to make it even easier,
we also also look at different input blocks. This allows us to shortcut
calculation time by a lot, since we don't have to do multiple rounds. But we
still have to brute force through every key option.

### Limiting the amount of keys

If we have done the first optimization, there is another optimization which
would lower the amount of possible keys. For the 128 (\\(2^{128}\\) different
keys), 192 (\\(2^{192}\\) different
keys) and 256 (\\(2^{256}\\) different
keys) bits key
variants, this leaves just \\(2^{12}\\), \\((3 \cdot 2^{11})\\) and \\(2^{13}\\)
key possibilities left, respectively. These are massive differences, which will
allow us to break _AES_ in just a few seconds.

How does it work? Please read back [How AES Works -
Shifting](./workings.md#shifting) for one second and see if you find what we can
exploit, when have a value before this step happens. As it mentions this, step
is needed to prevent __attacking each column individually__. Since we can now
produce a value before this step is done. We can attempt to break parts of the
key one at the time. The parts of this key are called sub-keys and they are 1
byte in size.

## Putting this together

Let us make a model of the memory states power usage.

```python
{{#include code/common.py:hyp_fn}}
```

