from typing import Any, Union

import pandas as pd
import numpy as np
from pandas import Series
from pandas.core.generic import NDFrame

series_1 = pd.Series([0, 1, 2, 3, 4])

# Replace '0' with '5'
series_1_updated: Union[Union[None, Series, NDFrame], Any] = series_1.replace(0, 5)
print(series_1_updated)

series_11_updated = series_1.mask(series_1 > 0)
print(series_11_updated)

series_12_updated = series_1.where(series_1 > 1, 10)
print(series_12_updated)

df_1 = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                     'B': [5, 6, 7, 8, 9],
                     'C': ['a', 'b', 'c', 'd', 'e']})
df_1.replace(0, 5)
print(df_1)
pattern_1 = [0, 1, 2, 3]
df_2 = df_1.replace(pattern_1, 4)
print(df_2)

pattern_2 = [4, 3, 2, 1]
df_3 = df_1.replace(pattern_1, pattern_2)
print(df_3)

df_4 = df_1.replace([1, 2], method='bfill')
print(f'Back Fill:\n{df_4}')

df_5 = df_1.replace([1, 2], method='ffill')
print(f'Front Fill:\n{df_5}')

series_2 = np.arange(10)
print(series_2)
print(series_2.dtype)

df_1.replace([0, 1, 2, 3], 4)
print(df_1)

df_2 = df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
print(df_2)

df_3 = df = pd.DataFrame(np.arange(10).reshape(2, -1), columns=['A', 'B', 'C', 'D', 'E'])
print(df_3)

df_4 = df = pd.DataFrame(np.arange(10).reshape(-2, 1), columns=['A'])
print(df_4)

df_5 = df = pd.DataFrame(np.arange(10).reshape(1, -2), columns=['A',  'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print(df_5)
