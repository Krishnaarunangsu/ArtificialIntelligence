import pandas as pd

# Creating the dataframe from csv
df_nba = pd.read_csv('../../../data/nba.csv')
print(f'Dataframe:\n{df_nba}')
print('****************************************')
# to print the full summary
print(f'Full Summary of the Dataframe:\n{df_nba.info}')
print('*******************Full Summary of the Dataframe*********************')
print(f'{df_nba.info(verbose=True, null_counts=False)}')
print('*******************Short Summary of the Dataframe*********************')
# Print the short summary of the
# dataframe by setting verbose = False
print(f'{df_nba.info(verbose=False)}')
# Print the full summary of the dataframe
# with null count excluded
print(f'{df_nba.info(verbose=True, null_counts=False)}')

# https://www.geeksforgeeks.org/python-pandas-dataframe-info/
