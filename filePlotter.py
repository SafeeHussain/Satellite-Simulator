# Old python file I used for plotting results with data frame
# (Frame of reference doc)
# File plotter to be used in Python

import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

# Tabulates the data
def Tabulator(fname):
    df = pd.read_csv(fname, delimiter=",", index_col=None)
    print(df)
    del df

# One figure of all combined subfigures
def SingleFigurePlotter(fname):
    df = pd.read_csv(fname,delimiter=',')
    dis = df['dist (m) '].to_numpy()
    Pprop = df["P|Prop(W) "].to_numpy()
    Pturb = df["P|Turb(N) "].to_numpy()
    Tprop = df["T|Prop(N) "].to_numpy()
    Tturb = df["T|Turb (N) "].to_numpy()

    # Figure settings
    plt.figure(figsize=(17.5,10))                   # Size of figure window
    plt.rcParams.update({'font.size': 14})          # Font size change
    plt.subplots_adjust(hspace = 0.5)               # Vertical Spacing
    disq = np.linspace(dis.min(), dis.max(), 100)   # Number of querry points

    # Subplot settings/
    plt.subplot(3,2,1)
    Pturbq = UnivariateSpline(dis, Pturb, s = 1)(disq)
    plt.title("Power extracted from turbine with varying distance")
    plt.plot(dis, Pturb, "rx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Pturbq, "r--")
    plt.ylabel("Turbine Power (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    plt.subplot(3,2,2)
    Ppropq = UnivariateSpline(dis, Pprop, s = 1)(disq)
    plt.title("Power exerted from the propeller with varying distance")
    plt.plot(dis, Pprop, "bx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Ppropq, "b--")
    plt.ylabel("Propeller Power (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    # No spline fit here, too random to fit a curve
    plt.subplot(3,2,3)
    m, c = np.polyfit(dis, Tturb, 1) # y = mx + c
    Tturbq = disq * m + c
    plt.title("Thrust of the turbine with varying distance")
    plt.plot(dis, Tturb, "rx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tturbq, "r--")
    plt.ylabel("Turbine Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    plt.subplot(3,2,4)
    Tpropq = UnivariateSpline(dis, Tprop, s = 1)(disq)
    plt.title("Thrust of the propeller with varying distance")
    plt.plot(dis, Tprop, "bx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tpropq, "b--")
    plt.ylabel("Propeller Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    plt.subplot(3,2,5)
    plt.title("Net Power loss from the turbine and the propeller")
    Ploss = Pprop - Pturb
    Plossq = UnivariateSpline(dis, Ploss, s = 1)(disq)
    plt.plot(dis, Ploss, "gx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Plossq, "g--")
    plt.ylabel("Net Power Loss (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    plt.subplot(3,2,6)
    plt.title("Resultant force between turbine and power")
    Tloss = Tprop - Tturb
    Tlossq = UnivariateSpline(dis, Tloss, s = 1)(disq)
    plt.plot(dis, Tloss, "gx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tlossq, "g--")
    plt.ylabel("Resultant Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.minorticks_on()

    plt.ylim(15, 16)

    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlots.png", bbox_inches='tight', pad_inches=0)

    plt.show()

# Multiple figures saved as seperate .pngs
def MultiFigurePlotter(fname):
    width = 16
    height = 7
    df = pd.read_csv(fname,delimiter=',')
    dis = df['dist (m) '].to_numpy()
    Pprop = df["P|Prop(W) "].to_numpy()
    Pturb = df["P|Turb(N) "].to_numpy()
    Tprop = df["T|Prop(N) "].to_numpy()
    Tturb = df["T|Turb (N) "].to_numpy()

    # General Settings
    plt.rcParams.update({'font.size': 28})          # Font size change
    # plt.subplots_adjust(hspace = 0.5)               # Vertical Spacing
    disq = np.linspace(dis.min(), dis.max(), 100)   # Number of querry points

    # Figure Settings
    plt.figure(1, figsize=(width,height))
    Pturbq = UnivariateSpline(dis, Pturb, s = 1)(disq)
    # plt.title("Power extracted from turbine with varying distance")
    plt.plot(dis, Pturb, "rx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Pturbq, "r--")
    plt.ylabel("Turbine Power (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsA.png", bbox_inches='tight', pad_inches=0)

    plt.figure(2, figsize=(width,height))
    Ppropq = UnivariateSpline(dis, Pprop, s = 1)(disq)
    # plt.title("Power exerted from the propeller with varying distance")
    plt.plot(dis, Pprop, "bx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Ppropq, "b--")
    plt.ylabel("Propeller Power (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsB.png", bbox_inches='tight', pad_inches=0)

    # No spline fit here, too random to fit a curve, do a straight line of best fit
    plt.figure(3, figsize=(width,height))
    m, c = np.polyfit(dis, Tturb, 1) # y = mx + c
    Tturbq = disq * m + c
    # plt.title("Thrust of the turbine with varying distance")
    plt.plot(dis, Tturb, "rx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tturbq, "r--")
    plt.ylabel("Turbine Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsC.png", bbox_inches='tight', pad_inches=0)

    plt.figure(4, figsize=(width,height))
    Tpropq = UnivariateSpline(dis, Tprop, s = 1)(disq)
    # plt.title("Thrust of the propeller with varying distance")
    plt.plot(dis, Tprop, "bx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tpropq, "b--")
    plt.ylabel("Propeller Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsD.png", bbox_inches='tight', pad_inches=0)

    plt.figure(5, figsize=(width,height))
    # plt.title("Net Power loss from the turbine and the propeller")
    Ploss = Pprop - Pturb
    Plossq = UnivariateSpline(dis, Ploss, s = 1)(disq)
    plt.plot(dis, Ploss, "gx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Plossq, "g--")
    plt.ylabel("Net Power Loss (W)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsE.png", bbox_inches='tight', pad_inches=0)

    plt.figure(6, figsize=(width,height))
    # plt.title("Resultant force between turbine and power")
    Tloss = Tprop - Tturb
    Tlossq = UnivariateSpline(dis, Tloss, s = 1)(disq)
    plt.plot(dis, Tloss, "gx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq, Tlossq, "g--")
    plt.ylabel("Resultant Thrust (N)")
    plt.xlabel("Distance (m)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.minorticks_on()
    plt.ylim(15, 16)
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsF.png", bbox_inches='tight', pad_inches=0)

    try:
        plt.show()
    except KeyboardInterrupt:
        plt.close('all')

# One figure of all combines subfigures
def SinglePropellerOnlyPlotter(fname1, fname2):

    # First csv file is propeller only
    df = pd.read_csv(fname1,delimiter=',')
    dis0 = df['dist (m) '].to_numpy()
    Tprop0 = df["P|Prop(W) "].to_numpy()     # Thrust of propeller
    Pprop0 = df["T|Turb (N) "].to_numpy()    # Power of propeller

    # Second csv file is propeller turbine config
    df = pd.read_csv(fname2,delimiter=',')
    dis = df['dist (m) '].to_numpy()
    Pprop = df["P|Prop(W) "].to_numpy()
    Pturb = df["P|Turb(N) "].to_numpy()
    Tprop = df["T|Prop(N) "].to_numpy()
    Tturb = df["T|Turb (N) "].to_numpy()

    # Figure settings
    plt.figure(figsize=(17.5,10))                           # Size of figure window
    plt.rcParams.update({'font.size': 14})                  # Font size change
    plt.subplots_adjust(hspace = 0.5)                       # Vertical Spacing
    disq0 = np.linspace(dis0.min(), dis0.max(), 100)        # Number of querry points, propeller only
    disq = np.linspace(dis.min(), dis.max(), 100)           # Number of querry points, propeller-turbine

    # Subplot settings
    # Propeller Power
    plt.subplot(2,2,1)
    Ppropq0 = UnivariateSpline(dis0, Pprop0, s = 1)(disq0)
    plt.title("Power exerted from the propeller with varying diameter")
    plt.plot(dis0, Pprop0, "mx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq0, Ppropq0, "m--")
    plt.ylabel("Propeller Power (W)")
    plt.xlabel("Disk's Diameter (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    # Propeller Thrust
    plt.subplot(2,2,2)
    Tpropq0 = UnivariateSpline(dis0, Tprop0, s = 1)(disq0)
    plt.title("Thrust of the propeller with varying diameter")
    plt.plot(dis0, Tprop0, "mx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq0, Tpropq0, "m--")
    plt.ylabel("Propeller Thrust (N)")
    plt.xlabel("Disk's Diameter (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()

    # Propeller only vs Propeller-turbine power comparison
    plt.subplot(2,2,3)
    plt.title("Net Power loss from the turbine and the propeller")
    Ploss = Pprop - Pturb
    Tloss = Tprop - Tturb
    # Plossq = UnivariateSpline(Tloss, Ploss, s = 1)(disq)
    plt.plot(Tprop0, Pprop0, "mx--", markersize = 12, markeredgewidth = 1.25, label = "Propeller Only")
    plt.plot(Tloss, Ploss, "gx--", markersize = 12, markeredgewidth = 1.25, label = "Propeller-turbine config")
    # plt.plot(Tprop0, Ppropq0, "m--")
    # plt.plot(Tloss, Plossq, "g--")
    plt.ylabel("Resultant Power (W)")
    plt.xlabel("Resultant Force (N)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.legend()

    plt.xlim(min(Tloss), max(Tloss))
    plt.ylim(250, 375)

    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsPropOnly.png", bbox_inches='tight', pad_inches=0)

    plt.show()

# Multiple figures saved as seperate .pngs
def MultiPropellerOnlyPlotter(fname1, fname2):

    # First csv file is propeller only

    df = pd.read_csv(fname1,delimiter=',')
    dis0 = df['dist (m) '].to_numpy()
    Tprop0 = df["P|Prop(W) "].to_numpy()     # Thrust of propeller
    Pprop0 = df["T|Turb (N) "].to_numpy()    # Power of propeller

    # Second csv file is propeller turbine config
    df = pd.read_csv(fname2,delimiter=',')
    dis = df['dist (m) '].to_numpy()
    Pprop = df["P|Prop(W) "].to_numpy()
    Pturb = df["P|Turb(N) "].to_numpy()
    Tprop = df["T|Prop(N) "].to_numpy()
    Tturb = df["T|Turb (N) "].to_numpy()

    # Figure settings
    width = 16
    height = 7
    plt.rcParams.update({'font.size': 28})                  # Font size change
    disq0 = np.linspace(dis0.min(), dis0.max(), 100)        # Number of querry points, propeller only
    disq = np.linspace(dis.min(), dis.max(), 100)           # Number of querry points, propeller-turbine

    # Subplot settings
    # Propeller Power
    plt.figure(1, figsize=(width, height))
    Ppropq0 = UnivariateSpline(dis0, Pprop0, s = 1)(disq0)
    plt.plot(dis0, Pprop0, "mx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq0, Ppropq0, "m--")
    plt.ylabel("Propeller Power (W)")
    plt.xlabel("Disk's Diameter (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsPropOnlyA.png", bbox_inches='tight', pad_inches=0)

    # Propeller Thrust
    plt.figure(2, figsize=(width, height))
    Tpropq0 = UnivariateSpline(dis0, Tprop0, s = 1)(disq0)
    plt.plot(dis0, Tprop0, "mx", markersize = 12, markeredgewidth = 1.25)
    plt.plot(disq0, Tpropq0, "m--")
    plt.ylabel("Propeller Thrust (N)")
    plt.xlabel("Disk's Diameter (m)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsPropOnlyB.png", bbox_inches='tight', pad_inches=0)

    # Propeller only vs Propeller-turbine power comparison
    plt.figure(3, figsize=(width, height))
    Ploss = Pprop - Pturb
    Tloss = Tprop - Tturb


    plt.plot(Tprop0, Pprop0, "mx--", markersize = 12, markeredgewidth = 1.25, label = "Propeller Only")
    plt.plot(Tloss, Ploss, "gx--", markersize = 12, markeredgewidth = 1.25, label = "Propeller-turbine config")

    plt.ylabel("Resultant Power (W)")
    plt.xlabel("Resultant Force (N)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.legend()
    plt.xlim(min(Tloss), max(Tloss))
    plt.ylim(250, 375)

    plt.savefig("/home/safee/Documents/UROP/UROP Pictures/Plots/PowerThrustPlotsPropOnlyC.png", bbox_inches='tight', pad_inches=0)


    plt.show()
