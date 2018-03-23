"""
Parallel FFTs on a Memory-Mapped File

Must have an IPython cluster running, for example:

>>> ipcluster start -n8

Timings on a Macbook Pro: 2.3GHz Intel Core i7, 8GB Memory
Timings are the minimum of 3 runs for each.

nengines     1     2     4     8
--------  ----  ----  ----  ----
time (s)  6.96  3.59  2.27  1.86
"""

import numpy
import time
from IPython.parallel import Client, require
from os.path import abspath

def equal_size_split(arr, view):
    """Return the number of rows each engine should work with."""
    return int(numpy.ceil(float(len(arr)) / len(view)))


@require('numpy')
def subsection_fft(row_slice, filename):
    """FFT run on each engine."""
    arr = numpy.load(filename, mmap_mode='r')
    numpy.fft.fft(arr[row_slice[0]:row_slice[1], :, :], axis=-1)


def parallel_ffts(view, filename="data.npy"):
    """ Run a number of FFTs in parallel on a memory-mapped file."""
    arr = numpy.load(filename, mmap_mode='r')
    offsets = numpy.arange(len(view) + 1) * equal_size_split(arr, view)
    row_slices = zip(offsets[:-1], offsets[1:])
    files = [filename]*len(view)
    parallel_results = view.map(subsection_fft, row_slices, files, block=True)
    return parallel_results


def time_scaling(nengines=(1, 2, 4, 8), filename="data.npy", repeats=3):
    """Time FFT times for various cluster sizes."""
    client = Client()

    results = []
    for n in nengines:
        runs = []
        for i in range(repeats):
            client.clear()
            view = client[:n]
            tic = time.time()
            parallel_ffts(view, abspath(filename))
            toc = time.time()
            runs.append(toc-tic)
        results.append(min(runs))

    return results


if __name__ == "__main__":
    res = time_scaling(filename="data.npy", repeats=3)
