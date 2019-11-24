from typing import Any, Union

import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
from textblob import TextBlob

df: Union[Union[TextFileReader, DataFrame], Any] = pd.read_csv(
    '../../../../data/Womens Clothing E-Commerce Reviews.csv')
print(f'Data Frame Columns :\n{df.columns}')
print('**************************************')
df.drop('Unnamed: 0', axis=1, inplace=True)
print(f'Data Frame Columns :\n{df.columns}')
print('**************************************')
print(f'Data Frame :\n{df.head(5)}')
df_1 = df[df['Review Text'].isnull()]
print('**************************************')
print(f'Review Text Blank Dataframe:\n{df_1}')
df_2 = df[~df['Review Text'].isnull()]
print('**************************************')
print(f'Review Text Non-Blank Dataframe:\n{df_2}')


def pre_process(review_text):
    """
    Function for cleaning the text
    Args:
        review_text:

    Returns:
        object: review_text

    """
    review_text = review_text.str.replace("(<br/>)", "")
    review_text = review_text.str.replace('(<a).*(>).*(</a>)', '')
    review_text = review_text.str.replace('(&amp)', '')
    review_text = review_text.str.replace('(&gt)', '')
    review_text = review_text.str.replace('(&lt)', '')
    review_text = review_text.str.replace('(\xa0)', ' ')
    return review_text


df['Review Text'] = pre_process(df['Review Text'])
print(type(df['Review Text']))
dict_1 = {'Review Text': df['Review Text']}
df_3 = pd.DataFrame(dict_1)
df_3.to_csv('../../../../data/review_text.csv')
# df['Review Text'].to_csv('../../../../data/review_text.csv')
# print(f'Processed Review Text Dataset:\n{df["Review Text"]}')
df['polarity'] = df['Review Text'].map(lambda text: TextBlob(text).sentiment.polarity)
