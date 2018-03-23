""" 
1. Read in the tops and logs from ud328.\*. Note: This step described here is 
   already done in this file. 
       
   For the logs, use the geoio.logs_io module.
   For the tops, write a small function to read in the
   tops information.  It is in the following form::
 
        HEADER from GEOCAP ud-328.prn
        MARKER 9060 9060 SS    GXS_A
        MARKER 9073 9073 SS    GXS_B

   The first line is a header line that can be ignored.
   The 2nd column is the marker depth, and the last column
   is the marker name.  Read the markers into a dictionary where
   the marker name is the key and its depth is the value.

2. Pull out the vp, vs and rhob values between the 
   GXS_E and GXS_F layers using masking.
3. Plot vs vs. vp and rhob vs. vp.
4. Calculate the mean and standard deviation for
   each of the arrays.
"""
from numpy import array, isnan, NaN, mean, std
from matplotlib.pyplot import plot, subplot, xlabel, ylabel, title, show, figure

from geoio import logs_io

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
logs, header = logs_io.log_read('ud328.crv')


# 2. Extract all values between GXS_E and GXS_F
all_depths = logs['DEPTH']
top = tops['GXS_E']
bottom = tops['GXS_F']

mask = (all_depths>=top) & (all_depths<bottom)
layer_logs = logs[mask]
depth = layer_logs['DEPTH']
vp = layer_logs['VP']
vs = layer_logs['VS']
rhob = layer_logs['RHOB']

# 3. Plot vs against vp and rhob against vp.
figure()
subplot(121)
plot(vp,vs,'o')
xlabel('vp')
ylabel('vs')
title('GXS_E layer')
subplot(122)
plot(vp,rhob,'o')
xlabel('vp')
ylabel('rhob')
title('GXS_E layer')
show()

# 4. Calculate the mean and std for vp, vs, and rhob in this layer.
print 'vp (mean, std):', mean(vp), std(vp)
print 'vs (mean, std):', mean(vs), std(vs)
print 'rhob (mean, std):', mean(rhob), std(rhob)

