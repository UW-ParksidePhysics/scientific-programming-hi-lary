"""import Final_Exam_Review"""
"from Final_Exam_Review import read_two_column_text, calculate_bivariate_statistics, calculate_quadratic_fit"
"from Final_Exam_Review import calculate_lowest_eigenvectors, fit_curve_array, plot_data_with_fit"
"from Final_Exam_Review import annotate_plot"
import os

# infile = r"C:\\Users\\cunli003\\Downloads\\Sn.Fd-3m.GGA-PBE.volumes_energies.dat"
# head, tail = os.path.split(infile)
# print(head, tail)

if __name__ == "__main__":
    def parse_file_name():
        filename = 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'
        filename_split = filename.split(".")[0:3]
        # infile = open(filename, 'r')
        # print(filename_split)
        return filename_split


    print(parse_file_name())
