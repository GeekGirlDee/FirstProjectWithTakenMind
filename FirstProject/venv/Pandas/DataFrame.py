import pandas as pd
from pandas import Series, DataFrame

#revenue_df = ([1,2,3])

revenue_df = pd.read_clipboard()
print revenue_df

#index amd columns
print revenue_df.columns
print revenue_df['Rank ']

#multiple columns
print DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry'])
