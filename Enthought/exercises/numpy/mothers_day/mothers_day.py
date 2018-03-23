"""
Mother's day
============

In the USA and Canada, Mother's Day is the second Sunday of May. Use
NumPy's datetime64 data type and datetime64 utilities to compute the date of
Mother's Day for the current year.

Note: NumPy datetime64 values can be created from a string with the format
YYYY-MM-DD HH:MM:SS.sss where everything after the year designation is
optional.

Bonus
~~~~~
Extract the current year programmatically using the datetime module from the
standard library.
"""
from numpy import busday_offset, datetime64
from datetime import datetime
