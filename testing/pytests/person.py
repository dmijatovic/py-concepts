from random import randint

def greet(person):
  return f"Hello {person['name']}"


def attack_damage(weight):
  damage = randint(1,100)
  return weight * damage

print(attack_damage(3))