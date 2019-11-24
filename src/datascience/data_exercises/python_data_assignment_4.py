import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print("\nNumber of columns:")
print(len(df.columns))

# https://stackoverflow.com/questions/44717137/count-number-of-columns-with-some-values-for-each-row-in-pandas
# https://www.geeksforgeeks.org/python-pandas-dataframe-diff/
# https://pythondata.com/quick-tip-comparing-two-pandas-dataframes-and-getting-the-differences/