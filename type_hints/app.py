
from typing import List

# type hinting params and returns


def sum(first: float, second: float) -> float:
  return first + second


def sumList(data: List) -> int:
  tot = 0
  for x in data:
    tot += x
  return tot


print(sum(3, 7))
print(sumList([1, 2, 3, 4, 5]))


class Book:
  pass


class BookShelf:
  def __init__(self, book: Book):
    self.books = []
    self.books.append(book)

  def getBook(self, pos: int) -> Book:
    return self.books[pos]

  def __repr__(self) -> str:
    return f"Bookshelf with {len(self.books)} books"

