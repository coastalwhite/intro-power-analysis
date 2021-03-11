# Breaking AES

[AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) or the
__Advanced Encryption Standard__, is one of the most popular symmetric encryption
algorithms in today's world. It is used for most encrypted conversations between
computers or applications. It is used by your chat apps and by your password
manager. AES has the advantage of being relatively fast and easy to understand.

Since AES is very widely used, any found vulnerability should be taken extremely
serious. It is widely considered that AES is mathematically secure and
therefore _perfect implementations_ of the algorithms should not be vulnerable to
most standard attacks. You can see a caveat here:

__Have we created perfect implementations of the AES algorithm?__

Although there are some AES implementations that have existed for over 2
decades. There are still regular updates to these libraries, because from time to
time people find new mistakes in the implementation of these
algorithms. Code is messy, people make mistakes or are ignorant. Side-channel
analysis is a attack-vector that is often overlooked or ignored since it
requires physical access to the device.

In this section we will have a look at how AES works, a naive implementation of
the algorithm and how power analysis can be used to expose the key used.
