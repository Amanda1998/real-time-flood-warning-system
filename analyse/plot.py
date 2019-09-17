
"""This function will be used in Task2D"""
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
from analyse.analysis import polyfit


def plot_water_levels(station, dates, levels):
    "i guess this function will plot water levels"
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    dates_conv = date2num(dates)
    poly, d0 = polyfit(dates_conv, levels, p)
    plt.plot(dates, levels, '.')

    x1 = np.linspace(dates_conv[0], dates_conv[-1], 30)
    plt.plot(x1, poly(x1 - d0))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()


