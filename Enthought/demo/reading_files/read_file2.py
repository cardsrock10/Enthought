"""
Read a text file into a list of lists.

Use a list comprehension.
"""


results = []
f = open('rcs.txt', 'r')

# Skip the first line.
f.readline()

# Read values and convert them to float.
for line in f:
    all = [float(val) for val in line.split()]
    results.append(all)
f.close()

# Print results.
for i in results:
    print i
