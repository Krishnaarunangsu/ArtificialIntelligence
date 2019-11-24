import pandas as pd
Df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/car/Chile.csv")
print(Df.columns)
print('***************************************************************************************')
column_list = [column for column in Df.columns]
print(column_list)
print('***************************************************************************************')
# print(Df)
print(Df.describe())
print('***************************************************************************************')
# Df.drop(Df.columns[Df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
print(Df.columns.str.contains('unnamed', case=False))
print(Df.columns[Df.columns.str.contains('unnamed', case=False)])
print('***************************************************************************************')
Df = Df.loc[:, ~Df.columns.str.contains('^Unnamed')]
# df = pd.read_csv('data.csv', index_col=0)
print(Df.describe())

# Df.drop(Df.columns[Df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
education_value_counts = Df["education"].value_counts()
print(f'Hi:{education_value_counts}')
