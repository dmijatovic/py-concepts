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
