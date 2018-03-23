""" 
NumPy Rockphysics
-----------------
    
Write a module called "rockphysics" that has a single
function called ggg that calculates bulk density (rhob)
from P-wave velocity (vp) using the Gardner, Gardner, 
Gregory relationship::

    rhob = 1.741*vp**0.25
    
Import that module into this module and use the ggg 
function to:

1. Calculate rhob from vp=2.0
2. Calculate rhob for all the values::
    
        vp = array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
   
3. Plot rhob vs. vp.    

See :ref:`numpy-rockphysics-solution`.
"""
from numpy import array
from matplotlib.pylab import plot, show, xlabel, ylabel

# Import the module [Use rockphysics in your example].
#import rockphysics
import rockphysics_solution as rockphysics

# 1. Calculate rhob for vp=2.0
vp = 2.0

# 2. Calculate rhob for vp array
vp = array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5]) # km/s

