
# Add list items

## Append Items
### To add an items to the end of the list, use the append() medtho:

thisList = ["apple", "banana", "cherry"];
thisList.append("orange")
print(thisList)

names = ["ankit", "bella", "honey", "mia"]
names.append("anya")
print(names)


## Insert Items
### To insert a list item at a specified index, use the insert() method


numbers= [1,2,3,4,5,6];
numbers.insert(1, 10);
print(numbers)

txt = ["hi", "hello", "arigato"];
txt.insert(2, "konichiwa")
print(txt)

## Add Any iterable
### The extend() method does not have to append lists
### you can add any iterable object (tuples, sets, lists, dictionaries)

### tuple
items = ["Bag", "Laptop", "pen", "headphone"];
thistuple = ("iphone", "ipad");
items.extend(thistuple);
print(items);

### even list
fruits = ["mango", "apple", "banana", "kiwi"];
someFruits = ["orange", "cherry"];
fruits.extend(someFruits);
print(fruits)

### sets
moreList = ["india", "usa", "japan"];
thisSet = {"russia", "korea"}
moreList.append(thisSet)
print(moreList)
