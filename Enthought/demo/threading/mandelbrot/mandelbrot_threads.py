"""Computing the Mandelbrot fractal with threads.

This is a threaded version of the Mandelbrot example (see Cython exercises).
The goal is to demonstrate that several threads can run concurrently by
releasing the GIL from within Cython. If you run this, it might be a good idea
to tweak NUM_POINTS so that the computation takes a noticeable amount of time,
and to have an (h)top window open so that you can see several threads being
scheduled concurrently.

"""
from threading import Thread
import time
import numpy as np

from mandel import generate_mandelbrot

NUM_THREADS = [1, 2, 4, 8]
NUM_POINTS = 5000


def run_threaded_example(num_threads, num_points=NUM_POINTS):
    """Compute Mandelbrot escape times using multiple threads.
    """

    x = np.r_[-2:1:num_points*1j]
    y = np.r_[-1.5:1.5:num_points*1j]
    d_trans = np.empty((num_points, num_points), dtype=np.int64)

    endpoints = np.asarray(
        np.linspace(0, num_points, num_threads + 1), dtype=np.int
    )
    threads = []
    for k in range(num_threads):
        start, stop = endpoints[k:k+2]
        t = Thread(
            target=generate_mandelbrot,
            args=(x[start:stop], y, d_trans[start:stop, :], 100)
        )
        threads.append(t)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return d_trans.T


if __name__ == '__main__':
    print("Execution time:")
    for num_threads in NUM_THREADS:
        start = time.time()
        d = run_threaded_example(num_threads)
        stop = time.time()
        print("{0} thread{1}: {2}s.".format(
            num_threads, 's' if num_threads > 1 else '', stop - start)
        )

    from matplotlib.pyplot import imshow, show, cm, savefig
    imshow(d, extent=[-2,1,-1.5,1.5], cmap=cm.gist_stern)
    show()
