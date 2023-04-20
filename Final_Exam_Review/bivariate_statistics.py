import numpy as np
from scipy import stats


def bivariate_statistics(data_array):  # data_array is from two_column_text_read
    statties = stats.stats.describe(data_array, axis=1)
    mean_y = statties.minmax[0][1]
    x_min, y_min = statties.minmax[0][0], statties.minmax[0][1]
    x_max, y_max = statties.minmax[-1][0], statties.minmax[-1][1]
    standard_deviation_of_y = np.sqrt(statties.variance[1])
    statistics = np.array([mean_y, standard_deviation_of_y, x_min, x_max, y_min, y_max])
    return statistics

