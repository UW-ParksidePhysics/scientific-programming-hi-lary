import numpy as np
import matplotlib as plt
import fit_curve_array as fit_curve_array


def plot_data_with_fit(data_array, fit_curve, data_format="", fit_format=""):
    scatter_plot = plt.plot(data_array[0, :], data_array[1, :], data_format)
    curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
    return scatter_plot, curve_plot
