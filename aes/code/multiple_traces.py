import numpy as np
import chipwhisperer as cw
from capture import scope, target

# Helper Functions
########################################
# ANCHOR: random_str_fn
import string
import random

def random_string(length):
    # Define the alphabet of the random string
    # Here we take the lowercase latin alphabet in ascii encoding
    # e.g. "cpjsapcnrsdtjvlo", "btqfocsprbualtwt" or "yzkwewjbkpmriccx"
    alphabet = string.ascii_lowercase

    # Return a string with the given length with randomly chosen chars
    return ''.join(random.choice(alphabet) for i in range(length))
# ANCHOR_END: random_str_fn
########################################

# Do the actual traces
########################################
# ANCHOR: multiple_traces
from tqdm import trange

# Define the key used for the encryption
# This key has to be 128 bits = 16 bytes
# = 16 ascii characters in length
key_str = 'H4ck3rm4n-l33t42'

# Convert the key to a byte array
key = bytearray(key_str, 'ascii')

# Define the constant for the amount of traces
N = 100

textins = []
traces = []

# Loop through all traces
for i in trange(N, desc="Capturing traces"):

    # Define the plain text used
    # This plain text has to be a multiple of
    # 128 bits = 16 bytes = 16 ascii characters in length.
    plain_text = bytearray(random_string(16), 'ascii')

    # Capture the actual trace
    trace = cw.capture_trace(scope, target, plain_text, key)

    # If the capture timed out move to the next capture
    if trace is None:
        continue

    textins.append(plain_text)
    traces.append(trace.wave)
# ANCHOR_END: multiple_traces
########################################

# Convert to numpy arrays
########################################
# ANCHOR: to_np_arrays
np_traces = np.asarray(traces)
np_textins = np.asarray(textins)
# ANCHOR_END: to_np_arrays

# ANCHOR: save_np_arrays
np.save('output/traces.npy', np_traces)
np.save('output/textins.npy', np_textins)
# ANCHOR_END: save_np_arrays
########################################

# Disconnect
########################################
scope.dis()
target.dis()
########################################

