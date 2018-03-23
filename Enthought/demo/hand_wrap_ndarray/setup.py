from setuptools import setup, Extension
import numpy

ext = Extension(name='nan2zero', sources=['nan2zero.c', 'nan2zero_wrap.c'],
                include_dirs=[numpy.get_include()])

setup(name="nan2zero", ext_modules=[ext])
