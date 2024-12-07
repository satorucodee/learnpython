# Join Lists

## Join Two Lists
### There are serveral ways to join, or concatenate, two or
### more lists in python.

### One of the easiest ways are by using the + operator.

list1 = [1,2,3,4]
list2 = [5,6,7,8]

list3 = list1+list2;
print(list3)


### Another way to join two lists is by appending all the items form list2 into list1, one by one:

thislist = ["a", 'b', 'c', 'd', 'e'];
latters = ["f", 'g', 'h', 'i', 'j', 'k']

for x in latters:
    thislist.append(x);

print(thislist)


### or you can use the extend() method, where the purpose is to add elments from one list to another list:

numbers = [1,2,3,4,5];
moreNumbers = [6,7,8,9];

moreNumbers.extend(numbers);
moreNumbers.sort()
print(moreNumbers)
