from vpython import *
import time
# import matplotlib.pyplot as plt
# import numpy

scene=canvas()

# Adjust string length, size of bob
sh=115
sa=20


# Stand and clamp
base = box(size=vector(30.0,2.0,30.0), pos=vector(0,0,0),color=color.orange)
rod = cylinder(radius=2.0, axis=vector(0,sh+5,0),pos=vector(0,1,0),)
arm = cylinder(radius=2.0, axis=vector(0,0,sa),pos=vector(0,sh,0))

# Thread and bob
l = 100
thread = cylinder(radius=0.2, axis=vector(0,-l,0),pos=vector(0,sh,sa))
ball = sphere(radius=5.0,pos=vector(0,sh-l-5.0,sa),color=color.red)

# Adjust initial angle
init_angle = 10 / 360 * 2 * pi
# Adjust damping
damping = 0


num_osc = 20
g = 9.81
starting_pos = vector((l+5.0)*sin(init_angle),sh-(l+5.0)*cos(init_angle),sa)


velo = arrow(pos=ball.pos,shaftwidth=2,axis=vector(0,0,0))

curr_angle = init_angle
curr_pos = starting_pos
ball.pos = curr_pos
thread.axis = curr_pos - thread.pos
time.sleep(2)

da = 0
dda = 0
dt = 0.01
t = 0

ballvelo=vector(0,0,0)
init_time = time.time()
peaks = 20
curr_peak = 0

# Graph settings
gr = graph(title='quantity against time graph', xtitle='q', ytitle='t', xmin=0, ymin=-100)
gr2 = graph(title='quantity against time graph', xtitle='q', ytitle='t', xmin=0, ymin=-100)
gr3 = graph(title='quantity against time graph', xtitle='q', ytitle='t', xmin=0, ymin=-100)
gx = gcurve(color=color.red, label="velocity", graph=gr)
gy = gcurve(color=color.blue, label="displacement", graph=gr2)
gz = gcurve(color=color.green, label="acceleration", graph=gr3)

# Starting the simulation
while time.time() - init_time < 20.0 and curr_peak < peaks * 2:
    rate(100)
    dda = -g * sin(curr_angle) / l - damping * da
    da += dda
    ballvelo.x = da * l * cos(curr_angle)
    ballvelo.y = da * l * sin(curr_angle)
    curr_angle += da * dt
    x = (l+5.0)*sin(curr_angle)
    y = sh -(l+5.0)*cos(curr_angle)
    curr_pos.x = x
    curr_pos.y = y
    ball.pos = curr_pos
    velo.pos = curr_pos
    velo.axis = ballvelo * 0.2
    thread.axis = curr_pos - thread.pos
    # print((ballvelo.x/abs(ballvelo.x)*sqrt(ballvelo.x**2+ballvelo.y**2)))
    if ballvelo.x == 0:
        gx.plot(t,0)
    else:
        gx.plot(t,(ballvelo.x/abs(ballvelo.x)*sqrt(ballvelo.x**2+ballvelo.y**2)))
    if curr_angle == 0:
        gy.plot(t,0)
    else:
        gy.plot(t,(curr_angle/abs(curr_angle))*sqrt((x-0)**2+(y-sh+(l+5.0))**2))
    gz.plot(t,da * l)
    if ballvelo.x == 0:
        curr_peak += 1
    t += dt
    pass