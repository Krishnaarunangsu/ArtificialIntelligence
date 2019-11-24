# Enumerate a List.
# You can iterate over the index and value of an item in a list by using a basic for loop

L = ['apples', 'bananas', 'oranges']
for idx, val in enumerate(L):
    print("index is %d and value is %s" % (idx, val))

print('****************************************************')
# Enumerate a Tuple
# Enumerating a tuple isn’t at all different from enumerating a list.

t = ('apples', 'bananas', 'oranges')
for idx, val in enumerate(t):
    print("index is %d and value is %s" % (idx, val))

print('************************************************************')
# Enumerate a List of Tuples (The Neat Way)
# Say you have a list of tuples where each tuple is a name-age pair.

L = [('Matt', 20), ('Karim', 30), ('Maya', 40)]
# Of course one way to enumerate the list is like this:

for idx, val in enumerate(L):
    name = val[0]
    age = val[1]
    print("index is %d, name is %s, and age is %d"
          % (idx, name, age))


print('************************************************************')
# Enumerate a string
str_1 = "Python"
for idx, ch in enumerate(str_1):
    print("index is %d and character is %s"
          % (idx, ch))


#  https://www.afternerd.com/blog/python-enumerate/