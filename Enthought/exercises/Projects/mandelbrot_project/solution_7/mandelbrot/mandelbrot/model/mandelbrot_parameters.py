import numpy
from traits.has_traits import HasTraits
from traits.trait_types import Int, Float
from traits.traits import Property


class MandelbrotParameters(HasTraits):
    """ Stores the parameters needed to visualize the Mandelbrot set.
    """

    # The number of points on each dimension of the grid.
    grid_size = Int(500)

    # Left limit for the x coordinates.
    xmin = Float(-2.0)

    # Right limit for the x coordinates.
    xmax = Float(1.0, auto_set=False)

    # Bottom limit for the y coordinates.
    ymin = Float(-1.5, auto_set=False)

    # Upper limit for the y coordinates.
    ymax = Float(1.5, auto_set=False)

    # Convenience property that returns a tuple with the bounds on the x axis.
    x_bounds = Property
    def _get_x_bounds(self):
        return (self.xmin, self.xmax)

    # 1D array with the x coordinates of the boundaries of the grid element.
    x_coords = Property
    def _get_x_coords(self):
        # The coordinates have 1 more element than the number of points in
        # the grid, because they represent the locations of pixel boundaries.
        return numpy.linspace(self.xmin, self.xmax, self.grid_size+1)

    # Convenience property that returns a tuple with the bounds on the y axis.
    y_bounds = Property(depends_on='ymin,ymax')
    def _get_y_bounds(self):
        return (self.ymin, self.ymax)

    # 1D array with the y coordinates of the boundaries of the grid element.
    y_coords = Property(depends_on='ymin,ymax')
    def _get_y_coords(self):
        # The coordinates have 1 more element than the number of points in
        # the grid, because they represent the locations of pixel boundaries.
        return numpy.linspace(self.ymin, self.ymax, self.grid_size+1)
