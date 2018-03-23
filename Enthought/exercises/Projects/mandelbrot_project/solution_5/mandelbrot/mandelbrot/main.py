from mandelbrot.model.core_numpy import mandelbrot_grid
from mandelbrot.ui.simple_plot import plot_escape_times


def main():
    x_bounds = -2, 1
    y_bounds = -1.5, 1.5
    n_points = 300
    
    escape_times = mandelbrot_grid(x_bounds, y_bounds, n_points)
    plot_escape_times(escape_times, x_bounds, y_bounds)


if __name__ == '__main__':
    print '--------- WELCOME TO THE MANDELBROT PLOTTING APPLICATION! ---------\n'
    main()
