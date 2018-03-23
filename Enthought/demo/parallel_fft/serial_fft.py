"""
Serial FFT for comparison to Parallel FFT.

Timings on a Macbook Pro: 2.3GHz Intel Core i7, 8GB Memory
>>> timeit serial_fft.main()
1 loops, best of 3: 6.98 s per loop
"""

import numpy as np

def main(filename="data.npy"):
    arr = np.load(filename)
    serial_result = np.fft.fft(arr, axis=-1)
