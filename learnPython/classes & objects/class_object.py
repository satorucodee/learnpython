
# Python Classes/Objects
# python in an object oriented programming langauge.
# Almost everthing in Python is an object, with its propertiess and methods.

## Class
# A class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5

## Create Object
# Now we can use the class named MyClass to create Objects:

p1 = MyClass()
print(p1.x) # 5

# The __init__() function
# All classes have a function called __init__(), which is always executed when the class
# is being initiated
# Use the __init__() function to assign values to object properties, or other operation that are necessary to do when the
# object is being created:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jhon", 36)

print(p1.name) # Jhon
print(p1.age) # 36

# NOTE: The self parameter is a reference to the current instance of the class, and is used
#       to access variable that belong to the class.
# NOTE: the __init__() function is called automatically every time the class is being
#       used to created a new object.


# The __str__() function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returend:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Jhon", 36)

print(p1)


# Object Methods
# Object can also contain methods. Methods in object are function that belong to
# the object

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def myfunc(self):
        print("Hello my name is " + self.name)

p2 = User("Jhon", "Jhon@gmail.com")
p2.myfunc()


# Self parameter
# The self parameter is a reference to the current instance of the class, and is used to access
# variables that belong to the class.

# It does not have to be names self, you can call it whetever you like, but it has to be
# the first paramerter of any function in the class.


class Example:
    def __init__(anything, name, age):
        anything.name = name
        anything.age = age

    def myfunc(abc):
        print('Hello my name is ' + abc.name)

b1 = Example("Jhon", 36)
b1.myfunc()

# You can modify properties on object like this
b1.age = 40

# you can delete properties on objects by using the del keyword:
del b1.age

# you can delete objects by using the del keyword:
del b1

