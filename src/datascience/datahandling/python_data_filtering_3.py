import pandas as pd
import numpy as np


numpy_series_1 = np.arange(10)
dataframe_1 = df = pd.DataFrame(numpy_series_1.reshape(-1, 2), columns=['A', 'B'])
print(dataframe_1)

filter_1 = dataframe_1 % 3 == 0
print(f'Filter:\n{filter_1}')
print(f'Filter Inversed:\n{~filter_1}')

dataframe_1_updated = dataframe_1.where(filter_1, -dataframe_1)
print(dataframe_1_updated)

# dataframe where vs numpy where
dataframe_1_check = dataframe_1.where(filter_1, -df) == np.where(filter_1, dataframe_1, -dataframe_1)
print(dataframe_1_check)

dataframe_11_check = dataframe_1.where(filter_1, -df) == dataframe_1.mask(~filter_1, -df)
print(dataframe_11_check)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.where.html