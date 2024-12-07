
mylist = ["apple", "banana", "cherry"]

# lists are use to store multiple items in a single variable.
# lists are created usign square brackets

thisList = ['book', 'pen', 'pencil']
print(thisList)

### list items are ordered, changeable, and allow duplicate values.

## ordered
### it means that the items have a defined order, and that order will not change.
### if you add new items to a list, the new items will be placed at the end of the list

## changeable
### the list is changeable, meaning that we can change, add, remove items in a list
### after it has been created

## allow duplicates
### since lists are indexed, lists can have items with same value

items = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print[items]

## list length
### to determine how many items a list has, use the len() function
print(len(items))

## list items - data types
### list items can be of any data type

list1 = ["appple", 1,"ankit", 'pen', True]
list2  = [1,2,3,4,5,6]
list3  = [True, False, False]

## type()
### from python's perspective, list are defined as objects with the data type 'list'

print(type(items)) # <class 'list'>

## the list() constructor
### it is also possible to use the list() constructor when creating a new list

thatlist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thatlist)


"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

*List is a collection which is ordered and changeable. Allows duplicate members.
*Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
*Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
*Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""


# Access list items
### list items are indexed and you can access them by referring to the index number:

thisNum = [1,2,3,4,55];
print(2) # 3

#NOTE: this first item has index 0

## Negative index
### negative index means start from the end

thisFruits = ["apple", 'banana', 'cherry']
print(thisFruits(-1)) # cherry

## range of indexes
### range of indexes by specifying where to start and where to end the range

print(thisFruits[1:2])


## check if item Exists
### to determin if a specified items is present in a list use the in keyword


thisNames = ["bella", 'honey', "lana", "jhon"]
if "jhon" in thisNames:
    print("Jhon in this list")


# change list items
### to change the value of a specific item, refer to the index number

theList = ["apple", "banana", "cherry"]
theList[1] = 'blackcurrant'
print(theList)

## change a range of item values
### If you insert more items than you replace,
### the new items will be inserted where you specified,
### and the remaining items will move accordingly:
theList[1:2] = ["orange", "blackcurrant"]
print(theList)


## insert items
### to insert a new list item, without replacing any of the existing value,
### we can use the insert() method

theList.insert(2, "mango");
print(theList)
