# Loop through list
### you can loo through the list items by using a for loop
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)


## Loop through the index numbers
### you an also loop through the list items by referring
### to thei index numbers
### use the range() and len() functions to create a suitable iterable
names = ["Kai", "bellla", "ankit", "honey"]
for i in range(len(names)):
    print(names[i])


## Using a while loop
### use the len() function to determine the length of the list,
### then start at 0 and loop your way through the list items by
### referring to their indexes
numbers = [1,2,3,4,8,5,5,9];
i = 0;
while i< len(numbers):
    print(numbers[i])
    i += 1


## Loop using list comprehension
### list comprehension offers the shortest syntax for looping through lists:
statusCodes = [404,500,200,201];
[print(x) for x in statusCodes]
