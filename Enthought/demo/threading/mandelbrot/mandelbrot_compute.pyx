#cython: boundscheck=False
cimport cython
cimport numpy as np


cdef int mandelbrot_escape(double complex c, int n) nogil:
    """ Mandelbrot set escape time algorithm in real and complex components
    """
    cdef double complex z
    cdef int i
    z = c
    for i in range(n):
        z = z*z + c
        if z.real*z.real + z.imag*z.imag >= 4.0:
           break
    else:
        i = -1
    return i


def generate_mandelbrot(
        cython.floating[:] xs,
        cython.floating[:] ys,
        cython.integral[:, :] d_trans,
        int n):
    """ Generate a mandelbrot set """
    cdef unsigned int i,j
    cdef unsigned int N = len(xs)
    cdef unsigned int M = len(ys)
    cdef double complex z

    with nogil:
        for j in range(M):
            for i in range(N):
                z = xs[i] + ys[j]*1j
                d_trans[i, j] = mandelbrot_escape(z, n)
