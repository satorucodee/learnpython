
# Slicing Strings

### you can return a range of characters by using the slice syntax
### the slice syntax is: string[start:stop:step]

name = 'Bella'
print(name[0:3])


# Slice from start
### By leaving out the start index, the range will start at the first character:

a = 'Hello, world'
print(a[:5])

# Slice to the end
### By leaving out the end index, the range will go to the end:

b= 'hello, world'
print(b[0:])


# Negative indexing
### Use negative indexes to start the slice from the end of the string:

c = 'Hello, world!'
print(c[-5:-2])

