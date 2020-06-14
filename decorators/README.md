# Decorator fn in python

Decorator function is used to decorate another function in Python. In order to do so it needs to be curried function (function that returns a function). See example below.

```python
def protect_fn(fn: FunctionType):
  def authorise(user):
    print("user...", user)
    if "admin" in user["roles"]:
      return fn()
    else:
      return f"401 - Not authorized"
  # return child fm
  return authorise


@protect_fn(user)
def get_admin_password() -> str:
  return "123456"

```

## Function name changes

When creating currying function as decorator the python will take over the name and the documentation of decorator (not decorated function). This is not desired. To solve this problem use functools.wraps method to tell python that this function is decorator.

```python
from types import FunctionType
from functools import wraps

user = {"username": "Susan", "roles": ["admin"]}


def protect_fn(fn: FunctionType):
  # use wraps to preserve original function name
  # and the documentation
  @wraps(fn)
  def authorise(user: dict) -> str:
    # print("user...", user)
    if "admin" in user["roles"]:
      return fn()
    else:
      return f"401 - Not authorized"
  # return child fm
  return authorise


@protect_fn
def get_admin_password() -> str:
  return "123456"

```

## Passing arguments to decorated function

To make decorators flexible you use `**args and, **kwargs` approach in order to accept any number of arguments and parameters.

```python

from types import FunctionType
from functools import wraps

user = {"username": "Susan", "roles": ["admin"]}


def protect_fn(fn: FunctionType):
  # use wraps to preserve original function name
  # and the documentation
  @wraps(fn)
  def authorise() -> str:
    # print("user...", user)
    if "admin" in user["roles"]:
      return fn()
    else:
      return f"401 - Not authorized"
  # return child fm
  return authorise


@protect_fn
def get_admin_password() -> str:
  return "123456"

```

## Using arguments in decorated function

This is simply achieved by creating additional top function that takes decorator specific arguments first and THEN RETURNS decorator function, which in turnes calls the original function with its parameters. This is 3 level deep fn (currying).

See protect.py for dem0

```python

from types import FunctionType
from functools import wraps

user = {"username": "Susan", "roles": ["user"]}


def protect_fn(user: dict = None):
  def decorator_fn(fn: FunctionType):
    @wraps(fn)
    def authorise(*args, **kwargs) -> str:
      if user == None:
        return "No user profile provided"
      # print("user...", user)
      if "admin" in user["roles"]:
        return fn(*args, **kwargs)
      else:
        return f"401 - Not authorized"
    return authorise
  return decorator_fn


@protect_fn()
def get_admin_password():
  return "123456"


print(get_admin_password())
print(get_admin_password.__name__)

```
