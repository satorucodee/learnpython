# Scope
# A variable is only available from inside the region it is created.
# This is called scope.

# Local Scope
# A varaible create inside a function belongs to the local scope of that function,
# and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

myfunc()

# Function inside function
# the local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
# A variable create in the main body of the python code is a global variable and belongs
# to the global scope.

# Global variables are available from within any scope, global and local.


y = 200

def myfunction():
    print(y)

myfunction()
print(y)


# Naming variables
# If you operate with the same variable name inside and outside of a function, python
# will treat them as two separate variables, one available in the global scope and one
# one available in the local scope.

name = "Jhon"

def thisfunc():
    name = "Bella"
    print(name)

thisfunc()
print(name)


# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use
# the global keyword.

def thatFunc():
    global a
    a = 500

thatFunc()
print(a)

# NOTE: Also, use the global keyword if you want to make a change to a global variable
#       inside a function



# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested function
# the nonlocal keyword makes the variable belongs to the outer function.

def giveName():
    x = 'Jane'
    def myfunc2():
        nonlocal x
        x = 'hello'
    myfunc2()
    return x

print(giveName())
