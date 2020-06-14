
from .blog import Blog


def setup0():
  b = Blog("title", "author")
  return b


def setup2():
  b = Blog("title", "author")
  data = [
      {"title": "title1"},
      {"title": "title2"}
  ]
  for d in data:
    b.posts.append(d)

  return b, data


def test_create_blog():
  b = setup0()
  assert b.title == "title"
  assert b.author == "author"
  assert b.posts == []


def test_repr_0_posts():
  b = setup0()
  exp = "Blog title by author, 0 posts"
  assert b.__repr__() == exp


def test_repr_2_posts():
  b, data = setup2()
  exp = "Blog title by author, 2 posts"
  assert b.__repr__() == exp


def test_json_no_posts():
  b = setup0()
  exp = {'title': 'title', 'author': 'author', 'posts': []}
  assert b.json() == exp


def test_json_2_posts():
  b, data = setup2()
  exp = {'title': 'title', 'author': 'author', 'posts': data}
  assert b.json() == exp
