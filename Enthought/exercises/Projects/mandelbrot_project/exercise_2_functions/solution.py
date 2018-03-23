"""
Mandelbrot set functions
------------------------

Using the code in exercise 1, create two functions:

1) The first takes bounds over x and y, and the size of the grid,
   and returns the escape times at those coordinates.
   Set the default grid size to 40 .

   For example, a call to this function might look like this:
      escape_times = mandelbrot_grid((-2, 1), (-1.5, 1.5), 40)

2) The second takes a grid of escape times and returns a string
   with the ASCII art representation.

   For example, a call to this function might look like this:
      mandel_ascii = times_to_ascii(escape_times)

3) Use the two functions to print a 50x50 Mandelbrot set using these
   grids:

   x_bounds = (-2, 1)
   y_bounds = (-1.5, 1.5)

   and
   
   x_bounds = (-0.5, 0.3)
   y_bounds = (0.55, 1.35)

"""


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

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x,  2*z_x*z_y + y

        # If we are diverging, return the number of iterations.
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1

    return i


def mandelbrot_grid(x_bounds, y_bounds, size=40):
    """ Return escape times at a grid of coordinates.

    Escape times are computed on a grid of size given by the `size` argument.
    x coordinates start at x_bounds[0] and end at x_bounds[1].
    y coordinates start at y_bounds[0] and end at y_bounds[1].

    """
    
    escape_times = []

    x0, x1 = x_bounds
    y0, y1 = y_bounds

    width = x1 - x0
    height = y1 - y0

    for i in range(size+1):
        row = []
        for j in range(size+1):
            x = j / float(size) * width + x0
            y = i / float(size) * height + y0
            t = mandelbrot_escape(x, y, 100)
            row.append(t)

        escape_times.append(row)

    return escape_times


def times_to_ascii(escape_times):
    """ Convert a grid of escape times to an ASCII string.
    """
    
    translation = [' ', '.', ':', 'o', 'O', '0', 'H', 'X', '#']

    mandel_ascii = ''
    for row in escape_times:
        for t in row:
            idx = min(t+1, len(translation)-1)
            mandel_ascii += translation[idx] * 3
        mandel_ascii += '\n'

    return mandel_ascii

escape_times = mandelbrot_grid((-2, 1), (-1.5, 1.5), 50)
mandel_ascii = times_to_ascii(escape_times)
print mandel_ascii

escape_times = mandelbrot_grid((-0.5, 0.3), (0.55, 1.35), 50)
mandel_ascii = times_to_ascii(escape_times)
print mandel_ascii
