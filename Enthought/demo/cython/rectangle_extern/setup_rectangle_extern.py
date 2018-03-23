"""
Setup.py from cython documentation to show how to wrap custom c++ code with
cython.
"""

from setuptools import setup, Extension
from Cython.Distutils import build_ext

# Skipping this method to build the extension because it fails with cython 0.16
"""
from Cython.Build import cythonize
setup(ext_modules = cythonize(
           "rectangle.pyx",            # our Cython source
           sources=["rectangle_extern.cpp"],  # additional source file(s)
           language="c++",                    # generate C++ code
      ),
  cmdclass = {'build_ext': build_ext}
  )
"""

ext = Extension("rectangle", sources = ["rectangle.pyx",
                                        "rectangle_extern.cpp"],
                language="c++")
setup(
  ext_modules=[ext],
  cmdclass = {'build_ext': build_ext}
)
