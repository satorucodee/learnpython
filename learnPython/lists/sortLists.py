# Sort Lists

## Sort List Alphanumerically
### List objects hava a sort() method that will
### sort the list alphanumerically, ascending, by default

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"];
thislist.sort();
print(thislist)

thisList = [100,1000, 80,50,70, 30,20,40,]
thisList.sort()
print(thisList)


## Sort Descending
### To sort descending, use the keyword argument reverse = True:

thatList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thatList.sort(reverse=True)
print(thatList)

thatlist = [10,20,30,50,40,60,90,80,70,100]
thatlist.sort(reverse=True)
print(thatlist)


## Customize sort function
""" You can also costomize your own function by using the keyword
argument key = function.

The function will return a number that will be used to sort the list
(the lowest number first)"""


def myFunc(n):
    return abs(n-50)  # sort the list based on how the number is to 50

numlist = [100,50,65,82,23]
numlist.sort(key=myFunc)
print(numlist)

## Case Insensitive Sort
### by defalt the sort() method is case sensitive, resulting in all capital letters being
### sorted before lower case letters.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

### perform a case-insensitive sort of the list

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


## reverse Order
### what if you want to reverse the order of a list, regardless of the alphabet?
### the reverse() method reverses the current sorting order of the elements

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
