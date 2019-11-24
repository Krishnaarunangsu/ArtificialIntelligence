import pandas as pd
import numpy as np
import cufflinks as cf
import plotly
plotly.tools.set_credentials_file(username='arunangsu', api_key='Kolkata@15')
from textblob import TextBlob

# from plotly import plotly
# from chart_studio.plotly import plotly
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#
#
# cf.go_offline()
# # cf.set_config_file(offline=False, world_readable=True)
#
# init_notebook_mode(connected=True)
# cf.go_offline()
# plotly.offline.init_notebook_mode(connected=True)

# tls.embed('https://plot.ly/~cufflinks/8')


df = pd.read_csv('../../data/Womens Clothing E-Commerce Reviews.csv')
# df = df.drop(df.filter(regex='Unnamed'), axis=1, inplace=True)
# print(df.head())
# print(df.columns)

df_review_blank = df[df['Review Text'].isnull()]
df = df[~df['Review Text'].isnull()]
# print(df_review_blank.head())


def pre_process(review_text):
    review_text = review_text.str.replace("(<br/>)", "")
    review_text = review_text.str.replace('(<a).*(>).*(</a>)', '')
    review_text = review_text.str.replace('(&amp)', '')
    review_text = review_text.str.replace('(&gt)', '')
    review_text = review_text.str.replace('(&lt)', '')
    review_text = review_text.str.replace('(\xa0)', ' ')
    return review_text


df['Review Text'] = pre_process(df['Review Text'])
# print(df['Review Text'])

df['polarity'] = df['Review Text'].map(lambda text: TextBlob(text).sentiment.polarity)
df['review_len'] = df['Review Text'].astype(str).apply(len)
df['word_count'] = df['Review Text'].apply(lambda x: len(str(x).split()))

print('************************************************************************')
print(f'Polarity of the Dataset:\n{df["polarity"]}')
print('************************************************************************')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
df_good_polarity = df[df['polarity'] >= 0.7]
print(f'Good Polarity:\n{df_good_polarity}')
print('************************************************************************')
# print(df['review_len'])


print('5 random reviews with the highest positive sentiment polarity: \n')
cl = df.loc[df.polarity == 1, ['Review Text']].sample(5).values
for c in cl:
    print(c[0])


print('5 random reviews with the most neutral sentiment(zero) polarity: \n')
cl = df.loc[df.polarity == 0, ['Review Text']].sample(5).values
for c in cl:
    print(c[0])


print('2 reviews with the most negative polarity: \n')
cl = df.loc[df.polarity == -0.97500000000000009, ['Review Text']].sample(2).values
for c in cl:
    print(c[0])


# https://stackoverflow.com/questions/45286593/error-using-plotly-on-pycharm

df['polarity'].iplot(
    kind='hist',
    bins=50,
    xTitle='polarity',
    linecolor='black',
    yTitle='count',
    title='Sentiment Polarity Distribution')


