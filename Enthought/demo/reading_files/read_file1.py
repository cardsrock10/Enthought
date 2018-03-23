"""
Read a text file into a list of lists.
"""


results = []
f = open('rcs.txt', 'r')

# Read all the lines.
lines = f.readlines()
f.close()

# Discard the header.
lines = lines[1:]

for line in lines:
    # Split each line into fields.
    fields = line.split()
    # Convert text to numbers.
    freq = float(fields[0])
    vv = float(fields[1])
    hh = float(fields[2])
    # Group and append to results.
    all = [freq, vv, hh]
    results.append(all)

for i in results:
    print i
