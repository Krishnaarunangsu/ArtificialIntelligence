import pandas as pd

the_list = [['sentence 1'], ['sentence 2'], ['sentence 3']]
df_1 = pd.Series((v[0] for v in the_list))
print(df_1)

df_3 = pd.DataFrame(df_1)
print(df_3)
list_god = ['Krishna', 'Gopal', 'Jagannath']
df_2 = pd.Series((v for v in list_god))
print(df_2)