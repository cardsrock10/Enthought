""" Core math functions to compute escape times for the Mandelbrot set. """

from numpy import empty
cimport numpy as np

cdef int mandelbrot_escape(double x, double y, int n):
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

    cdef double z_x = 0
    cdef double z_y = 0

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x,  2*z_x*z_y + y

        # If we are diverging, return the number of iterations.
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1

    return i

def _mandelbrot_grid(double x0, double x1, double y0, double y1, int size):

    cdef np.ndarray[int, ndim=2] escape_times = \
        empty((size+1, size+1), dtype=int)

    cdef double x, y
    cdef int i, j
    cdef double width = x1 - x0
    cdef double height = y1 - y0
    cdef double d_size = size

    for i in range(size+1):
        for j in range(size+1):
            x = j / d_size * width + x0
            y = i / d_size * height + y0
            escape_times[i,j] = mandelbrot_escape(x, y, 100)

    return escape_times

def mandelbrot_grid(x_bounds, y_bounds, int size):
    """ Return escape times at a grid of coordinates.

    Escape times are computed on a grid of size given by the `size` argument.
    x coordinates start at x_bounds[0] and end at x_bounds[1].
    y coordinates start at y_bounds[0] and end at y_bounds[1].

    """

    x0, x1 = x_bounds
    y0, y1 = y_bounds

    return _mandelbrot_grid(x0, x1, y0, y1, size)
