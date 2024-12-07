
# Remove Dictionary Items
# There are serveral methods to remove items from a dictionary

# the pop() MEHTOD remove the items with the specified key name:

thisdict = {
    "barnd": "Ford",
    "model": "Mustang",
    "year": 2020
}

thisdict.pop("year");
print(thisdict) # {'barnd': 'Ford', 'model': 'Mustang'}


# the popitem() method removes the last inserted item (in version 3.7, a random item is removed instead):

thisdict.popitem();
print(thisdict) # {"brand": "Ford"}


# the del keyword removes the items with the specified key name:

del thisdict["barnd"]
print(thisdict) # {}


# the clear() method empties the dictionary

thisPerson = {
    "name":"Jhon",
    "age": 18
}

thisdict.clear()
print(thisPerson) # {}
