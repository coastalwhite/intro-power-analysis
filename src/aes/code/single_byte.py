import numpy as np
from common import traces, textins, num_traces, num_points
from unoptimized_common import calculate_correlation_coefficients

# ANCHOR: additional_imports
from tqdm import trange
# ANCHOR_END: additional_imports

# ANCHOR: manual_analysis
# ANCHOR: loop_single_byte_wrapped
# Looping through all possible bytes
########################################
# ANCHOR: loop_single_byte
# Save all correlation coefficients
max_correlation_coefficients = np.zeros(256)

# Loop through values this subkey
for subkey in trange(0xff + 1, desc="Attack Subkey"):
    max_correlation_coefficients[subkey] = max(abs(
        calculate_correlation_coefficients(subkey, 0)
    ))
# ANCHOR_END: loop_single_byte
########################################
# ANCHOR_END: loop_single_byte_wrapped

# Plotting the max_correlation_coefficients
########################################
# ANCHOR: plot_single_byte
import matplotlib.pyplot as plt

plt.plot(max_correlation_coefficients)
plt.show()
# ANCHOR_END: plot_single_byte
########################################
# ANCHOR_END: manual_analysis

# Plotting the correlation explanation
########################################
# ANCHOR: plot_pearson_expl
plt.plot(
    abs(calculate_correlation_coefficients(0x48, 0)),
    label='correct'
)
plt.plot(
    abs(calculate_correlation_coefficients(0x00, 0)),
    label='wrong'
)

plt.legend()
plt.show()
# ANCHOR_END: plot_pearson_expl
########################################

# ANCHOR: auto_best_wrapped 
# Printing the best guess
########################################
# ANCHOR: auto_best 
# Select the element with the highest correlation
best_guess = np.argmax(max_correlation_coefficients)

# Print both the hex value and the ASCII character
print("Best guess: {:02x} or '{}'".format(best_guess, chr(best_guess)))
# ANCHOR_END: auto_best 
########################################
# ANCHOR_END: auto_best_wrapped 
