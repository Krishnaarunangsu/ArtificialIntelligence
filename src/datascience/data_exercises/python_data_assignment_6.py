import pandas as pd

the_list = [['sentence 1'], ['sentence 2'], ['sentence 3']]
df_1 = pd.Series((v[0] for v in the_list))
print(df_1)

list_god = ['Krishna', 'Gopal', 'Jagannath']
df_2 = pd.Series((v for v in list_god))
print(df_2)

# https://stackoverflow.com/questions/21646791/convert-python-list-to-pandas-series
# https://www.geeksforgeeks.org/create-a-pandas-series-from-array/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.array.html
# https://datascience.stackexchange.com/questions/26333/convert-a-list-of-lists-into-a-pandas-dataframe
# https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
# https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm
# https://www.ritchieng.com/creating-dataframe-from-objects/