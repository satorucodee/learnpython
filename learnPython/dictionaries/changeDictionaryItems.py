
# Change Dictionary Items

# change values
# you can change the value of a specifc items by referring to its key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964

}

thisdict["year"] = 2018

# update dictionary
# the update() method will update the dictionary with the items from the given argument

thisdict.update({"year": 2020})
