import matplotlib as plt

"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""

# some constants (will eventually be moved to a text file)

# Saturn V
mass_saturn = 2800000  # kg
thrust_saturn = 34500000  # N
# Falcon 9
mass_falcon = 540054  # kg
thrust_falcon = 7607000  # N
# SLS Block 1
mass_block = 26082156  # kg
thrust_block = 3991613  # N  !!! fact check this !!!


def total_mass():
    rocket_mass_array = [mass_saturn, mass_falcon, mass_block]
    payload = 8300  # kg, the largest payload possible that can be used by all three rockets
    collective_mass = payload + rocket_mass_array[0]
    return collective_mass


def rocket_simulation(collective_mass):
    thrust_array = [thrust_saturn, thrust_falcon, thrust_block]
    time = 0
    dt = 0.1  # change in time
    dm = 0.1  # change in mass
    gravity = -9.81  # m/s/s
    initial_velocity = 0
    position_array = []
    velocity_array = []
    acceleration_array = []
    position = initial_velocity * time + (1 / 2) * ((thrust_array[0] - gravity) / (collective_mass - dm)) * time ** 2
    velocity = (thrust_array[0] - gravity) / (collective_mass - dm) * time
    acceleration = (thrust_array[0] - (collective_mass - dm) * gravity) / (collective_mass - dm)
    position_array.append(position)
    velocity_array.append(velocity)
    acceleration_array.append(acceleration)
    time = time + dt
    collective_mass = collective_mass - dm
    return position_array, velocity_array, acceleration_array


print(rocket_simulation(total_mass())[0])

"""
plt.plot()
"""
