# Automatically cracking an entire key

In this chapter we are going to expand upon the [Manual
Analysis](./manual-analysis.md) chapter to make the process automatic and work
on the entire key. Most of what is discussed in this chapter is quite trivial.
If you feel quite comfortable with what was discussed in the previous chapters,
by all means skip this chapter and attempt implement it yourself. If you get
stuck, you can always come here to get a hint.

## Where were we?

At the moment we have code for modeling the _AES_ memory based power state,
creating correlation coefficients and a piece to plot the results.

```python
{{#include code/unoptimized_common.py:additional_imports}}
{{#include code/single_byte.py:additional_imports}}

{{#include code/common.py:all}}

{{#include code/unoptimized_common.py:manual_analysis}}

{{#include code/single_byte.py:manual_analysis}}
```

## Automatically picking the best subkey guess

At the moment we plot the graph of the maximum correlation coefficients and we
determine from there what is the correct option. We can easily automate this
using the observation that the correct option has the highest correlation
coefficient. For this we can use the numpy `argmax` function.

Replace the code for plotting with the following code.

```python
{{#include code/single_byte.py:auto_best}}
```

Now the code will automatically print out the option with the highest
correlation coefficient.

> __Note:__ If we have done only a few traces and our correlation coefficients
> are a bit less reliable, we can use `np.argsort(...)[::-1]` to select multiple
> options. With this we can, for example, try to brute force with the top 5.

## Cracking an entire key

In order for us to crack the entire key, we can just add another `for` loop.
This loop will go through all subkeys.

This will turn the first following code into the second piece of code.

```python
{{#include code/single_byte.py:loop_single_byte_wrapped}}

{{#include code/single_byte.py:auto_best_wrapped}}
```

```python
{{#include code/multiple_bytes.py:extra_loop}}
```

> __Note:__ Our code is not very efficient and thus is might take quite a
> bit of time for it to crack entire key.

This should output the following.

```text
Best guess:
48 34 63 6b 33 72 6d 34 6e 2d 6c 33 33 74 34 32
H4ck3rm4n-l33t42
```
