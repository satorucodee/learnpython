
# While Loops
# with the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1

# NOTE: remember to increment i, or else the loop will continue forever

# The break Statement
# with the break statement we can stop the loop even if the while condition is true:

i =1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement
# with the continue statement we can stop the current iteration, and continue with the next:

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
