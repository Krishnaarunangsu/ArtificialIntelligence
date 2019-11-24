# list_variable = [x for x in iterable]

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]

Q = [x ** 3 for x in range(10)]

print(Q)

# Initialize the kilometer list
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct 'feet' with 'map()
feet = map(lambda x: float(3280.8399) * x, kilometer)

# Print `feet` as a list
print(list(feet))