Improving the Mandelbrot code using numpy
-----------------------------------------

In this exercise, we'll create a more efficient version of 'mandelbrot_escape'
and 'mandelbrot_grid' using numpy operations.

1. Copy the module 'model/core.py' and create a new module
   'model/core_numpy.py'.

2. Modify the 'mandelbrot_grid' function using numpy arrays so that the
   double loop disappears. You'll need to modify the 'mandelbrot_escape'
   function slightly so that it accepts 2D arrays of coordinates as input.

3. Add a module ui/simple_plot.py with a function that plots escape times
   using matplotlib.

4. Update main.py to compute escape times using core_numpy and plot them using
   matplotlib.

5. Compare execution times.
