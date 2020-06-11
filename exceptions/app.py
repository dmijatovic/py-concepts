"""
Custom error classes help you granulate errors in more detail and to 
fit better your app.
"""


class myCustomError(ValueError):
  pass


class pageNotFoundError(LookupError):
  pass


class IncorrectPasswordError(ValueError):
  pass


# number = input("Enter a number")

# try:
#   print = (str(int(number)*2))
# except ValueError:
#   print("Invalid number! Try again")

# -----------------
# AttributeError
class NoPropClass():
  pass


try:
  c = NoPropClass()
  c.noProp()
except AttributeError:
  print("No prop method missing!")


# -----------------
# ImportError

try:
  import myAwesomeLib
except ImportError:
  print("This lib does not exists")


# -----------------
# KeyError

my_dict = {'key_i_have': "Value"}

try:
  x = my_dict['key_idont_have']
except KeyError:
  print("This key does not exists")


# -----------------
# TypeError

try:
  x = int([])
except TypeError:
  print("Variable of incorrect type")

# -----------------
# IOError

try:
  open('file_not_existatnt.yxy', 'r')
except IOError:
  print("Something went wrong with the file")


# -----------------
# RuntimeError
# general error

try:
  e = asdasd()
except NameError:
  print("Function or method missing")
