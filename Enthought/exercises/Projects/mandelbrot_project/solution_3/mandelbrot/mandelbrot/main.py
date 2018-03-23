from mandelbrot.model.core import mandelbrot_grid
from mandelbrot.ui.ascii import times_to_ascii


def main():
    x_bounds = -2, 1
    y_bounds = -1.5, 1.5
    n_points = 50
    
    escape_times = mandelbrot_grid(x_bounds, y_bounds, n_points)
    mandel_ascii = times_to_ascii(escape_times)

    print mandel_ascii


if __name__ == '__main__':
    print '--------- WELCOME TO THE MANDELBROT ASCII ART APPLICATION! ---------\n'
    main()
