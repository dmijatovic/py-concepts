# loop over multiple lists at the same time using ZIP fn

names=["name 1", "name 2","name 3","name 4", "name 5"]
roles=["role 1","role 2","role 3","role 4", "role 5" ]
stars=["star 1","star 2","star 3","star 4", "star 5" ]

for name,role,star in zip(names,roles, stars):
  print(name,role,star)


# The same can be done using dictionary(different data layout)
persons=[
  {"name":"name 1","role":"role 1", "star":"star 1"},
  {"name":"name 2","role":"role 2", "star":"star 2"},
  {"name":"name 3","role":"role 3", "star":"star 3"},
  {"name":"name 4","role":"role 4", "star":"star 4"}
]

for person in persons:
  print(person["name"], person["role"], person["star"])