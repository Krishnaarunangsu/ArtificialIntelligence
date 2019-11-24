# numpy.linspace() in Python

# About :
# numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None) : Returns number spaces evenly w.r.t interval. Similar to arange but instead of step it uses sample number.
# Parameters :
# -> start  : [optional] start of interval range. By default start = 0
# -> stop   : end of interval range
# -> restep : If True, return (samples, step). By deflut restep = False
# -> num    : [int, optional] No. of samples to generate
# -> dtype  : type of output array

# Return :
# -> ndarray
# -> step : [float, optional], if restep = True
from typing import Optional, Union, Tuple
import numpy as np
import pandas as pd
from numpy.core._multiarray_umath import ndarray

# restep set to True
y = np.linspace(2.0, 3.0, num=5, retstep=True)
print(y)

# To evaluate sign in long range
x: Union[ndarray, Tuple[ndarray, Optional[float]]] = np.linspace(0, 2, 10)
print(type(x))
print(x)
sin_x = np.sin(x)
print(sin_x)

series_1 = pd.Series(x)
print(series_1)

series_2 = pd.Series(sin_x)
print(series_2)

df_1 = pd.DataFrame({'x': series_1, 'sin(x)': series_2})
print(df_1)