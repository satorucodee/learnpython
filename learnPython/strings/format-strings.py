
# String format

# age = 36;
# txt = "My name is John, I am" + age
# print(txt)

### but we can combine strings and numbers by using f-strings or the format() method!

# F-strings
"""F-string was introduced in python 3.6,
and is now the preferred way of formating strings

to specify a string as an f-string,
simply put an f in front of the string literral,
and add curly bracketes {} as placeholders for
variables and other operations"""

age = 36
txt = f"My name is Jhon, I am {age}"
print(txt);


# placeholders and modifires
### a palceholder can contain variables,
### operations, functions, and modifiers to
### to format the value

price = 60
txt = f"Ths price is {price} dollars"
print(txt)


### a placeholder can include a modifier to format the value.
### a modifier is include by adding a colon : follwed by
### a legal formating type, like .2f which means fixed point
### number with 2 decimals:

number = 100
txt = f"My number is {number:.2f}"
print(txt)


# a placeholder can contain python code, like math operations:
txt= f"This price is {20*30} dollars"
print(txt)

