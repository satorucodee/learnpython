
# Modify Strings
### pyhton has a set of built-in methods that you can use on string

# upper case
### the upper() method returns the string in upper case:
a = "hello"
print(a.upper());


# Lower case
### the lower() method returns the string in lower case
b = "world"
print(b.lower());


# remove whitespace
### whitespace is the space before and after the actual text,
### and very often you want to remove this space
### the strip() method removes any whitespace from the begining or the end:

c = "   hello   "
print(c.strip())

# replace string
### the replace() method replaces a string with another string

txt = "Hello, world";
print(txt.replace("H", "A"))


# split string
### the split() method splits the string into substrings if it finds instances of the separator:
txt = "apple, banana, cherry"
print(txt.split(","))

