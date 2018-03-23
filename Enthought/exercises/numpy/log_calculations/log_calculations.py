""" 
NumPy Log Calculations
----------------------

Read logs into numpy arrays and do various calculations with them.


1. Read in the logs found in the file :file:`short_logs.crv`.
   Use the function numpy.genfromtxt with the keyword option names=True.
   It returns a "structured array" that can behave similarly to a
   dictionary::

        >>> from numpy import genfromtxt
        >>> logs = genfromtxt('short_logs.crv', names=True)
        >>> logs['DEPTH']
        [8922.0, 8922.5, 8923.0, ...]
        >>> logs['S-SONIC']
        [171.7472, 171.7398, 171.7325, ...]

2. Get the VP and VSH logs out of the dictionary.

3. Remove samples where either VP or VSH has a NULL value.

4. Use array methods to calculate the peak-to-peak, mean and
   standard deviation for VP.

5. Now, use VSH to identify VP values for sand and shale.
   Assume VSH < 0.3 implies sand, and VSH > 0.7 implies shale.
   Print the peak-to-peak value, mean and standard deviation for
   each case.

6. Using VP, explore the methods found on the set of slides titled
   "Summary of array attributes/methods" 

See :ref:`log-calculations`.
"""
from numpy import genfromtxt

# 1. Read in the logs found in the file 'short_logs.crv'.
logs = genfromtxt('short_logs.crv', names=True)
