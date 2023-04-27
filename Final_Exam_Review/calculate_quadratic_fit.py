import numpy as np
from two_column_text_read import two_column_text_read


def calculate_quadratic_fit(data_array):
    x_values = data_array[0, :]
    y_values = data_array[1, :]
    quadratic_coefficients = np.polyfit(x_values, y_values, 2)
    return quadratic_coefficients


print(calculate_quadratic_fit(two_column_text_read('practice_data')))
