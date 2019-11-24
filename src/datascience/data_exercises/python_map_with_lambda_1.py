# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]

numbers_sum = map(lambda x, y: x + y, numbers_1, numbers_2)
print(list(numbers_sum))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# https://www.geeksforgeeks.org/python-map-function/