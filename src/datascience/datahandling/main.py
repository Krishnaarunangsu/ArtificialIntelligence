import pandas as pd

data = pd.read_csv('../../../data/bank.csv')
print(data.describe())