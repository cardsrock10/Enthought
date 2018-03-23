"""
Read a text file into a list of lists.

Maybe *too* compact.
"""

print [[float(val) for val in l.split()]
       for l in open("rcs.txt", "r")
       if l[0] != "#"]
