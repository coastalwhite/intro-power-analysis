# Power Analysis Introductory Walkthrough

> **What will this course cover?**
>
> * [Chapter 2](./preparing.md) - Installing and configuring capture and
>   analysis tools
> * [Chapter 3](./rsa.md) - Explain *Simple Power Analysis* by looking at the
>   RSA algorithm
> * [Chapter 4](./aes.md) - Explain *Correlation Power Analysis* by looking at
>   the AES algorithm
> * [Chapter 5](./compiling.md) - Setting up tools to compile custom algorithms

IT Security has many fields and layers, all of which aim to investigate how to
break and protect the core principles of information security. These principles
are confidentiality, integrity and availability[^tenets]. One of these fields is
[Side-Channel analysis]. Here the focus lies on how technology interacts with the
world around it, and what analysis these interactions can tell us about
calculations or operations done by the technology.

One of the techniques within [Side-Channel analysis] which aims to break
confidentiality is [Power analysis]. [Power analysis] looks at the power
consumption of hardware in order to make statements about the specific
calculations done within a computer. Some calculations require a higher amount
of power than other calculations.

Take a look at the following picture. If we know that the following _Figure 1_
records a sequence of two different computations - namely, squaring and
taking a product - and we also know that squaring takes marginally less time
than taking a product in this case. You could hypothesize where the power trace
is taking a product and where the trace is squaring a number.

![Power Analysis of RSA](./assets/power_analysis.png)

_Figure 1: Power Trace of a [RSA] encryption by
[Audriusa](https://en.wikipedia.org/wiki/Power_analysis#/media/File:Power_attack_full.png)
(GPFL)

## Purpose of this walkthrough

This walkthrough is meant to be an introduction into both power analysis and
using the [ChipWhisperer] framework.  It expects you to have some basic
knowledge of [Python] and probably [C].  It also helps to be comfortable with a
terminal and the shell. This walkthrough is not about programming or the shell,
however, and most of what is discussed could be followed along with, even if you
have very little programming experience. There is, however, a lot of pseudocode.

Furthermore, if you plan on doing your own traces, you will need a
[ChipWhisperer] capturing board. This walkthrough will provide predefined data
sets, so you can do some analysis without doing the traces yourself. This
could save you from buying a [ChipWhisperer] capturing board. It is, however,
highly recommended doing traces yourself. If you are looking at buying a
[ChipWhisperer] capturing board and don't know what to use, this walkthrough is
created using on the [CW Lite ARM] variant. It is a relatively cheap all-in-one
solution.

## ChipWhisperer

Normally, to make these power measurements on microprocessors, you need a lot of
expensive equipment.  Equipment such as multimeters, oscilloscopes, different
microcontrollers, connectors, etc. This is where the [ChipWhisperer] comes in.
The [ChipWhisperer] framework provides microcontrollers to test and run you
algorithms on, which are referred to as _targets_. But also provides
measurement devices, which when put together with a target is referred to as a
_scope_. [ChipWhisperer] goes further than a playground and can be used in
real world environments, which makes an ideal framework to learn power analysis
with. Partially because scopes can also be connected to other unrelated
microprocessors in order to do power measurements on those.

## Errors and contributing

This walkthrough along with all the content made for it can be found on
[GitHub](https://github.com/coastalwhite/intro-power-analysis). If you find any
errors or feel like something is unclear/left untouched, don't hesitate to
create an issue or pull-request on the page there.

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[C]: https://en.wikipedia.org/wiki/Python_(programming_language)
[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[Power analysis]: https://en.wikipedia.org/wiki/Power_analysis
[ChipWhisperer]: https://github.com/newaetech/chipwhisperer
[Side-Channel analysis]: https://en.wikipedia.org/wiki/Side-channel_attack
[CW Lite ARM]: https://www.newae.com/products/NAE-CWLITE-ARM
[^tenets]: [Three Tenets of Information Security by Mark
Burnette](https://www.lbmc.com/blog/three-tenets-of-information-security/)
