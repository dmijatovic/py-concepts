"""
Python does not have SWITCH statement as in some other lanauages.
Instead we define object/dictionary and use index as key.
"""
def get_planet_name(id):
  # This doesn't work; Fix it!
  name=""
  switch={
      1: "Mercury",
      2: "Venus",
      3: "Earth",
      4: "Mars",
      5: "Jupiter",
      6: "Saturn",
      7: "Uranus",
      8: "Neptune"
  }
  return switch[id]

print(get_planet_name(3))