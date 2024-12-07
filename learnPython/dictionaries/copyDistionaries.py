
# Copy a dictionary

"""
You cannot copy a dictionary simply by typing dict2 = dict1,
because: dict2 will only be a referece to dict1, and change made in
dict1 will automatically also be made in dict2
"""

# there are ways to make a copy, one way is to use the built-in dictinary
# method copy()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


mydict = thisdict.copy()
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# another way to make a copy is to use the built-in function dict()

anotherDict = dict(thisdict)
print(anotherDict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
