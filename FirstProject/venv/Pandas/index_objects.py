import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print series1

index1 = series1.index
print index1

print index1[2:]

#negative indexes are important for project creation
print index1[-2:]
print index1[:-2]

print index1[2:3]
print index1[2:4]

#
index1[0] = 'e' #it is not allowed in series and dataframe
print index1
