from read_two_column_text import read_two_column_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
import numpy as np

if __name__ == "__main__":
    filename = 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'


    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        return filename_split




    print(read_two_column_text(filename))

# def make_data_arrays():
     #    infile = open(filename, 'r').readlines()
     #    # 1st column is volumes_cells, 2nd column is total_energies
     #    volumes_cells = np.array([])
     #    total_energies = np.array([])
     #    for line in infile:
     #        words = line.split()
     #        first = float(words[0][0:-4])*10**1
     #        second = float(words[1][0:-4])*10**3
     #        volumes_cells = np.append(volumes_cells, first)
     #        total_energies = np.append(total_energies, second)
     #    return [volumes_cells, total_energies]