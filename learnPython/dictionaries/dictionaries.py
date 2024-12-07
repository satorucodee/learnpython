
# Python Dictionaries

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is orderd*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(thisdict["brand"]) # Ford

# Duplicate values will overwrite existing values:

thatdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thatdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# To determin how many items a dictionary has, use the len() function:

print(len(thatdict)) # 3

# The values in dictionary items can be of any data type:

thisPerson = {
    "name": "Jhon",
    "age": 18,
    "isProgrammer": True,
    "device": ["Macbook Pro m4", "iphone 16",]
}



# It is also possible to use the dict() constructor to make a dictionary

theDict = dict(name = 'Jhon', age=36, country= 'USA')
