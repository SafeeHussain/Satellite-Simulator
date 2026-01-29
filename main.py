# import PySide6.QtCore

# Importing functions
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
tf = 8000
dt = 0.1
n = int(tf // dt)


# State space, 2D satellite

# Using single lists
# x, u, y, v
# x = [Radius]
# y = [0.0]
# u = [0.0]
# v = [10000.0]

# Using Data Frames
# x0 = pd.DataFrame(
#     {
#         "x": [Radius],
#         "y": [0.0],
#         "u": [0.0],
#         "v": [1000.0],
#     }
# )

cols = ["x", "y", "u", "v"]
x0 = pd.DataFrame(np.nan, index=range(n+1), columns=cols)

x0.loc[0] = [Radius, 0.0, 0.0, 1000.0]  # set initial state


print(x0.iloc[0, 0])


# I always keep forgetting the syntax for numpy
# print(x0[0, 0])
# print(x0[1, 0])

# Same goes for matplotlib
fig, ax = plt.subplots(figsize=(7, 7), dpi=200)


# r = sqrt(x[0]**2 + y[0]**2)
r = sqrt(x0.iloc[0, 0] ** 2 + x0.iloc[0, 0] ** 2)

for i in range(0, n):
    # acc_x = -mu * x[i] / (r**3)
    # acc_y = -mu * y[i] / (r**3)
    acc = -mu / (r**3) * np.array([x0.iloc[i, 0], x0.iloc[i, 1]])

    # Distance changes
    # x.append(u[i]*dt + x[i])
    # y.append(v[i]*dt + y[i])
    x0.iloc[i + 1, 0] = x0.iloc[i, 2] * dt + x0.iloc[i, 0]
    x0.iloc[i + 1, 1] = x0.iloc[i, 3] * dt + x0.iloc[i, 1]

    # Velocity changes
    # u.append(u[i] + acc_x*dt)
    # v.append(v[i] + acc_y*dt)
    x0.iloc[i + 1, 2] = acc[0] * dt + x0.iloc[i, 2]
    x0.iloc[i + 1, 3] = acc[1] * dt + x0.iloc[i, 3]

# print("x = " , x , "y = " , y)

# print(x0)
plt.plot(x0.x, x0.y)
plt.show()
