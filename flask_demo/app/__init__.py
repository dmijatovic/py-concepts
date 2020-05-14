from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

"""
Initialize this package
"""
app = Flask(__name__)
# Set the key for form protection of CSSF
app.config['SECRET_KEY']="01545c0cdd271a8177bea35d4d4b0517"
# define sqllite database location (uri)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# define login page for route guards
login_manager.login_view = 'login'
# define message login type (bootstrap class)
login_manager.login_message_category = "info"

"""
Import routes after app initalization to avoid circular references
"""
from app import routes
