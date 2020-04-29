# Generators

Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

The key words in generator function are yield and next.

```python

def generator(lst=[]):
  for item in lst:
    yield item

def processFile(fileName):
  print("processing file", fileName)

# calling generator
fileName = generator(['file 1', 'file 2', 'file 3'])

next(fileName)

```
