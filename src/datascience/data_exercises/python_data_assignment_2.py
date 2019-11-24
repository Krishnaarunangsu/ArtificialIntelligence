# Syntax:
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
# Every parameter has some default values execept the ‘by’ parameter.
# Parameters:
# by: Single/List of column names to sort Data Frame by.
# axis: 0 or ‘index’ for rows and 1 or ‘columns’ for Column.
# ascending: Boolean value which sorts Data frame in ascending order if True.
# inplace: Boolean value. Makes the changes in passed data frame itself if True.
# kind: String which can have three inputs(‘quicksort’, ‘mergesort’ or ‘heapsort’) of algorithm used to sort data frame.
# na_position: Takes two string input ‘last’ or ‘first’ to set position of Null values. Default is ‘last’.

# Return Type:
# Returns a sorted Data Frame with Same dimensions as of the function caller Data Frame.

# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("../../../data/nba.csv")

# display
print(data)
print('********************************************')
data_1 = data.sort_values("Name", axis=0, ascending=True,
                          inplace=False, na_position='last')

print(data_1)

print('********************************************')
data.sort_values("Name", axis=0, ascending=True,
                 inplace=True, na_position='last')

print(data)

# sorting data frame by name
data.sort_values("Salary", axis=0, ascending=True,
                 inplace=True, na_position='first')
# display
print(data)

# https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-1/
# https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-2/
# https://www.geeksforgeeks.org/python-pandas-dataframe-sample/
# https://www.geeksforgeeks.org/python-pandas-series-reset_index/

