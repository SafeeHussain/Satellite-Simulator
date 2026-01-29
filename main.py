# import PySide6.QtCore

# Importing functions
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


# Earth radius, radius of the earth to be added onto
Earth_Radius = 6371e3
Orbit_Radius = 20e3
# Total satellite radius
Radius = Earth_Radius + Orbit_Radius
print(Radius)

# Standard gravitational parameter
mu = 3.986e14

# time settings
t0 = 0
tf = 6000
dt = 0.1
n = int(tf // dt)


# State space, 2D satellite
# x, u, y, v
x = [Radius]
y = [0.0]
u = [0.0]
v = [10000.0]


# I always keep forgetting the syntax for numpy
# print(x0[0, 0])
# print(x0[1, 0])

# Same goes for matplotlib
fig, ax = plt.subplots(figsize=(7, 7), dpi=200)


# r = sqrt(x0[0,0]**2 + x0[1,0]**2)
r = sqrt(x[0]**2 + y[0]**2)

for i in range(0,n):
    acc_x = -mu * x[i] / (r**3)
    acc_y = -mu * y[i] / (r**3)
    print(acc_x)

    # Distance changes
    x.append(u[i]*dt + x[i])
    y.append(v[i]*dt + y[i])
    # x0[0, 0] = x0[0, 1]*dt + x0[0, 0]
    # x0[1, 0] = x0[1, 1]*dt + x0[1, 0]

    # Velocity changes
    u.append(u[i] + acc_x*dt)
    v.append(v[i] + acc_y*dt)
    # x0[0, 1] = acc * dt + x0[0, 1]
    # x0[1, 1] = acc * dt + x0[1, 1]



# print("x = " , x , "y = " , y)

plt.plot(x, y)

