# Introduction into Power Analysis

An introductory walkthrough into the concepts and workings of Power Analysis
using the [ChipWhisperer](https://github.com/newaetech/chipwhisperer) framework.
Will take one through breaking the
[RSA](https://en.wikipedia.org/wiki/RSA_\(cryptosystem\)) and
[AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) algorithms
with Power Analysis, and provide exercises to practice.

[Link](https://coastalwhite.github.io/intro-power-analysis/) to the walkthrough.

Made to be part a Master's Course of the [Leiden
University](https://www.universiteitleiden.nl/en).

## Preliminaries

This course expects the reader to be reasonably familiar and comfortable with
programming C / Rust and Python. Furthermore, it is highly recommended to have a
rough understanding of Computer Architecture and encryption methodologies,
although this is not strictly necessary. The walkthrough should take one through
the core material and provide references to further reading if unfamiliar topics
pop up.

This course makes use of the
[ChipWhisperer](https://github.com/newaetech/chipwhisperer) framework to do the
power measurements. The course provides example datasets for all exercises for
when the reader does not have a
[ChipWhisperer](https://github.com/newaetech/chipwhisperer) available, although
it is recommended to follow along for the measurements as well. One should be
able to do their measurements with an oscilloscope or other devices as well. The
theory behind the data analysis should remain the same.

## Content of the walkthrough

The walkthrough contains [how to setup your
environment](https://coastalwhite.github.io/intro-power-analysis/preparing.html)
to be able to run measurements on the
[ChipWhisperer](https://github.com/newaetech/chipwhisperer), install all the
necessary libraries and even how to create your own binaries to run on the
target board. This is followed by an explanation of breaking
[RSA](https://coastalwhite.github.io/intro-power-analysis/rsa) and
[AES](https://coastalwhite.github.io/intro-power-analysis/aes). Each of which
containing their own practice exercises for the reader. Ending with a [final
assignment](https://coastalwhite.github.io/intro-power-analysis/assignment.html),
which is mostly handy for universities using this walkthrough to assess the
knowledge gained by the student.

## Building from source

The source code here uses the [mdBook](https://github.com/rust-lang/mdBook)
project to generate a webpage from markdown files. In order to build from
source, install the `mdbook` binary and run the `mdbook build` command in the
root directory of this repository. This will create a `/book` directory
containing the webpages.

Alternatively, one could also (with the help of mdBook) compile into other
formats such as [epub](https://github.com/Michael-F-Bryan/mdbook-epub) and PDF
(using the print function on the webpage).

## License

Licensed under a MIT license.

## Contributing

If any mistake or out-of-date content is found, please either submit a
[issue](https://github.com/coastalwhite/intro-power-analysis/issues) or [pull
request](https://github.com/coastalwhite/intro-power-analysis/pulls) in this
repository.
