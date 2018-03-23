""" 
Select Layer
------------

1. Read in the tops and logs from ud328.\*. Note: This step described here
   is already done in this file. 
       
   For the logs, use numpy.genfromtxt with names=True.
   For the tops, write a small function to read in the
   tops information.  It is in the following form::
 
        HEADER from GEOCAP ud-328.prn
        MARKER 9060 9060 SS    GXS_A
        MARKER 9073 9073 SS    GXS_B

   The first line is a header line that can be ignored.
   The 2nd column is the marker depth, and the last column
   is the marker name.  Read the markers into a dictionary where
   the marker name is the key and its depth is the value.

2. Pull out the VP, VS and RHOB values between the 
   GXS_E and GXS_F layers using masking.

3. Plot VS vs. VP and RHOB vs. VP.

4. Calculate the mean and standard deviation for
   each of the arrays.

See :ref:`select-layer-solution`.
"""
from numpy import genfromtxt, mean, std
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, show, figure

# 1. Read the logs and tops.

def tops_from_file(file_name):
    """ Return a dictionary tops marker, depth pairs from a file.
    """
    file = open(file_name)
    
    # Skip header line
    file.readline()
    
    tops = {}
    for line in file:
        fields = line.split()
        depth = float(fields[1])
        top = fields[4]
        tops[top] = depth
    return tops        

tops = tops_from_file('ud328.top')
logs = genfromtxt('ud328.crv', names=True)
