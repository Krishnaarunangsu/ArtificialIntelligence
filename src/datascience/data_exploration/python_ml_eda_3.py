import numpy as np
import pandas as pd

df_sales_data = pd.read_csv("../../../data/sales_data_types.csv")
print(f'Sales Data:{df_sales_data}')
print(df_sales_data[['2016', '2017']])
# print(df_sales_data['2016'] + df_sales_data['2017'])
print(f'Dataframe DTypes:\n{df_sales_data.dtypes}')
print('*******************************************')
print(f'Dataframe DTypes:\n{df_sales_data.info()}')
print('*******************************************')
print(df_sales_data['Customer Number'].astype('int'))
df_sales_data["Customer Number"] = df_sales_data['Customer Number'].astype('int64')
print('*******************************************')
print(f'Dataframe DTypes:\n{df_sales_data.dtypes}')
print('*******************************************')
print(f'Dataframe-Sales Data:\n{df_sales_data}')
