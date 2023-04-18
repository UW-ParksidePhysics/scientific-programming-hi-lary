import matplotlib.pyplot as plt
import numpy as np

"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""

time_range = np.arange(0, 601, 0.1)


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
    dm = 0.1  # change in mass
    gravity = 9.81  # m/s/s
    initial_velocity = 0
    # lists to be plotted
    position_list = []
    velocity_list = []
    acceleration_list = []
    for t in time_range:
        position = initial_velocity * (time + t) + (1 / 2) * \
                   (thrust_array - gravity) / (collective_mass_array - dm) * (time + t) ** 2
        velocity = (thrust_array - gravity) / (collective_mass_array - dm) * (time + t)
        acceleration = thrust_array - ((collective_mass_array - dm) * gravity) / (collective_mass_array - dm)
        position_list.append(position)
        velocity_list.append(velocity)
        acceleration_list.append(acceleration)
        collective_mass_array = collective_mass_array - dm
       # for mass in collective_mass_array:
           # collective_mass_array.pop(mass)
           # new_mass = mass - dm
            #collective_mass_array.append(new_mass)
    return position_list, velocity_list, acceleration_list


# print(total_mass())
# print(rocket_simulation(total_mass())[0])
# print(saturn_rocket_simulation(total_mass())[1])
# print(saturn_rocket_simulation(total_mass())[2])


# position plot
plt.plot(time_range, rocket_simulation(total_mass())[0])
plt.title('Position v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (meters)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

# velocity plot
plt.plot(time_range, rocket_simulation(total_mass())[1])
plt.title('Velocity v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (meters/second)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

# acceleration plot
plt.plot(time_range, rocket_simulation(total_mass())[2])
plt.title('Acceleration v Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (meters/second/second)')
plt.legend(['Saturn V', 'Falcon 9', 'SLS Block 1'])
plt.show()

