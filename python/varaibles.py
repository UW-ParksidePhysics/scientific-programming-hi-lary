time = 1.0  # s
initial_position = 10.0  # m
initial_velocity = 0.0  # m/s
gravitational_acceleration = 10.0  # m/s/s

position = initial_position \
           + initial_velocity * time \
           - 0.5 * gravitational_acceleration * time ** 2

print(f'y({time:.0e} s, y0 = {initial_position} m, v0 = {initial_velocity} m/s) = {position} m')
