import matplotlib.pyplot as plt
import numpy as np

"""
This code contains information on the rockets Saturn V, Falcon 9, and SLS Block 1.
The goal is to produce the following plots:
position v time
velocity v time
acceleration v time
mass v time
"""

time_range = np.arange(0, 601, 0.1)  # 600 seconds = 10 minutes (enough time to get to orbit)


def total_mass():
    # mass constants
    mass_saturn = 2800000  # kg
    mass_falcon = 540054  # kg
    mass_block = 26082156  # kg
    # build a mass array
    rocket_mass_array = np.array([mass_saturn, mass_falcon, mass_block])
    payload = 8300  # kg, the largest payload possible that can be used by all three rockets
    collective_mass_array = rocket_mass_array + payload
    return collective_mass_array


def rocket_simulation(collective_mass_array):
    # thrust constants to build thrust array
    thrust_saturn = 34500000  # N
    thrust_falcon = 7607000  # N
    thrust_block = 3991613  # N  !!! fact check this !!!
    thrust_array = np.array([thrust_saturn, thrust_falcon, thrust_block])
    # other constants
    time = 0
    dm = 20000 / 600  # change in mass i.e. payload / time range
    gravity = 9.81  # m/s/s
    initial_velocity = 0
    # lists to be plotted
    position_list = []
    velocity_list = []
    acceleration_list = []
    mass_list = []
    for t in time_range:
        position = initial_velocity * (time + t) + (1 / 2) * \
                   (thrust_array - gravity) / (collective_mass_array - dm) * (time + t) ** 2
        velocity = (thrust_array - gravity) / (collective_mass_array - dm) * (time + t)
        acceleration = thrust_array - ((collective_mass_array - dm) * gravity) / (collective_mass_array - dm)
        position_list.append(position)
        velocity_list.append(velocity)
        acceleration_list.append(acceleration)
        mass_list.append(collective_mass_array)
        collective_mass_array = collective_mass_array - dm  # update change in mass
    return [[position_list, velocity_list], [acceleration_list, mass_list]]


def plots():
    output_list = rocket_simulation(total_mass())
    figure, axes = plt.subplots(nrows=2, ncols=2, layout='constrained')
    for row_index, row in enumerate(output_list):
        for column_index, column in enumerate(row):
            axes[row_index][column_index].plot(time_range, column)
            axes[row_index][column_index].set_xlabel('Time (seconds)')
            axes[0][0].set_ylabel('Position (meters)')
            axes[0][0].set_title('Position v Time')
            axes[0][1].set_ylabel('Velocity (m/s)')
            axes[0][1].set_title('Velocity v Time')
            axes[1][0].set_ylabel('Acceleration (m/s/s)')
            axes[1][0].set_title('Acceleration v Time')
            axes[1][1].set_ylabel('Mass (kg)')
            axes[1][1].set_title('Mass v Time')
    return


plots()
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()
exit()

"""
# position plot
plt.plot(time_range, positions)
plt.title('Position v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (meters)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

# velocity plot
plt.plot(time_range, velocities)
plt.title('Velocity v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (meters/second)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

# acceleration plot
plt.plot(time_range, accelerations)
plt.title('Acceleration v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (meters/second/second)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

# mass v time
plt.plot(time_range, masses)
plt.show()
"""
