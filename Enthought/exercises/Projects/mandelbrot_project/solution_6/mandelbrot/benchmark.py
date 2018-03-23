import time
from mandelbrot.model.core import mandelbrot_grid as mg_python
from mandelbrot.model.core_numpy import mandelbrot_grid as mg_numpy
from mandelbrot.model.core_cython import mandelbrot_grid as mg_cython

x_bounds = -2, 1
y_bounds = -1.5, 1.5
n_points = 300

start_time = time.time()
escape_times = mg_python(x_bounds, y_bounds, n_points)
print 'Pure Python code (sec):', time.time() - start_time

start_time = time.time()
escape_times = mg_numpy(x_bounds, y_bounds, n_points)
print 'numpy code (sec):', time.time() - start_time

start_time = time.time()
escape_times = mg_cython(x_bounds, y_bounds, n_points)
print 'Cython code (sec):', time.time() - start_time
