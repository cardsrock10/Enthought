""" 
NumPy Log Calculations
----------------------

Read logs into numpy arrays and do various calculations with them.

    
1. Read in the logs found in the file :file:`short_logs.crv`.
   Use the CRV file reader found in :mod:`geoio.logs_io`.  It returns
   a "structured array" that can behave similarly to a  dictionary::

        >>> from geoio import logs_io
        >>> logs, header = logs_io.log_read('short_logs.crv')
        >>> logs['DEPTH']
        [8922.0, 8922.5, 8923.0, ...]
        >>> logs['S-SONIC']
        [171.7472, 171.7398, 171.7325, ...]

2. Grab the vp and vsh logs out of the dictionary.
   Print the peak-to-peak, sum, mean, and std of values for vp.

3. Remove samples where either vp or vsh has a NULL value.

4. Use array methods to calculate the peak-to-peak, mean, and std
   for vp.

5. Now, use vsh to identify vp values for sand and shale. 
   Print the peak-to-peak, mean, and std values for each case.        
   
6. Using vp, explore the methods found on the set of slides titled
   "Summary of array attributes/methods" 

See :ref:`geoio-log-calculations-solution`.
"""
from numpy import array, isfinite

# 1. Read in the logs found in the file 'short_logs.crv'.
from geoio import logs_io

logs, header = logs_io.log_read('short_logs.crv')
