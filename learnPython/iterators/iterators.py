# Iterators
# an iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse
# through all the values.
# Technically, in python, an iterator is object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

# iterator vs iterable
# lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers
# which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Event strings are iterable objects, and can return an iterator

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Create an iterator
# To create an object/class as an iterator you have to implement the methods
# __iter__() and __next__() to your object.

# the __iter__() method acts similar, you can do operations (initializing etc), but
# must always return the iterator object itself.

# the __next__() method also allow you to do operations, and must returns the next item
# in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
# The example above would continie forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from goint on forever, we can use the StopIteration statement.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


