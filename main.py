# Importing functions
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Note:
#     - The units of this simulator has been updated to be working in km and km/s
#     - So be careful when it comes to doing calculations and ensuring the units are consistent


# Earth radius, radius of the earth to be added onto
Earth_Radius = 6371 # km
Orbit_Radius = 20   # km
# Total satellite radius
Radius = Earth_Radius + Orbit_Radius
print(Radius)

# Standard gravitational parameter
mu = 398600.4418

# time settings
t0 = 0.0
tf = 8000.0
dt = 1
n = int(tf // dt)
t = np.round(np.arange(t0, tf, dt), 2)

# Function for finding the next time instance
def dxdt(x0):
    r = sqrt(x0[0] ** 2 + x0[1] ** 2)
    acc = -mu / (r**3) * np.array([x0[0], x0[1]])
    dxdt = np.array([x0[2], x0[3], acc[0], acc[1]])
    return dxdt


# Function to find next time step, in RK4 style
def solver(x0):   
    # k1 = f(y, v, h)
    k1 = dxdt(x0)

    # k2 = f(y + k11 * dt / 2, v + k12 * dt / 2, h + k13 * dt / 2)
    k2 = dxdt(x0 + k1 * dt/2)

    # k3 = f(y + k21 * dt / 2, v + k22 * dt / 2, h + k23 * dt / 2)
    k3 = dxdt(x0 + k2 * dt/2)

    # k4 = f(y + k31 * dt, v + k32 * dt, h + k33)
    k4 = dxdt(x0 + k3 * dt)

    print(k1, "\n", k2, "\n", k3, "\n", k4)

    # y(n + 1) = y(n) + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    x0 = dt/6.0 * (k1 + 2*k2 + 2*k3 + k4) + x0

    return x0


# State space, 2D satellite, using an array
# x0 = [x, y, u, v]
v0 = np.sqrt(mu / Radius)
x0 = np.array([Radius, 0.0, 0.0, v0])
print(x0)


# File header writing
with open("history.txt", "w") as f:
    f.write("t, x, y, u, v\n")          # optional separator/header line
# File array writing
with open("history.txt", "a") as f:
    for i in range(n):
        t_write = str(t[i])
        print(t_write)
        f.write(t_write)
        f.write(", ")
        np.savetxt(f, x0.reshape(1, -1), fmt="%g", delimiter=",")
        x0 = solver(x0)




# Plotting
df = pd.read_csv("history.txt")
df.columns = df.columns.str.strip()
print(df)

time = df['t'].to_numpy()

x = df['x'].to_numpy()
y = df['y'].to_numpy()
u = df['u'].to_numpy()
v = df['v'].to_numpy()


fig, ax = plt.subplots(figsize=(7, 7), dpi=500)
plt.plot(x, y)
plt.show()
