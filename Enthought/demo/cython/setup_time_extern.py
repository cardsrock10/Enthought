from setuptools import setup, Extension
from Cython.Distutils import build_ext

setup(
  ext_modules=[ Extension("time_extern", ["time_extern.pyx"]) ],
  cmdclass = {'build_ext': build_ext}
)
