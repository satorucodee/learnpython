
# If...Else

# An 'if statement' is written by usnig the if keyword.

a = 22;
b = 200;
if b > a:
    print("B is greater than a")

# Indentation
# python relies on indentation (whitespace at the begining of a line) to define
# scope in the code. Other programing languages ofter use curly-brackets for this purpose.

# Elif
# The elif keyword is Python's way of saying 'if the previous conditions were not true,
# then try this condition"

a  = 33;
b = 33;
if b > a:
    print("b is grater than a")
elif a == b:
    print("a and b are equal")

# Else
# the else keyword catches anything which isn't caught by the preceding conditions.

a= 200;
b= 33;
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is grater than b")


# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

if a > b: print("a is greater than b")

# Short Hand If...Else
# If you have only one statement to execute, one for if, and one for else,
# you can put it all on the same line:

a = 2
b = 330
print("A") if a < b else print("B")

# you can also have multiple else statement on the same line

a = 300;
b = 330;
print("A") if a > b else print("=") if a==b else print("B")

# AND
# the and keyword is logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b and c < a:
    print("Both conditions are True")

# OR
# the or keywoed is a logical operator, and is used to combine conditional statements:

a = 200
b = 20
c = 500
if a > b or a < c:
    print("At least one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the
# conditional statement:

a = 33
b = 200
if not a>b:
    print("a is not greater than b")

# Nested If

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content.
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

