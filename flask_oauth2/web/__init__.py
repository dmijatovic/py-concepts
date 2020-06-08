from flask import Flask

app = Flask(__name__)

# Set the key for form protection of CSSF
app.config['SECRET_KEY']="01545c0cdd271a8177bea35d4d4b0517"
app.config['JWT_ALGO']='HS512'

from web import routes
