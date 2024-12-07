
# Copy Lists
### You cannot copy a list simply by typing list2 = list1, because: list2
### will only be a reference to list1, and changed made in list1 will
### automatically also be made in list2


## Use the copy() method
### You can use the built-in list method copy() to copy a list

thislist = ["apple", "banana", 'cherry']
mylist = thislist.copy()
print(mylist)

list1 = ["Bag", "Pen", "Paper", "Laptop"]
list2 = list1.copy();
print(list2);


## Use the list() method
### Another way to make a copy is to use the built-in method list()

fruits = ["apple", "banana", "cherry", "coco"]
someFruits = list(fruits)
print(fruits);

names = ["Ankit", "Bella", "Anya", "Harverd"]
someNames = list(names)
print(someNames);


## Use the slice operator
### You can also make a copy of a list by using the : (slice) operator.

langauges = ["Python", "JavaScript", "Rust", "Dart"]
skills = langauges[:];
print(skills)
