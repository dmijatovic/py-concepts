from person import Person
from movie import Movie

def main():
  Nika = Person("Nikita", "2004-02-24","director")
  Tamara = Person("Tamara", "2001-02-12", "actor")

  m1 = Movie("Tarzan","actie")
  m2 = Movie("Just do it","actie")
  m3 = Movie("Another day","actie")

  Nika.movies.append(m1)
  Tamara.movies.append(m2)
  Nika.movies.append(m3)

  # print(Nika)
  print(Nika.telMeAboutYou())
  print(Tamara.telMeAboutYou())

main()