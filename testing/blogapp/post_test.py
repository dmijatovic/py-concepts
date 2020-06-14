from .post import Post


def setup():
  data = {'title': 'title', 'content': 'content'}
  p = Post(**data)
  return p, data


def test_create_post():
  p, data = setup()
  assert p.title == "title"
  assert p.content == "content"


def test_json():
  p, data = setup()
  assert p.json() == data
