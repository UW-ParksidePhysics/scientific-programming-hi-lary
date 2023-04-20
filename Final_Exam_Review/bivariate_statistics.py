import numpy as np
from scipy import stats


def bivariate_statistics(data_array):  # data_array is from two_column_text_read
    statts = stats.stats.describe(data_array, axis=1)
