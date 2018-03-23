"""
Lithology String
----------------

You are given the following string:

   lith = "s s s S l L l l L q q Q q s s L l q "

"lith" is a string of lithology flags where each character
represents the lithology for a log sample in the well.

* s: shale
* q: quartz
* l: limestone

Ignoring case, find the percentage of each lithology type
within the well.
"""

lith = "s s s S l L l l L q q Q q s s L l q "

# force everything to lower case.
lith = lith.lower()

# now count the yes votes.
shale = lith.count("s")
quartz = lith.count("q")
limestone = lith.count("l")

total = shale + quartz + limestone

# Notice cast to float! Otherwise you have an integer division.
print "percentage of each lithology:"
print "% shale:", shale/float(total) * 100
print "% quartz:", quartz/float(total) * 100
print "% limestone:", limestone/float(total) * 100

# Alternative approach using future behavior of integer
# division yielding floats.
# NOTE: THIS LINE MUST BE AT BEGINNING OF FILE
#from __future__ import division
#
#print "percentage of each lithology:"
#print "% shale:", shale/total * 100
#print "% quartz:", quartz/total * 100
#print "% limestone:", limestone/total * 100
