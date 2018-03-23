Chaco + Traits UI viewer for the Mandelbrot set
-----------------------------------------------

Build a Mandelbrot set viewer for the Mandelbrot set.

1. Write a Traits UI dialog that requests the bounds of the Mandelbrot set,
   and the number of points. When the user presses "Ok", it plots the
   Mandelbrot set using the given parameters and exits.

2. Create a Traits UI application that displays the Mandelbrot set using
   Chaco.

3. Write a tool that allows zooming in the plot using the mouse wheel.
   Use the file 'mandelzoom_tool.py' in the exercise directory as a starting
   point.

4. Add a button to reset the view to the initial state.

5. Add a dropdown menu to select the colormap for the plot.
   The colormaps are in 'chaco.default_colormaps'
   In default_colormaps, there is a dictionary 'color_map_name_dict'
   mapping colormap names to colormaps that can be used to define
   a Enum trait.
