Optimization using Numba
------------------------

Create a copy of 'core.py' called 'core_numba.py'.

The goal of the exercise is to optimize the 'mandelbrot_escape' function
as much as possible using Numba!

1. Measure the time needed by the Python and numpy code to produce a
   300 x 300 image.

2. Modify the main.py script so that it computes and displays the
   Mandelbrot set image using the Numba module.

4. Use the @autojit decorator and measure its performance.

5. Use the @jit decorator and measure its performance.
