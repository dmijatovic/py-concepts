"""
Multiple inheritance. It can be quite complex and difficult to understand.
It is not used often due to complexity.

NOTE! if more than one class use same methods the first method that is found is used.
It is not overwritten by later classes.
"""


class ClassA:
  def hi(self):
    print("Hello")


class ClassB:
  def hi(self):
    print("Hi")


class ClassC(ClassA, ClassB):
  pass


class ClassD(ClassB, ClassA):
  pass


c = ClassC()
d = ClassD()

c.hi()
d.hi()
