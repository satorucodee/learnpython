
# Try Except
# The try block lets you test a block of code for errors.
# The except blocks lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code regardless of the result of the try and except blocks

# Exception Handling
try:
  print(x)
except:
  print("An exception occurred")


# Many Exceptions

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Else

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# Finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# => Raise an exception
# As a python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# -> You can define what kind of error to raise, and the text to print to the user

y = 'hello'

if not type(y) is int:
    raise TypeError("Only integers are allowed")
