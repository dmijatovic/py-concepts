# set attribute of class dynamically

class Person:
  # just let it work without errors
  pass

p = Person()

first_key="firstName"
first_val="Dusan"

# set new prop on class
setattr(p,first_key,first_val)

# disable pylint http://pylint.pycqa.org/en/latest/user_guide/message-control.html
# pylint: disable=no-member
print("Get attribute 1:", p.firstName)

first = getattr(p,first_key)

print("Get attribute 2:", first)

# Applying is based on dictionary (data)
person_info={'firstName':'Dusan', 'lastName': 'Mijatovic','dataOfBirth':"1970-11-25"}
# loop dictionary
for key,val in person_info.items():
  setattr(p,key,val)

for key in person_info.keys():
  print(f"person.{key}={getattr(p,key)}")