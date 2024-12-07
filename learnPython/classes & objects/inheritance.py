
# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties
# from another class.

# Create a parent class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("Jhon", "Deo")
x.printname()


# Create a child class
class Student(Person):
    pass

# NOTE: uSE the pass keyword when you do not want to add any other properties or methods to the class.

# Now the student class has the same properties and methods as the Person class.

x = Student("Mike", "Olsen")
x.printname() # Mike, Olsen

# We want to add the __inti__() function to the child class (instead of the pass keyword).

class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.
        self.fname = fname
        self.lname = lname

# NOTE: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the
# parent's __init__() function

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Use the super() function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
    def __int__(self, fname, lname):
        super().__int__(fname, lname)

# By using the super() function, you do not have to use the name of the parent
# element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
