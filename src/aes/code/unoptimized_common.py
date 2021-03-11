from common import traces, textins, num_traces, num_points, hypothetical_power_usage

# ANCHOR: additional_imports
import numpy as np
# ANCHOR_END: additional_imports

# ANCHOR: manual_analysis
# Pearson correlation
########################################
# ANCHOR: pearson_basic
def covariance(X, Y):
    if len(X) != len(Y):
        print("Lengths are unequal, quiting...")
        quit()

    n = len(X)
    mean_x = np.mean(X, dtype=np.float64)
    mean_y = np.mean(Y, dtype=np.float64)

    return np.sum((X - mean_x) * (Y - mean_y)) / n

def standard_deviation(X):
    n = len(X)
    mean_x = np.mean(X, dtype=np.float64)

    return np.sqrt( np.sum( np.power( (X - mean_x), 2 ) ) / n )

def pearson_correlation_coefficient(X, Y):
    cov = covariance(X, Y)
    sd_x = standard_deviation(X)
    sd_y = standard_deviation(Y)

    return cov / ( sd_x * sd_y ) 
# ANCHOR_END: pearson_basic
########################################

# Define a function to calculate the Correlation Coefficients for a byte in a
# subkey.
########################################
# ANCHOR: calc_correlations
def calculate_correlation_coefficients(subkey, subkey_index):
    # Declare a numpy for the hypothetical power usage
    hypothetical_power = np.zeros(num_traces)

    for trace_index in range(0, num_traces):
        hypothetical_power[trace_index] = hypothetical_power_usage(
            subkey,
            textins[trace_index][subkey_index]
        )

    # We are going to the determine correlations between each trace point
    # and the hypothetical power usage. This will save all those coefficients
    point_correlation = np.zeros(num_points)

    # Loop through all points and determine their correlation coefficients
    for point_index in range(0, num_points):
        point_correlation[point_index] = pearson_correlation_coefficient(
            hypothetical_power,

            # Look at the individual traces points for every trace
            traces[:, point_index]
        )

    return point_correlation
# ANCHOR_END: calc_correlations
########################################
# ANCHOR: manual_analysis
