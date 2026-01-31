# Instead of writing using a dataframe, perhaps write using np arrays

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
t0 = 0.0
tf = 8000.0
dt = 1
t = np.arange(t0, tf, dt)
n = int(tf // dt)

# Function for finding the next time instance
def x1(x0,  mu):
    r = sqrt(x0[0] ** 2 + x0[1] ** 2)
    acc = -mu / (r**3) * np.array([x0[0], x0[1]])
    x1 = np.array([x0[2], x0[3], acc[0], acc[1]]) * dt + x0
    return x1

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
        x0 = x1(x0, mu)



# Plotting
df = pd.read_csv("history.txt")
df.columns = df.columns.str.strip()
print(df)

time = df['t'].to_numpy()

x = df['x'].to_numpy()
y = df['y'].to_numpy()
u = df['u'].to_numpy()
v = df['v'].to_numpy()


fig, ax = plt.subplots(figsize=(2, 2), dpi=500)
plt.plot(x, y)
plt.show()
