import pandas as pd
import numpy as np


df = pd.read_csv('../../../data/data_handling_1.csv')
print(df)
df['Activate'] = np.where(df['Activate'] == 'Y', True, False)
print(df['Activate'].dtype)