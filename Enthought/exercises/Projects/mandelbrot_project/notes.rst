Ex 1 ASCII Art (45 min)
=======================

Requires: loops, string operations

Given a "black-box" function that computes the escape time at a given
coordinate, iterate over a grid of points and print an ASCII representation
of a Mandelbrot set.

How then convert escape times to characters is open-ended, I used a simple
look-up table.


Ex 2 Functions (30 min)
=======================

Requires: functions

Take the code from ex.1 and encapsulate it in two functions.


Ex 3 Mandelbrot project (20 min)
================================

Requires: modules, packages

Re-organize the code to look like a conventional Python project.


Ex 4 (placeholder)
==================

Placeholder for an additional exercise.


Ex 5 Numpy (45 min)
===================

Requires: numpy, matplotlib


Ex 6 Cython (45 min)
====================

Requires: slides about Cython, *not* including the Mandelbrot example that
          solves this exercise


The solution includes the use of OpenMP, but the students are not expected
go that far.


Benchmarks on 2.3Ghz Mac Book Pro, May 8, 2013:

x_bounds = -2, 1
y_bounds = -1.5, 1.5
n_points = 300

pure Python                         1.76   sec
numpy vectorized                    0.18   sec x10
cython with Python code             1.21   sec x1.5 (core_cython_0.pyx)
+ types                             0.024  sec x73  (core_cython_1_types.pyx)
+ numpy array                       0.0098 sec x180 (core_cython_2_numpy.pyx)
+ prange (export OMP_NUM_THREADS=8) 0.0025 sec x740 (core_cython_3_prange.pyx)


x_bounds = -2, 1
y_bounds = -1.5, 1.5
n_points = 1000

pure Python                         19.87 sec
numpy vectorized                    5.98  sec x3
cython (export OMP_NUM_THREADS=8)   0.025 sec x8745 (core_cython_3_prange.pyx)


Ex 6bis Numba (20 min)
======================

Requires: extra slides about Numba


Benchmarks on 2.3Ghz Mac Book Pro, May 8, 2013, run on an Ubuntu VM:


x_bounds = -2, 1
y_bounds = -1.5, 1.5
n_points = 300

pure Python                         1.38  sec
numpy vectorized                    0.20  sec x7
cython (export OMP_NUM_THREADS=8)   0.005 sec x276 (core_cython_3_prange.pyx)
numba                               0.010 sec x138


x_bounds = -2, 1
y_bounds = -1.5, 1.5
n_points = 1000

pure Python                         15.13 sec
numpy vectorized                    4.04  sec x4
cython (export OMP_NUM_THREADS=8)   0.04  sec x378 (core_cython_3_prange.pyx)
numba                               0.11  sec x138


Ex 7 Chaco and Traits UI (1 h)
==============================

Requires: Traits, Traits UI, Chaco

Still work in progres...
