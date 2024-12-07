# Python - remove list items

## remove specified item
### the remove() method removes the specified items

thisList = ["apple","banana", "cherry"];
thisList.remove("banana");
print(thisList)

### if there are more than one items with the specified
### value, the remove() method removes the first occurrence

thislist = ["apple", "banana", "cherry", "kiwi","cherry"]
thislist.remove("cherry")
print(thislist)


## remove specified index
### the pop() method removes the specified index

names = ["bella", "ankit", "kai"];
names.pop(2);
print(names)

someNames = ["Jhon", "Albert", "Shai"]
someNames.pop(1);
print(someNames)

### if you do not specify the index, the pop()
### method removes the last item

codes = [91, 1, 3, 12];
codes.pop();
print(codes) # [91,1,3]


## the del keyword also remove the specified index
thatList = ["apple", "banana", "cherry"]
del thatList[2];
print(thatList); # ["apple", "banana"]


## the del keyword can also delete the list completely
skills = ["Python", "JavaScript", "Dart"];
del skills;
# print(skills) # Error


## Clear the list
### the clear() method empties the list
### the list still remains, but it has no content

icons = ["⚡", "🍺", "🥶", "⛄"];
icons.clear();
print(icons)
