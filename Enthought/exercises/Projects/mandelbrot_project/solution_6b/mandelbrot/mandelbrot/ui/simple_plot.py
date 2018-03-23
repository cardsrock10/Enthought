""" Functions to display a Mandelbrot set using 'matplotlib'. """

import matplotlib.pyplot as plt

def plot_escape_times(escape_times, x_bounds, y_bounds):
    plt.imshow(escape_times, extent=(x_bounds[0], x_bounds[1], y_bounds[0], y_bounds[1]))
    plt.show()
