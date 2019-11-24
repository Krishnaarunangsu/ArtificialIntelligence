# Step 1: Import packages and classes


import numpy as np
from sklearn.linear_model import LinearRegression

# Step 2: Provide data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x)
print(x.shape)

y = y = np.array([5, 20, 14, 32, 22, 38])
print(y)
print(y.shape)

# Step 3: Create a model and fit it
model = LinearRegression()
model.fit(x, y)
# model = LinearRegression().fit(x, y)

# Step 4: Get results
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('slope:', model.coef_)