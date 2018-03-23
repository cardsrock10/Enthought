""" Functions to display a Mandelbrot set using ASCII characters. """

def times_to_ascii(escape_times):
    """ Convert a grid of escape times to an ASCII string.
    """
    
    translation = [' ', '.', ':', 'o', 'O', '0', 'H', 'X', '#']

    mandel_ascii = ''
    for row in escape_times:
        for t in row:
            idx = min(t+1, len(translation)-1)
            mandel_ascii += translation[idx] * 3
        mandel_ascii += '\n'

    return mandel_ascii
