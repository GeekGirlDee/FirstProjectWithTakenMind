import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

#create new series as series1
series1 = Series([1, 2, 3, 4], index=['e', 'f', 'g', 'h'])
print series1

#creating new indexes using reindex
series2 = series1.reindex(['e', 'f', 'g', 'h', 'i', 'j'])
print series2

#using fillvalue
#it checks if a new value is created and if that is true it will
#assihn a new value to the index
series3 = series2.reindex(['e', 'f', 'g', 'h', 'i', 'j', 'k'], fill_value=10)
print series3

#using reindex methods => ffill
cars = Series(['VW', 'Audi', 'BMW'], index=[0, 4, 8])
print cars

ranger =range(13)
print ranger
cars = cars.reindex(ranger, method="ffill") #forward fill
print cars

#create new dataframe using randn
df_1 = DataFrame(randn(25).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print df_1

#reindexing rows of dataframe
df_2 = df_1.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
print df_2

#reindexing columns of dataframe
df_3 = df_2.reindex(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
print df_3

#using .ix[] to reindex
df_4 = df_1.ix[['a', 'b', 'c', 'd', 'e', 'f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]
print df_4
