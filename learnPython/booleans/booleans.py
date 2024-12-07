
# python booleans

### Booleans represent one of two values: True or False
### When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)


### When you run a condition in an if statement, Python returns True or False:

a = 200;
b= 20;

if (a < b):
    print("A is less than B")
else:
    print("A is greater than B")


# Evaluate value and varaibles
### the bool() function allow you to evaluate any value, and give you True or False in return

print(bool("Hello"))
print(bool(15))
print(bool(False))


# Some value are false
### except empty values [], {}, (), "", and 0, False, None

bool([])
bool({})
bool(())
bool("")
bool(0)
bool(None)
bool(False)


"""One more value, or object in this case,
evaluates to False, and that is if you
have an object that is made from a class
with a __len__ function that returns 0 or False:"""

class myClass():
    def __len__(self):
        return 0

myobj = myClass()
print(bool(myobj))



# function can return a boolean

def func():
    return True

if func():
    print("Yes")
else:
    print("No")



"""Python also has many built-in functions
that return a boolean value,
like the isinstance() function,
which can be used to determine
if an object is of a certain data type:"""

x = 200
print(isinstance(x, int))
