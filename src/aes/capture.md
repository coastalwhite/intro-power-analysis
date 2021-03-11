# Capturing multiple traces

AES is a lot more complex than RSA. Although looking at one trace of RSA can
give you a lot of information about the key used, with AES it is a lot more
common to take multiple traces and average them out. Here we are gonna have a
look at how we can upload the _AES_ source code to the chipwhisperer, and then
capture multiple power traces.

## Base setup

Assuming that you have [setup your environment](../preparing.md), we first have
to connect to the scope and the target. The scope being the measuring device and
the target being the microprocessor, which is going to run the encryption
algorithm. In order to connect to the scope and the target, we need the
following code.

```python
{{#include code/capture.py:setup}}
```

In order to disconnect them again, we can use the following code.

```python
{{#include code/first_trace.py:disconnect}}
```

## Flashing the source code

Depending on what target we are using, we need different software. We can compile
this ourselves, but most compiled code can also be found online. I suggest
looking at [this repository TODO INSERT LINK
HERE](http://github.com/coastalwhite).

Assuming we are using the Chipwhisperer Lite 32-bit addition, we can the
CWLITEARM hex file. in order to upload the program to the target, we can use
the following python code.

```python
{{#include code/capture.py:program}}
```

## Capturing a trace

In order to run our first trace, we need a key and some plain text. The program
we are using is based on __128 bit AES__ and therefore we should provide a
128 bit key and a multiple or 128 bits for our plain text. We can quite easily
create our first trace, with the following code.

```python
{{#include code/first_trace.py:single_trace}}
```

This is very interesting, but we don't really have any confirmation or
visualization. So let us visualize it with [pyplot](https://github.com/matplotlib/matplotlib).

```python
{{#include code/first_trace.py:plot_single_trace}}
```

This should look something like _Figure 1_.

![AES Single Power Trace](../assets/aes_single_trace_plot.png)

_Figure 1: AES Single Power Trace_

## Capturing more than one trace

We can turn this into multiple traces with a simple `for` loop. Here we are
going to be using the [tqdm library](https://github.com/tqdm/tqdm), to have a
nice progress bar. So let us create 100 traces with random input text and save
all relevant data into a [numpy](https://github.com/numpy/numpy) arrays.
This way we can save the eventual traces and plain texts to a file.

First we define a function for creating random plain text strings.

```python
{{#include code/multiple_traces.py:random_str_fn}}
```

Then we capture some traces.

```python
{{#include code/multiple_traces.py:multiple_traces}}
```

Then we turn this into numpy arrays.

```python
{{#include code/multiple_traces.py:to_np_arrays}}
```

Then we can save it to a file.

```python
{{#include code/multiple_traces.py:save_np_arrays}}
```

This way we can later load it.

> For more information on how to do scripting with the ChipWhisperer python
> module have a look over [here](https://wiki.newae.com/Making_Scripts).
> __Disclaimer:__ This is quite heavy.
