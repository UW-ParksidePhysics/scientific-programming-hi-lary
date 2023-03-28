import vpython as vp

initial_position_one = vp.vector(1, 2, 3)
initial_velocity_one = vp.vector(1, 1, 1)
ball_one = vp.sphere(pos=initial_position_one, radius=0.1, color=vp.color.yellow, make_trail=True)
initial_position_two = vp.vector(4, 5, 6)
initial_velocity_two = vp.vector(-1, -1, -1)
ball_two = vp.sphere(pos=initial_position_two, radius=0.1, color=vp.color.purple, make_trail=True)

animation_time_step = 0.1  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x_one = initial_position_one.x + initial_velocity_one.x * time
    y_one = initial_position_one.y + initial_velocity_one.y * time
    z_one = initial_position_one.z + initial_velocity_one.z * time
    ball_one.pos = vp.vector(x_one, y_one, z_one)
    x_two = initial_position_two.x + initial_velocity_two.x * time
    y_two = initial_position_two.y + initial_velocity_two.y * time
    z_two = initial_position_two.z + initial_velocity_two.z * time
    ball_two.pos = vp.vector(x_two, y_two, z_two)
    time += time_step
