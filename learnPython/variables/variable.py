
# variables are container for storing data values
### a variable is created the moment you first assign value to it.

x = 5
y = "Jhon"
print(x)
print(y)

number = 10
number  = "ten"
print(10)

# cating
### If you want to specify the data type of a variable, this can be done with casting.

a = str("3")
b = int(3);
c = float(3)

print(a)
print(b)
print(c)


# get the type
### you can get the data type of a variable with the type() function.

print(type(a))
print(type(b))
print(type(c))

# single quotes or double quotes
### String variables can be declared either by using single or double quotes

x = "John"
# is the same as
x = 'John'

# case sensitive
### variable name are case-sensitive.

username = 'jhon'
Username = 'doe'

print(username)
print(Username)

# Many Values to Multiple Variables
j,k,l = "ankit", 'bella', 'harvard'
print(j,k,l)

# one value to multiple variables
m = n = o = "orange"
print(m,n,o)

# unpack a collection
list = ["apple", "banana", "cherry"]
apple, banana, cherry = list
print(apple, banana, cherry)


# global variable
magic = "global variable"
def myfunc():
    print("this is " + magic)

myfunc()


def myfuncTwo():
    magic = "local variable"
    print("this is " + magic)

myfuncTwo()


# the global keyword
### To create a global variable inside a function, you can use the global keyword.
def random():
    global thunder
    thunder = "thunder is thunder"

random();
print("this is thunder " + thunder)

### Also, use the global keyword if you want to change a global variable inside a function.

country = "USA"

def changeCountry():
    global country
    country = "India"

changeCountry()
print("this is " + country)


