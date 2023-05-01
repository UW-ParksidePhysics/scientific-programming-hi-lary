import numpy as np
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_bivariate_statistics import bivariate_statistics
from read_two_column_text import two_column_text_read


def fit_curve_array(quadratic_coefficients, statistics, number_of_points=100):
    if statistics[3] < statistics[2]:
        # if x_max < x_min:
        raise ArithmeticError
    if number_of_points <= 2:
        raise IndexError
    x_values = np.linspace(statistics[2], statistics[3], number_of_points)
    y_values = np.polyval(quadratic_coefficients, x_values)
    fit_curve = np.array((x_values, y_values))
    return fit_curve


print(fit_curve_array(calculate_quadratic_fit(two_column_text_read('volume_energies')),
                      bivariate_statistics(two_column_text_read('volume_energies'))))
