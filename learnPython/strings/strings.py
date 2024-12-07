
# python string
### strings in python are surrounded by either single or double quotation marks.
### 'hello' is the same as "hello"

print("hello")
print('hello')

# quotes inside quotes
### you can use quotes inside a string.
### as long as they don't match the quotes surrounding the string

print("It's alright")
print("He is called Jhonny'")
print('He is called "johnny"')

# assign string to a variable
a = "hello"
print(a)

# multiline string
### you can assign a multiline string to a variable by using three quotes.

text = """This is multiline string.
this is first line string.
this is third line string... and so on"""

# NOTE: in the result, the line breaks are inserted at the same position as in the code.

# string are arrray
### strings in Python are arrays of bytes representing unicode characters.
### Square brackets can be used to access elements of the string.

movie = 'Avengers'
print(movie[0])

# lopping through a string
### Since strings are arrays, we can loop through the characters in a strin

for x in "yourself":
    print(x);

# string length
### To get the length of a string, use the len() function.

quote = "Do it";
print(len(quote))

# check string
### To check if a certain phrase or character is present in a string, we can use the keyword in.

text = "Hello, this is me"
print('Hello' in text)

# use if

if "Hello" in text:
    print("Hello is present")

# check if not
### we can use the keyword not in.

anotherTxt = "This is homeside"
print('Hello' not in anotherTxt)


