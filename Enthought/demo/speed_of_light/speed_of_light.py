
# Numeric library imports
from numpy import loadtxt

# Plotting imports
from matplotlib import pyplot as plt

# Distance light traveled in Newcomb's experiment
distance = 7400.0

# Read the measurements from the data file.
# There are a number of comments at the top of the file marked with "#"
measured_time = loadtxt('speed_of_light.dat', comments="#")

# measurements were in nanseconds difference from 24800 ns.
measured_time += 24800.0

# Convert measured times to measured velocities.
measured_velocity = distance / measured_time * 10.0  # m/ns * 10 == 1e8m/s

# Plot a bar plot of the histogrammed data.
plt.hold(False)

plt.hist(measured_velocity, bins=30)

plt.xlabel("velocity (1e8 m/s)")
plt.ylabel("counts")
plt.title("Newcomb's Speed of Light Measurement Histogram")

# Put a vertical line in where the actual velocity is.
actual = 2.99792458
plt.axvline(actual, color='r', linewidth=2, hold=True)
plt.axis('auto')

# Ensure that the plot is shown.
plt.show()
