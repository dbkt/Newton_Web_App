import time

from matplotlib import pyplot as plt
import numpy as np


def plot_settings_common(f, x_sol, x_fin, fig, ax):
    # Define x_axis depending on whether solution is within the range of x_values created in all iterations
    ax.grid()
    ax.set_facecolor('#EBEBEB')
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)

    if x_fin < min(min(x_sol), 0.01):
        x_axis = np.linspace(x_fin, max(x_sol), 10000)
    elif x_fin > max(x_sol):
        x_axis = np.linspace(min(x_sol), x_fin, 10000)
    else:
        x_axis = np.linspace(min(min(x_sol), 0.01), max(x_sol), 10000)

    ax.scatter(x_axis, f(x_axis), marker=".", color="silver")
    ax.scatter([x_fin], [f(x_fin)], color="red")

    ax.axhline(0, color="black", linewidth=0.55, linestyle="-")
    ax.axvline(0, color="black", linewidth=0.55, linestyle="-")

    return fig


def plot_settings_root(f, x_before, x_now, ax):
    x = np.linspace(x_before, x_now, 10000)
    y = np.linspace(f(x_before), 0, 10000)
    return ax.plot(x, y, zorder=1, linestyle='dashed')


def plot_settings_axis(f, x_now, ax):
    x = np.linspace(x_now, x_now + 0.000000001, 10000)
    y = np.linspace(0, f(x_now), 10000)
    return ax.plot(x, y, zorder=1, linestyle='dashed')
    return x, y
