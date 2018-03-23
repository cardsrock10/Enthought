import numpy

from chaco.api import ArrayPlotData, Plot
from enable.api import ComponentEditor
from traits.api import Float, HasTraits, Instance, Int, Property
from traitsui.api import Item, ModelView, View, VGroup

from mandelbrot.model.core_numpy import mandelbrot_grid


class MandelbrotParameters(HasTraits):
    """ Stores the parameters needed to visualize the Mandelbrot set.
    """

    # The number of points on each dimension of the grid.
    grid_size = Int(300)

    # Left limit for the x coordinates.
    xmin = Float(-2.0)

    # Right limit for the x coordinates.
    xmax = Float(1.0)

    # Bottom limit for the y coordinates.
    ymin = Float(-1.5)

    # Upper limit for the y coordinates.
    ymax = Float(1.5)

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
    y_bounds = Property
    def _get_y_bounds(self):
        return (self.ymin, self.ymax)

    # 1D array with the y coordinates of the boundaries of the grid element.
    y_coords = Property
    def _get_y_coords(self):
        # The coordinates have 1 more element than the number of points in
        # the grid, because they represent the locations of pixel boundaries.
        return numpy.linspace(self.ymin, self.ymax, self.grid_size+1)


class MandelbrotView(ModelView):
    """ Traits UI and Chaco view of a Mandelbrot set. """

    # The model part of this UI.
    model = Instance(MandelbrotParameters)

    # The Chaco data source for the Mandelbrot set.
    plot_data = Instance(ArrayPlotData)

    def _plot_data_default(self):
        mandelbrot = mandelbrot_grid(
            self.model.x_bounds,
            self.model.y_bounds,
            self.model.grid_size
        )

        plot_data = ArrayPlotData(mandelbrot=mandelbrot)

        return plot_data

    # The Chaco plot.
    mandelbrot_plot = Instance(Plot)

    def _mandelbrot_plot_default(self):

        plot = Plot(self.plot_data)

        renderer = plot.img_plot(
            'mandelbrot',
            xbounds=self.model.x_coords,
            ybounds=self.model.y_coords)[0]

        plot.aspect_ratio = 1.0

        return plot

    # Traits UI definition of the UI.
    traits_view = View(
        VGroup(
            Item('mandelbrot_plot', editor=ComponentEditor(), show_label=False),
        ),
        resizable=True,
    )
