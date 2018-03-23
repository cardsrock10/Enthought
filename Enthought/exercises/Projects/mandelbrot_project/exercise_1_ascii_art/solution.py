"""
Mandelbrot set ASCII art
------------------------

At the start of this file we define a function to compute the escape times at
a given coordinate (x, y) in the Mandelbrot set. For the moment, you can
use it as a black box that can be called as

    >>> time = mandelbrot_escape(-1, 0.5)

You can read the docstring to have more details about the arguments of the function:

    >>> help(mandelbrot_escape)


1. Compute the escape times at these (x, y) coordinates:
   coords = [(-1, 0.5), (-1, 0), (0.5, -0.3), (0.5, 0.3)]

   The expected result is [4, -1, 5, 5]

2. Build a list-of-lists of the Mandelbrot set escape times on a 21x21 grid
   of coordinates between  x = -2 ... 1  and y = -1.5 ... 1.5 .

   The result is going to look similar to this:
   [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 2, 2, ...],
    ...
    [0, 0, 0, 0, 0, 1, ...]]

3. Use the escape times to create an ASCII-art representation of the
   Mandelbrot set, e.g.

...............::::::::::::::::::::::::::::::::::::::::::::::::
............:::::::::::::::::::::::::::::::::::::::::::::::::::
.........:::::::::ooooooooooooooooooooooooooo::::::::::::::::::
......::::::ooooooooooooooooooOOOOOO###HHHOOOoooooo::::::::::::
......:::oooooooooooooooOOOOOOOOO000######000OOOoooooo:::::::::
...:::oooooooooooooooOOOOOO000HHHXXX      XXX000OOOoooooo::::::
...:::ooooooooooooOOO000000XXX               ######oooooo::::::
...oooooooooOOOHHH000HHHXXX                     XXXOOOoooooo:::
...oooOOOOOO000############                     ###OOOoooooo:::
...OOOOOO000######                              ###OOOoooooo:::
...                                             XXXOOOoooooo:::
...OOOOOO000######                              ###OOOoooooo:::
...oooOOOOOO000############                     ###OOOoooooo:::
...oooooooooOOOHHH000HHHXXX                     XXXOOOoooooo:::
...:::ooooooooooooOOO000000XXX               ######oooooo::::::
...:::oooooooooooooooOOOOOO000HHHXXX      XXX000OOOoooooo::::::
......:::oooooooooooooooOOOOOOOOO000######000OOOoooooo:::::::::
......::::::ooooooooooooooooooOOOOOO###HHHOOOoooooo::::::::::::
.........:::::::::ooooooooooooooooooooooooooo::::::::::::::::::
............:::::::::::::::::::::::::::::::::::::::::::::::::::
...............::::::::::::::::::::::::::::::::::::::::::::::::

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

# 1. Compute the escape times at these (x, y) coordinates:
#    coords = [(-1, 0.5), (-1, 0), (0.5, -0.3), (0.5, 0.3)]

coords = [(-1, 0.5), (-1, 0), (0.5, -0.3), (0.5, 0.3)]
values = [mandelbrot_escape(xy[0], xy[1]) for xy in coords]


# 2. Build a list-of-lists of the Mandelbrot set escape times on a 20x20 grid
#    of coordinates between  x = -2 ... 1  and y = -1.5 ... 1.5 .

escape_times = []
SIZE = 20

for i in range(SIZE+1):
    row = []
    for j in range(SIZE+1):
        x = j / float(SIZE) * 3 - 2
        y = i / float(SIZE) * 3 - 1.5
        t = mandelbrot_escape(x, y)
        row.append(t)

    escape_times.append(row)



# 3. Use the escape times to create an ASCII-art representation of the
#    Mandelbrot set.

translation_table = [' ', '.', ':', 'o', 'O', '0', 'H', 'X', '#']

mandel_ascii = ''
for row in escape_times:
    for t in row:
        idx = min(t+1, len(translation_table)-1)

        # An alternative for logarithmic conversion:
        # idx = min((t+1).bit_length(), len(translation_table)-1)

        mandel_ascii += translation_table[idx] * 3

    mandel_ascii += '\n'

print mandel_ascii
