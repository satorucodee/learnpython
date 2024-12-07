
# Python Tuples

mytuples = ("apple", "banana", "cherry");

# Tuples are used to store multiple items in single variable.
# a tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets ()

thistuple = ("apple", "banana", "cherry");
print(thistuple)


# Tuple items are ordered, unchangeable, and allow duplicate values.

# Create Tuple with one item
# you have to add a comma after the item, otherwise Python will
# not recognize it as a tuple.

thattuple = ("apple",)
print(type(thattuple)) # <class 'tuple'>

# HACK: #not a tuple
atuple = ("apple")
print(type(atuple)) # <class 'str'>

# Tuple items can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,2,3,4,5,6)
tuple3 = ("apple", 1,2,3,"string", True, False)

# From Python's perspective, tuples are defined as objects with data
# type 'tuple';

# It is also possible to use the tuple() constructor to make a tuple.

nameTuple = tuple(("ankit", "bella", "jhon"))

# Change Tuple values
# Once a tuple is created, you cannot change its values. Tuples are
# unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change
# the list, and convert the list back into a tuple.

# convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x);
y[1] = 'kiwi'
x = tuple(y)
print(x) # ('apple', 'kiwi', 'cherry')

# same as the add tuple but different

a = ("apple", "banana", "cherry")
b = list(a)
b.append("orange")
a = tuple(b)
print(a) # ('apple', 'banana', 'cherry', 'orange')

# or merge two tuples
j = ("apple", "banana", "cherry")
k = ("orange",)
j += k;
print(j) # ('apple', 'banana', 'cherry', 'orange')

# same apply on remove items
m = ("apple", "banana", "cherry")
n = list(m)
n.remove("apple");
m = tuple(n)
print(m) # ('apple', 'kiwi', 'cherry')


# or you can delete the tuple completely
c = ("apple", "banana", "cherry")
del c
# print (c) this will raise an error because thetuple no
# longer exits

# unpacking a tuple
# when we create a tuple, we normally assign value to it. This is
# called "packing" a tuple:
# but, in python, we are also allowed to extract the value back into
# variables. This is called "unpacking"

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits;
print(green, yellow, red) # apple banana cherry

# NOTE:
# The number of variable must match the number of value in the
# tuple, if not, you must use an asterisk to collect the remaining values as a list.

skills = ("JavaScript", "Python", "Java", 'Node.js')
(Js, Python, *skillsPack) = skills
print(Js) # JavaScript
print(Python) # Python
print(skillsPack) # ['Java', 'Node.js']

# multiply tuples
# if you want to multiply the content of a tuple a given number of times,
# you can use the * operator:

languages = ("english", "hindi", "japanese")
mytuple = languages * 2;
print(mytuple) # ('english', 'hindi', 'japanese', 'english', 'hindi', 'japanese')

# Tuple Methods
# python has two built-in methods that you can use on tuples

# count -> returns the number of times a specified value occurs in a tuple
# index() -> search the tuple for a specifed value and returns the position of
# where it was found

isTuple = ("apple", "banana","appple", "cherry", "apple")
hasApple = isTuple.count("apple")
print(hasApple) # 3

appleIndex = isTuple.index("apple");
print(appleIndex) # 0
