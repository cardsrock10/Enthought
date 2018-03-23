from numpy.distutils.core import setup, Extension
import os


os.system("swig -python example3b.i")

sources = ['example3b_wrap.c', 'vect.c']

setup(name="_example3b",
      version="1.0",
      ext_modules=[Extension("_example3b", sources)])
