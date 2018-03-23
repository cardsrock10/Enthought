""" This file provides a supporting function for the financial_plot exercise.
Refer to the financial_plot.py file for the description of the exercise.
"""
import numpy as np


def load_stock_data(filename):
    with open(filename) as f:
        headers = f.readline().strip().split(",")
        dtype = [(name, 'f4') for name in headers[1:]]
        dtype = [("date", "datetime64[D]")] + dtype

        # Aug2014: there is a bug in genfromtxt with Python3, so we can't pass
        # the file object without getting a
        # TypeError: Can't convert 'bytes' object to str implicitly

        #data = np.genfromtxt(f, delimiter=",", dtype=dtype)
    data = np.genfromtxt(filename, skiprows=1, delimiter=",", dtype=dtype)
    return data
