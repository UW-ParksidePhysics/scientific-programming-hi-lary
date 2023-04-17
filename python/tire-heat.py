import numpy as np
import matplotlib.pyplot as plt


def calculate_final_temperature(masses, specific_heat, initial_speed, initial_temperature):
    """
    calculates the final temperature by equating the kinetic energy change to heat flow
    :param masses: list [heat sink mass, kinetic mass]
    :param specific_heat:
    :param initial_speed:
    :param initial_temperature:
    :return:  final_temperature
    """
    mass_ratio = sum(masses) / masses[0]
    final_temperature = 0.5 * (mass_ratio/specific_heat) * initial_speed ** 2 + initial_temperature
    return final_temperature


def extract_tire_data(url):
    """

    :param url:
    :return: speed ratings, tire load indexes
    """
    import pandas as pd
    url_tables=pd.read_html(url)
    speed_ratings=url_tables[0]
    tire_load_indexes=url_tables[1]
    return speed_ratings, tire_load_indexes

def convert_units(input_value, input_units, output_units):
    """

    :param input_value:
    :param input_units:
    :param output_units:
    :return: output value in output units
    """
    miles_to_meters = 1609.344
    hours_to_seconds = 3600
    pounds_to_kilograms = 0.45359237
    if input_units == 'mph' and output_units == 'm/s':
        output_value = input_value * miles_to_meters/hours_to_seconds
    elif input_units == 'lbs' and output_units == 'kg':
        output_value = input_value * pounds_to_kilograms
    return output_value


if __name__  == "__main__":
    print("calculating tire heat")

    tire_data_url = 'https://www.justtires.com/en-US/learn/load-index-speed-rating'
    ratings, load_indexes = extract_tire_data(tire_data_url)
    tire_speed_ratings = ratings['Maximum speed (MPH)'][0:7].astype('float').to_numpy()
    tire_load = load_indexes['Load (lbs)'].astype('float').to_numpy()
    tire_speed_ratings = convert_units(tire_speed_ratings, 'mph', 'm/s')
    tire_load = convert_units(tire_load, 'lbs', 'kg')

  # https://www.matweb.com/search/datasheet_print.aspx?matguid=6588439546ac4492965c894ddff3f5da
    tire_specific_heat = 0.440  ## J/g°C
    tire_mass = convert_units(18, 'lbs', 'kg')

    starting_temperature = 273.15 + 25
    for load in tire_load:
        total_mass = 4 * (tire_mass + load)
        print(total_mass)
        temperatures = calculate_final_temperature([tire_mass, total_mass], tire_specific_heat, tire_speed_ratings,
                                                   starting_temperature)

        plt.plot(tire_speed_ratings, temperatures-starting_temperature, label=f'{load:.0f}')
# label the x-axis using xlabel, label y-axis using ylabel, create a le,gend using
    #labelequals in play command plt.function
    plt.xlabel("Velocity at the start of the skid [m/s]")
    plt.ylabel("Temperature change of tire [K]")

    plt.legend()
    plt.show()

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

""" In this draft I have defined all my variables which get used in the functions, and I've defined my functions
    which output the final tension and frequency for each string and the displacement it undergoes.  There are six
    different displacements used and they are defined in a list/array.  The output of the tension function is used 
    in the frequency function, and then the output of the frequency function is graphed against the displacement"""

string_length = 0.6477  # meters
spring_constant_individual = 2000  # N/m

""" There are three identical springs that act on the bridge in the same direction with the same displacement so the 
    so this can be written as a single spring with a spring constant three times greater than the individual springs"""
spring_constant_system = 6000  # N/m

# Tension of each string at equilibrium (t_initial):
t_initial_high_e = 70.87  # N
t_initial_b = 68.15  # N
t_initial_g = 73.62  # N
t_initial_d = 80.77  # N
t_initial_a = 85.57  # N
t_initial_low_e = 77.41  # N

# mass of each string
mass_high_e = 3.85e-4  # kg
mass_b = 6.94e-4  # kg
mass_g = 1.19e-3  # kg
mass_d = 2.19e-3  # kg
mass_a = 4.18e-3  # kg
mass_low_e = 6.69e-3  # kg

# initial frequencies of each string
f_initial_high_e = 329.63  # Hz
f_initial_b = 246.94  # Hz
f_initial_g = 196.00  # Hz
f_initial_d = 146.83  # Hz
f_initial_a = 110.00  # Hz
f_initial_low_e = 82.41  # Hz

f_initial = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
displacement = [0.000, 0.001, 0.002, 0.004, 0.006, 0.008]  # meters


def t_final_high_e(displacement):
    t_final_high_e_array = []
    for i in displacement:
        t_final = t_initial_high_e - spring_constant_system * i
        tension = "{:.2f}".format(t_final)
        t_final_high_e_array.append(tension)
    return t_final_high_e_array


print(f'The final tension of the high E string after each respective displacement is {t_final_high_e(displacement)} \
Newtons')


def f_final_high_e(displacement):
    f_final_high_e_array = []
    for i in displacement:
        f_final = (1 / (2 * string_length)) * \
                  sqrt((t_initial_high_e - spring_constant_system * i) / (mass_high_e / string_length))
        frequency = "{:.2f}".format(f_final)
        f_final_high_e_array.append(frequency)
    return f_final_high_e_array


print(f'The final frequency of the the high E string after each respective displacement and resulting change in \
tension is {f_final_high_e(displacement)} Hz')
print()

f_high_e = []
for i in f_final_high_e(displacement):
    f_high_e.append(f_final_high_e(displacement))

x_values = displacement
y_values1 = f_initial
y_values2 = f_high_e[0]

plt.plot(x_values, y_values2)
plt.xlabel('Displacement')
plt.ylabel('Frequency')
plt.show()

# each subsequent function does the same thing for every string except they don't have the plotting

#
# def t_final_b(displacement):
#     t_final_b_array = []
#     for i in displacement:
#         t_final = t_initial_b - spring_constant_system * i
#         tension = "{:.2f}".format(t_final)
#         t_final_b_array.append(tension)
#     return t_final_b_array
#
#
# print(f'The final tension of the B string after each respective displacement is {t_final_b(displacement)} \
# Newtons')
#
#
# def f_final_b(displacement):
#     f_final_b_array = []
#     for i in displacement:
#         f_final = (1 / (2 * string_length)) * \
#                     sqrt((t_initial_b - spring_constant_system * i) / (mass_b / string_length))
#         frequency = "{:.2f}".format(f_final)
#         f_final_b_array.append(frequency)
#     return f_final_b_array
#
#
# print(f'The final frequency of the the B string after each respective displacement and resulting change in \
# tension is {f_final_b(displacement)} Hz')
# print()
#
# def t_final_g(displacement):
#     t_final_g_array = []
#     for i in displacement:
#         t_final = t_initial_g - spring_constant_system * i
#         tension = "{:.2f}".format(t_final)
#         t_final_g_array.append(tension)
#     return t_final_g_array
#
#
# print(f'The final tension of the G string after each respective displacement is {t_final_g(displacement)} \
# Newtons')
#
#
# def f_final_g(displacement):
#     f_final_g_array = []
#     for i in displacement:
#         f_final = (1 / (2 * string_length)) * \
#                     sqrt((t_initial_g - spring_constant_system * i) / (mass_g / string_length))
#         frequency = "{:.2f}".format(f_final)
#         f_final_g_array.append(frequency)
#     return f_final_g_array
#
#
# print(f'The final frequency of the the G string after each respective displacement and resulting change in \
# tension is {f_final_g(displacement)} Hz')
# print()
#
# def t_final_d(displacement):
#     t_final_d_array = []
#     for i in displacement:
#         t_final = t_initial_d - spring_constant_system * i
#         tension = "{:.2f}".format(t_final)
#         t_final_d_array.append(tension)
#     return t_final_d_array
#
#
# print(f'The final tension of the D string after each respective displacement is {t_final_d(displacement)} \
# Newtons')
#
#
# def f_final_d(displacement):
#     f_final_d_array = []
#     for i in displacement:
#         f_final = (1 / (2 * string_length)) * \
#                     sqrt((t_initial_d - spring_constant_system * i) / (mass_d / string_length))
#         frequency = "{:.2f}".format(f_final)
#         f_final_d_array.append(frequency)
#     return f_final_d_array
#
#
# print(f'The final frequency of the the D string after each respective displacement and resulting change in \
# tension is {f_final_d(displacement)} Hz')
# print()
#
# def t_final_a(displacement):
#     t_final_a_array = []
#     for i in displacement:
#         t_final = t_initial_a - spring_constant_system * i
#         tension = "{:.2f}".format(t_final)
#         t_final_a_array.append(tension)
#     return t_final_a_array
#
#
# print(f'The final tension of the A string after each respective displacement is {t_final_a(displacement)} \
# Newtons')
#
#
# def f_final_a(displacement):
#     f_final_a_array = []
#     for i in displacement:
#         f_final = (1 / (2 * string_length)) * \
#                     sqrt((t_initial_a - spring_constant_system * i) / (mass_a / string_length))
#         frequency = "{:.2f}".format(f_final)
#         f_final_a_array.append(frequency)
#     return f_final_a_array
#
#
# print(f'The final frequency of the the A string after each respective displacement and resulting change in \
# tension is {f_final_a(displacement)} Hz')
# print()
#
# def t_final_low_e(displacement):
#     t_final_low_e_array = []
#     for i in displacement:
#         t_final = t_initial_low_e - spring_constant_system * i
#         tension = "{:.2f}".format(t_final)
#         t_final_low_e_array.append(tension)
#     return t_final_low_e_array
#
#
# print(f'The final tension of the low E string after each respective displacement is {t_final_low_e(displacement)} \
# Newtons')
#
#
# def f_final_low_e(displacement):
#     f_final_low_e_array = []
#     for i in displacement:
#         f_final = (1 / (2 * string_length)) * \
#                     sqrt((t_initial_low_e - spring_constant_system * i) / (mass_low_e / string_length))
#         frequency = "{:.2f}".format(f_final)
#         f_final_low_e_array.append(frequency)
#     return f_final_low_e_array
#
#
# print(f'The final frequency of the the low E string after each respective displacement and resulting change in \
# tension is {f_final_low_e(displacement)} Hz')


# # Draft code comments
#
# Does the code run without error?
# If any error occurs, can you suggest a potential fix?
#
# How understandable is the output of the code?
# Point out any parts you do not understand.
#
# How readable is the code itself?
# Say where formatting or commenting would make the code more readable or where PEP-8 is violated.
#
# How clearly do the code comments describe the problem it is trying to solve?
# Identify places that would benefit from a clearer comment.
#
# How clearly do the variable names relate to the concepts they concretize?
# Point out any variables you don't recognize, and/or suggest better names. Check for PEP-8 compliance.
#
# How well does the range of variables capture the problem described?
# Identify extraneous regions that could be left out or important regions that should be included.
#
# To what degree does the script follow a functional programming paradigm, packaging all major components of the script
# into separately defined functions that pass information among them in a small number of lines? Identify ways in which
# the functionalization of the code could be improved.
# How clearly do the visualizations show the solutions to the problem?
#
# Say if there is extraneous whitespace or the co-domain or domain of the data should be changed or any other ways the
# visualizations could be more effective
#
