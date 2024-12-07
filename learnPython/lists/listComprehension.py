# List Comprehension
"""
List comprehension offers a shorter syntax when you want to create a new list
based on the value of an existing list.

HACK:
Based on a list of fruits, you want list, contaning only the fruit with
the letter "a" in the name.

without list comprehension you will have to write a for statement with condition
"""


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x);

print(newlist)


### with lis comprehension you can do all that with only one of code.

thelist = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in thelist if "a" in x]
print(newList)

## syntax
### newlist = [expression for item in iterable if condition == True]


## condition
### the condition is like a filter that only accept the items that valuate to True
### the condition is optional and can be omitted

newlist = [x for x in fruits if x != "apple"]


## iterable
### the iterable can be any iterable object, like a list, tuple, set, etc
newlist = [x for x in range(10)] # you can use the range() function to create an iterbale

## expression
### the expression is the current items in the iteration,
### but it is also the outcome, which you can manipulate
### before it ends up like a list item in the new list:

newlist = [x.upper() for x in fruits]

## you can set the outcome to whetever you like

### set all values in the new list to "hello"
codes = [200, 300, 400, 500]
newList = ["hello" for x in codes]
print(newList)

## the expression can also contain conditions,
## not like a filter, but as a way to manipulate
## the outcome

newlist = [x if x != "banana" else "orange" for x in fruits]
