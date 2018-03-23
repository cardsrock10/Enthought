from enable.api import BaseTool
from traits.api import Float, Instance
from mandelbrot.model.mandelbrot_parameters import MandelbrotParameters


class MandelzoomTool(BaseTool):
    """ Zoom in and out the Mandelbrot set using the mouse wheel. """

    params = Instance(MandelbrotParameters)

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

        pass

    def zoom_out(self, x, y):
        """ Zoom out and center at the coordinates (x, y). """

        pass
