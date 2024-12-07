
# Add Dictionary Items

# Adding Items
# Adding an items to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] =  'red'
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# update Dictionary
# The update() mehtod will update the dictionary with the items from given argument.
# If the item does not exist, the item will be added.

thisdict.update({"country": "USA"})
