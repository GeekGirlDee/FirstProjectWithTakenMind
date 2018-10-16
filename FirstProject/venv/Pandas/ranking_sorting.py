import numpy as np
import pandas as pd
from pandas import Series
from numpy.random import randn

ser1 = Series([500, 1000, 1500], index=['a','c','b' ])
print ser1

#sorting arraays by index
print ser1.sort_index()

#Sort by values
print "Sort by values"
print ser1.sort_values()

print ser1.rank()

# Ranking of series is the basics of sorting
ser2 = Series(randn(10))
print ser2
print ser2.rank()
print ser2.sort_values()
print ser2.rank()



