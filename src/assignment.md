# Assignment

As a final assignment for this topic, there should detailed report on some
component of power analysis including a demonstration and what effect it has on
possible attack vectors. A few categories of what we can look at along with some
example topics:

* Breaking an encryption algorithm which is not discussed in this walkthrough.
  Possibly combined with some protections against power analysis. Some examples
  are:
  * Breaking the [Ed25519](https://en.wikipedia.org/wiki/Curve25519)
    algorithm and providing some protections against power analysis. (Have a look
    at the [following implementation TODO]())
  * Breaking [ChaCha](https://en.wikipedia.org/wiki/Salsa20) stream ciphers and
    providing some protections against power analysis. (Have a look at the
    [following implementation TODO]())
* Providing multiple protections on RSA or AES along with analysis of their
  effectiveness and remaining attack vectors.
* Breaking algorithms by using the data power analysis provides us in new ways.
  * Apply machine learning to the data provides by a power-trace of an
    encryption algorithm and determine its effectiveness.
  * Look further into optimizing the amount traces needed to do a correlation
    power analysis attack. How many traces can reliably crack a certain
    algorithm? Can this be improved in some way?

These are just a few examples within the many possible topics. If another
creative idea pops up, feel free to give it a shot. The only requirements are
within the report are a **reproducible demonstration and explanation of your
method** and a **description of (remaining) attack vectors through power
analysis**.

## Grading / What will be looked at

There are a few important topics to which is going to be payed attention whilst
grading.

### Complexity and creativity of method

How difficult and 
