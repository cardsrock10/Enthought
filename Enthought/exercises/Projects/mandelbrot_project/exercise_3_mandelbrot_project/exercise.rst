Mandelbrot project
------------------

Create a package for the Mandelbrot project.

The final directory structure should look like this:

mandelbrot (root of project)
|
|- mandelbrot (main package)
|  |
|  |- model (contains code to do compute a Mandelbrot set)
|  |  |- __init__.py
|  |  |- core.py (put the mandelbrot_escape and the mandelbrot_grid functions here)
|  |
|  |- ui (contains code to display the Mandelbrot set)
|  |  |
|  |  |- __init__.py
|  |  |- ascii.py
|  |
|  |- __init__.py
|  |- main.py
|
|- README.txt

1) Put the function that creates an ASCII representation from Exercise 3 in
   'ascii.py', and the 'mandelbrot_escape' and 'mandelbrot_grid' functions in
   'core.py'.

2) In 'main.py', create a script that, when executed, computes the escape times
   on a grid and prints out its ASCII representation.
