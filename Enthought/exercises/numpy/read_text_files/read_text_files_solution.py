""" 
Read text files with genfromtxt or loadtxt
------------------------------------------

In the following, you are asked to use genfromtxt() or loadtxt() to
read a text file into a numpy array.  These files demonstrate some
common challenges that arise when reading text files.

1. The file data1.out looks like this::

      NAME|RATIO|ALPHA|BETA|AGE
      BE45|1.3|99.32|14.3|17.5
      WN33|5.1|78.19|18.0|5.3
      KP10||48.19|65.0|24.0
      KM44|6.6|81.25|31.0|16.0
      KM45|6.6|80.00|34.0|16.0
      KR21||45.0|60.0|24.0
      WN51|5.5|80.00|15.0|4.0

   Note that the fields are separated with a vertical bar.  Also note that
   there are a few missing values in the "RATIO" column.
  
   Use genfromtxt(), with appropriate arguments, to read this data into a
   structured array.  Replace the missing "RATIO" values with the value 1.0
   as the data is read.
  
   Print the mean values of the RATIO and AGE columns.

2. Last year your summer intern developed a FORTRAN program which wrote three
   columns of data (x, y, and z) to a text file.  You have just run it again,
   but with parameter values very different from what you used last time.
   You find that the output, data2.out, contains these lines::

       5.000 80.103  4.003
      15.000 84.544  1.984
      25.000 95.041  2.887
      35.000 99.522  4.095
      45.000107.543  5.163
      55.000113.834  6.554
      65.000117.543  8.234
      75.000121.077 11.400
      85.000120.813 13.481
      95.000119.549 15.333
     105.000117.435 16.501

   There are supposed to be three columns, but the values in the middle
   column are bigger than before, and now there is no space between the first
   and second columns after the first four rows.

   genfromtxt() can deal with this; read the docstring, paying special
   attention to the 'delimiter' argument.

   Use genfromtxt() to read this file, and use matplotlib with subplot to
   make two plots, y vs. x and z vs. x, in a single plot figure.


3. Here is the file data3.csv::

      code,sales,zip
      ER,17.5,78701
      ER,8.9,78704
      ER,1.4,78703
      ER,19.2,77036
      ER,18.1,77251
      ER,4.0,77281
      HN,1.4,80026
      HN,3.2,80301
      HN,0.5,80302
      HN,1.0,80303
      HN,0.3,80466
      KP,4.9,02101
      KP,0.2,02102
      KP,1.0,02103
      KP,0.9,02104
      KP,1.8,02105
      TY,0.3,04401
      TY,0.1,04406
 
   The third column is a Zip Code.  Read this data into a numpy structured
   array, such that the Zip Code data is stored as a five character string.

"""

import matplotlib.pyplot as plt
from numpy import genfromtxt

# 1. Solution

data = genfromtxt("data1.out", delimiter='|', dtype=None, names=True,
                  missing_values='', filling_values='1')

print
print "Part 1: data is"
print data
print "Mean RATIO is", data['RATIO'].mean()
print "Mean AGE is", data['AGE'].mean()

# 2. Solution

# Each field is 7 characters wide, so using delimiter=(7,7,7) will work.
data = genfromtxt('data2.out', delimiter=(7,7,7))

print
print "Part 2: plotting..."
plt.clf()
plt.subplot(2, 1, 1)
plt.plot(data[:,0], data[:,1], 'bo-')
plt.ylabel('y')
plt.title('Data from "data2.out"')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(data[:,0], data[:,2], 'ro-')
plt.ylabel('z')
plt.xlabel('x')
plt.grid(True)
plt.show()

# 3. Solution

data = genfromtxt("data3.csv", delimiter=',', dtype=('S2', 'float64', 'S5'),
                  names=True)

print
print "Part 3: data is"
print data
