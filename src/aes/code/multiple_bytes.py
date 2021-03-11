import numpy as np
from common import traces, textins, num_traces, num_points
from unoptimized_common import calculate_correlation_coefficients

# ANCHOR: additional_imports
from tqdm import trange
# ANCHOR_END: additional_imports

# ANCHOR: extra_loop
# Looping through all subkeys
########################################
# ANCHOR: loop_all_bytes
# The eventual key guess
best_guess = np.zeros(16)

# Loop through all possible subkeys
for subkey_index in trange(16, desc="Subkey Index"):
    # Save all correlation coefficients
    max_correlation_coefficients = np.zeros(256)

    # Loop through values this subkey
    for subkey in range(0x00, 0xff + 1):
        max_correlation_coefficients[subkey] = max(abs(
            calculate_correlation_coefficients(subkey, subkey_index)
        ))
    
    # Save the best guess
    best_guess[subkey_index] = np.argmax(max_correlation_coefficients)
# ANCHOR: loop_all_bytes
########################################

# Printing the best guess
########################################
# ANCHOR: auto_best 
print("Best guess:")
for b in best_guess: print("{:02x} ".format(int(b)), end="")
print("")
for b in best_guess: print("{}".format(chr(int(b))), end="")
print("")
# ANCHOR_END: auto_best 
########################################
# ANCHOR: extra_loop
