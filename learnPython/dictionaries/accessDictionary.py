
# Access Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
    "brand": 'Ford',
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"] # Mustang

# There is also a method called get() that will give you the same result:

y = thisdict.get('model') # Mustang

# Get keys
# The keys() method will return a list of all the keys in the dictionary

z = thisdict.keys()

# Get Values
# The values() method will return a list of all the values in the dictionary

a = thisdict.values()

# Get Items
# the items() method will return each item in a dictionary, as tuples in a list

b = thisdict.items();
print(b)

# check if key exists
# to determine if a specified key is present in a dictionary use the in keyword

if "model" in thisdict:
    print("Yesm 'model' is one of the keys in the thisdict dictionary")

