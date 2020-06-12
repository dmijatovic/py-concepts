# Classes

The classes can be seen as containers (modules) that hold related properties and methods. Classes are main paradigm of object oriented programming. Beside encapsulization the classes are used in the realm of inheritance.

## Builtin methods

There are class built in methods for comparation expressing if something is greater or less. These methods are shown in the example below: **gt** returns true/false for `greater than`.

```python

class Curency:
  def __init__(self,amount,conversion_rate):
    self.amount = amount
    self.conversion_rate = conversion_rate
  def __gt__(self,other):
    return self.to_usd() > other.to_usd()
  def __ge__(self,other):
  def __lt__(self,other):
  def __le__(self,other):
  def __eq__(self,other):

pound=Curency(1000)
euro=Curency(1000)

euro > pound

```
