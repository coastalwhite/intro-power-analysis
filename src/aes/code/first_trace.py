import numpy as np
import chipwhisperer as cw
from capture import scope, target

# Do the actual traces
########################################
# ANCHOR: single_trace
# Define the key used for the encryption
# This key has to be 128 bits = 16 bytes
# = 16 ascii characters in length
key_str = 'H4ck3rm4n-l33t42'

# Convert the key to a byte array
key = bytearray(key_str, 'ascii')

# Define the plain text used
# This plain text has to be a multiple of
# 128 bits = 16 bytes = 16 ascii characters in length.
plain_text = bytearray('a' * 16, 'ascii')

# Capture the actual trace
trace = cw.capture_trace(scope, target, plain_text, key)
# ANCHOR_END: single_trace
########################################

# Plotting the trace
########################################
# ANCHOR: plot_single_trace
import matplotlib.pyplot as plt

plt.plot(trace.wave)
plt.show()
# ANCHOR_END: plot_single_trace
########################################

# Disconnect
########################################
# ANCHOR: disconnect
scope.dis()
target.dis()
# ANCHOR_END: disconnect
########################################
