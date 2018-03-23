from enable.api import BaseTool
from traits.api import Float, Instance
from mandelbrot.model.mandelbrot_parameters import MandelbrotParameters


class MandelzoomTool(BaseTool):
    """ Zoom in and out the Mandelbrot set using the mouse wheel. """

    params = Instance(MandelbrotParameters)

    zoom_in_factor = Float(1.2)

    def normal_mouse_wheel(self, event):
        """ Called when the mouse wheel state changes. """

        # event.mouse_wheel is positive when the wheel moves up and negative
        # when is moves down, and zero otherwise

        x, y = self.component.map_data((event.x, event.y))
        if event.mouse_wheel != 0:
            if event.mouse_wheel > 0:
                self.zoom_in(x, y)
            else:
                self.zoom_out(x, y)

            event.handled = True

    def zoom_in(self, x, y):
        """ Zoom in and center at the coordinates (x, y). """

        params = self.params
        width = (params.xmax - params.xmin) / self.zoom_in_factor
        height = (params.ymax - params.ymin) / self.zoom_in_factor

        params.xmin = x - width/2.0
        params.xmax = x + width/2.0
        params.ymin = y - height/2.0
        params.ymax = y + height/2.0

    def zoom_out(self, x, y):
        """ Zoom out and center at the coordinates (x, y). """

        params = self.params
        width = (params.xmax - params.xmin) * self.zoom_in_factor
        height = (params.ymax - params.ymin) * self.zoom_in_factor

        params.xmin = x - width/2.0
        params.xmax = x + width/2.0
        params.ymin = y - height/2.0
        params.ymax = y + height/2.0
