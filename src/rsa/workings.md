# A deeper look at RSA

RSA is quite an simple algorithm, but to understand how and why we can crack RSA
using power traces. It is important to understand the method RSA uses in quite
some depth. In the chapter on AES, we will go a bit deeper into cache based
side-channel attacks and why they work exactly, but here we will do a few
assumptions to focus on the important bits.

## What is RSA?

RSA is used to do asymmetric encryption. This means we have two keys. Most of
the time this means we have one to encrypt plain text to cipher text, one to
decrypt cipher text back to plain text. It is common to have one of these keys
be public and the other be private and secret. Thus, they might also be called
to the public and private key.

RSA uses one simple principle. For encryption with public key \\( e \\), for
every byte of our plain text \\(b_i\\) we have encrypted byte \\( c_i=b_i^e \\)
modulo some integer \\( N \\). For decryption with private key \\( d \\), for
every byte of our cipher text \\(c_i\\) we have encrypted byte \\( b_i=c_i^d \\)
modulo some integer \\( N \\). The relationship between these numbers is not as
important for now.

One might wonder how these computations are actually done on the bare hardware.
It turns out that we can interpret this as repeated multiplication and squaring.
This is how that works.

If we are given a number \\( x \\) and we are tasked with the raising it to the
13th power, we might to it as follows:

\\[ x^{13} = x \cdot x^{12} = x \cdot (x^6)^2 = x \cdot ((x^3)^2)^2 = x \cdot
((x \cdot x^2)^2)^2 \\]

Which means that, if we go from inwards to outwards, we can in some Python
pseudo code which calculates the power 13 of any number:

```python
# Raise to the power 13 by repeated squaring and multiplication
function to_power_13(n):
    step_value = n

    step_value = pow(step_value, 2) #           x^2
    step_value = n * step_value     #       x * x^2
    step_value = pow(step_value, 2) #      (x * x^2)^2
    step_value = pow(step_value, 2) #     ((x * x^2)^2)^2
    step_value = n * step_value     # x * ((x * x^2)^2)^2

    return step_value
```

We also might notice that has very close ties to binary. For example, the 


