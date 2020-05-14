from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

# User authentication with flask-login
# this method need to be implemented
# with specific decorator. And you pass
# UserMixin into your User class
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


#-------------------------------
# Table definitions
#-------------------------------
class User(db.Model, UserMixin):
  """
  User model will created user table in database. Note that table name is lowercase while class begins with capital; User(class) = user(table).
  If you want custom table names it can be defined with attributes
  """
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(100),unique=True,nullable=False)
  email = db.Column(db.String(100),unique=True,nullable=False)
  picture = db.Column(db.String(20), unique=False,nullable=False,default="default.jpg")
  # passwords will be hashed
  password = db.Column(db.String(60),nullable=False)

  # create relationship between User and Post classes in database
  # lazy indicates that need to be loaded as necessary
  posts = db.relationship('Post', backref="author", lazy=True)

  # define how to print object
  def __repr__(self):
    return f"User: {self.username}, {self.email}"

class Post(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(254), nullable=False)
  createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)

  # create link to userid
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

  # define how to print object
  def __repr__(self):
    return f"Post: {self.title}, {self.createdAt}"
