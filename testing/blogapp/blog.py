
class Blog:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.posts = []

  def __repr__(self):
    return f"Blog {self.title} by {self.author}, {len(self.posts)} posts"

  def json(self):
    return {
        'title': self.title,
        'author': self.author,
        'posts': self.posts
    }
