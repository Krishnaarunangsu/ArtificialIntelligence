# Dummy Variables for Nominal
# Ordinal vs. Nominal
# In general, one would translate categorical variables into dummy variables (or a host of other methodologies), because they were nominal, e.g. they had no sense of a > b > c . In OPs original question, this would only be performed on the Cities, like London, Zurich, New York.

# Dummy Variables for Nominal
# For this type of issue, pandas provides -- by far -- the easiest transformation using pandas.get_dummies.

import numpy as np

numpy_series_1 = np.random.randint(low=0, high=3, size=100)
print(numpy_series_1)
print('**************************************************************')

# numpy.random.rand() in Python
# About :
# numpy.random.rand(d0, d1, …, dn) : creates an array of specified shape and fills it with random values.
# Parameters :
#
# d0, d1, ..., dn : [int, optional]Dimension of the returned array we require,
# If no argument is given a single Python float is returned.

# Return :
# Array of defined shape, filled with random values.
# Code 1 : Randomly constructing 1D array
# 1D Array filled with random values :
numpy_series_2 = np.random.rand(3)
print(numpy_series_2)
print('**************************************************************')

# Code 2 : Randomly constructing 2D array
numpy_series_3 = np.random.rand(3, 4)
print(numpy_series_3)
print('**************************************************************')

# Code 3 : Randomly constructing 3D array
numpy_series_4 = np.random.rand(2, 2, 2)
print(numpy_series_4)
print('**************************************************************')

# More Ptactice
# https://www.geeksforgeeks.org/numpy-random-rand-python/