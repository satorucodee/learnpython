
# List Methods

thelist = [1,2,3,4,5,6,7,8,9,10, 10];

thelist.append(11); # adds an element at the end of the list
print(thelist);

# thelist.clear() # removes all the elements from the list
print(thelist)

copylist = thelist.copy() # returns a copy of the list
print(copylist)

thisCount = thelist.count(10) # return number of occurrences of value
print(thisCount)

thelist.extend([12,13,14,15]) # add the elements of a list(or any iterable), to the end of the current list
print(thelist)

theIndex= thelist.index(5) # Returns the index of the first element with the specified value
print(theIndex)

thelist.insert(16,16) # Adds an element at the specified position
print(thelist)

removeditem = thelist.pop() # removes the elements at the specified position or end of the list without index
print(removeditem);

thelist.remove(1) # removes the items with the specified value
print(thelist);

thelist.reverse() # reverse the order of the list
print(thelist);

thelist.sort() # sorts the list
print(thelist)
