
# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as prameters, into a function.
# A function can return data as a result.

# Create a function
# In python a function defined using the def keyword:

def myFunction():
    print("Hello from a function")

# To call a function, use the function name followed by parenthesis:
myFunction();

# Arguments
# Information can be passed into function as arguments.
# Aruments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

def my_func(name):
    print("hello" + name)

my_func("Jhon")  # Jhon

# Arguments are often shortened to args in Python documentations

# Parameters or Arguments?
# The terms parameter and arguments can be used for the same thing: information
# that are passed into a function

# NOTE: From a function's perspective:
# HACK: A parameter is the variable listed inside the parentheses in the function definition.
# HACK: An argument is the value that is send to the function when it is called.

# Number of arguments
# By default, a function must be called with the correct numbre of arguments.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add
# a * before the parameter name in the function defination.

# This way the function will recevie a tuple of arguments, and can access the items accordingly:

def thisFunc(*kids):
    print("This youngest child is " + kids[2])

thisFunc("Jhon", "Matt", "Lnius");

# Arbitrary Arguments are often shortened to *args in Python documentations.

# Keyword Arguments

# You can also send arguments with the key = value syntax
# tHIS way the order of the  arguments does not matter.

def my_childs(child3, child1, child2):
    print("The youngest child is " + child2)

my_childs(child1="bash", child3="Shell", child2="Zsh")

# tHE phrase keyword arguments are often shortened to kwargs in Python documentations.

# Arbitrary keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your
# function, add two askterisk: ** before the parameter name in the function definition.

def thisfun(**kid):
    print("His last name is " + kid["lname"])

thisfun(fname = "Jhon", lname="Deo")


# Default Parameter Value
# If we call the function without arguments, it uses the default value:

def func(country = "INDIA"):
    print("I am from " + country)

func("USA")
func()
func("JAPAN")
func("Russia")

# Return Values
# To let a function return a value, use the return statement

def calculator(x):
    return x * 10

print(calculator(4))
print(calculator(10))
print(calculator(5))

# Positional-Only Arguments
# You can specify that a function can have only positional arguments, or Only keyword
# arguments. To specify that a function can have only positional arguments, add ,/ after the arguments:

def that_func(x,/):
    print(x)

# that_func(3, 2);

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def key_func(*, x):
    print(x)

key_func(x = 50);

# Combine Positional-Only and Keyword-Only
# You can combine the two arguments types in the same function.
# Any arguments before the /, are positional-only, and any arguments after the *,
# are keyword-only

def combine_functype(a,b,/,*,c,d):
    print(a+b+c+d)

combine_functype(2, 3, c = 10, d = 100)


# NOTE: Recursion
# Python also accepts function recurison, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function
# call itself. This has the benefit of meaning that you can loop through data to reach a result.

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
        return result

print("Recursion Result")
tri_recursion(6)
