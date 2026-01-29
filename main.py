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
dt = 1
n = int(tf // dt)


# State space, 2D satellite
# x, u, y, v
x0 = np.array([[5, 1],
               [10, 0]])

x = 0

# I always keep forgetting the syntax for numpy
print(x0[0, 0])
print(x0[1, 0])

# Same goes for matplotlib
fig, ax = plt.subplots()


r = sqrt(x0[0,0]**2 + x0[1,0]**2)

for i in range(0,n):
    acc = -mu * r/ (r**3)

    # Distance changes
    x0[0, 0] = x0[0, 1]*dt + x0[0, 0]
    x0[1, 0] = x0[1, 1]*dt + x0[1, 0]

    # Velocity changes
    x0[0, 1] = acc * dt + x0[0, 1]
    x0[1, 1] = acc * dt + x0[1, 1]



    # print("u = " , x0[0, 1] , "v = " , x0[1, 1])
    # print("x = " , x0[0, 0] , "y = " , x0[1, 0])
