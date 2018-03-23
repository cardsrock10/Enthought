from chaco.api import AbstractPlotRenderer, ArrayPlotData, DataRange1D, Plot
import chaco.default_colormaps as dc
from enable.api import ComponentEditor
from traits.api import Button, Enum, Instance, on_trait_change
from traitsui.api import HGroup, Item, ModelView, TextEditor, View, VGroup

from mandelbrot.model.core_cython import mandelbrot_grid
from mandelbrot.model.mandelbrot_parameters import MandelbrotParameters
from mandelbrot.ui.mandelzoom_tool import MandelzoomTool


_coords_text_editor = TextEditor(auto_set=False, enter_set=True,
                                 evaluate=float)

class MandelbrotView(ModelView):
    """ Traits UI and Chaco view of a Mandelbrot set. """

    # The model part of this UI.
    model = Instance(MandelbrotParameters)

    # The Chaco plot.
    mandelbrot_plot = Instance(Plot)
    def _mandelbrot_plot_default(self):
        return self._create_mandelbrot_plot()

    # The Chaco data source for the Mandelbrot set.
    mandelbrot_plot_data = Instance(ArrayPlotData)
    def _mandelbrot_plot_data_default(self):
        plot_data = ArrayPlotData()
        self._set_plot_data(plot_data)
        return plot_data

    # The Chaco plot renderer.
    mandelbrot_renderer = Instance(AbstractPlotRenderer)

    # A button that resets the view to the default one.
    reset_view = Button
    def _reset_view_fired(self):
        self.model.set(xmin=-2, xmax=1, ymin=-1.5, ymax=1.5)

    # The colormap of the plot.
    colormap = Enum(dc.color_map_name_dict.keys())

    @on_trait_change('colormap')
    def set_colormap(self):
        data_range = DataRange1D(low=-1.0, high=200)
        colormap = dc.color_map_name_dict[self.colormap](data_range)

        self.mandelbrot_renderer.color_mapper = colormap
        self.mandelbrot_renderer.invalidate_and_redraw()

    @on_trait_change('model:xmin,model:xmax,model:ymin,model:ymax')
    def _update_plot_data_and_bounds(self):
        """ Update the image data and the plot bounds when the bounds change.
        """
        self._set_plot_data(self.mandelbrot_plot_data)
        self.mandelbrot_plot = self._create_mandelbrot_plot()

    def _create_mandelbrot_plot(self):
        plot = Plot(self.mandelbrot_plot_data)

        self.mandelbrot_renderer = plot.img_plot(
            'mandelbrot',
            xbounds=self.model.x_coords,
            ybounds=self.model.y_coords,
            name='mandelbrot_plot')[0]

        plot.aspect_ratio = 1.0
        plot.tools.append(MandelzoomTool(component=plot, params=self.model))
        self.set_colormap()

        return plot

    def _set_plot_data(self, plot_data):
        mandelbrot = mandelbrot_grid(
            self.model.x_bounds,
            self.model.y_bounds,
            self.model.grid_size
        )

        plot_data.set_data('mandelbrot', mandelbrot)

    # Traits UI definition of the UI.
    traits_view = View(
        VGroup(
            Item('mandelbrot_plot', editor=ComponentEditor(), show_label=False),
            HGroup(
                Item('colormap'),
                Item('reset_view', show_label=False)
            ),
        ),
        resizable=True,
    )
