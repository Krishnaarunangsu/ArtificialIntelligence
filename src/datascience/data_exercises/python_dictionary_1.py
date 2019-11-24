# Creating an empty dictionary
dictionary_1 = dict()
dictionary_2 = {}
print(f'Dictionary-1:{dictionary_1} Type:{type(dictionary_1)}')
print(f'Dictionary-2:{dictionary_2} Type:{type(dictionary_2)}')

# Creating a Dictionary with Integer Keys
dictionary_3 = {1: 'God', 2: 'is', 3: 'Great'}
print(dictionary_3)

# Creating a Dictionary with mixed Keys
dictionary_4 = {'Name': 'God', 1: [1, 2, 3, 4]}
print(dictionary_4)

# Creating a Dictionary with dict() method
dictionary_5 = dict({'Name': 'God', 1: [1, 2, 3, 4]})
print(dictionary_5)

# Creating a Dictionary with each item as pair
dictionary_6 = dict([(1, 'Jagannath'), (2, 'Krishna')])
print(dictionary_6)
