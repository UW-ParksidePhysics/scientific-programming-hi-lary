import vpython as vp

initial_position_one = vp.vector(-10., -10, 0.)
initial_velocity_one = vp.vector(25., 25, 0.)
ball_one = vp.sphere(pos=initial_position_one, radius=0.5, color=vp.color.blue, make_trail=True)
initial_position_two = vp.vector(-10., 10, 0.)
initial_velocity_two = vp.vector(25., -25, 0.)
ball_two = vp.sphere(pos=initial_position_two, radius=0.5, color=vp.color.yellow, make_trail=True)

wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 1.

time = 0.
ball_velocity_one = initial_velocity_one
ball_velocity_two = initial_velocity_two
while time < stop_time:
    vp.rate(rate_of_animation)
    if ball_one.pos.x > wall.pos.x:
        ball_velocity_one.x = -ball_velocity_one.x  # reverse ball velocity
    ball_one.pos.x += ball_velocity_one.x * time_step
    ball_one.pos.y += ball_velocity_one.y * time_step
    ball_one.pos.z += ball_velocity_one.z * time_step
    if ball_two.pos.x > wall.pos.x:
        ball_velocity_two.x = -ball_velocity_two.x
    ball_two.pos.x += ball_velocity_two.x * time_step
    ball_two.pos.y += ball_velocity_two.y * time_step
    ball_two.pos.z += ball_velocity_two.z * time_step
    time += time_step
