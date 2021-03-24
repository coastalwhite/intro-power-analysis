# Power Analysis Introductory Walkthrough

IT Security has many fields and layers, all of which aim to investigate how to
break and protect the cores principles of information security which are confidentiality,
integrity and availability. One of these fields is Hardware Security. Here the
focus lies on the how the physical parts of our electronics handle these
principles and what we can do to break and protect them.

One of the techniques within hardware security which aims break confidentiality
is power analysis. Power analysis looks at the power consumption of hardware in
order to make statements about the calculations done within a computer. Some
calculations require a higher wattage then other calculations.

Take a look at the following picture. If we know that the following _Figure 1_
records the a sequence of two different computations - namely, squaring and
taking a product - and we also know that squaring takes marginally less time
than taking a product in this case. You could maybe identify where the power
trace is taking a product and where the trace is squaring a number.

![Power Analysis of RSA](./assets/power_analysis.png)

_Figure 1: Power Trace of a RSA encryption by
[Audriusa](https://en.wikipedia.org/wiki/Power_analysis#/media/File:Power_attack_full.png)
(GPFL)_

## What do you need for this walkthrough

This walkthrough is meant to be a introduction into both power analysis and
using the [ChipWhisperer](https://github.com/newaetech/chipwhisperer) framework.
It expects you to have some basic knowledge of Python (and probably C or Rust).
It also helps to be comfortable with the terminal/shell. This walkthrough is
not about programming or the shell, however, and most of what is discussed could
be followed along with, even if you have very little programming experience.

Furthermore, if you plan on doing your own traces, you will need a
[ChipWhisperer](https://github.com/newaetech/chipwhisperer) board. This
walkthrough will provide predefined data sets, so you can do analysis without
doing the traces yourself. This could save you from buying a ChipWhisperer
board. It is, however, highly recommended to do some traces yourself. If you are
looking at buying a ChipWhisperer board and don't know what to use, this
walkthrough is based on the [CW Lite
ARM](https://www.newae.com/products/NAE-CWLITE-ARM) variant. It is a relatively
cheap all-in-one solution.

## ChipWhisperer

Normally, to make these measurements, you need a lot of expensive equipment.
Equipment such as multimeters, oscilloscopes, different microcontrollers,
connectors, etc. This is where the [ChipWhisperer
framework](https://github.com/newaetech/chipwhisperer) comes in. The
ChipWhisperer framework provides microcontrollers to test and run you
algorithms on, which are referred to as __targets__. But also provides
measurement devices, which when put together with a target is referred to as a
__scope__. The ChipWhisperer goes further than a playground and can be used in
real world environments, which makes an ideal framework to learn power analysis
with.
