"""
NumPy Log Calculations
----------------------

Read logs into numpy arrays and do various calculations with them.
 
"""
from numpy import genfromtxt

# 1. Read in the logs found in the file 'short_logs.crv',
logs = genfromtxt('short_logs.crv', names=True)

# 2. Get the VP and VSH logs out of the dictionary. 
vp = logs['VP']
vsh = logs['VSH']

# 3. Remove samples where either VP or VSH has a NULL value.
good_mask = (vp != -999.25) & (vsh != -999.25)
vp = vp[good_mask]
vsh = vsh[good_mask]

# 4. Use array methods to calculate the peak-to-peak value, mean and
#    standard deviation for VP.
print 'vp peak-to-peak:', vp.ptp()   
print 'vp mean:', vp.mean()   
print 'vp std:', vp.std()

# 5. Now, use VSH to identify VP values for sand and shale.
vp_sand = vp[vsh<.3]
vp_shale = vp[vsh>.7]

print 'sand vp (samples, mean, std, peak-to-peak): %d, %3.2f, %3.2f, %3.2f' % \
         (len(vp_sand), vp_sand.mean(), vp_sand.std(), vp_sand.ptp())
print 'shale vp (samples, mean, std, peak-to-peak):%d, %3.2f, %3.2f, %3.2f' % \
         (len(vp_shale), vp_shale.mean(), vp_shale.std(), vp_shale.ptp())
   
        
        
