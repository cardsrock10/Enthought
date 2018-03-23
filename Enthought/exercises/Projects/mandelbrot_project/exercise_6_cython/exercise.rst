Optimization using Cython
-------------------------

Create a copy of 'core.py' called 'core_cython.pyx', a Cython file.

The goal of the exercise is to optimize the 'mandelbrot_escape' function
as much as possible using Cython!

1. Measure the time needed by the Python and numpy code to produce a
   300 x 300 image.

2. Create a setup.py file to build the Cython extension (you can copy
   the one provided in this directory if you are unsure about how do this).

   Build the cython extension with the command

   $ python setup.py build_ext --inplace

3. Modify the main.py script so that it computes and displays the
   Mandelbrot set image using the Cython module.

4. Measure the speed of the Cython module before writing any
   Cython-specific code.

5. Add variable typing for all the scalar variables in the core_cython.pyx
   file. Make 'mandelbrot_escape' a C-only function. Re-compile, and see
   how much of a speed-up you get.

6. Add variable typing for all the numpy arrays. Re-compile, and see how much
   of a speed-up you get.

7. If you feel adventurous, find out about the parallelization features of
   Cython and try to use it in your code! Re-compile, and see how much
   of a speed-up you get.
   http://docs.cython.org/src/userguide/parallelism.html
