import numpy as np

a = np.array(
    [
        [[1, 2, 3], [2, 2, 3]],
        [[2, 4, 5], [1, 3, 6]],
        [[1, 2, 4], [2, 3, 4]],
        [[1, 2, 4], [1, 2, 6]]
    ]
)

print(a.shape)

x = np.array([[[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]],
              [[9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],
              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]]])

print(x.shape)

# #axis = 0
for j in range(0, x.shape[1]):
    for k in range(0, x.shape[2]):
        print("element = ", (j, k), " ", [x[i, j, k] for i in range(0, x.shape[0])])

print(x.sum(axis=0))

# axis = 1
for i in range(0, x.shape[0]):
    for k in range(0, x.shape[2]):
        print("element = ", (i, k), " ", [x[i, j, k] for j in range(0, x.shape[1])])

# for sum, axis is the first keyword, so we may omit it,
print('**********************')
print(x.sum(0))
print('**********************')
print(x.sum(1))
print('**********************')
print(x.sum(2))
