import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# revenue_df = ([1,2,3])

revenue_df = pd.read_clipboard()
# print revenue_df

# index amd columns
print revenue_df.columns
print revenue_df['Rank ']

# multiple columns
print DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry'])

# Nan Values only
revenue_df2 = DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry', 'Profit'])
print revenue_df2

# head and tail
print revenue_df.head(2)
print revenue_df.tail(2)

# access rows in df
print revenue_df.ix[0]
# this is for first row and the column name
print revenue_df.ix[5]
# this will show the last five rows

# assigning values to numpy
# numpy

array1 = np.array([1, 2, 3, 4, 5, 6])
revenue_df2['Profit'] = array1
print revenue_df2

# series
profits = Series([900, 1000], index=[3, 5])
revenue_df2['Profit'] = profits
print revenue_df2

# deletion
del revenue_df2['Profit']
print revenue_df2

# Dictionary
sample = {
    'company': ['A', 'B'],
    'Profit' : [1000, 5000]
}
print sample

sampl_df = DataFrame(sample)
print sample
