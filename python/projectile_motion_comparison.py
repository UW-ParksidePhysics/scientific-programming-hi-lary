import vpython as vp

# text
Earth = vp.text(text="EARTH", pos=vp.vector(10, 5, -2), align='center', height=1, color=vp.color.green,
                axis=vp.vector(1, 0, 0), up=vp.vector(0, 0, 1))
Mars = vp.text(text="MARS", pos=vp.vector(0, -5, -2), align='center', height=1, color=vp.color.red,
               axis=vp.vector(1, 0, 0), up=vp.vector(0, 0, 1))
Moon = vp.text(text="MOON", pos=vp.vector(-10, -15, -2), align='center', height=1, color=vp.color.gray(0.5),
               axis=vp.vector(1, 0, 0), up=vp.vector(0, 0, 1))

# constants and scenes
earth_gravity = -9.81  # m/s/s
scene_earth = vp.box(pos=vp.vector(10, 10, 0), size=vp.vector(10, 10, 0.5), color=vp.color.green)
mars_gravity = -3.7  # m/s/s
scene_mars = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(10, 10, 0.5), color=vp.color.red)
moon_gravity = -1.7  # m/s/s
scene_moon = vp.box(pos=vp.vector(-10, -10, 0), size=vp.vector(10, 10, 0.5), color=vp.color.gray(0.5))

box_thickness = 0.5
sphere_radius = 0.5
# earth sphere
initial_pos_earth = vp.vector(5, 5, box_thickness + sphere_radius)
initial_vel_earth = vp.vector(1, 1, 10)
ball_earth = vp.sphere(pos=initial_pos_earth, radius=sphere_radius, color=vp.color.blue, make_trail=True)
# mars sphere
initial_pos_mars = vp.vector(-5, -5, box_thickness + sphere_radius)
initial_vel_mars = vp.vector(1, 1, 10)
ball_mars = vp.sphere(pos=initial_pos_mars, radius=sphere_radius, color=vp.color.magenta, make_trail=True)
# moon sphere
initial_pos_moon = vp.vector(-15, -15, box_thickness + sphere_radius)
initial_pos_earth = vp.vector(5, 5, box_thickness+sphere_radius)
initial_vel_earth = vp.vector(1, 1, 10)
ball_earth = vp.sphere(pos=initial_pos_earth, radius=sphere_radius, color=vp.color.blue, make_trail=True)
# mars sphere
initial_pos_mars = vp.vector(-5, -5, box_thickness+sphere_radius)
initial_vel_mars = vp.vector(1, 1, 10)
ball_mars = vp.sphere(pos=initial_pos_mars, radius=sphere_radius, color=vp.color.magenta, make_trail=True)
# moon sphere
initial_pos_moon = vp.vector(-15, -15, box_thickness+sphere_radius)
initial_vel_moon = vp.vector(1, 1, 10)
ball_moon = vp.sphere(pos=initial_pos_moon, radius=sphere_radius, color=vp.color.white, make_trail=True)

# for animation
animation_time_step = 0.01  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.005
time = 0.

vp.scene.forward = vp.vec(-0.5, 3.0, -2.0)

# earth loop
while ball_earth.pos.z >= box_thickness + sphere_radius:
    vp.rate(rate_of_animation)
    ball_vel_earth = initial_vel_earth.z + earth_gravity * time  # vo + a*t
    if ball_earth.pos.z < box_thickness + sphere_radius:
        initial_vel_earth.x = 0
        initial_vel_earth.y = 0
        initial_vel_earth.z = 0
    ball_earth.pos.x += initial_vel_earth.x * time_step
    ball_earth.pos.y += initial_vel_earth.y * time_step
    ball_earth.pos.z += ball_vel_earth * time_step

    time += time_step

time = 0
# mars loop
while ball_mars.pos.z >= box_thickness + sphere_radius:
    vp.rate(rate_of_animation)
    ball_vel_mars = initial_vel_mars.z + mars_gravity * time  # vo + a*t
    if ball_mars.pos.z < 1:
        initial_vel_mars.x = 0
        initial_vel_mars.y = 0
        initial_vel_mars.z = 0

    ball_mars.pos.x += initial_vel_mars.x * time_step
    ball_mars.pos.y += initial_vel_mars.y * time_step
    ball_mars.pos.z += ball_vel_mars * time_step

    time += time_step

time = 0
# moon loop
while ball_moon.pos.z >= box_thickness + sphere_radius:
    vp.rate(rate_of_animation)
    ball_vel_moon = initial_vel_moon.z + moon_gravity * time  # vo + a*t
    # if ball_moon.pos.z < 1:
    #     initial_vel_moon.x = 0
    #     initial_vel_moon.y = 0
    #     initial_vel_moon.z = 0

    if ball_moon.pos.z >= 1:
        ball_moon.pos.x += initial_vel_moon.x * time_step
        ball_moon.pos.y += initial_vel_moon.y * time_step
        ball_moon.pos.z += ball_vel_moon * time_step
    else:
        break

    time += time_step
