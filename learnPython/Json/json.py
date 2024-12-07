
# JSON
# json is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation

import json


# => Parse JSON - convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# => Convert from python to JSON
# if you have python object, you can convert it into a JSON string by using the
# json.dumps() methods.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# NOTE: You can convert Python objects of the following types, into JSON strings:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# -> convert a python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


# => Format the Result
# -> use the indent parameter to define the numbers of indents:
print(json.dumps(x, indent=4))

# -> use the separators parameter to change the default sperator
# default value is (", ", ": "), which means using a comma and a space to
# separate each object, and a colon and a space to separate keys from values:
print(json.dumps(x, indent=4, separators=(".", " = ")))

# -> Order the Result
# the json.dumps() method has parameters to order the keys in the result:
print(json.dumps(x, indent=4, sort_keys=True))
