import pandas as pd
from pandas import Series
import numpy as np

object = Series([5, 10, 15, 20])
print object

# shows that it starts at 0 and stops at 4 and steps once
print object.values
print object.index

# using numpy arrays in series
data_array = np.array((['a', 'b', 'c']))
s = Series(data_array)
print s

#custom index also for change of index values
s = Series(data_array, index=[100, 101, 102])
print s
s = Series(data_array)