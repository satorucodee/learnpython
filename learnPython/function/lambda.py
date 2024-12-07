# Lambda
# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a: a + 10;
print(x(5))  # 15

total = lambda a, b, c : a + b + c
print(total(1,2,3)) # 6

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2);
print(mydoubler(10)) # 20
