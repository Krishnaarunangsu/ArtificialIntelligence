# Import Libraries

# This is to suppress the warning messages (if any) generated in our code
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

# Comment this if the data visualisations doesn't work on your side
# %matplotlib inline

# We are using whitegrid style for our seaborn plots. This is like the most basic one
sns.set_style(style='whitegrid')
# dataset = pd.read_csv('../input/train.csv')
dataset = pd.read_csv('../../../data/train.csv')
print(f'Dataframe Details:\n{dataset.describe()}')
print('******************************************')
print(f'Dataset Summary-Full:{dataset.info()}')
print('******************************************')
print(f'Dataset Summary-Short:{dataset.info(verbose=False)}')
assert isinstance(dataset.shape, object)
nrow, ncol = dataset.shape
#print(nrow, ncol)
print('******************************************')
print(f'Dataset Shape:{nrow, ncol}')
# Let's look at first few rows of our dataset
print('*******************First three rows of Dataset***********************')
print(dataset.head(3))

# Create a separate dataframe which has only Categorical Variables
print('*******************Categorical Columns of the Dataset***********************')
ds_cat = dataset.select_dtypes(include='object').copy()
print(ds_cat.head(2))

# Basic Stats for each variable
print(ds_cat['MSZoning'].unique())
print(len(ds_cat['MSZoning'].unique()))

# Count of distinct categories in our variable but this time we don't want to count any nan values
print(ds_cat['MSZoning'].nunique())

# Number of Missing Values in that variable (for all the rows)
print(ds_cat['MSZoning'].isnull().sum())

# Percentage of Missing Values in that variable
print(ds_cat['MSZoning'].isnull().sum() / nrow)

# Let's multiple by 100 and keep only 1 decimal places
print((ds_cat['MSZoning'].isnull().sum() / nrow).round(3) * 100)

# Count Plot by MSZoning
sns.countplot(data=ds_cat, x='MSZoning')
# plt.show()

# Since we are working on a supervised ML problem we should also look at the relationship
# between the dependent variable and independent variable. In order to do that let's add
# our dependent variable to this dataset.
ds_cat['SalePrice'] = dataset.loc[ds_cat.index, 'SalePrice'].copy()
len(ds_cat.columns)  # 43 means 11 rows will be needed

#  Box Plot
sns.boxplot(data=ds_cat, x='MSZoning', y='SalePrice')
# plt.show()

# Violin Plot
sns.violinplot(data=ds_cat, x='MSZoning', y='SalePrice')
plt.show()

# Swarm Plot
sns.swarmplot(data=ds_cat, x='MSZoning', y='SalePrice')

# Combine Violin Plot & Swarm Plot
sns.violinplot(data=ds_cat, x='MSZoning', y='SalePrice')
sns.swarmplot(data=ds_cat, x='MSZoning', y='SalePrice', color='k', alpha=0.6)

# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way
# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way/notebook
# https://towardsdatascience.com/a-starter-pack-to-exploratory-data-analysis-with-python-pandas-seaborn-and-scikit-learn-a77889485baf
# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-a-beginner-s-way
# https://machinelearningmastery.com/automate-machine-learning-workflows-pipelines-python-scikit-learn/
