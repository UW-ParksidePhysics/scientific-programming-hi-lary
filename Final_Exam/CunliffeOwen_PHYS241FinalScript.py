from read_two_column_text import read_two_column_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
from generate_matrix import *
from equations_of_state import *
from convert_units import convert_units
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

if __name__ == "__main__":
    filename = 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'
    display_graph = 'True'

    # Fit an Equation of State
    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        chemical_symbol = filename_split[0]
        crystal_symbol = filename_split[1]
        density_correlation = filename_split[2]
        return chemical_symbol, crystal_symbol, density_correlation


    # making the data to plot
    two_column_data = (read_two_column_text(filename)) / 2
    statistical_data = calculate_bivariate_statistics(two_column_data)
    quad_fit_data = calculate_quadratic_fit(two_column_data)

    # fitting the data
    fit_eos_curve, fit_eos_parameters = fit_eos(two_column_data[0], two_column_data[1],
                                                quad_fit_data, eos='birch-murnaghan')
    new_fit_curve = fit_curve_array(quad_fit_data, statistical_data[2], statistical_data[3], number_of_points=50)

    # putting data to plot into lists
    volume_array1 = convert_units(new_fit_curve[0], 'bohr/atom', 'angstrom**3/atom')
    energy_array1 = convert_units(new_fit_curve[1], 'rydberg/atom', 'eV/atom')
    volume_list1 = [convert_units(new_fit_curve[0], 'bohr/atom', 'angstrom**3/atom')]
    energy_list1 = [convert_units(new_fit_curve[1], 'rydberg/atom', 'eV/atom')]
    bulk_modulus = convert_units(fit_eos_parameters[1], 'rydberg/bohr**3', 'gigapascals')

    volume_list2 = [convert_units(two_column_data[0], 'bohr/atom', 'angstrom**3/atom')]
    energy_list2 = [convert_units(two_column_data[1], 'rydberg/atom', 'eV/atom')]

    # plotting
    plt.plot(np.array(volume_array1), np.array(energy_array1), color='black')
    plt.plot(volume_list2, energy_list2, 'bo')

    x_range = max(volume_array1) - min(volume_array1)
    y_range = max(energy_array1) - min(energy_array1)
    x_limits = [min(volume_array1) - (0.1 * x_range), max(volume_array1) + (0.1 * x_range)]
    y_limits = [min(energy_array1) - (0.1 * y_range), max(energy_array1) + (0.1 * y_range)]

    plt.xlim(x_limits[0], x_limits[1])
    plt.ylim(y_limits[0], y_limits[1])
    plt.xlabel(r'$V\/(\mathrm{Å^3/atom})$')
    plt.ylabel(r'$E\/(\mathrm{eV/atom})$')

    # adding name to bottom left
    annotate_plot({'string': f"Created by Hillary :) \n {date.today().isoformat()}",
                   'position': np.array([min(volume_array1) - 0.1, min(energy_array1) - 0.3]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding crystal symbol to top left
    crystal_symbol_plot = None
    if parse_file_name()[1] == 'Fm-3m':
        crystal_symbol_plot = r"$Fm\overline{3}m$"
    else:
        crystal_symbol_plot = r"$Fd\overline{3}m$"

    annotate_plot({'string': f"{crystal_symbol_plot}",
                   'position': np.array([min(volume_array1) - 0.1, max(energy_array1) - 0.05]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding bulk modulus to top top left
    annotate_plot({'string': f"$K_0 = {bulk_modulus:.1f}\/$GPa",
                   'position': np.array([min(volume_array1) - 0.1, max(energy_array1) + 0.1]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding equilibrium volume
    """x_list = [volume_list1[energy_list1.index(min(energy_list1))],
              volume_list1[energy_list1.index(min(energy_list1))]]
    y_list = [min(energy_array1), y_limits[0]]
    vertical_line_y_max = min(energy_array1) - y_limits[0]
    plt.plot(x_list, y_list, 'k--')
    annotate_plot({'string': f"$V_0 = {fit_eos_parameters[3]:.2f}\/$GPa", 'position': np.array([0.6, 0.25]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})"""

    if display_graph == 'True':
        plt.show()
    else:
        exit()

    # Visualize Vectors in Space
    matrix = generate_matrix(min(volume_array1), max(volume_array1), number_of_dimensions=100,
                             potential_name='harmonic', potential_parameter=200)
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix)
    grid = np.linspace(-10, 10, dimension_number=100)
    if __eigenfunctions__[0] in eigenvectors:
        index = np.where(eigenvectors == __eigenfunctions__[0])[0]
        eigenvectors[index] = abs(eigenvectors[index])
    plt.plot(grid, eigenvectors[0], 'b-')
    plt.plot(grid, eigenvectors[1], 'g-')
    plt.plot(grid, eigenvectors[2], 'r-')
    plt.axhline(0, color='black')