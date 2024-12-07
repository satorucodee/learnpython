

# python numbers
### there are three numeric types in python

x = 1 # int
y = 2.5 # float
z = 3j # complex

print(type(x)) # int
print(type(y)) # float
print(type(z)) # complex

# int
### Int, or Interger, is a whole number, positive or negative, without decimals, of unlimited length.
a = 1;
b = 123456679976547898765432345432;
c = -2345345

print(type(a)) # int
print(type(b)) # int
print(type(c)) # int

# float
### Float, or Floating point number, is a number, positive or negative, containing one or more decimals.
d = 1.0;
e = 10.1;
f = -3.4;

print(type(d)) # float
print(type(e)) # float
print(type(f)) # float


# complex
### Complex numbers are written with a "j" as the imaginary part.
j = 3+5j
k = 2j
l = -2j

print(type(j)) # complex
print(type(k)) # complex
print(type(l)) # complex

# type conversion
### You can convert from one type to another with the int(), float() and complex() methods.

interger_num = 10;
float_num = 10.5;
complex_num = 3+5j;

# convert int to float
q = float(interger_num); # 10.0

# convert float to int
r = int(float_num) # 10

# convert int to complex
s = complex(interger_num); # (10+0j

# NOTE: you can not covert complex to int
