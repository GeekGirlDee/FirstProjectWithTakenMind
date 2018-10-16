from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

# 2d array
# np.nan stands for non value
array1 = np.array([[10,np.nan,20],[30,40,np.nan]])
print array1

# creating a Data Frame
# this dataframe will print out the index which is the row number labled 1 2
# columns are numbered  A B C
df1 = DataFrame(array1, index=[1,2],columns=list('ABC'))
print df1

#Sum operarions well known as sum() in python
# this will sum up each column
print df1.sum()
#this is to calculate each row/indexes
print df1.sum(axis=1)

#This will show the minimum values of the column
print "Minimun"
print df1.min()

#This will show the maximum values of the column
print "Maximum"
print df1.max()

#This will show the minimum and maximum values of the index
# It does not show the value but shows the index/ row of the values with the min and max values
print "Max of index"
print df1.idxmax()

print "Min of index"
print df1.idxmin()

# Cumilitive Sums leave the first index as it is
# and adds the second index with the first indexx to get the outcome
print "Cumulitive Sum"
print df1.cumsum()

# Describe function helps with oral sets such as:
# count, mean, standard deviation, minimum, mpercentages (25%, 50%, 75%) and max
print "Describe Function"
print df1.describe()

#this dataframe looks at random numbers with a 3*3 grid
# it has an index of 123 and column ABC
df2 = DataFrame(randn(9).reshape(3,3),index=[1,2,3],columns=list('ABC'))
print "New DataFrame"
print df2
# a graph is created to show the values of the dataframe
#plt.plot(df2)
#plt.legend(df2.columns, loc="lower right")
#plt.savefig('dataframe.png')
#plt.show()

ser1 =Series(list('abccaabd'))
print "abc"
print ser1.unique()

# show the frequency in which the number are represented in a series
# it shows the each value on the list and the number which represents
# the number of times it appears
print "Frequency"
print ser1.value_counts()