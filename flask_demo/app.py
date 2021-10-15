from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# Set the key for form protection of CSSF
app.config['SECRET_KEY']="01545c0cdd271a8177bea35d4d4b0517"

posts=[{
  'author':'Mister twister',
  'title':'Blog post 1',
  'content':'This is my first blogpost.',
  'createdAt':'2020-05-11 16:24:33'
  },{
  'author':'Mister twister 2',
  'title':'Blog post 2',
  'content':'This is my 2 blogpost.',
  'createdAt':'2020-05-11 16:25:33'
  }
]

routes=[
  {'label':'Home', 'path':'/'},
  {'label':'About', 'path':'/about'},
  {'label':'Blogs', 'path':'/blogs'}
]

# url_for('static', filename='index.css')

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title="Home page - Flask demo", routes=routes)

@app.route("/about")
def about():
  return render_template("about.html", title="About page - Flask demo", routes=routes)

@app.route("/blogs")
def blogs():
  return render_template("blogs.html",
    title="Blogs page - Flask demk",
    posts=posts, routes=routes)

@app.route("/register")
def blogs():
  form = RegistrationForm()
  return render_template("register.html",
    title="Register",
    form=form,
    routes=routes)



if __name__ == '__main__':
  # This debug mode is not executed when in uwsgi mode
  app.run(debug=True)