import jwt
from datetime import datetime, timedelta
from flask import jsonify, request, make_response
from web import app
from functools import wraps

ALGO = app.config['JWT_ALGO']
KEY = app.config['SECRET_KEY']

def protected_route(fn):
  @wraps(fn)
  def decorated(*args,**kwargs):
    token = request.args.get('token')

    if not token:
      return jsonify({'message':'Token is missing'}), 401
    try:
      data = jwt.decode(token, KEY, algorithms=[ALGO])
    except:
      return jsonify({'message':'Token is NOT VALID!'}), 403

    return fn(*args,**kwargs)

  return decorated


@app.route("/")
def home():
  return """
    <h1>Hello JWT world!</h1>
    <p>
      To create token go to <a href="/login">login</a> page.
      Login with password = password. You will het JWT back.
      Then go with JWT as query string to /protected page.
      Url should look someting like this:
      <div>
      http://localhost:5000/protected?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZHVzYW4iLCJleHAiOjE1ODk4MDYxMzl9.AEUy3lO0WpjDsgZA3Pu9yIvYjR4aAJ-_CLg0Te3kt28
      </div>
    </p>
  """

@app.route("/login")
def login():
  # basic authentication form
  auth = request.authorization
  # if correct
  if auth and auth.password == 'password':
    expTime = datetime.utcnow() + timedelta(seconds=30)
    # encode jwt (payload as {} and secret)
    token = jwt.encode({'user': auth.username,'exp': expTime}, KEY, algorithm=ALGO)
    # token is in byte format and need to be decoded
    decoded = token.decode('UTF-8')
    # print("Token...", decoded)
    return {'token': decoded}, 200
  # if not correct return standard login form
  return make_response("Could not verify", 401,\
    {"WWW-authenticate":"Basic realm = 'Login required'"})

@app.route("/protected")
@protected_route
def protected():
  return "This is protected route"
