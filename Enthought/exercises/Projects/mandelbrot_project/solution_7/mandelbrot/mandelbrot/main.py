from mandelbrot.model.mandelbrot_parameters import MandelbrotParameters
from mandelbrot.ui.mandelbrot_view import MandelbrotView


def main():
    params = MandelbrotParameters()
    view = MandelbrotView(model=params)
    view.configure_traits()


if __name__ == '__main__':
    print '--------- WELCOME TO THE MANDELBROT VIEWER! ---------\n'
    main()
