
# Built-in data types
### Variables can store data of different types, and different types can do different things.

# geting the data type
### you can get data type using type() function

x = 5
print(type(x))

# setting the data type
### In python, the data type is set when you assign a value to variable

x = "hi" # strinx = 10 # int
x = ["apple", "banana", "cherry"] # lix = 3.14 # float
x = range(5) # range
x = {"name": "ankit",  "age": 18} # dict
x  = True # boolean
x = None # None
x = 1j # complex
x = ("India", "USA", "Japan") # tuple
e = {1, 2, 3} # set
x = frozenset({1, 2, 3}) # frozenset
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview


# setting the specific data type - HACK: manually

x = str("Hello World")	#str
x = int(20)	# int
x = float(20.5)	# float
x = complex(1j)	# complex
x = list(("apple", "banana", "cherry"))	# list
x = tuple(("apple", "banana", "cherry"))	# tuple
x = range(6)	# range
x = dict(name="John", age=36)	# dict
x = set(("apple", "banana", "cherry"))	# set
x = frozenset(("apple", "banana", "cherry"))	# frozenset
x = bool(5)	# bool
x = bytes(5)	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview
