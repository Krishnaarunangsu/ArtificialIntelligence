import numpy as np

numpy_array_1 = np.array(['a', 'b', 'c', 'd', 'e'], ndmin=2)
print(numpy_array_1)
print(numpy_array_1.dtype)

numpy_array_2 = np.array([['a', 'b'], ['c', 'd', 'e']])
print(numpy_array_2)
print(numpy_array_2.dtype)

numpy_array_3 = np.array(['a', 'b', 'c', 'd', 'e'], ndmin=1)
print(numpy_array_3)
print(numpy_array_3.dtype)

numpy_array_4 = np.array([1, 2, 7, 9, 8], dtype=complex)
print(numpy_array_4)
print(numpy_array_4.dtype)
