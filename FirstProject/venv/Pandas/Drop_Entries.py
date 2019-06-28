import pandas as pd
import numpy as np
from pandas import Series, DataFrame

cars = Series(['BMW', 'Audi', 'Marc'], index=['a', 'b', 'c'])
print cars

cars = cars.drop('a')
print cars

# data frame

cars_df = DataFrame(np.arange(9).reshape(3, 3), index=['BMW', 'Audi', 'Marc'], columns=['rev', 'pro', 'exp'])
print cars_df

# Drop using the name and axis
cars_df = cars_df.drop('BMW', axis=0)
print cars_df

# type: DataFrame # Drop a column use the axis as an index number
cars_df1 = cars_df.drop('pro', axis=1)
print cars_df1
