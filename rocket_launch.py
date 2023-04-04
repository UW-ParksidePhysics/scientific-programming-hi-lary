"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""

# some constants (will eventually be moved to a text file)
payload = 8300  # kg, the largest payload possible that can be used by all three rockets
gravity = -9.81  # m/s/s
# Saturn V
mass_saturn = 2800000  # kg
thrust_saturn = 34500000  # N
# Falcon 9
mass_falcon = 540054  # kg
thrust_falcon = 7607000  # N
# SLS Block 1
mass_block = 26082156  # kg
thrust_block = 3991613  # N  !!! fact check this !!!


# position as a function of time
def position(mass, thrust, time):
    position =
