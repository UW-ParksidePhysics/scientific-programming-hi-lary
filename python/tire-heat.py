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


# # Draft code comments
#
# Does the code run without error?
# If any error occurs, can you suggest a potential fix?
"""The code runs nicely and produces a lovely graph."""
# How understandable is the output of the code?
# Point out any parts you do not understand.
"""The graph is labeled well, though I am unsure what the numbers next to the different colors mean.
I'm assuming that they are all different tires."""
# How readable is the code itself?
# Say where formatting or commenting would make the code more readable or where PEP-8 is violated.
"""Fairly readable. In the beginning I am unsure where the masses array (line 13) comes from and the url data (line 26) 
comes from, but aside from that, everything is clear."""
# How clearly do the code comments describe the problem it is trying to solve?
# Identify places that would benefit from a clearer comment.
"""Starting at line 49, I am unsure about the specifics of what the code is doing."""
# How clearly do the variable names relate to the concepts they concretize?
# Point out any variables you don't recognize, and/or suggest better names. Check for PEP-8 compliance.
"""Variable names make sense and are labeled with units, good job."""
# How well does the range of variables capture the problem described?
# Identify extraneous regions that could be left out or important regions that should be included.
"""It seems that all variables defined are used when appropriate."""
# To what degree does the script follow a functional programming paradigm, packaging all major components of the script
# into separately defined functions that pass information among them in a small number of lines? Identify ways in which
# the functionalization of the code could be improved.
"""The steps taken in the code is overall very linear as in it goes step by step in order to solve the given problem.
The code functions well."""
# How clearly do the visualizations show the solutions to the problem?
"""The visualization clearly shows the relationship of velocity and temperature and is aesthetically pleasing."""
# Say if there is extraneous whitespace or the co-domain or domain of the data should be changed or any other ways the
# visualizations could be more effective
"""At first glance, no obvious domain issues."""
