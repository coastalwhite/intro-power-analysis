import numpy as np
from common import traces, textins, num_traces, num_points, hypothetical_power_usage

# Optimized version of the calculate_correlation_coefficients function
########################################
# ANCHOR: optimized_calc_correlations
point_means = np.mean(traces, axis=0, dtype=np.float64)
point_mean_diff = traces - point_means

point_mean_diff_squared_sum = np.sum(np.power(point_mean_diff, 2), axis=0)

def optimized_calculate_correlation_coefficients(subkey, subkey_index):
    # Declare a numpy for the hypothetical power usage
    hypothetical_power = np.zeros(num_traces)

    for trace_index in range(0, num_traces):
        hypothetical_power[trace_index] = hypothetical_power_usage(
            subkey,
            textins[trace_index][subkey_index]
        )

    hypothetical_power_mean = np.mean(hypothetical_power, dtype=np.float64)
    hypothetical_power_mean_diff = hypothetical_power - hypothetical_power_mean

    hypothetical_power_mean_diff_sum_squared = np.sum(
        np.power(hypothetical_power_mean_diff, 2)
    )

    # We are going to the determine correlations between each trace point
    # and the hypothetical power usage. This will save all those coefficients
    point_correlation = np.zeros(num_points)

    # Loop through all points and determine their correlation coefficients
    for point_index in range(0, num_points):
        point_correlation[point_index] = np.sum(
            hypothetical_power_mean_diff *

            # Look at the individual traces points for every trace
            point_mean_diff[:, point_index]
        ) / np.sqrt(hypothetical_power_mean_diff_sum_squared *
                point_mean_diff_squared_sum[point_index])

    return point_correlation
# ANCHOR_END: optimized_calc_correlations
########################################
