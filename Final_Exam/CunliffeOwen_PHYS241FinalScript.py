"""import Final_Exam_Review"""
"from Final_Exam_Review import read_two_column_text, calculate_bivariate_statistics, calculate_quadratic_fit"
"from Final_Exam_Review import calculate_lowest_eigenvectors, fit_curve_array, plot_data_with_fit"
"from Final_Exam_Review import annotate_plot"
import os
import numpy as np

# infile = r"C:\\Users\\cunli003\\Downloads\\Sn.Fd-3m.GGA-PBE.volumes_energies.dat"
# head, tail = os.path.split(infile)
# print(head, tail)

if __name__ == "__main__":
    filename = 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'


    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        return filename_split


    def make_data_arrays():
        infile = open(filename, 'r').readlines()
        # 1st column is volumes_cells, 2nd column is total_energies
        volumes_cells = np.array([])
        total_energies = np.array([])
        for line in infile:
            words = line.split()
            first = float(words[0][0:-4])*10**1
            second = float(words[1][0:-4])*10**3
            volumes_cells = np.append(volumes_cells, first)
            total_energies = np.append(total_energies, second)
        return [volumes_cells, total_energies]


    print(make_data_arrays())
