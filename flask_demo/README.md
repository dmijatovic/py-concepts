# Flask webserver

Flask is basic web server in python

## Install

```bash
pip3 install flask
```

## Defining env variables to run flask

You can define env variables for flask app in order to start it just with flask command

```bash
# export filename
export FLASK_APP=app.py
# run in DEBUG mode (with auto reloads)
export FLASK_DEBUG=1
# run flask
flask run
```

Another approach is to have definition at the bottom of the app.py file

```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
  # This debug mode is not executed when in uwsgi mode
  app.run(debug=True)
```

## Routing with flask

The routing is done using decorator on the method.

```python
# 2 routes covered with one method
# / and /home
@app.route("/")
@app.route("/home")
def home():
  return "<h1>Hello world</h1>"

# /about route handled here
@app.route("/about")
def about():
  return "<h1>About page</h1>"

# dynamic routes
@app.route("/dynamic/<int:id>")
def dynamic(id):
  return f"<h1>About page {id}</h1>"


```

## Templates with Jinja2

We can use multiline string for simple staff, like this.

```python
@app.route("/about")
def about():
  return '''
    <h1>This is page header</h1>
    <section>Just a secton example</section>
  '''
```

But more structured approach is to have template files separately. Falsk uses [Jinja2 templating engine](https://jinja.palletsprojects.com/en/2.11.x/templates/). The folder name need to be templates and need to next to app.py(at the sample level).

Example of template implementation and passing data.

```python
# routes data
routes=[
  {'label':'Home', 'path':'/'},
  {'label':'About', 'path':'/about'},
  {'label':'Blogs', 'path':'/blogs'}
]

# passing data to templating engine
@app.route("/home")
def home():
  return render_template("home.html", routes=routes)

```

Using data in html template. For more info see [this page](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures).

```html
<nav class="app-nav">
  <!-- Jinja2 loop and using data -->
  {% for route in routes%}
  <a href="{{route.path}}" class="app-nav-link">{{route.label}}</a>
  {% endfor%}
</nav>
```

### Partial templates (blocks)

Composing template sections is possible with Jinja2. Mental model is demonstrated using layout.html template.

- layout.html: holds the basic page structure including navigation

```html
<section class="page-body">
  <!--
    HERE WE INSERT CONTENT FROM
    SPECIFIC PAGE TEMPLATE
  --->
  {% block content %}{% endblock content %}
</section>
```

- blogs.html: page injects content block into template.

```html
<!-- section from home.html template -->
{% block content %}
<h1>Page content title</h1>
<div>
  This is body of the home page template
</div>
{% endblock content %}
```

## Static content

Static content should be at folder static and need to be loaded. The url_for function from flask need to be pasted into html template.

```python
# import url_for
from flask import Flask, render_template, url_for
```

```html
<!--importing static index.css file -->
<link rel="stylesheet" href="{{url_for('static',filename='index.css')}}" />
```

## Forms input

Commonly used library for form input is [flask-wtf](https://flask-wtf.readthedocs.io/en/stable/quickstart.html). The library can be installed via pip. It has extended validation features.

```bash
# install lib
pip3 install flask-wtf
# install email validator
pip3 install wtforms[email]
pip install email_validator
```

The forms are python classes which are converted to html output. For CSSF security we add secret key to out flask app. The secret key can be generated like this.

```bash
# start interpeter
python3
# import lib
import secrets
# create random string with len=16
secrets.token_hex(16)
# generates this: 01545c0cdd271a8177bea35d4d4b0517
```

```python
app = Flask(__name__)
# set the key
app.config['SECRET_KEY']="01545c0cdd271a8177bea35d4d4b0517"
```

Make env variable to take this value (not to be in the code!!!)

### Form validations with flask-wtf

The forms are defined in forms.py module. We have two classes: RegistrationForm and LoginForm. wtforms module has number of validators from basic to more custom. For custom validation we create an method within form class.

```python
# import validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

# define registraton form
class RegistrationForm(FlaskForm):
  username=StringField("Username",
    validators=[DataRequired(),Length(min=4,max=100)])
  email=StringField("Email",
    validators=[DataRequired(), Email()])
  password=PasswordField("Password",
    validators=[DataRequired(),Length(min=6,max=100)])
  confirm_password=PasswordField("Confirm password",
    validators=[DataRequired(), EqualTo('password')])

  submit=SubmitField("Sign up")

  # custom validation temaplate
  def validate_field(self,field):
    if True:
      raise ValidationError('Validation message')
  # for each validation we need method
  def validate_username(self,email):
    email = User.query.filter_by(email=email.data).first()
    if email:
      raise ValidationError(f'Email {email.data} already used')

```

### File uploads with flask_wtf

To be able to upload files (images) we use file module of flask_wtf.
See forms.py for complete implementation.

```python
# import module to handle image upload
from flask_wtf.file import FileField, FileAllowed

# add this picture field to your form class
class UpdateAccountForm(FlaskForm):
  # ...
  picture = FileField("Update profile picture",
    validators=[FileAllowed(['jpg','png','svg'])])
  # ...
```

Add the upload field to form template (see account.html) and enctype for uploading files (multipart/form-date).

```html
<!-- include enctype multipart for image upload -->
<form method="POST" action="" enctype="multipart/form-data">
  <!-- ... other stuff... -->
  <!-- image upload -->
  <div class="form-group">
    {{form.picture.label()}} {{form.picture(class="form-control-file")}} {% if
    form.picture.errors %} {% for error in form.picture.errors %}
    <span class="text-danger"> {{error}} </span><br />
    {% endfor %} {% endif %}
  </div>
  <!-- ... other stuff... -->
</form>
```

Handle data upload, see routers.py for complete (working) code.

```python

def save_picture(form_picture):
  # ensure random filename
  random_hex = secrets.token_hex(8)
  # split filename into basename and extension
  # _ means we will not use first param
  _,f_ext = os.path.splitext(form_picture.filename)
  # construct filename
  pic_file = random_hex + f_ext
  pic_path = os.path.join(app.root_path,'static/profiles', pic_file)
  # save picture
  form_picture.save(pic_path)

  return pic_file

# if the picture is uploaded
if form.picture.data:
  pic_file = save_picture(form.picture.data)
  current_user.image_file = pic_file

```

### Image file resizing

The avatar images for our profile are set to be 9rem. We should resize larger images before uploading in order to save disk space and speedup upload.

For resizing we use Pillow library.

```bash
# install resizing lib
pip install Pillow
```

See routes.py save_picture method for complete implementation.

```python
# import Pillow lib
from PIL import Image
# set dimension as tupple
pic_dim = (144,144)
# load it to img object
image = Image.open(form_picture)
# resize it
image.thumbnail(pic_dim)
# save resized picture
image.save(pic_path)

```

## Local enviroment and project dependencies

It is good practice for larger projects to use local project environments. Using virtual env you ensure the package versions used in the project are locked (similar to package.lock file). In python there are 3 major ways to do this.

- Standard venv package. This is the latest one and it is baked standard into pyhon. It requires python 3.3 or higher. You do not have to install anythin. NOTE! after creating venv you use `python` and `pip` commands even if you normally use `python3` and `pip3` as default commands on your machine to activate python v3. Standard venv package does not support loading various python versions than the standard ones you have on your machine. If you need virtual environement with specific python version (not your default versions) you need to use package `virtualenv` (see point 2). For detailed walk trough see this [instruction video](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

```bash
# list all
pip3 list
# create virtual environment at the current folder
python3 -m venv .venv
# activate p36env - it will show
source .venv/bin/activate
# validate python version
which python
# list packages in selected env
pip list
# install required packages
pip install flask
# create requirements file
pip freeze
# create requirements file from global env
pip3 freeze --local > requirements.txt
# install requirements
pip install -r requirements.txt
# deactivate virtual environment
decativate
```

Note you might need to install wheel package if you get error during installation of other packages: "Failed building wheel for wrapt".

```bash
# solves Failed building wheel for wrapt error at package install
pip install wheel
```

- virtualenv: older package that was quite popular before venv module is introduced. See this [instruction video](https://www.youtube.com/watch?v=N5vscPTWKOk) for more info.

```bash
# install virtualenv
pip3 install virtualenv
# list all global packages
pip3 list
```

### Create requirements file

On an existing project you can extract libraries used in the project to a requirements.txt file.

```bash
# save dependencies in the requirements file
pip3 freeze --local > requirements.txt
# install dependencies
pip3 install -r requirements.txt
```

## SQL Databases with SQLAlchemy

Common approach is to use SQLLite in development and Postgres in production. These two seem to have same syntax. Only the database urls are different. The package used to connect is [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).

```bash
# install sql alchemy
pip install flask-sqlalchemy

```

### SQL Lite and PostgreSQL

It is light database that amounts to one db file on disk. It used for development and easiest to setup.

We define location of database in our app. We use /// to indicate relative path. In out example we define it to be in the root

```python
# define sqllite database location (uri)
app.config['SQLALCHEMY_DATABASE_URI']="sqllite:///data.db"
```

### SQLAlchemy

This module enables us to represent data as classes. Each python class will represent an table in database. These classes are known as models.

```python
class User(db.Model):
  """
  User model will created user table in database. Note that table name is lowercase while class begins with capital; User(class) = user(table).
  If you want custom table names it can be defined with attributes
  """
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(100),unique=True,nullable=False)
  email = db.Column(db.String(100),unique=True,nullable=False)
  image_file = db.Column(db.String(20), unique=False,nullable=False,default="default.jpg")
  # passwords will be hashed
  password = db.Column(db.String(60),nullable=False)

  # create relationship between User and Post classes in database
  # lazy indicates that need to be loaded as necessary
  posts = db.relationship('Post', backref="author", lazy=True)

  # define how to print object
  def __repr__(self):
    return f"User: {self.username}, {self.email}"
```

After defining model you can create database from python interpreter using bash. Ensure you are in the project directory and using proper virtual enviroment (venv) of the project.

### Create database

```bash
# start python interpreter
python
# import db from your app
from app import db
# create database
db.create_all()
# valdate that database is crated at defined location
# this sqlite file site.db
# delete database
db.drop_all()
```

### Create tables from models

```python
# create tables from models User and Post
from app import User, Post
# create test user 1
user1 = User(username='Dusan', email='a@b.com',password='password')
# add user1 to db
db.session.add(user1)
# create test user 2
user1 = User(username='John', email='a@c.com',password='password')
# add user2 to db
db.session.add(user2)
# commit changes
db.session.commit()
```

### Queries

```python
# get all users
User.query.all()
# get forst
User.query.first()

# filter by username Cory
User.query.filter_by(username='Cory').all()
# take a first match
User.query.filter_by(username='Cory').first()

# ORDER posts by createdAt and return
Post.query.order_by(Post.createdAt.desc()).all()

# load first user into variable
user1 = User.query.first()
print(user1.id)

# get user with specific id
user1 = User.query.get(1)

# getting relational field
user1.posts


```

### Create posts and link it to user

```python
# create fist posts for user 1
post1 = Post(title="Blog 1", content="This is my content", user_id=user1.id)
db.session.add(post1)
post2 = Post(title="Blog 2", content="This is my content 2", user_id=user1.id)
db.session.add(post2)
# commit changes to db
db.session.commit()
```

### Using backref feature from relation created in user model

```python
# get first post
post = Post.query.first()
# get author info thanks to backref argument we defined in User model
post.author
post.author.id
```

### Pagination

SQLAlchemy makes is quite easy to paginate returned data. When using paginate() method the object is returned with number of usefull props (use dir(object) to list them).

```python
# improt db model
from app.model import Post
# return all posts
posts = Post.query.all()
# paginate selection and return complete object
# default amount of rec is 20 per page
postPag = Post.query.paginate()
# take posts from page 2
postPag2 = Post.query.paginate(page=2)
# return 5 posts per page
postPag2 = Post.query.paginate(per_page=5)
```

Loop in html need to be slightly adjusted for pagination in Jinja2 template

```html
{% for post in posts.items %}
<section class="blog-post">
  <!--
    HTML content here
    See blogs.html template file for more details
  -->
</section>
{% endfor %}

<!-- pagination section -->
{% for page_num in posts.iter_pages() %} {% if page_num %}
<a href="{{url_for('blogs',page=page_num)}}" class="btn btn-outline-info mb-4"
  >{{ page_num }}
</a>
{% else %} ... {% endif %} {% endfor %}
```

For excellent video explanation [see this video](https://www.youtube.com/watch?v=PSWf2TjTGNY&list=PLRiZb4DNOVQdTOd1-n2TkU06Dgdzpv4nx&index=10)

## Package structure for your app

Converting module into packages. It is easier. When moving peace of codes you can get circular import. In out example we extracted models into separate files.
When python runs models.py module it runs complete file. As we importing User and Post into app.py file at the top, python reads models.py file and finds import of db from app.py file. At this point python has not went trough complete app.py file. Hence it did not found db variable which is declared later in app.py script. So it trows error that it can import User module. Excellent video on this [is here](https://www.youtube.com/watch?v=44PvX0Yv368).

To create package in python you simple need to create **init** file in the folder with the same name as out main file. In this example

- create app folder and in that folder "**init**.py" file.
- move all project files except app.py into app folder
- rename app.py to run.py
- import app from app module (**init**.py)

```python
# __init__.py file in the folder app needs to have variable app
from app import app
```

### Importing local module into package

```python
# reference to package name
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
```

### Watch for circular module imports

Eventhough we packaged our app it is still possible to create circular imports! Be mindfull when and where are local modules imported into a package. In our example we need to import routes after the app is initialized.

## Encripting passwords

Common practice is NOT to save plain user passwords into database. To encript passwords common package used is bcrypt. There is flask extension.

```bash
# install bcrypt package
pip install flask_bcrypt

#-----------
# usage
#---------------
from flask_bcrypt import Bcrypt

# instantiate class
bc = Bcrypt()
# generate hashed password in bytes
hash = bc.generate_password_hash('password')
# decode to utf-8 string
hash = bc.generate_password_hash('password').decode('utf-8')
# validate hashed password
check = bc.check_password_hash(hash,'password')

```

## Authentication

There are 3 methods to authentication with Flask: sessions, cookies and JWT tokens.

### JWT tokens

This article discusses [JWT approach and its advantages](https://realpython.com/token-based-authentication-with-flask/). There is a repo with [complete code here](https://github.com/realpython/flask-jwt-auth).

In this video authentication is showed using [flask login manager](https://www.youtube.com/watch?v=CSHx6eCkmv0).

### Session manager (flask-login)

Popular session manager module for flask is flask-login module. It is session manager that takes care of authentication and maintins user session. This [video demonstrate use of flask-login](https://www.youtube.com/watch?v=CSHx6eCkmv0)

```bash
# install flask login
pip install flask-login
```

Implementation in **init**.py we import library as define it as middleware.

```python
# import library
from flask_login import LoginManager
# apply it to flask app
login_manager = LoginManager(app)
# define login page for route guards
login_manager.login_view = 'login'
# define message login type (bootstrap class)
login_manager.login_message_category = "info"

```

In the router module we validate if the user is logged in and handle appropriately.

```python
from flask_login import login_user, current_user, logout_user

@app.route("/register",methods=["GET","POST"])
def register():
  # if user authenticated we redirect
  if current_user.is_authenticated:
    return redirect(url_for("home"))

''' PROTECTED ROUTE with login_required decorator '''
@app.route("/account")
@login_required
def account():
  return render_template("account.html",
    title="Account",
    # form=form,
    routes=routes)

```

For protected routes

In the html template we can use same method to show/hide routes

```html
<nav class="nav justify-content-end">
  {% if current_user.is_authenticated %}
  <a href="account" class="nav-link">Account</a>
  <a href="logout" class="nav-link">Logout</a>
  {% else %}
  <a href="login" class="nav-link">Login</a>
  <a href="register" class="nav-link">Register</a>
  {% endif%}
</nav>
```

### Accessing query parameters

To access query params in flask we import request module. Using params we can extract param.

```python
# import request object
from flask import request
# get next param from url
next_page = request.args.get('next')
```

## Debugging Flask using browser

When flask is in development mode detailed information about error will be provided to user. It is even possible to run and debug code from the browser using debuggin PIN!

## Flask app deployment

The deployment is based on [this video](https://www.youtube.com/watch?v=goToXTC96Co) from the same author who created this flask demo.

The video deploys on linux machine (Ubuntu 18.10) in the cloud. I will describe how machine is setup here.

- ssh into a Ubuntu server.
- setup ssh

```bash
# update
sudo apt update
# set hostname to flask-server
hostnamectl set-hostname flask-server
# check hostname
hostname
# save hostname with proper ip in hosts file
nano /etc/hosts
# 192.168.1.12 flask-server
# create new user with privileges
adduser dmijatovic
# create password
# other info is optional
# add user to sudo group
adduser dmijatovic sudo
# logout and log back in as dmijatovic user
# ssh into machine with new user
ssh dmijatovic@192.168.1.12
# setup ssh key based authtication
# more info https://www.youtube.com/watch?v=vpk_1gldOAE
# withing user home create .ssh folder
mkdir .ssh
# on YOUR LOCAL MACHINE
# create and copy your ssh key to server
ssh-keygen -b 4096
# leave on default and empty pass frase
# keys are created id_rsa and id_rsa.pub
# move your public key to server
# secure copy from machine to server to home directory
scp ~/.ssh/id_rsa.pub dmijatovic@192.168.1.7:~/.ssh/authorized_keys
# update permissions on the server for .ssh folder
sudo chmod 700 ~/.ssh
# all files should have different mode (see link for more info)
sudo chmod 600 ~/.ssh/*
# disable root login via ssh in ssh config file on server
sudo nano /etc/ssh/sshd_config
# PermitRootLogin yes -> no
# PasswordAuthentication yes -> no
# save and restart ssh server
sudo systemctl restart sshd
```

- setup firewall

```bash
# install uncomplicated firewall
sudo apt install ufw
# allow outgoing transport
sudo ufw default allow outgoing
# deny incoming traffic
sudo ufw default deny incoming
# set specifi allowance: ssh, http, https
sudo ufw allow ssh
# allow incoming traffic port 5000
sudo ufw allow 5000
# later we will allow http port 80 and https 443
sudo ufw allow http/tcp
# enable firewall
sudo ufw enable
# view status - which port are open/closed
sudo ufw status
```

- deploy Flask app: you can clone, or FTP it. or bash copy it

```bash
# first create dependecies from your venv in the project folder
pip freeze > requirements.txt
# upload you flask project to server:users home folder
scp -r ./flask_demo dmijatovic@192.168.1.7:~/
# confirm app folder is on server
ls -lha # in your homefolder
# install python3-pip
sudo apt install python3-pip
# install virutal environemnt
sudo apt install python3-venv
# create virtual environment in the project flask_demo
python3 -m venv ~/flask_demo/venv
# confirm venv folder is created
# activate venv
source venv/bin/activate
# confirm venv is activated
# install requirements
pip install -r requirements.txt
# set env variables in your project in config file
sudo touch /etc/config.json
# edit file with variables
sudo nano /etc/config.json
# {
#   "SECRET_KEY":"ASDASDASDASDASDdfgeysrtyrty",
#    ... ETC...
# }
```

```python
# adjust you config.py file to load config.json env variables
import json
with open('/etc/config.json') as config_file:
  config = json.load(config_file)

# all env variables are now in config object
SECRET_KEY = config.get('SECRET_KEY')
```

- test application on port 5000

- make application avaliable with nginx and ...

```bash
# install nginx
sudo apt install nginx
# install gunicorn use venv and pip
pip install gunicorn
# update nginx config and instruct it to use gunicorn for python
# remove nginx default config
sudo rm /etc/nginx/sites-enabled/default
# create new config
sudo nano /etc/nginx/sites-enabled/flaskblog
```

Edit nginx config file

```nginx
server{
  listen 80;
  server_name 192.168.1.7;

  #static files
  location /static{
    # location to static folder on the server
    alias /home/dmijatovic/flask_demo/app/static;
  }
  # other traffic to gunicorn (default on port 8000)
  location /{
    proxy_pass http://localhost:8000;
    include /etc/nginx/proxy_params;
    proxy_redirect off;
  }

}
```

Additional setup firewal

```bash
# allow http port 80 and https 443
sudo ufw allow http/tcp

# remove allowed rule of 5000 (it was only for testing)
sudo ufw delete allow 5000

# restart nginx to load new config
sudo systemctl restart nginx

# start gunicorn with 3 workers
# advice on #workers 2 x #cores + 1
# gunicorn -w 3 run:app

# define gunicorn to supervise
sudo apt install supervisor
# setup supervisor - create new config file
sudo nano /etc/supervisor/conf.d/flask_demo.conf
#
```

Content of supervisor config file

```conf
[program:flaskdemo]
directory:/home/dmijatovic/flask_demo
command=/home/dmijatovic/flask_demo/venv/bin/gunicorn -w 3 run:app
user=dmijatovic
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flask_demo/flask_demo.err.log
stdout_logfile=/var/log/flask_demo/flask_demo.out.log
```

- create logfile

```bash
# create dir for logfiles
sudo mkdir -p /var/log/flask_demo
# create log files
sudo touch /var/log/flask_demo/flask_demo.err.log
sudo touch /var/log/flask_demo/flask_demo.out.log
# restart superviser
sudo supervisorctl reload
```

- Nginx max size of files to upload

```bash
# open basic config file of nginx
sudo nano /etc/nginx/nginx.conf

# find the key types_hash_max_size
# below set additional allowance
client_max_body_size 5M;
# save config file

# resart nginx
sudo systemctl restart nginx
```
