# Find empty or NaN entry in Pandas Dataframe
import numpy as np
import pandas as pd
from src.datascience.datahandling.csv_reader import CSVReader

csv_reader = CSVReader('../../../data/train3.csv')
dataframe_result: object = csv_reader.import_data()
print(f'Original Content-Dataframe:\n{dataframe_result}')
print('*********************************************************')
print(np.where(pd.isnull(dataframe_result)))
print(dataframe_result.iloc[2, 5])
print(np.where(dataframe_result.applymap(lambda x: x == '')))

# https://stackoverflow.com/questions/27159189/find-empty-or-nan-entry-in-pandas-dataframe
# https://thispointer.com/pandas-4-ways-to-check-if-a-dataframe-is-empty-in-python/
