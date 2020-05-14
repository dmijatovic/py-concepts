import os
import secrets

from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required

from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostNewForm
from app.models import User, Post
from app.data import routes


@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", title="Home page - Flask demo", routes=routes)

@app.route("/about")
def about():
  return render_template("about.html", title="About page - Flask demo", routes=routes)

@app.route("/register",methods=["GET","POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for("home"))

  form = RegistrationForm()
  # if form is valid/filled in
  # print("Validate...", form.validate_on_submit())
  if form.validate_on_submit():
    # hash the password
    hashed_pass = bcrypt.generate_password_hash(form.password.data)
    # create user records
    user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
    # # add to db
    db.session.add(user)
    db.session.commit()
    # f string supported in python v3.6 and higher
    flash(f'Account created for {form.username.data}!','success')
    print(f'Account created for {form.username.data}!')
    return redirect(url_for('login'))

  # else return form
  return render_template("register.html",
    title="Register",
    form=form,
    routes=routes)

@app.route("/login",methods=["GET","POST"])
def login():
  # check if user is logged in
  if current_user.is_authenticated:
    return redirect(url_for("home"))
  # get form content
  form = LoginForm()
  # check if content valid
  if form.validate_on_submit():
    # get user by email
    user = User.query.filter_by(email=form.email.data).first()
    # check if user found and password is correct
    if user and bcrypt.check_password_hash(user.password,form.password.data):
      login_user(user, remember = form.remember.data)
      next_page = request.args.get('next')
      if next_page:
        return redirect(next_page)
      else:
        return redirect(url_for('home'))
    else:
      # f string supported in python v3.6 and higher
      flash(f'Failed to loggin! Email or password incorrect','danger')

  return render_template("login.html",
    title="Login",
    form=form,
    routes=routes)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))


def save_picture(form_picture):
  # ensure random filename
  random_hex = secrets.token_hex(8)
  # split filename into basename and extension
  # _ means we will not use first param
  _,f_ext = os.path.splitext(form_picture.filename)
  # construct filename
  pic_file = random_hex + f_ext
  pic_path = os.path.join(app.root_path,'static/profiles', pic_file)
  # resize picture
  pic_dim = (288,288)
  img = Image.open(form_picture)
  img.thumbnail(pic_dim)
  # save resized picture
  img.save(pic_path)
  # save picture
  # form_picture.save(pic_path)

  return pic_file

@app.route("/account", methods=["GET","POST"])
@login_required
def account():
  form = UpdateAccountForm()

  if form.validate_on_submit():
    # if the picture is uploaded
    if form.picture.data:
      pic_file = save_picture(form.picture.data)
      current_user.picture = pic_file
    # update user account info using SQLAlchemy
    current_user.username = form.username.data
    current_user.email = form.email.data
    # commit this update
    db.session.commit()
    # notify
    flash('Your account info is updated','success')
    # redirect to refresh data and start new GET session
    # when we are here we had POST method
    return redirect(url_for('account'))
  elif request.method == 'GET':
    # populate form data
    form.username.data = current_user.username
    form.email.data = current_user.email

  picture = url_for('static', filename='profiles/' + current_user.picture)

  return render_template("account.html",
    title="Account",
    picture=picture,
    form=form,
    routes=routes)

@app.route("/blogs")
@login_required
def blogs():
  # extract query param
  page = request.args.get('page',1,type=int)
  # paginate blogs 5 per data
  posts = Post.query.order_by(Post.createdAt.desc()).paginate(page=page,per_page=2)

  return render_template("blogs.html",
    title="Blogs page - Flask demo",
    posts=posts, routes=routes)

@app.route("/blogs/new",methods=["GET","POST"])
@login_required
def blogs_new():

  form=PostNewForm()

  if form.validate_on_submit():
    # note author as backref
    post = Post(title=form.title.data,
      content=form.content.data,
      author=current_user)
    db.session.add(post)
    db.session.commit()
    flash("Post is created","success")
    return redirect(url_for('blogs'))

  return render_template("blog_new.html",
    title="New post",
    legend_text="Create new post",
    form=form,
    routes=routes)

@app.route("/blogs/<int:id>",methods=["GET"])
@login_required
def blogs_view(id):
  post = Post.query.get_or_404(id)

  return render_template("blog_view.html",
    title=post.title,
    post=post,
    routes=routes
  )

@app.route("/blogs/<int:id>/edit",methods=["GET","POST"])
@login_required
def blogs_edit(id):
  post = Post.query.get_or_404(id)

  if post.author != current_user:
    abort(403)

  form = PostNewForm()

  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash("Your post is updated",'success')
    return redirect(url_for('blogs_view',id=post.id))
  elif request.method=="GET":
    form.title.data = post.title
    form.content.data = post.content

  return render_template("blog_new.html",
    title=post.title,
    legend_text="Edit existing post",
    post=post,
    form=form,
    routes=routes
  )

@app.route("/blogs/<int:id>/delete", methods=["GET"])
@login_required
def blogs_delete(id):
  post = Post.query.get_or_404(id)

  if post.author != current_user:
    abort(403)

  db.session.delete(post)
  db.session.commit()

  flash("Your post is DELETED",'success')

  return redirect(url_for('blogs'))

# @app.route("/blogs/user/<str:username>")
# @login_required
# def blogs_user(username):
#   # get used filter
#   user = User.query.filter_by(username=username).first_or_404
#   # extract query param
#   page = request.args.get('page',1,type=int)
#   # filter for user, order by date and paginate blogs 2 per page
#   posts = Post.query\
#     .filter_by(author=user)\
#     .order_by(Post.createdAt.desc())\
#     .paginate(page=page,per_page=2)

#   return render_template("blogs.html",
#     title="Blogs page - Flask demo",
#     posts=posts, routes=routes)
