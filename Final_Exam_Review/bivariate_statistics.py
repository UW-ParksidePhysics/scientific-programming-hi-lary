import numpy as np
from scipy import stats
from two_column_text_read import two_column_text_read


def bivariate_statistics(data_array):  # data_array is from two_column_text_read
    if len(data_array) != 2 or len(data_array[0]) <= 1:
        raise IndexError
    statties = stats.stats.describe(data_array, axis=1)
    mean_y = statties.minmax[0][1]
    x_min, y_min = statties.minmax[0][0], statties.minmax[0][1]
    x_max, y_max = statties.minmax[-1][0], statties.minmax[-1][1]
    standard_deviation_of_y = np.sqrt(statties.variance[1])
    statistics = np.array([mean_y, standard_deviation_of_y, x_min, x_max, y_min, y_max])
    return statistics


print(bivariate_statistics(two_column_text_read('practice_data')))
