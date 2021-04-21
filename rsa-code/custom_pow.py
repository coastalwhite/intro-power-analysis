# ANCHOR: function_def
# Custom implementation of pow(x, y)
def custom_pow(x, y):
    res = 1

    # Until we have reached the highest power
    while (y > 0):
        # If the last byte is a one
        if (y & 0x01):
            res *= x

        # Move on to the next byte
        y >>= 1
        x *= x

    return res
# ANCHOR_END: function_def

# ANCHOR: mod_function_def
# Custom implementation of pow(x, y) % p
# With p >= 2
def custom_pow_mod(x, y, p):
    res = 1

    # Until we have reached the highest power
    while (y > 0):
        # If the last byte is a one
        if (y & 0x01):
            res *= x
            res %= p # Make sure we stay modulo p

        # Move on to the next byte
        y >>= 1
        x *= x
        x %= p # Make sure we stay modulo p

    return res
# ANCHOR_END: mod_function_def

for i in range(0, 10):
    for j in range(0, 10):
        assert(custom_pow(i, j) == pow(i, j))

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(2, 100):
            assert(custom_pow_mod(i, j, k) == pow(i, j) % k)
