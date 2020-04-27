
class Person:

  def __init__(self, name, dateOfBirth, ocupation):
    self.name = name
    self.dateOfBirth = dateOfBirth
    self.ocupation = ocupation
    self.eyeColor=None
    self.height=None
    self.movies=[]

  def __repr__(self):
    return "class User, instance {}".format(self.name)

  def telMeAboutYou(self):
    return f'Hi, my name is {self.name}. I am an {self.ocupation}! I am in {len(self.movies)} movies!'
