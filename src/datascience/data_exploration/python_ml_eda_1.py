import pandas as pd

# Creating the dataframe from csv
df_nba = pd.read_csv('../../../data/nba.csv')
print(f'Dataframe Columns:\n{df_nba.columns}')
print('****************************************')
# Getting dataframe columns from iterables
for column in df_nba.columns:
    print(f'Column Name is:{column}')
    print(f'Column dtype is: {df_nba[column].dtype}')
    print('#####################################')

print('********************Converting dataframe column iterables to list********************')
# Converting dataframe column iterables to list
dataframe_column_list: list = list(df_nba.columns)
print(f'Dataframe Column List:\n{dataframe_column_list}')
print('********************column.values method returns an array of index.********************')
# column.values method returs an array of index.
dataframe_column_array = list(df_nba.columns.values)
print(f'Dataframe Column Array:\n{dataframe_column_array}')
print('********************Converting dataframe column iterables to list********************')
dataframe_column_list_2: list = list(df_nba.columns.values.tolist())
print(f'Dataframe Column List:\n{dataframe_column_list_2}')
print('********************Converting dataframe column iterables to list********************')
#  Using sorted() method
# Sorted() method will return the list of columns sorted in alphabetical order.
sorted_dataframe_column_list = sorted(dataframe_column_list)
print(f'Sorted Dataframe Column List:\n{sorted_dataframe_column_list}')

# dtypes, types
# https://pbpython.com/pandas_dtypes.html
# https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/
# https://www.geeksforgeeks.org/how-to-select-multiple-columns-in-a-pandas-dataframe/
