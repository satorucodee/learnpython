
# Python sets
# sets are used to store multiple items in a single variable

thisset = {"apple", "banana", "cherry"}
print(thisset) # {'cherry', 'banana', 'apple'}

# NOTE: Sets are unordered, so you cannot to sure in which order the
#       items will appear

# Set items are unordered, unchangeable, and do not allow
# duplicate values.

# Duplicates not allowed
# Sets cannot have two items with the same value

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {"apple", "banana", "cherry"}

# NOTE: The value True and 1 are considered the same values in
#       sets, and are treated as duplicates:

thatset = {"apple", "banana", "cherry", True, 1,2}
print(thatset) # {True, 2,  "apple", "cherry", 'banana'}

# NOTE: The Values False and 0 are considered the same in sets, and are
#       treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) # {False, True, "apple", "banana", "cherry"}

# Get the length of a set
# to determine how many items a set has, use the len() function
a = {"apple", "banana", "cherry"}
print(len(a)) # {"apple", "banana", "cherry"}

# set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1,2,3,4,5,6,7}
set3 = {1,2,3, True, "apple", False, 4, True}

# The set() constructor
# It is also possible to use the set() constructor to make a set.

x = set({"apple", "banana", "cherry"})
print(x) # {"apple", "banana", "cherry"}

