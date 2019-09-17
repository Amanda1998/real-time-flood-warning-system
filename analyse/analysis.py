
import numpy as np


def polyfit(dates, levels, p):
    p_coeff = np.polyfit(dates - dates[0], levels, p)
    return np.poly1d(p_coeff), dates[0]
