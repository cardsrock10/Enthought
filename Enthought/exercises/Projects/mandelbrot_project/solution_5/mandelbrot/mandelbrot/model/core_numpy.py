""" Core math functions to compute escape times for the Mandelbrot set. """

import numpy

def mandelbrot_escape(x, y, n=100):
    """Mandelbrot set escape time algorithm for a given c = x + i*y coordinate.

    Return the number of iterations necessary to escape abouve a fixed threshold
    (4.0) by repeatedly applying the formula:

    z_0 = 0
    z_n = z_{n-1} ^ 2 + c

    If the formula did not escape after `n` iterations, return -1 .

    Parameters
    ----------
    x, y -- float
        Real and imaginary part of the complex number z.

    n -- integer
        Maximum number of iterations.
    """

    z_x = 0
    z_y = 0

    times = numpy.empty(x.shape, dtype=int)
    times.fill(-1)

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x,  2*z_x*z_y + y

        # If we are diverging, return the number of iterations.
        diverged = z_x**2 + z_y**2 >= 4.0
        times[diverged & (times==-1)] = i

    return times

def mandelbrot_grid(x_bounds, y_bounds, size=40):
    """ Return escape times at a grid of coordinates.

    Escape times are computed on a grid of size given by the `size` argument.
    x coordinates start at x_bounds[0] and end at x_bounds[1].
    y coordinates start at y_bounds[0] and end at y_bounds[1].

    """
    
    escape_times = []

    x = numpy.linspace(x_bounds[0], x_bounds[1], size)
    y = numpy.linspace(y_bounds[0], y_bounds[1], size)
    x_grid, y_grid = numpy.meshgrid(x,y)

    return mandelbrot_escape(x_grid, y_grid, 100)
