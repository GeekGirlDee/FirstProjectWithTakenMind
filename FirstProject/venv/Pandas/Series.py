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
s = Series(data_array,index= ['index1', 'index2','index3'])
print s

# Using real life examples
revenue = Series([20, 80, 40, 35], index=['ola', 'uber', 'grab', 'goje'])
print revenue['ola']
#Condition statement inside a condition
print revenue[revenue>=35]

#using boolean to check if the condition is avalable
print 'ola' in revenue

revenue_dict = revenue.to_dict()
print revenue_dict

# this is used when data is been added and user needs to see what has been included
# and which index is not complete
index2 = ['ola', 'uber', 'grab', 'goje','lyft']
revenue2 = Series(revenue,index2)
print revenue2

# This code shows if there are null values in the data type
print pd.isnull(revenue2)  # this uses a boolean operator
print pd.notnull(revenue2)

# addition of series is adding to series together
print revenue + revenue2

#this is to assign names to variables
revenue2.name="Company Revenues"
revenue2.index.name="Company Names"
print revenue2
