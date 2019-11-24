# Python List Comprehension and Slicing
# List comprehension is an elegant way to define and create list in python. We can create lists just like mathematical statements and in one line only. The syntax of list comprehension is easier to grasp.
#
# A list comprehension generally consist of these parts :
#    Output expression,
#    input sequence,
#    a variable representing member of input sequence and
#    an optional predicate part.
#
# For example :
#
# lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
#
# here, x ** 2 is output expression,
#       range (1, 11)  is input sequence,
#       x is variable and
#       if x % 2 == 1 is predicate part.
# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)
print('********************************************************')

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(odd_square)
print('********************************************************')

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print(power_of_2)
print('********************************************************')

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
print(noprimes)

# Let’s understand how to use range() function with the help of a simple example.
print('\n********************************************************')
print("Python range() example to print numbers from range 0 to 6")
for i in range(6):
    print(i, end=', ')

print('\n********************************************************')
for i in range(2, 8):
    for j in range(i*2, 50, i):

        print(j)
        print('\n********************************************************')

# https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/