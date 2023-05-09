from read_two_column_text import read_two_column_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
from equations_of_state import *
from convert_units import convert_units
import numpy as np

if __name__ == "__main__":
    filename = 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'


    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        chemical_symbol = filename_split[0]
        crystal_symbol = filename_split[1]
        density_correlation = filename_split[2]
        return chemical_symbol, crystal_symbol, density_correlation


    two_column_data = (read_two_column_text(filename)) / 2
    statistical_data = calculate_bivariate_statistics(two_column_data)
    quad_fit_data = calculate_quadratic_fit(two_column_data)
    fit_eos_curve, fit_eos_parameters = fit_eos(statistical_data[0], statistical_data[1],
                                                quad_fit_data, eos='birch-murnaghan')
    x_fit_curve = fit_curve_array(quad_fit_data, statistical_data[2], statistical_data[3], number_of_points=50)
    volume_list1 = [convert_units(volume, 'bohr/atom', 'angstrom**3/atom') for volume in x_fit_curve[0]]
    energy_list1 = [convert_units(energy, 'rydberg/atom', 'eV/atom') for energy in x_fit_curve[1]]
    bulk_modulus = convert_units(eos_parameters[1], 'rydberg/bohr**3', 'gigapascals')

    volume_list2 = [convert_units(volume, 'bohr/atom', 'angstrom**3/atom') for volume in two_column_data[0]]
    energy_list2 = [convert_units(energy, 'rydberg/atom', 'eV/atom') for energy in two_column_data[1]]

    plt.plot(volume_list1, energy_list1, 'black')
    plt.plot(volume_list2, energy_list2, 'bo')

    plt.show()

