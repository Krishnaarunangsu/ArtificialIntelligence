fruits = ['Apple', 'Banana']

# 1.append(): add to the end of the list
# We can add an element to the end of the list or at any given index.
# There are ways to add elements from an iterable to the list.
# We can also use + operator to concatenate multiple lists to create a new list.
print(f'Current fruit list:{fruits}')

fruit_to_be_inserted = input(f'Please enter a fruit name:\n')
fruits.append(fruit_to_be_inserted)
print(f'Updated fruit list:{fruits}')

# 2.insert(). add element at the given index of a list
# This function is useful to add element at the specified index of the list.
num_list = [1, 2, 3, 4, 5]
print(f'Current number list:{num_list}')
number_to_be_inserted = int(input(f'Please enter a number to be inserted:\n'))
index_for_the_new_number \
    = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add rhe number:\n'))
# Put the validation & the business exception
num_list.insert(index_for_the_new_number, number_to_be_inserted)
print(f'New number list:{num_list}')

# 3. extend(): append iterable elements to the list
# extending the iterable elements
# This function is useful to append elements from an iterable to the end of the list.
num_iter: list = []
num_iter.extend([1, 2])  # extending the list elements
print(num_iter)
num_iter.extend((3, 4))  # extending the tuple elements
print(num_iter)
num_iter.extend('ABC')  # extending string elements
print(num_iter)

# List Concatenation: concatenate multiple lists using + operator If you have to concatenate multiple lists,
# you can use the “+” operator. This will create a new list and Mthe original lists will remain unchanged.
evens: list =[2, 4, 6, 8]
odds: list =[1, 3, 5, 7, 9]
num_system: list = odds+evens
print(f'Number System with odd & even:{num_system}')
