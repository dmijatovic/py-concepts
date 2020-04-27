
class Movie:
  def __init__(self, name, genre):
    self.name = name
    self.genre = genre
    self.directors=[]
    self.actors=[]
    self.duration=[]

  def __repr__(self):
    return "Movie {}".format(self.name)