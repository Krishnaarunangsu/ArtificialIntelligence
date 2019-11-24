import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DF = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv")
print(DF)
y = list(DF.columns)
print(y)
x = [column for column in y]
print(x)

numpy_array_float_1 = np.array(['1', '2', '3']).astype(np.float)
print(numpy_array_float_1)
print(numpy_array_float_1.tolist())
# y = np.array(y).astype(np.int)
# plt.boxplot(y)
# plt.show()
