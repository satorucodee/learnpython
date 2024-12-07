# Module
# consider a module to be the same as a code library
# a file containing a set of functions you want to include in your application.

# Create a module
# to create a module just save the code you want in a file with the file extension .py

def greeting(name):
    print("Hello, " + name )

# Use a module
# now we can use the module we just created, by using the import statement:

# import mymodule
# mymodule.greeating("Jhon")

# NOTE: When using a function from module, use the syntax: module_name.function_name.


# Variable in module
# The module can contain function, as already described, but also variables of all types
# (arrays, dictionaries, object etc):

person1 = {
    "name": "Jhon",
    "age": 36,
    "country": "Norway"
}

# import the module mymodule, and access the person1 dictionary:
# import mymodule
# a = mymodule.person1["age"]
# print(a)


# Naming a module
# you can name the module file whatever you like, but it must have
# the file extension .py

# Re-naming a Module
# you can create an alias when you import a module, by using the as keyword:
# import mymodule as mx

# Built-in Modules
# There are several built-in modules in python, which you can import whennever you like.

import platform
x = platform.system()
print(x)

# Using the dir() function
# There is a built-in function to list all the function names (or variable names) in a module.
# The dir() function:
x = dir(platform)
print(x)

# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import from module
# you can choose only parts from a module, by using the from keyword.

