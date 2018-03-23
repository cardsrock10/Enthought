""" Read logs into numpy arrays and do various calculations with them.

    
    1. Read in the logs found in the file 'short_logs.crv'.
       Use the CRV file reader found in geoio.logs_io.  It will return
       a "structured array" that can behave similarly to a  dictionary:
    
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
"""
from numpy import array, isfinite

# 1. Read in the logs found in the file 'short_logs.crv'.
from geoio import logs_io

logs, header = logs_io.log_read('short_logs.crv')
        
# 2. Grab the vp and vsh logs out of the dictionary.  Calculate
#    Print out the peak-to-peak, sum, mean, and std of values for vp.
vp = logs['VP']
vsh = logs['VSH']

# 3. remove samples where either vp or vsh has a NULL value.
nan_mask = isfinite(vp) & isfinite(vsh)
vp = vp[nan_mask]
vsh = vsh[nan_mask]

# 4. Use array methods to calculate the peak-to-peak, sum, mean, and std
#    for vp.
print 'vp peak-to-peak:', vp.ptp()   
print 'vp mean:', vp.mean()   
print 'vp std:', vp.std()


# 5. Now, use vsh to identify vp values for sand and shale. 
# Print their peak-to-peak mean, and std values for each case.
vp_sand = vp[vsh<.3]
vp_shale = vp[vsh>.7]

print 'sand vp (samples, mean, std, peak-to-peak): %d, %3.2f, %3.2f, %3.2f' % \
         (len(vp_sand), vp_sand.mean(), vp_sand.std(), vp_sand.ptp())
print 'shale vp (samples, mean, std, peak-to-peak):%d, %3.2f, %3.2f, %3.2f' % \
         (len(vp_shale), vp_shale.mean(), vp_shale.std(), vp_shale.ptp())
   
        
        
