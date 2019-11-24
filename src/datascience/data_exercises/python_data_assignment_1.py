import pandas as pd
import numpy as np

movies_df = pd.read_excel('../../../data/movie_ticket_sales.xlsx')
print(movies_df)
print('**********************************************************')
print(movies_df.info())
print('**********************************************************')
print(movies_df.describe())
print('**********************************************************')
movies_portland_df_check = movies_df['theater_location'] == 'PortLand'
print(movies_portland_df_check)
print('**********************************************************')
movies_portland_df = movies_df[movies_df['theater_location'] == 'PortLand']
print(movies_portland_df)
print('**********************************************************')
movies_portland_df_sorted_by_ticket_quantity = movies_portland_df.sort_values(by='ticket_quantity', ascending=False)
print(movies_portland_df_sorted_by_ticket_quantity)
print('**********************************************************')
print(movies_portland_df_sorted_by_ticket_quantity.reset_index())
print('**********************************************************')
print(movies_portland_df_sorted_by_ticket_quantity.reset_index(drop=True))
print('**********************************************************')
print(movies_portland_df.head())
print('**********************************************************')
print(movies_portland_df.head(3))
print('**********************************************************')
print(movies_portland_df_sorted_by_ticket_quantity.head(1))
print('**********************************************************')
print(movies_portland_df_sorted_by_ticket_quantity.reset_index().head(1))
print('**********************************************************')
movies_df['sales_usd'] = movies_df['ticket_quantity'] * 20
print(movies_df)
print('**********************************************************')
# movies_df_movie_name = movies_df.groupby('theater_location').groups
movies_df_movie_name = movies_df.groupby('theater_location')
print(movies_df_movie_name)
print('**********************************************************')
print(movies_df_movie_name.first())



# https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/